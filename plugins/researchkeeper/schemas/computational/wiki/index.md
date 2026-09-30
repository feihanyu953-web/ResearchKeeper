# computer_kb wiki 索引

> `computer_kb/wiki/` 是展示层。关键参数定义、报错修复结论、workflow 检查点和本地验证结论必须能追溯到 `computer_kb/records/`。

## 按页面类型导航

| 类型 | 目录 | 用途 |
|---|---|---|
| 概念页 | `concepts/` | 参数、命令、文件、模型、计算概念解释 |
| 报错页 | `errors/` | 报错原文、原因、排查步骤、修复边界 |
| 工作流 | `workflows/` | 端到端计算流程和检查点 |
| 实体页 | `entities/` | 软件版本、模型、机器、脚本工具 |
| 元信息 | `meta/` | 维护规则、过时标记、引用约定 |

## 当前状态

| 页面 | 类型 | 状态 | 追溯 records |
|---|---|---|---|
| `concepts/vasp_aimd_md_parameters.md` | VASP AIMD/MD 参数组 | Seed2 已建 | `computer_kb/records/vasp_md.md` |
| `concepts/lammps_command_index.md` | LAMMPS 全命令/样式索引 | Seed3B 已建 | `computer_kb/records/lammps.md` |
| `concepts/lammps_md_basics.md` | LAMMPS MD 基础命令组 | Seed3 已建 | `computer_kb/records/lammps_md.md` |
| `concepts/vasp_scf_accuracy_chain.md` | VASP SCF 精度金字塔 | P1 | `computer_kb/records/relations/vasp_scf_accuracy_chain.md` |
| `concepts/vasp_neb_chain.md` | VASP NEB/CI-NEB 参数链 | P2 | `computer_kb/records/relations/vasp_neb_chain.md` |
| `concepts/vasp_dft_plus_u_guide.md` | VASP DFT+U 选取指南 | P2 | `computer_kb/records/relations/vasp_dft_plus_u.md` |
| `concepts/vasp_md_thermostat_guide.md` | VASP MD thermostat 选择指南 | P3 | `computer_kb/records/relations/vasp_md_thermostat_chain.md` |
| `concepts/vasp_adsorption_energy_chain.md` | VASP 吸附能+CHE 自由能图参数链 | P1 | `computer_kb/records/relations/vasp_adsorption_energy_chain.md` |
| `concepts/vasp_electronic_structure_chain.md` | VASP DOS/PDOS/d-band/Bader 参数链 | P2 | `computer_kb/records/relations/vasp_electronic_structure_chain.md` |
| `concepts/vasp_vaspsol_implicit_solvent.md` | VASPsol 隐式溶剂 | P1 | `computer_kb/records/templates/vasp_vaspsol_implicit_solvent.md` |
| `concepts/lammps_md_setup_chain.md` | LAMMPS MD 前置命令链 | P4 | `computer_kb/records/relations/lammps_md_setup_chain.md` |
| `concepts/lammps_md_fix_thermostat_chain.md` | LAMMPS thermostat/integration 链 | P4 | `computer_kb/records/relations/lammps_md_fix_thermostat_chain.md` |

## 报错页

| 页面 | 类型 | 状态 | 追溯 records |
|---|---|---|---|
| `errors/lammps_lost_atoms.md` | LAMMPS Lost atoms | Seed9 已建 | `computer_kb/records/errors.md` |
| `errors/lammps_non_numeric_instability.md` | LAMMPS non-numeric instability | Seed9 已建 | `computer_kb/records/errors.md` |
| `errors/lammps_out_of_range_atoms.md` | LAMMPS out-of-range atoms | Seed9 已建 | `computer_kb/records/errors.md` |
| `errors/lammps_unrecognized_style_package.md` | LAMMPS unrecognized style/package | Seed9 已建 | `computer_kb/records/errors.md` |
| `errors/lammps_energy_stress_not_tallied.md` | LAMMPS energy/stress not tallied | Seed9 已建 | `computer_kb/records/errors.md` |
| `errors/vasp_scf_not_converge.md` | VASP SCF 不收敛 | P1 skeleton | `computer_kb/records/error_chains/vasp_scf_not_converge.md` |
| `errors/vasp_neb_not_converge.md` | VASP NEB 不收敛 | P2 skeleton | `computer_kb/records/error_chains/vasp_neb_not_converge.md` |
| `errors/vasp_md_atom_explosion.md` | AIMD 离子步爆炸 | P3 skeleton | `computer_kb/records/error_chains/vasp_md_atom_explosion.md` |
| `errors/vasp_adsorption_energy_abnormal.md` | 吸附能异常 | P1 skeleton | `computer_kb/records/error_chains/vasp_adsorption_energy_abnormal.md` |
| `errors/vasp_dos_dband_abnormal.md` | DOS/d-band 异常 | P2 skeleton | `computer_kb/records/error_chains/vasp_dos_dband_abnormal.md` |
| `errors/lammps_md_energy_nan.md` | MD 能量 NaN/发散 | P4 skeleton | `computer_kb/records/error_chains/lammps_md_energy_nan.md` |
| `errors/aimd_temperature_runaway.md` | VASP AIMD 温度失控与 blowup | Seed11 local_verified | `computer_kb/records/errors.md` |

新增页面时必须按 `computer_kb/SCHEMA.md` 和 `computer_kb/REVIEWER.md` 保持可追溯。
## Obsidian Links

**Concepts（12）**

- [[vasp_aimd_md_parameters]]
- [[vasp_scf_accuracy_chain]]
- [[vasp_neb_chain]]
- [[vasp_adsorption_energy_chain]]
- [[vasp_electronic_structure_chain]]
- [[vasp_dft_plus_u_guide]]
- [[vasp_md_thermostat_guide]]
- [[vasp_vaspsol_implicit_solvent]]
- [[lammps_command_index]]
- [[lammps_md_basics]]
- [[lammps_md_setup_chain]]
- [[lammps_md_fix_thermostat_chain]]
**Errors（12）**

- [[vasp_scf_not_converge]]
- [[vasp_neb_not_converge]]
- [[vasp_md_atom_explosion]]
- [[vasp_adsorption_energy_abnormal]]
- [[vasp_dos_dband_abnormal]]
- [[aimd_temperature_runaway]]
- [[lammps_lost_atoms]]
- [[lammps_non_numeric_instability]]
- [[lammps_out_of_range_atoms]]
- [[lammps_unrecognized_style_package]]
- [[lammps_energy_stress_not_tallied]]
- [[lammps_md_energy_nan]]

**Workflows（0）**

当前公开分发不包含个人研究 workflow 页面。
