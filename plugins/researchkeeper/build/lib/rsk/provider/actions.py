"""Provider Protocol v1 action implementations."""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import shutil
import tempfile
from typing import Callable

from rsk.provider import PROVIDER_NAME, PROTOCOL_VERSION, provider_version
from rsk.provider.protocol import failure


def _validate_query_inputs(request: dict) -> tuple[str, int, bool]:
    inputs = request["inputs"]
    required = {"query", "top_k", "claims"}
    extra = sorted(set(inputs) - required)
    missing = sorted(required - set(inputs))
    if extra or missing:
        raise failure(
            "validation",
            "query inputs are invalid",
            request_id=request["request_id"],
            action="query",
            details={"extra": extra, "missing": missing},
        )
    query = inputs["query"]
    top_k = inputs["top_k"]
    claims = inputs["claims"]
    if not isinstance(query, str) or not query.strip():
        raise failure(
            "validation",
            "inputs.query must be a non-empty string",
            request_id=request["request_id"],
            action="query",
        )
    if (
        not isinstance(top_k, int)
        or isinstance(top_k, bool)
        or not 1 <= top_k <= 100
    ):
        raise failure(
            "validation",
            "inputs.top_k must be an integer from 1 through 100",
            request_id=request["request_id"],
            action="query",
        )
    if not isinstance(claims, bool):
        raise failure(
            "validation",
            "inputs.claims must be a boolean",
            request_id=request["request_id"],
            action="query",
        )
    return query.strip(), top_k, claims


def _write_bytes_atomic(path: Path, content: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        dir=path.parent,
        prefix=f".{path.name}.",
        suffix=".tmp",
        delete=False,
    ) as handle:
        temporary = Path(handle.name)
        handle.write(content)
        handle.flush()
        os.fsync(handle.fileno())
    try:
        os.replace(temporary, path)
    finally:
        if temporary.exists():
            temporary.unlink()


def _artifact(
    path: Path,
    *,
    output_dir: Path,
    artifact_type: str,
    produced_by: str,
) -> dict:
    content = path.read_bytes()
    return {
        "path": str(path.relative_to(output_dir)),
        "type": artifact_type,
        "size": len(content),
        "sha256": hashlib.sha256(content).hexdigest(),
        "produced_by": produced_by,
    }


def _success_document(
    request: dict,
    *,
    artifacts: list[dict],
    warnings: list[str],
    provenance: dict,
) -> dict:
    return {
        "protocol_version": PROTOCOL_VERSION,
        "request_id": request["request_id"],
        "provider": PROVIDER_NAME,
        "action": request["action"],
        "status": "success",
        "artifacts": artifacts,
        "warnings": warnings,
        "provenance": {
            "provider_version": provider_version(),
            **provenance,
        },
    }


def execute_doctor() -> dict:
    """Return read-only runtime health inside a protocol success envelope."""
    from rsk.config import get_runtime_paths
    from rsk.doctor import build_doctor_report
    from rsk.install_state import InstallState

    paths = get_runtime_paths()
    plugin_data = os.environ.get("CLAUDE_PLUGIN_DATA", "").strip()
    data_dir = (
        Path(plugin_data).expanduser().resolve()
        if plugin_data
        else paths.user_data
    )
    report = build_doctor_report(
        paths=paths,
        state=InstallState(data_dir),
    )
    request = {
        "request_id": "doctor",
        "action": "doctor",
    }
    warnings = (
        []
        if report["status"] == "pass"
        else [f"health_{report['status']}"]
    )
    return _success_document(
        request,
        artifacts=[],
        warnings=warnings,
        provenance={"doctor": report},
    )


