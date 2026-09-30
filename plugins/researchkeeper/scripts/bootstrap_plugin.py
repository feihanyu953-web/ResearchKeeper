"""Create and atomically activate the Claude Code plugin dependency venv."""

from __future__ import annotations

import argparse
from collections.abc import Callable
from dataclasses import dataclass
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import venv
from typing import Any


SUPPORTED_PYTHON = (3, 11)
SUPPORTED_DEVICES = frozenset({"cpu", "cuda"})
MARKER_NAME = ".rsk-bootstrap.json"
CUDA_LOCK_NAME = "requirements.cuda.lock"
WINDOWS_LEGACY_MAX_PATH = 259
WINDOWS_CUDA_PATH_SUFFIX_BUDGET = 150
CUDA_SMOKE_CODE = (
    "import torch; "
    "assert torch.version.cuda is not None, 'torch has no CUDA runtime'; "
    "assert torch.cuda.is_available(), 'torch.cuda is unavailable'; "
    "tensor = torch.tensor([1.0], device='cuda'); "
    "torch.cuda.synchronize(); "
    "assert float(tensor.cpu()[0]) == 1.0"
)


class BootstrapError(RuntimeError):
    """Raised when no new plugin installation can be safely activated."""


@dataclass(frozen=True)
class BootstrapResult:
    """The active lock-hash installation selected by bootstrap."""

    lock_hash: str
    venv: Path
    python: Path
    reused: bool
    device: str


def _version_text(version: tuple[int, ...]) -> str:
    return ".".join(str(part) for part in version[:3])


def _venv_python(venv_dir: Path) -> Path:
    return (
        venv_dir / "Scripts" / "python.exe"
        if os.name == "nt"
        else venv_dir / "bin" / "python"
    )


def _create_environment(destination: Path) -> None:
    venv.EnvBuilder(
        with_pip=True,
        clear=False,
        symlinks=False,
        upgrade=False,
        upgrade_deps=False,
    ).create(destination)


def _run_command(
    command: list[str],
    *,
    cwd: Path,
    env: dict[str, str],
) -> None:
    subprocess.run(
        command,
        cwd=cwd,
        env=env,
        check=True,
    )


def _run_step(
    label: str,
    command: list[str],
    *,
    cwd: Path,
    env: dict[str, str],
    command_runner: Callable[..., None],
) -> None:
    try:
        command_runner(command, cwd=cwd, env=env)
    except (OSError, subprocess.CalledProcessError) as exc:
        raise BootstrapError(f"{label} failed") from exc


