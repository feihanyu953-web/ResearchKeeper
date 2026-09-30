# -*- coding: utf-8 -*-
"""
numpy 语义查询 — LitMind 检索入口

用法:
    python -m rsk.vector.query "界面水氢键网络如何影响PCET"
    python -m rsk.vector.query "Cs+ PMF 最小值" --top 5 --json
    echo "阳离子尺寸对吸附能的影响" | python -m rsk.vector.query --stdin
"""

import argparse, json, os, re, sys
from collections import defaultdict
import numpy as np
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import urlopen

# Force UTF-8 on Windows consoles to avoid GBK encoding errors
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

from rsk.config import PROJECT_ROOT, get_runtime_paths, get_vector_db_dir
VECTOR_DB_DIR = get_vector_db_dir()
from rsk.vector._config import DEVICE, retrieval_value
from rsk.vector.model import load_bge_m3
QUERY_SERVER_URL = os.environ.get("RSK_QUERY_SERVER", "http://127.0.0.1:8765")

# Keyword-overlap boost and module diversity quota for claim retrieval.
# Compensate pure-cosine bias toward long descriptive records; resolve via
# workspace configs/retrieval.yaml, env vars (RSK_KEYWORD_BOOST /
# RSK_QUOTA_*), then built-in defaults.
KEYWORD_BOOST = float(retrieval_value("keyword_boost", "0.45"))
QUOTA_MODULE_CAPS = {
    "literature": int(retrieval_value("quota_literature", "2")),
    "chain": int(retrieval_value("quota_chain", "1")),
    "claims": int(retrieval_value("quota_claims", "2")),
}

_CJK_RUN = re.compile(r"[一-鿿]+")


def _query_keyword_tokens(text: str) -> set[str]:
    """Tokenize text for keyword overlap without a tokenizer dependency.

    English words are lowercased; contiguous CJK runs are split into
    overlapping 3-grams (2-char runs kept as-is; single chars dropped).
    """
    tokens: set[str] = set()
    tokens.update(re.findall(r"[a-z0-9]+", text.lower()))
    for run in _CJK_RUN.findall(text):
        run_len = len(run)
        if run_len >= 3:
            tokens.update(run[i : i + 3] for i in range(run_len - 2))
        elif run_len == 2:
            tokens.add(run)
    return tokens


def _keyword_overlap(question: str, doc_text: str) -> float:
    """Fraction of query tokens also present in the document (0..1)."""
    query_tokens = _query_keyword_tokens(question)
    if not query_tokens:
        return 0.0
    doc_tokens = _query_keyword_tokens(doc_text)
    if not doc_tokens:
        return 0.0
    return len(query_tokens & doc_tokens) / len(query_tokens)


def format_json_results(question, collection_name, results):
    output = {"query": question, "collection": collection_name, "results": []}
    for i in range(len(results["ids"][0])):
        meta = results["metadatas"][0][i]
        result = {
            "rank": i + 1,
            "chunk_id": results["ids"][0][i],
            "text": results["documents"][0][i][:500] + (
                "..." if len(results["documents"][0][i]) > 500 else ""),
        }
        # claims collection metadata
        if "record_id" in meta and meta.get("record_id"):
            result["record_id"] = meta["record_id"]
            result["paper_id"] = meta.get("paper_id", "?")
            result["module"] = meta.get("module", "?")
            result["source_file"] = meta.get("source_file", "?")
            result["claim_type"] = meta.get("claim_type", "")
        elif "paper_id" in meta:
            result["paper_id"] = meta.get("paper_id", "?")
            result["roles"] = list(meta.get("roles") or ())
            result["module_names"] = list(meta.get("module_names") or ())
            result["n_records"] = meta.get("n_records", 0)
        else:
            result["source"] = meta.get("source", "?")
            result["section"] = meta.get("section", "?")
        output["results"].append(result)
    return output


