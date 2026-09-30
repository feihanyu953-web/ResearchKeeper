# errors

一页一个典型 error signature。

当前已有 error 页面：

**VASP**

- `vasp_scf_not_converge.md` — SCF 不收敛
- `vasp_neb_not_converge.md` — NEB 不收敛
- `vasp_md_atom_explosion.md` — AIMD 离子步爆炸
- `vasp_adsorption_energy_abnormal.md` — 吸附能异常
- `vasp_dos_dband_abnormal.md` — DOS/d-band 异常
- `aimd_temperature_runaway.md` — AIMD 温度失控与 blowup

**LAMMPS**

- `lammps_lost_atoms.md`
- `lammps_non_numeric_instability.md`
- `lammps_out_of_range_atoms.md`
- `lammps_unrecognized_style_package.md`
- `lammps_energy_stress_not_tallied.md`
- `lammps_md_energy_nan.md` — MD 能量 NaN/发散

这些是官方文档驱动的 error/symptom 路由；真实本地 error log 仍应作为新记录单独入库。

建议格式：

1. 报错原文。
2. 快速判断。
3. 常见原因。
4. 排查顺序。
5. 修复方式和危险修复提醒。
6. 相关 workflow、concept 和 record。

## Obsidian Links

**VASP**

- [[vasp_scf_not_converge]]
- [[vasp_neb_not_converge]]
- [[vasp_md_atom_explosion]]
- [[vasp_adsorption_energy_abnormal]]
- [[vasp_dos_dband_abnormal]]
- [[aimd_temperature_runaway]]

**LAMMPS**

- [[lammps_lost_atoms]]
- [[lammps_non_numeric_instability]]
- [[lammps_out_of_range_atoms]]
- [[lammps_unrecognized_style_package]]
- [[lammps_energy_stress_not_tallied]]
- [[lammps_md_energy_nan]]
