# check_hash.ps1 — invoked by rsk.cmd / rsk
# Validates lock_hash (if present in active.json) and extracts python path.
# Outputs "RSK_PYTHON=<path>" on stdout for the caller to capture.
param(
    [Parameter(Mandatory)]
    [string]$ActiveJson
)

$ErrorActionPreference = "Stop"
try {
    $j = Get-Content $ActiveJson -Raw | ConvertFrom-Json
} catch {
    Write-Error "Cannot parse active.json: $_"
    exit 1
}

# Validate lock_hash if present (64 hex chars)
$h = $j.lock_hash
if ($h -and $h -notmatch '^[0-9a-f]{64}$') {
    Write-Error "Invalid lock_hash in active.json"
    exit 1
}

# Emit python path for caller
$py = $j.python
if (-not $py) {
    Write-Error "No python field in active.json"
    exit 1
}
Write-Output "RSK_PYTHON=$py"
exit 0
