"""
Batch write kb module records — append schema_v1 records to kb/*.md from JSON intermediate results.

Usage:
  python -m rsk.kb.writer --input tmp/extracted_Hengan2026.json
  python -m rsk.kb.writer --input-dir tmp/extracted/        # batch process all JSON in directory
  python -m rsk.kb.writer --input-dir tmp/extracted/ --dry-run  # preview only, no write

Input JSON format (sub-agent output):
  [
    {
      "paper_id": "Hengan2026",
      "module": "synthesis",
      "schema_version": "schema_v1",
      "category": "...",
      "subject": "...",
      "metric": "...",
      "value": "...",
      "unit": "...",
      "condition": "...",
      "source": "[Author Year, Journal, Fig. X]",
      "confidence": "single_source",
      "note": "..."
    },
    ...
  ]

record_id is auto-assigned (globally incremental per module). record_id fields in input are ignored.
"""

import argparse
from collections import defaultdict
from dataclasses import dataclass
import json
import os
from pathlib import Path
import re
import sys
import tempfile
from typing import Mapping

import yaml

from rsk.config import PROJECT_ROOT

# Force UTF-8 stdout/stderr on Windows (non-GBK characters like subscripts crash print)
for _stream in (sys.stdout, sys.stderr):
    if hasattr(_stream, "reconfigure") and (_stream.encoding or "").lower() not in ("utf-8", "utf8"):
        try:
            _stream.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass

REQUIRED_FIELDS = [
    "paper_id", "module", "schema_version", "category", "subject",
    "metric", "value", "unit", "condition", "source", "confidence", "note"
]

# -- helpers --------------------------------------------------------

def _get_current_max_ids(kb_dir, module_map):
    """Scan kb module files, return {module: max_id_number}"""
    max_ids = {}
    for mod, file_name in module_map.items():
        fpath = kb_dir / file_name
        if not fpath.exists():
            max_ids[mod] = 0
            continue
        max_n = 0
        with open(fpath, "r", encoding="utf-8") as f:
            for line in f:
                m = re.match(rf"\|\s*{mod}-(\d+)\s*\|", line)
                if m:
                    n = int(m.group(1))
                    if n > max_n:
                        max_n = n
        max_ids[mod] = max_n
    return max_ids


def _validate_record(rec: dict, idx: int, modules) -> list[str]:
    """Return list of errors, empty list = pass"""
    errors = []
    for field in REQUIRED_FIELDS:
        if field not in rec or rec[field] is None:
            errors.append(f"record[{idx}]: missing required field '{field}'")
    if rec.get("module") not in modules:
        errors.append(f"record[{idx}]: unknown module '{rec.get('module')}'")
    if not rec.get("source", "").strip():
        errors.append(f"record[{idx}]: empty source field")
    else:
        from rsk.kb.bibliography import (
            BIBLIOGRAPHY_CATEGORY,
            BIBLIOGRAPHY_METRIC,
        )
        from rsk.kb.source import validate_source_for_write

        bibliography = (
            rec.get("category") == BIBLIOGRAPHY_CATEGORY
            and rec.get("metric") == BIBLIOGRAPHY_METRIC
        )
        errors.extend(
            f"record[{idx}]: {error}"
            for error in validate_source_for_write(
                rec.get("source"),
                paper_id=str(rec.get("paper_id", "")),
                bibliography=bibliography,
            )
        )
    return errors


PLACEHOLDER_PATTERNS = [
    "原条目未载明", "需回原文核对", "原条目未拆分",
    "unknown", "N/A", "TBD", "待核对",
]

PERCENTAGE_METRICS = {
    "FE", "Faradaic efficiency", "法拉第效率", "FE%", "faradaic efficiency",
    "selectivity", "选择性", "conversion", "转化率", "yield", "产率",
}

# Regex patterns for word-boundary-aware percentage metric matching.
# Simple substring match ("fe" in "lifetime") produces false positives.
_PERCENTAGE_PATTERNS = [
    re.compile(r'\b' + re.escape(pm) + r'\b', re.IGNORECASE)
    for pm in sorted(PERCENTAGE_METRICS, key=len, reverse=True)
]


