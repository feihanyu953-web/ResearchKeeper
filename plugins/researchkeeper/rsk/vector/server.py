# -*- coding: utf-8 -*-
"""
Persistent LitMind vector query server.

The command-line query path reloads bge-m3 for every request. This server keeps
the embedding model and vector data warm, then exposes the same query shape
over a localhost-only HTTP endpoint.

Usage:
    python -m rsk.vector.server
    python -m rsk.vector.query "界面水氢键网络如何影响 PCET" --claims --json
"""

import argparse
import ipaddress
import json
import os
import socket
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

import numpy as np


from rsk.config import PROJECT_ROOT, get_module_names
from rsk.vector._config import MODEL_HOME, MODEL_PATH, DEVICE, code_version
from rsk.vector.model import load_bge_m3
from rsk.vector.query import _ordered_modules

PROJECT_ROOT = Path(PROJECT_ROOT)  # ensure Path object
VECTOR_DB_DIR = PROJECT_ROOT / "vector_db"
DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 8765
EMBED_PROTOCOL = "rsk-embed-v1"
MAX_EMBED_BODY_BYTES = 1024 * 1024
MAX_EMBED_TEXTS = 128
MAX_EMBED_TEXT_CHARS = 8192
MAX_EMBED_BATCH_SIZE = 64


def validate_server_bind(host):
    """Reject non-loopback binds because /embed has no remote auth layer."""
    normalized = str(host).strip().lower()
    if normalized == "localhost":
        return
    try:
        address = ipaddress.ip_address(normalized)
    except ValueError as exc:
        raise ValueError(
            "embedding server host must be a loopback address"
        ) from exc
    if not address.is_loopback:
        raise ValueError("embedding server host must be a loopback address")


