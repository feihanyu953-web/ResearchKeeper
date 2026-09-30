"""Load rsk_config.yaml, resolve environment variables, provide global settings."""

from collections.abc import Mapping
import os
from pathlib import Path
import yaml

from rsk.paths import RuntimePaths


_RUNTIME_PATHS = RuntimePaths.resolve()
PROJECT_ROOT = _RUNTIME_PATHS.workspace


def get_runtime_paths() -> RuntimePaths:
    """Return the paths configured for the current process."""
    return _RUNTIME_PATHS


def configure_runtime_paths(
    cli_workspace: str | Path | None = None,
    *,
    environ: Mapping[str, str] | None = None,
    cwd: str | Path | None = None,
    user_data: str | Path | None = None,
    user_cache: str | Path | None = None,
) -> RuntimePaths:
    """Resolve and activate paths before command handlers import other modules."""
    global _RUNTIME_PATHS, PROJECT_ROOT

    _RUNTIME_PATHS = RuntimePaths.resolve(
        cli_workspace=cli_workspace,
        environ=environ,
        cwd=cwd,
        user_data=user_data,
        user_cache=user_cache,
    )
    PROJECT_ROOT = _RUNTIME_PATHS.workspace
    return _RUNTIME_PATHS


def _load_config():
    """Load rsk_config.yaml from project root. Returns {} if not found."""
    config_path = PROJECT_ROOT / "rsk_config.yaml"
    if config_path.exists():
        with open(config_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f) or {}
    return {}


def get(key, default=None):
    """Get a config value by dotted key, e.g. 'zotero.db_path'.

    Priority: environment variable RSK_<KEY> > rsk_config.yaml > default.
    """
    env_key = f"RSK_{key.replace('.', '_').upper()}"
    env_val = os.environ.get(env_key, "").strip()
    if env_val:
        return env_val

    parts = key.split(".")
    val = _load_config()
    for p in parts:
        if isinstance(val, dict):
            val = val.get(p)
        else:
            return default
    return val if val is not None else default


def get_model_cache_dir():
    """Resolve model cache directory. Default: per-user cache/models."""
    raw = get("model_cache_dir")
    if raw is None:
        return str(_RUNTIME_PATHS.model_cache)
    path = Path(raw).expanduser()
    if not path.is_absolute():
        path = _RUNTIME_PATHS.user_cache / path
    return str(path.resolve())


def get_kb_dir():
    return PROJECT_ROOT / "kb"


def get_compute_kb_dir():
    return PROJECT_ROOT / "computer_kb"


def is_compute_kb_enabled():
    """Check if compute KB extension is enabled."""
    return str(get("compute_kb.enabled", False)).lower() in ("true", "1", "yes")


def get_vector_db_dir():
    raw = get("vector_db_dir")
    if raw is None:
        return _RUNTIME_PATHS.vector_db
    p = Path(raw)
    if not p.is_absolute():
        p = PROJECT_ROOT / p
    return p


def get_modules_config_path():
    raw = get("kb_modules", "schemas/generated/modules.yaml")
    p = Path(raw)
    if not p.is_absolute():
        p = PROJECT_ROOT / p
    return p


def load_modules():
    """Load active workspace module definitions in authoritative order."""
    path = get_modules_config_path()
    if not path.exists():
        raise FileNotFoundError(
            f"Modules config not found: {path}\n"
            "Configure the empty workspace schema first."
        )
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    if not isinstance(data, dict) or not isinstance(data.get("modules"), list):
        raise ValueError(f"Invalid active modules config: {path}")
    modules = data["modules"]
    if not all(
        isinstance(module, dict)
        and module.get("name")
        and module.get("file")
        for module in modules
    ):
        raise ValueError(f"Invalid active module entry: {path}")
    return modules


def get_module_names():
    """Return list of module names, e.g. ['synthesis', 'performance', ...]."""
    return [m["name"] for m in load_modules()]


def get_module_files():
    """Return list of module markdown filenames, e.g. ['synthesis.md', ...]."""
    return [m["file"] for m in load_modules()]
