# computer_kb Schema v0.2

`computer_kb/records/` 是计算软件知识库的事实层。所有 records 条目必须可追溯、可审计、可交叉链接。

核心原则：

> records 记录证据，wiki 负责解释。

## 1. 适用范围

本 schema 适用于：

```text
computer_kb/records/*.md
computer_kb/records/relations/*.md
computer_kb/records/templates/*.md
computer_kb/records/error_chains/*.md
```

不适用于论文 `kb/*.md`。论文计算参数仍按 `kb/SCHEMA.md` 写入 `kb/methods.md` 或 `kb/relations.md`。

## 2. record_type

允许的记录类型：

```text
parameter      # 软件参数，例如 ENCUT、EDIFF、POTIM
command        # 软件命令，例如 LAMMPS fix nvt、pair_style
file_format    # 输入/输出文件格式，例如 INCAR、OUTCAR、vasprun.xml、dump.lammpstrj
error          # 报错或异常症状
workflow       # 单软件或跨软件计算流程
concept        # 计算概念，例如 SCF convergence、dataset diversity
environment    # 本地环境、依赖、版本、编译/安装问题
relation       # 参数间关系，存活在 records/relations/ (v0.2 新增)
template       # 任务→参数决策模板，存活在 records/templates/ (v0.2 新增)
error_chain    # 报错→参数诊断链，存活在 records/error_chains/ (v0.2 新增)
```

> v0.2 新增的 `relation`、`template`、`error_chain` 必须完整继承第 3 节通用字段，再追加各类型专用字段（见第 18-20 节）。

## 3. 通用字段

所有 records 条目必须包含：

```yaml
record_id: vasp-param-ENCUT-0001
record_type: parameter
scope: single_software
software:
  - VASP
topic: ENCUT
source_type: official_doc
source_ref: https://...
version_or_doc_date: VASP 6.x / 2026-05-21 / unknown
claim: ENCUT controls the plane-wave kinetic energy cutoff.
evidence_level: must
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/ENCUT.md
related_records:
  - vasp-param-PREC-0001
note: 适用范围、限制、版本差异或未解决问题。
last_checked: 2026-05-21
```

## 4. 字段说明

| 字段 | 必填 | 说明 |
|---|---|---|
| `record_id` | 是 | 稳定编号。命名规则：`parameter` → `software-type-topic-N`；`relation` → `rel-software-topic-N`；`template` → `tmpl-software-task-N`；`error_chain` → `errchain-software-error-N` |
| `record_type` | 是 | 见允许类型 |
| `scope` | 是 | `single_software` 或 `multi_software` |
| `software` | 是 | 真实软件/工具名列表，不得留空 |
| `topic` | 是 | 参数、命令、报错、workflow 或概念名 |
| `source_type` | 是 | 来源类型 |
| `source_ref` | 是 | URL、本地文件路径、issue 链接或日志路径 |
| `version_or_doc_date` | 是 | 软件版本、文档日期或 `unknown` |
| `claim` | 是 | 这条记录说明什么 |
| `evidence_level` | 是 | 判断强度 |
| `confidence` | 是 | 可信度 |
| `related_wiki` | 是 | 对应 wiki 展示页；没有则写 `[]` |
| `related_records` | 是 | 相关 record；没有则写 `[]` |
| `note` | 是 | 限制、适用范围、版本差异、推测边界 |
| `last_checked` | 是 | 最后核对日期 |

## 5. scope 与 software

单软件记录：

```yaml
scope: single_software
software:
  - VASP
```

跨软件 workflow：

```yaml
scope: multi_software
software:
  - VASP
  - LAMMPS
```

禁止：

```yaml
software:
  - CrossSoftware
```

也禁止：

```yaml
scope: multi_software
software: []
```

## 6. software 允许列表

第一阶段重点：

- `VASP`
- `LAMMPS`

后续可扩展真实软件/工具名：

- 第一性原理主程序：`CP2K`、`QE`、`Gaussian`、`ORCA`、`CASTEP`
- MD 主程序：`GROMACS`
- 辅助/后处理工具：`VASPKIT`、`ASE`、`pymatgen`、`VASPsol`、`VTST`

禁止：

- `CrossSoftware`
- `DFT software`、`MD engine` 等泛称
- 自创缩写

## 7. source_type

允许的来源类型：

