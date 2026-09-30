# -*- coding: utf-8 -*-
"""
Schema records → 自然语言 claims 索引

读取 kb/*.md 的 schema_v1 表行，将每条 13 字段记录合成为自然语言 claim，
输出为 JSONL 供 sync_vectors.py --from-claims 嵌入到 kb_claims collection。

用法:
    python -m rsk.vector.claims                    # 输出到 stdout
    python -m rsk.vector.claims -o outputs/claims_index.jsonl
"""

import argparse, json, os, re, sys
from collections import defaultdict
from pathlib import Path

from rsk.config import PROJECT_ROOT
from rsk.kb.coverage import active_modules, load_active_schema
from rsk.kb.source import parse_source
from rsk.vector._config import retrieval_value

CLAIM_FIELDS = (
    "record_id",
    "schema_version",
    "paper_id",
    "module",
    "category",
    "subject",
    "metric",
    "value",
    "unit",
    "condition",
    "source",
    "confidence",
    "note",
)

# Retrieval-facing truncation limits. Tuned for long descriptive values
# (e.g. Chinese medical literature); resolve via workspace
# configs/retrieval.yaml, env vars (RSK_CLAIM_VALUE_LIMIT etc.), then
# built-in defaults. See rsk.vector._config.retrieval_value.
CLAIM_VALUE_LIMIT = int(retrieval_value("claim_value_limit", "160"))
CHAIN_VALUE_LIMIT = int(retrieval_value("chain_value_limit", "60"))
CHAIN_TOTAL_LIMIT = int(retrieval_value("chain_total_limit", "1100"))

SEMANTIC_NOISE = {"", "无", "None", "n/a"}


def _clean(value) -> str:
    return str(value or "").strip()


def parse_schema_rows(filepath):
    """Parse a pipe-delimited schema_v1 table, return list of dicts."""
    rows = []
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    in_table = False
    for line in lines:
        line = line.strip()
        if re.match(r"\| record_id\s+\|", line):
            in_table = True
            continue
        if not in_table:
            continue
        if not line.startswith("|"):
            continue
        if "---|---" in line:
            continue
        # Split by pipe, keeping internal content. Protect || within fields.
        line_safe = line.replace("||", "__DBLPIPE__")
        parts = [p.strip().replace("__DBLPIPE__", "||") for p in line_safe.split("|")]
        # Remove leading/trailing empty from split
        if parts and parts[0] == "":
            parts = parts[1:]
        if parts and parts[-1] == "":
            parts = parts[:-1]
        if len(parts) < 13:
            continue
        record = {
            "record_id": parts[0],
            "schema_version": parts[1],
            "paper_id": parts[2],
            "module": parts[3],
            "category": parts[4],
            "subject": parts[5],
            "metric": parts[6],
            "value": parts[7],
            "unit": parts[8],
            "condition": parts[9],
            "source": parts[10],
            "confidence": parts[11],
            "note": parts[12] if len(parts) > 12 else "",
        }
        rows.append(record)
    return rows


def build_claim(record):
    """Build one discipline-neutral claim from the stable 13-field contract.

    Semantic fields (category/subject/metric/value/unit/condition) are
    front-loaded and bookkeeping noise is dropped (record_id/schema_version,
    empty ``unit``): the old flat ``key=value`` rendering diluted semantic
    signal, and long descriptive values acted as global attractors under
    pure-cosine retrieval. Values are capped at :data:`CLAIM_VALUE_LIMIT`.
    """
    category = _clean(record.get("category"))
    subject = _clean(record.get("subject"))
    metric = _clean(record.get("metric"))
    value = _clean(record.get("value"))
    unit = _clean(record.get("unit"))
    condition = _clean(record.get("condition"))
    note = _clean(record.get("note"))
    paper_id = _clean(record.get("paper_id"))
    source = _clean(record.get("source"))
    confidence = _clean(record.get("confidence"))

    parts = []
    if category and category not in SEMANTIC_NOISE:
        parts.append(f"[{category}]")
    if subject:
        parts.append(subject[:CLAIM_VALUE_LIMIT])
    if metric and metric not in SEMANTIC_NOISE:
        measured = f"{metric} = {value}" if value else metric
        if unit and unit not in SEMANTIC_NOISE:
            measured += f" {unit}"
        parts.append(measured[:CLAIM_VALUE_LIMIT])
    elif value:
        parts.append(value[:CLAIM_VALUE_LIMIT])
    if condition and condition not in SEMANTIC_NOISE:
        parts.append(f"条件: {condition[:CLAIM_VALUE_LIMIT]}")
    if note:
        parts.append(note[:CLAIM_VALUE_LIMIT])
    if paper_id:
        parts.append(f"paper={paper_id}")
    if source and source not in SEMANTIC_NOISE:
        source_clean = re.sub(r"[\[\]]", "", source)[:120]
        parts.append(f"来源: {source_clean}")
    if confidence and confidence != "single_source":
        parts.append(f"confidence={confidence}")
    return " | ".join(parts)


