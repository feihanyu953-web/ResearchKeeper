"""bge-m3 model completeness and immutable identity records."""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
import os
from pathlib import Path
import re
from typing import Any


MODEL_ID = "BAAI/bge-m3"
MODEL_MANIFEST_NAME = "model-manifest.json"
REQUIRED_MODEL_FILES = (
    "config.json",
    "modules.json",
    "sentence_bert_config.json",
    "tokenizer_config.json",
)
WEIGHT_PATTERNS = (
    "model.safetensors",
    "model-*.safetensors",
    "pytorch_model.bin",
    "pytorch_model-*.bin",
)
WEIGHT_REQUIREMENT = "model.safetensors"
ALLOWED_SOURCES = {"huggingface", "modelscope", "existing-cache"}
IMMUTABLE_REVISION = re.compile(r"^[0-9a-fA-F]{40,64}$")


class ModelManifestError(RuntimeError):
    """Raised when model identity evidence is invalid or cannot be verified."""


@dataclass(frozen=True)
class ModelStatus:
    """Completeness result for a local bge-m3 model directory."""

    state: str
    missing: tuple[str, ...]

    @property
    def complete(self) -> bool:
        return self.state == "complete"


def _has_nonempty_file(path: Path) -> bool:
    return path.is_file() and path.stat().st_size > 0


def _has_model_weights(model_dir: Path) -> bool:
    return any(
        _has_nonempty_file(candidate)
        for pattern in WEIGHT_PATTERNS
        for candidate in model_dir.glob(pattern)
    )


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _model_files(model_dir: Path) -> list[Path]:
    return sorted(
        (
            path
            for path in model_dir.rglob("*")
            if path.is_file()
            and path.name != MODEL_MANIFEST_NAME
            and ".cache" not in path.relative_to(model_dir).parts
        ),
        key=lambda path: path.relative_to(model_dir).as_posix(),
    )


def validate_model_revision(revision: str) -> None:
    if not IMMUTABLE_REVISION.fullmatch(revision):
        raise ModelManifestError(
            "Model revision must be an immutable commit hash, not a moving ref"
            f" (resolve one with `git ls-remote https://www.modelscope.cn/{MODEL_ID}.git "
            "HEAD` and set RSK_BGE_MODELSCOPE_REVISION=<commit-hash>)"
        )


def _validate_source(source: str) -> None:
    if source not in ALLOWED_SOURCES:
        allowed = ", ".join(sorted(ALLOWED_SOURCES))
        raise ModelManifestError(f"Model source must be one of: {allowed}")


def _manifest_payload(
    model_dir: Path,
    *,
    revision: str,
    source: str,
) -> dict[str, Any]:
    validate_model_revision(revision)
    _validate_source(source)
    files = [
        {
            "path": path.relative_to(model_dir).as_posix(),
            "size": path.stat().st_size,
            "sha256": _sha256(path),
        }
        for path in _model_files(model_dir)
    ]
    if not files:
        raise ModelManifestError("Cannot create a manifest for an empty model")
    return {
        "model_id": MODEL_ID,
        "revision": revision.lower(),
        "source": source,
        "files": files,
    }


def write_model_manifest(
    model_dir: str | Path,
    *,
    revision: str,
    source: str,
) -> Path:
    """Atomically record pinned identity and hashes for a local model."""
    resolved = Path(model_dir)
    payload = _manifest_payload(
        resolved,
        revision=revision,
        source=source,
    )
    manifest_path = resolved / MODEL_MANIFEST_NAME
    temporary_path = resolved / f".{MODEL_MANIFEST_NAME}.{os.getpid()}.tmp"
    try:
        with temporary_path.open("w", encoding="utf-8", newline="\n") as handle:
            json.dump(
                payload,
                handle,
                ensure_ascii=False,
                indent=2,
                sort_keys=True,
            )
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary_path, manifest_path)
    finally:
        if temporary_path.exists():
            temporary_path.unlink()
    return manifest_path


def load_model_manifest(model_dir: str | Path) -> dict[str, Any]:
    """Load and structurally validate immutable model identity evidence."""
    manifest_path = Path(model_dir) / MODEL_MANIFEST_NAME
    try:
        payload = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ModelManifestError(
            f"Cannot read {MODEL_MANIFEST_NAME}: {exc}"
        ) from exc
    if not isinstance(payload, dict):
        raise ModelManifestError("Model manifest must be a JSON object")
    if payload.get("model_id") != MODEL_ID:
        raise ModelManifestError(f"Model manifest must identify {MODEL_ID}")
    revision = payload.get("revision")
    source = payload.get("source")
    files = payload.get("files")
    if not isinstance(revision, str):
        raise ModelManifestError("Model manifest revision must be a string")
    if not isinstance(source, str):
        raise ModelManifestError("Model manifest source must be a string")
    validate_model_revision(revision)
    _validate_source(source)
    if not isinstance(files, list) or not files:
        raise ModelManifestError("Model manifest files must be a non-empty list")
    for entry in files:
        if (
            not isinstance(entry, dict)
            or not isinstance(entry.get("path"), str)
            or not isinstance(entry.get("size"), int)
            or entry["size"] < 1
            or not isinstance(entry.get("sha256"), str)
            or not re.fullmatch(r"[0-9a-f]{64}", entry["sha256"])
        ):
            raise ModelManifestError("Model manifest contains an invalid file entry")
        relative = Path(entry["path"])
        if relative.is_absolute() or ".." in relative.parts:
            raise ModelManifestError("Model manifest contains an unsafe file path")
    return payload


def model_status(model_dir: str | Path) -> ModelStatus:
    """Return complete only when every critical model artifact is present."""
    resolved = Path(model_dir)
    missing = [
        relative_path
        for relative_path in REQUIRED_MODEL_FILES
        if not _has_nonempty_file(resolved / relative_path)
    ]
    if not _has_model_weights(resolved):
        missing.append(WEIGHT_REQUIREMENT)
    manifest_path = resolved / MODEL_MANIFEST_NAME
    if not manifest_path.is_file():
        missing.append(MODEL_MANIFEST_NAME)
    else:
        try:
            manifest = load_model_manifest(resolved)
        except ModelManifestError:
            missing.append(f"invalid:{MODEL_MANIFEST_NAME}")
        else:
            declared = {
                entry["path"]: entry
                for entry in manifest["files"]
            }
            actual = {
                path.relative_to(resolved).as_posix(): path
                for path in _model_files(resolved)
            }
            for relative_path, entry in declared.items():
                path = actual.get(relative_path)
                if path is None:
                    missing.append(f"manifest-missing:{relative_path}")
                    continue
                if path.stat().st_size != entry["size"]:
                    missing.append(f"size-mismatch:{relative_path}")
                    continue
                if _sha256(path) != entry["sha256"]:
                    missing.append(f"hash-mismatch:{relative_path}")
            for relative_path in sorted(set(actual) - set(declared)):
                missing.append(f"untracked-file:{relative_path}")
    return ModelStatus(
        state="incomplete" if missing else "complete",
        missing=tuple(dict.fromkeys(missing)),
    )
