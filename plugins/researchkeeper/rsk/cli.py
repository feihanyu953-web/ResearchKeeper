"""ResearchKeeper CLI entry point."""

import argparse
import os
import sys
import yaml
from pathlib import Path

# Force UTF-8 on Windows to avoid GBK encoding errors with special characters
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


def _update_config(key_path, value):
    """Update a key in rsk_config.yaml. Creates file if missing."""
    import yaml as _yaml
    from rsk.config import PROJECT_ROOT as _PROJECT_ROOT
    config_path = _PROJECT_ROOT / "rsk_config.yaml"
    config = {}
    if config_path.exists():
        with open(config_path, "r", encoding="utf-8") as f:
            config = _yaml.safe_load(f) or {}
    parts = key_path.split(".")
    c = config
    for p in parts[:-1]:
        c = c.setdefault(p, {})
    c[parts[-1]] = value
    with open(config_path, "w", encoding="utf-8") as f:
        _yaml.dump(config, f, allow_unicode=True, default_flow_style=False)


def cmd_init(args):
    """Initialize a ResearchKeeper project."""
    from rsk.config import PROJECT_ROOT
    from rsk.schema.contract import (
        builtin_template_root,
        load_builtin_template,
    )
    from rsk.schema.materialize import materialize_schema

    if args.interactive:
        print(
            "Interactive schema selection is handled by "
            "/researchkeeper:configure-schema.",
            file=sys.stderr,
        )
        return 2

    template_root = builtin_template_root()
    proposal = load_builtin_template(
        "generic-science",
        template_root=template_root,
    )
    result = materialize_schema(
        workspace=PROJECT_ROOT,
        template_root=template_root,
        proposal=proposal,
    )
    print(result.status)
    return 0


def cmd_search(args):
    """Search the knowledge base."""
    from rsk.vector.query import format_json_results
    import json as _json
    # Delegate to query module
    sys.argv = ["query.py", args.query]
    if args.claims:
        sys.argv.append("--claims")
    sys.argv.extend(["--top", str(args.top)])
    if args.json_output:
        sys.argv.append("--json")
    if getattr(args, "expand", False):
        sys.argv.append("--expand")
    from rsk.vector import query as qm
    qm.main()


def cmd_sync(args):
    """Sync kb to vector_db. Supports --input/--input-dir for JSON→kb writing first."""
    import subprocess

    # Step 1: If user provided JSON input, write to kb first
    if args.input or args.input_dir:
        from rsk.kb.writer import main as writer_main
        writer_argv = []
        if args.input:
            writer_argv.extend(["--input", args.input])
        if args.input_dir:
            writer_argv.extend(["--input-dir", args.input_dir])
        if args.dry_run:
            writer_argv.append("--dry-run")
        if getattr(args, "strict", False):
            writer_argv.append("--strict")
        import sys as _sys
        _sys.argv = ["rsk.kb.writer"] + writer_argv
        writer_main()
        print("")

    # Step 2: Vector sync
    cmd = [sys.executable, "-m", "rsk.vector.sync"]
    if args.full:
        cmd.append("--full")
    if args.dry_run:
        cmd.append("--dry-run")
    if args.skip_claims:
        cmd.append("--skip-claims")
    if args.from_claims:
        cmd.append("--from-claims")
    subprocess.run(cmd)


def cmd_serve(args):
    """Start persistent query server."""
    from rsk.vector.server import main as serve_main
    sys.argv = ["server.py", "--port", str(args.port)]
    serve_main()


def cmd_import(args):
    """Import from Zotero."""
    from rsk.zotero.reader import export_all
    import json as _json
    import os as _os
    db_path = args.db
    if not db_path:
        db_path = _os.path.join(_os.path.expanduser("~"), "Zotero", "zotero.sqlite")
    papers, stats = export_all(db_path)
    out_dir = args.output or "outputs"
    _os.makedirs(out_dir, exist_ok=True)
    out_path = _os.path.join(out_dir, "zotero_export.json")
    with open(out_path, "w", encoding="utf-8") as f:
        _json.dump({"stats": stats, "papers": papers}, f, ensure_ascii=False, indent=2)
    print(f"Exported {stats['total']} papers -> {out_path}")


def cmd_parse(args):
    """Parse PDFs to Markdown (single-file or Zotero batch)."""
    if getattr(args, "pdf", None):
        from rsk.parser.pdf import cmd_single

        cmd_single(args)
        return
    if not args.from_zotero:
        raise SystemExit("rsk parse: specify --pdf <file> or --from-zotero")
    from rsk.parser.pdf import cmd_batch
    import os as _os
    class FakeArgs:
        from_zotero = args.from_zotero
        output_dir = args.output_dir or "tmp"
    cmd_batch(FakeArgs())


