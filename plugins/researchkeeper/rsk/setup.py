"""Recoverable ResearchKeeper setup workflow."""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
from pathlib import Path
import sys
from typing import Any, Callable

import numpy as np

from rsk.install_state import InstallState, InstallStateError
from rsk.schema.materialize import (
    active_schema_fingerprint,
    workspace_schema_status,
)


SUPPORTED_PYTHON = (3, 11)
SMOKE_DOCUMENTS = (
    "VASP SCF convergence setup smoke document",
    "LAMMPS molecular dynamics setup smoke document",
)


class SetupError(RuntimeError):
    """Raised when setup cannot safely reach ready state."""


class ConfirmationRequired(SetupError):
    """Raised when a non-interactive setup lacks explicit consent."""


@dataclass(frozen=True)
class DownloadedModel:
    model: Any
    revision: str


@dataclass(frozen=True)
class SetupResult:
    ready: dict[str, Any]
    reused: bool


def _version_text(version: tuple[int, ...]) -> str:
    return ".".join(str(part) for part in version[:3])


def _default_gpu_available() -> bool:
    try:
        import torch

        return bool(torch.cuda.is_available())
    except Exception:
        return False


def _encode(model: Any, texts: list[str]) -> np.ndarray:
    embeddings = np.asarray(
        model.encode(
            texts,
            show_progress_bar=False,
            normalize_embeddings=True,
        ),
        dtype=np.float32,
    )
    if embeddings.ndim != 2 or embeddings.shape[0] != len(texts):
        raise SetupError("Embedding smoke returned an invalid shape")
    if embeddings.shape[1] == 0 or not np.isfinite(embeddings).all():
        raise SetupError("Embedding smoke returned invalid values")
    return embeddings


def _embedding_smoke(model: Any) -> None:
    _encode(model, ["ResearchKeeper embedding smoke"])


