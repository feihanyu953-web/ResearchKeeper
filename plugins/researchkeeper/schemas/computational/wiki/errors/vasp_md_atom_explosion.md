---
software: VASP
category: error
status: seed
seed: "P3"
records:
  - error_chains/vasp_md_atom_explosion.md
  - errors.md  # vasp-error-md-atom-explosion-0003
---

# AIMD 离子步爆炸排查

> 事实追溯到 `computer_kb/records/error_chains/vasp_md_atom_explosion.md`。

## 症状

- 第一步或前几步 OSZICAR 中 T 骤升 (> 1000 K)
- 力 > 100 eV/Å
- OUTCAR 中离子位移 > 0.5 Å/step

## 排查

### 1. 检查初始结构

```python
from ase.io import read
atoms = read("POSCAR")
d = atoms.get_all_distances()
# 找 d < 0.5 Å 的原子对
```

有重叠 → 先 minimize 或重建结构。

### 2. 检查 POTIM

含 H → POTIM ≤ 0.5 fs (POTIM=0.5)
无 H → POTIM ≤ 1.0 fs

### 3. 检查 thermostat

```bash
grep MDALGO INCAR
grep LANGEVIN_GAMMA INCAR  # MDALGO=3 必须
grep SMASS INCAR            # MDALGO=2 必须
```

## 不要做

- 盲目加大 thermostat coupling "镇压"爆炸 → 掩盖根本原因

## 关联

- [[vasp_aimd_md_parameters]]
