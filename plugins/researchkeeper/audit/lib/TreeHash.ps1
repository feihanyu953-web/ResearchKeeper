# TreeHash.ps1 — shared file-manifest and Get-TreeHashV1 implementation
# Dot-sourced by kb_review_gate.ps1, computer_kb_review_gate.ps1,
# New-AuditReceipt.ps1, New-ComputerKbAuditReceipt.ps1, approve_kb_audit.ps1
#
# Keep in sync across all consumers by editing ONLY this file.

function Get-AuditedFileEntriesV1 {
    param(
        [string[]]$ScanScope,
        [string[]]$ExcludedPaths,
        [string]$ProjectRoot
    )

    $allFiles = @()
    $seen = @{}

    foreach ($scope in $ScanScope) {
        $scopeNorm = $scope.Replace('\', '/')
        $parts = $scopeNorm -split '/'
        $rootDir = $parts[0]
        $filePattern = $parts[-1]
        $isRecursive = ($parts -contains '**')
        $targetDir = Join-Path $ProjectRoot $rootDir

        if (-not (Test-Path -LiteralPath $targetDir)) { continue }

        $getArgs = @{
            LiteralPath = $targetDir
            Filter      = $filePattern
            File        = $true
            ErrorAction = [System.Management.Automation.ActionPreference]::SilentlyContinue
        }
        if ($isRecursive) { $getArgs['Recurse'] = $true }

        Get-ChildItem @getArgs | ForEach-Object {
            $absPath = $_.FullName
            if (-not $seen.ContainsKey($absPath)) {
                $seen[$absPath] = $true
                $allFiles += $_
            }
        }
    }

    $resolvedRoot = [System.IO.Path]::GetFullPath($ProjectRoot)
    $normRoot = $resolvedRoot.Replace('\', '/').TrimEnd('/') + '/'

    $included = @()
    foreach ($f in $allFiles) {
        $relPath = $f.FullName.Replace('\', '/')
        if ($relPath.StartsWith($normRoot, [StringComparison]::OrdinalIgnoreCase)) {
            $relPath = $relPath.Substring($normRoot.Length)
        }
        $relPath = $relPath.Replace('\', '/')

        $excluded = $false
        foreach ($ex in $ExcludedPaths) {
            $exNorm = $ex.Replace('\', '/')
            if ($exNorm.EndsWith('/**')) {
                $prefix = $exNorm.Substring(0, $exNorm.Length - 3)
                if ($relPath.StartsWith($prefix, [StringComparison]::OrdinalIgnoreCase)) {
                    $excluded = $true
                    break
                }
            } elseif ($relPath -eq $exNorm) {
                $excluded = $true
                break
            } elseif ($relPath.StartsWith($exNorm, [StringComparison]::OrdinalIgnoreCase)) {
                $excluded = $true
                break
            }
        }
        if (-not $excluded) {
            $included += @{ Path = $f.FullName; RelPath = $relPath }
        }
    }

    return @($included | Sort-Object { $_.RelPath } -Culture '')
}

function Get-FileManifestV1 {
    param(
        [string[]]$ScanScope,
        [string[]]$ExcludedPaths,
        [string]$ProjectRoot
    )

    $manifest = [ordered]@{}
    $entries = @(
        Get-AuditedFileEntriesV1 `
            -ScanScope $ScanScope `
            -ExcludedPaths $ExcludedPaths `
            -ProjectRoot $ProjectRoot
    )
    foreach ($item in $entries) {
        $bytes = [System.IO.File]::ReadAllBytes($item.Path)
        $sha = [System.Security.Cryptography.SHA256]::Create()
        $fileHash = [BitConverter]::ToString($sha.ComputeHash($bytes)).Replace("-", "").ToLower()
        $manifest[$item.RelPath] = $fileHash
    }
    return $manifest
}

function Compare-FileManifestV1 {
    param(
        $PreviousManifest,
        $CurrentManifest
    )

    if ($null -eq $PreviousManifest) {
        return [ordered]@{
            baseline_manifest_unavailable = $true
            added = @()
            modified = @()
            deleted = @()
        }
    }

    $previous = @{}
    foreach ($property in $PreviousManifest.PSObject.Properties) {
        $previous[$property.Name] = [string]$property.Value
    }
    $current = @{}
    foreach ($property in $CurrentManifest.PSObject.Properties) {
        $current[$property.Name] = [string]$property.Value
    }

    return [ordered]@{
        baseline_manifest_unavailable = $false
        added = @($current.Keys | Where-Object {
            -not $previous.ContainsKey($_)
        } | Sort-Object)
        modified = @($current.Keys | Where-Object {
            $previous.ContainsKey($_) -and $previous[$_] -ne $current[$_]
        } | Sort-Object)
        deleted = @($previous.Keys | Where-Object {
            -not $current.ContainsKey($_)
        } | Sort-Object)
    }
}

function Get-TreeHashV1 {
    param(
        [string[]]$ScanScope,
        [string[]]$ExcludedPaths,
        [string]$ProjectRoot
    )

    $fileManifest = Get-FileManifestV1 `
        -ScanScope $ScanScope `
        -ExcludedPaths $ExcludedPaths `
        -ProjectRoot $ProjectRoot
    $manifestLines = foreach ($entry in $fileManifest.GetEnumerator()) {
        "$($entry.Key)`n$($entry.Value)`n"
    }
    $manifestBytes = [System.Text.Encoding]::UTF8.GetBytes(
        $manifestLines -join ""
    )
    $treeSha = [System.Security.Cryptography.SHA256]::Create()
    return [BitConverter]::ToString($treeSha.ComputeHash($manifestBytes)).Replace("-", "").ToLower()
}

function Get-SchemaFingerprintV1 {
    param(
        [Parameter(Mandatory = $true)]
        [string]$ProjectRoot
    )

    $files = [ordered]@{
        modules = "schemas/generated/modules.yaml"
        vector_gate_queries = "schemas/generated/vector_gate_queries.yaml"
        index = "kb/INDEX.md"
        schema = "kb/SCHEMA.md"
        reviewer = "kb/REVIEWER.md"
    }
    $sha = [System.Security.Cryptography.SHA256]::Create()
    foreach ($entry in $files.GetEnumerator()) {
        $path = Join-Path $ProjectRoot $entry.Value
        if (-not (Test-Path -LiteralPath $path -PathType Leaf)) {
            throw "Missing schema fingerprint input: $($entry.Value)"
        }
        $label = [System.Text.Encoding]::UTF8.GetBytes($entry.Key)
        $zero = [byte[]]@(0)
        $bytes = [System.IO.File]::ReadAllBytes($path)
        [void]$sha.TransformBlock($label, 0, $label.Length, $label, 0)
        [void]$sha.TransformBlock($zero, 0, 1, $zero, 0)
        [void]$sha.TransformBlock($bytes, 0, $bytes.Length, $bytes, 0)
        [void]$sha.TransformBlock($zero, 0, 1, $zero, 0)
    }
    [void]$sha.TransformFinalBlock([byte[]]@(), 0, 0)
    return [BitConverter]::ToString($sha.Hash).Replace("-", "").ToLower()
}
