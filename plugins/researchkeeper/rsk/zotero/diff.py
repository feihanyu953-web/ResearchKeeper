# -*- coding: utf-8 -*-
"""Zotero vs kb diff: find papers in Zotero not yet ingested into knowledge base.

Usage:
  # Default path (auto-read from outputs/zotero_export.json)
  python -m rsk.zotero.diff

  # Specify input file
  python -m rsk.zotero.diff --zotero outputs/zotero_export.json

  # Export filtered JSON for batch ingestion (feed to pdf_parser.py batch)
  python -m rsk.zotero.diff --export tmp/unmatched.json

Dependency: run zotero_reader.py first to generate zotero_export.json.

Notes:
  - Zotero uses FirstAuthorYear naming; kb uses custom paper_id (which may be given name / DOI suffix / topic name).
  - KNOWN_ALIASES manually maintains known naming discrepancies. Items marked "-> alias" in diff output are covered by this mapping.
  - SKIP_TITLE_KEYWORDS excludes review articles, addon items, etc. that should not be ingested.
"""

import argparse, json, os, re, sys
from pathlib import Path

from rsk.config import PROJECT_ROOT, get_kb_dir
KB_DIR = get_kb_dir()
DEFAULT_ZOTERO = PROJECT_ROOT / "outputs" / "zotero_export.json"

# Manual maintenance: Zotero FirstAuthorYear -> kb paper_id
# When kb uses given name / DOI suffix / topic name instead of family name, register here.
# Diff output will mark "-> alias".
KNOWN_ALIASES = {
    'Lan2023':      'Jiao2023',       # kb uses given name "Jiao"
    'Tashrifi2021': 'Zahra2021',      # kb uses given name "Zahra"
    'Ju2025':       'AOR2025',        # kb uses topic name
    'Zhou2025':     'Fengchun2025',   # kb uses full given name
    'Shao2022':     'e2022',          # kb uses DOI suffix
}

# Exclusion items
# Zotero entries whose title contains any of these keywords are excluded from diff (e.g. review articles, addon items).
SKIP_TITLE_KEYWORDS = [
    'Addon item',
]


def load_kb_paper_ids(kb_dir):
    """Scan kb/*.md for all schema_v1 record paper_ids, return set."""
    pids = set()
    for fname in ['literature.md', 'synthesis.md', 'performance.md',
                  'spectra.md', 'mechanism.md', 'methods.md']:
        fpath = os.path.join(kb_dir, fname)
        if not os.path.exists(fpath):
            continue
        with open(fpath, 'r', encoding='utf-8') as f:
            for line in f:
                m = re.match(r'\|\s*\S+-\d+\s*\|\s*schema_v1\s*\|\s*(\S+?)\s*\|', line)
                if m:
                    pids.add(m.group(1))
    return pids


def load_zotero_papers(zotero_path):
    """Load zotero_export.json, return papers list."""
    with open(zotero_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data.get('papers', [])


def make_signature(paper):
    """Generate FirstAuthorYear signature from Zotero paper."""
    authors = paper.get('authors', [])
    first_last = authors[0]['lastName'] if authors else '?'
    # Remove spaces and special chars (e.g. "Brotons Rufes" -> "BrotonsRufes")
    first_last = re.sub(r'\s+', '', first_last)
    year = paper.get('year', '') or '0'
    return f"{first_last}{year}"


def diff(zotero_path, kb_dir):
    """Execute diff, return (matched, unmatched) lists."""
    kb_pids = load_kb_paper_ids(kb_dir)
    papers = load_zotero_papers(zotero_path)

    matched = []
    unmatched = []

    for p in papers:
        title = p.get('title', '')
        if not title:
            continue
        if any(kw.lower() in title.lower() for kw in SKIP_TITLE_KEYWORDS):
            continue

        authors = p.get('authors', [])
        first_last = authors[0]['lastName'] if authors else '?'
        year = p.get('year', '') or '0'
        sig = make_signature(p)

        # 1) Direct alias mapping
        resolved = KNOWN_ALIASES.get(sig, sig)
        if resolved in kb_pids:
            matched.append({
                'zotero_sig': sig,
                'kb_pid': resolved,
                'via': 'alias' if sig != resolved else 'direct',
                'title': title[:120],
                'authors': ', '.join(a['lastName'] for a in authors[:3]),
                'year': year,
            })
            continue

        # 2) Fuzzy match: kb pid starts with first_last + year
        found = False
        for pid in kb_pids:
            if pid.lower().startswith(first_last.lower()) and str(year) in pid:
                matched.append({
                    'zotero_sig': sig,
                    'kb_pid': pid,
                    'via': 'fuzzy',
                    'title': title[:120],
                    'authors': ', '.join(a['lastName'] for a in authors[:3]),
                    'year': year,
                })
                found = True
                break
        if found:
            continue

        # 3) Unmatched
        unmatched.append(p)

    return matched, unmatched, kb_pids


def main():
    p = argparse.ArgumentParser(
        description='Zotero vs kb diff: list papers in Zotero not yet ingested into knowledge base')
    p.add_argument('--zotero', default=str(DEFAULT_ZOTERO),
                   help=f'zotero_export.json path (default: {DEFAULT_ZOTERO})')
    p.add_argument('--kb-dir', default=str(KB_DIR),
                   help=f'kb directory path (default: {KB_DIR})')
    p.add_argument('--export',
                   help='Export unmatched papers as filtered JSON (for pdf_parser.py batch use)')
    p.add_argument('--quiet', action='store_true',
                   help='Only output unmatched paper list, no statistics')
    args = p.parse_args()

    matched, unmatched, kb_pids = diff(args.zotero, args.kb_dir)

    if not args.quiet:
        print(f"kb paper_ids: {len(kb_pids)}")
        print(f"Matched (in kb): {len(matched)}")
        print(f"Unmatched: {len(unmatched)}")
        print()

    if unmatched:
        print("=" * 70)
        print("  The following papers are in Zotero but not yet in the knowledge base")
        print("=" * 70)
        for i, p in enumerate(unmatched):
            authors = ', '.join(a['lastName'] for a in p.get('authors', [])[:3])
            year = p.get('year', '?')
            title = p['title'][:120]
            has_pdf = 'Y' if p.get('pdfPath') else 'N'
            key = p.get('key', '?')
            doi = p.get('doi', '') or ''
            journal = (p.get('journal', '') or '')[:50]
            sig = make_signature(p)
            print(f"\n[{i+1}] {authors} ({year}) [PDF:{has_pdf}]  -> suggested paper_id: {sig}")
            print(f"    {title}")
            if journal:
                print(f"    {journal}")
            if doi:
                print(f"    DOI: {doi}")
    else:
        print("All Zotero papers are already in kb.")

    if not args.quiet and matched:
        print(f"\n(Matched {len(matched)} papers, "
              f"{sum(1 for m in matched if m['via']=='alias')} via alias mapping, "
              f"{sum(1 for m in matched if m['via']=='fuzzy')} via fuzzy matching)")

    if args.export:
        out_path = args.export
        os.makedirs(os.path.dirname(out_path) or '.', exist_ok=True)
        with open(out_path, 'w', encoding='utf-8') as f:
            json.dump({'stats': {'total': len(unmatched)}, 'papers': unmatched},
                      f, ensure_ascii=False, indent=2)
        print(f"\nExported {len(unmatched)} unmatched papers to: {out_path}")


if __name__ == '__main__':
    main()
