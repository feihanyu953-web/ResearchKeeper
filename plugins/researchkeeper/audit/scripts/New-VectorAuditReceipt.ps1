param(
    [string]$Status = "PASS",

    [string]$RetrievalReportDigest = "",

    [switch]$AllowMissingRetrievalDigest,

    [Parameter(Mandatory = $true)]
    [string]$ProjectRoot
)

$projectDir = [System.IO.Path]::GetFullPath($ProjectRoot)

if (-not $RetrievalReportDigest -and -not $AllowMissingRetrievalDigest) {
    throw "RetrievalReportDigest is required. Save or hash the vector retrieval audit report, then rerun with -RetrievalReportDigest <sha256>. Use -AllowMissingRetrievalDigest only for explicit legacy recovery."
}

$libPath = Join-Path (Split-Path -Parent $PSScriptRoot) "lib\TreeHash.ps1"
. $libPath

$receiptDir = Join-Path $projectDir "kb\.audit\receipts"
New-Item -ItemType Directory -Path $receiptDir -Force | Out-Null

$hashFile = Join-Path $projectDir "records\.vector_tree_hash"
$vectorTreeHash = if (Test-Path $hashFile) { (Get-Content $hashFile -Raw).Trim() } else { "unknown" }
$fileManifest = Get-FileManifestV1 `
    -ScanScope @("vector_db/**/*") `
    -ExcludedPaths @("vector_db/.tmp/**") `
    -ProjectRoot $projectDir
$schemaFingerprint = Get-SchemaFingerprintV1 -ProjectRoot $projectDir
$gatePath = Join-Path $projectDir (
    "schemas\generated\vector_gate_queries.yaml"
)
$vectorGateHash = (
    Get-FileHash -LiteralPath $gatePath -Algorithm SHA256
).Hash.ToLower()
$summaryPath = Join-Path $projectDir "vector_db\summary.json"
$syncSummary = if (Test-Path -LiteralPath $summaryPath) {
    Get-Content -LiteralPath $summaryPath -Raw -Encoding UTF8 |
        ConvertFrom-Json
} else {
    $null
}

$ts = Get-Date -Format "yyyyMMddHHmmss"
$receiptFile = Join-Path $receiptDir "vector_audit_receipt_$ts.json"

$receipt = @{
    schema = "vector_audit_receipt_v1"
    timestamp = (Get-Date -Format "yyyy-MM-ddTHH:mm:sszzz")
    status = $Status
    vector_db_tree_hash = $vectorTreeHash
    file_manifest = $fileManifest
    schema_fingerprint = $schemaFingerprint
    vector_gate_hash = $vectorGateHash
    embedding_backend = if ($syncSummary) {
        [string]$syncSummary.embedding_backend
    } else {
        ""
    }
    embedding_fallback_reason = if ($syncSummary) {
        [string]$syncSummary.embedding_fallback_reason
    } else {
        ""
    }
    audit_log_path = "records/vector_audit_log.jsonl"
    retrieval_report_digest = $RetrievalReportDigest
    retrieval_report_digest_note = if ($RetrievalReportDigest) { "required vector retrieval audit report hash" } else { "missing digest allowed by explicit legacy override" }
} | ConvertTo-Json -Depth 8

$receipt | Out-File -FilePath $receiptFile -Encoding utf8
Write-Output "Receipt created: $receiptFile"
