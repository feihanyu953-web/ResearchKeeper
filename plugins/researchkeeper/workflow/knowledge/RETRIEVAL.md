# Knowledge Retrieval Protocol

## Two-Step Retrieval

### Step 1: Vector search → locate record_id (+ full paper profile)

```powershell
rsk search "your research question" --claims --top 5 --expand
```

Output shows `record_id`, `paper_id`, `module`, `source_file` for each result.

`--expand` additionally returns the **complete paper profile** for every hit
paper. Claims are grouped in the active concrete-module order from
`schemas/generated/modules.yaml`; unknown legacy modules are retained after
the active modules instead of being discarded.

### Step 2: Read kb file → extract full schema row

Open the indicated `kb/<module>.md` file, search for the `record_id`, and extract the complete 13-field schema row.

### Fallback

If top-5 claims don't match your question:
1. State "向量检索未命中相关记录" (no vector match)
2. Use Grep to search kb files directly: `Grep "keyword" kb/*.md`

### JSON output

```powershell
rsk search "query" --claims --top 5 --expand --json
```

The JSON contains an `expanded` field: `{paper_id: {module: [claim_text, ...]}}`.

## Two-Layer Architecture

| Collection | File | Use |
|------------|------|-----|
| `kb_claims` | `vector_db/claims_embeddings.npy` + `claims_meta.json` | Default — precise claim-level search. Includes `chain-<paper_id>` composite claims that concatenate each paper's cross-module logic chain |
| `kb_papers` | `vector_db/papers_embeddings.npy` + `papers_meta.json` | Fallback — full-text chunk search |
