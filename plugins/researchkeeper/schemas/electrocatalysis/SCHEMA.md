# 电催化知识库 Schema v1

> 适用范围：选择 `electrocatalysis` 模板后由
> `schemas/generated/modules.yaml` 激活的 concrete modules。精读笔记和
> `wiki/` 概念页保持人读格式，但其中关键数据必须能回溯到 schema 化 kb
> 条目。

## 核心原则

- `kb` 是结构化事实层；`wiki` 是展示层；`已阅读文献` 是完整阅读档案。
- 后续新增、补充、迁移的 kb 条目必须使用 `schema_v1` 字段，不再新增旧格式表格。
- 缺失信息不得编造，统一写 `原条目未载明，需回原文核对`。
- 每条新记录必须有 `source`，且 `source` 必须包含论文标识和
  Fig./Table/Section/Methods/SI 等出处；书目信息可使用 PDF front matter、
  Zotero metadata 或 DOI metadata。旧 source 无法完整解析时保留原字符串并
  报告兼容 warning。
- 若旧条目迁移时无法拆出 `value` 和 `unit`，保留 `metric` 与 `note`，并将 `value`/`unit` 标为待核对。
- Reviewer 只读审计；审计日志由主 AI 写入 `kb/REVIEWER_LOG.md`。
- 每篇论文必须在 `kb/coverage/<paper_id>.md` 对全部活动模块声明
  `covered`、`not_applicable` 或 `missing`；N/A 必须有理由和证据位置。

## 通用字段

所有模块至少包含以下字段：

| 字段 | 必填 | 说明 |
|---|---|---|
| `record_id` | 是 | 稳定条目编号，格式建议：`module-0001` |
| `schema_version` | 是 | 当前固定为 `schema_v1` |
| `paper_id` | 是 | 论文短标识，如 `Shen2026`、`Wang2021_ORR` |
| `module` | 是 | 必须是活动 `schemas/generated/modules.yaml` 中的 concrete module name |
| `category` | 是 | 原模块内主题标题或分类 |
| `subject` | 是 | 催化剂、体系、路径、方法、文献或表征对象 |
| `metric` | 是 | 数据项名称，如 FE、峰位、势垒、合成温度、DFT 泛函 |
| `value` | 是 | 具体数值或描述；无法拆分时写 `原条目未拆分，见 note` |
| `unit` | 是 | 单位；无单位或无法拆分时写 `无` 或 `原条目未载明，需回原文核对` |
| `condition` | 是 | 电解液、电位、测试构型、计算模型、表征条件等 |
| `source` | 是 | `[Author Year, Journal/Section/Fig./Table/SI]` |
| `confidence` | 是 | `single_source` / `multi_source` / `verified` / `conflict` / `migrated_from_legacy` |
| `note` | 是 | 保留原始字段、解释、冲突、缺失项、推测边界 |

## 模块专用建议

### entities

优先拆分催化剂、载体、电解质、反应物、中间体和样品的身份、组成、
结构与状态；同一实体跨模块命名必须一致，并能回溯组成或结构证据。

### synthesis

优先拆分：

| 字段 | 含义 |
|---|---|
| `subject` | 催化剂或材料 |
| `metric` | 前驱体、用量、温度、时间、气氛、洗涤、热处理、负载量 |
| `condition` | 合成路线、水热/电沉积/热解/浸渍等 |

### performance

优先拆分：

| 字段 | 含义 |
|---|---|
| `subject` | 催化剂 + 反应 |
| `metric` | FE、current density、yield、rate、Tafel、TOF、stability、selectivity |
| `value` | 数值 |
| `unit` | `%`、`mA cm^-2`、`mmol h^-1 gcat^-1`、`h` 等 |
| `condition` | 电位、电解液、电池构型、底物浓度 |

### conditions

优先拆分电位、参比标尺、电解液、pH、浓度、温度、压力、电池构型、
气氛与其他边界条件，并保留单位和适用语境。

### spectra

优先拆分：

| 字段 | 含义 |
|---|---|
| `subject` | 材料/体系/中间体 |
| `metric` | 技术 + 峰/信号，如 Raman peak、XPS BE、m/z、EXAFS CN |
| `value` | 峰位、结合能、m/z、键长、配位数 |
| `unit` | `cm^-1`、`eV`、`m/z`、`Å`、`无` |
| `condition` | 原位条件、电位、光照、反应物 |

### mechanism

优先拆分：

| 字段 | 含义 |
|---|---|
| `subject` | 反应路径、活性位、描述符、中间体 |
| `metric` | RDS、barrier、ΔG、adsorption mode、descriptor、evidence |
| `value` | 数值或路径描述 |
| `unit` | `eV`、`Å`、`无` |
| `condition` | 模型、表面、电解质、反应条件 |

### methods

优先拆分：

| 字段 | 含义 |
|---|---|
| `subject` | 方法、构型、计算设置、表征方案 |
| `metric` | cell type、reference electrode、functional、k-points、slab、probe、reactor |
| `value` | 参数值 |
| `unit` | 物理单位或 `无` |
| `condition` | 适用体系或用途 |

### claims

优先拆分作者结论、局限、意义和外推主张。主张必须由已有记录与原文证据
支持，并保留限定语和适用边界。

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
## 审计要求（数据质量契约，非审计流程）

> 审计流程与维度表见 `kb/REVIEWER.md`。本节仅定义 schema 层面的数据完整性要求。

Reviewer 对 schema 化 kb 至少检查：

1. 必填字段是否齐全。
2. `source` 是否逐行存在，且不是笼统段落来源。
3. `value` 和 `unit` 是否能拆则拆；不能拆时是否在 `note` 说明。
4. `confidence=migrated_from_legacy` 的条目是否保留原始信息且未编造缺失字段。
5. `wiki` 中关键数字是否能追溯到 schema 化 kb 条目。
6. 后续新增条目不得使用旧格式表格。

