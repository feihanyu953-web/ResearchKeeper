# Installation and first setup

ResearchKeeper v0.2.0 supports Python **3.11.x** only (`>=3.11,<3.12`). It has a standalone CLI and a Claude Code plugin entry point. A workspace holds the schema, KB, and vector index; installation and model cache remain separate from it.

## Standalone CLI

From a source checkout or built distribution, use a verified Python 3.11 launcher. The base installation includes runtime packages for bge-m3; use the `dev` extra only for development and testing.

```powershell
py -3.11 -m pip install .
```

```bash
python3.11 -m pip install .
```

Choose a workspace explicitly. Do not use the package installation directory as the workspace.

```bash
rsk schema status --workspace <workspace> --json
rsk schema list --json
```

Prepare a valid proposal outside `kb/`, validate it, show the preview to the workspace owner, and apply it only after approval:

```bash
rsk schema validate --workspace <workspace> --proposal <proposal> --json
rsk schema apply --workspace <workspace> --proposal <proposal> --yes --json
rsk schema status --workspace <workspace> --json
rsk doctor --workspace <workspace> --json
```

Start from `generic-science` or `electrocatalysis`, or create a custom proposal as described in [schema customization](schema-customization.md). Do not use the legacy generic three-module or interactive `rsk init` flow as v0.2.0 first-installation guidance.

After a valid schema exists, run setup. `--yes` explicitly confirms workspace creation and model download/reuse; choose `cpu` unless CUDA was separately selected by the user.

```bash
rsk setup --workspace <workspace> --device cpu --non-interactive --yes --json
rsk doctor --workspace <workspace> --json
```

## Claude Code plugin

This release candidate has no published marketplace source or identifier. For pre-release local testing, extract or otherwise use the plugin root and start a Claude Code session with the local plugin directory:

```bash
claude --plugin-dir <plugin-root>
```

If the package provides a plugin `.zip`, use that package as the local plugin source according to the Claude Code CLI's supported local-plugin workflow. This local-source path is **session-only**. Persistent installation with `claude plugin install <plugin>@<marketplace>` applies only after an actual marketplace source and identifier have been published or configured; do not invent either value for this release candidate.

The plugin uses `${CLAUDE_PLUGIN_ROOT}` for immutable files and `${CLAUDE_PLUGIN_DATA}` for isolated dependency/bootstrap state. In the loaded Claude Code session invoke:

```text
/researchkeeper:setup
```

The setup skill checks Python 3.11, plugin-data directory, dependency locks,
selected CPU/CUDA profile, and active installation, then asks before
bootstrapping dependencies. CPU remains the default. CUDA must be explicitly
selected before bootstrap so the pinned overlay is installed and verified
before model setup. Provide an explicit workspace and use the
first-installation skill below; setup separately requests model-download
consent after schema validation.

## First schema in an empty KB

Invoke:

```text
/researchkeeper:configure-schema
```

This workflow is only for an explicit workspace with no paper records:

1. It runs `schema status --json` and stops for `configured_nonempty` or `invalid`.
2. It lists `generic-science` and `electrocatalysis`, gathers the research area and desired concrete modules, and preserves all seven roles.
3. It saves a proposal outside KB content paths, validates it, and previews the exact module-to-file and module-to-role mapping.
4. It applies only after explicit approval, then runs `schema status` and `doctor`.

It does not bootstrap dependencies, download a model, create embeddings, or write vector indexes. A non-empty KB is fail-closed in v0.2.0: there is no automatic migration, replacement, schema generation, or rollback. Export and review existing data before choosing a separately approved migration approach.

## Model, cache, and device consent

First setup downloads or reuses BAAI/bge-m3. Budget approximately **2.2 GB** for the initial model transfer; the exact size varies by upstream revision and transport. `doctor --json` reports the resolved model path. Standalone and plugin runtime use the platform-specific ResearchKeeper user-cache `models/` directory, never a project-local `models/` directory. Plugin active-install state and CPU dependency venvs are under `${CLAUDE_PLUGIN_DATA}`. Windows CUDA venvs use the managed short root documented below; `active.json` records their absolute location. None of these environments are stored in the model cache.