def _build_minimal_index(model: Any, vector_db: Path) -> Path:
    smoke_dir = vector_db / "setup-smoke"
    smoke_dir.mkdir(parents=True, exist_ok=True)
    embeddings = _encode(model, list(SMOKE_DOCUMENTS))
    np.save(smoke_dir / "embeddings.npy", embeddings)
    (smoke_dir / "metadata.json").write_text(
        json.dumps(
            [{"text": text, "position": index} for index, text in enumerate(
                SMOKE_DOCUMENTS
            )],
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    return smoke_dir


def _query_smoke(model: Any, smoke_dir: Path) -> None:
    embeddings = np.load(smoke_dir / "embeddings.npy")
    query = _encode(model, ["VASP SCF convergence"])[0]
    if embeddings.ndim != 2 or embeddings.shape[1] != query.shape[0]:
        raise SetupError("Query smoke index has an invalid shape")
    scores = embeddings @ query
    if scores.size == 0 or not np.isfinite(scores).all():
        raise SetupError("Query smoke returned invalid scores")
    if int(np.argmax(scores)) != 0:
        raise SetupError("Query smoke did not retrieve the VASP fixture")


def _model_revision(model_cache: Path) -> str:
    from rsk.vector.model_manifest import (
        load_model_manifest,
        model_status,
    )

    model_dir = model_cache / "bge-m3"
    completeness = model_status(model_dir)
    if not completeness.complete:
        missing = ", ".join(completeness.missing)
        raise SetupError(f"Downloaded bge-m3 model is incomplete: {missing}")
    return str(load_model_manifest(model_dir)["revision"])


class BgeM3Downloader:
    """Adapter around the current bge-m3 loader for production setup."""

    def download(self, *, model_cache: Path, device: str) -> DownloadedModel:
        from rsk.vector.model import load_bge_m3

        model = load_bge_m3(device=device)
        return DownloadedModel(
            model=model,
            revision=_model_revision(model_cache),
        )


def dependency_lock_hash(package_root: str | Path | None = None) -> str:
    """Return a lock hash, or an explicit provisional hash before Task 5."""
    root = (
        Path(package_root).resolve()
        if package_root is not None
        else Path(__file__).resolve().parents[1]
    )
    lock_path = root / "requirements.lock"
    if lock_path.is_file():
        return "sha256:" + hashlib.sha256(lock_path.read_bytes()).hexdigest()
    pyproject_path = root / "pyproject.toml"
    if pyproject_path.is_file():
        digest = hashlib.sha256(pyproject_path.read_bytes()).hexdigest()
        return f"unlocked-pyproject-sha256:{digest}"
    raise SetupError("No dependency lock or pyproject.toml is available")


def run_setup(
    *,
    workspace: str | Path,
    data_dir: str | Path,
    downloader: Any,
    state: InstallState,
    model_cache: str | Path | None = None,
    vector_db: str | Path | None = None,
    device: str = "auto",
    confirmed: bool = False,
    gpu_consent: bool | None = None,
    gpu_available: Callable[[], bool] = _default_gpu_available,
    lock_hash: str,
    python_version: tuple[int, ...] | None = None,
) -> SetupResult:
    """Run preflight through query smoke, publishing ready only at the end."""
    workspace_path = Path(workspace).expanduser().resolve()
    data_path = Path(data_dir).expanduser().resolve()
    model_cache_path = Path(
        model_cache if model_cache is not None else data_path / "models"
    ).expanduser().resolve()
    vector_db_path = Path(
        vector_db if vector_db is not None else workspace_path / "vector_db"
    ).expanduser().resolve()
    version = tuple(python_version or sys.version_info[:3])

    if state.data_dir != data_path:
        raise SetupError("InstallState data directory does not match data_dir")

    try:
        if version[:2] != SUPPORTED_PYTHON:
            raise SetupError(
                f"Python 3.11 is required; found {_version_text(version)}"
            )
        if not lock_hash.strip():
            raise SetupError("lock_hash is required")
        if device not in {"auto", "cpu", "cuda"}:
            raise SetupError(f"Unsupported device mode: {device}")

        schema_status = workspace_schema_status(workspace_path)
        if schema_status not in {"configured_empty", "configured_nonempty"}:
            raise SetupError(
                f"workspace schema is {schema_status}; configure schema first"
            )
        fingerprint = active_schema_fingerprint(workspace_path)

        ready = state.load_ready()
        if ready is not None:
            manifest_revision = _model_revision(model_cache_path)
            if ready.get("model_revision") != manifest_revision:
                raise SetupError(
                    "ready.json revision does not match model-manifest.json"
                )
            if (
                ready.get("workspace") == str(workspace_path)
                and ready.get("schema_fingerprint") == fingerprint
            ):
                return SetupResult(ready=ready, reused=True)

        has_cuda = bool(gpu_available())
        if device == "cuda":
            if not has_cuda:
                raise SetupError("CUDA was requested but is not available")
            device_mode = "cuda"
        elif device == "auto" and has_cuda and gpu_consent is True:
            device_mode = "cuda"
        else:
            device_mode = "cpu"

        if not confirmed:
            raise ConfirmationRequired(
                "Explicit confirmation is required before downloading the model"
            )

        state.begin(
            {
                "python": _version_text(version),
                "lock_hash": lock_hash,
                "device_mode": device_mode,
                "workspace": str(workspace_path),
                "schema_fingerprint": fingerprint,
            }
        )

        workspace_path.mkdir(parents=True, exist_ok=True)
        model_cache_path.mkdir(parents=True, exist_ok=True)
        vector_db_path.mkdir(parents=True, exist_ok=True)

        downloaded = downloader.download(
            model_cache=model_cache_path,
            device=device_mode,
        )
        if (
            not isinstance(downloaded, DownloadedModel)
            or not downloaded.revision.strip()
        ):
            raise SetupError("Downloader did not provide a model revision")

        manifest_revision = _model_revision(model_cache_path)
        if downloaded.revision != manifest_revision:
            raise SetupError(
                "Downloader revision does not match model-manifest.json"
            )

        _embedding_smoke(downloaded.model)
        smoke_dir = _build_minimal_index(downloaded.model, vector_db_path)
        _query_smoke(downloaded.model, smoke_dir)

        ready_payload = {
            "python": _version_text(version),
            "lock_hash": lock_hash,
            "model_revision": downloaded.revision,
            "device_mode": device_mode,
            "workspace": str(workspace_path),
            "schema_fingerprint": fingerprint,
            "data_dir": str(data_path),
            "model_cache": str(model_cache_path),
            "vector_db": str(vector_db_path),
        }
        return SetupResult(
            ready=state.mark_ready(ready_payload),
            reused=False,
        )
    except ConfirmationRequired:
        raise
    except Exception as exc:
        state.mark_failure(exc)
        if isinstance(exc, SetupError):
            raise
        if isinstance(exc, InstallStateError):
            raise SetupError(str(exc)) from exc
        raise SetupError(str(exc)) from exc
