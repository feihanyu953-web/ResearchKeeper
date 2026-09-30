---
software: LAMMPS
category: error
status: seed
seed: "P4"
records:
  - records/error_chains/lammps_md_energy_nan.md
  - records/errors.md  # lammps-error-energy-nan-0007
---

# LAMMPS MD 能量 NaN 排查

> 事实追溯到 `computer_kb/records/error_chains/lammps_md_energy_nan.md`。

## 排查三步

1. **timestep**: 含 H 体系 → 0.5 fs; metal units: `timestep 0.0005`
2. **初始结构**: 最短原子间距 > 0.5 Å
3. **pair_coeff**: potential model 文件存在且可读; 元素顺序与 data 匹配

## 关联

- [[lammps_md_setup_chain]] — 前置命令链
- [[lammps_lost_atoms]] — 丢失原子 (邻居问题)
