"""Strict Provider Protocol v1 request and stdout boundary."""

from __future__ import annotations

from contextlib import redirect_stdout
from dataclasses import dataclass
import json
from pathlib import Path
import re
import sys
from typing import Callable, TypeVar

from rsk.provider import (
    PROTOCOL_VERSION,
    PROVIDER_ACTIONS,
    PROVIDER_NAME,
)


EXIT_VALIDATION = 2
EXIT_DEPENDENCY = 3
EXIT_EXECUTION = 4
EXIT_PROTOCOL = 5

_REQUEST_FIELDS = {
    "protocol_version",
    "request_id",
    "provider",
    "action",
    "inputs",
    "output_dir",
}
_REQUEST_ID = re.compile(r"^[A-Za-z0-9._-]{1,128}$")
_ACTION = re.compile(r"^[a-z][a-z0-9-]*$")
_T = TypeVar("_T")


@dataclass(frozen=True)
class ProviderFailure(Exception):
    """A failure that maps directly to a Provider Protocol error document."""

    code: str
    message: str
    exit_code: int
    request_id: str = "unknown"
    action: str = "unknown"
    details: dict | None = None

    def __str__(self) -> str:
        return self.message


def safe_request_id(value: object) -> str:
    """Return a schema-valid request id for an error response."""
    text = value if isinstance(value, str) else ""
    return text if _REQUEST_ID.fullmatch(text) else "unknown"


def safe_action(value: object) -> str:
    """Return a schema-valid action for an error response."""
    text = value if isinstance(value, str) else ""
    return text if _ACTION.fullmatch(text) else "unknown"


def failure(
    code: str,
    message: str,
    *,
    request_id: str = "unknown",
    action: str = "unknown",
    details: dict | None = None,
) -> ProviderFailure:
    """Build a failure with the exit code fixed by the protocol."""
    exit_codes = {
        "validation": EXIT_VALIDATION,
        "dependency": EXIT_DEPENDENCY,
        "execution": EXIT_EXECUTION,
        "protocol": EXIT_PROTOCOL,
    }
    return ProviderFailure(
        code=code,
        message=message,
        exit_code=exit_codes[code],
        request_id=safe_request_id(request_id),
        action=safe_action(action),
        details=details,
    )


def error_document(problem: ProviderFailure) -> dict:
    """Convert a failure to the strict Provider Protocol error shape."""
    error = {
        "code": problem.code,
        "message": problem.message,
    }
    if problem.details:
        error["details"] = problem.details
    return {
        "protocol_version": PROTOCOL_VERSION,
        "request_id": problem.request_id,
        "provider": PROVIDER_NAME,
        "action": problem.action,
        "status": "error",
        "error": error,
    }


def emit_document(document: dict) -> None:
    """Write exactly one UTF-8 JSON document to protocol stdout."""
    sys.stdout.write(
        json.dumps(
            document,
            ensure_ascii=False,
            separators=(",", ":"),
        )
        + "\n"
    )


def run_action_isolated(action: Callable[..., _T], *args, **kwargs) -> _T:
    """Redirect all action/library stdout to diagnostic stderr."""
    with redirect_stdout(sys.stderr):
        return action(*args, **kwargs)


def validate_cli_action(action: object) -> str:
    """Reject unknown actions before request loading or execution."""
    normalized = safe_action(action)
    allowed = {"describe", "doctor", *PROVIDER_ACTIONS}
    if normalized not in allowed:
        raise failure(
            "protocol",
            f"Unknown provider action: {normalized}",
            action=normalized,
        )
    return normalized


def load_request(path: Path | None, *, cli_action: str) -> dict:
    """Load and strictly validate a Provider Protocol v1 request."""
    if path is None:
        raise failure(
            "validation",
            "--request is required for provider actions",
            action=cli_action,
        )
    try:
        raw = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise failure(
            "validation",
            f"Cannot read request JSON: {exc}",
            action=cli_action,
        ) from exc
    if not isinstance(raw, dict):
        raise failure(
            "validation",
            "Provider request must be a JSON object",
            action=cli_action,
        )

    request_id = safe_request_id(raw.get("request_id"))
    request_action = safe_action(raw.get("action"))
    if raw.get("protocol_version") != PROTOCOL_VERSION:
        raise failure(
            "protocol",
            "Unsupported protocol_version",
            request_id=request_id,
            action=request_action or cli_action,
            details={"supported": PROTOCOL_VERSION},
        )
    if raw.get("provider") != PROVIDER_NAME:
        raise failure(
            "protocol",
            "Request targets a different provider",
            request_id=request_id,
            action=request_action or cli_action,
        )
    if request_action not in PROVIDER_ACTIONS:
        raise failure(
            "protocol",
            f"Unknown request action: {request_action}",
            request_id=request_id,
            action=request_action,
        )
    if request_action != cli_action:
        raise failure(
            "protocol",
            "CLI action does not match request action",
            request_id=request_id,
            action=request_action,
        )

    extra = sorted(set(raw) - _REQUEST_FIELDS)
    missing = sorted(_REQUEST_FIELDS - set(raw))
    if extra or missing:
        raise failure(
            "validation",
            "Provider request fields are invalid",
            request_id=request_id,
            action=request_action,
            details={"extra": extra, "missing": missing},
        )
    if request_id == "unknown":
        raise failure(
            "validation",
            "request_id is invalid",
            action=request_action,
        )
    if not isinstance(raw["inputs"], dict):
        raise failure(
            "validation",
            "inputs must be an object",
            request_id=request_id,
            action=request_action,
        )
    if not isinstance(raw["output_dir"], str) or not raw["output_dir"].strip():
        raise failure(
            "validation",
            "output_dir must be a non-empty native path string",
            request_id=request_id,
            action=request_action,
        )
    return raw
