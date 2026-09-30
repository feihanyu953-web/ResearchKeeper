# Schema customization

Schema customization is a first-installation operation for an explicit empty workspace. It decides the files into which future paper records will be routed; it does not infer or rewrite an existing KB.

## Built-in proposals and seven roles

`rsk schema list --json` exposes two builtin proposal sources:

| Builtin | Concrete module mapping |
|---|---|
| `generic-science` | `literature→literature`, `entities→entities`, `methods→methods`, `conditions→conditions`, `results→results`, `relations→relations`, `claims→claims` |
| `electrocatalysis` | `literature→literature`, `entities→entities`, `synthesis→methods`, `methods→methods`, `conditions→conditions`, `performance→results`, `spectra→results`, `mechanism→relations`, `claims→claims` |

The stable semantic roles are `literature`, `entities`, `methods`, `conditions`, `results`, `relations`, and `claims`. Every proposal represents all seven, and exactly one module has the `literature` role. Multiple concrete modules may share another role, as `synthesis` and `methods` do in the electrocatalysis builtin.

## Custom proposal contract

A custom YAML or JSON proposal contains `template_id`, `template_version`, `schema_version: schema_v1`, `modules`, and `vector_gate_queries`. Every module must include:

```text
name, display, file, role, description, trigger_keywords,
extract_rules, audit_focus
```

Names and files must be unique safe relative names; a module file is a simple `.md` filename, not a path. Each vector-gate query has `query` and `expected_role` selected from the seven roles. Save the proposal outside `kb/`, `schemas/generated/`, and formal content paths.

Validate before requesting approval:

```bash
rsk schema validate --workspace <workspace> --proposal <proposal> --json
```

The preview reports selected modules, files, roles, and vector-gate query count. The workspace owner reviews that exact map. Only then apply:

```bash
rsk schema apply --workspace <workspace> --proposal <proposal> --yes --json
rsk schema status --workspace <workspace> --json
```

`--yes` is the CLI representation of explicit approval.

## Fail-closed lifecycle

First materialization writes an active module map, vector-gate config, KB protocol files, coverage directory, and empty module tables. Applying the byte-identical proposal again to the same empty workspace is idempotent. Conflicting proposals fail, as does any structural change after real KB records exist. ResearchKeeper v0.2.0 does **not** automatically migrate, replace, version, or roll back a non-empty KB.

## Coverage declarations

Each paper needs a coverage declaration for every active concrete module:

| Status | Meaning | Required evidence |
|---|---|---|
| `covered` | A source-backed record is present in the module. | Record source identifies the paper/SI location. |
| `not_applicable` | The module genuinely does not apply to the paper. | State the reason and quote or point to original paper/SI evidence checked. An unavailable source cannot be verified as PASS. |
| `missing` | Applicable content is absent or not extracted. | State what is missing; this is not completion. |

Coverage is audit metadata and excluded from semantic embeddings. An independent read-only reviewer verifies `not_applicable` evidence rather than accepting the writer's assertion.

## Empty-KB audit semantics

After schema materialization but before papers are ingested, the KB can be `configured_empty` and pass structural validation. It has no paper content, vectors, or retrieval corpus. Content audit, vector audit, and retrieval audit are therefore **N/A**, not PASS. Do not convert N/A into a quality or release claim.