def enrich_claim(
    claim_text,
    record,
    *,
    template_id="electrocatalysis",
):
    """Append Chinese/English synonyms for key terminology to bridge the bge-m3 cross-lingual gap."""
    if template_id != "electrocatalysis":
        return claim_text
    text = claim_text
    module = record.get("module", "")
    subject = record.get("subject", "")
    metric = record.get("metric", "")
    value = record.get("value", "")
    condition = record.get("condition", "")
    category = record.get("category", "")

    # Combined context for smart detection
    ctx = f"{text} {subject} {metric} {condition} {category}".lower()

    # Prepend topic tags for strong signal (embedding front-weighted)
    prefix_tag = None
    synonyms = []

    # === CO2RR — needs strongest signal because "FE" dominates ===
    if any(t in ctx for t in ("co₂", "co2", "co₂rr", "co2rr", "co2 reduction", "co2 electroreduction", "co₂ reduction", "carbon dioxide")):
        if "甲酰胺" not in text and "formamide" not in text.lower() and "hconh" not in ctx:
            prefix_tag = "[CO2电还原 CO2RR]"
            if "CO2还原" not in text:
                synonyms.append("二氧化碳电还原 carbon dioxide electroreduction")

    # === NO3RR — distinguish NH3 vs acetamide ===
    if any(t in ctx for t in ("no₃rr", "no₃⁻", "no3rr", "nitrate reduction", "no₃→", "no₃⁻→nh₃", "no3-to-nh3", "no2rr", "no₂rr")):
        if "乙酰胺" in text or "acetamide" in ctx:
            # This is NO3RR→acetamide cascade, not pure NO3RR→NH3
            if "硝酸盐" not in text:
                synonyms.append("硝酸盐级联乙酰胺合成")
        else:
            prefix_tag = "[NO₃RR硝酸盐电还原合成氨]"
            if "硝酸盐电还原" not in text:
                synonyms.append("nitrate electroreduction to ammonia")

    # === Other reaction terminology ===
    if any(t in ctx for t in ("aor", "氨氧化", "ammonia oxidation", "nh₃→n₂", "nh3→n2")):
        if "氨氧化" not in text:
            synonyms.append("氨氧化反应")
        if "AOR" not in text:
            synonyms.append("ammonia oxidation reaction AOR")

    if any(t in ctx for t in ("her", "析氢", "h₂ evolution", "h2 evolution", "hydrogen evolution")):
        if "析氢" not in text:
            synonyms.append("析氢反应")
        if "HER" not in text:
            synonyms.append("hydrogen evolution reaction HER")

    if any(t in ctx for t in ("oer", "析氧", "o₂ evolution", "oxygen evolution")):
        if "析氧" not in text:
            synonyms.append("析氧反应")
        if "OER" not in text:
            synonyms.append("oxygen evolution reaction OER")

    if any(t in ctx for t in ("nr", "n₂rr", "n2rr", "氮还原", "nitrogen reduction")):
        if "氮还原" not in text:
            synonyms.append("氮气还原合成氨")
        if "NRR" not in text:
            synonyms.append("nitrogen reduction reaction NRR")

    # === C-N coupling ===
    if any(t in ctx for t in ("c-n偶联", "c-n coupling", "c−n coupling", "c–n coupling", "cn coupling", "胺合成", "酰胺合成", "尿素合成")):
        if "C-N偶联" not in text:
            synonyms.append("C-N偶联电合成")
        if "C-N coupling" not in text:
            synonyms.append("electrocatalytic C-N coupling")

    # === RDS / barrier ===
    if any(t in ctx for t in ("rds", "决速步", "rate-determining", "势垒", "能垒", "barrier", "δg", "δe")):
        if "决速步" not in text:
            synonyms.append("决速步速率控制步骤")
        if "RDS" not in text:
            synonyms.append("rate-determining step RDS energy barrier")

    # === Synthesis methods ===
    if any(t in ctx for t in ("pyrolysis", "热解", "calcination", "煅烧", "annealing", "退火", "°c", "℃", "temperature")):
        if module == "synthesis":
            if "热解" not in text and "煅烧" not in text:
                synonyms.append("热解煅烧退火合成条件")
            if "pyrolysis calcination" not in text:
                synonyms.append("synthesis condition pyrolysis calcination temperature")

    # === Electrolyte / cation ===
    if any(t in ctx for t in ("koh", "naoh", "khco₃", "nahco₃", "h₂so₄", "hcl", "electrolyte", "电解液", "电解")):
        if "电解液" not in text:
            synonyms.append("电解液")
        if "electrolyte" not in text:
            synonyms.append("electrolyte")

    if any(t in ctx for t in ("阳离子", "cation", "li⁺", "na⁺", "k⁺", "cs⁺", "li+", "na+", "k+", "cs+", "alkali")):
        if "阳离子" not in text:
            synonyms.append("阳离子效应碱金属")
        if "cation effect" not in text:
            synonyms.append("alkali metal cation effect")

    # === Characterization ===
    if any(t in ctx for t in ("xps", "xanes", "exafs", "raman", "ftir", "seiras", "dems", "nmr", "epr")):
        techniques = []
        if "xps" in ctx and "XPS" not in text: techniques.append("XPS X射线光电子能谱")
        if "raman" in ctx and "Raman" not in text: techniques.append("Raman拉曼光谱")
        if "ftir" in ctx and "FTIR" not in text: techniques.append("FTIR红外光谱")
        if "xanes" in ctx and "XANES" not in text: techniques.append("XANES X射线吸收近边结构")
        if techniques:
            synonyms.extend(techniques)

    # === DFT / computation ===
    if any(t in ctx for t in ("dft", "vasp", "d-band", "d band", "d带", "bader", "pdos", "自由能", "free energy", "δg", "aimd")):
        if "DFT" not in text:
            synonyms.append("DFT密度泛函理论计算")
        if "d-band" not in text and "d band" in ctx:
            synonyms.append("d-band center d带中心")

    # Append synonyms as searchable tags
    if synonyms:
        text += " [同义词: " + " | ".join(synonyms) + "]"
    # Prepend topic tag for embedding front-weighting
    if prefix_tag:
        text = prefix_tag + " " + text

    return text


