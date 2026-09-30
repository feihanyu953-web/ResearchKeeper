"""Read-only diagnostics for ResearchKeeper runtime and installation state."""

from __future__ import annotations

import argparse
import importlib
import json
from pathlib import Path
import sys
from typing import Any, Callable

from rsk.install_state import InstallState, InstallStateError
from rsk.paths import RuntimePaths
from rsk.schema.materialize import (
    active_schema_fingerprint,
    workspace_schema_status,
)


SUPPORTED_PYTHON = (3, 11)
_STATUS_RANK = {"pass": 0, "warn": 1, "fail": 2}
BOOTSTRAP_IMPORTS = (
    "fitz",
    "huggingface_hub",
    "modelscope",
    "numpy",
    "platformdirs",
    "sentence_transformers",
    "torch",
    "yaml",
)


def _version_text(version: tuple[int, ...]) -> str:
    return ".".join(str(part) for part in version[:3])


def _default_cuda_available() -> bool:
    try:
        import torch

        return bool(torch.cuda.is_available())
    except Exception:
        return False


def build_bootstrap_smoke_report(
    *,
    python_version: tuple[int, ...] | None = None,
    importer: Callable[[str], Any] = importlib.import_module,
) -> dict[str, Any]:
    """Check plugin runtime imports without reading or downloading a model."""
    version = tuple(python_version or sys.version_info[:3])
    imports: dict[str, str] = {}
    errors: dict[str, str] = {}
    for module_name in BOOTSTRAP_IMPORTS:
        try:
            importer(module_name)
        except Exception as exc:
            imports[module_name] = "fail"
            errors[module_name] = f"{type(exc).__name__}: {exc}"
        else:
            imports[module_name] = "pass"

    python_supported = version[:2] == SUPPORTED_PYTHON
    return {
        "status": (
            "pass"
            if python_supported and not errors
            else "fail"
        ),
        "python": {
            "version": _version_text(version),
            "supported": python_supported,
            "required": "3.11.x",
        },
        "imports": imports,
        "errors": errors,
    }


