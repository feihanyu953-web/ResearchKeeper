# computer_kb 来源登记

本文件登记 `computer_kb` 允许引用的官方来源、本地日志来源和本地验证来源。

第一阶段允许来源：

| source_type | 说明 | 使用边界 |
|---|---|---|
| `official_doc` | 官方文档 | 可作为软件行为和参数定义基准 |
| `official_repo` | 官方 README/docs/examples | 可作为官方示例或推荐流程 |
| `official_issue` | 官方 issue/discussion，尤其 maintainer 回复 | 可解释边界情况、版本差异和真实 bug |
| `local_error_log` | 本地真实报错日志 | 只证明本地出现过该问题，不自动证明修复有效 |
| `local_verified` | 本地已验证成功流程或修复 | 必须记录体系、软件版本、证据路径和适用范围 |

## 官方来源待补

| 软件 | 来源 | source_type | 状态 |
|---|---|---|---|
| VASP | VASP Wiki INCAR tag category | `official_doc` | active: full INCAR tag index; public entries retain their official URLs |
| VASP | VASP Wiki Molecular dynamics / Thermostats pages | `official_doc` | active: Seed2 MD/AIMD deep records; public entries retain their official URLs |
| LAMMPS | LAMMPS official command/style index pages | `official_doc` | active: full command/style index; public entries retain their official URLs |
| LAMMPS | LAMMPS official command documentation | `official_doc` | active: Seed3 MD basics; public entries retain their official URLs |
| VASP | Official VASP output and ASE IO docs | `official_doc` | not_implemented: Seed7 已随 MLFF 内容移除；该文档仍为通用官方来源 |
| LAMMPS | Official LAMMPS run/fix/thermo/dump docs | `official_doc` | not_implemented: Seed8 已随 MLFF 内容移除；该文档仍为通用官方来源 |
| LAMMPS | Official LAMMPS errors documentation | `official_doc` | active: Seed9 LAMMPS common error routes |

## 非主库来源

第一阶段不纳入 CSDN、知乎、个人博客、非官方论坛经验贴。若未来纳入，必须放入低置信度区域并标明不能覆盖官方记录。