def _is_percentage_metric(metric: str) -> bool:
    """Check whether metric is a percentage-type metric using word boundaries.

    Uses regex word-boundary matching to avoid substring false positives
    (e.g. "lifetime" should NOT match "FE" even though "fe" is a substring).
    """
    for pat in _PERCENTAGE_PATTERNS:
        if pat.search(metric):
            return True
    return False

def _semantic_validate(
    rec: dict,
    idx: int,
    *,
    role_map: dict[str, str] | None = None,
) -> list[str]:
    """Semantic validation: value/unit reasonability (pre-write gate, all templates).

    Validation is role-aware — it uses semantic roles (results, relations, etc.)
    rather than concrete module names, so it works across all schema templates.
    """
    warnings = []
    mod = str(rec.get("module", ""))
    metric = str(rec.get("metric", "")).strip()
    value = str(rec.get("value", "")).strip()
    unit = str(rec.get("unit", "")).strip()

    # Resolve the semantic role from the role map (default empty string)
    role = ""
    if role_map and mod in role_map:
        role = str(role_map[mod]).strip()

    # ---- all modules: placeholder text detection ----
    if value:
        for pat in PLACEHOLDER_PATTERNS:
            if pat in value:
                warnings.append(
                    f"record[{idx}]: value contains placeholder text '{pat}' "
                    f"but no missing_status field — "
                    f"consider annotating not_reported / not_found / ambiguous in note")
                break

    # ---- all modules: source field location specifier check ----
    source = str(rec.get("source", "")).strip()
    if source:
        location_keywords = [
            "Fig", "Figure", "Table", "Section", "SI", "Methods", "Results",
            "图", "表", "节", "全文", "摘要", "讨论段", "Eq",
            "PDF front matter", "Zotero metadata", "DOI metadata",
            "Supplementary",
        ]
        has_location = any(kw in source for kw in location_keywords)
        if not has_location:
            warnings.append(
                f"record[{idx}]: source lacks location specifier "
                f"(Fig/Table/Section/SI/Methods) — current: {source[:80]}")

    # ---- results role: value/unit reasonability ----
    if role == "results":
        # Check for percentage-type metrics (word-boundary matching)
        is_percentage = _is_percentage_metric(metric)
        if is_percentage:
            try:
                v = float(value)
                if v < 0:
                    warnings.append(
                        f"record[{idx}]: results percentage value={value} is negative, "
                        f"suspected potential/energy value stored instead — "
                        f"check if value/unit swapped")
                elif v > 100:
                    warnings.append(
                        f"record[{idx}]: results percentage value={value} >100%, "
                        f"please verify against source")
            except ValueError:
                pass  # non-numeric value, OK (may be descriptive text)

    # ---- relations role: value should not be empty ----
    if role == "relations":
        if not value:
            warnings.append(
                f"record[{idx}]: relations value is empty — "
                f"please fill in mechanism or relationship description")
        if not unit and not value:
            warnings.append(
                f"record[{idx}]: relations value and unit are both empty")

    return warnings


def _sanitize_cell(text) -> str:
    """Clean cell content: halfwidth pipe → fullwidth (prevents Markdown table breakage), newlines → spaces."""
    return str(text).replace("|", "｜").replace("\r\n", " ").replace("\n", " ").strip()


def _format_row(rec: dict, record_id: str) -> str:
    """Format a record as a kb table row"""
    fields = [
        record_id,
        rec.get("schema_version", "schema_v1"),
        rec.get("paper_id", ""),
        rec.get("module", ""),
        _sanitize_cell(rec.get("category", "")),
        _sanitize_cell(rec.get("subject", "")),
        _sanitize_cell(rec.get("metric", "")),
        _sanitize_cell(rec.get("value", "")),
        _sanitize_cell(rec.get("unit", "")),
        _sanitize_cell(rec.get("condition", "")),
        _sanitize_cell(rec.get("source", "")),
        rec.get("confidence", "single_source"),
        _sanitize_cell(rec.get("note", "")),
    ]
    return "| " + " | ".join(fields) + " |\n"