def print_results(output, use_claims=False):
    print(f"Query: {output['query']}\n")
    for item in output["results"]:
        text = item["text"][:400]
        prefix = ""
        if use_claims:
            if item.get("claim_type") == "system_synthesized_chain":
                prefix = "[导航节点] "
            print(f"{prefix}[{item['rank']}] {item.get('record_id', item['chunk_id'])} | "
                  f"paper={item.get('paper_id', '?')} | {item.get('module', '?')} | "
                  f"{item.get('source_file', '?')}")
        elif "paper_id" in item:
            print(
                f"[{item['rank']}] {item.get('paper_id', '?')} | "
                f"modules={len(item.get('module_names', ()))} | "
                f"records={item.get('n_records', 0)}"
            )
        else:
            print(
                f"[{item['rank']}] {item.get('source', '?')} | "
                f"{item.get('section', '?')}"
            )
        print(f"    {text}{'...' if len(item['text']) > 400 else ''}\n")
    enumeration = output.get("enumeration")
    if enumeration:
        fields = ", ".join(enumeration["scan_fields"])
        print(
            "Deterministic lexical supplement: "
            f"{enumeration['lexical_match_count']} matches across {fields}."
        )
        print(f"Limitation: {enumeration['limitation']}\n")


def _ordered_modules(by_module, module_order=None):
    if not module_order:
        return by_module
    ordered = {}
    for module in module_order:
        if module in by_module:
            ordered[module] = by_module[module]
    for module, claims in by_module.items():
        if module not in ordered:
            ordered[module] = claims
    return ordered


def expand_papers_from_meta(hits, claims_meta_path, module_order=None):
    """Expand top-k hits to include all claims from the same papers.

    Args:
        hits: list of hit dicts from format_json_results (must have paper_id)
        claims_meta_path: path to claims_meta.json

    Returns:
        dict: {paper_id: {module: [claim_text, ...]}}
    """
    import json as _json
    paper_ids = {h.get("paper_id") for h in hits if h.get("paper_id") and h["paper_id"] != "?"}
    if not paper_ids:
        return {}

    with open(claims_meta_path, "r", encoding="utf-8") as f:
        all_metas = _json.load(f)

    expanded = {}
    for pid in sorted(paper_ids):
        paper_claims = [m for m in all_metas if m.get("paper_id") == pid]
        by_module = {}
        for c in paper_claims:
            mod = c.get("module", "unknown")
            claim_text = c.get("claim_text", "")
            if mod not in by_module:
                by_module[mod] = []
            by_module[mod].append(claim_text)
        if by_module:
            expanded[pid] = _ordered_modules(by_module, module_order)
    return expanded


def print_expanded_results(expanded, module_order=None):
    """Print expanded paper context in human-readable format."""
    if not expanded:
        return
    if module_order is None:
        from rsk.config import get_module_names

        module_order = tuple(get_module_names())
    for pid, modules in expanded.items():
        print(f"\n=== {pid} — 完整论文画像 ===")
        for mod, claims in _ordered_modules(modules, module_order).items():
            for claim in claims[:5]:
                print(f"  [{mod}] {claim[:200]}")
        print()


def query_server(question, top_k=5, use_claims=False, timeout=2.0, expand=False):
    params = urlencode({"q": question, "top": top_k, "claims": int(use_claims), "expand": int(expand)})
    with urlopen(f"{QUERY_SERVER_URL}/query?{params}", timeout=timeout) as response:
        if response.status != 200:
            raise RuntimeError(f"server returned HTTP {response.status}")
        return json.loads(response.read().decode("utf-8"))


_STALE_SERVER_CHECKED = False


def _warn_if_server_stale() -> None:
    """Warn once when the running server's code version differs from ours.

    The persistent server loads code/indexes at startup and never reloads;
    querying it after an upgrade silently returns stale results, which reads
    as "the fix did nothing". Warn so the operator restarts it (rsk serve)
    or bypasses it (--no-server).
    """
    global _STALE_SERVER_CHECKED
    if _STALE_SERVER_CHECKED:
        return
    _STALE_SERVER_CHECKED = True
    from rsk.vector._config import code_version

    try:
        with urlopen(f"{QUERY_SERVER_URL}/health", timeout=1.0) as response:
            if response.status != 200:
                return
            health = json.loads(response.read().decode("utf-8"))
    except Exception:
        return  # server unreachable; query_server() will fall back
    server_version = health.get("code_version")
    if server_version and server_version != code_version():
        print(
            "WARN: running query server reports code version "
            f"{server_version}, current sources are {code_version()}; "
            "results may be stale. Restart the server (rsk serve) or use "
            "--no-server.",
            file=sys.stderr,
        )