Model download is **Hugging Face first, ModelScope fallback** (useful when `huggingface.co` is unreachable, e.g. mainland China without a proxy). Both paths pin an immutable commit hash so the snapshot stays auditable. The ModelScope fallback normally resolves the master commit hash automatically via `git ls-remote`; when that resolution fails (no `git`, or the remote is unreachable), setup fails with a message showing how to resolve and pin the hash manually:

```powershell
git ls-remote https://www.modelscope.cn/BAAI/bge-m3.git HEAD
# → <40-hex commit hash>
$env:RSK_BGE_MODELSCOPE_REVISION = "<40-hex commit hash>"
rsk setup --workspace <ws> --device cpu --non-interactive --yes --json
```

`RSK_BGE_MODELSCOPE_REVISION` always overrides automatic resolution when set.

### Retrieval tuning (workspace `configs/retrieval.yaml`)

Claim/chunk truncation limits and query scoring knobs resolve by priority:
**environment variable → workspace `configs/retrieval.yaml` → built-in default**.
Persist tuning decisions in the workspace so they survive sessions and
processes (the AI can write this file after a vector audit instead of setting
session env vars):

```yaml
# {workspace}/configs/retrieval.yaml
retrieval:
  claim_value_limit: 160    # per-field cap in claim text (RSK_CLAIM_VALUE_LIMIT)
  chain_value_limit: 60     # per-segment cap in chain claims (RSK_CHAIN_VALUE_LIMIT)
  chain_total_limit: 1100   # total chain cap, segments dropped whole (RSK_CHAIN_TOTAL_LIMIT)
  keyword_boost: 0.45       # keyword-overlap weight (RSK_KEYWORD_BOOST)
  quota_literature: 2       # diversity quotas (RSK_QUOTA_LITERATURE / _CHAIN / _CLAIMS)
  quota_chain: 1
  quota_claims: 2
```

Defaults are tuned for long descriptive values (e.g. Chinese medical
literature); short structured records (electrocatalysis) work with the same
defaults.

CUDA/GPU is optional acceleration. CPU is a complete supported fallback; use
`--device cpu` when CUDA is absent, incompatible, or not approved. GPU
availability never provides consent, and schema approval never authorizes a
model download.

The plugin bootstrap has two dependency profiles:

```powershell
# CPU default
py -3.11 "${CLAUDE_PLUGIN_ROOT}\scripts\bootstrap_plugin.py" --plugin-root "${CLAUDE_PLUGIN_ROOT}" --plugin-data "${CLAUDE_PLUGIN_DATA}" --device cpu

# Explicit CUDA 12.8 overlay
py -3.11 "${CLAUDE_PLUGIN_ROOT}\scripts\bootstrap_plugin.py" --plugin-root "${CLAUDE_PLUGIN_ROOT}" --plugin-data "${CLAUDE_PLUGIN_DATA}" --device cuda
```

The CUDA profile installs `requirements.cuda.lock` after the base lock and
does not activate the environment unless importing torch, detecting the CUDA
runtime, reporting `torch.cuda.is_available()`, and allocating a small CUDA
tensor all succeed. CPU and CUDA use different environment identities.

On Windows, the CUDA profile defaults to the shorter per-user root
`${env:LOCALAPPDATA}\ResearchKeeper\cuda-venvs`. A conservative preflight
rejects a projected torch installation path that could exceed legacy
`MAX_PATH`; rerun with a shorter user-writable path when needed:

```powershell
py -3.11 "${CLAUDE_PLUGIN_ROOT}\scripts\bootstrap_plugin.py" --plugin-root "${CLAUDE_PLUGIN_ROOT}" --plugin-data "${CLAUDE_PLUGIN_DATA}" --device cuda --venv-root "C:\rsk-venvs"
```

## Verification states

`doctor --json` reports Python, installation state, workspace, schema, model, device, and vector-db state. A structurally configured empty KB is usable for schema validation but contains no records or embeddings. Content, vector, and retrieval audits are **N/A**, not PASS, until those inputs exist.
