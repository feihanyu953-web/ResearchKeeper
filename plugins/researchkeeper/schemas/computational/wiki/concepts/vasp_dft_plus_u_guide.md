---
software: VASP
category: concept
status: seed
seed: "P2"
records:
  - relations/vasp_dft_plus_u.md
---

# VASP DFT+U 选取指南

> 事实追溯到 `computer_kb/records/relations/vasp_dft_plus_u.md`。

## 什么时候加 +U

| 情况 | 加 U? |
|---|---|
| Ni/Co/Fe/Mn 氧化物/氢氧化物 | 是 (Dudarev LDAUTYPE=2) |
| 金属 Ni/Co/Fe slab | 可选 (U 值一般较小) |
| Pt/Pd/Cu/Au 金属 | 不加 (d band 填满/近满) |

## 领域常用 U_eff (PBE, Dudarev)

| 元素 | U_eff 范围 (eV) | 备注 |
|---|---|---|
| Ni | 3.5-6.0 | 价态/配位依赖大 |
| Co | 3.0-4.0 | |
| Fe | 4.0-5.0 | |
| Mn | 3.5-5.0 | |
| Cu | 4.0-6.0 | CuO 需加, 金属 Cu 可不加 |

> 必须做 U 扫描! 不同体系/泛函的有效 U 不同。

## 最小 INCAR

```
LDAU      = .TRUE.
LDAUTYPE  = 2
LDAUL     = 2 2 -1      # Ni Co O → d d none
LDAUU     = 3.5 3.5 0   # Ni U_eff=3.5, Co U_eff=3.5
LDAUJ     = 1.0 1.0 0   # Dudarev 时 J 对结果影响小
```

## 关联概念

- [[vasp_scf_accuracy_chain]] — SCF 精度金字塔（+U 体系的 SCF 底座）
- [[vasp_electronic_structure_chain]] — DOS/PDOS/d-band 参数链（+U 影响电子结构）
- [[vasp_adsorption_energy_chain]] — 吸附能参数链（氧化物表面常需 +U）