def build_doctor_report(
    *,
    paths: RuntimePaths,
    state: InstallState,
    python_version: tuple[int, ...] | None = None,
    cuda_available: Callable[[], bool] = _default_cuda_available,
) -> dict[str, Any]:
    """Inspect runtime state without creating or modifying any files."""
    checks: list[dict[str, str]] = []

    def add_check(name: str, status: str, message: str) -> None:
        checks.append({"name": name, "status": status, "message": message})

    version = tuple(python_version or sys.version_info[:3])
    python_supported = version[:2] == SUPPORTED_PYTHON
    add_check(
        "python",
        "pass" if python_supported else "fail",
        (
            f"Python {_version_text(version)} is supported"
            if python_supported
            else f"Python 3.11.x is required; found {_version_text(version)}"
        ),
    )

    ready: dict[str, Any] | None
    try:
        ready = state.load_ready()
    except InstallStateError as exc:
        ready = None
        add_check("installation_state", "fail", str(exc))
    else:
        if ready is None:
            add_check(
                "installation_state",
                "warn",
                "Setup has not produced ready.json",
            )
        else:
            add_check(
                "installation_state",
                "pass",
                "ready.json is valid",
            )

    workspace_exists = paths.workspace.is_dir()
    add_check(
        "workspace",
        "pass" if workspace_exists else ("fail" if ready else "warn"),
        (
            f"Workspace exists: {paths.workspace}"
            if workspace_exists
            else f"Workspace is missing: {paths.workspace}"
        ),
    )

    schema_state = workspace_schema_status(paths.workspace)
    schema_status = (
        "pass"
        if schema_state in {"configured_empty", "configured_nonempty"}
        else ("fail" if schema_state == "invalid" else "warn")
    )
    fingerprint = None
    if schema_status == "pass":
        fingerprint = active_schema_fingerprint(paths.workspace)
    add_check(
        "schema",
        schema_status,
        f"Workspace schema is {schema_state}",
    )
    knowledge_status = (
        "empty"
        if schema_state == "configured_empty"
        else (
            "nonempty"
            if schema_state == "configured_nonempty"
            else "unknown"
        )
    )

    if ready is not None:
        if (
            ready.get("workspace") != str(paths.workspace)
            or ready.get("schema_fingerprint") != fingerprint
        ):
            for check in checks:
                if check["name"] == "installation_state":
                    check["status"] = "warn"
                    check["message"] = (
                        "ready.json belongs to a different workspace or "
                        "schema fingerprint"
                    )
                    break

    model_cache = Path(
        ready.get("model_cache", paths.model_cache) if ready else paths.model_cache
    )
    model_dir = model_cache / "bge-m3"
    from rsk.vector.model_manifest import (
        load_model_manifest,
        model_status,
    )

    completeness = model_status(model_dir)
    model_complete = completeness.complete
    manifest_revision = None
    model_message = (
        f"Model snapshot is complete: {model_dir}"
        if model_complete
        else (
            "Model snapshot is incomplete: "
            + ", ".join(completeness.missing)
        )
    )
    if model_complete:
        manifest_revision = str(
            load_model_manifest(model_dir)["revision"]
        )
        ready_revision = (
            str(ready.get("model_revision"))
            if ready and ready.get("model_revision") is not None
            else None
        )
        if ready_revision is not None and ready_revision != manifest_revision:
            model_complete = False
            model_message = (
                "ready.json model revision does not match "
                "model-manifest.json"
            )
    add_check(
        "model",
        "pass" if model_complete else ("fail" if ready else "warn"),
        model_message,
    )

    has_cuda = bool(cuda_available())
    device_mode = (
        str(ready.get("device_mode", "cpu"))
        if ready
        else ("cuda" if has_cuda else "cpu")
    )
    device_ok = device_mode != "cuda" or has_cuda
    add_check(
        "device",
        "pass" if device_ok else "fail",
        (
            f"Device mode {device_mode} is available"
            if device_ok
            else "ready.json requires CUDA but CUDA is unavailable"
        ),
    )

    vector_db = Path(
        ready.get("vector_db", paths.vector_db) if ready else paths.vector_db
    )
    vector_exists = vector_db.is_dir()
    vector_status = (
        "not_initialized"
        if knowledge_status == "empty"
        else ("initialized" if vector_exists else "missing")
    )
    add_check(
        "vector_db",
        "pass" if vector_exists else ("fail" if ready else "warn"),
        (
            f"Vector database exists: {vector_db}"
            if vector_exists
            else f"Vector database is missing: {vector_db}"
        ),
    )

    overall = max(
        (check["status"] for check in checks),
        key=_STATUS_RANK.__getitem__,
    )
    return {
        "status": overall,
        "python": {
            "version": _version_text(version),
            "supported": python_supported,
            "required": "3.11.x",
        },
        "workspace": {
            "path": str(paths.workspace),
            "exists": workspace_exists,
        },
        "schema": {
            "status": schema_status,
            "state": schema_state,
            "fingerprint": fingerprint,
        },
        "knowledge_base": {
            "status": knowledge_status,
        },
        "model": {
            "path": str(model_dir),
            "exists": model_complete,
            "revision": (
                manifest_revision
                or (ready.get("model_revision") if ready else None)
            ),
            "missing": list(completeness.missing),
        },
        "device": {
            "mode": device_mode,
            "cuda_available": has_cuda,
        },
        "vector_db": {
            "path": str(vector_db),
            "exists": vector_exists,
            "status": vector_status,
        },
        "checks": checks,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="ResearchKeeper runtime diagnostics.",
    )
    parser.add_argument(
        "--bootstrap-smoke",
        action="store_true",
        help="check Python and imports without inspecting model state",
    )
    args = parser.parse_args(argv)
    if not args.bootstrap_smoke:
        parser.error("--bootstrap-smoke is required for module execution")

    report = build_bootstrap_smoke_report()
    json.dump(report, sys.stdout, ensure_ascii=False)
    sys.stdout.write("\n")
    return 0 if report["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