@dataclass(frozen=True)
class WriteResult:
    record_ids: tuple[str, ...]


@dataclass(frozen=True)
class PaperWriteOutcome:
    paper_id: str
    status: str
    record_ids: tuple[str, ...] = ()
    errors: tuple[str, ...] = ()


@dataclass(frozen=True)
class BatchWriteResult:
    outcomes: tuple[PaperWriteOutcome, ...]


def _workspace_module_map(workspace: Path) -> dict[str, str]:
    from rsk.kb.coverage import active_module_map

    return active_module_map(workspace)


def _current_max_id(path: Path, module: str) -> int:
    if not path.is_file():
        return 0
    values = [
        int(match.group(1))
        for match in re.finditer(
            rf"(?m)^\|\s*{re.escape(module)}-(\d+)\s*\|",
            path.read_text(encoding="utf-8"),
        )
    ]
    return max(values, default=0)


def _prepare_records(
    records: list[dict],
    *,
    workspace: Path,
) -> tuple[list[dict], dict[str, tuple[str, ...]]]:
    module_map = _workspace_module_map(workspace)
    prepared: list[dict] = []
    next_ids = {
        module: _current_max_id(
            workspace / "kb" / file,
            module,
        )
        + 1
        for module, file in module_map.items()
    }
    assigned: dict[str, list[str]] = defaultdict(list)
    for index, record in enumerate(records):
        errors = []
        for field in REQUIRED_FIELDS:
            if field not in record or record[field] is None:
                errors.append(f"missing required field {field!r}")
        module = str(record.get("module", ""))
        if module not in module_map:
            errors.append(f"unknown module {module!r}")
        if not str(record.get("source", "")).strip():
            errors.append("source is empty")
        else:
            from rsk.kb.bibliography import (
                BIBLIOGRAPHY_CATEGORY,
                BIBLIOGRAPHY_METRIC,
            )
            from rsk.kb.source import validate_source_for_write

            bibliography = (
                record.get("category") == BIBLIOGRAPHY_CATEGORY
                and record.get("metric") == BIBLIOGRAPHY_METRIC
            )
            errors.extend(
                validate_source_for_write(
                    record.get("source"),
                    paper_id=str(record.get("paper_id", "")),
                    bibliography=bibliography,
                )
            )
        if errors:
            raise ValueError(f"record[{index}]: " + "; ".join(errors))
        item = dict(record)
        record_id = f"{module}-{next_ids[module]:04d}"
        next_ids[module] += 1
        item["_assigned_id"] = record_id
        prepared.append(item)
        assigned[module].append(record_id)
    return prepared, {
        module: tuple(record_ids)
        for module, record_ids in assigned.items()
    }


def _row_cells(line: str) -> list[str] | None:
    if not line.lstrip().startswith("|"):
        return None
    cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
    return cells if len(cells) >= 13 else None


def _existing_bibliography_id(
    path: Path,
    *,
    paper_id: str,
    module: str,
) -> str | None:
    from rsk.kb.bibliography import (
        BIBLIOGRAPHY_CATEGORY,
        BIBLIOGRAPHY_METRIC,
    )

    matches = []
    for line in path.read_text(encoding="utf-8").splitlines():
        cells = _row_cells(line)
        if (
            cells is not None
            and cells[2] == paper_id
            and cells[3] == module
            and cells[4] == BIBLIOGRAPHY_CATEGORY
            and cells[6] == BIBLIOGRAPHY_METRIC
        ):
            matches.append(cells[0])
    if len(matches) > 1:
        raise ValueError(
            f"{paper_id}: duplicate bibliographic metadata records"
        )
    return matches[0] if matches else None


def _replace_row(text: str, record: dict, record_id: str) -> str:
    lines = text.splitlines()
    matches = [
        index
        for index, line in enumerate(lines)
        if (
            (cells := _row_cells(line)) is not None
            and cells[0] == record_id
        )
    ]
    if len(matches) != 1:
        raise ValueError(
            f"expected one existing row for {record_id}, found {len(matches)}"
        )
    lines[matches[0]] = _format_row(record, record_id).rstrip("\n")
    return "\n".join(lines) + "\n"


