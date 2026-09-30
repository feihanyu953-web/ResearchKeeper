"""Deterministic lexical scanning for explicit enumeration queries."""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path
import operator
import re
import unicodedata
from typing import Callable, Iterable, Sequence

from rsk.kb.coverage import active_modules
from rsk.vector.claims import parse_schema_rows


SCAN_FIELDS = (
    "subject",
    "category",
    "metric",
    "value",
    "condition",
    "note",
    "source",
)

_COMPARATORS: dict[str, Callable[[float, float], bool]] = {
    ">": operator.gt,
    ">=": operator.ge,
    "<": operator.lt,
    "<=": operator.le,
    "=": operator.eq,
}
_COMPARATOR_RE = re.compile(
    r"^\s*(>=|<=|>|<|=)\s*"
    r"([-+]?(?:\d+(?:\.\d*)?|\.\d+))\s*([^\d\s]*)\s*$"
)
_NUMBER_RE = re.compile(r"[-+]?(?:\d+(?:\.\d*)?|\.\d+)")


def normalize_text(value: object) -> str:
    """Normalize case, Unicode width, and common comparison symbols."""
    text = unicodedata.normalize("NFKC", str(value or "")).casefold()
    return (
        text.replace("≥", ">=")
        .replace("≤", "<=")
        .replace("≧", ">=")
        .replace("≦", "<=")
    )


def _numeric_constraint(keyword: str):
    match = _COMPARATOR_RE.fullmatch(normalize_text(keyword))
    if not match:
        return None
    comparator, raw_number, unit = match.groups()
    return _COMPARATORS[comparator], float(raw_number), unit


def _numeric_field_matches(
    value: object,
    constraint: tuple[Callable[[float, float], bool], float, str],
) -> bool:
    compare, target, required_unit = constraint
    normalized = normalize_text(value)
    if required_unit and required_unit not in normalized:
        return False
    return any(compare(float(number), target) for number in _NUMBER_RE.findall(normalized))


def _matched_fields(record: dict[str, object], keyword: str) -> list[str]:
    constraint = _numeric_constraint(keyword)
    if constraint is not None:
        return [
            field
            for field in SCAN_FIELDS
            if _numeric_field_matches(record.get(field, ""), constraint)
        ]
    needle = normalize_text(keyword).strip()
    if not needle:
        return []
    return [
        field
        for field in SCAN_FIELDS
        if needle in normalize_text(record.get(field, ""))
    ]


def _record_text(record: dict[str, object]) -> str:
    return " | ".join(
        f"{field}={str(record.get(field, '') or '').strip()}"
        for field in SCAN_FIELDS
        if str(record.get(field, "") or "").strip()
    )


def scan_records(
    workspace: Path,
    keywords: Sequence[str],
    *,
    match_all: bool = True,
) -> list[dict[str, object]]:
    """Scan every active module record using explicit lexical criteria.

    The result is deterministic and auditable, but is only a supplement to
    vector retrieval. Lexical matching is not proof of absolute completeness.
    """
    criteria = [str(keyword).strip() for keyword in keywords if str(keyword).strip()]
    if not criteria:
        raise ValueError("at least one non-empty scan keyword is required")

    root = Path(workspace)
    results: list[dict[str, object]] = []
    for configured in active_modules(root):
        module_name = str(configured["name"])
        role = str(configured.get("role", ""))
        module_file = str(configured["file"])
        path = root / "kb" / module_file
        if not path.is_file():
            raise FileNotFoundError(
                f"active module file is missing: {path}"
            )
        for record in parse_schema_rows(path):
            keyword_matches = [
                _matched_fields(record, keyword)
                for keyword in criteria
            ]
            selected = (
                all(keyword_matches)
                if match_all
                else any(keyword_matches)
            )
            if not selected:
                continue
            matched = [
                field
                for field in SCAN_FIELDS
                if any(field in fields for fields in keyword_matches)
            ]
            results.append(
                {
                    "record_id": record.get("record_id", ""),
                    "paper_id": record.get("paper_id", ""),
                    "module": module_name,
                    "role": role,
                    "matched_fields": matched,
                    "source": record.get("source", ""),
                    "source_file": f"kb/{module_file}",
                    "text": _record_text(record),
                }
            )
    return results


def merge_with_vector_results(
    vector_output: dict[str, object],
    lexical_results: Iterable[dict[str, object]],
) -> dict[str, object]:
    """Merge vector and lexical hits by record_id with provenance labels."""
    output = deepcopy(vector_output)
    vector_results = list(output.get("results", []))
    lexical = list(lexical_results)
    by_record: dict[str, dict[str, object]] = {}
    merged: list[dict[str, object]] = []

    for item in vector_results:
        candidate = dict(item)
        candidate["match_source"] = "vector"
        record_id = str(candidate.get("record_id", ""))
        if record_id:
            by_record[record_id] = candidate
        merged.append(candidate)

    for item in lexical:
        candidate = dict(item)
        record_id = str(candidate.get("record_id", ""))
        existing = by_record.get(record_id) if record_id else None
        if existing is not None:
            existing["match_source"] = "both"
            existing["matched_fields"] = list(
                candidate.get("matched_fields", [])
            )
            existing["lexical_source"] = candidate.get("source", "")
            continue
        candidate["chunk_id"] = record_id
        candidate["match_source"] = "lexical"
        merged.append(candidate)
        if record_id:
            by_record[record_id] = candidate

    for rank, item in enumerate(merged, start=1):
        item["rank"] = rank
    output["results"] = merged
    output["enumeration"] = {
        "mode": "vector_plus_lexical",
        "scan_fields": list(SCAN_FIELDS),
        "lexical_match_count": len(lexical),
        "merged_result_count": len(merged),
        "limitation": (
            "The deterministic lexical scan supplements vector retrieval; "
            "it is not proof of absolute completeness."
        ),
    }
    return output
