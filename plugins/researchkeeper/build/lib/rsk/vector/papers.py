"""Build one deterministic discovery abstract per paper."""

from __future__ import annotations

from collections import defaultdict
from pathlib import Path
import sys
from typing import TextIO

from rsk.kb.coverage import active_modules
from rsk.vector.claims import parse_schema_rows


_EMPTY_VALUES = frozenset(
    {
        "",
        "-",
        "n/a",
        "na",
        "none",
        "not available",
        "unknown",
        "无",
        "未报告",
    }
)
_BIBLIOGRAPHY_CATEGORIES = frozenset(
    {
        "bibliographic metadata",
        "bibliographic_metadata",
        "bibliography",
        "文献信息",
    }
)
_ABSTRACT_MARKERS = frozenset(
    {
        "abstract",
        "core contribution",
        "core_contribution",
        "paper abstract",
        "paper index",
        "contribution",
        "摘要",
        "核心贡献",
        "论文摘要",
        "论文索引",
        "索引",
    }
)


def _normalized(value: object) -> str:
    return " ".join(str(value or "").strip().casefold().split())


def _meaningful(value: object) -> bool:
    return _normalized(value) not in _EMPTY_VALUES


def _is_bibliography(record: dict[str, str]) -> bool:
    return (
        _normalized(record.get("category")) in _BIBLIOGRAPHY_CATEGORIES
        or _normalized(record.get("metric")) == "bibliographic_metadata"
    )


def _explicit_abstract(record: dict[str, str]) -> str | None:
    """Return an explicitly identified abstract/contribution, never a title."""
    if _is_bibliography(record):
        return None
    category = _normalized(record.get("category"))
    metric = _normalized(record.get("metric"))
    if category not in _ABSTRACT_MARKERS and metric not in _ABSTRACT_MARKERS:
        return None
    for field in ("value", "note"):
        candidate = str(record.get(field, "") or "").strip()
        if _meaningful(candidate) and len(candidate) >= 30:
            return candidate
    return None


def _paper_title(records: list[dict[str, str]]) -> str | None:
    for record in records:
        if not _is_bibliography(record):
            continue
        title = str(record.get("subject", "") or "").strip()
        if _meaningful(title):
            return title
    return None


def _fact_text(record: dict[str, str]) -> str | None:
    if _is_bibliography(record):
        return None
    subject = str(record.get("subject", "") or "").strip()
    metric = str(record.get("metric", "") or "").strip()
    value = str(record.get("value", "") or "").strip()
    unit = str(record.get("unit", "") or "").strip()
    condition = str(record.get("condition", "") or "").strip()
    note = str(record.get("note", "") or "").strip()

    parts: list[str] = []
    if _meaningful(subject):
        parts.append(subject)
    if _meaningful(metric) or _meaningful(value):
        measurement = metric if _meaningful(metric) else "value"
        if _meaningful(value):
            measurement += f"={value}"
        if _meaningful(unit):
            measurement += f" {unit}"
        parts.append(measurement)
    if _meaningful(condition):
        parts.append(f"condition={condition}")
    if len(parts) < 2 and _meaningful(note):
        parts.append(note)
    if not parts:
        return None
    return ": ".join(parts[:2]) + (
        "; " + "; ".join(parts[2:]) if len(parts) > 2 else ""
    )


def _truncate(text: str, max_chars: int) -> str:
    if len(text) <= max_chars:
        return text
    if max_chars < 4:
        return text[:max_chars]
    return text[: max_chars - 3].rstrip() + "..."


def build_paper_abstracts(
    workspace: Path,
    *,
    max_chars: int = 1200,
    stderr: TextIO | None = None,
) -> list[dict[str, object]]:
    """Aggregate all active concrete modules into paper-level abstracts.

    Explicit literature-role abstracts take priority. If none exists, every
    usable fact record is grouped in active schema order. Bibliographic records
    may supply a title but cannot, by themselves, produce an abstract.
    """
    root = Path(workspace).expanduser().resolve()
    modules = active_modules(root)
    records_by_paper: dict[str, list[dict[str, str]]] = defaultdict(list)
    module_order: list[str] = []
    role_by_module: dict[str, str] = {}
    literature_modules: set[str] = set()

    for module in modules:
        name = str(module["name"])
        role = str(module.get("role", ""))
        module_order.append(name)
        role_by_module[name] = role
        if role == "literature":
            literature_modules.add(name)
        path = root / "kb" / str(module["file"])
        if not path.is_file():
            continue
        for record in parse_schema_rows(path):
            paper_id = str(record.get("paper_id", "") or "").strip()
            if not paper_id:
                continue
            normalized_record = dict(record)
            normalized_record["module"] = name
            normalized_record["_role"] = role
            records_by_paper[paper_id].append(normalized_record)

    reports = stderr if stderr is not None else sys.stderr
    abstracts: list[dict[str, object]] = []
    for paper_id in sorted(records_by_paper):
        records = records_by_paper[paper_id]
        concrete_modules = [
            module
            for module in module_order
            if any(record["module"] == module for record in records)
        ]
        roles: list[str] = []
        for module in concrete_modules:
            role = role_by_module[module]
            if role and role not in roles:
                roles.append(role)

        explicit = next(
            (
                candidate
                for record in records
                if record["module"] in literature_modules
                for candidate in (_explicit_abstract(record),)
                if candidate
            ),
            None,
        )
        if explicit:
            abstract = f"[paper] {paper_id}. {explicit}"
        else:
            facts_by_module: dict[str, list[str]] = defaultdict(list)
            for record in records:
                fact = _fact_text(record)
                if fact:
                    facts_by_module[record["module"]].append(fact)
            if not any(facts_by_module.values()):
                print(
                    f"[SKIP] {paper_id}: no usable fact records for "
                    "paper abstract",
                    file=reports,
                )
                continue
            title = _paper_title(records)
            header = f"[paper] {paper_id}."
            if title:
                header += f" {title}."
            lines = [header]
            for module in module_order:
                role = role_by_module[module]
                for fact in facts_by_module.get(module, ()):
                    lines.append(
                        f"[role:{role}; module:{module}] {fact}"
                    )
            abstract = "\n".join(lines)

        abstracts.append(
            {
                "paper_id": paper_id,
                "abstract": _truncate(abstract, max_chars),
                "roles": roles,
                "module_names": concrete_modules,
                "n_records": len(records),
            }
        )
    return abstracts