def _append_rows(text: str, records: list[dict]) -> str:
    if text and not text.endswith("\n"):
        text += "\n"
    return text + "".join(
        _format_row(record, record["_assigned_id"])
        for record in records
    )


def _write_temp(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        mode="w",
        encoding="utf-8",
        newline="\n",
        dir=path.parent,
        prefix=f".{path.stem}-",
        suffix=".tmp",
        delete=False,
    ) as handle:
        handle.write(content)
        handle.flush()
        os.fsync(handle.fileno())
        return Path(handle.name)


def _restore_bytes(path: Path, content: bytes | None) -> None:
    if content is None:
        if path.exists():
            path.unlink()
        return
    with tempfile.NamedTemporaryFile(
        mode="wb",
        dir=path.parent,
        prefix=f".{path.stem}-rollback-",
        suffix=".tmp",
        delete=False,
    ) as handle:
        handle.write(content)
        handle.flush()
        os.fsync(handle.fileno())
        temporary = Path(handle.name)
    try:
        os.replace(temporary, path)
    finally:
        if temporary.exists():
            temporary.unlink()


def _commit_text_transaction(changes: Mapping[Path, str]) -> None:
    """Replace all paper-owned files and restore originals on failure."""
    originals = {
        path: path.read_bytes() if path.exists() else None
        for path in changes
    }
    temporaries = {
        path: _write_temp(path, content)
        for path, content in changes.items()
    }
    replaced: list[Path] = []
    try:
        for path, temporary in temporaries.items():
            os.replace(temporary, path)
            replaced.append(path)
    except Exception:
        rollback_errors = []
        for path in reversed(replaced):
            try:
                _restore_bytes(path, originals[path])
            except Exception as rollback_error:
                rollback_errors.append(f"{path}: {rollback_error}")
        if rollback_errors:
            raise RuntimeError(
                "paper transaction failed and rollback was incomplete: "
                + "; ".join(rollback_errors)
            )
        raise
    finally:
        for temporary in temporaries.values():
            if temporary.exists():
                temporary.unlink()


