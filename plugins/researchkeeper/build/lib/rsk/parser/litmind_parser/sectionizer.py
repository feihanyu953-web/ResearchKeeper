"""
LitMind · 章节识别器 — 中英文学术论文章节边界检测
"""

from __future__ import annotations

import re
from typing import Optional
from .models import PaperSections

_NUM = r"(?:\d+\.?\s*|(?:I{1,3}V?|IV|VI{0,3})\.?\s*)?"

SECTION_PATTERNS_EN: dict[str, list[re.Pattern]] = {
    "abstract": [
        re.compile(rf"^{_NUM}[Aa]bstract\s*\.?\s*$"),
        re.compile(rf"^{_NUM}[Aa]bstract\.\s+\w"),
    ],
    "introduction": [
        re.compile(rf"^{_NUM}[Ii]ntroduction\s*$"),
        re.compile(rf"^{_NUM}[Ii]ntroduction\s*\.?\s*$"),
    ],
    "methods": [
        re.compile(rf"^{_NUM}[Mm]ethods?\s*$"),
        re.compile(rf"^{_NUM}[Mm]aterials?\s+(?:and\s+)?[Mm]ethods?\s*$"),
        re.compile(rf"^{_NUM}[Mm]ethodology\s*$"),
        re.compile(rf"^{_NUM}[Ee]xperimental\s+(?:setup|procedures?|design|protocol)\s*$"),
    ],
    "results": [
        re.compile(rf"^{_NUM}[Rr]esults?\s*$"),
        re.compile(rf"^{_NUM}[Rr]esults?\s+.*$"),
    ],
    "discussion": [
        re.compile(rf"^{_NUM}[Dd]iscussion\s*$"),
    ],
    "conclusion": [
        re.compile(rf"^{_NUM}[Cc]onclusion[s]?\s*$"),
        re.compile(rf"^{_NUM}[Ss]ummary\s*$"),
        re.compile(rf"^{_NUM}[Cc]oncluding\s+[Rr]emarks?\s*$"),
    ],
    "references": [
        re.compile(r"^[Rr]eferences?\s*$"),
        re.compile(r"^[Bb]ibliography\s*$"),
        re.compile(r"^[Cc]itations?\s*$"),
        re.compile(r"^[Ww]orks\s+[Cc]ited\s*$"),
        re.compile(r"^Acknowledg(?:e)?ment\s*$", re.I),
    ],
}

SECTION_PATTERNS_CN: dict[str, list[re.Pattern]] = {
    "abstract": [re.compile(r"^摘\s*要\s*\.?\s*$")],
    "introduction": [re.compile(r"^(?:引\s*言|前\s*言|绪\s*论|概\s*述|引\s*论)\s*\.?\s*$")],
    "methods": [re.compile(r"^(?:研究\s*方法|实验\s*方法|材料\s*与\s*方[法式]|方[法式]|实验\s*设计|研究对象)\s*\.?\s*$")],
    "results": [re.compile(r"^(?:研究\s*结果|实验\s*结果|结\s*果|分析\s*结果)\s*\.?\s*$")],
    "discussion": [re.compile(r"^(?:讨\s*论|分析与\s*讨论)\s*\.?\s*$")],
    "conclusion": [re.compile(r"^(?:结\s*论|结\s*语|总\s*结|研究\s*结论)\s*\.?\s*$")],
    "references": [re.compile(r"^(?:参\s*考\s*文\s*献|参考书目|参考文献|致\s*谢)\s*\.?\s*$")],
}

def _merge_patterns() -> dict[str, list[re.Pattern]]:
    merged: dict[str, list[re.Pattern]] = {}
    for key in SECTION_PATTERNS_EN:
        merged.setdefault(key, []).extend(SECTION_PATTERNS_EN[key])
    for key in SECTION_PATTERNS_CN:
        merged.setdefault(key, []).extend(SECTION_PATTERNS_CN[key])
    return merged

def _detect_section_boundaries(lines: list[str]) -> dict[str, tuple[int, int]]:
    patterns = _merge_patterns()
    boundaries: dict[str, int] = {}
    for i, line in enumerate(lines):
        stripped = line.strip()
        if not stripped:
            continue
        for section_key, pats in patterns.items():
            if section_key in boundaries:
                continue
            for pat in pats:
                m = pat.match(stripped)
                if m:
                    is_inline = m.end() < len(stripped)
                    boundaries[section_key] = (i, is_inline)
                    break
    sorted_sections = sorted(boundaries.items(), key=lambda x: x[1][0])
    result: dict[str, tuple[int, int]] = {}
    items = list(sorted_sections)
    for idx, (key, (line_idx, inline)) in enumerate(items):
        start = line_idx if inline else line_idx + 1
        end = items[idx + 1][1][0] if idx + 1 < len(items) else len(lines)
        result[key] = (start, end)
    return result

def sectionize(full_text: str) -> PaperSections:
    sections = PaperSections()
    lines = full_text.split("\n")
    if not lines or not full_text.strip():
        sections.other = full_text
        return sections
    boundaries = _detect_section_boundaries(lines)
    taken_lines: set[int] = set()
    for section_key, (start, end) in boundaries.items():
        content = "\n".join(lines[start + 1:end]).strip()
        setattr(sections, section_key, content)
        taken_lines.update(range(start, end))
    all_lines_set = set(range(len(lines)))
    remaining = sorted(all_lines_set - taken_lines)
    if remaining:
        other_text = "\n".join(lines[i] for i in remaining).strip()
        if not boundaries:
            sections.other = other_text
        else:
            sections.other = other_text
    return sections

def extract_section(text: str, section_name: str) -> str:
    sections = sectionize(text)
    return getattr(sections, section_name, "")
