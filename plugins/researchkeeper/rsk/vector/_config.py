"""Shared constants for vector scripts."""

import hashlib
import os
import sys
from pathlib import Path
from rsk.config import get_model_cache_dir, get_runtime_paths


# bge-m3 model path
MODEL_HOME = get_model_cache_dir()
MODEL_PATH = str(Path(MODEL_HOME) / "bge-m3")

# Auto-inject SENTENCE_TRANSFORMERS_HOME
os.environ.setdefault("SENTENCE_TRANSFORMERS_HOME", MODEL_HOME)

# Default plugin-data location, mirroring bin/rsk.cmd's fallback so bare
# `python -m rsk.vector.*` processes can still discover the active install.
_PLUGIN_DATA_DEFAULT = os.path.join(
    os.path.expanduser("~"),
    ".claude",
    "plugins",
    "data",
    "researchkeeper-researchkeeper-local",
)


def _resolve_device():
    """Return the explicitly authorized device, defaulting safely to CPU.

    Priority:
    1. configs/bge_device.txt — permanent workspace config
    2. RSK_BGE_DEVICE — explicit session override
    3. ready.json — device accepted during setup
    4. cpu — hardware visibility alone never authorizes CUDA

    A silent CPU fallback misled operators into thinking GPU was broken;
    the fallback now emits a WARN and the plugin-data lookup falls back to
    the default path used by bin/rsk.cmd when the env var is absent.
    """
    runtime_paths = get_runtime_paths()
    config_path = runtime_paths.workspace / "configs" / "bge_device.txt"
    if config_path.exists():
        first_line = config_path.read_text(encoding="utf-8").split("\n")[0].strip()
        first_line = first_line.split("#")[0].strip()
        if first_line.lower() in ("cuda", "cpu"):
            return first_line.lower()

    env_val = os.environ.get("RSK_BGE_DEVICE", "").strip().lower()
    if env_val in ("cuda", "cpu"):
        return env_val

    # Tier 2.5: CLAUDE_PLUGIN_DATA/install/ready.json (plugin bootstrap)
    plugin_data = os.environ.get("CLAUDE_PLUGIN_DATA", "").strip()
    if not plugin_data and Path(_PLUGIN_DATA_DEFAULT).exists():
        plugin_data = _PLUGIN_DATA_DEFAULT
    if plugin_data:
        try:
            from rsk.install_state import InstallState, InstallStateError
            plugin_ready = InstallState(Path(plugin_data)).load_ready()
            if plugin_ready and plugin_ready.get("device_mode") in ("cuda", "cpu"):
                return str(plugin_ready["device_mode"])
        except Exception:
            pass

    # Tier 3: per-user install state (backward compat)
    try:
        from rsk.install_state import InstallState, InstallStateError

        ready = InstallState(runtime_paths.user_data).load_ready()
        if ready and ready.get("device_mode") in ("cuda", "cpu"):
            return str(ready["device_mode"])
    except (InstallStateError, OSError, ValueError):
        pass
    except Exception:
        pass

    print(
        "WARN: no explicit device source found, DEVICE=CPU "
        "(set configs/bge_device.txt or RSK_BGE_DEVICE to override)",
        file=sys.stderr,
    )
    return "cpu"


DEVICE = _resolve_device()

_VECTOR_CODE_FILES = (
    "_config.py",
    "claims.py",
    "model.py",
    "model_manifest.py",
    "query.py",
    "server.py",
    "sync.py",
)


def code_version() -> str:
    """Content hash of the vector-layer sources for stale-server detection.

    The running server and the CLI must agree on this value; when they
    differ the server is serving stale code/indexes and should be restarted
    (``rsk serve``) or bypassed (``--no-server``).
    """
    vector_dir = Path(__file__).resolve().parent
    digest = hashlib.sha256()
    for name in _VECTOR_CODE_FILES:
        digest.update(name.encode("utf-8"))
        try:
            digest.update((vector_dir / name).read_bytes())
        except OSError:
            digest.update(b"<missing>")
    return digest.hexdigest()[:16]


_RETRIEVAL_CONFIG_CACHE: dict | None = None


def _load_retrieval_config() -> dict:
    """Load workspace retrieval tuning from configs/retrieval.yaml (cached)."""
    global _RETRIEVAL_CONFIG_CACHE
    if _RETRIEVAL_CONFIG_CACHE is not None:
        return _RETRIEVAL_CONFIG_CACHE
    config: dict = {}
    candidate = os.environ.get("RSK_RETRIEVAL_CONFIG", "").strip()
    if not candidate:
        candidate = str(
            get_runtime_paths().workspace / "configs" / "retrieval.yaml"
        )
    if candidate and Path(candidate).is_file():
        try:
            import yaml

            data = yaml.safe_load(Path(candidate).read_text(encoding="utf-8"))
            if isinstance(data, dict):
                loaded = data.get("retrieval", data)
                if isinstance(loaded, dict):
                    config = loaded
        except Exception:
            config = {}
    _RETRIEVAL_CONFIG_CACHE = config
    return config


def retrieval_value(key: str, default: str) -> str:
    """Resolve one retrieval tuning value: env var > workspace config > default.

    ``key`` is the snake_case config name (e.g. ``claim_value_limit``); the
    matching environment variable is ``RSK_<UPPER>`` (e.g.
    ``RSK_CLAIM_VALUE_LIMIT``). Persist tuning decisions in the workspace at
    ``configs/retrieval.yaml`` so they survive sessions and processes:
    ``{"retrieval": {"claim_value_limit": 200}}``.
    """
    env_val = os.environ.get("RSK_" + key.upper(), "").strip()
    if env_val:
        return env_val
    config = _load_retrieval_config()
    value = config.get(key)
    if value is not None:
        return str(value)
    return default
