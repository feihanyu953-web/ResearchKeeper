"""
SI table numeric consistency validator — cross-references extracted JSON records
against parsed SI tables to catch value/condition mismatches before kb write.

This fills the gap between "LLM transcribes numbers from SI tables" and "rsk sync
writes them to kb" — catching errors where the LLM pairs values with wrong column
headers (e.g., dGad assigned to neutral instead of acidic).

IMPORTANT LIMITATIONS (read before interpreting results):
- This is a HEURISTIC tool, not a general-purpose SI validator.
- The table parser relies on pdftotext-style vertical format with hardcoded
  column-condition mapping (Bmim/Emim × Acid/Neutral/Alkaline). It will NOT
  work for papers with different IL cations or condition schemes.
- Numeric matching uses ±0.02 eV tolerance and CAN produce false matches
  for non-dGad values (Bader charges, limiting potentials, etc.).
- The --strict flag enables additional gating (module/subject keywords) to
  reduce false matches but may also miss real mismatches.
- When no SI tables are parsed, the tool reports status=no_tables (exit 1)
  rather than falsely claiming validation passed.
- Always review mismatch output manually — the tool is a screening aid,
  not a substitute for human verification of LLM-extracted data.

Usage:
  python scripts/validate_si_consistency.py \
    --parsed-si tmp/IQTR8DGX.md \
    --extracted-dir tmp/extracted/
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

# Force UTF-8 on Windows to avoid GBK encoding errors
if sys.platform == "win32":
    for _stream in (sys.stdout, sys.stderr):
        if hasattr(_stream, "reconfigure"):
            try:
                _stream.reconfigure(encoding="utf-8", errors="replace")
            except Exception:
                pass

# ── Species name normalization ────────────────────────────────

_SPECIES_ALIASES = {
    "co2": "*CO2", "cooh": "*COOH", "co": "*CO",
    "coco": "*COCO", "cocoh": "*COCOH", "cohco": "*COHCOH",
    "cco": "*CCO", "ccoh": "*CC(OH)NH2", "cc(oh)nh2": "*CC(OH)NH2",
    "chconh2": "*CHCONH2", "ch2conh2": "*CH2CONH2", "ch3conh2": "*CH3CONH2",
    "no3": "*NO3", "no3h": "*NO3H", "no2": "*NO2", "no": "*NO",
    "noh": "*NOH", "n": "*N", "nh": "*NH", "nh2": "*NH2", "nh3": "*NH3",
    "hno": "*HNO", "hnoh": "*HNOH", "h2noh": "*H2NOH",
    "cono": "*CONO", "conoh": "*CONOH", "con": "*CON",
    "ncono": "*NCONO", "nconoh": "*NCONOH", "ncon": "*NCON",
    "hncon": "*HNCON", "hnconh": "*HNCONH",
    "nh2conh2": "*NH2CONH2",
    "cho": "*CHO", "coh": "*COH", "h": "*H",
    "sur": "*Sur",
}

SI_COLUMN_ORDER = [
    ("Bmim Acid", 2),
    ("Bmim Neutral", 2),
    ("Bmim Alkaline", 2),
    ("Emim Acid", 2),
    ("Emim Neutral", 2),
    ("Emim Alkaline", 2),
]

# Keywords in subject/metric/note that suggest a record is plausibly
# about adsorption free energies (used under --strict to filter out
# records that happen to have similar numeric values, e.g. Bader charges).
# This check uses ONLY keyword matching against record fields — no
# hardcoded module names, so it works across all schema templates
# (generic-science, electrocatalysis, custom).
_DGAD_SUBJECT_KEYWORDS = [
    "dGad", "ΔGad", "Gad", "adsorption energy", "吸附能",
    "adsorption free energy", "ΔG_ad", "dG_ad", "binding energy",
    "Gtot", "free energy", "自由能",
]


def _normalize_species(name: str) -> str:
    cleaned = name.strip().replace(" ", "").replace("_", "").lower()
    if cleaned.startswith("*"):
        cleaned = cleaned[1:]
    if cleaned in _SPECIES_ALIASES:
        return _SPECIES_ALIASES[cleaned]
    return "*" + name.strip().lstrip("*")


# ── SI table parsing ──────────────────────────────────────────

def _parse_si_tables(md_text: str) -> dict[str, dict[str, list[dict[str, Any]]]]:
    """Parse SI markdown tables from vertical (pdftotext-style) format.

    Each species name is followed by N numeric values (one per line).
    N = 6 conditions x 2 fields (Gtot, dGad) = 12 values per species.
    """
    lines = md_text.split("\n")
    tables: dict[str, dict[str, list[dict]]] = defaultdict(lambda: defaultdict(list))

    in_supplementary = False
    parsing_table = None

    for i, line in enumerate(lines):
        stripped = line.strip()
        if not stripped:
            continue

        if "## Supplementary Information" in line or "SI File:" in line:
            in_supplementary = True
            continue
        if not in_supplementary:
            continue

        # Detect table section
        if re.search(r'Table\s+S2', stripped, re.IGNORECASE) and 'acetamide' in stripped.lower():
            parsing_table = "Table S2"
            continue
        elif re.search(r'Table\s+S3', stripped, re.IGNORECASE):
            parsing_table = "Table S3"
            continue
        elif re.search(r'Table\s+S4', stripped, re.IGNORECASE):
            parsing_table = "Table S4"
            continue

        # End of table
        if parsing_table and (re.search(r'Table\s+S\d', stripped, re.IGNORECASE)
                              or stripped.startswith('Refs')
                              or stripped.startswith('Reference')):
            parsing_table = None
            continue

        if not parsing_table:
            continue

        # Skip headers
        if re.match(r'^(System|Energy|Gtot|dGa|Gad|Surfaces?)$', stripped, re.IGNORECASE):
            continue
        if re.match(r'^[BE]mim\s+(Acid|Neutral|Alkaline)$', stripped, re.IGNORECASE):
            continue

        # Species name detection
        try:
            float(stripped.strip("*"))
            is_species = False
        except ValueError:
            is_species = re.match(r'^\*?[A-Z][\w().*+-]+', stripped) is not None

        if is_species:
            species = _normalize_species(stripped)
            numeric_buffer = []
            expected_count = sum(count for _, count in SI_COLUMN_ORDER)

            for j in range(i + 1, min(i + 1 + expected_count + 10, len(lines))):
                ahead = lines[j].strip()
                if not ahead:
                    continue
                if re.match(r'^\*?[A-Z][\w().*+-]+', ahead):
                    try:
                        float(ahead.strip("*"))
                    except ValueError:
                        break
                nums = re.findall(r'[-+]?\d+\.\d+', ahead)
                if len(nums) == 1:
                    numeric_buffer.append(float(nums[0]))
                if len(numeric_buffer) >= expected_count:
                    break

            idx = 0
            for condition, count in SI_COLUMN_ORDER:
                if idx + count <= len(numeric_buffer):
                    entry = {"species": species}
                    if count >= 1:
                        entry["Gtot"] = numeric_buffer[idx]
                    if count >= 2:
                        entry["dGad"] = numeric_buffer[idx + 1]
                    tables[parsing_table][condition].append(entry)
                    idx += count

    return dict(tables)


def _build_lookup(tables: dict) -> dict[str, dict[str, float | str]]:
    """Build (species, condition) -> {dGad, Gtot, table} lookup."""
    lookup: dict[str, dict[str, float | str]] = defaultdict(dict)
    for table_name, conditions in tables.items():
        for condition, rows in conditions.items():
            for row in rows:
                key = "%s::%s" % (row["species"], condition)
                if "dGad" in row:
                    lookup[key]["dGad"] = row["dGad"]
                if "Gtot" in row:
                    lookup[key]["Gtot"] = row["Gtot"]
                lookup[key]["table"] = table_name
    return dict(lookup)


# ── Record extraction ─────────────────────────────────────────

def _extract_records(json_path: Path) -> list[dict]:
    """Extract all records from JSON, scanning value+condition+note for numerics.

    Handles three input shapes:
      - list of record dicts (direct sub-agent output)
      - dict with "schema_candidates": {module: [records]} (envelope format)
      - dict containing record-dict fields (single record)
    """
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    records: list[dict] = []
    if isinstance(data, list):
        records = data
    elif isinstance(data, dict):
        sc = data.get("schema_candidates")
        if isinstance(sc, dict):
            for mod, recs in sc.items():
                if isinstance(recs, list):
                    for r in recs:
                        if isinstance(r, dict):
                            r = dict(r)
                            r["module"] = mod
                            records.append(r)
        else:
            # Single record dict — wrap as one-element list
            if any(k in data for k in ("paper_id", "module", "subject", "metric", "value")):
                records = [data]

    out = []
    for r in records:
        if not isinstance(r, dict):
            continue
        all_text = " ".join([
            str(r.get("value", "")),
            str(r.get("condition", "")),
            str(r.get("note", "")),
        ])
        numbers = re.findall(r"[-+]?\d+\.\d+", all_text)
        if numbers:
            out.append({
                "module": str(r.get("module", "")),
                "subject": str(r.get("subject", "")),
                "metric": str(r.get("metric", "")),
                "value": str(r.get("value", "")),
                "condition": str(r.get("condition", "")),
                "note": str(r.get("note", "")),
                "numbers": [float(n) for n in numbers],
                "source": str(r.get("source", "")),
            })
    return out


# ── Validation ────────────────────────────────────────────────

def _detect_claim(condition_text: str, subject_text: str) -> tuple[str | None, str | None]:
    """Parse condition text to detect claimed (cation, pH)."""
    text = (condition_text + " " + subject_text).lower()
    cation = None
    if "bmim" in text:
        cation = "Bmim"
    elif "emim" in text:
        cation = "Emim"

    ph = None
    if "acid" in text or "h3o" in text or "酸性" in condition_text:
        ph = "Acid"
    elif "alkaline" in text or "碱性" in condition_text:
        ph = "Alkaline"
    elif "neutral" in text or "中性" in condition_text:
        ph = "Neutral"

    return cation, ph


def _is_dgad_context(rec: dict) -> bool:
    """Heuristic: is this record plausibly about dGad adsorption energies?

    Filters out Bader charges, limiting potentials, kinetic barriers, etc.
    that happen to have numeric values near dGad magnitudes.
    """
    # Only use subject + metric for exclusion checks — note fields often
    # contain cross-references to Bader/Hirshfeld/etc. that are not the
    # primary content of the record.
    subject_metric = (
        str(rec.get("subject", "")) + " "
        + str(rec.get("metric", ""))
    ).lower()

    # Use all three fields for positive dGad detection
    combined = subject_metric + " " + str(rec.get("note", "")).lower()

    # Explicitly exclude known non-dGad quantities (subject + metric only)
    _NON_DGAD_PATTERNS = [
        "bader", "limiting potential", "限制电位", "u_l",
        "barrier", "势垒", "kinetic barrier",
        "band gap", "bandgap", "带隙",
        "d band", "d-band", "dband center",
        "work function", "功函",
        "formation energy", "形成能",
    ]
    for pat in _NON_DGAD_PATTERNS:
        if pat in subject_metric:
            return False

    # Positive indicators of dGad context (all fields)
    for kw in _DGAD_SUBJECT_KEYWORDS:
        if kw.lower() in combined:
            return True
    return False


def validate(parsed_si: Path, extracted: Path, *, strict: bool = False) -> tuple[list[dict], list[dict]]:
    """Main validation. Returns (mismatches, warnings)."""
    si_text = parsed_si.read_text(encoding="utf-8")
    tables = _parse_si_tables(si_text)
    gt = _build_lookup(tables)
    records = _extract_records(extracted)

    mismatches: list[dict] = []
    warnings: list[dict] = []

    if not gt:
        warnings.append({
            "type": "no_tables",
            "message": (
                "No SI tables parsed from text. The validator relies on "
                "pdftotext-style vertical table format with Bmim/Emim × "
                "Acid/Neutral/Alkaline structure. Papers with different IL "
                "cations or table layouts cannot be validated."
            ),
        })
        return mismatches, warnings

    for rec in records:
        # Under --strict, skip records unlikely to be dGad-related
        if strict:
            if not _is_dgad_context(rec):
                continue

        cation, ph = _detect_claim(rec["condition"], rec["subject"])
        if not cation or not ph:
            continue

        claimed = "%s %s" % (cation, ph)

        for num in rec["numbers"]:
            if abs(num) > 500:
                continue

            for gt_key, gt_data in gt.items():
                gt_dgad = gt_data.get("dGad")
                if gt_dgad is None:
                    continue
                if abs(num - gt_dgad) >= 0.02:
                    continue

                gt_species, actual_cond = gt_key.split("::", 1)

                if actual_cond.lower() == claimed.lower():
                    break  # Match correct — no issue

                # Mismatch detected — but check ambiguity first
                claimed_key = "%s::%s" % (gt_species, claimed)
                claimed_dgad = gt.get(claimed_key, {}).get("dGad")
                if claimed_dgad is not None and abs(num - claimed_dgad) < 0.02:
                    break  # Value exists in both conditions

                mismatches.append({
                    "module": rec["module"],
                    "subject": rec["subject"],
                    "value": rec["value"],
                    "numeric_value": num,
                    "species": gt_species,
                    "claimed_condition": claimed,
                    "actual_condition": actual_cond,
                    "record_condition": rec["condition"],
                    "record_source": rec["source"],
                    "fix": (
                        "Change condition from '%s' to '%s', or use the correct "
                        "value for '%s' which is dGad=%s eV" % (
                            claimed, actual_cond, claimed,
                            "%.2f" % claimed_dgad if claimed_dgad else "N/A"
                        )
                    ),
                })
                break

    return mismatches, warnings


# ── CLI ───────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="SI table numeric consistency validator (heuristic — review output manually)"
    )
    parser.add_argument("--parsed-si", required=True,
                        help="Path to parsed SI markdown file")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--extracted", help="Single extracted JSON file")
    group.add_argument("--extracted-dir", help="Directory of JSON files (batch)")
    parser.add_argument("--json", action="store_true", dest="json_output",
                        help="Output machine-readable JSON")
    parser.add_argument("--strict", action="store_true",
                        help="Enable dGad-context gating to reduce false matches "
                             "(skips records lacking dGad-related context)")
    args = parser.parse_args()

    parsed_si = Path(args.parsed_si)
    if not parsed_si.is_file():
        print("Error: parsed SI file not found: " + str(args.parsed_si), file=sys.stderr)
        sys.exit(1)

    json_files = []
    if args.extracted:
        json_files = [Path(args.extracted)]
    else:
        json_files = sorted(Path(args.extracted_dir).glob("*.json"))

    if not json_files:
        print("Error: no JSON files found", file=sys.stderr)
        sys.exit(1)

    all_mismatches = []
    all_warnings = []

    for jf in json_files:
        mismatches, warnings = validate(parsed_si, jf, strict=args.strict)
        all_mismatches.extend(mismatches)
        all_warnings.extend(warnings)

    # Determine status: no_tables means we couldn't validate at all
    has_no_tables = any(w["type"] == "no_tables" for w in all_warnings)
    if has_no_tables:
        status = "no_tables"
    elif all_mismatches:
        status = "fail"
    else:
        status = "pass"

    result = {
        "status": status,
        "files_checked": len(json_files),
        "mismatch_count": len(all_mismatches),
        "mismatches": all_mismatches,
        "warning_count": len(all_warnings),
        "warnings": all_warnings,
    }

    if args.json_output:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        if all_mismatches:
            print("\n*** %d VALUE-CONDITION MISMATCH(ES) FOUND ***\n" % len(all_mismatches))
            for m in all_mismatches:
                print("  [%s] %s" % (m["module"], m["subject"]))
                print("    Value: %.4f (dGad)" % m["numeric_value"])
                print("    Claimed: %s" % m["claimed_condition"])
                print("    Actual:  %s (per SI tables)" % m["actual_condition"])
                print("    Species: %s" % m["species"])
                print("    -> %s" % m["fix"])
                print()
        elif has_no_tables:
            print("\nNo SI tables could be parsed — validation was not performed.")
            print("This validator requires pdftotext-style vertical table format")
            print("with Bmim/Emim × Acid/Neutral/Alkaline column structure.")
        else:
            print("\nAll numeric values consistent with SI tables (%d file(s) checked)" % len(json_files))

        if all_warnings:
            print("\n%d warning(s):" % len(all_warnings))
            for w in all_warnings:
                print("  [%s] %s" % (w["type"], w["message"]))

    # Exit codes: 2=real mismatches, 1=no_tables (could not validate), 0=pass
    if all_mismatches:
        sys.exit(2)
    elif has_no_tables:
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
