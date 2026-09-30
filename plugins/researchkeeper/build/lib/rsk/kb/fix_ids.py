"""Fix paper_id normalization: normalize old paper_ids to canonical IDs from literature.md.
Only modifies the paper_id field, does not change other content.
Usage: python -m rsk.kb.fix_ids (--dry-run)
"""
import sys, re
from pathlib import Path

from rsk.config import PROJECT_ROOT, get_kb_dir
KB_DIR = get_kb_dir()

# paper_id mapping: {file: [(record_id_prefix, old_pid, new_pid), ...]}
# Format: (record_id, old_paper_id, new_paper_id)
REPLACEMENTS = [
    # Add your paper_id mappings here. Example:
    # ("mechanism.md", "mechanism-0052", "OldName", "NewName"),
]

def main():
    dry_run = "--dry-run" in sys.argv
    changed = 0

    for filename, rec_id, old_pid, new_pid in REPLACEMENTS:
        fpath = KB_DIR / filename
        if not fpath.exists():
            print(f"MISSING: {filename}")
            continue

        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        # Find the line with this record_id and old paper_id
        pattern = rf"^(\| {re.escape(rec_id)} \| schema_v1 \| ){re.escape(old_pid)}( \|)"
        replacement = f"\\1{new_pid}\\2"
        new_content, n = re.subn(pattern, replacement, content, flags=re.MULTILINE)

        if n == 0:
            print(f"NOT FOUND: {filename} {rec_id} {old_pid}->{new_pid}")
        elif n > 1:
            print(f"MULTI-MATCH: {filename} {rec_id} ({n} matches) -- skipping")
        else:
            if not dry_run:
                with open(fpath, "w", encoding="utf-8") as f:
                    f.write(new_content)
            changed += 1
            print(f"{'[DRY] ' if dry_run else ''}OK: {filename} {rec_id}: {old_pid}->{new_pid}")

    print(f"\n{'[DRY RUN] ' if dry_run else ''}Changed: {changed}/{len(REPLACEMENTS)} records")

if __name__ == "__main__":
    main()
