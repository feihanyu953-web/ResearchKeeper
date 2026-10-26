# LitMind 入库与检索

## 标准调用环境

Claude Code plugin 只通过 `${CLAUDE_PLUGIN_ROOT}/bin/rsk`（POSIX）或
`${CLAUDE_PLUGIN_ROOT}\bin\rsk.cmd`（Windows）调用活动安装，并为每条命令
显式传入 workspace。依赖状态位于 `${CLAUDE_PLUGIN_DATA}`；workspace 不得
放在 plugin root 或 plugin data 中。

## 快速导航

| 你要做什么 | 跳转 |
|---|---|
| 查知识：某体系/反应/方法在 kb 中有没有记录 | [§检索流程](#检索流程论文知识问答强制执行) |
| 入库：把新论文导入 kb + 向量 | [§入库流程](#入库流程完整的-zotero--kb--向量链路) |
| 对账：Zotero 中哪些论文未入 kb | `rsk diff` → 输出未入库列表 |

## 入库流程（完整的 Zotero → kb → 向量链路）

所有入库（单篇或批量）走同一管线，差异仅在"AI 精读提取"阶段的执行方式。

**入库前必须参考**：
- `kb/INDEX.md` — 路由规则（什么数据存哪个模块）、入库策略（综述 vs 实验论文）
- `kb/SCHEMA.md` — 数据格式（13 字段 schema_v1）

### 补全 vs 新入库 区分

| 触发词 | 意图 | 操作差异 |
|---|---|---|
| "导入"/"入库" | 新论文入库 | 全流程 |
| "补全"/"补充"/"完善" | 补全已有论文 | 先对比 kb 文件确认缺失范围，只补缺失模块 |

补全流程：
1. 读取 `schemas/generated/modules.yaml` 与已有 coverage，按活动模块确认缺失范围
2. 检查是否已有转换好的文字（tmp/ 目录），有则跳过 PDF 解析
3. 精读缺失模块
4. 写入 kb（rsk sync）
5. 向量同步（rsk sync）
6. 主 AI 入库验收

```
┌─ 文本管道 ───────────────┐   ┌─ AI 精读提取 ──────────┐   ┌─ 写入+同步 ───────────────┐
│ rsk import → rsk parse     │ → │ 单篇: READING.md 主AI  │ → │ rsk sync → rsk sync          │
│ 标准化文本                  │   │ 批量: 子agent并行       │   │ rsk search 可检索             │
└───────────────────────────┘   └──────────────────────┘   └──────────────────────────┘
```

### Step 1: Zotero 导出

```powershell
rsk import --from-zotero
# → outputs/zotero_export.json
```

### Step 2: PDF 文本解析

```powershell
rsk parse --from-zotero outputs/zotero_export.json --output-dir tmp/
```

> 若仅需解析部分论文，先生成过滤版 JSON 再传入 `--from-zotero`。
> rsk parse 产出的是**原始文本段落**（Markdown），不是 schema_v1 记录。


### Step 2.5: SI 表数值一致性校验（推荐，可选）

向 `rsk sync` 写入前，建议运行 SI 表数值交叉校验，捕获 LLM 转录时
将数值错配到错误条件列的常见错误：

```powershell
rsk validate-si --parsed-si tmp/<key>.md --extracted-dir tmp/extracted/ --json
```

- 解析 SI 表中的数值矩阵（逐列 Gtot/ΔGad），与提取的 JSON 记录逐值比对
- 检测 value→condition 错配（如 -1.36 eV 配给中性而非酸性）
- `--json` 输出可程序化分析；exit code 2 = 发现错配
- 仅适用于 SI 包含结构化数值表（Table S2-S4 模式）的论文

### Step 3: AI 精读提取 → 写入 kb

**这是从文本段落提取 schema_v1 记录的关键步骤**，不可跳过。数据提取检查清单见 `kb/SCHEMA.md` 附录。

#### 单篇精读（N=1）

主 AI 亲自精读，按 `workflow/paper-reading/READING.md` 完整 10 板块流程
→ 按活动 concrete modules 提取 schema 记录 → 写入适用模块。

#### 批量入库（N≥2）

**触发**：用户说"批量导入 N 篇论文"（N≥2）。N≥5 时建议先走 `workflow/paper-reading/TRIAGE.md` 快速筛选协议（仅凭 title+abstract 做高/中/低评级，"高"才全文精读、"中"只入 literature 索引、"低"跳过留原因），避免逢文必读的精读开销。

**分片策略**：`agent_count = min(ceil(N / 2), 8)`，每个 agent 处理 1-2 篇论文。

**硬上限**：单轮并行 agent 不超过 **8 个**。Agent 框架在高并发下有进程回收延迟；超过 8 个可能导致部分 agent 完成任务后仍被框架标记为"运行中"，触发 callback hook 阻塞。

**N > 16 时分批**：每批 ≤ 8 个 agent，等前一批全部完成（所有 TaskOutput 返回完整输出）后再启动下一批。分批间主 AI 可以开始做质量门禁检查。

| 论文数 N | agent 数（每轮） | 每 agent 论文数 | 批次 |
|----------|-----------------|----------------|------|
| 2-4 | 2 | 1-2 | 1 轮 |
| 5-8 | 4 | 1-2 | 1 轮 |
| 9-16 | min(ceil(N/2), 8) | 1-2 | 1 轮 |
| 17-32 | 8 | 2-4 | 2 轮（每轮 8 agent） |
| 33+ | 8 | ceil(N / 轮数) | ceil(N / 16) 轮 |

**已知问题**：Claude Code v2.x 框架在高并发 `run_in_background` 场景下，偶尔出现子进程已退出但框架侧状态未清除的情况。症状为 `TaskOutput(task_id, block=true)` 返回 "No task found" 且 `callback` hook 持续报 "Background subagents are still running"。此问题不影响 agent 输出文件（已落盘），但会阻塞会话结束。**严格遵循上表分批可避免此问题。**

如果仍遇到该问题：
```bash
# 1. 确认所有 agent 输出已落盘
ls tmp/extracted/

# 2. 直接 Ctrl+C 中断会话（agent 输出文件不受影响）

# 3. 新开会话，从"主 AI 质量门禁"步骤继续
rsk sync --input-dir tmp/extracted/
```

##### 子 Agent 约束

子 agent 为通用 agent + 标准化 prompt。独立上下文，不继承主会话。

**允许**：读 PDF/SI/pdftotext；读 READING.md、SCHEMA.md；建 source_map；产 YAML 中间结果。

**禁止**：写 wiki/REVIEWER_LOG；生成 receipt；分配 record_id（填 "TBD-by-main"）；调 reviewer agent；写 已阅读文献/；**写 literature 记录**（文献记录由主 AI 通过 `bibliography.py` 从 Zotero 元数据自动生成，PDF 解析文本中不含 DOI 等元数据）。

##### 执行器适配

**Claude Code / deepseek-v4**：文本管道优先 — rsk parse 或 pdftotext -layout；不支持原生 PDF 视觉。

**具备原生 PDF/视觉能力的执行器**：原生 PDF 优先 + pdftotext 辅助确认 Fig./Table 编号。

##### 中间结果格式

子 agent 返回 YAML-like 中间结果。每篇论文一个结果块，多篇用 `---` 分隔。

```yaml
paper_id: "AuthorYear"
title: "完整标题"
evidence_status: "full_text"

source_map:
  - claim_or_data: "数据描述"
    source: "Fig. X / Table Y / Section Z.Z"

module_coverage:
  <每个活动模块名>:
    status: covered | not_applicable | missing
    record_ids: []           # covered 由主 AI 写入后填真实 ID
    reason: ""               # not_applicable / missing 必填
    evidence_checked: []     # not_applicable 必须列原文/SI 位置

schema_candidates:
  <活动模块名>:
    - record_id: "TBD-by-main"
      paper_id: "AuthorYear"
      module: "<活动模块名>"
      category: "..."
      subject: "..."
      metric: "..."
      value: "..."
      unit: "..."
      condition: "..."
      source: "[Author Year, Journal, Fig. X / Table Y]"
      confidence: "single_source | multi_source | verified"
      note: ""
  # 只列当前 schema 中适用的 concrete modules（literature 除外——由主 AI 通过 bibliography.py 自动生成）

wiki_sync_candidates:
  concepts_to_update: []
  concepts_to_create: []
  paper_stub_needed: false

missing_data_evidence:
  - module: "<活动模块名>"
    statement: "原文经扫描，Section X.X (Methods)，[具体说明]"

risk_flags: []
```

**格式铁律**：
- 子 agent 中间结果**优先要求输出 JSON**；YAML-like 文本在手工转换时曾因缩进/引号差异导致解析器反复回退。主 AI 转换时逐块核对括号与引号闭合。
- source_map 每条精确对应一个 Fig./Table/Section
- schema_candidates 每条有 source 字段含具体编号
- record_id 一律 "TBD-by-main"
- missing_data_evidence 必须注明扫描了哪个 Section
- value/unit 能拆则拆

##### 主 AI 质量门禁（不可跳过）

对每个 agent 的中间结果执行：

1. **source_map 完整性**：条目 ≥5，每条有唯一 Fig./Table/Section
2. **module_coverage**：活动模块必须逐一声明；covered 引用真实记录，
   not_applicable 有 reason + evidence_checked，missing 直接阻断
3. **schema_candidates 逐条**：有 source、value/unit 已拆分、无编造字段
4. **missing_data_evidence 质量**：禁用笼统"原文未说明"

```
逐篇独立判定状态机（不因单篇失败阻断整批）：
- accepted：全部门禁达标 → 进入写入
- partial：主体达标，个别模块 missing 且有完整 missing_data_evidence → 允许写入，coverage 如实标记
- retryable_failed：门禁未达标且属可修复（如缺 source_map 条目）→ 只重 spawn 该篇（更严格 prompt），其余论文继续；重试仍不达标 → 主 AI 亲自精读该篇
- needs_human_review：3 轮重试仍失败 → 写 kb/REVIEWER_LOG.md 待用户裁决，不阻塞其他论文
```

##### 分批写入（主 AI 执行）

主 AI 负责将子 agent 产出的 YAML 中间结果转换为 JSON 并调用 `rsk sync` 写入 kb。

**Step 1: 保存 JSON 文件**

> **先清空再写入（强制）**：每次批量写入前必须清空 `tmp/extracted/` 上一批残留——
> `--input-dir` 会把目录内所有 JSON 一并写入，而 record_id 按 concrete module
> 全局递增，残留混入后无法事后安全剔除。

将每个子 agent 的完整 ingest envelope（`paper_id`、
`schema_candidates`、`module_coverage`）转为 JSON，保存到
`tmp/extracted/` 目录：

```powershell
# 目录结构
tmp/extracted/
├── paper1.json    # 子 agent 1 产出
├── paper2.json    # 子 agent 2 产出
└── paper3.json    # 子 agent 3 产出
```

JSON 格式（每篇论文一个对象，coverage 不得丢弃）：

```json
[
  {
    "paper_id": "Li2023",
    "module": "synthesis",
    "schema_version": "schema_v1",
    "category": "合成条件",
    "subject": "水热法合成 Pt/C 催化剂",
    "metric": "温度",
    "value": "180",
    "unit": "°C",
    "condition": "12h, 0.5M NaOH",
    "source": "[Li 2023, ACS Catal., Table 1]",
    "confidence": "single_source",
    "note": ""
  }
]
```

**Step 2: 调用 rsk sync**

```powershell
# 预览待写入记录（不实际写入）
rsk sync --input-dir tmp/extracted/ --dry-run

# 批量写入所有 JSON
rsk sync --input-dir tmp/extracted/

# 单个文件写入
rsk sync --input tmp/extracted/paper1.json
```

脚本功能：
- 验证 12 个必需字段（paper_id, module, category, subject, metric, value, unit, condition, source, confidence, note, schema_version）
- 自动分配 record_id（按 concrete module 全局递增）
- 按活动 `name -> file` 映射追加到 `kb/*.md`
- 同步持久化 `kb/coverage/<paper_id>.md`

**Step 3: 更新 literature.md 索引（强制通过 bibliography.py）**

literature 记录**不得**由子 agent 生成——PDF 解析文本中不含 DOI、通讯地址等元数据，
且子 agent 无法访问 Zotero 数据库。主 AI 必须按以下步骤生成文献记录：

1. **从 `outputs/zotero_export.json` 提取元数据**：按 paper_id/Zotero key 匹配，获取
   `authors`、`title`、`journal`、`year`、`doi`。

2. **补充作者单位**：从 PDF front matter 解析 `first_author_affiliation`
   和 `corresponding_affiliations`；若第一作者单位仍缺失，
   `bibliography.py` 可从 Crossref 自动补充第一作者单位。
   Crossref 不用于推断通讯作者单位。

3. **调用 `rsk/kb/bibliography.py:build_bibliography_record()`** 生成标准 13 字段
   文献记录。该函数自动将作者、DOI、期刊、年份等信息存入 `value` 字段，将完整书目
   元数据序列化为 JSON 存入 `note` 字段，category 固定为 `"文献信息"`、
   metric 固定为 `"bibliographic_metadata"`。

4. **通过 `rsk/kb/bibliography.py:upsert_bibliography_record()` 写入**，确保每篇
   论文只有一条 literature 记录（已存在时原地替换，避免重复）。

**Step 3.5（可选，精读增强）：评价类记录**

书目记录之外，主 AI 在精读验收后可为每篇论文补 4-6 条**评价类记录**，作为后续
对比综合、研究空白挖掘的证据源（仅由主 AI 亲写，子 agent 仍禁写）：

- 主题清单：创新代价 / 作者承认的局限 / 审稿视角质疑 / 反直觉结果归因 /
  理论贡献 / 实践启示。
- 写入位置：结论、限制与证据边界对应的 `claims` role module（按活动
  `schemas/generated/modules.yaml` 解析；旧 6 模块工作区惯例写 literature，
  以活动 schema 的 role 映射为准）。
- **attribution 纪律（不可跳过）**：`note` 字段以归因前缀开头——
  `attribution:作者`（论文原文立场，可当论文观点引用，confidence 可为
  verified/single_source）、`attribution:AI审稿视角`（AI 评价，必须转述带标签、
  不得冒充论文内容）、`attribution:AI推测`（显式标注推测）。涉及原文的条目
  `source` 仍须指向具体 Section/Fig./Table；纯 AI 推测条目 source 写明
  "AI 推测，无原文出处"。

**Step 4: 同步 wiki/**

按 `workflow/knowledge/WIKI_SYNC.md` 同步 wiki 概念页和论文页。

##### 最终对账

全部批次完成后：
- 确认 N 篇全部在 literature.md 建索引
- 逐篇核验每个活动模块均有合法 coverage 状态
- 未达标 → 继续处理 → 重新对账
- 全部达标 → 输出完成摘要

**完成告知格式**：
```
批量导入完成：N/N 篇全部入库
[1/N] Author (Year) — 入了 X 条合成 + Y 条性能 + Z 条谱图 + W 条机理 + V 条方法
...
wiki 同步：概念页 [A, B] 已更新
```

##### 防偷懒检查点

- [ ] 每篇有 source_map（≥5 条）
- [ ] source 含具体 Fig./Table/Section 编号
- [ ] missing_data_evidence 注明扫描了哪个 Section
- [ ] not_applicable 有 evidence 支撑
- [ ] 综述论文分类框架完整提取

##### 完成标准

1. 全部 N 篇在 literature.md 有索引
2. 每篇活动模块 coverage 完整；所有 N/A 均有理由、证据并等待独立核验

### Step 4: 向量同步

```powershell
rsk sync           # 增量同步
rsk sync --full    # 全量重建
```


## 检索流程（论文知识问答强制执行）

任何涉及"某篇论文 / 某个体系 / 某类反应 / 某种方法是否在 kb 中有记录"的问题，**不得只凭 AI 记忆或直接读 kb 文件回答**。必须先用向量检索定位到具体 record_id，再读取完整 schema 行。

> 最高优先级规则见插件 `skills/researchkeeper/references/RSK-DETAILED-GUIDE.md`「专业问答强制检索前置（不可跳过）」：专业问题先检索、未命中走外部检索、回答按证据层标注。

### 两层检索架构

kb 有两套向量集合：

| 集合 | 存储后端 | 内容 | 适用场景 |
|---|---|---|---|
| `kb_claims` | numpy `.npy` | 13 字段生成的 claim，以及按活动 module order 构造、排除 literature role 的 `chain-<paper_id>` 跨模块 claim；学科同义词只由相应模板显式启用 | **默认检索入口** |
| `kb_papers` | numpy `.npy` | per-record 自然语言 chunk | 兜底全文语义匹配 |

> **v1.3 numpy 全量**：claims 和 papers 均使用 numpy 存储（`vector_db/*_embeddings.npy` + `*_meta.json`）。全内存 cosine 检索，零外部依赖。此前 ChromaDB 1.x Windows HNSW 索引持久化 bug 已彻底规避。

### 强制调用命令

**第一优先**——claims 检索 + 论文画像扩展（返回 record_id + 同论文全部模块 claim，可精确定位）：

```powershell
rsk search "<query>" --claims --top 5 --expand
```

**兜底**——papers 检索（claims 未命中时使用）：

```powershell
rsk search "<query>" --top 5
```

**JSON 输出**（供程序解析）：

```powershell
rsk search "<query>" --claims --top 5 --expand --json
```

### 执行顺序（两步检索）

向量库是**精准定位工具**，不是数据来源。claims 存储的是自然语言摘要，完整的 13 字段 schema 记录必须从 kb 文件读取。

**第一步：向量检索定位 record_id**

```powershell
rsk search "用户问题原文" --claims --top 5 --expand
```

输出示例：
```
[1] methods-0042 | paper=Li2023 | methods | methods.md
    [DFT计算] Li2023 — PBE+D3泛函, 截断能500eV. 来源: [Li 2023, ACS Catal., Table S1]
```

`--expand` 会在结果前额外输出该论文的完整画像（各模块 claim 按模块分组），避免只看到孤立片段而丢失前后实验逻辑。

**第二步：读取 kb 文件获取完整数据**

```powershell
Read kb/methods.md → 搜索 "methods-0042" → 提取完整 schema 行
```

完整 schema 行包含 13 个字段：
```
| methods-0042 | schema_v1 | Li2023 | methods | DFT参数 | 截断能 | ENCUT | 500 | eV | 静态计算 | [Li 2023, ACS Catal., Table S1] | single_source | PAW_PBE |
```

**输出格式**：

```
【向量检索 → claims】record_id: methods-0042
【schema 精读】
- 论文: Li2023
- 参数: 截断能 = 500 eV
- 条件: 静态计算
- 出处: [Li 2023, ACS Catal., Table S1]
- 备注: PAW_PBE
```

**兜底机制**：

若 top-5 claim 的 paper_id、module、语义与问题均不对口：
1. 明确说"向量检索未命中相关记录"
2. 用 Grep 兜底搜索 kb 文件：`Grep "关键词" kb/*.md`

### Claims 索引（自动维护）

`rsk sync` 默认在同步 `kb_papers` 后**自动重建** claims 索引：

```
rsk sync  →  kb_papers（按活动 concrete modules 生成 per-record chunks）
         →  [auto] build_claims.py → claims_index.jsonl（1562 claims）
         →  [auto] sync_claims()  →  claims_embeddings.npy + claims_meta.json
```

若只更新 claims 不重建 kb_papers：
```powershell
rsk sync --from-claims --full
```

> ⚠️ `--from-claims` 只重嵌入**现有** claims_index.jsonl，不会重新运行 claim
> 构建逻辑。修改了 claim 构造规则（同义词、chain claim 规则等）后，必须先走
> 默认 `rsk sync`（自动重建 claims）或 `--full`，`--from-claims` 才有意义。
> 另外常驻服务会把向量缓存在内存——`rsk sync` 后必须重启服务并做刷新验证，
> 见 `workflow/vector/VECTOR.md`「sync 后必须重启常驻服务」。

跳过自动 claims rebuild（仅在不需要刷新 claims 时使用）：
```powershell
rsk sync --skip-claims
```

> `build_claims.py` 将 13 字段 schema 行统一合成为自然语言 claim。
> 只有 `electrocatalysis` profile 显式启用领域同义词扩展；generic-science/custom
> schema 保持学科中立。
> `sync_claims()` 将 claims 嵌入为 `claims_embeddings.npy`（float32 归一化向量）+ `claims_meta.json`（含 record_id/paper_id/module/source_file/claim_text），查询时 numpy cosine 相似度检索。

## 向量库维护

```powershell
rsk sync           # 增量同步（kb_papers + claims 均增量）
rsk sync --full    # 全量重建（kb_papers + claims 均全量）
rsk sync --dry-run # 预览变更
rsk sync --skip-claims  # 只同步 kb_papers，跳过 claims
```

> **增量策略**：`rsk sync` 按实际 KB Markdown hash 检测新增、修改和删除，
> 只重建变化 concrete module 的 papers/claims；coverage 和 audit metadata
> 永不进入 embedding。日常补全无需默认使用 `--full`。

## 质量审计

用户通过 `/researchkeeper:audit-all` 手动触发。详见插件 `skills/audit-all/SKILL.md`（含 sync 后强制重启服务与刷新验证的 Step 0.5）。

## rsk 命令索引

| 命令 | 用途 |
|---|---|
| `rsk import --from-zotero` | Zotero → JSON 元数据导出 |
| `rsk parse --from-zotero` | PDF → 文本段落（Markdown），自动合并 SI |
| `rsk sync` | 写入 kb + 向量库同步（增量 / `--full` 全量 / `--skip-claims` 跳过 claims） |
| `rsk search` | 语义检索入口（`--claims` 精准 / 默认 papers 兜底） |
| `rsk diff` | Zotero vs kb 对账：找出来入库论文 |
| `rsk fix-ids` | 批量归一化 paper_id |
| `rsk verify` | 入库后验收：验证 paper_id 在 kb 中的模块覆盖 |
| `rsk serve` | 常驻查询服务（高频检索时先启动，避免重复加载 bge-m3） |
| `rsk audit-sync` | 同步后向量审计 |

## 依赖

- bge-m3: auto-downloaded (see rsk_config.yaml model_cache_dir)
- Zotero 7: (configured via rsk_config.yaml)