def _atomic_write_json(path: Path, payload: dict[str, Any]) -> None:
    temporary_path: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir=path.parent,
            prefix=f".{path.stem}-",
            suffix=".tmp",
            delete=False,
        ) as handle:
            json.dump(payload, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
            temporary_path = Path(handle.name)
        os.replace(temporary_path, path)
    finally:
        if temporary_path is not None and temporary_path.exists():
            temporary_path.unlink()


def _load_marker(venv_dir: Path) -> dict[str, Any] | None:
    marker_path = venv_dir / MARKER_NAME
    if not marker_path.is_file():
        return None
    try:
        payload = json.loads(marker_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError):
        return None
    return payload if isinstance(payload, dict) else None


def _is_reusable(venv_dir: Path, lock_hash: str, device: str) -> bool:
    marker = _load_marker(venv_dir)
    return bool(
        marker
        and marker.get("schema_version") == 1
        and marker.get("lock_hash") == lock_hash
        and marker.get("device", "cpu") == device
        and _venv_python(venv_dir).is_file()
    )


def _remove_temporary_venv(path: Path, venvs_root: Path) -> None:
    resolved_path = path.resolve()
    resolved_root = venvs_root.resolve()
    if (
        resolved_path.parent != resolved_root
        or not resolved_path.name.startswith(".build-")
    ):
        raise BootstrapError(
            f"Refusing to remove unexpected bootstrap path: {resolved_path}"
        )
    if resolved_path.exists():
        shutil.rmtree(resolved_path)


def _smoke_environment(plugin_root: Path) -> dict[str, str]:
    environment = os.environ.copy()
    existing = environment.get("PYTHONPATH", "")
    environment["PYTHONPATH"] = (
        str(plugin_root)
        if not existing
        else os.pathsep.join((str(plugin_root), existing))
    )
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    return environment


def _lock_hash(
    lock_path: Path,
    *,
    device: str,
    cuda_lock_path: Path | None,
) -> str:
    base = lock_path.read_bytes()
    if device == "cpu":
        return hashlib.sha256(base).hexdigest()
    assert cuda_lock_path is not None
    digest = hashlib.sha256()
    digest.update(base)
    digest.update(b"\0cuda\0")
    digest.update(cuda_lock_path.read_bytes())
    return digest.hexdigest()


def _resolve_venvs_root(
    *,
    plugin_data: Path,
    device: str,
    venv_root: str | Path | None,
    platform_name: str,
    local_app_data: str | Path | None,
) -> Path:
    if venv_root is not None:
        return Path(venv_root).expanduser().resolve()
    if device != "cuda" or platform_name != "nt":
        return (plugin_data / "venvs").resolve()
    local_root = local_app_data or os.environ.get("LOCALAPPDATA")
    if not local_root:
        raise BootstrapError(
            "LOCALAPPDATA is unavailable for the managed Windows CUDA "
            "environment; pass --venv-root with a short user-writable path"
        )
    return (
        Path(local_root).expanduser()
        / "ResearchKeeper"
        / "cuda-venvs"
    ).resolve()


def _validate_windows_cuda_path(target: Path) -> None:
    projected = (
        len(str(target))
        + 1
        + WINDOWS_CUDA_PATH_SUFFIX_BUDGET
    )
    if projected > WINDOWS_LEGACY_MAX_PATH:
        raise BootstrapError(
            "Windows CUDA environment path is too long for a conservative "
            f"torch wheel install (target={len(str(target))}, "
            f"reserved_suffix={WINDOWS_CUDA_PATH_SUFFIX_BUDGET}, "
            f"projected={projected}, max={WINDOWS_LEGACY_MAX_PATH}); "
            "rerun with --venv-root set to a shorter user-writable path"
        )


def _run_cuda_smoke(
    python: Path,
    *,
    plugin_root: Path,
    environment: dict[str, str],
    command_runner: Callable[..., None],
) -> None:
    _run_step(
        "CUDA smoke",
        [str(python), "-c", CUDA_SMOKE_CODE],
        cwd=plugin_root,
        env=environment,
        command_runner=command_runner,
    )


def _activate(
    *,
    active_path: Path,
    lock_hash: str,
    venv_dir: Path,
    plugin_root: Path,
    device: str,
    now: Callable[[], datetime],
) -> None:
    payload = {
        "schema_version": 1,
        "lock_hash": lock_hash,
        "venv": str(venv_dir.resolve()),
        "python": str(_venv_python(venv_dir).resolve()),
        "plugin_root": str(plugin_root.resolve()),
        "activated_at": now().isoformat(),
    }
    if device != "cpu":
        payload["device"] = device
    active_path.parent.mkdir(parents=True, exist_ok=True)
    _atomic_write_json(
        active_path,
        payload,
    )


def bootstrap_plugin(
    *,
    plugin_root: str | Path,
    plugin_data: str | Path,
    device: str = "cpu",
    venv_root: str | Path | None = None,
    python_version: tuple[int, ...] | None = None,
    environment_creator: Callable[[Path], None] = _create_environment,
    command_runner: Callable[..., None] = _run_command,
    now: Callable[[], datetime] = lambda: datetime.now(timezone.utc),
    platform_name: str = os.name,
    local_app_data: str | Path | None = None,
) -> BootstrapResult:
    """Create, smoke, and select the venv for the current dependency lock."""
    version = tuple(python_version or sys.version_info[:3])
    if version[:2] != SUPPORTED_PYTHON:
        raise BootstrapError(
            "Python 3.11.x is required; found "
            + _version_text(version)
        )
    device = str(device).strip().lower()
    if device not in SUPPORTED_DEVICES:
        raise BootstrapError(
            f"Unsupported device profile {device!r}; choose cpu or cuda"
        )

    root = Path(plugin_root).expanduser().resolve()
    data = Path(plugin_data).expanduser().resolve()
    lock_path = root / "requirements.lock"
    if not lock_path.is_file():
        raise BootstrapError(f"Dependency lock is missing: {lock_path}")
    if not (root / "pyproject.toml").is_file() or not (root / "rsk").is_dir():
        raise BootstrapError(f"Invalid ResearchKeeper plugin root: {root}")

    cuda_lock_path = root / CUDA_LOCK_NAME if device == "cuda" else None
    if cuda_lock_path is not None and not cuda_lock_path.is_file():
        raise BootstrapError(
            f"CUDA dependency overlay is missing: {cuda_lock_path}"
        )
    lock_hash = _lock_hash(
        lock_path,
        device=device,
        cuda_lock_path=cuda_lock_path,
    )
    venvs_root = _resolve_venvs_root(
        plugin_data=data,
        device=device,
        venv_root=venv_root,
        platform_name=platform_name,
        local_app_data=local_app_data,
    )
    target_name = (
        lock_hash if device == "cpu" else f"cuda-{lock_hash[:16]}"
    )
    target = venvs_root / target_name
    if device == "cuda" and platform_name == "nt":
        _validate_windows_cuda_path(target)
    active_path = data / "venvs" / "active.json"
    target_python = _venv_python(target)
    base_environment = os.environ.copy()
    smoke_environment = _smoke_environment(root)

    if target.exists():
        if not _is_reusable(target, lock_hash, device):
            raise BootstrapError(
                f"Existing lock-hash venv is incomplete: {target}"
            )
        if device == "cuda":
            _run_cuda_smoke(
                target_python,
                plugin_root=root,
                environment=smoke_environment,
                command_runner=command_runner,
            )
        _run_step(
            "bootstrap smoke",
            [
                str(target_python),
                "-m",
                "rsk.doctor",
                "--bootstrap-smoke",
            ],
            cwd=root,
            env=smoke_environment,
            command_runner=command_runner,
        )
        _activate(
            active_path=active_path,
            lock_hash=lock_hash,
            venv_dir=target,
            plugin_root=root,
            device=device,
            now=now,
        )
        return BootstrapResult(
            lock_hash=lock_hash,
            venv=target.resolve(),
            python=target_python.resolve(),
            reused=True,
            device=device,
        )

    venvs_root.mkdir(parents=True, exist_ok=True)
    temporary: Path | None = Path(
        tempfile.mkdtemp(
            prefix=".build-",
            dir=venvs_root,
        )
    )
    try:
        try:
            environment_creator(temporary)
        except Exception as exc:
            raise BootstrapError("venv creation failed") from exc

        temporary_python = _venv_python(temporary)
        if not temporary_python.is_file():
            raise BootstrapError("venv creation did not produce Python")

        _run_step(
            "dependency installation",
            [
                str(temporary_python),
                "-m",
                "pip",
                "install",
                "--disable-pip-version-check",
                "--requirement",
                str(lock_path),
            ],
            cwd=root,
            env=base_environment,
            command_runner=command_runner,
        )
        if cuda_lock_path is not None:
            _run_step(
                "CUDA dependency overlay",
                [
                    str(temporary_python),
                    "-m",
                    "pip",
                    "install",
                    "--disable-pip-version-check",
                    "--force-reinstall",
                    "--no-deps",
                    "--requirement",
                    str(cuda_lock_path),
                ],
                cwd=root,
                env=base_environment,
                command_runner=command_runner,
            )
        _run_step(
            "plugin installation",
            [
                str(temporary_python),
                "-m",
                "pip",
                "install",
                "--disable-pip-version-check",
                "--no-deps",
                str(root),
            ],
            cwd=root,
            env=base_environment,
            command_runner=command_runner,
        )
        if device == "cuda":
            _run_cuda_smoke(
                temporary_python,
                plugin_root=root,
                environment=smoke_environment,
                command_runner=command_runner,
            )
        _run_step(
            "bootstrap smoke",
            [
                str(temporary_python),
                "-m",
                "rsk.doctor",
                "--bootstrap-smoke",
            ],
            cwd=root,
            env=smoke_environment,
            command_runner=command_runner,
        )
        marker = {
            "schema_version": 1,
            "lock_hash": lock_hash,
            "python": _version_text(version),
            "plugin_root": str(root),
            "completed_at": now().isoformat(),
        }
        if device != "cpu":
            marker["device"] = device
        _atomic_write_json(temporary / MARKER_NAME, marker)
        os.replace(temporary, target)
        temporary = None
        _activate(
            active_path=active_path,
            lock_hash=lock_hash,
            venv_dir=target,
            plugin_root=root,
            device=device,
            now=now,
        )
    finally:
        if temporary is not None and temporary.exists():
            _remove_temporary_venv(temporary, venvs_root)

    return BootstrapResult(
        lock_hash=lock_hash,
        venv=target.resolve(),
        python=target_python.resolve(),
        reused=False,
        device=device,
    )


def _parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Bootstrap the ResearchKeeper Claude Code plugin venv.",
    )
    parser.add_argument("--plugin-root", required=True, type=Path)
    parser.add_argument("--plugin-data", required=True, type=Path)
    parser.add_argument(
        "--device",
        choices=sorted(SUPPORTED_DEVICES),
        default="cpu",
        help="Dependency profile to install (default: cpu).",
    )
    parser.add_argument(
        "--venv-root",
        type=Path,
        help=(
            "Optional venv storage root. CUDA on Windows otherwise uses a "
            "managed short root under LOCALAPPDATA."
        ),
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = _parse_args(argv)
    try:
        result = bootstrap_plugin(
            plugin_root=args.plugin_root,
            plugin_data=args.plugin_data,
            device=args.device,
            venv_root=args.venv_root,
        )
    except BootstrapError as exc:
        print(f"ResearchKeeper bootstrap failed: {exc}", file=sys.stderr)
        return 1

    json.dump(
        {
            "status": "pass",
            "lock_hash": result.lock_hash,
            "venv": str(result.venv),
            "python": str(result.python),
            "reused": result.reused,
            "device": result.device,
        },
        sys.stdout,
        ensure_ascii=False,
    )
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
