# -*- coding: utf-8 -*-
"""
kb Markdown → numpy 向量同步

用法:
    python -m rsk.vector.sync           # 增量同步
    python -m rsk.vector.sync --full    # 全量重建
    python -m rsk.vector.sync --dry-run # 预览变更

存储:
    vector_db/papers_embeddings.npy  — kb_papers (N×1024 float32, L2归一化)
    vector_db/papers_meta.json       — kb_papers 元数据
    vector_db/claims_embeddings.npy  — kb_claims (N×1024 float32, L2归一化)
    vector_db/claims_meta.json       — kb_claims 元数据
"""

import argparse, hashlib, json, os, sys
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen
import numpy as np
from rsk.vector._config import MODEL_PATH
from rsk.vector.model import load_bge_m3
from rsk.vector.papers import build_paper_abstracts

from rsk.config import PROJECT_ROOT, get_kb_dir, get_vector_db_dir
from rsk.kb.coverage import active_modules
KB_DIR = get_kb_dir()
VECTOR_DB_DIR = get_vector_db_dir()
MANIFEST_PATH = VECTOR_DB_DIR / "manifest.json"
SUMMARY_PATH = VECTOR_DB_DIR / "summary.json"
PAPERS_EMB_PATH = VECTOR_DB_DIR / "papers_embeddings.npy"
PAPERS_META_PATH = VECTOR_DB_DIR / "papers_meta.json"
# MODEL_PATH and SENTENCE_TRANSFORMERS_HOME auto-set by _config import
EXCLUDE_FILES = {"REVIEWER_LOG.md", "INDEX.md", "REVIEWER.md", "SCHEMA.md", "qa.md"}
EXCLUDE_DIRS = {".audit", "reference", "coverage"}
SERVER_URL = os.environ.get(
    "RSK_QUERY_SERVER",
    "http://127.0.0.1:8765",
).rstrip("/")
EMBED_PROTOCOL = "rsk-embed-v1"


class EmbeddingServerError(RuntimeError):
    """Stable client-side failure for the optional loopback backend."""


def _loopback_server_url(server_url):
    parsed = urlparse(str(server_url))
    if (
        parsed.scheme != "http"
        or parsed.username
        or parsed.password
        or parsed.hostname not in {"127.0.0.1", "::1", "localhost"}
    ):
        raise ValueError("embedding server URL must use loopback HTTP")
    return str(server_url).rstrip("/")


def _server_healthy(*, server_url=SERVER_URL, timeout=2):
    """Return whether a compatible loopback embedding service is ready."""
    try:
        base_url = _loopback_server_url(server_url)
        with urlopen(f"{base_url}/health", timeout=timeout) as response:
            if response.status != 200:
                return False
            payload = json.loads(response.read().decode("utf-8"))
        return (
            payload.get("status") == "ok"
            and payload.get("embed_protocol") == EMBED_PROTOCOL
        )
    except Exception:
        return False