```text
official_doc        # 官方文档
official_repo       # 官方仓库 README/docs/examples
official_issue      # 官方 issue/discussion/maintainer 回复
local_error_log     # 本地真实报错日志
local_verified      # 本地已验证成功流程或修复
```

第一阶段不允许主 records 使用 CSDN、知乎、个人博客、非官方论坛。若未来使用，必须另建低置信度区域。

## 8. evidence_level

允许值：

```text
must      # 官方明确要求，或本地不这样做会失败
should    # 官方推荐，或本地多次验证更稳
avoid     # 官方不推荐，或本地验证会导致错误
check     # 不一定错，但必须检查
unknown   # 证据不足
```

`must` 和 `avoid` 必须有强来源支持，不能只来自 AI 推测。

## 9. confidence

允许值：

```text
official               # 官方文档或官方仓库明确说明
maintainer_explained   # 官方 issue/discussion 中维护者解释
local_verified         # 本地已验证成功
local_unverified       # 本地真实记录但尚未验证修复
conflict               # 与其他来源存在冲突，需并列呈现
```

## 10. evidence_level × confidence 组合校验

需要 FAIL 的情况：

- `evidence_level=must` 或 `avoid`，但没有 `source_ref` 或 `source_type`。
- `evidence_level=unknown`，却写成确定性 `claim`。
- `confidence=local_verified`，但没有本地证据路径。
- AI 推测被写成 `official` 或 `maintainer_explained`。

需要 WARNING/解释的情况：

- `evidence_level=must + confidence=conflict`：不一刀切禁止，但必须解释冲突来源和适用范围。
- `evidence_level=avoid + confidence=local_verified`：必须说明本地验证的是“做 X 会失败”，不是“没做过 X”。
- `evidence_level=must + confidence=local_unverified`：必须说明是官方强制但本地未验证，或改为 `check`/`should`。

## 11. 本地验证边界

本地经验必须限定：

- 体系。
- 软件版本。
- 输入/输出证据路径。
- 是否只在当前机器/当前体系验证。

不能把某个体系的 `local_verified` 经验泛化成全局软件规则。

## 12. 参数/命令类专用字段

适用于：

```text
record_type: parameter | command
```

建议追加字段：

```yaml
parameter_name: ENCUT
command_name: fix nvt
file_or_context: INCAR / LAMMPS input
definition: 官方定义或维护者解释
default_behavior: 默认行为；未知写 unknown
common_use:
  - slab calculation
  - AIMD
risk_if_misused:
  - 能量或力不收敛
  - 后续计算数据质量受影响
related_parameters:
  - PREC
  - EDIFF
```

## 13. 报错类专用字段

适用于：

```text
record_type: error
```

建议追加字段：

```yaml
exact_error: "Lost atoms: original ... current ..."
symptom: 模拟中断，原子丢失或数值发散
likely_causes:
  - timestep 过大
  - 初始结构重叠
diagnosis_steps:
  - 检查完整 log
  - 检查初始结构最短距离
  - 降低 timestep 做短测试
fixes:
  - 先 minimize
  - 降温启动
verified_on: 本地体系、软件版本或 unknown
unsafe_fixes:
  - 不建议直接无视 thermo 异常继续跑长程 MD
```

## 14. workflow 类专用字段

适用于：

```text
record_type: workflow
```

建议追加字段：

```yaml
goal: 从 VASP DFT 结果接入 LAMMPS 做 MD
inputs:
  - VASP relaxed structures
  - OUTCAR / vasprun.xml
outputs:
  - validation metrics
  - LAMMPS runnable input
steps:
  - VASP relax
  - VASP AIMD / sampling
  - dataset extraction
  - validation
  - LAMMPS deployment
checkpoints:
  - SCF convergence
  - force sanity check
  - dataset diversity
  - validation RMSE
  - short MD stability
failure_links:
  - vasp-error-scf-not-converged-0001
  - lammps-error-lost-atoms-0001
local_status: seed | partial_local_verified | local_verified
```

## 15. 冲突字段

任何 record 都可以追加：

```yaml
conflict:
  has_conflict: true
  conflict_with:
    - paper_kb:methods-0123
    - computer_kb:vasp-param-ENCUT-0001
  conflict_summary: 论文参数与官方推荐或本地验证经验不一致
  resolution: 并列保留；回答时说明适用范围，并建议本地小测试
```

冲突不得通过删除某一方来源来解决。

## 16. relation 专用字段

