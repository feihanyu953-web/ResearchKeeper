"""Generate bibliography-backed frontmatter candidates without writing notes."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Mapping

import yaml

from rsk.kb.bibliography import (
    BIBLIOGRAPHY_CATEGORY,
    BIBLIOGRAPHY_METRIC,
    literature_module,
)
from rsk.vector.claims import parse_schema_rows


FRONTMATTER_FIELDS = (
    "title",
    "authors",
    "year",
    "journal",
    "doi",
    "corresponding_authors",
    "first_author_affiliation",
    "corresponding_affiliations",
    "kb_literature_record",
)
_NOTE_TO_FRONTMATTER_FIELDS = FRONTMATTER_FIELDS[:-1]


def _empty_candidate() -> dict[str, object]:
    return {field: None for field in FRONTMATTER_FIELDS}


def _diagnostic(field: str, code: str, message: str) -> dict[str, str]:
    return {
        "field": field,
        "code": code,
        "message": message,
    }


def _is_missing(value: object) -> bool:
    return value is None or value == "" or value == [] or value == ()


def build_frontmatter_candidate(
    workspace: Path,
    paper_id: str,
) -> dict[str, object]:
    """Return managed frontmatter fields and field-level evidence gaps."""
    root = Path(workspace).expanduser().resolve()
    paper_id = str(paper_id).strip()
    if not paper_id:
        raise ValueError("paper_id is required")
    module = literature_module(root)
    path = root / "kb" / str(module["file"])
    matches = [
        record
        for record in parse_schema_rows(path)
        if (
            record.get("paper_id") == paper_id
            and record.get("module") == str(module["name"])
            and record.get("category") == BIBLIOGRAPHY_CATEGORY
            and record.get("metric") == BIBLIOGRAPHY_METRIC
        )
    ]
    if len(matches) != 1:
        code = (
            "missing_bibliography_record"
            if not matches
            else "duplicate_bibliography_records"
        )
        message = (
            f"{paper_id}: no bibliographic metadata record in the active "
            "literature role"
            if not matches
            else f"{paper_id}: multiple bibliographic metadata records"
        )
        return {
            "mode": "candidate",
            "paper_id": paper_id,
            "candidate": _empty_candidate(),
            "diagnostics": [
                _diagnostic(field, code, message)
                for field in FRONTMATTER_FIELDS
            ],
        }

    record = matches[0]
    try:
        note = json.loads(str(record.get("note", "")))
    except json.JSONDecodeError:
        note = None
    if not isinstance(note, dict):
        return {
            "mode": "candidate",
            "paper_id": paper_id,
            "candidate": _empty_candidate(),
            "diagnostics": [
                _diagnostic(
                    field,
                    "invalid_bibliography_note",
                    f"{paper_id}: bibliography note is not a JSON object",
                )
                for field in FRONTMATTER_FIELDS
            ],
        }

    candidate = {
        field: note.get(field)
        for field in _NOTE_TO_FRONTMATTER_FIELDS
    }
    candidate["kb_literature_record"] = record["record_id"]
    diagnostics = [
        _diagnostic(
            field,
            "missing_bibliography_value",
            f"{paper_id}: bibliography field {field} lacks verified evidence",
        )
        for field, value in candidate.items()
        if _is_missing(value)
    ]
    return {
        "mode": "candidate",
        "paper_id": paper_id,
        "candidate": candidate,
        "diagnostics": diagnostics,
    }


def diff_frontmatter(
    existing: Mapping[str, object],
    candidate_result: Mapping[str, object],
) -> dict[str, object]:
    """Compare managed candidates without modifying the existing mapping."""
    raw_candidate = candidate_result.get("candidate")
    if not isinstance(raw_candidate, Mapping):
        raise ValueError("candidate_result.candidate must be an object")
    add: dict[str, object] = {}
    unchanged: dict[str, object] = {}
    conflicts: dict[str, dict[str, object]] = {}
    preserved: dict[str, object] = {}
    handled: set[str] = set()

    for field in FRONTMATTER_FIELDS:
        value = raw_candidate.get(field)
        if _is_missing(value):
            if field in existing:
                preserved[field] = existing[field]
                handled.add(field)
            continue
        if field not in existing:
            add[field] = value
        elif existing[field] == value:
            unchanged[field] = value
            handled.add(field)
        else:
            conflicts[field] = {
                "existing": existing[field],
                "candidate": value,
            }
            handled.add(field)
    for field, value in existing.items():
        if field not in handled and field not in add:
            preserved[field] = value

    return {
        "mode": "diff",
        "paper_id": candidate_result.get("paper_id"),
        "add": add,
        "unchanged": unchanged,
        "conflicts": conflicts,
        "preserved": preserved,
        "diagnostics": list(candidate_result.get("diagnostics") or ()),
    }


def load_existing_frontmatter(path: Path) -> dict[str, object]:
    """Read YAML or the first YAML frontmatter block from Markdown."""
    source = Path(path).expanduser().resolve()
    text = source.read_text(encoding="utf-8")
    lines = text.splitlines()
    if lines and lines[0].strip() == "---":
        try:
            closing = next(
                index
                for index, line in enumerate(lines[1:], start=1)
                if line.strip() == "---"
            )
        except StopIteration as exc:
            raise ValueError(
                f"unterminated YAML frontmatter: {source}"
            ) from exc
        text = "\n".join(lines[1:closing])
    payload = yaml.safe_load(text) or {}
    if not isinstance(payload, dict):
        raise ValueError(f"frontmatter must be an object: {source}")
    return {str(key): value for key, value in payload.items()}