---

## 附录：子领域数据提取检查清单

精读论文时按 Step 1 论文定位勾选的子领域挂载对应模块。

### Ⅰ 电催化（实验）

- 催化剂：组分 / 合成 / 形貌（TEM/SEM/HAADF）/ 负载量 / ECSA 测定方式。
- 电解液：种类 / 浓度 / pH / 阳离子（K⁺/Na⁺/Cs⁺/Li⁺）。
- 测试构型：H-cell / flow cell / MEA / GDE，参考电极换算（vs. RHE）、iR 补偿百分比。
- 性能：FE / jpartial / 过电位 / Tafel / 稳定性时长 + 衰减率。
- 选择性：HER / 副反应如何被抑制。
- 活性位点：XAS / SEIRAS / Raman / DEMS / isotope labeling。
- 产物定量：GC / HPLC / NMR / IC，检出限与误差范围。

### Ⅱ C-N 偶联

- N 源：NO₃⁻ / NO₂⁻ / NO / N₂ / NH₂OH，浓度。
- C 源：CO₂ / CO / 醛 / 胺。
- 产物：尿素 / 酰胺 / 胺 / 腈 / 氨基酸。
- C-N 键形成步：哪两个中间体偶联（*CO+*NH₂ / *NHCO+*NH₂ / *CO+*NO）。
- 协同效应：相比单独 NO₃RR、CO₂RR 的增益体现在哪。
- 同位素证据（¹⁵N / ¹³C）：用来证明什么。
- 产率单位：FE / mmol/h/cm² / mg/h/mg_cat。
- 空白对照：无 C 源 / 无 N 源 / 无催化剂。
- 副产物谱：NH₃ / H₂ / CO / HCOOH。

### Ⅲ 电氧化

- 底物：甲醇 / 乙醇 / 甘油 / 尿素 / HMF / 胺类。
- 是否替代 OER，热力学优势（理论电位差）。
- 机理：直接氧化 vs. *OH 介导 vs. 高价金属介导 vs. 晶格氧参与。
- 产物分布与选择性（电氧化中选择性常比活性更关键）。
- 是否与阴极 HER / CO₂RR / NO₃RR 耦合。
- 活性物种：MOOH / 高价金属 / 晶格氧标记证据。

### Ⅳ 界面水微环境

- 探测：SEIRAS / in-situ Raman / SFG / AIMD / MLFF-MD。
- 结构描述符：H-down vs. O-down、ice-like vs. liquid-like、悬挂 OH、4-coord water、dangling/dihedral/tetrahedral/hydrated-ion。
- 阳离子效应：水合半径 / 特性吸附 / 界面电场与水网络的影响。
- EDL：IHP / OHP / Stern 层水取向 / 扩散层。
- H-bond 网络连通性如何影响 PCET、质子传输。
- 关键质疑：界面水是"参与反应"还是"调控反应"？证据链是否闭合？

### Ⅴ DFT 计算

- 软件：VASP / CP2K / QE / Gaussian / ORCA。
- 泛函 + 色散校正：PBE / RPBE / SCAN / HSE + D3 / optB86b-vdW。
- Slab：层数 / 真空层厚度 / k-points / 底层固定层数 / 对称性。
- Hubbard U（3d TM）：U 值选取依据。
- 电化学界面：CHE / GC-DFT（Sabatier-Andersen 等）/ 显式溶剂 / 隐式（VASPsol）。
- 自由能图：ΔG / ZPE / 熵校正 / 决速步。
- 动力学：NEB / CI-NEB 势垒。
- 描述符：d-band / eg 占据 / OH 结合能 / Bader / ICOHP。
- 电子结构：PDOS / COHP / 电荷密度差 / ELF / 轨道杂化。
- 检查点：参考态合理性、溶剂处理、收敛性、敏感性测试。

### Ⅵ MLFF + MD

- 架构：DeePMD / NequIP / Allegro / GAP / SchNet / PaiNN。
- 训练集：AIMD 来源 / 数据规模 / 采样策略（主动学习 / DPGEN / on-the-fly）。
- 精度：能量与力的 MAE / RMSE，与 AIMD 对比的物性（RDF / 振动谱）。
- 尺度：原子数 / 模拟时长（ps / ns / μs）。
- 带电界面 / 恒电势：显式离子 / Grand Canonical MD / 双层水 setup。
- 增强采样：metadynamics / umbrella sampling / SMD / replica exchange / committor analysis。
- 自由能：PMF 曲线对应的物理过程，CV 选取合理性。
- 物性：RDF / ADF / MSD / 扩散系数 / H-bond 寿命 / 配位数演化。
- 关键质疑：MLFF 是否覆盖反应路径相空间？是否进入外推区？

### 综述论文特殊提取规则

- **分类框架**：所有类别独立列出（类别名 + 定义 + 特征参数 + 代表案例 + 原文献编号），不可省略任何一类。
- **方法学进展**：每种方法学（XAS / SHINERS / SEIRAS / AIMD 等）单独成节，含原理 + 关键参数 + 1-2 个代表案例 + 综述未覆盖但重要的方法。
- **标志性数据列表**：表格组织，按反应类型分组（HER / OER / CO₂RR / NO₃RR / ...），每条标注原文献编号（ref XX, 作者+期刊+年份）。
- **机理通路**：提炼 3-7 条，每条注明证据来源（实验/计算/谁的论文），标记"实验↔计算配合最完备的金标准案例"。
- **种子论文清单**：独立列出 3-5 篇最值得追读的原文献（作者 + 期刊 + 年份 + 卷 + 页码）。
