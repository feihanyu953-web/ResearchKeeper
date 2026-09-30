# -*- coding: utf-8 -*-
"""
审计层 1：向量生成完整性校验（确定性）

输入: vector_db/summary.json（sync_vectors.py 输出）
输出: records/vector_audit_log.jsonl (append)
"""

import json, os, sys, yaml
import re
from datetime import datetime, timezone, timedelta
from pathlib import Path

from rsk.config import PROJECT_ROOT, get, get_kb_dir, get_vector_db_dir
from rsk.kb.coverage import active_modules
from rsk.schema.materialize import workspace_schema_status

KB_DIR = get_kb_dir()
VECTOR_DB_DIR = get_vector_db_dir()
_gate_raw = get(
    "audit.vector_gate_config",
    "schemas/generated/vector_gate_queries.yaml",
)
GATE_CONFIG_PATH = Path(_gate_raw)
if not GATE_CONFIG_PATH.is_absolute():
    GATE_CONFIG_PATH = PROJECT_ROOT / GATE_CONFIG_PATH
AUDIT_LOG_PATH = PROJECT_ROOT / "records" / "vector_audit_log.jsonl"
EXCLUDE_FILES = {"REVIEWER_LOG.md", "INDEX.md", "REVIEWER.md", "SCHEMA.md", "qa.md"}
EXCLUDE_DIRS = {".audit", "reference", "coverage"}


def load_gate_queries(workspace):
    """Load the actual active query list for one explicit workspace."""
    path = (
        Path(workspace)
        / "schemas"
        / "generated"
        / "vector_gate_queries.yaml"
    )
    payload = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    queries = payload.get("test_queries")
    if not isinstance(queries, list):
        raise ValueError("active vector gate test_queries must be a list")
    if not all(isinstance(query, dict) for query in queries):
        raise ValueError("each active vector gate query must be an object")
    return tuple(dict(query) for query in queries)


def resolve_expected_modules(workspace, expected_role):
    """Resolve a stable role to concrete modules in active schema order."""
    return tuple(
        str(module["name"])
        for module in active_modules(Path(workspace))
        if str(module.get("role", "")) == expected_role
    )


def paper_abstract_issues(metadata):
    """Return deterministic integrity issues for one paper-level vector row."""
    issues = []
    paper_id = metadata.get("paper_id")
    abstract = metadata.get("abstract")
    roles = metadata.get("roles")
    module_names = metadata.get("module_names")
    n_records = metadata.get("n_records")
    if not isinstance(paper_id, str) or not paper_id.strip():
        issues.append("paper_id is required")
    if not isinstance(abstract, str) or len(abstract.strip()) < 30:
        issues.append("abstract is missing or too short")
    if not isinstance(roles, list) or not roles:
        issues.append("roles must be a non-empty list")
    if not isinstance(module_names, list) or not module_names:
        issues.append("module_names must be a non-empty list")
    if (
        isinstance(n_records, bool)
        or not isinstance(n_records, int)
        or n_records < 1
    ):
        issues.append("n_records must be a positive integer")
    return issues


def _threshold_number(value, default):
    if isinstance(value, (int, float)):
        return float(value)
    match = re.search(r"-?\d+(?:\.\d+)?", str(value))
    return float(match.group(0)) if match else float(default)


def count_kb_files():
    count = 0
    for md in KB_DIR.rglob("*.md"):
        parts = md.relative_to(KB_DIR).parts
        if parts[0] in EXCLUDE_DIRS or md.name in EXCLUDE_FILES:
            continue
        if any(p.startswith(".") for p in parts):
            continue
        count += 1
    return count