适用于 `record_type: relation`，在通用字段之外追加：

```yaml
record_id: rel-vasp-scf-precision-chain-0001  # 命名规则: rel-<software>-<topic_slug>-N
relation_type: overrides | requires_companion | mutually_constrained | coupled_accuracy | mutually_exclusive | prerequisite | strengthens
relation_basis:              # 关系推导依据（区别于 source_type）
  - official_cross_ref       # 官方文档交叉引用
  - official_category        # 官方分类体系同组
  - physical_constraint      # 物理/数学公式决定
  - domain_knowledge         # 领域经验推断，待本地验证
  - local_verified           # 本地跑过验证
  - code_analysis            # 从源码逻辑推断
parameters:                  # [{name, role, constraint}] 参与关系的参数列表
relation_rules:              # [{id, type, from, to, detail, decision, consequence}]
failure_signatures:          # [{symptom, likely}] 关系破坏时的症状
```

| 字段 | 必填 | 说明 |
|---|---|---|
| `relation_type` | 是 | 关系类型 |
| `relation_basis` | 是 | 关系推导依据列表，不可为空 |
| `parameters` | 是 | 参与关系的参数，每个含 role + constraint |
| `relation_rules` | 是 | 具体规则，每条含 type + from + to + detail + decision + consequence |
| `failure_signatures` | 否 | 关系破坏时的症状；有则写 |

`relation_basis` 与 `source_type` 分工：
- `source_type` 保持现有枚举，表示证据来源类型（official_doc / official_repo / local_error_log / local_verified）
- `relation_basis` 表示「这条关系是怎么推出来的」（official_cross_ref / physical_constraint / domain_knowledge / local_verified）
- 两者独立，可组合：`source_type: official_doc` + `relation_basis: [official_cross_ref, physical_constraint]`

## 17. template 专用字段

适用于 `record_type: template`，在通用字段之外追加：

```yaml
record_id: tmpl-vasp-aimd-nvt-pt-water-0001  # 命名规则: tmpl-<software>-<task_slug>-N
applies_to:                  # {systems, tasks, metals} 适用场景
hardware_profile:            # {gpu, max_batch_size, ...} 硬件约束（仅写实测值）
prerequisites:               # [{step, why, reference}] 前置步骤
parameters:                  # [{name, value, record, reasoning, constraint, source_type, source_ref}] 参数决策表
generated_command:           # 或 generated_input，可直接使用的命令或输入文件
critical_gotchas:            # [{symptom, cause, fix}] 该任务域的专属坑位
success_criteria:            # [{check, threshold}] 验收标准
```

| 字段 | 必填 | 说明 |
|---|---|---|
| `applies_to` | 是 | 适用场景描述 |
| `hardware_profile` | 否 | 硬件约束；有则仅写实测验证过的数值 |
| `prerequisites` | 是 | 前置步骤列表 |
| `parameters` | 是 | 参数决策表。每项的 source_type + source_ref 标记来源，不可用自由文本 |
| `generated_command` | 否 | 可直接使用的命令或输入文件模板 |
| `critical_gotchas` | 是 | 该任务的专属坑位 |
| `success_criteria` | 是 | 如何判断任务成功 |

## 18. error_chain 专用字段

适用于 `record_type: error_chain`，在通用字段之外追加：

```yaml
record_id: errchain-lammps-md-energy-nan-0007  # 命名规则: errchain-<software>-<error_slug>-N
exact_error:                  # 原始报错信息
diagnosis_chain:              # [{level, question, check, action}] 分层排查，至少 2 层，最深一层指向 root_cause
parameter_root_cause:         # [{parameter, issue, record}] 指向具体参数 records
relations_involved:           # [relation_id] 指向关系层
fixes:                        # [{priority, action, how, verified, evidence_status}] 按优先级排序
unsafe_fixes:                 # [{action, why_bad}] 禁止的修复方法
verified_on:                  # {environment, hardware, evidence_path[], verification_date}
```

| 字段 | 必填 | 说明 |
|---|---|---|
| `exact_error` | 是 | 原始报错原文或关键行 |
| `diagnosis_chain` | 是 | 至少 2 层排查步骤，最深一层指向 root_cause |
| `parameter_root_cause` | 是 | 指向具体 parameter records |
| `relations_involved` | 否 | 指向 relation records |
| `fixes` | 是 | 按 priority 排序。每项含 verified(bool) + evidence_status(string) |
| `unsafe_fixes` | 是 | 已知危险修法列表 |
| `verified_on` | 否 | 有证据时填写 environment/hardware/evidence_path/verification_date |

