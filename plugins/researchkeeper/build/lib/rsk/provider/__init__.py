"""ResearchKeeper Provider Protocol v1 boundary."""

from __future__ import annotations

from importlib.metadata import PackageNotFoundError, version


PROTOCOL_VERSION = "1.0"
PROVIDER_NAME = "rsk"
PROVIDER_ACTIONS = ("query", "write-candidate")


def provider_version() -> str:
    """Return the installed distribution version with a source-tree fallback."""
    try:
        return version("rsk")
    except PackageNotFoundError:
        return "0.1.0"
