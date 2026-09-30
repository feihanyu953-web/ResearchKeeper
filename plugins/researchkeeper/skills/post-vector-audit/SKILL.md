---
name: post-vector-audit
description: Use after running `rsk sync` when vector_db/ has been modified. Enforces a two-layer audit (sync integrity + retrieval quality) via vector-retrieval-auditor agent with a fact-only prompt template that prevents the main AI from injecting bias.
---

# Post-Vector Audit

## Overview

Wraps the two-layer vector audit in a fixed prompt template. After `rsk sync` runs, this skill:
1. Runs `rsk audit-sync` (Layer 1 — deterministic)
2. Spawns `vector-retrieval-auditor` agent (Layer 2 — semantic retrieval quality + Layer 2b chain claim audit)
3. Guides the main AI through fix → `New-VectorAuditReceipt.ps1` → log

## When to Use

- After any run of `rsk sync` (incremental or full)
- Before ending a session that modified `vector_db/`

## Mandatory Reads

```
CLAUDE.md → docs/paper-reader/GATES.md → schemas/generated/modules.yaml → schemas/generated/vector_gate_queries.yaml → vector_db/REVIEWER.md
```

## Step 1: Run Layer 1 (sync audit)

```powershell
$projectRoot = "<explicit workspace>"
$rsk = Join-Path $env:CLAUDE_PLUGIN_ROOT "bin\rsk.cmd"
& $rsk --workspace $projectRoot audit-sync
```

If exit code != 0 (FAIL), identify issues from stdout, fix root cause, re-run `rsk sync`, then re-run this step. Do NOT proceed to Step 2 until Layer 1 status is PASS or WARN.

## Step 2: Collect Facts

Gather ONLY factual inputs:
- Path: `vector_db/summary.json`
- Path: `schemas/generated/vector_gate_queries.yaml`
- Path: `records/vector_audit_log.jsonl` (latest sync entry)
- Any kb files recently added/modified (from git diff or sync summary)

## Step 3: Spawn Reviewer with Neutral Prompt

The prompt sent to `vector-retrieval-auditor` MUST follow this exact template:

```text
Task type: vector sync audit

Sync summary: vector_db/summary.json
Gate config: schemas/generated/vector_gate_queries.yaml
Audit log: records/vector_audit_log.jsonl
KB directory: kb/
Vector DB: vector_db/

Audit independently per vector_db/REVIEWER.md. Run every query in the active
gate list via `rsk search` (`--claims` for kb_claims, default for kb_papers).
Resolve each `expected_role` through the active module mapping. Also run any
configured chain_test_queries. Apply each query's scenario, language, expected
behavior, and expected role ground truth. Evaluate fidelity, recall, chunk
quality, chain claim coverage, and consistency per the protocol.
```

### Template Rules (NON-NEGOTIABLE)

The prompt MUST NOT contain:
- "sync went well" / "should be fine"
- "只检查" / "快速" / "简要" / "spot-check"
- Any fidelity/recall prediction
- Any PASS pre-verdict
- Record counts or coverage numbers from the main AI

## Step 4: Act on Report

**If PASS:**
1. Save the retrieval audit report under `vector_db/.audit/reports/`.
2. Compute its SHA256 digest with `Get-FileHash -Algorithm SHA256`.
3. Run
   `powershell "${CLAUDE_PLUGIN_ROOT}/audit/scripts/New-VectorAuditReceipt.ps1" -ProjectRoot "<explicit workspace>" -RetrievalReportDigest <sha256>`.
4. Append reviewer's JSONL line to `records/vector_audit_log.jsonl`.
5. Report to user: "Vector audit PASS, receipt generated."

**If FAIL:**
1. Identify root cause (missing kb files → re-sync; poor chunking → adjust chunk_size/overlap in `rsk/vector/sync.py`; bad retrieval → check embedding model)
2. Fix and re-run `rsk sync`
3. Return to Step 1 (max 3 rounds)
4. After PASS, save/hash the retrieval audit report, then run receipt + log
5. A failure remains BLOCKING after three rounds unless every failed item has
   a specific technical reason, attempted fixes, remaining risk, corresponding
   files and evidence; the decision is written to the reviewer log; and the
   user explicitly confirms the deferral. Generic schedule or change-size
   statements are not sufficient reasons by themselves.

Do not generate PASS receipts without a retrieval audit report digest. `-AllowMissingRetrievalDigest` is only for explicit legacy recovery.

## Gate Independence

The vector gate is independent of kb/wiki gate and computer_kb gate. A PASS receipt from kb/wiki does NOT clear the vector gate. All three must pass independently.