def query_local(question, top_k=5, use_claims=False):
    if not VECTOR_DB_DIR.exists():
        print("[ERROR] vector_db not found. Run sync_vectors.py first.", file=sys.stderr)
        sys.exit(1)

    model = load_bge_m3(device=DEVICE)
    q_emb = model.encode([question], show_progress_bar=False, normalize_embeddings=True)[0]

    if use_claims:
        return _query_claims_numpy(question, q_emb, top_k)
    else:
        return _query_papers_numpy(question, q_emb, top_k)


def _query_claims_numpy(question, q_emb, top_k):
    """Query claims via numpy cosine similarity with keyword boost + quota."""
    import numpy as np
    emb_path = VECTOR_DB_DIR / "claims_embeddings.npy"
    meta_path = VECTOR_DB_DIR / "claims_meta.json"
    if not emb_path.exists() or not meta_path.exists():
        print("[ERROR] claims_embeddings.npy or claims_meta.json not found. "
              "Run sync_vectors.py --from-claims first.", file=sys.stderr)
        sys.exit(1)

    embeddings = np.load(emb_path)  # (N, 1024), already L2-normalized
    with open(meta_path, "r", encoding="utf-8") as f:
        metas = json.load(f)

    # Cosine similarity = dot product (both normalized)
    scores = np.dot(embeddings, q_emb)  # (N,)
    # Keyword overlap boost: long descriptive records otherwise act as
    # global attractors; add KEYWORD_BOOST × query-token overlap rate.
    doc_texts = [
        metas[i].get("retrieval_text") or metas[i].get("claim_text", "")
        for i in range(len(metas))
    ]
    boosts = np.asarray(
        [KEYWORD_BOOST * _keyword_overlap(question, text) for text in doc_texts],
        dtype=float,
    )
    blended = scores + boosts

    # Diversity quota: paper-level composites (literature index / chain /
    # claims statements) cap their seats so module-specific records can
    # still enter top-k.
    order = np.argsort(blended)[::-1]
    counts: dict[str, int] = defaultdict(int)
    chosen: list[int] = []
    for idx in order:
        if len(chosen) >= top_k:
            break
        module = metas[idx].get("module", "")
        cap = QUOTA_MODULE_CAPS.get(module)
        if cap is not None and counts[module] >= cap:
            continue
        chosen.append(idx)
        counts[module] += 1
    top_idx = np.asarray(chosen, dtype=int)

    # Build result dict (compatible with format_json_results)
    results = {
        "ids": [[metas[i]["record_id"] for i in top_idx]],
        "documents": [[metas[i].get("claim_text", "") for i in top_idx]],
        "metadatas": [[{
            "record_id": metas[i]["record_id"],
            "paper_id": metas[i]["paper_id"],
            "module": metas[i]["module"],
            "source_file": metas[i]["source_file"],
            "claim_type": metas[i].get("claim_type", ""),
        } for i in top_idx]],
    }
    return format_json_results(question, "kb_claims", results)