def audit_sync():
    if workspace_schema_status(PROJECT_ROOT) == "configured_empty":
        result = {
            "layer": "sync",
            "status": "N/A",
            "metrics": {},
            "issues": ["no knowledge records"],
        }
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return result
    summary_path = VECTOR_DB_DIR / "summary.json"
    if not summary_path.exists():
        result = {"layer": "sync", "status": "FAIL", "metrics": {},
            "issues": ["summary.json not found"]}
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return result

    with open(summary_path, "r", encoding="utf-8") as f:
        summary = json.load(f)

    if GATE_CONFIG_PATH.exists():
        with open(GATE_CONFIG_PATH, "r", encoding="utf-8") as f:
            gate = yaml.safe_load(f)
    else:
        gate = {
            "sync_audit": {"pass": {"coverage": 1.0, "truncation": 0},
                           "warn": {"coverage": 0.95, "truncation": 5},
                           "fail": {"coverage": 0.95, "truncation": 5}}
        }

    issues = []
    kb_count = count_kb_files()
    manifest_path = VECTOR_DB_DIR / "manifest.json"
    vector_count = 0
    if manifest_path.exists():
        with open(manifest_path, "r", encoding="utf-8") as f:
            manifest = json.load(f)
        vector_count = len(manifest)

    coverage = vector_count / kb_count if kb_count > 0 else 0
    if coverage < 1.0:
        issues.append(f"Coverage: {coverage:.2f} ({kb_count - vector_count} files missing vectors)")

    truncations = 0
    papers_meta_path = VECTOR_DB_DIR / "papers_meta.json"
    if papers_meta_path.exists():
        with open(papers_meta_path, "r", encoding="utf-8") as f:
            papers = json.load(f)
        for p in papers:
            if "abstract" in p or "paper_id" in p:
                metadata_issues = paper_abstract_issues(p)
                if metadata_issues:
                    truncations += 1
                    if truncations <= 3:
                        issues.append(
                            "Invalid paper abstract "
                            f"{p.get('paper_id', p.get('chunk_id', '?'))}: "
                            + "; ".join(metadata_issues)
                        )
                continue
            doc = p.get("text", "")
            # Legacy per-record schema chunks: short complete records are valid.
            if p.get("record_id", ""):
                continue
            if (
                doc
                and len(doc) < 200
                and not doc.strip().endswith((".", "。", "?"))
            ):
                truncations += 1
                if truncations <= 3:
                    issues.append(
                        "Possible truncation chunk "
                        f"{p['chunk_id']}: {len(doc)} chars"
                    )
    else:
        issues.append("papers_meta.json not found")

    if truncations > 0:
        issues.append(f"Truncation count: {truncations}")

    sync_policy = gate.get("sync_audit") or {}
    pass_policy = sync_policy.get("pass") or {}
    warn_policy = sync_policy.get("warn") or {}
    fail_policy = sync_policy.get("fail") or {}
    pass_coverage = _threshold_number(
        pass_policy.get("coverage"),
        1.0,
    )
    pass_truncation = int(
        _threshold_number(pass_policy.get("truncation"), 0)
    )
    fail_coverage = _threshold_number(
        fail_policy.get("coverage"),
        warn_policy.get("coverage", pass_coverage),
    )
    fail_truncation = int(
        _threshold_number(
            fail_policy.get("truncation"),
            warn_policy.get("truncation", pass_truncation + 1),
        )
    )

    status = "PASS"
    if coverage < fail_coverage or truncations >= fail_truncation:
        status = "FAIL"
    elif coverage < pass_coverage or truncations > pass_truncation:
        status = "WARN"

    result = {
        "ts": datetime.now(timezone(timedelta(hours=8))).isoformat(),
        "layer": "sync",
        "status": status,
        "metrics": {"coverage": round(coverage, 4), "truncations": truncations,
            "total_files": kb_count, "vector_files": vector_count},
        "issues": issues
    }

    AUDIT_LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(AUDIT_LOG_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps(result, ensure_ascii=False) + "\n")

    print(json.dumps(result, indent=2, ensure_ascii=False))
    return result

if __name__ == "__main__":
    result = audit_sync()
    if result["status"] == "FAIL":
        sys.exit(1)
