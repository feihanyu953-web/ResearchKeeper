"""Schema-driven bibliographic records for paper identity and provenance."""

from __future__ import annotations

from dataclasses import dataclass
import json
import os
from pathlib import Path
import re
import tempfile
from typing import Any, Mapping

from rsk.kb.coverage import CoverageError, active_modules


BIBLIOGRAPHY_CATEGORY = "文献信息"
BIBLIOGRAPHY_METRIC = "bibliographic_metadata"
BIBLIOGRAPHY_NOTE_KEYS = (
    "title",
    "authors",
    "corresponding_authors",
    "journal",
    "year",
    "doi",
    "first_author_affiliation",
    "corresponding_affiliations",
    "affiliation_source",
    "verification",
)


@dataclass(frozen=True)
class BibliographyUpsertResult:
    record_id: str
    created: bool
    path: Path


def literature_module(workspace: Path) -> dict[str, Any]:
    """Resolve the unique concrete module carrying the literature role."""
    matches = [
        module
        for module in active_modules(workspace)
        if str(module.get("role", "")) == "literature"
    ]
    if len(matches) != 1:
        raise CoverageError(
            "active schema requires exactly one literature role; "
            f"found {len(matches)}"
        )
    return matches[0]


def _string_list(value: object, *, field: str) -> list[str]:
    if value is None:
        return []
    if not isinstance(value, (list, tuple)):
        raise ValueError(f"bibliography.{field} must be a list")
    return [str(item).strip() for item in value if str(item).strip()]


def _nullable_string(value: object) -> str | None:
    if value is None:
        return None
    text = str(value).strip()
    return text or None


def _crossref_affiliation(doi: str, timeout: int = 10) -> tuple[str | None, list[str]]:
    """Try Crossref API for first-author affiliation ONLY.

    Returns (first_author_affiliation, [corresponding_affiliations]).
    corresponding_affiliations is ALWAYS empty from this function — Crossref
    author lists do not reliably tag corresponding authors, and treating all
    author affiliations as corresponding is deterministic metadata pollution.

    first_author_affiliation is taken from authors[0] (the actual first author
    in publication order), NOT from "the first author who happens to have an
    affiliation entry in Crossref data".
    """
    if not doi or not doi.strip():
        return None, []
    try:
        import urllib.request
        import urllib.error
        url = f"https://api.crossref.org/works/{doi.strip()}"
        req = urllib.request.Request(
            url,
            headers={"User-Agent": "ResearchKeeper/0.2 (mailto:nobody@example.com)"},
        )
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except Exception:
        return None, []

    msg = data.get("message", {})
    authors = msg.get("author", [])

    # Only use the actual first author (index 0) — never fall through
    # to later authors if the first author has no affiliation entry.
    first_aff: str | None = None
    if authors:
        first_author = authors[0]
        affs = first_author.get("affiliation", [])
        for aff in affs:
            name = str(aff.get("name", "")).strip()
            if name and "orcid" not in name.lower():
                first_aff = name
                break

    # We do NOT auto-fill corresponding_affiliations from Crossref.
    # The author list's "sequence" field is not a reliable corresponding-
    # author marker, and polluting the record with all author affiliations
    # is worse than leaving it empty for the user to fill.
    return first_aff, []


def normalize_bibliography(
    bibliography: Mapping[str, object],
) -> dict[str, object]:
    """Return the fixed public bibliography note without inferred facts."""
    title = str(bibliography.get("title", "")).strip()
    source = str(bibliography.get("source", "")).strip()
    verification = str(bibliography.get("verification", "")).strip()
    if not title:
        raise ValueError("bibliography.title is required")
    if not source:
        raise ValueError("bibliography.source is required")
    if not verification:
        raise ValueError("bibliography.verification is required")
    year_value = bibliography.get("year")
    if year_value in (None, ""):
        year: int | str | None = None
    elif isinstance(year_value, int):
        year = year_value
    else:
        year = str(year_value).strip() or None
    return {
        "title": title,
        "authors": _string_list(
            bibliography.get("authors"),
            field="authors",
        ),
        "corresponding_authors": _string_list(
            bibliography.get("corresponding_authors"),
            field="corresponding_authors",
        ),
        "journal": str(bibliography.get("journal", "")).strip(),
        "year": year,
        "doi": _nullable_string(bibliography.get("doi")),
        "first_author_affiliation": _nullable_string(
            bibliography.get("first_author_affiliation")
        ),
        "corresponding_affiliations": _string_list(
            bibliography.get("corresponding_affiliations"),
            field="corresponding_affiliations",
        ),
        "affiliation_source": str(
            bibliography.get("affiliation_source", "not_looked_up")
        ),
        "verification": verification,
    }


