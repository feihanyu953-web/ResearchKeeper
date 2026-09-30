---
name: audit-all
description: 手动触发全流程审计（kb/wiki gate + vector gate）。检查常驻服务、比对 tree hash、按需执行两层审计、生成 receipt、写入日志。当用户说"审计"/"audit"/"检查gate"/"生成receipt"时触发。
---

# Audit-All 手动审计 Skill

## 用途

用户手动触发完整的 kb + vector + computer_kb 审计流程。**不依赖任何 hook**，通过直接比对 tree hash 与 receipt 来判断是否需要审计。

首先读取活动 schema。若状态为 `configured_empty`，只报告
`schema gate: PASS`；content、vector sync、retrieval 均报告
`N/A (no knowledge records)`，不得生成这些层的 PASS receipt。

## 触发词

- `/audit-all`
- "审计" / "audit" / "检查gate" / "生成receipt" / "跑审计"

## 流程

### Step 0: 常驻服务检查（强制）

使用发布包内的单次启动与健康轮询脚本。它会先检查已有服务；只有不健康时
才启动一次，并在总超时内轮询 `/health`。进程提前退出与冷启动超时会分别
报错，并给出 stdout/stderr 日志路径。

```powershell
$projectRoot = "<explicit workspace>"
$rsk = Join-Path $env:CLAUDE_PLUGIN_ROOT "bin\rsk.cmd"
$serverLogs = Join-Path $env:CLAUDE_PLUGIN_DATA "logs"
$server = & "${CLAUDE_PLUGIN_ROOT}\audit\scripts\Ensure-RskQueryServer.ps1" `
    -RskCommand $rsk `
    -Workspace $projectRoot `
    -LogDirectory $serverLogs `
    -TimeoutSeconds 180 `
    -PollIntervalMilliseconds 1000
$server | ConvertTo-Json -Depth 4
```

`TimeoutSeconds` 可以按机器冷启动实测调整。脚本失败后必须读取所报告的日志
并停止当前 audit；不得无条件再次启动第二个服务进程。

### Step 1: 比对 tree hash（不依赖 hook）

**不用 hook，直接调用 `Get-TreeHashV1` 计算当前 hash 并与最新 receipt 比对。**

#### 1a. kb/wiki gate

```powershell
$projectRoot = "<explicit workspace>"
Set-Location -LiteralPath $projectRoot
. (Join-Path $env:CLAUDE_PLUGIN_ROOT "audit\lib\TreeHash.ps1")

$kbHash = Get-TreeHashV1 -ScanScope @("kb/**/*.md") -ExcludedPaths @("kb/REVIEWER_LOG.md", "kb/.audit/**", "kb/INDEX.md", "kb/SCHEMA.md", "kb/REVIEWER.md") -ProjectRoot $projectRoot
$wikiHash = Get-TreeHashV1 -ScanScope @("wiki/**/*.md") -ExcludedPaths @("wiki/index.md", "wiki/log.md") -ProjectRoot $projectRoot
$currentManifest = Get-FileManifestV1 -ScanScope @("kb/**/*.md", "wiki/**/*.md") -ExcludedPaths @("kb/REVIEWER_LOG.md", "kb/.audit/**", "kb/INDEX.md", "kb/SCHEMA.md", "kb/REVIEWER.md", "wiki/index.md", "wiki/log.md") -ProjectRoot $projectRoot

Write-Host "current kb_hash: $kbHash"
Write-Host "current wiki_hash: $wikiHash"

# 找最新 PASS receipt
$receiptDir = "kb\.audit\receipts"
$latest = Get-ChildItem $receiptDir -Filter "*.json" -File -ErrorAction SilentlyContinue |
    ForEach-Object { Get-Content $_.FullName -Raw -Encoding UTF8 | ConvertFrom-Json } |
    Where-Object { $_.verdict -eq "PASS" } |
    Sort-Object { [DateTime]$_.audited_at } -Descending |
    Select-Object -First 1

