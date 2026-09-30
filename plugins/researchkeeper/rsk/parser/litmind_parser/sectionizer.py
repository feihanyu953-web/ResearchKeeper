"""
LitMind · 章节识别器 — 中英文学术论文章节边界检测
"""

from __future__ import annotations

import re
from typing import Optional
from .models import PaperSections

_NUM = r"(?:\d+\.?\s*|(?:I{1,3}V?|IV|VI{0,3})\.?\s*)?"
# 英文标题统一忽略大小写：ACS/Nature 等期刊标题常为全大写（INTRODUCTION、
# RESULTS AND DISCUSSION）。CN 模式无大小写概念，不适用。
_I = re.IGNORECASE

SECTION_PATTERNS_EN: dict[str, list[re.Pattern]] = {
    "abstract": [
        re.compile(rf"^{_NUM}abstract\s*\.?\s*$", _I),
        # 行内摘要："Abstract. text ..." 或 "ABSTRACT: text ..."（ACS 实际格式）
        re.compile(rf"^{_NUM}abstract[\.:]\s+\w", _I),
    ],
    "introduction": [
        re.compile(rf"^{_NUM}introduction\s*\.?\s*$", _I),
    ],
    "methods": [
        re.compile(rf"^{_NUM}methods?\s*$", _I),
        re.compile(rf"^{_NUM}materials?\s+(?:and\s+)?methods?\s*$", _I),
        re.compile(rf"^{_NUM}methodology\s*$", _I),
        re.compile(rf"^{_NUM}experimental\s+(?:section|setup|procedures?|design|protocol)\s*$", _I),
    ],
    "results": [
        re.compile(rf"^{_NUM}results?\s*$", _I),
        re.compile(rf"^{_NUM}results?\s+.*$", _I),
    ],
    "discussion": [
        re.compile(rf"^{_NUM}discussion\s*$", _I),
    ],
    "conclusion": [
        re.compile(rf"^{_NUM}conclusion[s]?\s*$", _I),
        re.compile(rf"^{_NUM}summary\s*$", _I),
        re.compile(rf"^{_NUM}concluding\s+remarks?\s*$", _I),
    ],
    "references": [
        # ACS 格式 "REFERENCES AND NOTES"
        re.compile(r"^references?(?:\s+and\s+notes)?\s*$", _I),
        re.compile(r"^bibliography\s*$", _I),
        re.compile(r"^citations?\s*$", _I),
        re.compile(r"^works\s+cited\s*$", _I),
        re.compile(r"^acknowledg(?:e)?ments?\s*$", _I),
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

# 行内标题（"Abstract. We report ..." / "ABSTRACT: We report ..."）的剥离前缀。
# 交替顺序长词在前，避免 "Materials and Methods" 被 "Methods" 截断。
_INLINE_HEADING_STRIP = re.compile(
    rf"^{_NUM}(?:abstract|introduction|materials?\s+(?:and\s+)?methods?|"
    rf"methods?|results?|discussion|conclusion[s]?|"
    rf"summary|concluding\s+remarks?)[\.:]\s+",
    re.IGNORECASE,
)

# 无标题布局回填（Nature/NC 系论文摘要与引言无标题行，正文直接开始）。
# 仅当 abstract 与 introduction 均空且存在 ≥2 个已识别章节边界时尝试：
# 从首章节之前的块中找第一个达标长段（≥150 字符、句末标点、≥1 个句子边界）
# 判为摘要，其后内容判为引言，之前（标题/作者/单位）留在 other。
# 找不到达标长段则放弃回填（宁缺勿错，防止作者块误入摘要）。
_ABSTRACT_MIN_CHARS = 150
_SENT_BOUNDARY_EN = re.compile(r"[.!?]\s+[A-Z0-9]")
_TERMINAL_RE = re.compile(r"[.!?。]$")


def _split_paragraphs(block: str) -> list[str]:
    return [
        re.sub(r"\s+", " ", p).strip()
        for p in re.split(r"\n\s*\n", block)
        if p.strip()
    ]


def _backfill_unlabeled(sections: PaperSections, block: str) -> None:
    paras = _split_paragraphs(block)
    for i, para in enumerate(paras):
        n_sents = max(len(_SENT_BOUNDARY_EN.findall(para)), para.count("。"))
        if (
            len(para) >= _ABSTRACT_MIN_CHARS
            and _TERMINAL_RE.search(para)
            and n_sents >= 1
        ):
            sections.abstract = para
            if i + 1 < len(paras):
                sections.introduction = "\n\n".join(paras[i + 1:])
            sections.other = "\n\n".join(paras[:i])
            return

def _merge_patterns() -> dict[str, list[re.Pattern]]:
    merged: dict[str, list[re.Pattern]] = {}
    for key in SECTION_PATTERNS_EN:
        merged.setdefault(key, []).extend(SECTION_PATTERNS_EN[key])
    for key in SECTION_PATTERNS_CN:
        merged.setdefault(key, []).extend(SECTION_PATTERNS_CN[key])
    return merged

def _detect_section_boundaries(lines: list[str]) -> dict[str, tuple[int, int, bool]]:
    patterns = _merge_patterns()
    boundaries: dict[str, tuple[int, bool]] = {}
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
    result: dict[str, tuple[int, int, bool]] = {}
    items = list(sorted_sections)
    for idx, (key, (line_idx, inline)) in enumerate(items):
        # 行内标题从标题行本身开始（首行剥离前缀）；非行内标题从下一行开始
        start = line_idx if inline else line_idx + 1
        end = items[idx + 1][1][0] if idx + 1 < len(items) else len(lines)
        result[key] = (start, end, inline)
    return result

def sectionize(full_text: str) -> PaperSections:
    sections = PaperSections()
    lines = full_text.split("\n")
    if not lines or not full_text.strip():
        sections.other = full_text
        return sections
    boundaries = _detect_section_boundaries(lines)
    taken_lines: set[int] = set()
    for section_key, (start, end, inline) in boundaries.items():
        seg = lines[start:end]
        if inline and seg:
            # 行内标题首行剥离标题前缀（如 "Abstract. We report ..." → "We report ..."）
            seg[0] = _INLINE_HEADING_STRIP.sub("", seg[0]).strip()
        content = "\n".join(seg).strip()
        setattr(sections, section_key, content)
        # 非行内标题的标题行本身归入 taken，避免泄漏进 other
        head = start if inline else start - 1
        taken_lines.update(range(head, end))
    all_lines_set = set(range(len(lines)))
    remaining = sorted(all_lines_set - taken_lines)
    if remaining:
        other_text = "\n".join(lines[i] for i in remaining).strip()
        sections.other = other_text
    if (
        not sections.abstract
        and not sections.introduction
        and len(boundaries) >= 2
    ):
        _backfill_unlabeled(sections, sections.other)
    return sections

def extract_section(text: str, section_name: str) -> str:
    sections = sectionize(text)
    return getattr(sections, section_name, "")
