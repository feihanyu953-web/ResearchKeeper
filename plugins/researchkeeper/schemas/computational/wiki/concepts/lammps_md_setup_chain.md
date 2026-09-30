---
software: LAMMPS
category: concept
status: seed
seed: "P4"
records:
  - relations/lammps_md_setup_chain.md
---

# LAMMPS MD 前置命令链

> 事实追溯到 `computer_kb/records/relations/lammps_md_setup_chain.md`。

## 命令顺序约束

```
units → atom_style → boundary → read_data → mass → pair_style → pair_coeff
```

units 在最前面——它决定所有后续命令中物理量的解释。

## 关键决策

- **units=metal**: 金属界面水体系（eV/Å/ps/K）
- **atom_style=atomic**: 电荷内含于模型，LAMMPS 侧只需坐标
- **timestep=0.0005 ps (0.5 fs)**: 含 H 水体系安全步长
- **boundary=p p p**: 3D 周期（slab 体系靠真空层隔开）

## 关联

- [[lammps_md_fix_thermostat_chain]] — thermostat/integration 链
- [[lammps_md_energy_nan]] — 能量 NaN 排查
- [[lammps_lost_atoms]] — 丢失原子排查
- [[lammps_non_numeric_instability]] — 数值不稳定排查
