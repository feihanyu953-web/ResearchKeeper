# Paper-Reader Wiki Sync Protocol

框架版本：v1.2-route

本文件承载论文 wiki/Obsidian 展示层同步规则。修改 `wiki/**/*.md` 前必须读取本文件和 `wiki/index.md`；如果同步来自论文 kb 入库，也必须读取 `kb/INDEX.md`。

## 展示层定位

`wiki/` 是论文知识网络和 Obsidian 展示层，不是独立事实源。

关键数字、谱峰、性能、机理判断必须能追溯到 `kb/*.md` 中的 `schema_v1` 记录。不得把未进入 schema 化 kb 的关键数字直接作为概念页事实。若某数字只存在于精读笔记而尚未写入 kb，先补入对应 kb 模块，再让 wiki 引用该数据。

## YAML frontmatter

本节只在当前任务同时包含导出笔记创建或更新时适用。若用户只要求修改 `wiki/**/*.md`，不得因为读取本文件而顺手修改 `已阅读文献/` 下的精读笔记。

需要创建或更新精读笔记时，先从活动 `literature` role 的固定书目 JSON
记录生成候选数据；不得手工重抄已有书目信息：

```powershell
$rsk = Join-Path $env:CLAUDE_PLUGIN_ROOT "bin\rsk.cmd"
& $rsk --workspace "<explicit workspace>" wiki-frontmatter "<paper_id>" --json
& $rsk --workspace "<explicit workspace>" wiki-frontmatter "<paper_id>" `
    --existing "<note.md>" --json
```

命令只输出 candidate/diff，不写笔记。受管理字段固定为 `title`、`authors`、
`year`、`journal`、`doi`、`corresponding_authors`、
`first_author_affiliation`、`corresponding_affiliations` 和
`kb_literature_record`。

- `add` 是笔记中尚不存在且有已核验证据的候选字段；
- `unchanged` 是已有值与 KB 一致的字段；
- `conflicts` 必须交给人工核对，不得静默采用任一侧；
- `preserved` 中的人工 `tags`、`method`、`system`、`type` 等字段不得覆盖；
- `diagnostics` 中每个缺失字段都保留证据缺口，不从其他论文或无关 record
  借值。

人工确认 candidate/diff 后，才可在笔记 `.md` 顶部（标题 `#` 之前）编辑 YAML
frontmatter。学科专属字段来自相应活动模块的已核验记录；所有数值字段仍须包含
数值、单位、条件和 source。

### 学科字段参考（以活动 schema 为准）

面向实验电催化 / 计算电化学工作区的常用约定（活动 schema 未覆盖时可参照）：

- `method`、`system`、`reaction` 必填；`catalyst`、`electrolyte` 对实验或
  实验+计算论文必填。
- `ΔG_RDS`、`barrier_*` 等计算字段有则填写，值必须包含步骤描述、数值和出处；
  `enhancement`、`FE`、`overpotential` 等实验字段有则填写。
- 所有数值字段必须附带出处，格式如
  `"步骤描述: 数值 (Table X, Fig. Y, Section Z)"`。
- `tags` 通常为 2-6 个标签，用于 Obsidian 图谱分组。
- 若论文类型无法适配某字段，直接省略，不填占位符。

## 关联概念标签

本节只在当前任务同时包含导出笔记创建或更新时适用。若用户只要求修改 `wiki/**/*.md`，不得因为读取本文件而顺手修改 `已阅读文献/` 下的精读笔记。

在笔记末尾（`## 附录` 之前或最后一行之后）追加：

```markdown
## 关联概念

- [[概念A]] · [[概念B]] · [[概念C]]
```

规则：

- 标签指向 `wiki/concepts/` 下已有概念页，使用文件名，不含路径和扩展名。
- 若现存概念页无法覆盖本文核心概念，先按 concept 聚合页规则创建概念页，再引用。
- 一篇论文通常 3-6 个概念标签。

## concept 聚合页

检查本次精读或入库的数据是否影响 `wiki/concepts/` 下已有概念页：

- 有影响：在相关概念页追加本文的新数据点、矛盾标记（`[!contradiction]`）或佐证信息，并链接回笔记（`[[笔记文件名]]`）。
- 新概念：创建 `wiki/concepts/<新概念>.md`，格式参照已有概念页，至少包含定义、关键数据、关联论文表和开放问题。
- 无影响：跳过，不为了形式新建概念页。

概念页中的关键事实必须能回到 `kb/` 的 schema 记录。已导出的精读笔记只能作为补充阅读入口或 Obsidian 反链，不得作为关键数字、谱峰、性能、机理判断的唯一事实来源。

## wiki/index.md 更新

按 `wiki/index.md` 的现有结构更新展示层索引：

- 在按子领域导航中更新概念页和论文数。
- 在按论文导航表中追加或修正论文条目。
- 在 Stub 论文表中移除已完成精读的 stub 或更新状态。
- 在实体索引中追加真实实体关系，不添加空泛实体。

同时更新 `wiki/log.md`，追加操作记录：

```markdown
| 日期 | ingest | 论文标题 | 更新了哪些概念页 |
```

## 与 kb schema 记录的追溯关系

`wiki/` 中的关键数字和机理判断必须能追溯到 `kb/SCHEMA.md` 约定的 schema 化记录。

同步时先读取 `schemas/generated/modules.yaml`，按 stable role 解析当前 concrete
module/file，不得假设固定模块名：

- 论文身份和书目信息回到唯一 `literature` role；
- 实体、材料、物种回到 `entities` role；
- 实验、计算或制备过程回到全部 `methods` role modules；
- 运行或测量条件回到 `conditions` role；
- 定量或定性观察回到全部 `results` role modules；
- 关系、机理和路径回到 `relations` role；
- 结论、限制和证据边界回到 `claims` role。

如果某类数据原文没有，必须在 kb 侧按规则标注“原文未说明”或“不适用”，不能在 wiki 侧绕过。
