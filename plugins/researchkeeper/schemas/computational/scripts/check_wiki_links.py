# -*- coding: utf-8 -*-
"""computer_kb wiki 链接完整性检查

检查项:
1. 孤儿页（无任何入链）
2. 零出链页面（不链接到任何其他页面）
3. 断链（[[]] 指向不存在的页面）
4. 建议链接（基于 software/topic 标签推荐）

用法:
    python computer_kb/scripts/check_wiki_links.py
    python computer_kb/scripts/check_wiki_links.py --json
    python computer_kb/scripts/check_wiki_links.py --root path/to/computer_kb

脚本位于 <computer_kb>/scripts/ 下，默认检查其兄弟目录 <computer_kb>/wiki/，
在 schema 包仓库内（schemas/computational/）和安装后（computer_kb/）均适用。
"""

import json
import re
import sys
from pathlib import Path

# Force UTF-8 on Windows consoles
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


def _parse_root_arg():
    """Parse optional --root <dir> (computer_kb root containing wiki/)."""
    if "--root" in sys.argv:
        idx = sys.argv.index("--root")
        if idx + 1 < len(sys.argv):
            return Path(sys.argv[idx + 1]).resolve()
    return None


_root = _parse_root_arg()
WIKI_DIR = (_root / "wiki") if _root else (Path(__file__).resolve().parents[1] / "wiki")


def get_all_pages():
    """Get all wiki pages (excluding README.md and index.md)."""
    pages = {}
    for md in WIKI_DIR.rglob("*.md"):
        if md.name in ("README.md", "index.md"):
            continue
        rel = md.relative_to(WIKI_DIR)
        page_name = md.stem
        pages[page_name] = {
            "path": str(rel).replace("\\", "/"),
            "dir": rel.parts[0] if len(rel.parts) > 1 else "",
            "full_path": md,
        }
    return pages


def extract_obsidian_links(filepath):
    """Extract [[...]] links from a markdown file."""
    text = filepath.read_text(encoding="utf-8")
    return re.findall(r"\[\[(.+?)\]\]", text)


def extract_software_tag(filepath):
    """Extract software tag from frontmatter."""
    text = filepath.read_text(encoding="utf-8")
    match = re.search(r"^software:\s*(.+)$", text, re.MULTILINE)
    if match:
        return [s.strip() for s in match.group(1).split(",")]
    return []


def check_links():
    """Run all link checks."""
    pages = get_all_pages()
    page_names = set(pages.keys())

    # Build link graph
    outgoing = {}  # page -> [linked pages]
    incoming = {}  # page -> [pages that link to it]
    broken = []    # (source_page, broken_target)

    for name, info in pages.items():
        links = extract_obsidian_links(info["full_path"])
        outgoing[name] = links
        for link in links:
            if link in page_names:
                incoming.setdefault(link, []).append(name)
            else:
                broken.append((name, link))

    # Find orphans (no incoming links)
    orphans = [name for name in page_names if name not in incoming]

    # Find zero-outgoing pages
    zero_out = [name for name, links in outgoing.items() if len(links) == 0]

    # Software-based suggestions
    software_map = {}
    for name, info in pages.items():
        sw = extract_software_tag(info["full_path"])
        for s in sw:
            software_map.setdefault(s, []).append(name)

    suggestions = []
    for name, info in pages.items():
        sw = extract_software_tag(info["full_path"])
        current_links = set(outgoing.get(name, []))
        for s in sw:
            for candidate in software_map.get(s, []):
                if candidate != name and candidate not in current_links:
                    suggestions.append((name, candidate, s))

    # Deduplicate suggestions
    seen = set()
    unique_suggestions = []
    for src, dst, sw in suggestions:
        key = (src, dst)
        if key not in seen:
            seen.add(key)
            unique_suggestions.append((src, dst, sw))

    report = {
        "total_pages": len(pages),
        "orphans": sorted(orphans),
        "zero_outgoing": sorted(zero_out),
        "broken_links": sorted(broken),
        "suggestions": sorted(unique_suggestions),
    }
    return report


def print_report(report):
    """Print human-readable report."""
    print(f"Wiki 链接检查报告 — {report['total_pages']} pages\n")

    if report["orphans"]:
        print(f"孤儿页（{len(report['orphans'])} 个，无任何入链）:")
        for p in report["orphans"]:
            print(f"  ✗ {p}")
    else:
        print("孤儿页: 无 ✓")

    if report["zero_outgoing"]:
        print(f"\n零出链页面（{len(report['zero_outgoing'])} 个）:")
        for p in report["zero_outgoing"]:
            print(f"  ✗ {p}")
    else:
        print("\n零出链页面: 无 ✓")

    if report["broken_links"]:
        print(f"\n断链（{len(report['broken_links'])} 个）:")
        for src, target in report["broken_links"]:
            print(f"  ✗ {src} → [[{target}]] (不存在)")
    else:
        print("\n断链: 无 ✓")

    if report["suggestions"]:
        print(f"\n建议链接（{len(report['suggestions'])} 条，基于 software 标签）:")
        for src, dst, sw in report["suggestions"][:20]:
            print(f"  → {src} 应链接到 {dst} (共同: {sw})")
        if len(report["suggestions"]) > 20:
            print(f"  ... 还有 {len(report['suggestions']) - 20} 条")


def main():
    report = check_links()
    if "--json" in sys.argv:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print_report(report)

    # Exit code: 1 if any issues found
    has_issues = (report["orphans"] or report["zero_outgoing"] or report["broken_links"])
    sys.exit(1 if has_issues else 0)


if __name__ == "__main__":
    main()
