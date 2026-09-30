<#
.SYNOPSIS
    鐢熸垚浣庡畨鍏ㄦā寮?(workflow-integrity) audit receipt銆?    鐢变富 AI 鍦?spawn reviewer 骞跺畬鎴愪慨澶嶅悗璋冪敤銆?
.PARAMETER Verdict
    PASS 鎴?FAIL锛岄粯璁?PASS銆?
.PARAMETER ReviewerReportDigest
    鍙€夈€俽eviewer 瀹¤鎶ュ憡鐨?SHA256 digest锛坕nformational only in workflow-integrity mode锛夈€?
.EXAMPLE
    powershell "${CLAUDE_PLUGIN_ROOT}/audit/scripts/New-AuditReceipt.ps1" -ProjectRoot "<explicit workspace>" -ReviewerReportDigest "abc123..."
#>

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

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = [System.IO.Path]::GetFullPath($ProjectRoot)
$kbDir = Join-Path $projectRoot "kb"
$wikiDir = Join-Path $projectRoot "wiki"
$receiptDir = Join-Path $kbDir ".audit\receipts"
$normProjectRoot = $projectRoot.Replace('\', '/').TrimEnd('/')



# ============================================================
# Compute hashes
# ============================================================
$kbHash = Get-TreeHashV1 `
    -ScanScope @("kb/**/*.md") `
    -ExcludedPaths @("kb/REVIEWER_LOG.md", "kb/.audit/**", "kb/INDEX.md", "kb/SCHEMA.md", "kb/REVIEWER.md") `
    -ProjectRoot $projectRoot

$wikiHash = Get-TreeHashV1 `
    -ScanScope @("wiki/**/*.md") `
    -ExcludedPaths @("wiki/index.md", "wiki/log.md") `
    -ProjectRoot $projectRoot
$fileManifest = Get-FileManifestV1 `
    -ScanScope @("kb/**/*.md", "wiki/**/*.md") `
    -ExcludedPaths @(
        "kb/REVIEWER_LOG.md",
        "kb/.audit/**",
        "kb/INDEX.md",
        "kb/SCHEMA.md",
        "kb/REVIEWER.md",
        "wiki/index.md",
        "wiki/log.md"
    ) `
    -ProjectRoot $projectRoot
$schemaFingerprint = Get-SchemaFingerprintV1 -ProjectRoot $projectRoot

# ============================================================
# Collect audited file list
# ============================================================
$auditedFiles = @($fileManifest.Keys)

# ============================================================
# Build receipt
# ============================================================
$receipt = @{
    schema_version           = "kb_audit_receipt_v1"
    project_root             = $normProjectRoot
    security_mode            = "workflow_integrity"
    reviewer                 = "kb-independent-reviewer"
    verdict                  = $Verdict
    audited_at               = (Get-Date -Format "yyyy-MM-ddTHH:mm:sszzz")
    expires_at               = $null
    scan_scope               = @("kb/**/*.md", "wiki/**/*.md")
    excluded_paths           = @("kb/REVIEWER_LOG.md", "kb/.audit/**")
    tree_hash_algorithm      = "tree_hash_v1_path_sorted_sha256"
    kb_tree_hash             = $kbHash
    wiki_tree_hash           = $wikiHash
    file_manifest            = $fileManifest
    schema_fingerprint       = $schemaFingerprint
    audited_files            = ($auditedFiles | Sort-Object)
    reviewer_report_digest   = if ($ReviewerReportDigest) { $ReviewerReportDigest } else { "" }
    reviewer_report_digest_note = if ($ReviewerReportDigest) { "required workflow-integrity reviewer report hash" } else { "missing digest allowed by explicit legacy override" }
    hook_version             = "kb_review_gate_v3"
    receipt_generator        = "New-AuditReceipt.ps1"
    created_by               = "main_ai"
}

# ============================================================
# Write receipt
# ============================================================
if (-not (Test-Path -LiteralPath $receiptDir)) {
    New-Item -ItemType Directory -Path $receiptDir -Force | Out-Null
}

$timestamp = Get-Date -Format "yyyyMMdd-HHmmss"
$filename = "receipt_${timestamp}_$($Verdict.ToLower()).json"
$filePath = Join-Path $receiptDir $filename

$receipt | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath $filePath -Encoding UTF8

Write-Output "Receipt generated: $filePath"
Write-Output "  kb_tree_hash:  $kbHash"
Write-Output "  wiki_tree_hash: $wikiHash"
Write-Output "  verdict:       $Verdict"
Write-Output "  mode:          workflow_integrity"
Write-Output "  audited_files: $($auditedFiles.Count) files"