$schemaFingerprint = Get-SchemaFingerprintV1 -ProjectRoot $projectRoot
if ($latest -and $latest.kb_tree_hash -eq $kbHash -and
    $latest.wiki_tree_hash -eq $wikiHash -and
    $latest.schema_fingerprint -eq $schemaFingerprint) {
    Write-Host "kb/wiki gate: PASS (receipt: $($latest.audited_at))"
} else {
    Write-Host "kb/wiki gate: NEED AUDIT (hash mismatch)"
    $changes = Compare-FileManifestV1 -PreviousManifest $latest.file_manifest -CurrentManifest ([PSCustomObject]$currentManifest)
    $changes | ConvertTo-Json -Depth 4
}
```

- 输出 `PASS` → 跳过，直接进入下一个 gate
- 输出 `NEED AUDIT` → **立即执行 Step 2，不经过任何二次筛选**

> Tree hash 是唯一判定依据。hash 不匹配 = 内容已变更 = 需要审计。不引入 `git diff` 作为中间层——它无法区分"本次 session 已 commit 的修改"和"上次 session 遗留的 dirty 文件"，会同时产生假阳性（dirty 文件来自历史 session）和假阴性（改动已 commit 所以 diff 为空）。

#### 1b. vector gate

```powershell
$projectRoot = "<explicit workspace>"
Set-Location -LiteralPath $projectRoot
. (Join-Path $env:CLAUDE_PLUGIN_ROOT "audit\lib\TreeHash.ps1")

$vHash = Get-TreeHashV1 -ScanScope @("vector_db/**/*") -ExcludedPaths @("vector_db/.tmp/**") -ProjectRoot $projectRoot
$currentManifest = Get-FileManifestV1 -ScanScope @("vector_db/**/*") -ExcludedPaths @("vector_db/.tmp/**") -ProjectRoot $projectRoot

Write-Host "current vector_hash: $vHash"

$receiptDir = "kb\.audit\receipts"
$latest = Get-ChildItem $receiptDir -Filter "*vector*.json" -File -ErrorAction SilentlyContinue |
    ForEach-Object { Get-Content $_.FullName -Raw -Encoding UTF8 | ConvertFrom-Json } |
    Where-Object { $_.status -eq "PASS" } |
    Sort-Object { [DateTime]$_.timestamp } -Descending |
    Select-Object -First 1

$gateHash = (Get-FileHash -LiteralPath (
    Join-Path $projectRoot "schemas\generated\vector_gate_queries.yaml"
) -Algorithm SHA256).Hash.ToLower()
if ($latest -and $latest.vector_db_tree_hash -eq $vHash -and
    $latest.schema_fingerprint -eq $schemaFingerprint -and
    $latest.vector_gate_hash -eq $gateHash) {
    Write-Host "vector gate: PASS (receipt: $($latest.timestamp))"
} else {
    Write-Host "vector gate: NEED AUDIT (hash mismatch)"
    $changes = Compare-FileManifestV1 -PreviousManifest $latest.file_manifest -CurrentManifest ([PSCustomObject]$currentManifest)
    $changes | ConvertTo-Json -Depth 4
}
```

- 输出 `PASS` → 跳过，直接进入下一个 gate
- 输出 `NEED AUDIT` → **立即执行 Step 3，不经过 `git diff` 二次筛选**（理由同上: tree hash 为唯一判定依据）

#### 1c. computer_kb gate

```powershell
$projectRoot = "<explicit workspace>"
Set-Location -LiteralPath $projectRoot
. (Join-Path $env:CLAUDE_PLUGIN_ROOT "audit\lib\TreeHash.ps1")

$ckbHash = Get-TreeHashV1 -ScanScope @("computer_kb/**/*.md") -ExcludedPaths @("computer_kb/REVIEWER_LOG.md", "computer_kb\.audit\**", "computer_kb/INDEX.md", "computer_kb/REVIEWER.md") -ProjectRoot $projectRoot
$currentManifest = Get-FileManifestV1 -ScanScope @("computer_kb/**/*.md") -ExcludedPaths @("computer_kb/REVIEWER_LOG.md", "computer_kb\.audit\**", "computer_kb/INDEX.md", "computer_kb/SCHEMA.md", "computer_kb/REVIEWER.md") -ProjectRoot $projectRoot

Write-Host "current computer_kb_hash: $ckbHash"

$receiptDir = "computer_kb\.audit\receipts"
$latest = Get-ChildItem $receiptDir -Filter "*.json" -File -ErrorAction SilentlyContinue |
    ForEach-Object { Get-Content $_.FullName -Raw -Encoding UTF8 | ConvertFrom-Json } |
    Where-Object { $_.verdict -eq "PASS" } |
    Sort-Object { [DateTime]$_.audited_at } -Descending |
    Select-Object -First 1

