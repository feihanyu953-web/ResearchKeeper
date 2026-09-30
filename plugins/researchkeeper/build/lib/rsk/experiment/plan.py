"""Generate a dynamic-schema reproduction plan from KB evidence."""

from __future__ import annotations

from pathlib import Path
import re
from typing import Iterable

from rsk.kb.coverage import active_modules
from rsk.vector.claims import parse_schema_rows


_MISSING = frozenset({"", "none", "n/a", "na", "unknown", "无", "未报告"})
_ROLE_PROMPTS = {
    "entities": (
        "Material, reactant, or system identity",
        ("material", "sample", "entity", "species", "材料", "样品", "物种"),
    ),
    "methods": (
        "Experimental or preparation method",
        (
            "method",
            "protocol",
            "procedure",
            "synthesis",
            "preparation",
            "方法",
            "步骤",
            "制备",
            "合成",
        ),
    ),
    "conditions": (
        "Operating and measurement conditions",
        (
            "condition",
            "temperature",
            "pressure",
            "potential",
            "electrolyte",
            "条件",
            "温度",
            "压力",
            "电位",
        ),
    ),
    "results": (
        "Target outcome and checkpoint",
        (
            "result",
            "outcome",
            "yield",
            "performance",
            "selectivity",
            "结果",
            "产率",
            "性能",
        ),
    ),
    "relations": (
        "Mechanistic or relational hypothesis",
        (
            "mechanism",
            "relation",
            "pathway",
            "hypothesis",
            "机理",
            "关系",
            "路径",
        ),
    ),
    "claims": (
        "Claim, limitation, and validation target",
        (
            "claim",
            "limitation",
            "conclusion",
            "validation",
            "结论",
            "限制",
            "验证",
        ),
    ),
}
_NUMBER = r"[+-]?(?:\d+(?:\.\d*)?|\.\d+)"
_RANGE_PATTERN = re.compile(
    rf"(?P<first>{_NUMBER})\s*(?:-|–|—|to|至)\s*"
    rf"(?P<second>{_NUMBER})",
    flags=re.IGNORECASE,
)
_VALUE_PATTERN = re.compile(
    rf"(?P<comparator>>=|<=|>|<|≥|≤|约|大约|≈|~)?\s*"
    rf"(?P<value>{_NUMBER})"
)
_COMPARATOR_MAP = {
    "≥": ">=",
    "≤": "<=",
    "约": "approximately",
    "大约": "approximately",
    "≈": "approximately",
    "~": "approximately",
}
_COMPUTATIONAL_PATTERN = re.compile(
    r"(?:"
    r"\bDFT\b|\bdensity functional\b|\bVASP\b|\bCP2K\b|"
    r"\bQuantum ESPRESSO\b|\bAIMD\b|\bLAMMPS\b|"
    r"\bmolecular dynamics\b|\bk-?points?\b|\bENCUT\b|"
    r"\bPBE\b|\bRPBE\b|\bSCAN\b|\bB3LYP\b|"
    r"密度泛函|分子动力学|计算方法|泛函|截断能"
    r")",
    flags=re.IGNORECASE,
)


def _meaningful(value: object) -> bool:
    return str(value or "").strip().casefold() not in _MISSING


def _cell(value: object) -> str:
    text = " ".join(str(value or "").split())
    return text.replace("|", r"\|")


def _pick(
    records: Iterable[dict[str, object]],
    keywords: Iterable[str],
    *,
    fields: tuple[str, ...] = ("subject",),
) -> dict[str, object] | None:
    """Return the first keyword match, never an unrelated fallback."""
    materialized = list(records)
    for keyword in keywords:
        normalized_keyword = str(keyword).casefold()
        for record in materialized:
            for field in fields:
                if normalized_keyword in str(
                    record.get(field, "")
                ).casefold():
                    return record
    return None


def parse_numeric_value(text: object) -> dict[str, object] | None:
    """Parse a comparator or range without losing the original value."""
    raw = str(text or "").strip()
    if not raw:
        return None
    range_match = _RANGE_PATTERN.search(raw)
    if range_match:
        return {
            "raw": raw,
            "comparator": None,
            "values": [
                float(range_match.group("first")),
                float(range_match.group("second")),
            ],
            "is_range": True,
            "unit": raw[range_match.end() :].strip(" ,;"),
        }
    value_match = _VALUE_PATTERN.search(raw)
    if not value_match:
        return None
    comparator = value_match.group("comparator")
    comparator = _COMPARATOR_MAP.get(comparator, comparator)
    return {
        "raw": raw,
        "comparator": comparator,
        "values": [float(value_match.group("value"))],
        "is_range": False,
        "unit": raw[value_match.end() :].strip(" ,;"),
    }


