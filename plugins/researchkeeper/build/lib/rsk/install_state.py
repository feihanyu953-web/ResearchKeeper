"""Atomic, recoverable installation state for ResearchKeeper setup."""

from __future__ import annotations

from datetime import datetime, timezone
import json
import os
from pathlib import Path
import tempfile
from typing import Any


READY_FIELDS = {
    "status",
    "python",
    "lock_hash",
    "model_revision",
    "device_mode",
    "completed_at",
    "schema_fingerprint",
    "workspace",
}


class InstallStateError(RuntimeError):
    """Raised when installation state is missing required structure."""


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


class InstallState:
    """Manage installing, ready, and last-failure markers under user data."""

    def __init__(self, data_dir: str | Path):
        self.data_dir = Path(data_dir).expanduser().resolve()
        self.install_dir = self.data_dir / "install"
        self.installing_path = self.install_dir / "installing.json"
        self.ready_path = self.install_dir / "ready.json"
        self.failure_path = self.install_dir / "last-failure.json"

    def _atomic_write(self, path: Path, payload: dict[str, Any]) -> None:
        self.install_dir.mkdir(parents=True, exist_ok=True)
        temporary_path: Path | None = None
        try:
            with tempfile.NamedTemporaryFile(
                mode="w",
                encoding="utf-8",
                dir=self.install_dir,
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

    def _read_json(self, path: Path) -> dict[str, Any] | None:
        if not path.exists():
            return None
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeError, json.JSONDecodeError) as exc:
            raise InstallStateError(f"Invalid installation state: {path.name}") from exc
        if not isinstance(payload, dict):
            raise InstallStateError(
                f"Invalid installation state object: {path.name}"
            )
        return payload

    def load_ready(self) -> dict[str, Any] | None:
        """Return validated ready state, or None when setup has not completed."""
        payload = self._read_json(self.ready_path)
        if payload is None:
            return None
        missing = sorted(READY_FIELDS.difference(payload))
        if missing or payload.get("status") != "ready":
            details = ", ".join(missing) if missing else "status"
            raise InstallStateError(
                f"Invalid installation state: ready.json missing {details}"
            )
        return payload

    def begin(self, payload: dict[str, Any]) -> None:
        """Start a new attempt after validating any interrupted marker."""
        interrupted = self._read_json(self.installing_path)
        if interrupted is not None:
            if interrupted.get("status") != "installing":
                raise InstallStateError(
                    "Invalid installation state: installing.json status"
                )
            self.mark_failure(
                RuntimeError("Previous setup attempt was interrupted")
            )

        marker = {
            "status": "installing",
            "started_at": _utc_now(),
            **payload,
        }
        self._atomic_write(self.installing_path, marker)

    def mark_ready(self, payload: dict[str, Any]) -> dict[str, Any]:
        """Atomically publish ready state from an active installing marker."""
        installing = self._read_json(self.installing_path)
        if installing is None or installing.get("status") != "installing":
            raise InstallStateError(
                "Cannot write ready.json without a valid installing.json"
            )

        ready = {
            "status": "ready",
            **payload,
            "completed_at": _utc_now(),
        }
        missing = sorted(READY_FIELDS.difference(ready))
        if missing:
            raise InstallStateError(
                "Cannot write ready.json; missing " + ", ".join(missing)
            )
        self._atomic_write(self.ready_path, ready)
        self.installing_path.unlink(missing_ok=True)
        return ready

    def mark_failure(self, error: BaseException) -> dict[str, Any]:
        """Record a failed attempt and ensure no ready marker survives."""
        failure = {
            "status": "failed",
            "failed_at": _utc_now(),
            "error_type": type(error).__name__,
            "error": str(error),
        }
        self.ready_path.unlink(missing_ok=True)
        self._atomic_write(self.failure_path, failure)
        self.installing_path.unlink(missing_ok=True)
        return failure
