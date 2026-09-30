# Getting Started with ResearchKeeper

## Prerequisites

- Python 3.10+
- Git
- Zotero 7 (optional for Zotero bridge)
- 4GB+ disk space for bge-m3 model

## Installation

```bash
git clone https://github.com/<user>/ResearchKeeper
cd ResearchKeeper
pip install -e ".[dev]"
```

## Quick Start

### 1. Initialize

```bash
rsk init --interactive
```

Follow the prompts. When asked about your research area, describe it in 2-3 sentences.
Then ask your AI assistant: "Help me configure rsk schemas"

### 2. Import from Zotero

```bash
rsk import --from-zotero --db "path/to/zotero.sqlite"
```

### 3. Parse PDFs

```bash
rsk parse --from-zotero outputs/zotero_export.json
```

### 4. AI deep-read and ingest

Ask your AI assistant to read a paper using the `workflow/paper-reading/READING.md` protocol.
The AI will write schema records to `kb/*.md`.

### 5. Sync to vector DB

```bash
rsk sync
```

### 6. Search

```bash
rsk search "your research question" --claims --top 5
```

### 7. Audit quality

Ask your AI assistant: `/audit-all`

## Customizing for Your Field

See [Customization Guide](customization.md).

## Architecture

See [Architecture Overview](architecture.md).