**fixes.verified 与 confidence 一致性规则**：
- `confidence: local_verified` 时 `fixes[0].verified` 必须为 `true` 且 `evidence_status` 指向可审计日志
- `confidence: local_unverified` 时 `fixes[0].verified` 应为 `false` 且 `evidence_status` 诚实说明缺什么证据
- 两者矛盾（如 `local_unverified` + `verified: true`）→ reviewer FAIL

## 19. records/errors.md 与 records/error_chains/ 的分工

| | `records/errors.md` | `records/error_chains/*.md` |
|---|---|---|
| record_type | `error` | `error_chain` |
| 存什么 | 错误基础事实：record_id、exact_error/symptom、官方来源、通用 likely_causes | 本地/任务特化诊断链：diagnosis_chain、parameter_root_cause、fix priority、unsafe_fixes、verified_on |
| 角色 | error index + 官方/通用错误事实入口 | 本地诊断链（关联硬件和体系） |
| 展开程度 | 不展开本地多步骤诊断链，不写硬件特化模板 | 完整分层诊断链 + 带证据的修复步骤 |
| 指向 | 可被 error_chain 通过 related_records 引用 | 必须通过 related_records 指回 errors.md 中的基础 error record |

冲突规则：
- 两处不得写互相矛盾的 fixes
- 如果 official doc 与 local fix 冲突，必须标 `confidence: conflict` 并说明适用范围
- 没有对应基础 error record 时，先在 errors.md 建 seed，再写 error_chain

## 20. wiki 追溯要求

`computer_kb/wiki/` 是展示层。凡是 wiki 页面包含以下内容，必须能追溯到 records：

- 参数定义。
- 强建议：`must` / `avoid`。
- 报错修复结论 → 追溯到 `records/errors.md` 或 `records/error_chains/*.md`。
- workflow 检查点。
- 参数关系解释 → 追溯到 `records/relations/*.md`。
- 任务参数建议 → 追溯到 `records/templates/*.md`。
- 版本差异。
- 本地已验证结论。

若暂时没有 records 支撑，必须标注：

```text
status: seed
evidence: needs_source
```

## 21. 禁止项

- 禁止把论文参数记录写入 `computer_kb/records/` 作为软件事实。
- 禁止把官方软件参数说明写入论文 `kb/methods.md`。
- 禁止把 AI 推测写成官方事实。
- 禁止使用 `CrossSoftware` 作为软件名。
- 禁止无来源的 `must` / `avoid`。

---

## 附录 B：wiki 页面链接模板

新建 wiki 页面时，必须包含以下链接段落。这不是可选的——缺少这些链接的页面会在 `check_wiki_links.py` 中被标记为孤儿页或零出链页面。

### 新建 error 页面模板

```markdown
---
software: <VASP|LAMMPS>
category: error
records:
  - records/error_chains/<error_chain_file>.md
---

# <报错标题>

> 事实追溯到 `computer_kb/records/error_chains/<error_chain_file>.md`。

## 错误签名

```
<报错原文关键行>
```

## 触发条件

<什么情况下会出现这个报错>

## 原因

<物理/数值/软件层面的解释>

## 修复方案

<逐步排查和修复>

## 相关概念

- [[<对应的 concept 页面>]] — <为什么相关>

## 相关报错

- [[<同软件/同类型的其他报错>]] — <鉴别诊断>
```

### 新建 concept 页面模板

```markdown
---
software: <VASP|LAMMPS>
category: concept
records:
  - records/<对应的 records 文件>.md
---

# <概念标题>

> 事实追溯到 `computer_kb/records/<对应的 records 文件>.md`。

## <正文内容>

## 常见错误

- [[<该概念相关的已知报错>]] — <一句话说明>

## 关联概念

- [[<上下游/同软件的其他概念>]] — <关系说明>
```

### 新建 workflow 页面模板

```markdown
---
software: <涉及的软件，逗号分隔>
category: workflow
records:
  - records/workflows.md
---

# <workflow 标题>

> 事实追溯到 `computer_kb/records/workflows.md`。

## <正文内容>

## 涉及概念

- [[<该 workflow 涉及的 concept 页面>]]

## 常见错误

- [[<该 workflow 中容易遇到的报错>]]
```