def _tree_sha256(root: Path) -> str:
    digest = hashlib.sha256()
    for path in sorted(
        (item for item in root.rglob("*") if item.is_file()),
        key=lambda item: item.relative_to(root).as_posix(),
    ):
        digest.update(path.relative_to(root).as_posix().encode("utf-8"))
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def execute_query(request: dict) -> dict:
    """Run the existing query boundary and write one verified JSON artifact."""
    question, top_k, claims = _validate_query_inputs(request)
    try:
        from rsk.vector.query import query

        output = query(
            question,
            top_k=top_k,
            json_out=False,
            use_claims=claims,
            no_server=False,
            expand=False,
        )
    except (ImportError, FileNotFoundError, SystemExit) as exc:
        raise failure(
            "dependency",
            "Query model or vector data is unavailable",
            request_id=request["request_id"],
            action="query",
            details={"exception": type(exc).__name__},
        ) from exc
    except Exception as exc:
        raise failure(
            "execution",
            "Query execution failed",
            request_id=request["request_id"],
            action="query",
            details={"exception": type(exc).__name__},
        ) from exc
    if not isinstance(output, dict) or not isinstance(
        output.get("results"),
        list,
    ):
        raise failure(
            "execution",
            "Query returned an invalid result",
            request_id=request["request_id"],
            action="query",
        )

    output_dir = Path(request["output_dir"]).expanduser().resolve()
    artifact_path = output_dir / "query-result.json"
    content = (
        json.dumps(
            output,
            ensure_ascii=False,
            indent=2,
            sort_keys=True,
        )
        + "\n"
    ).encode("utf-8")
    try:
        _write_bytes_atomic(artifact_path, content)
        artifact = _artifact(
            artifact_path,
            output_dir=output_dir,
            artifact_type="researchkeeper-query-result",
            produced_by="rsk:query",
        )
    except OSError as exc:
        raise failure(
            "execution",
            "Cannot write query artifact",
            request_id=request["request_id"],
            action="query",
            details={"exception": type(exc).__name__},
        ) from exc

    warnings = [] if output["results"] else ["no_matches"]
    return _success_document(
        request,
        artifacts=[artifact],
        warnings=warnings,
        provenance={
            "top_k": top_k,
            "claims": claims,
        },
    )


def _validate_candidate_inputs(request: dict) -> dict:
    inputs = request["inputs"]
    if set(inputs) != {"candidate"}:
        raise failure(
            "validation",
            "write-candidate inputs must contain only candidate",
            request_id=request["request_id"],
            action="write-candidate",
            details={
                "extra": sorted(set(inputs) - {"candidate"}),
                "missing": sorted({"candidate"} - set(inputs)),
            },
        )
    candidate = inputs["candidate"]
    if not isinstance(candidate, dict):
        raise failure(
            "validation",
            "inputs.candidate must be a JSON object",
            request_id=request["request_id"],
            action="write-candidate",
        )
    return candidate


