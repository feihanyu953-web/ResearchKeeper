---
software: VASP
category: error
status: seed
seed: "P2"
records:
  - records/error_chains/vasp_dos_dband_abnormal.md
  - records/errors.md  # vasp-error-dos-dband-abnormal-0005
---

# VASP DOS/d-band 计算异常排查

> 事实追溯到 `computer_kb/records/error_chains/vasp_dos_dband_abnormal.md`。

## 常见症状

- d-band center 与文献差 >0.2 eV
- PDOS 只有 spd 分解无 dl-m 轨道
- Bader charge 总和 ≠ 总电子数
- E_fermi 位置在 DOS 图中明显错误

## 排查三步

1. **CHGCAR 存在？** non-SCF (ICHARG=11) 前必须先跑 SCF (ICHARG=2)
2. **LORBIT≥10？** → `grep LORBIT INCAR` → LORBIT=11 (完整 lm 分解)
3. **NEDOS 够？** → `grep NEDOS INCAR` → ≥2000 for d-band center

## 关联

- [[vasp_scf_not_converge]] — SCF 不收敛则 CHGCAR 不可用
- [[vasp_electronic_structure_chain]] — DOS/PDOS/d-band 参数链
