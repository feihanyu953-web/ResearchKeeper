"""CLI adapter for the ResearchKeeper provider boundary."""

from __future__ import annotations

from pathlib import Path

from rsk.provider import (
    PROTOCOL_VERSION,
    PROVIDER_ACTIONS,
    PROVIDER_NAME,
    provider_version,
)
from rsk.provider.protocol import (
    ProviderFailure,
    emit_document,
    error_document,
    failure,
    load_request,
    run_action_isolated,
    validate_cli_action,
)


def cmd_provider(args) -> int:
    """Emit one protocol document for provider discovery or an action."""
    try:
        action = validate_cli_action(args.provider_action)
        if action == "describe":
            emit_document(
                {
                    "protocol_version": PROTOCOL_VERSION,
                    "provider": PROVIDER_NAME,
                    "provider_version": provider_version(),
                    "actions": list(PROVIDER_ACTIONS),
                    "capabilities": {"vector_backend": "bge-m3"},
                }
            )
            return 0
        if action == "doctor":
            from rsk.provider.actions import execute_doctor

            result = run_action_isolated(execute_doctor)
            emit_document(result)
            return 0

        request = load_request(args.request, cli_action=action)
        from rsk.provider.actions import dispatch_action

        result = run_action_isolated(dispatch_action, request)
        emit_document(result)
        return 0
    except ProviderFailure as problem:
        emit_document(error_document(problem))
        return problem.exit_code
    except Exception as exc:
        problem = failure(
            "execution",
            "Provider execution failed",
            action=getattr(args, "provider_action", "unknown"),
            details={"exception": type(exc).__name__},
        )
        emit_document(error_document(problem))
        return problem.exit_code


def add_provider_parser(subparsers) -> None:
    """Register ``rsk provider`` without importing query/model dependencies."""
    parser = subparsers.add_parser(
        "provider",
        help="Expose Provider Protocol v1 actions",
    )
    parser.add_argument("provider_action")
    parser.add_argument("--request", type=Path)
    parser.add_argument("--json", action="store_true", dest="json_output")
    parser.set_defaults(func=cmd_provider)
