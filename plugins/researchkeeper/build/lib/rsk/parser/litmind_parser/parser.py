"""
LitMind · Paper Parser 主入口 — PDF → 清洗 → 章节识别 → PaperContent
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Optional

from .cleaner import clean_with_captions
from .models import PaperContent, PaperSections
from .sectionizer import sectionize


def _read_pdf_pymupdf(pdf_path: str) -> tuple[str, list[str], int]:
    import fitz
    doc = fitz.open(pdf_path)
    pages: list[str] = []
    full_text_parts: list[str] = []
    for page_num in range(len(doc)):
        page = doc[page_num]
        page_text = page.get_text("text")
        pages.append(page_text)
        full_text_parts.append(page_text)
    doc.close()
    return "\n\n".join(full_text_parts), pages, len(pages)


def _read_pdf_fallback(pdf_path: str) -> tuple[str, list[str], int]:
    try:
        import pdfplumber
        pages: list[str] = []
        with pdfplumber.open(pdf_path) as pdf:
            for p in pdf.pages:
                text = p.extract_text() or ""
                pages.append(text)
        return "\n\n".join(pages), pages, len(pages)
    except ImportError:
        pass
    try:
        from PyPDF2 import PdfReader
        pages = []
        reader = PdfReader(pdf_path)
        for p in reader.pages:
            text = p.extract_text() or ""
            pages.append(text)
        return "\n\n".join(pages), pages, len(pages)
    except ImportError:
        pass
    raise ImportError(
        "需要安装 PDF 解析库:\n"
        "  pip install pymupdf\n"
        "  或 pip install pdfplumber\n"
        "  或 pip install PyPDF2"
    )


def read_pdf(pdf_path: str) -> tuple[str, list[str], int]:
    try:
        return _read_pdf_pymupdf(pdf_path)
    except ImportError:
        try:
            return _read_pdf_fallback(pdf_path)
        except ImportError:
            raise ImportError(
                "No PDF reader available.\n"
                "Install one of: pip install pymupdf\n"
                "               pip install pdfplumber\n"
                "               pip install PyPDF2"
            )


def parse_pdf(pdf_path: str, paper_key: str = "", engine: str = "auto") -> PaperContent:
    content = PaperContent(paperKey=paper_key, sourcePath=pdf_path)
    if not pdf_path or not os.path.exists(pdf_path):
        content.parseErrors.append(f"PDF file not found: {pdf_path}")
        return content
    try:
        full_text, pages, page_count = read_pdf(pdf_path)
        content.rawText = full_text
        content.pageCount = page_count
        if not full_text.strip():
            content.parseErrors.append("No text extracted from PDF")
            return content
        cleaned_result = clean_with_captions(full_text, pages=pages)
        cleaned = cleaned_result["text"]
        content.fullText = cleaned
        content.sections = sectionize(cleaned)
        content.sections.figure_captions = cleaned_result["figure_captions"]
        content.sections.table_captions = cleaned_result["table_captions"]
        content.charCount = len(cleaned)
        content.parseSuccess = True
    except ImportError as e:
        content.parseErrors.append(str(e))
        return content
    except Exception as e:
        content.parseErrors.append(f"Parse error: {e}")
    return content


def parse_multiple(pdf_paths: list[tuple[str, str]], engine: str = "auto") -> list[PaperContent]:
    results = []
    for path, key in pdf_paths:
        results.append(parse_pdf(path, paper_key=key, engine=engine))
    return results
