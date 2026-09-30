"""Backward-compatible phase-A parsing for record source strings."""

from __future__ import annotations

import re


_LOCATION_PATTERN = re.compile(
    r"(?:"
    r"PDF\s+front\s+matter|Zotero\s+metadata|DOI\s+metadata|"
    r"Supplementary\s+Information|Supplementary\s+Methods|"
    r"Experimental\s+Section|Conclusions?|Mechanistic\s+Studies|"
    r"Figure?\.?\s*[A-Za-z]?\d+[A-Za-z]?|"
    r"Fig\.?\s*[A-Za-z]?\d+[A-Za-z]?|"
    r"Table\s*[A-Za-z]?\d+[A-Za-z]?|"
    r"Scheme\s*S?\d+[A-Za-z]?|"
    r"Eq(?:uation)?\.?\s*S?\d+[A-Za-z]?|"
    r"Section\s*[A-Za-z]?\d+(?:\.\d+)*|"
    r"Methods?|Results?|Discussion|Abstract|"
    r"\bSI(?:\s*[A-Za-z]?\d+)?\b|"
    r"图\s*[A-Za-z]?\d+[A-Za-z]?|"
    r"表\s*[A-Za-z]?\d+[A-Za-z]?|"
    r"第?\s*\d+(?:\.\d+)*\s*节|"
    r"补充信息|补充方法|方法|全文|摘要|讨论段|"
    r"引言|绪论|讨论|结论"
    r")",
    flags=re.IGNORECASE,
)
_YEAR_PATTERN = re.compile(r"\b((?:19|20)\d{2})\b")
_PAPER_ID_PATTERN = re.compile(
    r"^(?P<author>[A-Za-z][A-Za-z-]*)(?P<year>(?:19|20)\d{2})"
)
_BIBLIOGRAPHY_LOCATIONS = frozenset(
    {
        "pdf front matter",
        "zotero metadata",
        "doi metadata",
    }
)


def _locations(raw: str) -> list[str]:
    result: list[str] = []
    seen: set[str] = set()
    for match in _LOCATION_PATTERN.finditer(raw):
        location = " ".join(match.group(0).split())
        key = location.casefold()
        if key not in seen:
            result.append(location)
            seen.add(key)
    return result


def parse_source(source: object) -> dict[str, object]:
    """Parse identity and locations while retaining every legacy raw string."""
    raw = str(source or "").strip()
    content = raw.strip("[]").strip()
    locations = _locations(content)
    segments = [
        segment.strip()
        for segment in content.split(",")
        if segment.strip()
    ]
    non_locations = [
        segment
        for segment in segments
        if not _LOCATION_PATTERN.search(segment)
    ]

    author = ""
    year = ""
    journal = ""
    identity_index: int | None = None
    if non_locations:
        paper_id_match = _PAPER_ID_PATTERN.match(non_locations[0])
        match = _YEAR_PATTERN.search(non_locations[0])
        if paper_id_match:
            author = paper_id_match.group("author")
            year = paper_id_match.group("year")
            identity_index = 0
        elif match:
            author = non_locations[0][: match.start()].strip(" ,;:-")
            year = match.group(1)
            identity_index = 0
        elif len(non_locations) > 1:
            match = _YEAR_PATTERN.fullmatch(non_locations[1])
            if match:
                author = non_locations[0].strip(" ,;:-")
                year = match.group(1)
                identity_index = 1
    if identity_index is not None:
        journal_candidates = non_locations[identity_index + 1 :]
        if journal_candidates:
            journal = journal_candidates[0]

    warnings = []
    if not raw:
        warnings.append("source is empty")
    elif not locations:
        warnings.append("source has no recognized location")
    if (
        raw
        and not author
        and not year
        and not any(
            location.casefold() in _BIBLIOGRAPHY_LOCATIONS
            for location in locations
        )
    ):
        warnings.append("source has no recognized paper identifier")
    return {
        "author": author,
        "year": year,
        "journal": journal,
        "locations": locations,
        "raw": raw,
        "warnings": warnings,
    }


def _identifies_paper(
    parsed: dict[str, object],
    *,
    paper_id: str,
    bibliography: bool,
) -> bool:
    raw = str(parsed["raw"])
    if paper_id.casefold() in raw.casefold():
        return True
    paper_match = _PAPER_ID_PATTERN.match(paper_id)
    if paper_match:
        expected_author = paper_match.group("author").casefold()
        expected_year = paper_match.group("year")
        author = str(parsed["author"]).casefold()
        if author.startswith(expected_author) and parsed["year"] == expected_year:
            return True
    if bibliography:
        return any(
            location.casefold() in {"zotero metadata", "doi metadata"}
            for location in parsed["locations"]
        )
    return False


def validate_source_for_write(
    source: object,
    *,
    paper_id: str,
    bibliography: bool = False,
) -> list[str]:
    """Validate new writes without rejecting legacy strings during reads."""
    parsed = parse_source(source)
    errors = []
    if not _identifies_paper(
        parsed,
        paper_id=str(paper_id),
        bibliography=bibliography,
    ):
        errors.append("source requires a paper identifier")
    if not parsed["locations"]:
        errors.append("source requires a recognized location")
    return errors
