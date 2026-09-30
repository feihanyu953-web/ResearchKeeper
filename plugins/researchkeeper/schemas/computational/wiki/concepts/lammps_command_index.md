---
software: LAMMPS
category: concept
status: seed
seed: 3B
records: lammps.md
---

# LAMMPS 全命令/样式索引

> 展示层页面。全量索引记录在 `computer_kb/records/lammps.md`；各记录保留可公开访问的官方来源 URL。

## 1. 当前覆盖

本页对应的是 LAMMPS 官方文档的 command/style 索引级导入，不是逐条命令精读。

| 类别 | 数量 | 说明 |
|---|---:|---|
| general commands | 113 | 普通输入脚本命令，如 `units`、`read_data`、`run`、`variable` |
| fix styles | 286 | `fix ...` 系列 |
| compute styles | 175 | `compute ...` 系列 |
| pair styles | 303 | `pair_style ...` 系列 |
| bond styles | 25 | `bond_style ...` 系列 |
| angle styles | 27 | `angle_style ...` 系列 |
| dihedral styles | 17 | `dihedral_style ...` 系列 |
| improper styles | 15 | `improper_style ...` 系列 |
| kspace styles | 22 | `kspace_style ...` 系列 |
| dump styles | 31 | `dump ...` 输出样式 |
| **合计** | **1011** | records/lammps.md 实际记录数（1014 为 MLFF 内容移除前旧值，现与 imported_count 一致） |

## 2. 如何使用

`computer_kb/records/lammps.md` 只回答一个问题：

> 官方 LAMMPS 文档是否列出了这个 command/style，它的官方页面在哪里？

如果要回答“这个命令怎么写、默认值是什么、风险是什么、和别的命令怎么搭配”，必须进入对应主题的深度 records，例如：

| 主题 | 深度 records / wiki |
|---|---|
| LAMMPS MD 基础脚本 | `computer_kb/records/lammps_md.md`; `computer_kb/wiki/concepts/lammps_md_basics.md` |
| LAMMPS 常见错误 | 待建 |
| LAMMPS RDF/MSD/stress 分析 | 待建 |

## 3. 索引边界

- `records/lammps.md` 是全命令索引层。
- `records/lammps_md.md` 是 MD 基础命令深度层。
- 后续不要在 `records/lammps.md` 里手工追加长解释；长解释应进入专题 records 或 wiki。
- package-specific 命令和加速变体只作为官方索引事实记录；是否当前本机可用，要另查编译包、运行环境或本地错误日志。

## 4. 回答路由

当用户问 LAMMPS 命令时：

1. 先查 `records/lammps.md` 确认官方页面和类别。
2. 如果是 MD 脚本骨架命令，再查 `records/lammps_md.md` 和 `wiki/concepts/lammps_md_basics.md`。
3. 如果涉及某个 package、GPU/KOKKOS 等扩展功能，不能只凭索引回答可用性，要查官方页面和本地编译/运行环境。
4. 如果涉及报错，优先进入 `records/errors.md` 和 `wiki/errors/`；没有记录时再从官方错误/命令页面补库。
## Obsidian Links

- [[lammps_md_basics]]


- [[lammps_unrecognized_style_package]]

