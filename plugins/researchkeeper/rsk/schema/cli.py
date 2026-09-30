"""CLI handlers for first-installation schema onboarding."""

from __future__ import annotations

import json
from pathlib import Path
import sys

from rsk.schema.contract import (
    SCIENTIFIC_ROLES,
    builtin_template_root,
    load_builtin_template,
    load_proposal,
    validate_proposal,
)
from rsk.schema.materialize import (
    SchemaMaterializationError,
    active_schema_fingerprint,
    materialize_schema,
    workspace_schema_status,
)


BUILTIN_TEMPLATE_IDS = ("electrocatalysis", "generic-science")


def _template_root() -> Path:
    return builtin_template_root()


def _emit(payload: dict[str, object], *, json_output: bool) -> None:
    if json_output:
        print(json.dumps(payload, ensure_ascii=False, separators=(",", ":")))
    else:
        print(json.dumps(payload, ensure_ascii=False, indent=2))


def _preview(proposal) -> dict[str, object]:
    return {
        "template_id": proposal.template_id,
        "template_version": proposal.template_version,
        "schema_version": proposal.schema_version,
        "module_count": len(proposal.modules),
        "modules": [
            {
                "name": module.name,
                "file": module.file,
                "role": module.role,
            }
            for module in proposal.modules
        ],
        "roles": sorted({module.role for module in proposal.modules}),
        "vector_gate_query_count": len(proposal.vector_gate_queries),
    }


def _proposal_error(errors) -> dict[str, object]:
    messages = [str(error) for error in errors]
    return {
        "status": "fail",
        "error": {
            "code": "invalid_schema_proposal",
            "message": "; ".join(messages),
        },
        "errors": messages,
        "preview": None,
    }


def cmd_schema_list(args) -> int:
    templates = []
    root = _template_root()
    try:
        for template_id in BUILTIN_TEMPLATE_IDS:
            proposal = load_builtin_template(
                template_id,
                template_root=root,
            )
            templates.append(
                {
                    "template_id": proposal.template_id,
                    "template_version": proposal.template_version,
                    "module_count": len(proposal.modules),
                    "roles": sorted(
                        {module.role for module in proposal.modules}
                    ),
                }
            )
    except (OSError, ValueError) as exc:
        _emit(
            {
                "status": "fail",
                "error": {
                    "code": "template_unavailable",
                    "message": str(exc),
                },
            },
            json_output=args.json_output,
        )
        return 1
    _emit(
        {
            "status": "pass",
            "scientific_roles": sorted(SCIENTIFIC_ROLES),
            "templates": templates,
        },
        json_output=args.json_output,
    )
    return 0


def cmd_schema_status(args) -> int:
    from rsk.config import get_runtime_paths

    workspace = get_runtime_paths().workspace
    status = workspace_schema_status(workspace)
    payload: dict[str, object] = {
        "status": "pass" if status != "invalid" else "fail",
        "schema_status": status,
        "workspace": str(workspace),
        "schema_fingerprint": None,
    }
    if status in {"configured_empty", "configured_nonempty"}:
        payload["schema_fingerprint"] = active_schema_fingerprint(workspace)
    _emit(payload, json_output=args.json_output)
    return 1 if status == "invalid" else 0


def _load_and_validate(path: Path):
    try:
        proposal = load_proposal(path)
    except (OSError, ValueError, TypeError, json.JSONDecodeError) as exc:
        return None, [f"cannot read proposal: {exc}"]
    return proposal, validate_proposal(proposal)


def cmd_schema_validate(args) -> int:
    proposal, errors = _load_and_validate(args.proposal)
    payload = (
        _proposal_error(errors)
        if errors
        else {
            "status": "pass",
            "errors": [],
            "preview": _preview(proposal),
        }
    )
    _emit(payload, json_output=args.json_output)
    return 2 if errors else 0


def cmd_schema_apply(args) -> int:
    from rsk.config import get_runtime_paths

    if not args.yes:
        print(
            "Explicit approval is required before schema materialization.",
            file=sys.stderr,
        )
        _emit(
            {
                "status": "fail",
                "error": {
                    "code": "confirmation_required",
                    "message": "schema apply requires --yes",
                },
            },
            json_output=args.json_output,
        )
        return 2

    proposal, errors = _load_and_validate(args.proposal)
    if errors or proposal is None:
        _emit(
            _proposal_error(errors),
            json_output=args.json_output,
        )
        return 2

    workspace = get_runtime_paths().workspace
    try:
        result = materialize_schema(
            workspace=workspace,
            template_root=_template_root(),
            proposal=proposal,
        )
    except SchemaMaterializationError as exc:
        _emit(
            {
                "status": "fail",
                "error": {
                    "code": "schema_apply_failed",
                    "message": str(exc),
                },
            },
            json_output=args.json_output,
        )
        return 2
    _emit(
        {
            "status": "pass",
            "schema_status": result.status,
            "workspace": str(workspace),
            "schema_fingerprint": result.schema_fingerprint,
            "reused": result.reused,
        },
        json_output=args.json_output,
    )
    return 0


def add_schema_parser(subparsers) -> None:
    schema = subparsers.add_parser(
        "schema",
        help="List, validate, apply, and inspect workspace schemas",
    )
    actions = schema.add_subparsers(dest="schema_command", required=True)

    list_parser = actions.add_parser("list")
    list_parser.add_argument("--json", action="store_true", dest="json_output")
    list_parser.set_defaults(func=cmd_schema_list)

    status_parser = actions.add_parser("status")
    status_parser.add_argument(
        "--workspace",
        dest="command_workspace",
        type=Path,
    )
    status_parser.add_argument(
        "--json",
        action="store_true",
        dest="json_output",
    )
    status_parser.set_defaults(func=cmd_schema_status)

    for name, handler in (
        ("validate", cmd_schema_validate),
        ("apply", cmd_schema_apply),
    ):
        parser = actions.add_parser(name)
        parser.add_argument(
            "--workspace",
            dest="command_workspace",
            type=Path,
            required=True,
        )
        parser.add_argument(
            "--proposal",
            type=Path,
            required=True,
        )
        parser.add_argument(
            "--json",
            action="store_true",
            dest="json_output",
        )
        if name == "apply":
            parser.add_argument("--yes", action="store_true")
        parser.set_defaults(func=handler)
