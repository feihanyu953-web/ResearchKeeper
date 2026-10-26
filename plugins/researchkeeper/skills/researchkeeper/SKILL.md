---
name: researchkeeper
description: Use when working with ResearchKeeper paper reading, knowledge retrieval, multi-paper comparison, batch triage/ranking, kb or wiki maintenance, vector search, VASP, or LAMMPS knowledge.
---

# Use ResearchKeeper

Run only the plugin wrapper backed by the active installation in
`${CLAUDE_PLUGIN_DATA}`. Never call an `rsk` executable found elsewhere on
PATH. If no active installation exists, ask the user to invoke
`/researchkeeper:setup`.

Before handling a paper, KB/wiki, enumeration, computation, or cross-domain
question, read
`${CLAUDE_PLUGIN_ROOT}/skills/researchkeeper/references/RSK-DETAILED-GUIDE.md`.
It preserves the detailed ResearchKeeper routing, retrieval hierarchy, evidence
labels, and write boundaries from the source `CLAUDE.md`. Apply it together
with this skill's explicit wrapper and workspace requirements.

## Select the workspace and route

Obtain an explicit workspace from the user and pass it with `--workspace`.
Keep the workspace separate from `${CLAUDE_PLUGIN_ROOT}` and
`${CLAUDE_PLUGIN_DATA}`.

Read the matching plugin workflow before acting:

| Task | Workflow |
|---|---|
| Paper reading or follow-up | `${CLAUDE_PLUGIN_ROOT}/workflow/paper-reading/READING.md` |
| Export notes or compile PDF | `${CLAUDE_PLUGIN_ROOT}/workflow/paper-reading/EXPORT.md` |
| Triage/rank a batch before ingest (title+abstract only) | `${CLAUDE_PLUGIN_ROOT}/workflow/paper-reading/TRIAGE.md` |
| Compare multiple papers on one topic (kb as source) | `${CLAUDE_PLUGIN_ROOT}/workflow/paper-reading/COMPARE.md` |
| Ingest papers | `${CLAUDE_PLUGIN_ROOT}/workflow/knowledge/INGEST.md` |
| Retrieve existing knowledge | `${CLAUDE_PLUGIN_ROOT}/workflow/knowledge/RETRIEVAL.md` |
| Modify wiki presentation | `${CLAUDE_PLUGIN_ROOT}/workflow/knowledge/WIKI_SYNC.md` |
| Vector sync or search | `${CLAUDE_PLUGIN_ROOT}/workflow/vector/VECTOR.md` |

Use `${CLAUDE_PLUGIN_ROOT}/bin/rsk` on POSIX and
`${CLAUDE_PLUGIN_ROOT}\bin\rsk.cmd` on Windows.

For an experiment-reproduction request, run
`experiment-plan <paper_id>` after reading the active schema. Treat its output
as an evidence-bound candidate: preserve every `（待补充）` gap, and do not add
a computational section unless the command found explicit DFT/MD method
records.

## Evidence and write boundary

For domain questions, run `search "<question>" --claims --top 5 --expand`
before answering. Label knowledge-base evidence separately from external
sources and AI inference. Never invent missing values.

Before any kb or wiki write, read
`schemas/generated/modules.yaml`, `kb/INDEX.md`, `kb/SCHEMA.md`, and
`kb/REVIEWER.md`; show the candidate change and obtain user approval. Route
through the active concrete `name -> file` mapping. Every paper must declare
`covered`, `not_applicable`, or `missing` for every active module. A
`not_applicable` declaration requires a reason and checked evidence and must
be verified by the independent reviewer. After an approved kb write, run the
required read-only audit and then perform incremental vector sync; do not
default to `--full`. Coverage and audit metadata must never be embedded.

Run `doctor --json` first when installation, model, device, or vector state is
uncertain. Report WARN or FAIL as-is and use `/researchkeeper:setup` for
recovery.
