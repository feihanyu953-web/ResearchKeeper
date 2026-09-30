"""
LitMind · PaperContent 数据模型
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field, asdict


@dataclass
class PaperSections:
    """论文各章节原始文本"""
    abstract: str = ""
    introduction: str = ""
    methods: str = ""
    results: str = ""
    discussion: str = ""
    conclusion: str = ""
    references: str = ""
    other: str = ""
    figure_captions: str = ""
    table_captions: str = ""


@dataclass
class PaperContent:
    """结构化论文全文"""
    paperKey: str = ""
    sourcePath: str = ""
    fullText: str = ""
    rawText: str = ""
    sections: PaperSections = field(default_factory=PaperSections)
    pageCount: int = 0
    charCount: int = 0
    parseSuccess: bool = False
    parseErrors: list[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        d = asdict(self)
        return d

    def to_json(self, ensure_ascii: bool = False, indent: int = 2) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=ensure_ascii, indent=indent)

    @classmethod
    def from_dict(cls, data: dict) -> "PaperContent":
        if isinstance(data.get("sections"), dict):
            data["sections"] = PaperSections(**data["sections"])
        return cls(**data)