def _embed_via_server(
    texts,
    batch_size=64,
    *,
    server_url=SERVER_URL,
    timeout=120,
):
    """Encode texts through the bounded loopback /embed protocol."""
    if not texts:
        return np.empty((0, 0), dtype=np.float32)
    if (
        isinstance(batch_size, bool)
        or not isinstance(batch_size, int)
        or not 1 <= batch_size <= 64
    ):
        raise ValueError("batch_size must be an integer from 1 to 64")
    base_url = _loopback_server_url(server_url)
    batches = []
    dimension = None
    for start in range(0, len(texts), batch_size):
        batch = list(texts[start : start + batch_size])
        body = json.dumps(
            {"texts": batch, "batch_size": batch_size},
            ensure_ascii=False,
        ).encode("utf-8")
        request = Request(
            f"{base_url}/embed",
            data=body,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with urlopen(request, timeout=timeout) as response:
                media_type = response.headers.get_content_type()
                if response.status != 200 or media_type != "application/json":
                    raise EmbeddingServerError(
                        "server returned an incompatible response"
                    )
                payload = json.loads(response.read().decode("utf-8"))
        except HTTPError as exc:
            raise EmbeddingServerError(
                f"server returned HTTP {exc.code}"
            ) from exc
        except (URLError, OSError, TimeoutError) as exc:
            raise EmbeddingServerError("server request failed") from exc
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise EmbeddingServerError("server returned invalid JSON") from exc

        embeddings = np.asarray(payload.get("embeddings"), dtype=np.float32)
        reported_dimension = payload.get("dimension")
        if (
            payload.get("count") != len(batch)
            or embeddings.ndim != 2
            or embeddings.shape[0] != len(batch)
            or embeddings.shape[1] == 0
            or reported_dimension != embeddings.shape[1]
            or not np.isfinite(embeddings).all()
        ):
            raise EmbeddingServerError(
                "server returned invalid embedding metadata"
            )
        if dimension is None:
            dimension = embeddings.shape[1]
        elif dimension != embeddings.shape[1]:
            raise EmbeddingServerError(
                "server changed embedding dimension between batches"
            )
        batches.append(embeddings)
    return np.vstack(batches)


def _get_embed_model(*, server_url=SERVER_URL):
    """Return an encoder and mutable state recording the actual backend."""
    state = {
        "embedding_backend": "server",
        "embedding_fallback_reason": "",
    }
    local_model = None

    def local_encode(texts, batch_size=64):
        nonlocal local_model
        if local_model is None:
            print(f"Loading bge-m3 locally from {MODEL_PATH}...")
            local_model = load_bge_m3()
        return np.asarray(
            local_model.encode(
                texts,
                batch_size=batch_size,
                show_progress_bar=False,
                normalize_embeddings=True,
            ),
            dtype=np.float32,
        )

    if not _server_healthy(server_url=server_url):
        state["embedding_backend"] = "local"
        state["embedding_fallback_reason"] = "server_unavailable"
        return local_encode, state

    print("Using loopback query server for embeddings.")

    def server_then_local(texts, batch_size=64):
        try:
            return _embed_via_server(
                texts,
                batch_size=batch_size,
                server_url=server_url,
            )
        except EmbeddingServerError as exc:
            state["embedding_backend"] = "local"
            state["embedding_fallback_reason"] = (
                f"server_embed_failed: {exc}"
            )
            print(
                "Loopback embedding failed; falling back to the local model "
                f"({exc})."
            )
            return local_encode(texts, batch_size=batch_size)

    return server_then_local, state

def hash_file(filepath):
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()

def scan_kb_files(kb_dir=None):
    root = Path(kb_dir).resolve() if kb_dir is not None else KB_DIR
    files = {}
    for md in root.rglob("*.md"):
        rel = md.relative_to(root)
        parts = rel.parts
        if parts[0] in EXCLUDE_DIRS or rel.name in EXCLUDE_FILES:
            continue
        if any(p.startswith(".") for p in parts):
            continue
        files[str(rel).replace("\\", "/")] = hash_file(md)
    return files


def affected_module_files(changed_files, *, workspace):
    """Select changed active module files, excluding metadata and legacy files."""
    configured = {
        str(module["file"])
        for module in active_modules(Path(workspace))
    }
    return {
        Path(file_name).name
        for file_name in changed_files
        if Path(file_name).name in configured
    }

def sync_vectors(full=False, dry_run=False):
    VECTOR_DB_DIR.mkdir(parents=True, exist_ok=True)
    current_files = scan_kb_files()

    # Load existing paper-level metadata for integrity and change statistics.
    existing_papers = []
    if PAPERS_META_PATH.exists() and not full:
        with open(PAPERS_META_PATH, "r", encoding="utf-8") as f:
            existing_papers = json.load(f)
        if not PAPERS_EMB_PATH.exists():
            raise RuntimeError(
                "papers_meta.json exists but papers_embeddings.npy is missing. "
                "Run sync_vectors.py --full to rebuild."
            )
        existing_embeddings = np.load(PAPERS_EMB_PATH)
        if len(existing_papers) != len(existing_embeddings):
            raise RuntimeError(
                "papers_meta.json and papers_embeddings.npy have different row counts. "
                "Run sync_vectors.py --full to rebuild."
            )
    paper_index_current = (
        not full
        and PAPERS_META_PATH.is_file()
        and PAPERS_EMB_PATH.is_file()
        and all(
            {
                "chunk_id",
                "paper_id",
                "abstract",
                "roles",
                "module_names",
                "n_records",
            }
            <= set(paper)
            for paper in existing_papers
        )
    )

    manifest = {}
    if MANIFEST_PATH.exists() and not full:
        with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
            manifest = json.load(f)

    new_files = {k: v for k, v in current_files.items() if k not in manifest}
    changed_files = {k: v for k, v in current_files.items() if k in manifest and manifest[k] != v}
    deleted_files = [k for k in manifest if k not in current_files]

    stats = {"total_files": len(current_files), "new_files": len(new_files),
        "changed_files": len(changed_files), "deleted_files": len(deleted_files),
        "new_chunks": 0, "updated_chunks": 0, "deleted_chunks": 0,
        "paper_count": len(existing_papers),
        "paper_rebuild_required": not paper_index_current,
        "_new_file_names": list(new_files.keys()),
        "_changed_file_names": list(changed_files.keys()),
        "_deleted_file_names": deleted_files}

    if dry_run:
        print(json.dumps(stats, indent=2, ensure_ascii=False))
        return stats

    if (
        not new_files
        and not changed_files
        and not deleted_files
        and paper_index_current
    ):
        print("No changes detected.")
        # Rewrite summary.json to clear stale state fields left by previous
        # runs (paper_rebuild_required=true after a successful rebuild,
        # embedding_fallback_reason from an old server outage); they mislead
        # diagnostics without any gate consuming them.
        stale = {}
        if SUMMARY_PATH.exists():
            try:
                stale = json.loads(SUMMARY_PATH.read_text(encoding="utf-8"))
            except (OSError, ValueError):
                stale = {}
        stats["paper_rebuild_required"] = False
        stats["embedding_backend"] = stale.get("embedding_backend", "")
        stats.pop("embedding_fallback_reason", None)
        with open(SUMMARY_PATH, "w", encoding="utf-8") as f:
            json.dump(stats, f, indent=2, ensure_ascii=False)
        return stats

    encode, embedding_state = _get_embed_model()

    # Any KB change can affect a cross-module paper summary, so rebuild the
    # small paper-level collection deterministically from every active module.
    abstracts = build_paper_abstracts(PROJECT_ROOT)
    texts = [str(item["abstract"]) for item in abstracts]
    if texts:
        all_embeddings = np.asarray(
            encode(texts, batch_size=64),
            dtype=np.float32,
        )
        if (
            all_embeddings.ndim != 2
            or all_embeddings.shape[0] != len(abstracts)
        ):
            raise RuntimeError(
                "paper abstract encoder returned an invalid row count"
            )
    else:
        all_embeddings = np.empty((0, 0), dtype=np.float32)

    all_papers = [
        {
            "chunk_id": str(item["paper_id"]),
            **item,
        }
        for item in abstracts
    ]
    existing_by_id = {
        str(item.get("chunk_id", "")): item
        for item in existing_papers
        if item.get("chunk_id")
    }
    current_by_id = {
        str(item["chunk_id"]): item
        for item in all_papers
    }
    stats["new_chunks"] = len(set(current_by_id) - set(existing_by_id))
    stats["deleted_chunks"] = len(set(existing_by_id) - set(current_by_id))
    stats["updated_chunks"] = sum(
        existing_by_id[chunk_id] != current_by_id[chunk_id]
        for chunk_id in set(existing_by_id) & set(current_by_id)
    )
    stats["paper_count"] = len(all_papers)
    # Papers were just rebuilt: the rebuild-required flag must not linger.
    stats["paper_rebuild_required"] = False

    # Save embeddings
    np.save(PAPERS_EMB_PATH, all_embeddings.astype(np.float32))

    # Save metadata (without embeddings)
    with open(PAPERS_META_PATH, "w", encoding="utf-8") as f:
        json.dump(all_papers, f, ensure_ascii=False)

    # Update manifest and summary
    with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
        json.dump(current_files, f, indent=2, ensure_ascii=False)
    stats.update(embedding_state)
    with open(SUMMARY_PATH, "w", encoding="utf-8") as f:
        json.dump(stats, f, indent=2, ensure_ascii=False)

    print(
        f"Paper abstracts sync done: {stats['new_chunks']} new, "
        f"{stats['updated_chunks']} updated, "
        f"{stats['deleted_chunks']} deleted; "
        f"embedding_backend={stats['embedding_backend']}"
    )
    return stats

def sync_claims(full=False, dry_run=False, affected_files=None):
    """Embed claims index (JSONL) into numpy arrays for local cosine retrieval.

    When affected_files is provided and full=False, performs incremental update:
    removes old claims from those source files and embeds only new ones.
    """
    import json as _json
    import numpy as np

    claims_path = PROJECT_ROOT / "outputs" / "claims_index.jsonl"
    if not claims_path.exists():
        print("claims_index.jsonl not found. Run build_claims first.", file=sys.stderr)
        return None

    claims = []
    with open(claims_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                claims.append(_json.loads(line))

    if dry_run:
        print(f"[dry-run] Would embed {len(claims)} claims.")
        return {"total_claims": len(claims)}

    is_incremental = not full and affected_files and len(affected_files) > 0

    if is_incremental:
        # Load existing claims and remove old entries from affected files
        emb_path = VECTOR_DB_DIR / "claims_embeddings.npy"
        meta_path = VECTOR_DB_DIR / "claims_meta.json"
        if emb_path.exists() and meta_path.exists():
            existing_embeddings = np.load(emb_path)
            with open(meta_path, "r", encoding="utf-8") as f:
                existing_metas = _json.load(f)
            # Keep only claims whose source_file is NOT in affected_files.
            # Chain claims (source_file="chain") are cross-module composites and
            # are always fully regenerated by build_index, so drop them here too
            # to avoid stale duplicates after every incremental sync.
            affected_set = set(affected_files) | {"chain"}
            keep_mask = [m.get("source_file", "") not in affected_set for m in existing_metas]
            keep_embeddings = existing_embeddings[keep_mask]
            keep_metas = [m for m, k in zip(existing_metas, keep_mask) if k]
            removed = len(existing_metas) - len(keep_metas)
            print(f"[claims:incremental] Kept {len(keep_metas)} existing claims, removed {removed} from {affected_files}")
        else:
            # First run with incremental mode — fall back to full embed
            print("[claims:incremental] No existing claims found, falling back to full embed.")
            keep_embeddings = np.empty((0, 0), dtype=np.float32)
            keep_metas = []
    else:
        keep_embeddings = np.empty((0, 0), dtype=np.float32)
        keep_metas = []

    encode, embedding_state = _get_embed_model()

    texts = [
        c.get("retrieval_text", c.get("claim_text", ""))
        for c in claims
    ]
    embeddings = encode(texts, batch_size=64)
    new_metas = []
    for claim in claims:
        metadata = {
            "record_id": claim["record_id"],
            "paper_id": claim["paper_id"],
            "module": claim["module"],
            "source_file": claim["source_file"],
            "claim_text": claim.get(
                "claim_text",
                claim.get("retrieval_text", ""),
            ),
            "retrieval_text": claim.get(
                "retrieval_text",
                claim.get("claim_text", ""),
            ),
            "claim_type": claim.get("claim_type", ""),
        }
        if "source_metadata" in claim:
            metadata["source_metadata"] = claim["source_metadata"]
        new_metas.append(metadata)

    # Merge: old kept + new
    if is_incremental and len(keep_metas) > 0:
        all_embeddings = np.vstack([keep_embeddings, embeddings])
        all_metas = keep_metas + new_metas
        print(f"[claims:incremental] Merged: {len(keep_metas)} kept + {len(new_metas)} new = {len(all_metas)} total claims")
    else:
        all_embeddings = embeddings
        all_metas = new_metas

    # Save
    emb_path = VECTOR_DB_DIR / "claims_embeddings.npy"
    np.save(emb_path, all_embeddings.astype(np.float32))

    meta_path = VECTOR_DB_DIR / "claims_meta.json"
    with open(meta_path, "w", encoding="utf-8") as f:
        _json.dump(all_metas, f, ensure_ascii=False)

    stats = {
        "total_claims": len(all_metas),
        "new_embedded": len(new_metas),
        **embedding_state,
    }
    print(
        f"Claims sync done: {len(all_metas)} claims saved to "
        f"{emb_path.name} + {meta_path.name}; "
        f"embedding_backend={stats['embedding_backend']}"
    )
    return stats


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--full", action="store_true", help="Full rebuild")
    p.add_argument("--dry-run", action="store_true", help="Preview without writing")
    p.add_argument("--from-claims", action="store_true", help="Build claims_embeddings.npy + claims_meta.json from claims_index.jsonl")
    p.add_argument("--skip-claims", action="store_true", help="Skip auto-rebuild of claims index (default: auto-rebuild)")
    args = p.parse_args()
    if args.from_claims:
        if args.full:
            # --from-claims --full must rebuild the source JSONL first,
            # otherwise it re-embeds stale claim texts after build_claim
            # changes (the previous behavior looked like the fix did nothing).
            from rsk.vector.claims import build_index as build_claims_index

            output_path = str(PROJECT_ROOT / "outputs" / "claims_index.jsonl")
            print("\n[auto] Rebuilding claims index (full, --from-claims --full)...")
            build_claims_index(output_path=output_path)
        sync_claims(full=args.full, dry_run=args.dry_run)
    else:
        result = sync_vectors(full=args.full, dry_run=args.dry_run)
        if not args.dry_run and result and not args.skip_claims:
            # Determine which kb source files were affected
            affected_raw = []
            if isinstance(result, dict):
                affected_raw = result.get("_new_file_names", []) + result.get("_changed_file_names", [])
            affected_source_files = affected_module_files(
                affected_raw,
                workspace=PROJECT_ROOT,
            )
            # Auto-rebuild claims index via direct function call
            from rsk.vector.claims import build_index as build_claims_index
            output_path = str(PROJECT_ROOT / "outputs" / "claims_index.jsonl")
            if args.full or not affected_source_files:
                # Full rebuild: all modules
                print("\n[auto] Rebuilding claims index (full)...")
                build_claims_index(output_path=output_path)
                sync_claims(full=True, dry_run=False)
            else:
                # Incremental rebuild: only affected files
                files_arg = ",".join(sorted(affected_source_files))
                print(f"\n[auto] Rebuilding claims index (incremental: {files_arg})...")
                build_claims_index(output_path=output_path, file_filter=list(affected_source_files))
                sync_claims(full=False, dry_run=False,
                            affected_files=list(affected_source_files))
