# Vector Workflow

本文件说明论文知识库的向量同步与查询流程。它只服务普通检索和入库后的向量刷新，不包含审计机制。

## 标准环境

Use the platform wrapper under `${CLAUDE_PLUGIN_ROOT}/bin/` and pass the
workspace explicitly. The wrapper selects the active Python 3.11 installation
from `${CLAUDE_PLUGIN_DATA}`; do not use an unrelated `rsk` from `PATH`.

```powershell
$workspace = "<explicit workspace>"
$rsk = Join-Path $env:CLAUDE_PLUGIN_ROOT "bin\rsk.cmd"
```

## 常驻查询服务

高频查询前先启动常驻服务，避免每次查询重复加载 bge-m3：

```powershell
& $rsk --workspace $workspace serve
```

服务监听 `http://127.0.0.1:8765`。`rsk/vector/query.py` 会优先连接常驻服务；连接失败时回退到本地加载。

## 两层检索

| 集合 | 文件 | 用途 |
|---|---|---|
| `kb_claims` | `vector_db/claims_embeddings.npy` + `vector_db/claims_meta.json` | 默认入口，按高信号 claim 定位 record_id（含 `chain-<paper_id>` 跨模块复合 claim） |
| `kb_papers` | `vector_db/papers_embeddings.npy` + `vector_db/papers_meta.json` | 兜底入口，按 per-record chunk 检索 |

## 查询

优先使用 claims，并加 `--expand` 拉取命中论文的完整画像（同一 paper_id 的全部模块 claim 按模块分组返回）：

```powershell
& $rsk --workspace $workspace search "<query>" --claims --top 5 --expand
```

兜底使用 papers：

```powershell
& $rsk --workspace $workspace search "<query>" --top 5
```

需要程序解析时使用 JSON（含 `expanded` 字段）：

```powershell
& $rsk --workspace $workspace search "<query>" --claims --top 5 --expand --json
```

## 同步

增量同步：

```powershell
& $rsk --workspace $workspace sync
```

预览变化：

```powershell
& $rsk --workspace $workspace sync --dry-run
```

全量重建：

```powershell
& $rsk --workspace $workspace sync --full
```

默认同步会刷新 `kb_papers`，并自动调用 `rsk/vector/claims.py` 重建 claims 索引（含 chain claims：每篇 ≥2 个非 literature 模块的论文自动生成一条 `chain-<paper_id>` 复合 claim，无需手动维护）。
