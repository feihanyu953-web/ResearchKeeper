param(
    [Parameter(Mandatory=$true, Position=0)]
    [string]$InputFile,
    [Parameter(Position=1)]
    [string]$OutputFile
)

if (-not (Test-Path $InputFile)) {
    Write-Error "File not found: $InputFile"
    exit 1
}

$InputFile = (Resolve-Path $InputFile).Path
$WorkDir = Split-Path $InputFile -Parent
$BaseName = [System.IO.Path]::GetFileNameWithoutExtension($InputFile)

if (-not $OutputFile) {
    $OutputFile = Join-Path $WorkDir "$BaseName.pdf"
} elseif (-not [System.IO.Path]::IsPathRooted($OutputFile)) {
    $OutputFile = Join-Path (Get-Location) $OutputFile
}

$HtmlFile = Join-Path $WorkDir "$BaseName.html"
$CssFile = Join-Path $PSScriptRoot "pdf_style.css"

# -- Resolve the plugin venv Python (mirrors bin/rsk.cmd's active.json lookup)
$ActiveJson = "$env:USERPROFILE\.claude\plugins\data\researchkeeper-researchkeeper-local\venvs\active.json"
if ($env:CLAUDE_PLUGIN_DATA) {
    $ActiveJson = "$env:CLAUDE_PLUGIN_DATA\venvs\active.json"
}
$VenvPython = $null
if (Test-Path $ActiveJson) {
    try {
        $active = Get-Content $ActiveJson -Raw | ConvertFrom-Json
        if ($active.python -and (Test-Path $active.python)) {
            $VenvPython = $active.python
        }
    } catch {
        $VenvPython = $null
    }
}

# -- Resolve pandoc: plugin venv pypandoc first, then system installs
$Pandoc = $null
if ($VenvPython) {
    try {
        $pyPandoc = & $VenvPython -c "import pypandoc; print(pypandoc.get_pandoc_path())" 2>$null
        if ($LASTEXITCODE -eq 0 -and $pyPandoc -and (Test-Path $pyPandoc)) {
            $Pandoc = $pyPandoc
        } elseif (-not $pyPandoc) {
            # venv is active but lacks pypandoc-binary (e.g. older lock):
            # install it into the plugin venv once, never into base.
            Write-Host "Installing pypandoc-binary into the plugin venv..." -ForegroundColor Yellow
            & $VenvPython -m pip install --disable-pip-version-check pypandoc-binary 2>$null
            if ($LASTEXITCODE -eq 0) {
                $pyPandoc = & $VenvPython -c "import pypandoc; print(pypandoc.get_pandoc_path())" 2>$null
                if ($pyPandoc -and (Test-Path $pyPandoc)) {
                    $Pandoc = $pyPandoc
                }
            }
        }
    } catch {
        $Pandoc = $null
    }
}
if (-not $Pandoc) {
    $pandocCmd = Get-Command pandoc -ErrorAction SilentlyContinue
    if ($pandocCmd) {
        $Pandoc = $pandocCmd.Source
    } elseif (Test-Path "$env:LOCALAPPDATA\Pandoc\pandoc.exe") {
        $Pandoc = "$env:LOCALAPPDATA\Pandoc\pandoc.exe"
    } elseif (Test-Path "C:\Program Files\Pandoc\pandoc.exe") {
        $Pandoc = "C:\Program Files\Pandoc\pandoc.exe"
    }
}
if (-not $Pandoc) {
    Write-Error "pandoc not found. Install: winget install --id JohnMacFarlane.Pandoc  (or rerun /researchkeeper:setup to install pypandoc-binary into the plugin venv)"
    exit 1
}

$EdgePath = $null
if (Test-Path "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe") {
    $EdgePath = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
} elseif (Test-Path "C:\Program Files\Microsoft\Edge\Application\msedge.exe") {
    $EdgePath = "C:\Program Files\Microsoft\Edge\Application\msedge.exe"
} else {
    Write-Error "Edge not found"
    exit 1
}

Write-Host "[1/2] MD -> HTML (pandoc)..." -ForegroundColor Cyan

$pandocArgs = @($InputFile, "-f", "markdown", "-t", "html5", "-s", "--metadata", "title=$BaseName", "--embed-resources", "-o", $HtmlFile)
if (Test-Path $CssFile) {
    $pandocArgs += @("--css=$CssFile")
}
& $Pandoc @pandocArgs

if (-not (Test-Path $HtmlFile)) {
    Write-Error "HTML generation failed"
    exit 1
}

Write-Host ("      HTML: " + [Math]::Round((Get-Item $HtmlFile).Length / 1KB, 1) + " KB") -ForegroundColor Gray

Write-Host "[2/2] HTML -> PDF (Edge)..." -ForegroundColor Cyan

$OutDir = Split-Path $OutputFile -Parent
if (-not (Test-Path $OutDir)) {
    New-Item -ItemType Directory -Path $OutDir -Force | Out-Null
}
if (Test-Path $OutputFile) {
    Remove-Item $OutputFile -Force -ErrorAction SilentlyContinue
}

$HtmlUrl = "file:///" + $HtmlFile.Replace('\', '/')

$oldEAP = $ErrorActionPreference
$ErrorActionPreference = "SilentlyContinue"
Start-Process -FilePath $EdgePath -ArgumentList "--headless", "--disable-gpu", "--no-pdf-header-footer", "--print-to-pdf=$OutputFile", $HtmlUrl -Wait -NoNewWindow
$ErrorActionPreference = $oldEAP

Start-Sleep -Seconds 2

Remove-Item $HtmlFile -Force -ErrorAction SilentlyContinue

if (Test-Path $OutputFile) {
    $size = [Math]::Round((Get-Item $OutputFile).Length / 1KB, 1)
    Write-Host "Done: $OutputFile ($size KB)" -ForegroundColor Green
} else {
    Write-Error "PDF generation failed"
    exit 1
}
