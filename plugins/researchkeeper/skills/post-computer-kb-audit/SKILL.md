---
name: post-computer-kb-audit
description: Use when modifications to computer_kb/**/*.md files are complete and audit + receipt generation is needed. Same architecture as post-kb-audit — enforces a fact-only prompt template for computer-kb-independent-reviewer to prevent the main AI from injecting bias or scope limitations.
---

# Post-Computer-KB Audit

## Overview

Wraps `computer-kb-independent-reviewer` invocation in a fixed prompt template. Identical architecture to `post-kb-audit` but targets the `computer_kb/` gate. The main AI cannot modify the reviewer's instructions — it can only supply facts.

## When to Use

- After any `Edit`/`Write`/`MultiEdit` to `computer_kb/**/*.md`
- After adding/modifying records, wiki pages, workflows, errors, relations, templates, or error chains
- After fixing issues from a previous FAIL report

Do NOT invoke mid-edit — only when all planned modifications are done.

## Mandatory Reads (before spawning reviewer)

```
CLAUDE.md -> workflow/computer-kb/query_router.md -> computer_kb/REVIEWER.md -> computer_kb/INDEX.md -> computer_kb/SCHEMA.md
```

## Step 1: Collect Facts

Run `git diff --name-only` to list modified files under `computer_kb/`.

Collect from the conversation context:
- Records/wiki/workflows/errors involved
- Paths to reference materials (official docs, error logs, verified evidence), if available
- Task type in <=5 words (e.g., "新增VASP record", "补充error_chain", "workflow更新")

## Step 2: Build Neutral Prompt

The prompt sent to `computer-kb-independent-reviewer` MUST follow this exact template. Do NOT add, remove, or rephrase any section.

```text
Task type: <<=5 words, factual only — "新增records" / "wiki更新" / "error_chain补充">

Modified files:
- <path relative to project root>
- ...

Reference materials (if available):
- Official docs: <path/URL or "not provided">
- Error logs: <path or "not provided">
- Local evidence: <path or "not provided">

Audit independently per computer_kb/REVIEWER.md. Read computer_kb/INDEX.md, computer_kb/SCHEMA.md, and all modified files before reaching a verdict. If modifications cite paper kb/*.md, read those as cross-reference only.
```

### Template Rules (NON-NEGOTIABLE)

The prompt MUST NOT contain:
- "PASS expected" / "should be fine" / "only a quick check needed"
- "只检查" / "快速" / "简要" / "Be concise" / "spot-check"
- "我已经确认" / "verified" / "confirmed"
- Any statement about what the working AI believes is true
- Scope limitations (e.g., "just check storage isolation")

The prompt MUST contain exactly:
- Task type (<=5 words)
- Modified file paths
- Reference material paths (or "not provided")

## Step 3: Spawn Reviewer

```
Agent(
  subagent_type: "computer-kb-independent-reviewer",
  model: "sonnet",
  prompt: <the exact template from Step 2>
)
```

The reviewer is read-only. It will output a PASS/FAIL report per `computer_kb/REVIEWER.md` format (13 dimensions A-M, including wiki link integrity check via `check_wiki_links.py`).

## Step 4: Act on Report

**If PASS:**
1. Save the reviewer report under `computer_kb\.audit\reports\`.
2. Compute its SHA256 digest with `Get-FileHash -Algorithm SHA256`.
3. Run
   `powershell "${CLAUDE_PLUGIN_ROOT}/audit/scripts/New-ComputerKbAuditReceipt.ps1" -ProjectRoot "<explicit workspace>" -ReviewerReportDigest <sha256>`.
4. Append reviewer summary to `computer_kb/REVIEWER_LOG.md`.
5. Report to user: "Audit PASS, receipt generated."

**If FAIL:**
1. Fix all BLOCKING items
2. Return to Step 2 (max 3 rounds total)
3. After PASS, save/hash the reviewer report, then run receipt + log
4. A failure remains BLOCKING after three rounds unless every failed item has:
   a specific technical reason, attempted fixes, remaining risk, corresponding
   files and evidence; the decision is written to the reviewer log; and the
   user explicitly confirms the deferral. Generic schedule or change-size
   statements are not sufficient reasons by themselves.

## Gate Independence

The `computer_kb` gate is independent of the `kb/wiki` gate. A PASS receipt from one does NOT clear the other. If both `kb/wiki` and `computer_kb` were modified, both audit skills must be invoked separately.

## Common Mistakes

- **Using kb-independent-reviewer for computer_kb files**: The two reviewers have different protocols. Use the correct one.
- **Skipping the template**: Writing a custom prompt defeats the purpose — the skill exists to prevent prompt bias.
- **Substituting receipts**: `New-ComputerKbAuditReceipt.ps1` != `New-AuditReceipt.ps1`. Use the right script.
- **Empty digest receipts**: Do not generate PASS receipts without a reviewer report digest. `-AllowMissingReviewerDigest` is only for explicit legacy recovery.
