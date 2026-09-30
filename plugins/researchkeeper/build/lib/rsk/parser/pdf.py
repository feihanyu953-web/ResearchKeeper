# -*- coding: utf-8 -*-
"""PDF text extraction with litmind_parser cleaning pipeline + SI auto-merge."""

import argparse, json, os, re, sys
from pathlib import Path

from rsk.parser.litmind_parser import parse_pdf


def parse_single(pdf_path, si_paths=None, output_path=None, title=None):
    """Parse main PDF through litmind_parser pipeline and optionally merge SI content.

    Returns (output_path_or_content, parse_success, error_msg).
    """
    result = parse_pdf(pdf_path)
    sections = result.sections

    si_texts = []
    if si_paths:
        for si_path in si_paths:
            try:
                si_result = parse_pdf(si_path)
                si_filename = os.path.basename(si_path)
                if hasattr(si_result, "fullText"):
                    full_text = si_result.fullText
                else:
                    full_text = str(si_result)
                si_texts.append(f"### SI File: {si_filename}\n\n{full_text}")
            except Exception as e:
                si_texts.append(f"### SI File: {si_filename}\n\n(Parse error: {e})")

    md = []
    if not title:
        title = os.path.splitext(os.path.basename(pdf_path))[0]
    md.append(f"# {title}\n")

    section_names = ["abstract", "introduction", "methods", "results",
                     "discussion", "conclusion", "references", "other"]
    for section in section_names:
        text = getattr(sections, section, "") or ""
        if text and len(text.strip()) > 10:
            section_title = "References" if section == "references" else section.capitalize()
            md.append(f"## {section_title}\n\n{text}\n")

    if si_texts:
        md.append("## Supplementary Information\n")
        md.extend(si_texts)

    content = "\n".join(md)
    success = result.parseSuccess
    error = "; ".join(result.parseErrors) if result.parseErrors else (
        "No sections extracted" if not any(getattr(sections, s, "") for s in section_names) else ""
    )

    if output_path:
        out = Path(output_path)
        out.parent.mkdir(parents=True, exist_ok=True)
        with open(out, "w", encoding="utf-8") as f:
            f.write(content)
        return str(out), success, error
    return content, success, error


def cmd_single(args):
    content, ok, err = parse_single(args.pdf, si_paths=args.si, output_path=args.output)
    if not ok:
        print(f"[WARN] {err}")
    if args.output:
        print(f"Written: {args.output}")
    else:
        preview = content[:500]
        print(preview + ("..." if len(content) > 500 else ""))


def cmd_batch(args):
    with open(args.from_zotero, "r", encoding="utf-8") as f:
        data = json.load(f)
    output_dir = Path(args.output_dir) if hasattr(args, 'output_dir') and args.output_dir else Path("tmp")
    output_dir.mkdir(parents=True, exist_ok=True)
    papers = data.get("papers", data) if isinstance(data, dict) else data
    total = len(papers)
    success = 0
    skipped = 0
    for i, paper in enumerate(papers, 1):
        pdf = paper.get("pdfPath", "")
        if not pdf or not os.path.exists(pdf):
            print(f"[{i}/{total}] SKIP: PDF not found - {(paper.get('title', '?') or '?')[:50]}")
            skipped += 1
            continue
        paper_key = paper.get("key", f"paper_{i}")
        paper_key = re.sub(r'[<>:\"/\\|?*]', '_', paper_key)
        paper_title = paper.get("title", "")
        si_paths = [s for s in paper.get("siPaths", []) if os.path.exists(s)]
        output_path = output_dir / f"{paper_key}.md"
        try:
            _, ok, err = parse_single(pdf, si_paths=si_paths, output_path=str(output_path), title=paper_title)
            if not ok:
                print(f"[{i}/{total}] FAIL: {err or 'PDF parse returned empty'} - {paper_title[:50]}")
                skipped += 1
            else:
                si_tag = f" (+{len(si_paths)} SI)" if si_paths else ""
                print(f"[{i}/{total}] OK: {output_path}{si_tag}")
                success += 1
        except Exception as e:
            print(f"[{i}/{total}] FAIL: {(paper.get('title', '?') or '?')[:50]} - {e}")
            skipped += 1
    print(f"\nProcessed: {success}/{total} success, {skipped} skipped")


def main():
    p = argparse.ArgumentParser(description="LitMind PDF Parser")
    sub = p.add_subparsers(dest="command")
    ps = sub.add_parser("single", help="Parse single PDF")
    ps.add_argument("pdf", help="PDF file path")
    ps.add_argument("--si", nargs="*", default=[], help="SI PDF files")
    ps.add_argument("-o", "--output", default=None, help="Output markdown path")
    ps.set_defaults(func=cmd_single)
    pb = sub.add_parser("batch", help="Batch parse from Zotero export")
    pb.add_argument("--from-zotero", required=True, help="zotero_export.json path")
    pb.add_argument("--output-dir", default="tmp", help="Output directory for markdown files")
    pb.set_defaults(func=cmd_batch)
    args = p.parse_args()
    if not args.command:
        p.print_help()
        sys.exit(1)
    args.func(args)


if __name__ == "__main__":
    main()