class LitMindQueryService:
    def __init__(self):
        if not VECTOR_DB_DIR.exists():
            raise RuntimeError("vector_db not found. Run sync_vectors.py first.")
        self.module_order = tuple(get_module_names())
        print("Loading bge-m3 embedding model...", flush=True)
        self.model = load_bge_m3()
        # Lazy-load all numpy arrays
        self._claims_embeddings = None
        self._claims_metas = None
        self._papers_embeddings = None
        self._papers_metas = None
        print("LitMind query service is warm.", flush=True)

    def _load_claims(self):
        if self._claims_embeddings is None:
            emb_path = VECTOR_DB_DIR / "claims_embeddings.npy"
            meta_path = VECTOR_DB_DIR / "claims_meta.json"
            if not emb_path.exists():
                raise RuntimeError("claims_embeddings.npy not found. Run sync_vectors.py --from-claims first.")
            self._claims_embeddings = np.load(emb_path)
            with open(meta_path, "r", encoding="utf-8") as f:
                self._claims_metas = json.load(f)

    def _load_papers(self):
        if self._papers_embeddings is None:
            emb_path = VECTOR_DB_DIR / "papers_embeddings.npy"
            meta_path = VECTOR_DB_DIR / "papers_meta.json"
            if not emb_path.exists():
                raise RuntimeError("papers_embeddings.npy not found. Run sync_vectors.py first.")
            self._papers_embeddings = np.load(emb_path)
            with open(meta_path, "r", encoding="utf-8") as f:
                self._papers_metas = json.load(f)

    def _expand_papers(self, hits):
        """Expand top-k hits to include all claims from the same papers."""
        paper_ids = {h.get("paper_id") for h in hits if h.get("paper_id") and h["paper_id"] != "?"}
        if not paper_ids:
            return {}
        expanded = {}
        for pid in sorted(paper_ids):
            paper_claims = [m for m in self._claims_metas if m.get("paper_id") == pid]
            by_module = {}
            for c in paper_claims:
                mod = c.get("module", "unknown")
                claim_text = c.get("claim_text", "")
                if mod not in by_module:
                    by_module[mod] = []
                by_module[mod].append(claim_text)
            if by_module:
                expanded[pid] = _ordered_modules(
                    by_module,
                    self.module_order,
                )
        return expanded

    def query(self, question, top_k=5, use_claims=False, expand=False):
        q_emb = self.model.encode([question], show_progress_bar=False, normalize_embeddings=True)[0]

        if use_claims:
            self._load_claims()
            scores = np.dot(self._claims_embeddings, q_emb)
            top_idx = np.argsort(scores)[::-1][:top_k]
            results = {
                "ids": [[self._claims_metas[i]["record_id"] for i in top_idx]],
                "documents": [[
                    self._claims_metas[i].get("claim_text", "")
                    for i in top_idx
                ]],
                "metadatas": [[{
                    "record_id": self._claims_metas[i]["record_id"],
                    "paper_id": self._claims_metas[i]["paper_id"],
                    "module": self._claims_metas[i]["module"],
                    "source_file": self._claims_metas[i]["source_file"],
                    "claim_type": self._claims_metas[i].get(
                        "claim_type",
                        "",
                    ),
                } for i in top_idx]],
            }
            output = format_results(question, "kb_claims", results)

            # Expand: pull all claims from same papers
            if expand:
                expanded = self._expand_papers(output.get("results", []))
                if expanded:
                    output["expanded"] = expanded

            return output
        else:
            self._load_papers()
            scores = np.dot(self._papers_embeddings, q_emb)
            top_idx = np.argsort(scores)[::-1][:top_k]
            documents = [
                self._papers_metas[i].get(
                    "abstract",
                    self._papers_metas[i].get("text", ""),
                )
                for i in top_idx
            ]
            paper_metadata = []
            for i in top_idx:
                meta = self._papers_metas[i]
                if "paper_id" in meta:
                    paper_metadata.append(
                        {
                            "paper_id": meta["paper_id"],
                            "roles": list(meta.get("roles") or ()),
                            "module_names": list(
                                meta.get("module_names") or ()
                            ),
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
                "ids": [[self._papers_metas[i]["chunk_id"] for i in top_idx]],
                "documents": [documents],
                "metadatas": [paper_metadata],
            }
            return format_results(question, "kb_papers", results)


def format_results(question, collection_name, results):
    output = {"query": question, "collection": collection_name, "results": []}
    if not results.get("ids") or not results["ids"]:
        return output
    for i in range(len(results["ids"][0])):
        meta = results["metadatas"][0][i] or {}
        doc = results["documents"][0][i] or ""
        item = {
            "rank": i + 1,
            "chunk_id": results["ids"][0][i],
            "text": doc[:500] + ("..." if len(doc) > 500 else ""),
        }
        if "record_id" in meta and meta.get("record_id"):
            item["record_id"] = meta["record_id"]
            item["paper_id"] = meta.get("paper_id", "?")
            item["module"] = meta.get("module", "?")
            item["source_file"] = meta.get("source_file", "?")
            item["claim_type"] = meta.get("claim_type", "")
        elif "paper_id" in meta:
            item["paper_id"] = meta.get("paper_id", "?")
            item["roles"] = list(meta.get("roles") or ())
            item["module_names"] = list(meta.get("module_names") or ())
            item["n_records"] = meta.get("n_records", 0)
        else:
            item["source"] = meta.get("source", "?")
            item["section"] = meta.get("section", "?")
        output["results"].append(item)
    return output


class Handler(BaseHTTPRequestHandler):
    service = None

    def _send_json(self, status, payload):
        body = json.dumps(payload, ensure_ascii=False, indent=2).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path == "/health":
            self._send_json(
                200,
                {
                    "status": "ok",
                    "service": "litmind-query",
                    "embed_protocol": EMBED_PROTOCOL,
                    "code_version": code_version(),
                    "device": DEVICE,
                },
            )
            return
        if parsed.path != "/query":
            self._send_json(404, {"error": "not found"})
            return

        params = parse_qs(parsed.query)
        question = (params.get("q") or [""])[0].strip()
        if not question:
            self._send_json(400, {"error": "missing q"})
            return
        try:
            top_k = int((params.get("top") or ["5"])[0])
        except ValueError:
            self._send_json(400, {"error": "top must be an integer"})
            return
        use_claims = (params.get("claims") or ["0"])[0] in {"1", "true", "True"}
        expand = (params.get("expand") or ["0"])[0] in {"1", "true", "True"}

        try:
            payload = self.service.query(question, top_k=top_k, use_claims=use_claims, expand=expand)
        except Exception as exc:
            self._send_json(500, {"error": str(exc)})
            return
        self._send_json(200, payload)

    def do_POST(self):
        parsed = urlparse(self.path)
        if parsed.path != "/embed":
            self._send_json(404, {"error": "not found"})
            return

        media_type = self.headers.get("Content-Type", "").split(";", 1)[
            0
        ].strip().lower()
        if media_type != "application/json":
            self._send_json(415, {"error": "application/json required"})
            return

        try:
            content_length = int(self.headers.get("Content-Length", "0"))
        except ValueError:
            self._send_json(400, {"error": "invalid content length"})
            return
        if content_length <= 0:
            self._send_json(400, {"error": "empty body"})
            return
        if content_length > MAX_EMBED_BODY_BYTES:
            self.rfile.read(min(content_length, MAX_EMBED_BODY_BYTES + 1))
            self._send_json(413, {"error": "request body too large"})
            return

        try:
            data = json.loads(
                self.rfile.read(content_length).decode("utf-8")
            )
        except (UnicodeDecodeError, json.JSONDecodeError):
            self._send_json(400, {"error": "invalid JSON"})
            return
        if not isinstance(data, dict):
            self._send_json(422, {"error": "JSON object required"})
            return

        texts = data.get("texts")
        if not isinstance(texts, list) or not texts:
            self._send_json(
                422,
                {"error": "texts must be a non-empty array"},
            )
            return
        if len(texts) > MAX_EMBED_TEXTS:
            self._send_json(413, {"error": "too many texts"})
            return
        if any(not isinstance(text, str) or not text for text in texts):
            self._send_json(
                422,
                {"error": "texts must contain non-empty strings"},
            )
            return
        if any(len(text) > MAX_EMBED_TEXT_CHARS for text in texts):
            self._send_json(413, {"error": "text too long"})
            return

        batch_size = data.get("batch_size", MAX_EMBED_BATCH_SIZE)
        if (
            isinstance(batch_size, bool)
            or not isinstance(batch_size, int)
            or not 1 <= batch_size <= MAX_EMBED_BATCH_SIZE
        ):
            self._send_json(
                422,
                {"error": "batch_size must be an integer from 1 to 64"},
            )
            return
        if self.service is None or getattr(self.service, "model", None) is None:
            self._send_json(
                503,
                {"error": "embedding model unavailable"},
            )
            return

        try:
            embeddings = np.asarray(
                self.service.model.encode(
                    texts,
                    batch_size=batch_size,
                    show_progress_bar=False,
                    normalize_embeddings=True,
                ),
                dtype=np.float32,
            )
            if (
                embeddings.ndim != 2
                or embeddings.shape[0] != len(texts)
                or embeddings.shape[1] == 0
                or not np.isfinite(embeddings).all()
            ):
                raise ValueError("invalid embedding output")
        except Exception as exc:
            print(
                f"[litmind-query] embed failed: {exc!r}",
                file=sys.stderr,
                flush=True,
            )
            self._send_json(
                503,
                {"error": "embedding model unavailable"},
            )
            return

        self._send_json(
            200,
            {
                "embeddings": embeddings.tolist(),
                "count": len(texts),
                "dimension": int(embeddings.shape[1]),
            },
        )

    def log_message(self, fmt, *args):
        sys.stderr.write("[litmind-query] " + (fmt % args) + "\n")


def _port_in_use(host, port):
    """Return True if host:port is already bound by another process."""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind((host, port))
        return False
    except OSError:
        return True
    finally:
        s.close()


def main():
    parser = argparse.ArgumentParser(description="Persistent LitMind query server")
    parser.add_argument("--host", default=DEFAULT_HOST)
    parser.add_argument("--port", type=int, default=DEFAULT_PORT)
    args = parser.parse_args()
    validate_server_bind(args.host)

    if _port_in_use(args.host, args.port):
        print(f"Port {args.host}:{args.port} is already in use. "
              f"litmind_query_server may already be running.", file=sys.stderr, flush=True)
        sys.exit(1)

    try:
        Handler.service = LitMindQueryService()
        print(f"DEVICE={DEVICE} code_version={code_version()}", flush=True)
        print(f"Binding HTTP server on {args.host}:{args.port}...", flush=True)
        server = ThreadingHTTPServer((args.host, args.port), Handler)
        print(f"LitMind query server listening on http://{args.host}:{args.port}", flush=True)
        print(
            "Health: /health | Query: /query?q=...&claims=1&top=5 "
            "| Embed: POST /embed",
            flush=True,
        )
        server.serve_forever()
    except Exception as exc:
        print(f"LitMind query server failed: {exc}", file=sys.stderr, flush=True)
        raise


if __name__ == "__main__":
    main()