def write_ingest_envelope(
    envelope: dict,
    *,
    workspace: Path,
    dry_run: bool = False,
) -> WriteResult:
    """Validate and atomically persist one complete paper envelope."""
    from rsk.kb.bibliography import (
        build_bibliography_record,
        literature_module,
    )
    from rsk.kb.coverage import (
        build_coverage,
        coverage_path,
        render_coverage_document,
    )

    workspace = Path(workspace).expanduser().resolve()
    paper_id = str(envelope.get("paper_id", "")).strip()
    schema_version = (
        str(envelope.get("schema_version", "")).strip() or "schema_v1"
    )
    candidates = envelope.get("schema_candidates")
    declarations = envelope.get("module_coverage")
    if not paper_id or not isinstance(candidates, dict):
        raise ValueError("ingest envelope requires paper_id and schema_candidates")
    if not isinstance(declarations, dict):
        raise ValueError("ingest envelope requires module_coverage")
    records: list[dict] = []
    for module, items in candidates.items():
        if not isinstance(items, list):
            raise ValueError(f"schema_candidates.{module} must be a list")
        for raw in items:
            record = dict(raw)
            record["module"] = module
            # Auto-fill envelope-level fields (module is already auto-filled);
            # an explicit per-record value that contradicts the envelope is an
            # error rather than silently overridden.
            record["schema_version"] = (
                str(record.get("schema_version") or schema_version)
            )
            if not str(record.get("paper_id", "")).strip():
                record["paper_id"] = paper_id
            elif str(record["paper_id"]) != paper_id:
                raise ValueError(f"{module}: paper_id does not match envelope")
            records.append(record)
    bibliography = envelope.get("bibliography")
    replacement: tuple[str, dict] | None = None
    if bibliography:
        if not isinstance(bibliography, Mapping):
            raise ValueError("bibliography must be an object")
        bibliography_record = build_bibliography_record(
            workspace=workspace,
            paper_id=paper_id,
            bibliography=bibliography,
        )
        literature = literature_module(workspace)
        literature_path = (
            workspace / "kb" / str(literature["file"])
        )
        existing_id = _existing_bibliography_id(
            literature_path,
            paper_id=paper_id,
            module=str(literature["name"]),
        )
        if existing_id is None:
            records.insert(0, bibliography_record)
        else:
            replacement = (existing_id, bibliography_record)
    prepared, raw_assigned = _prepare_records(
        records,
        workspace=workspace,
    )
    assigned = {
        module: list(record_ids)
        for module, record_ids in raw_assigned.items()
    }
    ordered_ids = [item["_assigned_id"] for item in prepared]
    if replacement is not None:
        existing_id, replacement_record = replacement
        module = str(replacement_record["module"])
        assigned.setdefault(module, []).insert(0, existing_id)
        ordered_ids.insert(0, existing_id)
    coverage = build_coverage(
        workspace=workspace,
        paper_id=paper_id,
        declarations=declarations,
        assigned_record_ids={
            module: tuple(record_ids)
            for module, record_ids in assigned.items()
        },
    )
    if dry_run:
        return WriteResult(record_ids=tuple(ordered_ids))
    module_map = _workspace_module_map(workspace)
    grouped: dict[str, list[dict]] = defaultdict(list)
    for item in prepared:
        grouped[str(item["module"])].append(item)
    changes: dict[Path, str] = {}
    for module, items in grouped.items():
        path = workspace / "kb" / module_map[module]
        changes[path] = _append_rows(
            path.read_text(encoding="utf-8"),
            items,
        )
    if replacement is not None:
        existing_id, replacement_record = replacement
        path = workspace / "kb" / module_map[
            str(replacement_record["module"])
        ]
        base = changes.get(path, path.read_text(encoding="utf-8"))
        changes[path] = _replace_row(
            base,
            replacement_record,
            existing_id,
        )
    changes[coverage_path(workspace, paper_id)] = (
        render_coverage_document(coverage)
    )
    _commit_text_transaction(changes)
    return WriteResult(record_ids=tuple(ordered_ids))


def write_ingest_batch(
    envelopes: list[dict],
    *,
    workspace: Path,
    dry_run: bool = False,
) -> BatchWriteResult:
    """Write valid papers independently without accepting partial papers."""
    outcomes = []
    for envelope in envelopes:
        paper_id = str(envelope.get("paper_id", "")).strip() or "<unknown>"
        try:
            result = write_ingest_envelope(
                envelope,
                workspace=workspace,
                dry_run=dry_run,
            )
        except (ValueError, OSError) as exc:
            outcomes.append(
                PaperWriteOutcome(
                    paper_id=paper_id,
                    status="retryable_failed",
                    errors=(str(exc),),
                )
            )
        else:
            outcomes.append(
                PaperWriteOutcome(
                    paper_id=paper_id,
                    status="accepted",
                    record_ids=result.record_ids,
                )
            )
    return BatchWriteResult(outcomes=tuple(outcomes))


def write_input_file(
    path: Path,
    *,
    workspace: Path,
    dry_run: bool = False,
) -> WriteResult:
    """Write one structured plugin ingest envelope without dropping coverage."""
    try:
        payload = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"cannot read ingest input: {exc}") from exc
    if not isinstance(payload, dict):
        raise ValueError("structured ingest input must be an object")
    if "schema_candidates" not in payload or "module_coverage" not in payload:
        raise ValueError(
            "structured ingest input requires schema_candidates and "
            "module_coverage"
        )
    return write_ingest_envelope(
        payload,
        workspace=workspace,
        dry_run=dry_run,
    )