def cmd_diff(args):
    """Diff Zotero vs kb."""
    import sys as _sys

    from rsk.zotero.diff import main as diff_main
    # diff_main() parses sys.argv with its own argparse; the top-level
    # rsk parser already consumed --workspace etc., so reset argv or the
    # diff subparser rejects them as unrecognized arguments.
    _sys.argv = ["rsk.zotero.diff"]
    diff_main()


def cmd_verify(args):
    """Verify ingest coverage."""
    import json as _json

    from rsk.kb.verify import verify_paper

    result = verify_paper(args.paper_id)
    payload = {
        "status": result.status,
        "paper_id": args.paper_id,
        "errors": list(result.errors),
        "reviewer_required": list(result.reviewer_required),
        "record_count": result.record_count,
    }
    if args.json_output:
        print(_json.dumps(payload, ensure_ascii=False))
    else:
        print(_json.dumps(payload, ensure_ascii=False, indent=2))
    return 0 if result.status == "pass" else 1


def cmd_fix_ids(args):
    """Normalize paper IDs."""
    from rsk.kb.fix_ids import main as fix_main
    fix_main()


def cmd_audit_sync(args):
    """Run vector sync audit."""
    from rsk.audit.sync_audit import audit_sync
    result = audit_sync()
    import json as _json
    print(_json.dumps(result, indent=2, ensure_ascii=False))


def cmd_wiki_frontmatter(args):
    """Emit a read-only frontmatter candidate or diff."""
    import json as _json

    from rsk.config import get_runtime_paths
    from rsk.wiki.frontmatter import (
        build_frontmatter_candidate,
        diff_frontmatter,
        load_existing_frontmatter,
    )

    candidate = build_frontmatter_candidate(
        get_runtime_paths().workspace,
        args.paper_id,
    )
    if args.existing:
        payload = diff_frontmatter(
            load_existing_frontmatter(args.existing),
            candidate,
        )
    else:
        payload = candidate
    if args.json_output:
        print(_json.dumps(payload, ensure_ascii=False))
    else:
        print(
            yaml.safe_dump(
                payload,
                allow_unicode=True,
                sort_keys=False,
            ).rstrip()
        )
    return 0


def cmd_experiment_plan(args):
    """Emit an evidence-bound experiment reproduction plan."""
    import json as _json

    from rsk.config import get_runtime_paths
    from rsk.experiment.plan import generate_plan

    plan = generate_plan(
        get_runtime_paths().workspace,
        args.paper_id,
    )
    if plan is None:
        payload = {
            "status": "fail",
            "paper_id": args.paper_id,
            "error": "no KB records found for paper",
        }
        if args.json_output:
            print(_json.dumps(payload, ensure_ascii=False))
        else:
            print(payload["error"], file=sys.stderr)
        return 1
    if args.json_output:
        print(
            _json.dumps(
                {
                    "status": "pass",
                    "paper_id": args.paper_id,
                    "plan": plan,
                },
                ensure_ascii=False,
            )
        )
    else:
        print(plan, end="")
    return 0


def cmd_compute_init(args):
    """Initialize Compute KB after initial setup."""
    import shutil
    from rsk.config import PROJECT_ROOT
    from rsk.schema.contract import builtin_template_root
    # Built-in computational schemas live under the plugin root, not workspace.
    src = builtin_template_root() / "computational"
    dst = PROJECT_ROOT / "computer_kb"
    if dst.exists():
        print("computer_kb/ already exists.")
        return
    shutil.copytree(src, dst)
    # Fusion layer (query router etc.) ships from the plugin workflow/ dir.
    wf_src = builtin_template_root().parent / "workflow" / "computer-kb"
    wf_dst = PROJECT_ROOT / "workflow" / "computer-kb"
    if wf_src.exists() and not wf_dst.exists():
        wf_dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(wf_src, wf_dst)
    _update_config("compute_kb.enabled", True)
    print("Compute KB initialized at computer_kb/")
    print("Storage isolation: kb/ (papers) | computer_kb/ (software)")
    print("Answer fusion: workflow/computer-kb/query_router.md")


def _print_cli_result(payload, *, json_output, stream=None):
    import json as _json

    if json_output:
        print(_json.dumps(payload, ensure_ascii=False), file=stream)
    elif payload["status"] == "pass":
        ready = payload["ready"]
        action = "reused" if payload.get("reused") else "completed"
        print(f"ResearchKeeper setup {action}.", file=stream)
        print(f"  Workspace: {ready['workspace']}", file=stream)
        print(f"  Model cache: {ready['model_cache']}", file=stream)
        print(f"  Device: {ready['device_mode']}", file=stream)
    else:
        print(payload["error"]["message"], file=stream or sys.stderr)


