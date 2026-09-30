"""Schema-bound audit state and independent N/A review decisions."""

from __future__ import annotations

import hashlib
from pathlib import Path
from typing import Mapping

from rsk.kb.coverage import load_coverage
from rsk.kb.bibliography import (
    BIBLIOGRAPHY_CATEGORY,
    BIBLIOGRAPHY_METRIC,
    literature_module,
)
from rsk.schema.materialize import (
    active_schema_fingerprint,
    workspace_schema_status,
)


_CONTENT_EXCLUDED = {
    "INDEX.md",
    "REVIEWER.md",
    "REVIEWER_LOG.md",
    "SCHEMA.md",
}
_NA_DECISIONS = {"confirmed", "false_na", "evidence_missing"}


def audit_bibliography_coverage(workspace: Path) -> dict[str, object]:
    """Report literature-role papers lacking bibliographic metadata."""
    workspace = Path(workspace).expanduser().resolve()
    module = literature_module(workspace)
    module_name = str(module["name"])
    path = workspace / "kb" / str(module["file"])
    paper_ids: set[str] = set()
    bibliography_ids: set[str] = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.lstrip().startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 13 or cells[3] != module_name:
            continue
        paper_id = cells[2]
        if not paper_id or paper_id == "paper_id":
            continue
        paper_ids.add(paper_id)
        if (
            cells[4] == BIBLIOGRAPHY_CATEGORY
            and cells[6] == BIBLIOGRAPHY_METRIC
        ):
            bibliography_ids.add(paper_id)
    missing = sorted(paper_ids - bibliography_ids)
    return {
        "status": "WARN" if missing else "PASS",
        "literature_module": module_name,
        "paper_count": len(paper_ids),
        "bibliography_count": len(bibliography_ids),
        "missing": missing,
    }


def _tree_hash(files: list[Path], root: Path) -> str:
    manifest = bytearray()
    for path in sorted(files, key=lambda item: item.relative_to(root).as_posix()):
        relative = path.relative_to(root).as_posix()
        file_hash = hashlib.sha256(path.read_bytes()).hexdigest()
        manifest.extend(f"{relative}\n{file_hash}\n".encode("utf-8"))
    return hashlib.sha256(bytes(manifest)).hexdigest()


def content_file_manifest(workspace: Path) -> dict[str, str]:
    """Return the audited KB files as normalized paths and SHA-256 values."""
    workspace = Path(workspace).expanduser().resolve()
    kb = workspace / "kb"
    files = [
        path
        for path in kb.rglob("*.md")
        if path.name not in _CONTENT_EXCLUDED
        and ".audit" not in path.relative_to(kb).parts
    ]
    return {
        path.relative_to(workspace).as_posix(): hashlib.sha256(
            path.read_bytes()
        ).hexdigest()
        for path in sorted(
            files,
            key=lambda item: item.relative_to(workspace).as_posix(),
        )
    }


def diff_file_manifests(
    previous: Mapping[str, str] | None,
    current: Mapping[str, str],
) -> dict[str, object]:
    """Explain adjacent receipt changes without inventing a legacy diff."""
    if previous is None:
        return {
            "baseline_manifest_unavailable": True,
            "added": [],
            "modified": [],
            "deleted": [],
        }
    previous_paths = set(previous)
    current_paths = set(current)
    return {
        "baseline_manifest_unavailable": False,
        "added": sorted(current_paths - previous_paths),
        "modified": sorted(
            path
            for path in previous_paths & current_paths
            if previous[path] != current[path]
        ),
        "deleted": sorted(previous_paths - current_paths),
    }


def content_tree_hash(workspace: Path) -> str:
    workspace = Path(workspace).expanduser().resolve()
    manifest = bytearray()
    for relative, file_hash in content_file_manifest(workspace).items():
        manifest.extend(f"{relative}\n{file_hash}\n".encode("utf-8"))
    return hashlib.sha256(bytes(manifest)).hexdigest()


def vector_gate_hash(workspace: Path) -> str:
    path = (
        Path(workspace)
        / "schemas"
        / "generated"
        / "vector_gate_queries.yaml"
    )
    return hashlib.sha256(path.read_bytes()).hexdigest()


def empty_workspace_audit(workspace: Path) -> dict[str, dict[str, str]]:
    if workspace_schema_status(workspace) != "configured_empty":
        raise ValueError("empty workspace audit requires configured_empty schema")
    return {
        "schema": {"status": "PASS"},
        "content": {
            "status": "N/A",
            "reason": "empty knowledge base",
        },
        "vector_sync": {
            "status": "N/A",
            "reason": "no knowledge records",
        },
        "retrieval": {
            "status": "N/A",
            "reason": "no knowledge records",
        },
    }


def assess_not_applicable_reviews(
    workspace: Path,
    paper_id: str,
    decisions: Mapping[str, Mapping[str, str]],
) -> dict[str, object]:
    coverage = load_coverage(workspace, paper_id)
    required = {
        module
        for module, entry in coverage.modules.items()
        if entry.status == "not_applicable"
    }
    errors: list[str] = []
    if set(decisions) != required:
        missing = sorted(required - set(decisions))
        extra = sorted(set(decisions) - required)
        if missing:
            errors.append("missing independent N/A reviews: " + ", ".join(missing))
        if extra:
            errors.append("unexpected independent N/A reviews: " + ", ".join(extra))
    for module in sorted(required & set(decisions)):
        raw = decisions[module]
        decision = str(raw.get("decision", ""))
        finding = str(raw.get("finding", "")).strip()
        if decision not in _NA_DECISIONS or not finding:
            errors.append(f"{module}: invalid independent N/A review")
        elif decision == "false_na":
            errors.append(
                f"{module}: false N/A; source content requires extraction"
            )
        elif decision == "evidence_missing":
            errors.append(
                f"{module}: original paper or SI evidence missing"
            )
    return {
        "status": "fail" if errors else "pass",
        "paper_id": paper_id,
        "reviewed_modules": sorted(required),
        "errors": errors,
    }


def audit_receipt_directory(workspace: Path, *, layer: str) -> Path:
    if layer not in {"kb", "vector"}:
        raise ValueError(f"unknown audit layer: {layer}")
    return Path(workspace) / "kb" / ".audit" / "receipts"


def build_audit_receipt(
    workspace: Path,
    *,
    verdict: str,
    reviewer_report_digest: str,
    include_vector_gate: bool = False,
) -> dict[str, object]:
    workspace = Path(workspace).expanduser().resolve()
    receipt: dict[str, object] = {
        "schema_version": "rsk_audit_receipt_v2",
        "verdict": verdict,
        "schema_fingerprint": active_schema_fingerprint(workspace),
        "content_tree_hash": content_tree_hash(workspace),
        "file_manifest": content_file_manifest(workspace),
        "reviewer_report_digest": reviewer_report_digest,
    }
    if include_vector_gate:
        receipt["vector_gate_hash"] = vector_gate_hash(workspace)
    return receipt


def validate_audit_receipt(
    workspace: Path,
    receipt: Mapping[str, object],
) -> list[str]:
    workspace = Path(workspace).expanduser().resolve()
    mismatches: list[str] = []
    expected = {
        "schema_fingerprint": active_schema_fingerprint(workspace),
        "content_tree_hash": content_tree_hash(workspace),
    }
    if "vector_gate_hash" in receipt:
        expected["vector_gate_hash"] = vector_gate_hash(workspace)
    if "file_manifest" in receipt:
        expected["file_manifest"] = content_file_manifest(workspace)
    for field, value in expected.items():
        if receipt.get(field) != value:
            mismatches.append(field)
    return mismatches
