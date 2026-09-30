"""Structured per-paper coverage metadata for active schema modules."""

from __future__ import annotations

from dataclasses import dataclass
import io
import os
from pathlib import Path
import re
import tempfile
from types import MappingProxyType
from typing import Any, Mapping

import yaml


COVERAGE_STATUSES = frozenset({"covered", "not_applicable", "missing"})


class CoverageError(ValueError):
    """Raised when coverage metadata violates the active schema."""


@dataclass(frozen=True)
class CoverageEntry:
    status: str
    reason: str = ""
    evidence_checked: tuple[str, ...] = ()
    record_ids: tuple[str, ...] = ()

    def as_dict(self) -> dict[str, object]:
        payload: dict[str, object] = {"status": self.status}
        if self.record_ids:
            payload["record_ids"] = list(self.record_ids)
        if self.reason:
            payload["reason"] = self.reason
        if self.evidence_checked:
            payload["evidence_checked"] = list(self.evidence_checked)
        return payload


@dataclass(frozen=True)
class PaperCoverage:
    paper_id: str
    modules: Mapping[str, CoverageEntry]


def load_active_schema(workspace: Path) -> dict[str, Any]:
    """Load the workspace-owned schema profile without consulting globals."""
    path = Path(workspace) / "schemas" / "generated" / "modules.yaml"
    try:
        payload = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except (OSError, yaml.YAMLError) as exc:
        raise CoverageError(f"cannot read active modules: {exc}") from exc
    if not isinstance(payload, dict):
        raise CoverageError("active schema must be an object")
    modules = payload.get("modules")
    if not isinstance(modules, list):
        raise CoverageError("active modules must be a list")
    return payload


def active_modules(workspace: Path) -> tuple[dict[str, Any], ...]:
    """Return concrete modules in their authoritative configured order."""
    payload = load_active_schema(workspace)
    modules = []
    for module in payload["modules"]:
        if not isinstance(module, dict):
            raise CoverageError("active module must be an object")
        name = str(module.get("name", ""))
        file = str(module.get("file", ""))
        if not name or not file:
            raise CoverageError("active module requires name and file")
        modules.append(dict(module))
    return tuple(modules)


def active_module_map(workspace: Path) -> dict[str, str]:
    result: dict[str, str] = {}
    for module in active_modules(workspace):
        result[str(module["name"])] = str(module["file"])
    return result


def build_coverage(
    *,
    workspace: Path,
    paper_id: str,
    declarations: Mapping[str, Mapping[str, Any]],
    assigned_record_ids: Mapping[str, tuple[str, ...]] | None = None,
) -> PaperCoverage:
    module_map = active_module_map(workspace)
    declared = set(declarations)
    active = set(module_map)
    if declared != active:
        missing = sorted(active - declared)
        extra = sorted(declared - active)
        details = []
        if missing:
            details.append("missing modules: " + ", ".join(missing))
        if extra:
            details.append("unknown modules: " + ", ".join(extra))
        raise CoverageError("; ".join(details))

    assigned = assigned_record_ids or {}
    entries: dict[str, CoverageEntry] = {}
    for module in module_map:
        raw = declarations[module]
        if not isinstance(raw, Mapping):
            raise CoverageError(f"{module}: coverage entry must be an object")
        status = str(raw.get("status", ""))
        if status not in COVERAGE_STATUSES:
            raise CoverageError(f"{module}: unknown coverage status {status!r}")
        reason = str(raw.get("reason", "")).strip()
        evidence = tuple(
            str(item).strip()
            for item in (raw.get("evidence_checked") or ())
            if str(item).strip()
        )
        record_ids = tuple(
            str(item).strip()
            for item in (
                raw.get("record_ids")
                or assigned.get(module)
                or ()
            )
            if str(item).strip()
        )
        if status == "covered" and not record_ids:
            raise CoverageError(
                f"{module}: covered requires at least one real record ID"
            )
        if status == "not_applicable" and (not reason or not evidence):
            raise CoverageError(
                f"{module}: not_applicable requires reason and evidence_checked"
            )
        entries[module] = CoverageEntry(
            status=status,
            reason=reason,
            evidence_checked=evidence,
            record_ids=record_ids,
        )
    return PaperCoverage(
        paper_id=paper_id,
        modules=MappingProxyType(entries),
    )


