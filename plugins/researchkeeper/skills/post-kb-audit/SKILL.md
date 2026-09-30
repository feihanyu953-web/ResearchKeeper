---
name: post-kb-audit
description: Use when modifications to kb/*.md or wiki/*.md files are complete and audit + receipt generation is needed. This skill hardens the reviewer invocation by enforcing a fact-only prompt template that prevents the main AI from injecting coverage predictions, PASS/FAIL bias, scope limitations, or diagnostic conclusions into the reviewer's instructions.
---

# Post-KB Audit

## Overview

Wraps `kb-independent-reviewer` invocation in a fixed prompt template. The main AI cannot modify the reviewer's instructions — it can only supply facts. This eliminates the "biased prompt" loophole where the working AI steers the reviewer toward a predetermined verdict.

## When to Use

- After any `Edit`/`Write`/`MultiEdit` to `kb/**/*.md` or `wiki/**/*.md`
- After batch ingest, schema migration, or wiki sync
- After fixing issues from a previous FAIL report

Do NOT invoke mid-edit — only when all planned modifications are done.

## Mandatory Reads (before spawning reviewer)

```
CLAUDE.md → docs/paper-reader/GATES.md → schemas/generated/modules.yaml → kb/INDEX.md → kb/SCHEMA.md → kb/REVIEWER.md → kb/coverage/<paper_id>.md
```

## Step 1: Collect Facts

Run `git diff --name-only` to list modified files under `kb/` and `wiki/`.

Collect from the conversation context:
- Paper IDs involved (e.g., `Liu2026_GB`, `Yan2026`)
- Paths to pdf_parser.py 输出 / PDF / SI source materials, if available
- Task type: MUST be one of the following enum values (no free-form):
  - `batch-ingest` — 完整批量入库，reviewer 强制检查活动 concrete modules
    的逐模块 coverage，并独立核验每个 N/A
  - `lit-index-only` — 仅文献索引（仅限用户明确要求或纯综述论文）
  - `module-supplement` — 已有论文补充模块记录
  - `schema-migration` — 格式/版本迁移，不检查模块覆盖
  - `wiki-sync` — wiki 展示层同步

## Step 2: Build Neutral Prompt

The prompt sent to `kb-independent-reviewer` MUST follow this exact template. Do NOT add, remove, or rephrase any section.

```text
Task type: <batch-ingest | lit-index-only | module-supplement | schema-migration | wiki-sync>

Modified files:
- <path relative to project root>
- ...

Paper IDs:
- <paper_id>
- ...

Source materials (if available):
- pdf_parser.py 输出: <path or "not provided">
- PDF: <path or "not provided">
- SI: <path or "not provided">

Audit independently per kb/REVIEWER.md. Read CLAUDE.md, kb/INDEX.md, kb/SCHEMA.md, and all modified files before reaching a verdict.
```

### Template Rules (NON-NEGOTIABLE)

The prompt MUST NOT contain:
- "all active modules are covered" or any coverage/N/A prediction
- "PASS expected" / "should be fine" / "only a quick check needed"
- "只检查" / "快速" / "简要" / "Be concise" / "spot-check"
- "我已经确认" / "verified" / "confirmed"
- Record count summaries (e.g., "added 48 new records")
- Any statement about what the working AI believes is true

The prompt MUST contain exactly:
- Task type (≤5 words, descriptive not diagnostic)
- Modified file paths
- Paper IDs
- Source material paths (or "not provided")

## Step 3: Spawn Reviewer

```
Agent(
  subagent_type: "kb-independent-reviewer",
  model: "sonnet",
  prompt: <the exact template from Step 2>
)
```

The reviewer is read-only. It will output a PASS/FAIL report per `kb/REVIEWER.md` format (12 dimensions: 0, A-K + J2 chain claim coverage).

## Step 4: Act on Report

**If PASS:**
1. Save the reviewer report under `kb/.audit/reports/`.
2. Compute its SHA256 digest with `Get-FileHash -Algorithm SHA256`.
3. Run
   `powershell "${CLAUDE_PLUGIN_ROOT}/audit/scripts/New-AuditReceipt.ps1" -ProjectRoot "<explicit workspace>" -ReviewerReportDigest <sha256>`.
4. Append reviewer summary to `kb/REVIEWER_LOG.md`.
5. Report to user: "Audit PASS, receipt generated."

**If FAIL:**
1. Fix all BLOCKING items
2. Return to Step 2 (max 3 rounds total)
3. After PASS, save/hash the reviewer report, then run receipt + log
4. A failure remains BLOCKING after three rounds unless every failed item has:
   a specific technical reason, attempted fixes, remaining risk, corresponding
   files and evidence; the decision is written to the reviewer log; and the
   user explicitly confirms the deferral. "Time is insufficient" or "the
   change is too large" is not a sufficient reason by itself.

## Common Mistakes

- **Adding coverage predictions to the prompt**: The reviewer must compare each
  active module and every N/A with the original paper/SI independently.
- **Skipping the template**: Writing a custom prompt that "just tells the reviewer what to check" is the exact loophole this skill closes.
- **Not providing source material paths**: If pdf_parser.py 输出/PDF is available but not listed, the reviewer cannot verify against ground truth.
- **Delegating receipt generation to reviewer**: The reviewer is read-only.
  The main AI saves the report, computes the digest, and runs the plugin-root
  receipt script with explicit `-ProjectRoot` and reviewer digest.
- **Empty digest receipts**: Do not generate PASS receipts without a reviewer report digest. `-AllowMissingReviewerDigest` is only for explicit legacy recovery.
