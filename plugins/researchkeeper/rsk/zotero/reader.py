# -*- coding: utf-8 -*-
"""
LitMind-Fork . Zotero Reader v2
Fixed: SI detection now uses resolved disk filename (not truncated DB path)
Enhanced: Zotero 7 path resolution with prefix-similarity matching and 3-layer SI matching
"""

import sqlite3, os, re, sys
from pathlib import Path
from collections import defaultdict

FIELD_NAMES = {}

SI_PATTERNS = [
    re.compile(r"(?i)_SI\."),
    re.compile(r"(?i)SI[_.-]"),
    re.compile(r"(?i)supp(mat|info|lementary|orting)"),
    re.compile(r"(?i)mmc\d+"),
    re.compile(r"(?i)MOESM"),
    re.compile(r"(?i)_si_\d+"),
    re.compile(r"(?i)sup-\d+"),
    re.compile(r"(?i)Supplementary"),
    re.compile(r"(?i)Supporting.Information"),
]

ARTICLE_ID_PATTERNS = [
    re.compile(r"([a-z]+\d+[a-z]?)", re.I),
    re.compile(r"(d\d[a-z]+\d+)", re.I),
    re.compile(r"([a-z]{4,}\d+)", re.I),
    re.compile(r"(S\d+-[\d]+)", re.I),
]

def _load_field_names(conn):
    FIELD_NAMES.clear()
    for row in conn.execute("SELECT fieldID, fieldName FROM fields"):
        FIELD_NAMES[row["fieldID"]] = row["fieldName"]

def _get_item_data(conn, item_id):
    cur = conn.execute("""SELECT id.fieldID, idv.value FROM itemData id JOIN itemDataValues idv ON id.valueID = idv.valueID WHERE id.itemID = ?""", (item_id,))
    return {FIELD_NAMES.get(r["fieldID"], f"f{r['fieldID']}"): r["value"] for r in cur}

def _get_creators(conn, item_id):
    cur = conn.execute("""SELECT c.firstName, c.lastName FROM itemCreators ic JOIN creators c ON ic.creatorID = c.creatorID WHERE ic.itemID = ? ORDER BY ic.orderIndex""", (item_id,))
    return [{"firstName": r["firstName"] or "", "lastName": r["lastName"] or ""} for r in cur]

def _get_tags(conn, item_id):
    cur = conn.execute("SELECT t.name FROM itemTags it JOIN tags t ON it.tagID = t.tagID WHERE it.itemID = ?", (item_id,))
    return [r["name"] for r in cur]

def _get_collections(conn, item_id):
    cur = conn.execute("""SELECT c.collectionName FROM collectionItems ci JOIN collections c ON ci.collectionID = c.collectionID WHERE ci.itemID = ?""", (item_id,))
    return [r["collectionName"] for r in cur]

def is_si(filename):
    """Check if filename matches SI naming patterns."""
    return any(p.search(filename) for p in SI_PATTERNS)

def resolve_path(item_key, raw_path, zotero_storage):
    """Zotero 7: storage/<key>/<filename>. Zotero 6 fallback."""
    if not raw_path:
        return ""
    if raw_path.startswith("storage:"):
        filename = raw_path[len("storage:"):]
        p7 = os.path.join(zotero_storage, item_key)
        if os.path.isdir(p7):
            candidates = []
            for f in os.listdir(p7):
                common = sum(1 for a, b in zip(f.lower(), filename.lower()) if a == b)
                candidates.append((common, f))
            if candidates:
                candidates.sort(reverse=True)
                best = candidates[0]
                # 5 is a safe lower bound: short article IDs (e.g. ja5c07718)
                # still get a reasonable prefix match without false positives.
                if best[0] >= min(5, len(filename)):
                    return os.path.join(p7, best[1])
        p6 = os.path.join(zotero_storage, filename)
        if os.path.exists(p6):
            return p6
        return ""
    if raw_path.startswith("attachments:"):
        filename = raw_path[len("attachments:"):]
        p7 = os.path.join(zotero_storage, item_key)
        if os.path.isdir(p7):
            for f in os.listdir(p7):
                if f.endswith(os.path.splitext(filename)[1]):
                    if len(f) > 5 and filename[:10].lower() in f.lower():
                        return os.path.join(p7, f)
    return raw_path

def extract_article_id(filename):
    """Extract publisher article ID from filename as matching key."""
    basename = os.path.splitext(os.path.basename(filename))[0]
    for pat in ARTICLE_ID_PATTERNS:
        m = pat.search(basename)
        if m:
            return m.group(1).lower()
    return None

def match_si_to_paper(papered_items, standalone_pdfs):
    """
    Three-layer SI matching.
    Layer 1: parentItemID (handled in export_all via attachments map)
    Layer 2: Common article ID in filename
    Layer 3: SI keyword detection as fallback (same storage dir match)
    """
    si_candidates = []
    for pdf in standalone_pdfs:
        if is_si(pdf["filename"]):
            art_id = extract_article_id(pdf["filename"])
            if art_id:
                si_candidates.append({"pdf": pdf, "art_id": art_id})
    for paper in papered_items:
        if not paper.get("pdfPath"):
            continue
        paper_art_id = extract_article_id(os.path.basename(paper["pdfPath"]))
        if not paper_art_id:
            continue
        for si in list(si_candidates):
            if si["art_id"] == paper_art_id:
                paper.setdefault("siPaths", []).append(si["pdf"]["path"])
                si_candidates.remove(si)
    for si in si_candidates:
        for paper in papered_items:
            if paper.get("pdfPath"):
                si_dir = os.path.dirname(si["pdf"]["path"])
                paper_dir = os.path.dirname(paper["pdfPath"])
                if si_dir == paper_dir:
                    paper.setdefault("siPaths", []).append(si["pdf"]["path"])
                    break
    return papered_items