def coverage_path(workspace: Path, paper_id: str) -> Path:
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]*", paper_id):
        raise CoverageError(f"unsafe paper_id: {paper_id!r}")
    return Path(workspace) / "kb" / "coverage" / f"{paper_id}.md"


def write_coverage(workspace: Path, coverage: PaperCoverage) -> Path:
    path = coverage_path(workspace, coverage.paper_id)
    path.parent.mkdir(parents=True, exist_ok=True)
    document = render_coverage_document(coverage)
    temporary: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir=path.parent,
            prefix=f".{coverage.paper_id}-",
            suffix=".tmp",
            delete=False,
        ) as handle:
            handle.write(document)
            handle.flush()
            os.fsync(handle.fileno())
            temporary = Path(handle.name)
        os.replace(temporary, path)
    finally:
        if temporary is not None and temporary.exists():
            temporary.unlink()
    return path


def render_coverage_document(coverage: PaperCoverage) -> str:
    """Serialize coverage without mutating the workspace."""
    payload = {
        "coverage_version": 1,
        "paper_id": coverage.paper_id,
        "modules": {
            name: entry.as_dict()
            for name, entry in coverage.modules.items()
        },
    }
    handle = io.StringIO()
    handle.write("# ResearchKeeper paper coverage\n")
    yaml.safe_dump(
        payload,
        handle,
        allow_unicode=True,
        sort_keys=False,
    )
    return handle.getvalue()


def load_coverage(workspace: Path, paper_id: str) -> PaperCoverage:
    path = coverage_path(workspace, paper_id)
    try:
        payload = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except (OSError, yaml.YAMLError) as exc:
        raise CoverageError(f"cannot read coverage for {paper_id}: {exc}") from exc
    if payload.get("paper_id") != paper_id:
        raise CoverageError(f"coverage paper_id mismatch for {paper_id}")
    raw_modules = payload.get("modules")
    if not isinstance(raw_modules, dict):
        raise CoverageError(f"coverage modules missing for {paper_id}")
    entries = {
        str(name): CoverageEntry(
            status=str(raw.get("status", "")),
            reason=str(raw.get("reason", "")),
            evidence_checked=tuple(raw.get("evidence_checked") or ()),
            record_ids=tuple(raw.get("record_ids") or ()),
        )
        for name, raw in raw_modules.items()
        if isinstance(raw, dict)
    }
    return PaperCoverage(
        paper_id=paper_id,
        modules=MappingProxyType(entries),
    )


def _record_ids_for_paper(path: Path, paper_id: str) -> set[str]:
    if not path.is_file():
        return set()
    result = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.lstrip().startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) >= 4 and cells[2] == paper_id:
            result.add(cells[0])
    return result


def validate_coverage(
    workspace: Path,
    coverage: PaperCoverage,
) -> tuple[list[str], tuple[str, ...], int]:
    errors: list[str] = []
    reviewer_required: list[str] = []
    record_count = 0
    module_map = active_module_map(workspace)
    if set(coverage.modules) != set(module_map):
        errors.append("coverage declarations do not match active modules")
        return errors, (), 0
    for module, file in module_map.items():
        entry = coverage.modules[module]
        if entry.status not in COVERAGE_STATUSES:
            errors.append(f"{module}: invalid coverage status")
        elif entry.status == "missing":
            errors.append(f"{module}: applicable content is missing")
        elif entry.status == "not_applicable":
            if not entry.reason or not entry.evidence_checked:
                errors.append(
                    f"{module}: not_applicable lacks reason or evidence"
                )
            else:
                reviewer_required.append(module)
        elif entry.status == "covered":
            actual = _record_ids_for_paper(
                Path(workspace) / "kb" / file,
                coverage.paper_id,
            )
            missing_ids = set(entry.record_ids) - actual
            if not entry.record_ids or missing_ids:
                errors.append(
                    f"{module}: covered record IDs are missing from kb/{file}"
                )
            else:
                record_count += len(entry.record_ids)
    return errors, tuple(reviewer_required), record_count
