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

## sync 后必须重启常驻服务（向量缓存无失效）

服务端在**首次查询**时 `np.load` 向量并永久缓存（`rsk/vector/server.py` 无 mtime 检查、无 reload 端点）。因此重建向量库不会影响已在运行的服务——它会一直提供进程启动那一刻的旧向量。`/health` 返回 ok **只证明进程活着，不证明向量新鲜**。

凡执行过 `rsk sync`（含 `--full`），继续使用常驻服务检索前必须先重启：

```powershell
Get-CimInstance Win32_Process -Filter "Name like '%python%'" |
  Where-Object { $_.CommandLine -like '*rsk.cli*serve*' } |
  ForEach-Object { Stop-Process -Id $_.ProcessId -Force }
& $rsk --workspace $workspace serve
```

刷新验证（取一条本轮新增或文本被修改的 record）：

```powershell
# 真值侧：rsk search 进程内直读磁盘，不经过服务
& $rsk --workspace $workspace search --claims "<该 record 的特征措辞>" --top 1 --json
# 服务侧：
Invoke-RestMethod "http://127.0.0.1:8765/query?q=<同一措辞 URL 转义>&claims=1&top=1"
```

两者文本不一致 → 服务缓存仍陈旧，重新重启并验证。重启是安全的：`rsk search` 不依赖服务，查询永远可回退本地加载。
