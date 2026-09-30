# Generic Science Schema

Every knowledge record uses the stable `schema_v1` fields:

| record_id | schema_version | paper_id | module | category | subject | metric | value | unit | condition | source | confidence | note |
|---|---|---|---|---|---|---|---|---|---|---|---|---|

The active concrete modules and their semantic roles are defined by
`schemas/generated/modules.yaml`. Module files contain paper knowledge;
`kb/coverage/` contains audit metadata and is not semantic paper content.

New record sources must identify the paper and include at least one
Fig./Table/Section/Methods/SI location. Bibliographic records may instead cite
PDF front matter, Zotero metadata, or DOI metadata. Legacy source strings remain
readable and produce compatibility warnings when they cannot be fully parsed.

---

### literature

literature 模块承载三类记录：论文索引、文献信息、评价。

**论文索引记录**（每篇 1 条）：

| 字段 | 含义 |
|---|---|
| `subject` | 论文、分类框架、种子文献 |
| `metric` | 核心贡献、子领域、类型、关键数字、精读状态 |
| `value` | 结构化描述 |
| `unit` | `无` |
| `condition` | 研究方向或反应体系 |

**文献信息记录**（每篇 1 条，脚本自动生成，禁止手工编写）：

每篇入库论文必须有一条 `category=文献信息`、`metric=bibliographic_metadata` 的记录，
由 `rsk/kb/bibliography.py` 从 Zotero 元数据 + Crossref API 生成：

| 字段 | 内容 |
|---|---|
| `subject` | 论文完整题目 |
| `value` | `Journal; Year; DOI: xxx` |
| `unit` | `无` |
| `condition` | `bibliographic identity verification` |
| `source` | `[Zotero metadata, DOI: xxx, PDF front matter]` |
| `note` | JSON: 完整书目元数据（title, authors, corresponding_authors, journal, year, doi, affiliations, affiliation_source, verification） |

**评价类记录**（每篇 4-6 条，对应 READING.md 板块 4/6/7/8）：

除事实类记录外，每篇论文应从精读笔记中提取以下评价类 `metric`：

| `metric` | 内容 | 来源板块 |
|---|---|---|
| `创新代价` | 机制改动引入的权衡（计算成本 / 数据需求 / 收敛难度 / 泛化损失 / 工艺复杂度） | 板块 6 |
| `作者承认局限` | 作者在 Limitations / Discussion 中自述的局限 | 板块 7a |
| `审稿质疑` | 按 6 维度检查提出的最强质疑（每条记录写一个维度） | 板块 7b |
| `异常归因` | 反直觉结果的三层归因压缩为 1-2 句 + 理论判定（challenge / extension / limitation） | 板块 4 |
| `理论贡献` | 对领域认识的修正 / 扩展 / 挑战 | 板块 8 理论轨 |
| `实践启示` | 可落地的工艺 / 判据 / 参数指引 | 板块 8 实践轨 |

**attribution 硬规则**：评价类记录的 `note` 字段必须以 `attribution:` 开头，取值仅三种：

- `attribution:作者` — 原文明确陈述（含作者自述局限、作者给出的解释）
- `attribution:AI审稿视角` — 精读时基于原文的分析判断
- `attribution:AI推测` — 原文未说明、由 AI 补充的推测

需要补充说明时接在后面，用**全角竖线**分隔：`attribution:AI推测｜补充说明……`
（禁止半角 `|`，会破坏 Markdown 表格结构）。

### 可选扩展字段

#### `missing_status`（数据缺失状态）

当 `value` 或 `unit` 为缺失/占位文本时，建议标注缺失原因：

| 值 | 含义 |
|---|---|
| `not_reported` | 原文未报告该数据 |
| `not_applicable` | 该字段对此记录类型不适用 |
| `parser_failed` | PDF/SI 解析失败，无法提取 |
| `source_unavailable` | SI 文件缺失或无法访问 |
| `not_found` | Agent 在可获得文本中未找到 |
| `ambiguous` | 原文存在但数据有歧义 |
| `not_reviewed` | 尚未经人工核对 |

---

## Module-specific guidance

### literature

Literature records follow the 三类记录 (three record types) convention above.
Every paper MUST have:
1. One 论文索引 record (category=论文索引)
2. One 文献信息 record (category=文献信息, metric=bibliographic_metadata, auto-generated)
3. Four to six 评价 records (metric=创新代价/作者承认局限/审稿质疑/异常归因/理论贡献/实践启示)

All 评价 records MUST include an `attribution:` prefix in the `note` field
per the hard rules above. Records without `attribution:` in evaluation entries
will be flagged by the reviewer (audit dimension on literature completeness).

### entities / methods / conditions / results / relations / claims

For these modules, follow the concrete module descriptions in
`schemas/generated/modules.yaml` with the following priorities:

- `subject`: What entity/method/condition/result/relation/claim is described
- `metric`: The specific measurable dimension
- `value` + `unit`: Always split; use `无` when no unit applies
- `condition`: Operational context (potential, electrolyte, temperature, etc.)
- `source`: Must include Fig./Table/Section/Methods/SI location
- `note`: Human-readable context, caveats, cross-references
