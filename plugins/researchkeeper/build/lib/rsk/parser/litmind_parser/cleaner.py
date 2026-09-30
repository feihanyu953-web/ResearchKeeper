"""
LitMind · 文本清洗器 — 页码/页眉页脚/噪声行/重复段落
"""

from __future__ import annotations

import re
from collections import Counter

PAGE_NUM_PATTERNS = [
    re.compile(r"^\s*\d+\s*$"),
    re.compile(r"^\s*-\s*\d+\s*-\s*$"),
    re.compile(r"^\s*\d+\s*of\s*\d+\s*$", re.I),
    re.compile(r"^\s*Page\s*\d+\s*$", re.I),
    re.compile(r"^\s*第\s*\d+\s*页\s*$"),
]

def _is_page_number(line: str) -> bool:
    for pat in PAGE_NUM_PATTERNS:
        if pat.match(line):
            return True
    return False

def _find_repeated_lines(pages: list[list[str]], threshold: float = 0.6) -> set[str]:
    if len(pages) < 3:
        return set()
    candidates: list[str] = []
    for page in pages:
        candidates.extend(page[:3])
        if len(page) > 3:
            candidates.extend(page[-3:])
    counter = Counter(candidates)
    min_count = max(2, int(len(pages) * threshold))
    return {line for line, count in counter.items() if count >= min_count}

def _remove_repeated_lines(text: str, repeated: set[str], lines_per_page: int = 3) -> str:
    blocks = text.split("\n\n")
    cleaned = []
    for block in blocks:
        lines = block.split("\n")
        if len(lines) <= lines_per_page and all(l.strip() in repeated for l in lines if l.strip()):
            continue
        cleaned.append(block)
    return "\n\n".join(cleaned)

def _deduplicate_paragraphs(text: str) -> str:
    paragraphs = text.split("\n\n")
    deduped = []
    prev = ""
    for para in paragraphs:
        stripped = para.strip()
        if stripped and stripped != prev:
            deduped.append(para)
            prev = stripped
        elif not stripped:
            deduped.append(para)
    return "\n\n".join(deduped)

NOISE_PATTERNS = [
    re.compile(r"^\s*doi:\s*10\.\S+", re.I),
    re.compile(r"^\s*(received|accepted|published)\s*:", re.I),
    re.compile(r"^\s*correspondence\s*(to|author)", re.I),
    re.compile(r"^\s*e[- ]?mail\s*:"),
    re.compile(r"^\s*copyright\s.*", re.I),
    re.compile(r"^\s*©\s"),
    re.compile(r"^\s*This\s+article\s+is\s+(an?\s+)?(open\s+access|protected|distributed)", re.I),
    re.compile(r"^\s*Author\s+(contributions|note)", re.I),
    re.compile(r"^\s*Conflict", re.I),
    re.compile(r"^\s*Funding", re.I),
    re.compile(r"^\s*Data\s+availability", re.I),
    re.compile(r"^\s*Supplementary", re.I),
    re.compile(r"^\s*Supporting\s+information", re.I),
    re.compile(r"^\s*Ethics", re.I),
]


CAPTION_PATTERN = re.compile(
    r"^\s*(?P<kind>fig(?:ure)?\.?|table)\s+"
    r"(?P<label>(?:S?\d+|[IVX]+)(?:[A-Za-z])?)"
    r"(?:\s*[\.\-:]\s*|\s+)",
    re.IGNORECASE,
)
SECTION_HEADING = re.compile(
    r"^\s*(?:abstract|introduction|methods?|results?|discussion|"
    r"conclusions?|references|acknowledg(?:e)?ments?)\s*$",
    re.IGNORECASE,
)


def _remove_noise_lines(text: str) -> str:
    lines = text.split("\n")
    cleaned = []
    for line in lines:
        if not line.strip():
            cleaned.append(line)
            continue
        if any(pat.match(line) for pat in NOISE_PATTERNS):
            continue
        cleaned.append(line)
    return "\n".join(cleaned)


def _extract_captions(text: str) -> tuple[str, str]:
    """Collect caption paragraphs while leaving every source line in place."""
    figure_captions: list[str] = []
    table_captions: list[str] = []
    current_kind: str | None = None
    current_lines: list[str] = []

    def flush() -> None:
        nonlocal current_kind, current_lines
        if current_kind is None or not current_lines:
            current_kind = None
            current_lines = []
            return
        paragraph = " ".join(
            part for part in (line.strip() for line in current_lines) if part
        )
        target = (
            table_captions
            if current_kind.lower() == "table"
            else figure_captions
        )
        target.append(paragraph)
        current_kind = None
        current_lines = []

    for line in text.splitlines():
        match = CAPTION_PATTERN.match(line)
        if match:
            flush()
            current_kind = match.group("kind")
            current_lines = [line]
            continue
        if current_kind is None:
            continue
        if not line.strip() or SECTION_HEADING.match(line):
            flush()
            continue
        current_lines.append(line)
    flush()
    return "\n".join(figure_captions), "\n".join(table_captions)


def clean(text: str, pages: list[str] | None = None) -> str:
    lines = text.split("\n")
    text = "\n".join(l for l in lines if not _is_page_number(l))
    if pages and len(pages) > 2:
        page_lines = [p.split("\n") for p in pages]
        repeated = _find_repeated_lines(page_lines)
        if repeated:
            text = _remove_repeated_lines(text, repeated)
    text = _remove_noise_lines(text)
    text = _deduplicate_paragraphs(text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def clean_with_captions(
    text: str,
    pages: list[str] | None = None,
) -> dict[str, str]:
    """Clean text and separately expose preserved caption paragraphs."""
    figure_captions, table_captions = _extract_captions(text)
    return {
        "text": clean(text, pages=pages),
        "figure_captions": figure_captions,
        "table_captions": table_captions,
    }
