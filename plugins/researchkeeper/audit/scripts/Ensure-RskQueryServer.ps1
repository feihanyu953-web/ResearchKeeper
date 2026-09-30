[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [ValidateNotNullOrEmpty()]
    [string]$RskCommand,

    [Parameter(Mandatory = $true)]
    [ValidateNotNullOrEmpty()]
    [string]$Workspace,

    [Parameter(Mandatory = $true)]
    [ValidateNotNullOrEmpty()]
    [string]$LogDirectory,

    [ValidateNotNullOrEmpty()]
    [string]$HealthUri = "http://127.0.0.1:8765/health",

    [ValidateRange(1, 3600)]
    [int]$TimeoutSeconds = 180,

    [ValidateRange(50, 60000)]
    [int]$PollIntervalMilliseconds = 1000,

    [scriptblock]$HealthProbe = {
        param($Uri)
        try {
            Invoke-RestMethod `
                -Uri $Uri `
                -TimeoutSec 3 `
                -ErrorAction Stop | Out-Null
            $true
        } catch {
            $false
        }
    },

    [scriptblock]$ProcessStarter = {
        param($Command, $Arguments, $StdoutPath, $StderrPath)
        Start-Process `
            -FilePath $Command `
            -ArgumentList $Arguments `
            -WindowStyle Hidden `
            -RedirectStandardOutput $StdoutPath `
            -RedirectStandardError $StderrPath `
            -PassThru
    },

    [scriptblock]$ProcessStateProbe = {
        param($Process)
        try {
            $Process.Refresh()
        } catch {
            # The properties below remain the authoritative state.
        }
        [pscustomobject]@{
            HasExited = [bool]$Process.HasExited
            ExitCode = if ($Process.HasExited) {
                $Process.ExitCode
            } else {
                $null
            }
        }
    },

    [scriptblock]$Sleeper = {
        param($Milliseconds)
        Start-Sleep -Milliseconds $Milliseconds
    },

    [scriptblock]$Clock = {
        [DateTimeOffset]::UtcNow
    }
)

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$resolvedWorkspace = (Resolve-Path -LiteralPath $Workspace).Path
$pollCount = 1
if ([bool](& $HealthProbe $HealthUri)) {
    [pscustomobject]@{
        status = "healthy"
        started = $false
        pid = $null
        wait_ms = 0
        poll_count = $pollCount
        health_uri = $HealthUri
        stdout = $null
        stderr = $null
    }
    return
}

New-Item -ItemType Directory -Path $LogDirectory -Force | Out-Null
$logRoot = (Resolve-Path -LiteralPath $LogDirectory).Path
$runId = "{0}-{1}" -f (
    [DateTimeOffset]::UtcNow.ToString("yyyyMMddTHHmmss")
), ([Guid]::NewGuid().ToString("N").Substring(0, 8))
$stdoutPath = Join-Path $logRoot "query-server-$runId.stdout.log"
$stderrPath = Join-Path $logRoot "query-server-$runId.stderr.log"
$arguments = @("--workspace", $resolvedWorkspace, "serve")

try {
    $process = & $ProcessStarter `
        $RskCommand `
        $arguments `
        $stdoutPath `
        $stderrPath
} catch {
    throw (
        "query server failed to start: {0}; stdout={1}; stderr={2}" -f `
        $_.Exception.Message, $stdoutPath, $stderrPath
    )
}
if ($null -eq $process -or $null -eq $process.Id) {
    throw (
        "query server starter returned no process; stdout={0}; stderr={1}" -f `
        $stdoutPath, $stderrPath
    )
}

$startedAt = [DateTimeOffset](& $Clock)
while ($true) {
    $pollCount += 1
    if ([bool](& $HealthProbe $HealthUri)) {
        $healthyAt = [DateTimeOffset](& $Clock)
        [pscustomobject]@{
            status = "healthy"
            started = $true
            pid = [int]$process.Id
            wait_ms = [int][Math]::Round(
                ($healthyAt - $startedAt).TotalMilliseconds
            )
            poll_count = $pollCount
            health_uri = $HealthUri
            stdout = $stdoutPath
            stderr = $stderrPath
        }
        return
    }

    $state = & $ProcessStateProbe $process
    if ([bool]$state.HasExited) {
        throw (
            "query server exited before becoming healthy: " +
            "exit_code={0}; stdout={1}; stderr={2}" -f `
            $state.ExitCode, $stdoutPath, $stderrPath
        )
    }

    $now = [DateTimeOffset](& $Clock)
    $elapsed = ($now - $startedAt).TotalSeconds
    if ($elapsed -ge $TimeoutSeconds) {
        throw (
            "query server health check timed out after {0}s: " +
            "pid={1}; stdout={2}; stderr={3}" -f `
            $TimeoutSeconds, $process.Id, $stdoutPath, $stderrPath
        )
    }
    & $Sleeper $PollIntervalMilliseconds
}
