# Provider Protocol v1

ResearchKeeper exposes a narrow machine-facing boundary through:

```bash
rsk --workspace <workspace> provider describe --json
rsk --workspace <workspace> provider doctor --json
rsk --workspace <workspace> provider <action> --request <request.json> --json
```

Protocol version is `1.0`; provider name is `rsk`; request actions are `query` and `write-candidate`. `describe` and `doctor` do not require a request file.

## Request and response boundary

An action request is a JSON object with exactly these fields:

```json
{
  "protocol_version": "1.0",
  "request_id": "run-001",
  "provider": "rsk",
  "action": "query",
  "inputs": {"query": "example", "top_k": 5, "claims": true},
  "output_dir": "artifacts/run-001"
}
```

`request_id` uses only letters, digits, `.`, `_`, and `-`, and is at most 128 characters. `output_dir` must be a nonempty native path. Unknown fields, wrong protocol/provider/action values, malformed input, and a CLI/request action mismatch are rejected.

Protocol stdout contains exactly one UTF-8 JSON document: either a success envelope or an error envelope. Action and library stdout are redirected to stderr, so callers must not parse diagnostics from stdout. Validation, dependency, execution, and protocol errors use distinct nonzero exit codes.

## `query`

`query` accepts exactly `query` (nonempty string), `top_k` (integer 1–100), and `claims` (boolean). It invokes the vector query boundary and writes `query-result.json` under `output_dir`, with artifact size and SHA-256 in the response. This is a read-oriented action with an output artifact; it does not modify the formal KB.

## `write-candidate` and approval boundary

`write-candidate` accepts exactly one input, `candidate`, a JSON object. It requires an initialized `kb/` and active `schemas/generated/modules.yaml`. The action copies both into a temporary shadow workspace, invokes the writer in dry-run mode, and compares the formal KB tree hash before and after.

Its `output_dir` must be outside `kb/`. On success it writes only these review artifacts outside the formal KB:

- `candidate.json`
- `candidate-preview.md`
- `candidate-provenance.json` (including schema fingerprint and before/after KB hashes)

This action does **not** write a candidate into the KB and does not constitute approval to do so. A person must inspect the preview and provenance and explicitly approve the normal KB write workflow. That later workflow must still read the active schema and KB policy, route by the active module-to-file map, preserve coverage declarations, and run its required read-only audit.