def export_all(db_path):
    conn = sqlite3.connect(f"file:{db_path}?immutable=1", uri=True)
    conn.execute("PRAGMA query_only = ON;")
    conn.row_factory = sqlite3.Row
    try:
        _load_field_names(conn)

        zotero_dir = str(Path(db_path).parent)
        zotero_storage = os.path.join(zotero_dir, "storage")

        # Collect standalone PDF attachments (not linked to any parent)
        all_standalone_attachments = []
        cur = conn.execute("""SELECT i.key, ia.path FROM itemAttachments ia JOIN items i ON ia.itemID = i.itemID WHERE ia.parentItemID IS NULL AND ia.contentType = 'application/pdf'""")
        for r in cur:
            all_standalone_attachments.append({"key": r["key"], "path": r["path"]})

        # Build attachment map
        attachments = defaultdict(list)
        cur = conn.execute("""SELECT i.key, ia.parentItemID, ia.path, ia.contentType FROM itemAttachments ia JOIN items i ON ia.itemID = i.itemID WHERE ia.path IS NOT NULL""")
        for r in cur:
            if r["parentItemID"]:
                attachments[r["parentItemID"]].append({"key": r["key"], "path": r["path"], "type": r["contentType"]})

        papers = []
        stats = {"total": 0, "with_pdf": 0, "with_si": 0, "without_pdf": 0}

        cur = conn.execute("""SELECT i.itemID, i.key, it.typeName FROM items i JOIN itemTypes it ON i.itemTypeID = it.itemTypeID WHERE it.typeName NOT IN ('note', 'attachment', 'annotation') AND i.itemID NOT IN (SELECT itemID FROM deletedItems) ORDER BY i.itemID""")

        for row in cur:
            item_id = row["itemID"]
            data = _get_item_data(conn, item_id)
            title = data.get("title", "")
            if not title:
                continue

            creators = _get_creators(conn, item_id)
            item_attachments = attachments.get(item_id, [])

            pdf_path = ""
            si_paths = []
            for att in item_attachments:
                full = resolve_path(att["key"], att["path"], zotero_storage)
                if not full or not os.path.exists(full):
                    continue
                if is_si(os.path.basename(full)):
                    si_paths.append(full)
                elif att["type"] == "application/pdf":
                    if not pdf_path:
                        pdf_path = full
                    else:
                        si_paths.append(full)

            stats["total"] += 1
            if pdf_path:
                stats["with_pdf"] += 1
            else:
                stats["without_pdf"] += 1
            if si_paths:
                stats["with_si"] += 1

            papers.append({
                "key": row["key"], "itemType": row["typeName"],
                "title": title, "year": data.get("date", "")[:4] if data.get("date") else None,
                "doi": data.get("DOI", ""), "journal": data.get("publicationTitle", ""),
                "authors": creators, "pdfPath": pdf_path, "siPaths": si_paths,
                "tags": _get_tags(conn, item_id),
                "collections": _get_collections(conn, item_id),
            })

        # SI matching for standalone PDFs not linked via parentItemID
        standalone_pdfs = []
        for att in all_standalone_attachments:
            full = resolve_path(att["key"], att["path"], zotero_storage)
            if full and os.path.exists(full):
                standalone_pdfs.append({"key": att["key"], "path": full, "filename": os.path.basename(full)})
        papers = match_si_to_paper(papers, standalone_pdfs)

        return papers, stats
    finally:
        conn.close()

if __name__ == "__main__":
    import json, argparse as _ap
    _p = _ap.ArgumentParser(description="Zotero Reader — export paper metadata")
    _p.add_argument("db_path", nargs="?", default=None, help="Path to zotero.sqlite")
    _p.add_argument("-o", "--output", default="outputs/zotero_export.json", help="Output JSON path")
    _args = _p.parse_args()

    db_path = _args.db_path
    if not db_path:
        db_path = os.path.join(os.path.expanduser("~"), "Zotero", "zotero.sqlite")

    papers, stats = export_all(db_path)
    print(f"Papers: {stats['total']} | PDF: {stats['with_pdf']} | No PDF: {stats['without_pdf']} | SI: {stats['with_si']}")

    si_papers = [p for p in papers if p["siPaths"]]
    print(f"\nPapers with SI: {len(si_papers)}")
    for p in si_papers[:8]:
        a = ", ".join([a["lastName"] for a in p["authors"][:2]])
        print(f"  [{p['key']}] {a} ({p['year']}) {p['title'][:50]}")
        for si in p["siPaths"]:
            print(f"    SI: {os.path.basename(si)[:70]}")

    out = _args.output
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        json.dump({"stats": stats, "papers": papers}, f, ensure_ascii=False, indent=2)
    print(f"\nExported: {out} ({os.path.getsize(out)/1024:.1f} KB)")