# -- main ----------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Batch write schema_v1 records to kb modules")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--input", "-i", help="Single JSON file path")
    group.add_argument("--input-dir", "-d", help="JSON file directory (batch process all .json)")
    parser.add_argument("--dry-run", action="store_true", help="Validate and preview only, no actual write")
    parser.add_argument("--strict", action="store_true",
                        help="Treat semantic warnings as errors (block write on warnings)")
    args = parser.parse_args()

    # Collect JSON files
    if args.input:
        json_files = [Path(args.input)]
    else:
        json_files = sorted(Path(args.input_dir).glob("*.json"))

    if not json_files:
        print("Error: no JSON input files found")
        sys.exit(1)

    # Read all records
    all_records = []
    load_errors = []
    structured_results = []
    for jf in json_files:
        try:
            with open(jf, "r", encoding="utf-8") as f:
                data = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError) as e:
            load_errors.append(f"{jf.name}: {e}")
            continue

        if (
            isinstance(data, dict)
            and "schema_candidates" in data
            and "module_coverage" in data
        ):
            try:
                structured_results.append(
                    write_ingest_envelope(
                        data,
                        workspace=PROJECT_ROOT,
                        dry_run=args.dry_run,
                    )
                )
            except (ValueError, OSError) as exc:
                load_errors.append(f"{jf.name}: {exc}")
            continue
        if isinstance(data, list) and data and all(
            isinstance(item, dict)
            and "schema_candidates" in item
            and "module_coverage" in item
            for item in data
        ):
            # Array-of-envelopes: route through the batch writer instead of
            # flattening into plain records (which would fail the required
            # 'module' field check).
            try:
                batch = write_ingest_batch(
                    data,
                    workspace=PROJECT_ROOT,
                    dry_run=args.dry_run,
                )
            except (ValueError, OSError) as exc:
                load_errors.append(f"{jf.name}: {exc}")
                continue
            structured_results.extend(
                WriteResult(record_ids=tuple(
                    outcome.record_ids
                    for outcome in batch.outcomes
                    if outcome.status == "accepted"
                ))
            )
            for outcome in batch.outcomes:
                if outcome.status == "retryable_failed":
                    load_errors.append(
                        f"{jf.name}: {outcome.paper_id}: "
                        + "; ".join(outcome.errors)
                    )
            continue
        if isinstance(data, list):
            records = data
        elif isinstance(data, dict):
            # Compat: nested format {"schema_candidates": {"synthesis": [...], ...}}
            if "schema_candidates" in data:
                records = []
                for mod, recs in data["schema_candidates"].items():
                    for r in recs:
                        r["module"] = mod
                        records.append(r)
            else:
                records = [data]
        else:
            load_errors.append(f"{jf.name}: unsupported JSON type {type(data)}")
            continue

        coverage_markers = [
            r for r in records if r.get("category") == "module_coverage"
        ]
        if coverage_markers:
            load_errors.append(
                f"{jf.name}: legacy module_coverage rows are not silently "
                "discarded; use the structured module_coverage envelope"
            )
        records = [
            r for r in records if r.get("category") != "module_coverage"
        ]
        all_records.extend(records)

    if load_errors:
        print("Load warnings:")
        for e in load_errors:
            print(f"  {e}")

    if not all_records and structured_results:
        total = sum(len(result.record_ids) for result in structured_results)
        print(f"Done: {total} structured records processed with coverage")
        return

    if not all_records:
        print("Error: no valid records to write")
        sys.exit(1)

    from rsk.kb.coverage import load_active_schema, active_module_map

    module_map = _workspace_module_map(PROJECT_ROOT)
    modules = tuple(module_map)
    kb_dir = Path(PROJECT_ROOT) / "kb"

    # Build role_map from active schema: {module_name: role}
    active_schema = load_active_schema(PROJECT_ROOT)
    raw_module_map = active_module_map(PROJECT_ROOT)
    role_map: dict[str, str] = {}
    try:
        from rsk.schema.contract import builtin_template_root

        template_root = builtin_template_root()
        template_id = str(active_schema.get("template_id", ""))
        if template_id:
            proposal = __import__(
                "rsk.schema.contract", fromlist=["load_builtin_template"]
            ).load_builtin_template(template_id, template_root=template_root)
            for module in getattr(proposal, "modules", []):
                role_map[str(module.name)] = str(module.role)
    except Exception:
        pass
    # Fallback: try to read roles from generated modules.yaml (workspace)
    if not role_map:
        try:
            modules_yaml_path = PROJECT_ROOT / "schemas" / "generated" / "modules.yaml"
            if modules_yaml_path.exists():
                with open(modules_yaml_path, "r", encoding="utf-8") as _mf:
                    modules_data = yaml.safe_load(_mf)
                for mod in (modules_data.get("modules") or []):
                    name = str(mod.get("name", ""))
                    role = str(mod.get("role", ""))
                    if name and role:
                        role_map[name] = role
        except Exception:
            pass
    # Last resort: module name → module name (correct only for generic-science
    # where module names happen to equal their semantic roles)
    if not role_map:
        for mod_name in raw_module_map:
            role_map[str(mod_name)] = str(mod_name)

    # Validate
    validation_errors = []
    for i, rec in enumerate(all_records):
        errs = _validate_record(rec, i, modules)
        validation_errors.extend(errs)

    if validation_errors:
        print(f"Structural validation failed ({len(validation_errors)} errors):")
        for e in validation_errors:
            print(f"  {e}")
        sys.exit(1)

    # Semantic check: value/unit reasonability review (role-aware, all templates).
    # By default prints warnings; with --strict, warnings become errors that block writes.
    semantic_warnings = []
    for i, rec in enumerate(all_records):
        semantic_warnings.extend(
            _semantic_validate(
                rec,
                i,
                role_map=role_map,
            )
        )
    if semantic_warnings:
        label = "ERRORS" if args.strict else "warnings"
        print(f"\nSemantic validation {label} ({len(semantic_warnings)} items):")
        for w in semantic_warnings:
            print(f"  {w}")
        if args.strict:
            print(f"\nSemantic validation failed ({len(semantic_warnings)} errors). Use --dry-run to preview, or fix the issues above.")
            sys.exit(1)

    # Group by module and assign IDs
    current_ids = _get_current_max_ids(kb_dir, module_map)
    module_groups = defaultdict(list)
    module_next_ids = {}

    for mod in modules:
        module_next_ids[mod] = current_ids.get(mod, 0) + 1

    for rec in all_records:
        mod = rec["module"]
        rid = f"{mod}-{module_next_ids[mod]:04d}"
        rec["_assigned_id"] = rid
        module_groups[mod].append(rec)
        module_next_ids[mod] += 1

    # Preview
    print(f"\n{'[DRY RUN] ' if args.dry_run else ''}Pending write: {len(all_records)} records")
    print(f"  Source files: {len(json_files)}")
    for mod in modules:
        n = len(module_groups[mod])
        if n > 0:
            first = module_groups[mod][0]["_assigned_id"]
            last = module_groups[mod][-1]["_assigned_id"]
            paper_ids = sorted(set(r["paper_id"] for r in module_groups[mod]))
            print(
                f"  {module_map[mod]}: +{n} records "
                f"({first} -> {last}) | papers: {', '.join(paper_ids)}"
            )

    if args.dry_run:
        print("\n[Dry run -- no actual write]")
        # Sample check: show first record from each module with records
        for mod in modules:
            recs = module_groups[mod]
            if not recs:
                continue
            r = recs[0]
            print(f"\n  [{r['module']}] {r.get('subject','')[:60]}")
            print(f"    metric={r.get('metric','')}  value={r.get('value','')}  unit={r.get('unit','')}")
            print(f"    source={r.get('source','')[:80]}")
        return

    # Write
    for mod in modules:
        recs = module_groups[mod]
        if not recs:
            continue
        fpath = kb_dir / module_map[mod]
        with open(fpath, "a", encoding="utf-8") as f:
            for rec in recs:
                f.write(_format_row(rec, rec["_assigned_id"]))
        print(f"  Written {fpath.name} ({len(recs)} records)")

    print(f"\nDone: {len(all_records)} records written to {len(module_groups)} modules")


if __name__ == "__main__":
    main()