def build_bibliography_record(
    *,
    workspace: Path,
    paper_id: str,
    bibliography: Mapping[str, object],
) -> dict[str, object]:
    """Build one 13-column record for the active literature module."""
    paper_id = str(paper_id).strip()
    if not paper_id:
        raise ValueError("paper_id is required")
    module = literature_module(workspace)
    note = normalize_bibliography(bibliography)

    # Auto-fill first-author affiliation from Crossref if not provided.
    # We do NOT auto-fill corresponding_affiliations — Crossref cannot
    # reliably distinguish corresponding authors from co-authors.
    doi = str(bibliography.get("doi", "")).strip()
    if doi and not note.get("first_author_affiliation"):
        first_aff, _corr_affs = _crossref_affiliation(doi)
        if first_aff:
            note["first_author_affiliation"] = first_aff
            note["affiliation_source"] = "Crossref API"

    compact = [
        str(note["journal"]).strip(),
        str(note["year"]) if note["year"] is not None else "",
        f"DOI: {note['doi']}" if note["doi"] is not None else "DOI: unavailable",
    ]
    return {
        "paper_id": paper_id,
        "module": str(module["name"]),
        "schema_version": "schema_v1",
        "category": BIBLIOGRAPHY_CATEGORY,
        "subject": str(note["title"]),
        "metric": BIBLIOGRAPHY_METRIC,
        "value": "; ".join(item for item in compact if item),
        "unit": "无",
        "condition": "bibliographic identity verification",
        "source": str(bibliography["source"]).strip(),
        "confidence": str(
            bibliography.get("confidence", "single_source")
        ).strip()
        or "single_source",
        "note": json.dumps(
            note,
            ensure_ascii=False,
            separators=(",", ":"),
        ),
    }


def _row_cells(line: str) -> list[str] | None:
    if not line.lstrip().startswith("|"):
        return None
    cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
    return cells if len(cells) >= 13 else None


def _atomic_write(path: Path, text: str) -> None:
    temporary: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            newline="\n",
            dir=path.parent,
            prefix=f".{path.stem}-",
            suffix=".tmp",
            delete=False,
        ) as handle:
            handle.write(text)
            handle.flush()
            os.fsync(handle.fileno())
            temporary = Path(handle.name)
        os.replace(temporary, path)
    finally:
        if temporary is not None and temporary.exists():
            temporary.unlink()


def upsert_bibliography_record(
    *,
    workspace: Path,
    paper_id: str,
    bibliography: Mapping[str, object],
) -> BibliographyUpsertResult:
    """Create or replace the paper's unique bibliography row in place."""
    from rsk.kb.writer import _format_row

    workspace = Path(workspace).expanduser().resolve()
    module = literature_module(workspace)
    module_name = str(module["name"])
    path = workspace / "kb" / str(module["file"])
    record = build_bibliography_record(
        workspace=workspace,
        paper_id=paper_id,
        bibliography=bibliography,
    )
    lines = path.read_text(encoding="utf-8").splitlines()
    matches: list[tuple[int, str]] = []
    for index, line in enumerate(lines):
        cells = _row_cells(line)
        if (
            cells is not None
            and cells[2] == paper_id
            and cells[3] == module_name
            and cells[4] == BIBLIOGRAPHY_CATEGORY
            and cells[6] == BIBLIOGRAPHY_METRIC
        ):
            matches.append((index, cells[0]))
    if len(matches) > 1:
        raise ValueError(
            f"{paper_id}: duplicate bibliographic metadata records"
        )
    if matches:
        index, record_id = matches[0]
        lines[index] = _format_row(record, record_id).rstrip("\n")
        created = False
    else:
        existing_ids = [
            int(match.group(1))
            for line in lines
            if (
                match := re.match(
                    rf"^\|\s*{re.escape(module_name)}-(\d+)\s*\|",
                    line,
                )
            )
        ]
        record_id = f"{module_name}-{max(existing_ids, default=0) + 1:04d}"
        lines.append(_format_row(record, record_id).rstrip("\n"))
        created = True
    _atomic_write(path, "\n".join(lines) + "\n")
    return BibliographyUpsertResult(
        record_id=record_id,
        created=created,
        path=path,
    )
