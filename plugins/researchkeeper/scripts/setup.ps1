# ResearchKeeper Windows Setup
# Run: powershell -ExecutionPolicy Bypass -File setup.ps1

Write-Host @"
============================================
 ResearchKeeper Setup (Windows)
============================================
"@ -ForegroundColor Cyan

$REQUIRED_PYTHON_MAJOR = 3
$REQUIRED_PYTHON_MINOR = 11

# ── Step 1: Detect / install Python 3.11.x ───────────────

Write-Host "`n[1/3] Checking Python 3.11..." -ForegroundColor Yellow

function Get-PythonVersion([string]$path) {
    try {
        $v = & $path -c "import sys; print(f'{sys.version_info[0]}.{sys.version_info[1]}')" 2>$null
        if ($LASTEXITCODE -eq 0 -and $v -match '^\d+\.\d+$') { return $v }
    } catch {}
    return $null
}

$candidates = @()
try { $c = Get-Command python -ErrorAction Stop; if ($c) { $candidates += $c.Source } } catch {}
try { $c = Get-Command python3 -ErrorAction Stop; if ($c) { $candidates += $c.Source } } catch {}
try { $c = Get-Command py -ErrorAction Stop; if ($c) { $candidates += $c.Source } } catch {}
# Anaconda/Miniconda base or 3.11 envs found via conda
$condaCmd = $null
try { $condaCmd = Get-Command conda -ErrorAction Stop } catch {}

$pythonCmd = $null
foreach ($candidate in ($candidates | Select-Object -Unique)) {
    $ver = Get-PythonVersion $candidate
    if ($ver -eq "$REQUIRED_PYTHON_MAJOR.$REQUIRED_PYTHON_MINOR") {
        $pythonCmd = $candidate
        Write-Host "  Found Python 3.11: $candidate" -ForegroundColor Green
        break
    } elseif ($ver) {
        Write-Host "  Skipping $candidate (Python $ver — 3.11.x required)" -ForegroundColor DarkGray
    }
}

# Prefer `py -3.11` explicitly when the launcher is available
if (-not $pythonCmd) {
    $pyLauncher = $null
    try { $pyLauncher = Get-Command py -ErrorAction Stop } catch {}
    if ($pyLauncher) {
        $v = & $pyLauncher.Source -3.11 -c "import sys; print(f'{sys.version_info[0]}.{sys.version_info[1]}')" 2>$null
        if ($LASTEXITCODE -eq 0 -and $v -eq "$REQUIRED_PYTHON_MAJOR.$REQUIRED_PYTHON_MINOR") {
            $pythonCmd = $pyLauncher.Source
            Write-Host "  Found Python 3.11 via py launcher" -ForegroundColor Green
        }
    }
}

if ($pythonCmd) {
    if ($condaCmd -and $pythonCmd -match 'conda|anaconda') {
        Write-Host "`n  Note: you are using a conda Python. The Claude Code plugin mode installs into its own" -ForegroundColor DarkYellow
        Write-Host "  isolated venv and will NOT touch your conda base environment. This standalone setup" -ForegroundColor DarkYellow
        Write-Host "  installs into the current environment, so consider 'conda create -n rsk311 python=3.11' first." -ForegroundColor DarkYellow
    }
} else {
    Write-Host "  Python 3.11.x (>=3.11,<3.12) not found." -ForegroundColor Red
    if ($condaCmd) {
        Write-Host "`n  Anaconda/Miniconda detected. Create a 3.11 environment with:" -ForegroundColor Yellow
        Write-Host "    conda create -n rsk311 python=3.11"
        Write-Host "    conda activate rsk311"
        Write-Host "  then re-run this script (or use the Claude Code plugin, which is fully isolated)." -ForegroundColor Yellow
    }

    # Check if winget is available for auto-install
    $winget = Get-Command winget -ErrorAction SilentlyContinue
    if ($winget) {
        Write-Host "`n  winget detected — can auto-install Python 3.11." -ForegroundColor Yellow
        $choice = Read-Host "  Install Python 3.11 now? [Y/n]"
        if ($choice -eq '' -or $choice -eq 'y' -or $choice -eq 'Y') {
            Write-Host "  Installing Python 3.11 via winget..." -ForegroundColor Cyan
            winget install Python.Python.3.11 --accept-package-agreements --accept-source-agreements
            if ($LASTEXITCODE -ne 0) {
                Write-Error "winget install failed. Please install Python manually:"
                Write-Host "  https://www.python.org/downloads/" -ForegroundColor Yellow
                exit 1
            }
            # Refresh PATH (newly installed Python may not be in current session)
            $env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" +
                         [System.Environment]::GetEnvironmentVariable("Path","User")
            Write-Host "  Python installed. Please re-run setup.ps1 in a new terminal." -ForegroundColor Green
            exit 0
        }
    }

    Write-Host "`n  Manual install options:" -ForegroundColor Yellow
    Write-Host "    1. Microsoft Store: search 'Python 3.11'"
    Write-Host "    2. Official installer: https://www.python.org/downloads/"
    Write-Host "    3. winget: winget install Python.Python.3.11"
    Write-Host "    4. Anaconda: conda create -n rsk311 python=3.11"
    Write-Host "`n  After installing, re-run this script.`n"
    exit 1
}

# ── Step 2: Install ResearchKeeper ───────────────────────

Write-Host "`n[2/3] Installing ResearchKeeper..." -ForegroundColor Yellow

$py = $pythonCmd
& $py -m pip install -e ".[dev]" 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Error "pip install failed. Check your Python environment."
    exit 1
}
Write-Host "  Package installed." -ForegroundColor Green

# ── Step 3: Initialize ───────────────────────────────────

Write-Host "`n[3/3] Initializing..." -ForegroundColor Yellow
rsk init --interactive

Write-Host @"

============================================
 Setup complete!
 Next: edit rsk_config.yaml if needed
       rsk import --from-zotero
       rsk sync
============================================
"@ -ForegroundColor Cyan