def _confirm_setup(prompt, *, json_output):
    stream = sys.stderr if json_output else sys.stdout
    print(f"{prompt} [y/N]: ", end="", file=stream, flush=True)
    return sys.stdin.readline().strip().lower() in {"y", "yes"}


def cmd_setup(args):
    """Run recoverable setup without downloading unless explicitly confirmed."""
    from contextlib import nullcontext, redirect_stdout
    import os

    from rsk.config import get_runtime_paths
    from rsk.install_state import InstallState
    from rsk.setup import (
        BgeM3Downloader,
        ConfirmationRequired,
        SetupError,
        dependency_lock_hash,
        run_setup,
    )

    paths = get_runtime_paths()
    plugin_data = os.environ.get("CLAUDE_PLUGIN_DATA", "").strip()
    data_dir = (
        Path(plugin_data).expanduser().resolve()
        if plugin_data
        else paths.user_data
    )

    if args.non_interactive and (not args.yes or args.device == "auto"):
        payload = {
            "status": "fail",
            "error": {
                "code": "confirmation_required",
                "message": (
                    "Non-interactive setup requires --yes and an explicit "
                    "--device cpu|cuda"
                ),
            },
        }
        _print_cli_result(payload, json_output=args.json_output)
        return 2

    if not args.json_output:
        print("ResearchKeeper setup")
        print(f"  Workspace: {paths.workspace}")
        print(f"  User data: {data_dir}")
        print(f"  Model cache: {paths.model_cache}")
        print("  Model download: approximately 2.2 GB")

    confirmed = args.yes
    if not confirmed:
        confirmed = _confirm_setup(
            "Create these directories and download/reuse bge-m3?",
            json_output=args.json_output,
        )
    if not confirmed:
        payload = {
            "status": "fail",
            "error": {
                "code": "confirmation_required",
                "message": "Setup cancelled before download",
            },
        }
        _print_cli_result(payload, json_output=args.json_output)
        return 2

    gpu_consent = args.device == "cuda"
    if args.device == "auto":
        gpu_consent = _confirm_setup(
            "Use CUDA when it is available?",
            json_output=args.json_output,
        )

    state = InstallState(data_dir)
    output_context = redirect_stdout(sys.stderr) if args.json_output else nullcontext()
    try:
        with output_context:
            result = run_setup(
                workspace=paths.workspace,
                data_dir=data_dir,
                model_cache=paths.model_cache,
                vector_db=paths.vector_db,
                downloader=BgeM3Downloader(),
                state=state,
                device=args.device,
                confirmed=True,
                gpu_consent=gpu_consent,
                lock_hash=dependency_lock_hash(),
            )
    except ConfirmationRequired as exc:
        payload = {
            "status": "fail",
            "error": {
                "code": "confirmation_required",
                "message": str(exc),
            },
        }
        _print_cli_result(payload, json_output=args.json_output)
        return 2
    except SetupError as exc:
        payload = {
            "status": "fail",
            "error": {
                "code": "setup_failed",
                "message": str(exc),
            },
        }
        _print_cli_result(payload, json_output=args.json_output)
        return 1

    payload = {
        "status": "pass",
        "reused": result.reused,
        "ready": result.ready,
    }
    _print_cli_result(payload, json_output=args.json_output)
    return 0


def cmd_doctor(args):
    """Report runtime health without modifying installation state."""
    import json as _json
    import os

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
    if args.json_output:
        print(_json.dumps(report, ensure_ascii=False))
    else:
        print(f"ResearchKeeper doctor: {report['status'].upper()}")
        for check in report["checks"]:
            print(
                f"  [{check['status'].upper()}] "
                f"{check['name']}: {check['message']}"
            )
    return 1 if report["status"] == "fail" else 0