def _query_papers_numpy(question, q_emb, top_k):
    """Query kb_papers via numpy cosine similarity."""
    emb_path = VECTOR_DB_DIR / "papers_embeddings.npy"
    meta_path = VECTOR_DB_DIR / "papers_meta.json"
    if not emb_path.exists() or not meta_path.exists():
        print("[ERROR] papers_embeddings.npy or papers_meta.json not found. "
              "Run sync_vectors.py first.", file=sys.stderr)
        sys.exit(1)

    embeddings = np.load(emb_path)
    with open(meta_path, "r", encoding="utf-8") as f:
        metas = json.load(f)

    scores = np.dot(embeddings, q_emb)
    top_idx = np.argsort(scores)[::-1][:top_k]

    documents = [
        metas[i].get("abstract", metas[i].get("text", ""))
        for i in top_idx
    ]
    paper_metadata = []
    for i in top_idx:
        meta = metas[i]
        if "paper_id" in meta:
            paper_metadata.append(
                {
                    "paper_id": meta["paper_id"],
                    "roles": list(meta.get("roles") or ()),
                    "module_names": list(meta.get("module_names") or ()),
                    "n_records": meta.get("n_records", 0),
                }
            )
        else:
            paper_metadata.append(
                {
                    "source": meta.get("source", "?"),
                    "section": meta.get("section", "?"),
                }
            )
    results = {
        "ids": [[metas[i]["chunk_id"] for i in top_idx]],
        "documents": [documents],
        "metadatas": [paper_metadata],
    }
    return format_json_results(question, "kb_papers", results)


def query(
    question,
    top_k=5,
    json_out=False,
    use_claims=False,
    no_server=False,
    expand=False,
    enumerate_all=False,
    scan_terms=None,
):
    effective_claims = use_claims or enumerate_all
    terms = list(scan_terms or ())
    if enumerate_all and not terms:
        raise ValueError(
            "explicit enumeration requires at least one --scan-term"
        )
    output = None
    if not no_server:
        _warn_if_server_stale()
        try:
            output = query_server(
                question,
                top_k=top_k,
                use_claims=effective_claims,
                expand=expand,
            )
        except Exception:
            output = None
    if output is None:
        output = query_local(
            question,
            top_k=top_k,
            use_claims=effective_claims,
        )

    if enumerate_all:
        from rsk.kb.scanner import (
            merge_with_vector_results,
            scan_records,
        )

        lexical = scan_records(
            get_runtime_paths().workspace,
            terms,
            match_all=True,
        )
        output = merge_with_vector_results(output, lexical)

    # Expand: pull all claims from same papers (local fallback if server didn't)
    expanded = None
    if expand and use_claims and "expanded" not in output:
        claims_meta_path = VECTOR_DB_DIR / "claims_meta.json"
        if claims_meta_path.exists():
            from rsk.config import get_module_names

            expanded = expand_papers_from_meta(
                output.get("results", []),
                claims_meta_path,
                module_order=tuple(get_module_names()),
            )
            output["expanded"] = expanded
    elif expand and "expanded" in output:
        expanded = output["expanded"]

    if json_out:
        json.dump(output, sys.stdout, ensure_ascii=False, indent=2)
        sys.stdout.write("\n")
    else:
        if expanded:
            print_expanded_results(expanded)
        print_results(output, use_claims=effective_claims)

    return output


def main():
    p = argparse.ArgumentParser(description="LitMind Vector Query")
    p.add_argument("question", nargs="?", help="Natural language query")
    p.add_argument("--stdin", action="store_true", help="Read query from stdin")
    p.add_argument("--top", type=int, default=5, help="Top-k results (default: 5)")
    p.add_argument("--json", action="store_true", dest="json_out", help="JSON output")
    p.add_argument("--claims", action="store_true", help="Query kb_claims collection (claims index)")
    p.add_argument("--expand", action="store_true", help="Expand results to include all modules from same papers")
    p.add_argument("--no-server", action="store_true", help="Disable localhost server lookup")
    p.add_argument(
        "--enumerate",
        action="store_true",
        dest="enumerate_all",
        help="Explicitly merge claims retrieval with deterministic KB scanning",
    )
    p.add_argument(
        "--scan-term",
        action="append",
        default=[],
        help="Lexical term or numeric comparator for --enumerate (repeatable)",
    )
    args = p.parse_args()

    question = args.question
    if args.stdin:
        question = sys.stdin.read().strip()
    if not question:
        p.error("No query provided. Pipe via stdin or pass as argument.")

    query(question, top_k=args.top, json_out=args.json_out,
          use_claims=args.claims, no_server=args.no_server, expand=args.expand,
          enumerate_all=args.enumerate_all, scan_terms=args.scan_term)


if __name__ == "__main__":
    main()
