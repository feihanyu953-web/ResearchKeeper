"""Resolve ResearchKeeper workspace and per-user runtime directories."""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
import os
from pathlib import Path

from platformdirs import user_cache_path, user_data_path


def _resolved(path: str | Path) -> Path:
    return Path(path).expanduser().resolve()


def _configured_workspace(cwd: Path) -> Path | None:
    for candidate in (cwd, *cwd.parents):
        if (candidate / "rsk_config.yaml").is_file():
            return candidate
    return None


@dataclass(frozen=True)
class RuntimePaths:
    """Immutable locations used by one ResearchKeeper invocation."""

    workspace: Path
    user_data: Path
    user_cache: Path
    model_cache: Path
    vector_db: Path

    @classmethod
    def resolve(
        cls,
        *,
        cli_workspace: str | Path | None = None,
        environ: Mapping[str, str] | None = None,
        cwd: str | Path | None = None,
        user_data: str | Path | None = None,
        user_cache: str | Path | None = None,
    ) -> "RuntimePaths":
        """Resolve paths with CLI, environment, config marker, then cwd priority."""
        environment = os.environ if environ is None else environ
        current_directory = _resolved(Path.cwd() if cwd is None else cwd)

        env_workspace = environment.get("RSK_ROOT", "").strip()
        if cli_workspace is not None:
            workspace = _resolved(cli_workspace)
        elif env_workspace:
            workspace = _resolved(env_workspace)
        else:
            workspace = _configured_workspace(current_directory) or current_directory

        data_root = _resolved(
            user_data
            if user_data is not None
            else user_data_path("ResearchKeeper", "RSK")
        )
        cache_root = _resolved(
            user_cache
            if user_cache is not None
            else user_cache_path("ResearchKeeper", "RSK")
        )

        return cls(
            workspace=workspace,
            user_data=data_root,
            user_cache=cache_root,
            model_cache=(cache_root / "models").resolve(),
            vector_db=(workspace / "vector_db").resolve(),
        )
