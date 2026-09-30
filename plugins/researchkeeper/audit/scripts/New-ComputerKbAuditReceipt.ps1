param(
    [ValidateSet("PASS", "FAIL")]
    [string]$Verdict = "PASS",

    [string]$ReviewerReportDigest = "",

    [switch]$AllowMissingReviewerDigest,

    [Parameter(Mandatory = $true)]
    [string]$ProjectRoot
)

$ErrorActionPreference = "Stop"

. (Join-Path (Split-Path -Parent $PSScriptRoot) "lib\TreeHash.ps1")

if (-not $ReviewerReportDigest -and -not $AllowMissingReviewerDigest) {
    throw "ReviewerReportDigest is required. Save or hash the reviewer report, then rerun with -ReviewerReportDigest <sha256>. Use -AllowMissingReviewerDigest only for explicit legacy recovery."
}

$projectRoot = [System.IO.Path]::GetFullPath($ProjectRoot)
$computerKbDir = Join-Path $projectRoot "computer_kb"
$receiptDir = Join-Path $computerKbDir ".audit\receipts"
$normProjectRoot = $projectRoot.Replace('\', '/').TrimEnd('/')

if (-not (Test-Path -LiteralPath $computerKbDir)) {
    throw "computer_kb directory does not exist; cannot generate audit receipt."
}



$computerKbHash = Get-TreeHashV1 `
    -ScanScope @("computer_kb/**/*.md") `
    -ExcludedPaths @("computer_kb/REVIEWER_LOG.md", "computer_kb\.audit\**", "computer_kb/INDEX.md", "computer_kb/SCHEMA.md", "computer_kb/REVIEWER.md") `
    -ProjectRoot $projectRoot
$fileManifest = Get-FileManifestV1 `
    -ScanScope @("computer_kb/**/*.md") `
    -ExcludedPaths @(
        "computer_kb/REVIEWER_LOG.md",
        "computer_kb\.audit\**",
        "computer_kb/INDEX.md",
        "computer_kb/SCHEMA.md",
        "computer_kb/REVIEWER.md"
    ) `
    -ProjectRoot $projectRoot

$auditedFiles = @($fileManifest.Keys)

$receipt = @{
    schema_version              = "computer_kb_audit_receipt_v1"
    project_root                = $normProjectRoot
    security_mode               = "workflow_integrity"
    reviewer                    = "computer-kb-independent-reviewer"
    verdict                     = $Verdict
    audited_at                  = (Get-Date -Format "yyyy-MM-ddTHH:mm:sszzz")
    expires_at                  = $null
    scan_scope                  = @("computer_kb/**/*.md")
    excluded_paths              = @("computer_kb/REVIEWER_LOG.md", "computer_kb\.audit\**")
    tree_hash_algorithm         = "tree_hash_v1_path_sorted_sha256"
    computer_kb_tree_hash       = $computerKbHash
    file_manifest               = $fileManifest
    audited_files               = ($auditedFiles | Sort-Object)
    reviewer_report_digest      = if ($ReviewerReportDigest) { $ReviewerReportDigest } else { "" }
    reviewer_report_digest_note = if ($ReviewerReportDigest) { "required workflow-integrity reviewer report hash" } else { "missing digest allowed by explicit legacy override" }
    hook_version                = "computer_kb_review_gate_v2"
    receipt_generator           = "New-ComputerKbAuditReceipt.ps1"
    created_by                  = "main_ai"
}

if (-not (Test-Path -LiteralPath $receiptDir)) {
    New-Item -ItemType Directory -Path $receiptDir -Force | Out-Null
}

$timestamp = Get-Date -Format "yyyyMMdd-HHmmss"
$filename = "receipt_${timestamp}_$($Verdict.ToLower()).json"
$filePath = Join-Path $receiptDir $filename

$receipt | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath $filePath -Encoding UTF8

Write-Output "Computer KB receipt generated: $filePath"
Write-Output "  computer_kb_tree_hash: $computerKbHash"
Write-Output "  verdict:               $Verdict"
Write-Output "  mode:                  workflow_integrity"
Write-Output "  audited_files:         $($auditedFiles.Count) files"
