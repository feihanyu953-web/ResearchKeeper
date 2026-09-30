# computer_kb · 计算软件知识库入口

框架版本：v0.2

`computer_kb/` 是独立于论文 `kb/` 的计算软件知识库，用于沉淀 VASP、LAMMPS 等计算软件的官方参数说明、官方 workflow、官方 issue/discussion、本地真实报错、本地验证经验和跨软件计算流程。

核心原则：

> 存储隔离，回答融合。

## 1. 与论文知识库的关系

`kb/` 是论文知识库（当前 generic-science schema 无独立论文 `wiki/` 展示层；下文 `wiki/` 相关描述为历史架构，按需启用）：

- `kb/methods.md`：记录某篇论文实际使用的计算参数、模型、方法。
- `kb/relations.md`：记录论文中的计算机理、能垒、路径、描述符（generic-science 模块名）。
- 原 `wiki/`：展示论文知识网络和概念关系。

`computer_kb/` 是计算软件知识库：

- 记录软件参数定义、输入文件规范、报错诊断、官方示例、本地验证流程。
- 不记录“某篇论文用了什么参数”，除非作为融合回答时引用论文 `kb`。
- 不向 `kb/*.md` 或原 `wiki/` 写入软件手册型内容。

## 2. 存储隔离

以下内容必须写入 `computer_kb/`，不得写入论文 `kb/`：

- VASP 官方参数解释，如 `ENCUT`、`EDIFF`、`ISMEAR`、`POTIM`。
- LAMMPS 命令解释，如 `pair_style`、`fix nvt`、`compute`。
- 软件官方报错说明和官方 issue/discussion。
- 本地真实 error log 和修复记录。
- VASP -> LAMMPS 等跨软件 workflow。

以下内容仍写入论文 `kb/`：

- 论文正文/SI 中出现的 DFT 参数。
- 论文给出的 slab、水层、k-points、泛函、U 值、AIMD 设置。
- 论文中的自由能、吸附能、Bader、d-band、反应路径。
- 论文方法学与机理结论。

## 3. 回答融合

回答计算相关问题时，不能只查一个库。必须综合以下来源：

1. **当前材料层**：当前论文 PDF/SI、用户给出的输入文件、报错日志、计算目录、脚本。
2. **论文知识层**：`kb/methods.md`、`kb/relations.md`、`kb/literature.md`（原 `wiki/` 展示层当前 schema 未启用）。
3. **计算软件层**：`computer_kb/records/`、`computer_kb/wiki/`、`workflow/computer-kb/`。
4. **AI 综合判断层**：基于前三层做适用性判断、风险识别、方案设计和下一步建议。

输出时优先使用证据标签：

- 【当前材料】
- 【论文知识】
- 【软件知识】
- 【本地经验】
- 【AI 判断】

## 4. 目录路由

```text
computer_kb/
  INDEX.md
  SCHEMA.md
  sources.md
  REVIEWER.md
  REVIEWER_LOG.md

  records/
    vasp.md
    vasp_md.md
    lammps.md
    lammps_md.md
    errors.md
    workflows.md
    relations/       ← 参数关系图 (v0.2 新增，首条 record 写入时创建)
    templates/       ← 任务→参数决策模板 (v0.2 新增，首条 record 写入时创建)
    error_chains/    ← 报错→参数诊断链 (v0.2 新增，首条 record 写入时创建)

  wiki/
    index.md
    concepts/
    errors/
    workflows/
    entities/
    meta/

```

`records/` 是事实层，必须有来源和证据等级。
`records/relations/` 编码参数间依赖关系（overrides / requires_companion / coupled_accuracy 等）。
`records/templates/` 编码任务→参数决策模板（含硬件约束、SBATCH、生成命令）。
`records/error_chains/` 编码报错→参数根因诊断链（分层排查、修复步骤、验证证据）。
  - 与 `records/errors.md` 共存：`errors.md` 为通用错误事实入口，`error_chains/` 为本地/任务特化诊断链。
`wiki/` 是展示层，用于解释、交叉链接和长期阅读。
`workflow/computer-kb/` 是融合层，规定如何把论文知识、软件知识和 AI 判断合并回答。

## 5. wiki 子目录定位

- `wiki/concepts/`：参数、命令、文件、模型、概念的解释页。
- `wiki/errors/`：一页一个典型 error signature，展开报错原文、原因、排查和修复边界。
- `wiki/workflows/`：端到端计算流程页面，串联 concepts、errors 和 records。
- `wiki/entities/`：软件版本、势函数文件、模型、机器、脚本工具等可复用实体页。
- `wiki/meta/`：维护规则、过时标记、与 `dft_models/` 的引用约定等元信息。

## 6. 来源边界

允许进入主库的来源：

- `official_doc`：VASP/LAMMPS 官方文档。
- `official_repo`：官方 GitHub README、docs、examples。
- `official_issue`：官方 issue/discussion，尤其是 maintainer 回复。
- `local_error_log`：本地真实报错记录。
- `local_verified`：本地已验证有效的修复或 workflow。

第一阶段不纳入 CSDN、知乎、个人博客、非官方论坛经验贴。若未来纳入，必须单独低置信度标记，不得覆盖官方记录。

## 7. 与 dft_models/ 的关系

`dft_models/` 是计算任务工作区，存放具体体系的输入文件、输出日志和计算结果。
`computer_kb/` 是计算知识库，从 `dft_models/`、官方文档和官方 issue 中提炼通用或半通用经验。

当前阶段保持松耦合：

- `computer_kb` 可以引用 `dft_models/` 中的具体路径作为 `local_verified` 或 `local_error_log` 证据。
- `dft_models/` 不受 `computer_kb` gate 扫描。
- `dft_models/` 暂不建立独立审计机制。

## 8. 问题路由

论文精读中问计算合理性：

```text
当前论文/PDF/SI
-> kb/methods.md + kb/relations.md
-> computer_kb 参数/官方说明
-> AI 判断适用性
```

设计自己的计算流程：

```text
论文 kb/wiki 中的相似体系经验
-> computer_kb workflows/concepts/errors
-> 本地已有模型/脚本/验证经验
-> AI 生成方案并标注风险
```

报错排查：

```text
本地 error log
-> computer_kb/wiki/errors
-> computer_kb/records/errors.md           # 通用错误事实入口
-> computer_kb/records/error_chains/       # 本地/任务特化诊断链
-> 官方 issue/doc
-> 相关 workflow 背景
-> AI 给出排查顺序
```

参数关系查询：

```text
computer_kb/records/relations/
-> 参数 A 的关系图
-> parameter A / parameter B 的 records
-> 官方交叉引用
-> AI 给出联动修改建议
```

任务参数设计：

```text
用户目标和硬件约束
-> computer_kb/records/templates/
-> 匹配任务域 template
-> 各参数的 records
-> 本地硬件验证证据
-> AI 生成参数组合
```

参数解释：

```text
computer_kb/wiki/concepts
-> computer_kb/records
-> 官方来源
-> 如涉及论文复现，再回查 kb/methods.md
```

## 9. 冲突处理

如果论文经验、官方文档、本地经验冲突，不得强行合并为一个结论。

- 并列呈现冲突来源。
- 标注每个来源的适用范围。
- 官方文档作为软件行为基准。
- 论文参数作为特定体系/版本/作者实践。
- 本地验证作为当前环境下的经验。
- 最终方案必须说明需要哪些小测试验证。