if ($latest -and $latest.computer_kb_tree_hash -eq $ckbHash) {
    Write-Host "computer_kb gate: PASS (receipt: $($latest.audited_at))"
} else {
    Write-Host "computer_kb gate: NEED AUDIT (hash mismatch)"
    $changes = Compare-FileManifestV1 -PreviousManifest $latest.file_manifest -CurrentManifest ([PSCustomObject]$currentManifest)
    $changes | ConvertTo-Json -Depth 4
}
```

- 输出 `PASS` → 跳过
- 输出 `NEED AUDIT` → **立即执行 Step 4**（理由同上: tree hash 为唯一判定依据）

### Step 2: kb/wiki gate 审计（仅在 NEED AUDIT 时）

调用 `post-kb-audit` skill：
1. 收集 facts（modified files, paper IDs, task type）
2. 构建中性 prompt（按模板，不加预测）
3. 派发 `kb-independent-reviewer` agent (sonnet)
4. 若 PASS → 保存报告 → 计算 SHA256 → 运行 `New-AuditReceipt.ps1` → 写入 `kb/REVIEWER_LOG.md`
5. 若 FAIL → 修复 → 重新审计（最多 3 轮）
6. **禁止自行判定 PASS**，必须等 reviewer 返回
7. 三轮仍失败时仍为 BLOCKING；只有逐项记录技术原因、已尝试修复、
   剩余风险、对应文件和证据，写入 reviewer log，并获得用户明确确认后，
   才能标为 NON-BLOCKING。旧 receipt 无 manifest 时必须报告
   `baseline_manifest_unavailable` 并完整审计。

### Step 3: vector gate 审计（仅在 NEED AUDIT 时）

**3a. Layer 1: sync 审计**

```powershell
$projectRoot = "<explicit workspace>"
$rsk = Join-Path $env:CLAUDE_PLUGIN_ROOT "bin\rsk.cmd"
& $rsk --workspace $projectRoot audit-sync 2>&1 |
    Out-File -Encoding utf8 (
        Join-Path $projectRoot "tmp\vector_audit_result.json"
    )
```

Read `tmp/vector_audit_result.json`。若 status != PASS，先修复再重新运行 `rsk sync`。

**3b. Layer 2 + 2b: 检索质量 + chain claim 审计**

调用 `post-vector-audit` skill：
1. 派发 `vector-retrieval-auditor` agent (sonnet)
2. auditor 会自动检查常驻服务、运行活动 gate 中的全部 test queries +
   chain_test_queries、评估 fidelity/recall/chain claim 覆盖
3. 若 PASS → 保存报告 → 计算 SHA256 → 运行 `New-VectorAuditReceipt.ps1` → 写入 `records/vector_audit_log.jsonl`
4. 若 FAIL → 修复 → 重新同步 → 重新审计（最多 3 轮）
5. 三轮仍失败的 NON-BLOCKING 处置适用与 Step 2 相同的全部条件。

### Step 4: computer_kb gate 审计（仅在 NEED AUDIT 时）

类似 kb/wiki gate，但用 `computer-kb-independent-reviewer` agent 和
`${CLAUDE_PLUGIN_ROOT}/audit/scripts/New-ComputerKbAuditReceipt.ps1`，并显式传入
workspace 的 `-ProjectRoot`。审计维度包括 wiki 链接完整性检查
（`check_wiki_links.py`）。

### Step 5: 汇报结果

向用户汇报所有 gate 的状态：

```
审计完成：
- kb/wiki gate: PASS (hash 匹配, receipt: 2026-06-12T15:56:44)
- vector gate: NEED AUDIT → 审计后 PASS (receipt: xxx)
- computer_kb gate: PASS (hash 匹配, receipt: 2026-06-11T16:03:01)
```

## 核心原则

- **不依赖 hook**：所有 gate 状态通过直接 tree hash 比对判断
- **常驻服务必须先启动**：vector gate Layer 2 依赖 `rsk search`（常驻查询服务）
- **编码问题**：PowerShell 捕获 Python 输出时，用 `2>&1 | Out-File -Encoding utf8` 写文件，然后 Read 文件
- **receipt 独立**：三个 gate 的 PASS receipt 不互相替代
- **修复循环**：FAIL → 修复 → 重新 spawn reviewer，不得自行判定 PASS
- **manifest 解释变化**：输出 added/modified/deleted；旧 receipt 缺 manifest
  时只输出 `baseline_manifest_unavailable` 并执行完整审计，不伪造 diff
