@echo off
setlocal EnableExtensions DisableDelayedExpansion

REM -- Self-locate plugin root from this script's own location: <plugin>\bin\rsk.cmd -> <plugin>
for %%I in ("%~dp0..") do set "RSK_PLUGIN_ROOT=%%~fI"

REM -- Fall back to defaults when the host does not inject these variables
if not defined CLAUDE_PLUGIN_ROOT set "CLAUDE_PLUGIN_ROOT=%RSK_PLUGIN_ROOT%"
if not defined CLAUDE_PLUGIN_DATA (
    if exist "%USERPROFILE%\.claude\plugins\data\researchkeeper-researchkeeper-local\venvs\active.json" (
        set "CLAUDE_PLUGIN_DATA=%USERPROFILE%\.claude\plugins\data\researchkeeper-researchkeeper-local"
    ) else if exist "%USERPROFILE%\.zcode\cli\plugins\data\researchkeeper@researchkeeper-local\venvs\active.json" (
        set "CLAUDE_PLUGIN_DATA=%USERPROFILE%\.zcode\cli\plugins\data\researchkeeper@researchkeeper-local"
    ) else (
        set "CLAUDE_PLUGIN_DATA=%USERPROFILE%\.claude\plugins\data\researchkeeper-researchkeeper-local"
    )
)

set "RSK_ACTIVE_FILE=%CLAUDE_PLUGIN_DATA%\venvs\active.json"
if not exist "%RSK_ACTIVE_FILE%" (
    >&2 echo ResearchKeeper: no active installation found at "%RSK_ACTIVE_FILE%"
    >&2 echo Run /researchkeeper:setup first, or set CLAUDE_PLUGIN_DATA to the plugin data directory.
    exit /b 3
)

REM -- check_hash.ps1 validates lock_hash format and outputs RSK_PYTHON=<path>
set "RSK_VENV_PYTHON="
for /f "tokens=1* delims==" %%A in ('powershell -NoProfile -ExecutionPolicy Bypass -File "%CLAUDE_PLUGIN_ROOT%\bin\check_hash.ps1" -ActiveJson "%RSK_ACTIVE_FILE%" 2^>nul') do if /I "%%A"=="RSK_PYTHON" set "RSK_VENV_PYTHON=%%B"
if "%RSK_VENV_PYTHON%"=="" (>&2 echo ResearchKeeper: active installation is invalid& exit /b 2)

if not exist "%RSK_VENV_PYTHON%" (
    >&2 echo ResearchKeeper: active venv Python is missing: "%RSK_VENV_PYTHON%"
    >&2 echo Run /researchkeeper:setup to rebuild the active installation.
    exit /b 2
)

if defined PYTHONPATH (set "PYTHONPATH=%CLAUDE_PLUGIN_ROOT%;%PYTHONPATH%") else (set "PYTHONPATH=%CLAUDE_PLUGIN_ROOT%")
"%RSK_VENV_PYTHON%" -m rsk.cli %*
set "RSK_EXIT_CODE=%ERRORLEVEL%"
exit /b %RSK_EXIT_CODE%