def _record_info_score(record) -> int:
    """Heuristic for chain selection: non-empty semantic fields, compactness."""
    score = 0
    for field in ("subject", "metric", "value", "condition"):
        value = _clean(record.get(field))
        if value and value not in SEMANTIC_NOISE:
            score += 1
    if len(_clean(record.get("value"))) <= 120:
        score += 1
    return score


def build_paper_chain_claim(
    paper_id,
    records_by_module,
    *,
    module_order=None,
    literature_modules=None,
):
    """Build a cross-module claim in configured concrete-module order.

    Picks the single information-dense record per module (rather than the
    first two), truncates per segment, and enforces a total cap by dropping
    whole trailing segments — a naive tail cut used to slice the final
    ``[claims]`` module empty, making conclusion-level queries unreachable.
    """
    parts = [f"[论文逻辑链] {paper_id}"]
    order = tuple(module_order or records_by_module.keys())
    literature = set(literature_modules or {"literature"})
    for module in order:
        if module in literature:
            continue
        records = records_by_module.get(module, ())
        if not records:
            continue
        best = max(records, key=_record_info_score)
        subject = _clean(best.get("subject"))
        metric = _clean(best.get("metric"))
        value = _clean(best.get("value"))
        unit = _clean(best.get("unit"))
        condition = _clean(best.get("condition"))
        segments = []
        if subject:
            segments.append(subject[:CHAIN_VALUE_LIMIT])
        if metric and metric not in SEMANTIC_NOISE:
            measured = f"{metric}={value}" if value else metric
            if unit and unit not in SEMANTIC_NOISE:
                measured += f" {unit}"
            segments.append(measured[:CHAIN_VALUE_LIMIT])
        elif value:
            segments.append(value[:CHAIN_VALUE_LIMIT])
        if condition and condition not in SEMANTIC_NOISE:
            segments.append(f"condition={condition[:CHAIN_VALUE_LIMIT]}")
        if segments:
            parts.append(f"[{module}] " + " | ".join(segments))

    sources = set()
    for module, records in records_by_module.items():
        if module in literature:
            continue
        for r in records:
            src = _clean(r.get("source"))
            if src and src not in SEMANTIC_NOISE:
                sources.add(re.sub(r"[\[\]]", "", src))
    if sources:
        parts.append(f"来源: {sorted(sources)[0]}")

    # Segment-aware cap: drop whole trailing segments instead of slicing the
    # final [module] block in half.
    kept: list[str] = []
    used = 0
    for part in parts:
        if used and used + len(part) + 2 > CHAIN_TOTAL_LIMIT:
            break
        kept.append(part)
        used += len(part) + 2
    return ". ".join(kept)


