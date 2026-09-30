# Architecture

ResearchKeeper has four layers:

1. **AI Agent Orchestration** (`.claude/`) — CLAUDE.md entry routing, reviewer agents, audit skills
2. **Workflow Routing** (`workflow/`) — Reading protocol, ingest pipeline, retrieval, wiki sync
3. **Python Toolchain** (`rsk/`) — Vector engine, PDF parser, Zotero bridge, KB writer, audit
4. **Data & Model Layer** — `kb/*.md` (pipe tables), `vector_db/` (numpy), `models/bge-m3`

See the [design spec](../../docs/superpowers/specs/2026-06-14-researchkeeper-open-source-design.md) for full details.
