"""Pinned bge-m3 download, identity verification, and device-aware loading."""

from __future__ import annotations

import os
from pathlib import Path
import shutil
import subprocess
from typing import Any, Callable

from rsk.vector._config import DEVICE, MODEL_HOME, MODEL_PATH
from rsk.vector.model_manifest import (
    MODEL_ID,
    load_model_manifest,
    model_status,
    validate_model_revision,
    write_model_manifest,
)


_DEFAULT = object()

_MODELSCOPE_REPO_URL_TEMPLATE = "https://www.modelscope.cn/{model_id}.git"


def _resolve_modelscope_revision(model_id: str) -> str:
    """Resolve the immutable master commit hash of a ModelScope model repo.

    ModelScope ``snapshot_download`` requires an immutable commit hash so the
    snapshot stays auditable; a moving ref like a branch name is rejected by
    :func:`validate_model_revision`. A first install has no way to know that
    hash in advance, so resolve it from the remote before downloading. Uses
    ``git ls-remote`` (Git for Windows / most POSIX systems); no third-party
    dependency is required.
    """
    repo_url = _MODELSCOPE_REPO_URL_TEMPLATE.format(model_id=model_id)
    try:
        proc = subprocess.run(
            ["git", "ls-remote", repo_url, "HEAD"],
            capture_output=True,
            text=True,
            timeout=60,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise RuntimeError(
            "Failed to resolve ModelScope master revision for "
            f"{model_id} (git unavailable or timed out: {exc}). "
            "Resolve it manually and retry with "
            "RSK_BGE_MODELSCOPE_REVISION=<commit-hash>, e.g. run:\n"
            f"  git ls-remote {repo_url} HEAD"
        ) from exc
    if proc.returncode != 0:
        raise RuntimeError(
            f"Failed to resolve ModelScope master revision for {model_id}: "
            f"{proc.stderr.strip() or 'git ls-remote failed'}. "
            "Resolve it manually and retry with "
            "RSK_BGE_MODELSCOPE_REVISION=<commit-hash>, e.g. run:\n"
            f"  git ls-remote {repo_url} HEAD"
        )
    lines = [line for line in proc.stdout.splitlines() if line.strip()]
    if not lines:
        raise RuntimeError(
            f"ModelScope did not return a commit for {model_id}. "
            "Resolve it manually and retry with "
            "RSK_BGE_MODELSCOPE_REVISION=<commit-hash>."
        )
    revision = lines[0].split()[0]
    validate_model_revision(revision)
    return revision


def _resolve_huggingface_revision(model_id: str) -> str:
    from huggingface_hub import HfApi

    revision = HfApi().model_info(model_id).sha
    if not isinstance(revision, str):
        raise RuntimeError("Hugging Face did not return a model commit")
    return revision


def _download_huggingface(
    model_id: str,
    *,
    revision: str,
    local_dir: str | Path,
) -> None:
    from huggingface_hub import snapshot_download

    snapshot_download(
        model_id,
        revision=revision,
        local_dir=str(local_dir),
        ignore_patterns=(
            "onnx/*",
            "imgs/*",
            "*.jpg",
            "*.webp",
        ),
    )


def _download_modelscope(
    model_id: str,
    *,
    revision: str,
    cache_dir: str | Path,
) -> str:
    from modelscope import snapshot_download

    return snapshot_download(
        model_id,
        revision=revision,
        cache_dir=str(cache_dir),
    )


def _verify_download(model_dir: Path) -> dict[str, Any]:
    status = model_status(model_dir)
    if not status.complete:
        missing = ", ".join(status.missing)
        raise RuntimeError(f"Downloaded bge-m3 model is incomplete: {missing}")
    return load_model_manifest(model_dir)


def ensure_model_downloaded(
    *,
    model_path: str | Path | None = None,
    model_home: str | Path | None = None,
    huggingface_resolver: Callable[[str], str] | None = None,
    huggingface_downloader: Callable[..., Any] | None = None,
    modelscope_downloader: Callable[..., Any] | None | object = _DEFAULT,
    modelscope_revision: str | None = None,
) -> dict[str, Any]:
    """Return verified identity, downloading only pinned snapshots if needed."""
    model_dir = Path(model_path if model_path is not None else MODEL_PATH)
    cache_root = Path(model_home if model_home is not None else MODEL_HOME)
    current = model_status(model_dir)
    if current.complete:
        return load_model_manifest(model_dir)

    model_dir.mkdir(parents=True, exist_ok=True)
    errors: list[str] = []
    resolve_huggingface = (
        huggingface_resolver
        if huggingface_resolver is not None
        else _resolve_huggingface_revision
    )
    download_huggingface = (
        huggingface_downloader
        if huggingface_downloader is not None
        else _download_huggingface
    )

    try:
        revision = resolve_huggingface(MODEL_ID)
        validate_model_revision(revision)
        download_huggingface(
            MODEL_ID,
            revision=revision,
            local_dir=model_dir,
        )
        write_model_manifest(
            model_dir,
            revision=revision,
            source="huggingface",
        )
        return _verify_download(model_dir)
    except Exception as exc:
        errors.append(f"Hugging Face: {exc}")

    if modelscope_downloader is _DEFAULT:
        download_modelscope = _download_modelscope
    else:
        download_modelscope = modelscope_downloader
    pinned_modelscope_revision = (
        modelscope_revision
        or os.environ.get("RSK_BGE_MODELSCOPE_REVISION", "").strip()
    )
    if download_modelscope is not None:
        try:
            if not pinned_modelscope_revision:
                # First install has no way to know the immutable hash in
                # advance: resolve it from the ModelScope remote automatically.
                pinned_modelscope_revision = _resolve_modelscope_revision(MODEL_ID)
            validate_model_revision(pinned_modelscope_revision)
            downloaded = Path(
                download_modelscope(
                    MODEL_ID,
                    revision=pinned_modelscope_revision,
                    cache_dir=cache_root,
                )
            )
            if downloaded.resolve() != model_dir.resolve():
                shutil.copytree(downloaded, model_dir, dirs_exist_ok=True)
            write_model_manifest(
                model_dir,
                revision=pinned_modelscope_revision,
                source="modelscope",
            )
            return _verify_download(model_dir)
        except Exception as exc:
            errors.append(f"ModelScope: {exc}")

    detail = "; ".join(errors)
    raise RuntimeError(
        "Failed to obtain a complete, immutable BAAI/bge-m3 snapshot at "
        f"{model_dir}: {detail}"
    )


def _ensure_model_downloaded() -> dict[str, Any]:
    """Compatibility wrapper for callers of the previous private helper."""
    return ensure_model_downloaded()


def load_bge_m3(device=None):
    """Load bge-m3 embedding model with CUDA fp16 optimization.

    On CUDA: loads directly in float16, saving ~1GB VRAM vs fp32.
    On CPU: standard float32 load.
    """
    ensure_model_downloaded()

    from sentence_transformers import SentenceTransformer

    if device is None:
        device = DEVICE

    if device == "cuda":
        import torch
        return SentenceTransformer(
            MODEL_PATH, device=device,
            model_kwargs={"torch_dtype": torch.float16}
        )
    return SentenceTransformer(MODEL_PATH, device=device)
