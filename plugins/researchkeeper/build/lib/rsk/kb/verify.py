# -*- coding: utf-8 -*-
"""Post-ingest verification: validate coverage of specified paper_ids across kb modules.

Usage:
  # Read paper_id list from file (one per line)
  python -m rsk.kb.verify --papers-file tmp/new_papers.txt

  # Specify directly on command line
  python -m rsk.kb.verify --papers Elena2025 Xu2021 Hu2026

  # Check all ingested papers' module coverage
  python -m rsk.kb.verify --all

  # Optional legacy statistics threshold (not an audit verdict)
  python -m rsk.kb.verify --papers Elena2025 Xu2021 --min-modules 4
"""

import argparse, re
from dataclasses import dataclass
from pathlib import Path
from collections import defaultdict

from rsk.config import PROJECT_ROOT


def _active_context(workspace=None, kb_dir=None):
    from rsk.kb.coverage import active_module_map

    root = Path(workspace or PROJECT_ROOT).expanduser().resolve()
    return (
        root,
        Path(kb_dir).expanduser().resolve()
        if kb_dir is not None
        else root / "kb",
        active_module_map(root),
    )


def get_coverage(paper_ids=None, *, workspace=None, kb_dir=None):
    """Scan kb modules, return {paper_id: {module: record_count}}.

    If paper_ids is None, return all.
    """
    coverage = defaultdict(lambda: defaultdict(int))
    filter_set = set(paper_ids) if paper_ids else None
    _root, kb_root, module_map = _active_context(workspace, kb_dir)

    for mod, file_name in module_map.items():
        fpath = kb_root / file_name
        if not fpath.exists():
            continue
        with fpath.open('r', encoding='utf-8') as f:
            for line in f:
                m = re.match(r'\|\s*\S+-\d+\s*\|\s*schema_v1\s*\|\s*(\S+?)\s*\|', line)
                if not m:
                    continue
                pid = m.group(1)
                if filter_set is None or pid in filter_set:
                    coverage[pid][mod] += 1

    return coverage


def print_coverage(coverage, min_modules=0, *, modules=()):
    """Print module coverage for each paper."""
    if not coverage:
        print("(no records found)")
        return

    total_ok = 0
    total_fail = 0

    module_names = tuple(modules)
    for pid in sorted(coverage.keys()):
        modules = coverage[pid]
        n_mods = len(modules)
        n_recs = sum(modules.values())
        mod_list = '+'.join(sorted(modules.keys()))
        ok = n_mods >= min_modules
        flag = 'OK' if ok else 'LOW'

        if ok:
            total_ok += 1
        else:
            total_fail += 1

        print(
            f"  [{flag}] {pid:25s} {n_recs:3d} records, "
            f"{n_mods}/{len(module_names)} modules ({mod_list})"
        )
        if not ok:
            missing = set(module_names) - set(modules.keys())
            print(f"        missing modules: {', '.join(sorted(missing))}")

    print(f"\n  >={min_modules} modules: {total_ok} papers"
          + (f", <{min_modules} modules: {total_fail} papers" if total_fail else ""))


@dataclass(frozen=True)
class VerificationResult:
    status: str
    errors: tuple[str, ...]
    reviewer_required: tuple[str, ...]
    record_count: int


def verify_paper(paper_id, *, workspace=None):
    """Verify mechanical coverage against the active workspace schema."""
    from rsk.kb.coverage import CoverageError, load_coverage, validate_coverage

    root = Path(workspace or PROJECT_ROOT).expanduser().resolve()
    try:
        coverage = load_coverage(root, paper_id)
        errors, reviewer_required, record_count = validate_coverage(
            root,
            coverage,
        )
    except CoverageError as exc:
        errors = [str(exc)]
        reviewer_required = ()
        record_count = 0
    return VerificationResult(
        status="fail" if errors else "pass",
        errors=tuple(errors),
        reviewer_required=tuple(reviewer_required),
        record_count=record_count,
    )


def main():
    p = argparse.ArgumentParser(
        description='Post-ingest verification: validate paper_id coverage across kb modules')
    src = p.add_mutually_exclusive_group(required=True)
    src.add_argument('--papers', nargs='*',
                     help='List of paper_ids to verify (space separated)')
    src.add_argument('--papers-file',
                     help='File containing paper_id list (one per line)')
    src.add_argument('--all', action='store_true',
                     help='Verify all paper_ids in kb')
    p.add_argument('--min-modules', type=int, default=0,
                   help='Minimum module threshold (default 0 = stats only)')
    p.add_argument('--kb-dir', default=None,
                   help='KB directory path (default: active workspace kb)')
    args = p.parse_args()

    # Parse paper_ids
    if args.all:
        paper_ids = None
    elif args.papers_file:
        with open(args.papers_file, 'r', encoding='utf-8') as f:
            paper_ids = [line.strip() for line in f if line.strip()
                        and not line.startswith('#')]
    else:
        paper_ids = args.papers

    _root, _kb_dir, module_map = _active_context(kb_dir=args.kb_dir)
    coverage = get_coverage(paper_ids, kb_dir=args.kb_dir)

    if paper_ids:
        # Check one by one
        missing = [pid for pid in paper_ids if pid not in coverage]
        print(f"Total kb paper_ids: {len(get_coverage(kb_dir=args.kb_dir))}")
        print(f"Checking {len(paper_ids)} papers...\n")
        print_coverage({pid: coverage.get(pid, {}) for pid in paper_ids},
                       min_modules=args.min_modules,
                       modules=module_map)
        if missing:
            print(f"\n  MISSING from kb entirely: {', '.join(missing)}")
    else:
        print(f"Total kb paper_ids: {len(coverage)}")
        print()
        print_coverage(
            coverage,
            min_modules=args.min_modules,
            modules=module_map,
        )


if __name__ == '__main__':
    main()