def build_index(output_path=None, file_filter=None, *, workspace=None):
    workspace_path = (
        Path(workspace).expanduser().resolve()
        if workspace is not None
        else PROJECT_ROOT
    )
    profile = load_active_schema(workspace_path)
    modules = active_modules(workspace_path)
    module_files = [str(module["file"]) for module in modules]
    module_order = [str(module["name"]) for module in modules]
    literature_modules = {
        str(module["name"])
        for module in modules
        if (
            str(module.get("role", "")) == "literature"
            or (
                not module.get("role")
                and str(module.get("name", "")) == "literature"
            )
        )
    }
    template_id = str(profile.get("template_id", "electrocatalysis"))
    kb_dir = workspace_path / "kb"
    claims = []
    target_files = file_filter if file_filter else module_files
    for fname in target_files:
        fpath = kb_dir / fname
        if not fpath.exists():
            print(f"[SKIP] {fname} not found", file=sys.stderr)
            continue
        records = parse_schema_rows(fpath)
        for rec in records:
            clean_text = build_claim(rec)
            if not clean_text or len(clean_text) < 15:
                continue
            retrieval_text = enrich_claim(
                clean_text,
                rec,
                template_id=template_id,
            )
            claims.append({
                "record_id": rec["record_id"],
                "paper_id": rec["paper_id"],
                "module": rec["module"],
                "source_file": fname,
                "source_metadata": parse_source(rec.get("source", "")),
                "claim_text": clean_text,
                "retrieval_text": retrieval_text,
            })
        print(f"[{fname}] {len(records)} records → {len([c for c in claims if c['source_file'] == fname])} claims", file=sys.stderr)

    # Build chain claims: group all records by paper_id across ALL module files.
    # Chain claims are cross-module composites — always scan every module file,
    # even under an incremental file_filter, so the paper grouping is complete.
    paper_records = defaultdict(lambda: defaultdict(list))
    for fname in module_files:
        fpath = kb_dir / fname
        if not fpath.exists():
            continue
        for rec in parse_schema_rows(fpath):
            paper_records[rec["paper_id"]][rec["module"]].append(rec)

    chain_count = 0
    for pid, by_module in paper_records.items():
        # Skip papers with only literature module (index-only entries)
        non_lit = {
            module: records
            for module, records in by_module.items()
            if module not in literature_modules
        }
        if len(non_lit) < 2:
            continue
        chain_text = build_paper_chain_claim(
            pid,
            by_module,
            module_order=module_order,
            literature_modules=literature_modules,
        )
        if chain_text and len(chain_text) >= 30:
            # Apply enrichment for cross-lingual bridging
            pseudo_record = {
                "module": "chain",
                "subject": pid,
                "metric": "", "value": "", "unit": "",
                "condition": "", "category": "论文逻辑链",
            }
            chain_retrieval_text = enrich_claim(
                chain_text,
                pseudo_record,
                template_id=template_id,
            )
            claims.append({
                "record_id": f"chain-{pid}",
                "paper_id": pid,
                "module": "chain",
                "source_file": "chain",
                "claim_type": "system_synthesized_chain",
                "claim_text": chain_text,
                "retrieval_text": chain_retrieval_text,
            })
            chain_count += 1

    print(f"[chain] {chain_count} paper chain claims generated", file=sys.stderr)

    if output_path:
        out = Path(output_path)
        out.parent.mkdir(parents=True, exist_ok=True)
        with open(out, "w", encoding="utf-8") as f:
            for c in claims:
                f.write(json.dumps(c, ensure_ascii=False) + "\n")
        print(f"Exported {len(claims)} claims to {output_path}", file=sys.stderr)
    else:
        for c in claims:
            print(json.dumps(c, ensure_ascii=False))

    return claims


def main():
    p = argparse.ArgumentParser(description="Build claims index from kb schema records")
    p.add_argument("-o", "--output", default=None, help="Output JSONL path (default: stdout)")
    p.add_argument(
        "--files",
        default=None,
        help="Comma-separated KB files to process (default: active modules)",
    )
    args = p.parse_args()
    file_filter = [f.strip() for f in args.files.split(",")] if args.files else None
    build_index(output_path=args.output, file_filter=file_filter)


if __name__ == "__main__":
    main()