def main(argv=None):
    p = argparse.ArgumentParser(
        description="ResearchKeeper — AI-assisted paper knowledge management"
    )
    p.add_argument(
        "--workspace",
        type=Path,
        help="ResearchKeeper workspace; overrides RSK_ROOT and current directory",
    )
    sub = p.add_subparsers(dest="command")

    sp_setup = sub.add_parser(
        "setup",
        help="Set up workspace, model cache, and recoverable installation state",
    )
    sp_setup.add_argument(
        "--workspace",
        dest="command_workspace",
        type=Path,
        help="ResearchKeeper workspace (subcommand alias for global --workspace)",
    )
    sp_setup.add_argument(
        "--device",
        choices=("auto", "cpu", "cuda"),
        default="auto",
    )
    sp_setup.add_argument("--non-interactive", action="store_true")
    sp_setup.add_argument(
        "--yes",
        action="store_true",
        help="Confirm workspace creation and model download/reuse",
    )
    sp_setup.add_argument("--json", action="store_true", dest="json_output")
    sp_setup.set_defaults(func=cmd_setup)

    sp_doctor = sub.add_parser(
        "doctor",
        help="Inspect Python, workspace, model, device, and vector state",
    )
    sp_doctor.add_argument(
        "--workspace",
        dest="command_workspace",
        type=Path,
        help="ResearchKeeper workspace (subcommand alias for global --workspace)",
    )
    sp_doctor.add_argument("--json", action="store_true", dest="json_output")
    sp_doctor.set_defaults(func=cmd_doctor)
    # ---- validate-si command ----
    def cmd_validate_si(args):
        """SI table numeric consistency validator for kb ingest data."""
        import subprocess as _sub

        candidates = []
        plugin_root = os.environ.get("CLAUDE_PLUGIN_ROOT", "").strip()
        if plugin_root:
            candidates.append(
                Path(plugin_root) / "scripts" / "validate_si_consistency.py"
            )
        candidates.extend(
            [
                Path(__file__).resolve().parents[1]
                / "scripts"
                / "validate_si_consistency.py",
                Path(sys.prefix)
                / "share"
                / "researchkeeper"
                / "plugin"
                / "scripts"
                / "validate_si_consistency.py",
            ]
        )
        script = next((path for path in candidates if path.is_file()), None)
        if script is None:
            print(
                "ResearchKeeper: validate-si helper is missing; "
                "reinstall the plugin.",
                file=sys.stderr,
            )
            raise SystemExit(1)
        cmd = [
            sys.executable, str(script),
            "--parsed-si", str(args.parsed_si),
        ]
        if args.extracted:
            cmd.extend(["--extracted", str(args.extracted)])
        elif args.extracted_dir:
            cmd.extend(["--extracted-dir", str(args.extracted_dir)])
        if args.json_output:
            cmd.append("--json")
        if getattr(args, "strict", False):
            cmd.append("--strict")
        result = _sub.run(
            cmd, capture_output=True, text=True, encoding="utf-8",
            env={**os.environ, "PYTHONIOENCODING": "utf-8"},
        )
        sys.stdout.write(result.stdout)
        if result.stderr:
            sys.stderr.write(result.stderr)
        sys.exit(result.returncode)

    sp_validate_si = sub.add_parser(
        "validate-si",
        help="Cross-reference kb ingest data against SI tables for value-condition mismatches",
    )
    sp_validate_si.add_argument(
        "--workspace", dest="command_workspace", type=Path,
        help="ResearchKeeper workspace",
    )
    sp_validate_si.add_argument(
        "--parsed-si", type=Path, required=True,
        help="Parsed SI markdown file (output of rsk parse)",
    )
    sp_validate_si.add_argument(
        "--extracted", type=Path, help="Single extracted JSON records file",
    )
    sp_validate_si.add_argument(
        "--extracted-dir", type=Path, help="Directory of extracted JSON files (batch)",
    )
    sp_validate_si.add_argument(
        "--strict", action="store_true",
        help="Enable dGad-context gating to reduce false mismatches",
    )
    sp_validate_si.add_argument(
        "--json", action="store_true", dest="json_output",
        help="Output results as JSON",
    )
    sp_validate_si.set_defaults(func=cmd_validate_si)


    from rsk.schema.cli import add_schema_parser

    add_schema_parser(sub)

    from rsk.provider.cli import add_provider_parser

    add_provider_parser(sub)

    sp_init = sub.add_parser("init", help="Initialize a new ResearchKeeper project")
    sp_init.add_argument("--interactive", action="store_true")
    sp_init.set_defaults(func=cmd_init)

    sp_import = sub.add_parser("import", help="Import papers from Zotero")
    sp_import.add_argument("--from-zotero", action="store_true")
    sp_import.add_argument("--db", help="Path to zotero.sqlite")
    sp_import.add_argument("-o", "--output", help="Output directory")
    sp_import.set_defaults(func=cmd_import)

    sp_parse = sub.add_parser("parse", help="Parse PDFs to Markdown text")
    sp_parse.add_argument(
        "--from-zotero",
        help="Batch parse from zotero_export.json",
    )
    sp_parse.add_argument("--output-dir", default="tmp")
    sp_parse.add_argument(
        "--pdf",
        help="Parse a single PDF file to Markdown (bypasses Zotero batch mode)",
    )
    sp_parse.add_argument(
        "--si",
        action="append",
        default=[],
        help="SI PDF path for single-file mode (repeatable)",
    )
    sp_parse.add_argument(
        "--output",
        help="Output .md path for single-file mode",
    )
    sp_parse.set_defaults(func=cmd_parse)

    sp_sync = sub.add_parser("sync", help="Sync kb to vector database (use --input/--input-dir to write JSON first)")
    sp_sync.add_argument("--full", action="store_true", help="Full rebuild")
    sp_sync.add_argument("--dry-run", action="store_true", help="Preview without writing")
    sp_sync.add_argument("--skip-claims", action="store_true", help="Skip claims index rebuild")
    sp_sync.add_argument("--from-claims", action="store_true", help="Rebuild claims only from claims_index.jsonl")
    sp_sync.add_argument("--input", help="Single JSON file to write to kb before sync")
    sp_sync.add_argument("--input-dir", help="Directory of JSON files to write to kb before sync")
    sp_sync.add_argument("--strict", action="store_true", help="Treat semantic warnings as errors (blocks write)")
    sp_sync.set_defaults(func=cmd_sync)

    sp_search = sub.add_parser("search", help="Semantic search the knowledge base")
    sp_search.add_argument("query", help="Search query")
    sp_search.add_argument("--claims", action="store_true")
    sp_search.add_argument("--top", type=int, default=5)
    sp_search.add_argument("--json", action="store_true", dest="json_output")
    sp_search.add_argument("--expand", action="store_true", help="Expand results to all modules of hit papers")
    sp_search.set_defaults(func=cmd_search)

    sp_serve = sub.add_parser("serve", help="Start persistent query server")
    sp_serve.add_argument("--port", type=int, default=8765)
    sp_serve.set_defaults(func=cmd_serve)

    sp_diff = sub.add_parser("diff", help="Show Zotero vs kb differences")
    sp_diff.add_argument("--from-zotero", action="store_true")
    sp_diff.set_defaults(func=cmd_diff)

    sp_verify = sub.add_parser("verify", help="Verify ingest coverage for a paper")
    sp_verify.add_argument("paper_id")
    sp_verify.add_argument("--json", action="store_true", dest="json_output")
    sp_verify.set_defaults(func=cmd_verify)

    sp_fix = sub.add_parser("fix-ids", help="Normalize paper IDs across kb modules")
    sp_fix.set_defaults(func=cmd_fix_ids)

    sp_audit = sub.add_parser("audit-sync", help="Run vector sync integrity audit")
    sp_audit.set_defaults(func=cmd_audit_sync)

    sp_frontmatter = sub.add_parser(
        "wiki-frontmatter",
        help="Generate a read-only bibliography-backed frontmatter candidate",
    )
    sp_frontmatter.add_argument("paper_id")
    sp_frontmatter.add_argument(
        "--existing",
        type=Path,
        help="Existing Markdown or YAML file to compare without writing",
    )
    sp_frontmatter.add_argument(
        "--json",
        action="store_true",
        dest="json_output",
    )
    sp_frontmatter.set_defaults(func=cmd_wiki_frontmatter)

    sp_experiment = sub.add_parser(
        "experiment-plan",
        help="Generate a role-driven reproduction plan from KB evidence",
    )
    sp_experiment.add_argument("paper_id")
    sp_experiment.add_argument(
        "--json",
        action="store_true",
        dest="json_output",
    )
    sp_experiment.set_defaults(func=cmd_experiment_plan)

    sp_compute = sub.add_parser("compute", help="Compute KB management (Phase 2)")
    sp_compute.add_argument(
        "--workspace",
        dest="command_workspace",
        type=Path,
        help="ResearchKeeper workspace (subcommand alias for global --workspace)",
    )
    sp_compute_sub = sp_compute.add_subparsers(dest="compute_cmd")
    sp_comp_init = sp_compute_sub.add_parser("init", help="Initialize Compute KB")
    sp_comp_init.add_argument(
        "--workspace",
        dest="command_workspace",
        type=Path,
        default=argparse.SUPPRESS,  # Don't override parent sp_compute's value
        help="ResearchKeeper workspace (subcommand alias for global --workspace)",
    )
    sp_comp_init.set_defaults(func=cmd_compute_init)

    args = p.parse_args(argv)
    if not args.command:
        p.print_help()
        sys.exit(1)

    from rsk.config import configure_runtime_paths

    command_workspace = getattr(args, "command_workspace", None)
    configure_runtime_paths(command_workspace or args.workspace)
    result = args.func(args)
    return result if isinstance(result, int) else 0


if __name__ == "__main__":
    raise SystemExit(main())
