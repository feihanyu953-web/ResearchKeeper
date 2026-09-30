# paper_to_compute · 论文计算参数到软件知识的桥接规则

框架版本：v0.1

本文件规定论文计算参数、论文机理结论与 `computer_kb` 软件知识之间如何互相引用。

## 核心原则

- 论文参数是论文事实，仍写入 `kb/methods.md` 或 `kb/relations.md`。
- 软件参数定义、报错、官方 workflow、本地验证经验写入 `computer_kb/`。
- 回答时可以融合引用，但存储时不能混写。

## 桥接场景

### 论文精读

如果论文出现 VASP/LAMMPS 等计算软件设置：

1. 先按 `kb/INDEX.md` 写入论文 `kb/methods.md`。
2. 如用户追问“这个参数是什么意思/是否合理”，再读取 `computer_kb/INDEX.md` 和 `workflow/computer-kb/query_router.md`。
3. 回答时并列呈现论文用法和软件定义。

### 计算方案设计

设计用户自己的流程时：

1. 从 `kb/literature.md`、`kb/methods.md`、`kb/relations.md` 找相似体系经验。
2. 从 `computer_kb/wiki/workflows/`、`records/` 找软件规则和本地经验。
3. 用 AI 判断给出适用性、风险和最小测试。

### 冲突

如果论文经验与官方软件知识冲突：

- 不删除任一来源。
- 记录冲突摘要。
- 回答时说明论文参数可能是特定体系/版本/作者经验，官方文档是软件行为基准。
- 最终建议必须包含本地小测试。