def execute_write_candidate(
    request: dict,
    *,
    workspace: Path | None = None,
    writer: Callable[..., object] | None = None,
) -> dict:
    """Validate a candidate with the writer dry-run without changing formal kb."""
    candidate = _validate_candidate_inputs(request)
    if workspace is None:
        from rsk.config import get_runtime_paths

        workspace = get_runtime_paths().workspace
    workspace = Path(workspace).expanduser().resolve()
    kb_dir = workspace / "kb"
    modules_path = workspace / "schemas" / "generated" / "modules.yaml"
    if not kb_dir.is_dir() or not modules_path.is_file():
        raise failure(
            "dependency",
            "Workspace knowledge base or active schema is not initialized",
            request_id=request["request_id"],
            action="write-candidate",
        )

    output_dir = Path(request["output_dir"]).expanduser().resolve()
    if output_dir == kb_dir or kb_dir in output_dir.parents:
        raise failure(
            "validation",
            "output_dir must be outside the formal knowledge base",
            request_id=request["request_id"],
            action="write-candidate",
        )
    before = _tree_sha256(kb_dir)
    try:
        from rsk.schema.materialize import active_schema_fingerprint

        if writer is None:
            from rsk.kb.writer import write_ingest_envelope

            writer = write_ingest_envelope
        output_dir.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(
            dir=output_dir,
            prefix=".rsk-candidate-validation-",
        ) as temporary:
            shadow = Path(temporary) / "workspace"
            shutil.copytree(kb_dir, shadow / "kb")
            shutil.copytree(
                workspace / "schemas" / "generated",
                shadow / "schemas" / "generated",
            )
            result = writer(
                candidate,
                workspace=shadow,
                dry_run=True,
            )
        fingerprint = active_schema_fingerprint(workspace)
    except (OSError, ValueError) as exc:
        raise failure(
            "validation",
            "Candidate failed writer dry-run validation",
            request_id=request["request_id"],
            action="write-candidate",
            details={
                "exception": type(exc).__name__,
                "message": str(exc),
            },
        ) from exc
    after = _tree_sha256(kb_dir)
    if before != after:
        raise failure(
            "execution",
            "Writer dry-run modified the formal knowledge base",
            request_id=request["request_id"],
            action="write-candidate",
            details={"before": before, "after": after},
        )

    candidate_path = output_dir / "candidate.json"
    preview_path = output_dir / "candidate-preview.md"
    provenance_path = output_dir / "candidate-provenance.json"
    candidate_content = (
        json.dumps(
            candidate,
            ensure_ascii=False,
            indent=2,
            sort_keys=True,
        )
        + "\n"
    ).encode("utf-8")
    record_lines = "\n".join(
        f"- `{record_id}`" for record_id in result.record_ids
    )
    preview_content = (
        "# ResearchKeeper candidate preview\n\n"
        f"- Request: `{request['request_id']}`\n"
        f"- Paper: `{candidate.get('paper_id', '')}`\n"
        "- Mode: writer validation dry-run\n"
        f"- Candidate records: {len(result.record_ids)}\n\n"
        "## Proposed record IDs\n\n"
        f"{record_lines or '- None'}\n"
    ).encode("utf-8")
    provenance = {
        "protocol_version": PROTOCOL_VERSION,
        "request_id": request["request_id"],
        "provider": PROVIDER_NAME,
        "action": "write-candidate",
        "dry_run": True,
        "schema_fingerprint": fingerprint,
        "kb_sha256_before": before,
        "kb_sha256_after": after,
        "record_ids": list(result.record_ids),
    }
    provenance_content = (
        json.dumps(
            provenance,
            ensure_ascii=False,
            indent=2,
            sort_keys=True,
        )
        + "\n"
    ).encode("utf-8")
    try:
        _write_bytes_atomic(candidate_path, candidate_content)
        _write_bytes_atomic(preview_path, preview_content)
        _write_bytes_atomic(provenance_path, provenance_content)
        artifacts = [
            _artifact(
                candidate_path,
                output_dir=output_dir,
                artifact_type="researchkeeper-candidate-json",
                produced_by="rsk:write-candidate",
            ),
            _artifact(
                preview_path,
                output_dir=output_dir,
                artifact_type="researchkeeper-candidate-preview",
                produced_by="rsk:write-candidate",
            ),
            _artifact(
                provenance_path,
                output_dir=output_dir,
                artifact_type="researchkeeper-candidate-provenance",
                produced_by="rsk:write-candidate",
            ),
        ]
    except OSError as exc:
        raise failure(
            "execution",
            "Cannot write candidate artifacts",
            request_id=request["request_id"],
            action="write-candidate",
            details={"exception": type(exc).__name__},
        ) from exc
    return _success_document(
        request,
        artifacts=artifacts,
        warnings=[],
        provenance=provenance,
    )


def dispatch_action(request: dict) -> dict:
    """Dispatch only actions registered for the ResearchKeeper provider."""
    if request["action"] == "query":
        return execute_query(request)
    if request["action"] == "write-candidate":
        return execute_write_candidate(request)
    raise failure(
        "protocol",
        "Unknown ResearchKeeper provider action",
        request_id=request["request_id"],
        action=request["action"],
    )
