#!/usr/bin/env bash
# ResearchKeeper Setup (Linux / macOS)
# Run: bash setup.sh
set -euo pipefail

REQUIRED_PYTHON_MAJOR=3
REQUIRED_PYTHON_MINOR=10

echo "============================================"
echo " ResearchKeeper Setup (Linux / macOS)"
echo "============================================"

# ── Step 1: Detect / install Python ──────────────────────

echo ""
echo "[1/3] Checking Python..."

PYTHON_CMD=""
for cmd in python3 python; do
    if command -v "$cmd" &> /dev/null; then
        ver=$("$cmd" --version 2>&1)
        major=$(echo "$ver" | grep -oP '\d+' | head -1)
        minor=$(echo "$ver" | grep -oP '\d+' | sed -n '2p')
        if [ "$major" -ge "$REQUIRED_PYTHON_MAJOR" ] && [ "$minor" -ge "$REQUIRED_PYTHON_MINOR" ] 2>/dev/null; then
            PYTHON_CMD="$cmd"
            echo "  Found: $ver ($(command -v "$cmd"))"
            break
        fi
    fi
done

if [ -z "$PYTHON_CMD" ]; then
    echo "  Python ${REQUIRED_PYTHON_MAJOR}.${REQUIRED_PYTHON_MINOR}+ not found."

    # Detect OS and suggest package manager
    OS="$(uname -s)"
    case "$OS" in
        Linux)
            if command -v apt &> /dev/null; then
                echo ""
                echo "  Detected apt (Debian/Ubuntu). Install Python?"
                read -rp "  Run 'sudo apt install python3 python3-pip python3-venv'? [Y/n] " choice
                if [ "$choice" = "" ] || [ "$choice" = "y" ] || [ "$choice" = "Y" ]; then
                    sudo apt update && sudo apt install -y python3 python3-pip python3-venv
                    PYTHON_CMD="python3"
                fi
            elif command -v dnf &> /dev/null; then
                echo ""
                echo "  Detected dnf (Fedora/RHEL)."
                read -rp "  Run 'sudo dnf install python3 python3-pip'? [Y/n] " choice
                if [ "$choice" = "" ] || [ "$choice" = "y" ] || [ "$choice" = "Y" ]; then
                    sudo dnf install -y python3 python3-pip
                    PYTHON_CMD="python3"
                fi
            elif command -v pacman &> /dev/null; then
                echo ""
                echo "  Detected pacman (Arch)."
                read -rp "  Run 'sudo pacman -S python python-pip'? [Y/n] " choice
                if [ "$choice" = "" ] || [ "$choice" = "y" ] || [ "$choice" = "Y" ]; then
                    sudo pacman -S --noconfirm python python-pip
                    PYTHON_CMD="python"
                fi
            fi
            ;;
        Darwin)
            if command -v brew &> /dev/null; then
                echo ""
                echo "  Detected Homebrew. Install Python?"
                read -rp "  Run 'brew install python@3.12'? [Y/n] " choice
                if [ "$choice" = "" ] || [ "$choice" = "y" ] || [ "$choice" = "Y" ]; then
                    brew install python@3.12
                    PYTHON_CMD="python3"
                fi
            fi
            ;;
    esac

    if [ -z "$PYTHON_CMD" ]; then
        echo ""
        echo "  Manual install options:"
        echo "    Linux:   sudo apt install python3 python3-pip  (Debian/Ubuntu)"
        echo "             sudo dnf install python3 python3-pip  (Fedora)"
        echo "             sudo pacman -S python python-pip      (Arch)"
        echo "    macOS:   brew install python@3.12"
        echo "    General: https://www.python.org/downloads/"
        echo ""
        echo "  After installing, re-run: bash setup.sh"
        exit 1
    fi
fi

# ── Step 2: Install ResearchKeeper ───────────────────────

echo ""
echo "[2/3] Installing ResearchKeeper..."

"$PYTHON_CMD" -m pip install -e ".[dev]"
echo "  Package installed."

# ── Step 3: Initialize ───────────────────────────────────

echo ""
echo "[3/3] Initializing..."
rsk init --interactive

echo ""
echo "============================================"
echo " Setup complete!"
echo " Next: edit rsk_config.yaml if needed"
echo "       rsk import --from-zotero"
echo "       rsk sync"
echo "============================================"
