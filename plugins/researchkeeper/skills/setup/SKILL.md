---
name: setup
description: Use when a user asks to install, bootstrap, repair, or reconfigure the ResearchKeeper Claude Code plugin.
disable-model-invocation: true
---

# Set up ResearchKeeper

Keep dependency bootstrap and model setup user-triggered. Never install
dependencies or download a model from SessionStart.

## 1. Preflight and consent

1. Resolve `${CLAUDE_PLUGIN_ROOT}` and `${CLAUDE_PLUGIN_DATA}`. If the host
   injected them, use those values. Otherwise derive them:
   - `${CLAUDE_PLUGIN_ROOT}`: the plugin root is the parent directory of the
     folder containing `scripts\bootstrap_plugin.py`. On Windows:
     `Split-Path (Split-Path (Resolve-Path "<path-to-plugin>\scripts\bootstrap_plugin.py"))`.
   - `${CLAUDE_PLUGIN_DATA}`: `$env:USERPROFILE\.claude\plugins\data\researchkeeper-researchkeeper-local`.
   Show the resolved values before proceeding.
2. Run `py -3.11 --version` on Windows or `python3.11 --version` on POSIX.
3. Ask the user to choose the dependency profile: `cpu` (default) or `cuda`.
   GPU visibility does not imply CUDA consent.
4. Show the detected Python version, plugin data directory, selected profile,
   applicable dependency lock(s), and whether an active installation already
   exists.
5. Explain that bootstrap creates or reuses an isolated profile-and-lock-hash
   venv. Ask for explicit consent before running it.

## 2. Bootstrap dependencies

Use exactly one verified Python 3.11 launcher. First resolve
`CLAUDE_PLUGIN_ROOT` / `CLAUDE_PLUGIN_DATA` per step 1, then:

```powershell
py -3.11 "${CLAUDE_PLUGIN_ROOT}\scripts\bootstrap_plugin.py" --plugin-root "${CLAUDE_PLUGIN_ROOT}" --plugin-data "${CLAUDE_PLUGIN_DATA}" --device cpu
```

```bash
python3.11 "${CLAUDE_PLUGIN_ROOT}/scripts/bootstrap_plugin.py" --plugin-root "${CLAUDE_PLUGIN_ROOT}" --plugin-data "${CLAUDE_PLUGIN_DATA}" --device cpu
```

For an explicitly approved CUDA profile, replace `--device cpu` with
`--device cuda`. This installs the pinned CUDA overlay after the CPU-default
lock and performs an actual `torch.cuda` tensor smoke before activation. On
Windows, CUDA venvs use a managed short root under
`${env:LOCALAPPDATA}\ResearchKeeper\cuda-venvs`; bootstrap fails before
installation if the projected torch path is unsafe. In that case rerun with a
short, user-writable `--venv-root`.

Bootstrap installs dependencies only. It must not download bge-m3.

## 3. Explicit workspace and schema

Ask the user to choose an explicit workspace. Run `schema status --json`.
When it is unconfigured, invoke `/researchkeeper:configure-schema`. Continue
only after structural validation reports a configured schema.

### 3.1 Compute KB initialization

After schema is confirmed, initialize the Compute KB for calculation knowledge
management:

```bash
rsk compute init --workspace <selected-workspace>
```

This copies the built-in computational schema records, wiki, and workflow
tools to `computer_kb/` under the workspace.  If `computer_kb/` already
exists the command is a no-op.  This step is required before the user can
query calculation-related knowledge through the query router.

## 4. Model and workspace setup

Run the platform wrapper with `doctor --json` and show its paths and checks.
Use the same `cpu` or `cuda` choice that was explicitly selected for dependency
bootstrap. Before running `setup`, disclose the bge-m3 download size and obtain
separate confirmation. Schema approval never implies model-download or device
consent.

Use `--non-interactive --yes` only after recording that confirmation. Do not
infer GPU consent from GPU availability.

## Recovery

| Failure | Recovery |
|---|---|
| Python is not 3.11.x | Install Python 3.11, then rerun bootstrap with that launcher. |
| Dependency install or smoke fails | Rerun bootstrap; the prior active venv remains selected. |
| Windows CUDA path preflight fails | Rerun bootstrap with `--venv-root` set to a shorter user-writable path. |
| CUDA overlay or tensor smoke fails | Preserve the failure, then either repair the CUDA prerequisites or explicitly choose the CPU profile and rerun bootstrap. |
| CUDA is unavailable or incompatible during model setup | Explicitly choose the CPU profile, rerun bootstrap, then run setup with `--device cpu`. |
| Model download or setup fails | Run `doctor --json`, preserve the failure record, then rerun setup. |