def collect_records(
    workspace: Path,
    paper_id: str,
) -> tuple[dict[str, object], ...]:
    """Collect a paper from every active concrete module in schema order."""
    root = Path(workspace).expanduser().resolve()
    paper_id = str(paper_id).strip()
    collected = []
    for module in active_modules(root):
        name = str(module["name"])
        display = str(module.get("display", "") or name)
        role = str(module.get("role", ""))
        file = str(module["file"])
        path = root / "kb" / file
        if not path.is_file():
            continue
        for record in parse_schema_rows(path):
            if str(record.get("paper_id", "")) != paper_id:
                continue
            collected.append(
                {
                    **record,
                    "_module_name": name,
                    "_module_display": display,
                    "_module_role": role,
                    "_source_file": file,
                }
            )
    return tuple(collected)


def _record_reference(record: dict[str, object] | None) -> str:
    if record is None:
        return "（待补充）"
    return (
        f"{record.get('record_id', '?')} | "
        f"{record.get('source', '（待补充）')}"
    )


def _record_value(record: dict[str, object]) -> str:
    value = str(record.get("value", "") or "").strip()
    unit = str(record.get("unit", "") or "").strip()
    if _meaningful(unit) and unit not in value:
        value = f"{value} {unit}".strip()
    return value if _meaningful(value) else "（待补充）"


def _is_computational(record: dict[str, object]) -> bool:
    evidence = " ".join(
        str(record.get(field, "") or "")
        for field in (
            "category",
            "subject",
            "metric",
            "value",
            "condition",
            "note",
        )
    )
    return bool(_COMPUTATIONAL_PATTERN.search(evidence))


def generate_plan(workspace: Path, paper_id: str) -> str | None:
    """Render a read-only Markdown plan with record/source traceability."""
    records = collect_records(workspace, paper_id)
    if not records:
        return None
    by_role: dict[str, list[dict[str, object]]] = {}
    by_module: dict[str, list[dict[str, object]]] = {}
    module_metadata: dict[str, tuple[str, str]] = {}
    for record in records:
        role = str(record["_module_role"])
        module = str(record["_module_name"])
        by_role.setdefault(role, []).append(record)
        by_module.setdefault(module, []).append(record)
        module_metadata[module] = (
            str(record["_module_display"]),
            role,
        )

    lines = [
        f"# Experiment reproduction plan: {paper_id}",
        "",
        "> Candidate generated only from active-schema KB records. "
        "Missing values remain explicit evidence gaps.",
        "",
        "## Role-driven reproduction checklist",
        "",
        "| Semantic role | Required item | Evidence |",
        "|---|---|---|",
    ]
    search_fields = (
        "subject",
        "category",
        "metric",
        "value",
        "condition",
        "note",
    )
    for role, (label, keywords) in _ROLE_PROMPTS.items():
        selected = _pick(
            by_role.get(role, ()),
            keywords,
            fields=search_fields,
        )
        lines.append(
            f"| `{role}` | {label} | {_cell(_record_reference(selected))} |"
        )

    lines.extend(["", "## Evidence by concrete module", ""])
    for module, module_records in by_module.items():
        display, role = module_metadata[module]
        lines.extend(
            [
                f"### {display} (`{module}`, role: `{role}`)",
                "",
                "| record_id | subject | metric and value | condition | source |",
                "|---|---|---|---|---|",
            ]
        )
        for record in module_records:
            metric = str(record.get("metric", "") or "").strip()
            measured = _record_value(record)
            lines.append(
                f"| {_cell(record.get('record_id'))} | "
                f"{_cell(record.get('subject'))} | "
                f"{_cell(metric)} = {_cell(measured)} | "
                f"{_cell(record.get('condition'))} | "
                f"{_cell(record.get('source'))} |"
            )
        lines.append("")

    computational = [
        record
        for record in by_role.get("methods", ())
        if _is_computational(record)
    ]
    if computational:
        lines.extend(
            [
                "## Computational reproduction",
                "",
                "This section exists because explicit computational-method "
                "records were found.",
                "",
                "| record_id | method evidence | value | source |",
                "|---|---|---|---|",
            ]
        )
        for record in computational:
            lines.append(
                f"| {_cell(record.get('record_id'))} | "
                f"{_cell(record.get('subject'))}: "
                f"{_cell(record.get('metric'))} | "
                f"{_cell(_record_value(record))} | "
                f"{_cell(record.get('source'))} |"
            )
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"
