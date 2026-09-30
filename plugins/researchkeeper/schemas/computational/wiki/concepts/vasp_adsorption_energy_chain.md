---
software: VASP
category: concept
status: seed
seed: "P1"
records:
  - relations/vasp_adsorption_energy_chain.md
  - templates/vasp_adsorbate_free_energy.md
---

# VASP 吸附能计算与 CHE 自由能图参数链

> 事实追溯到 `computer_kb/records/relations/vasp_adsorption_energy_chain.md` 和 `computer_kb/records/templates/vasp_adsorbate_free_energy.md`。

## 三步能量计算

```
E_ads = E_slab+ads − E_slab − E_gas
```

三项必须在**相同计算精度**下求值（ENCUT/PREC/k-points 一致）。

## 偶极校正：为什么必须开

单侧吸附 slab 失去 z 方向镜面对称 → 周期性边界产生虚假电场 → 吸附能系统性偏差 (0.1-0.3 eV)。

```fortran
IDIPOL = 3
LDIPOL = .TRUE.
```

## CHE 自由能校正

$$\Delta G = \Delta E_{DFT} + \Delta ZPE - T\Delta S + \Delta G_{solvation}$$

- $\Delta E_{DFT}$: 三部分能量（统一精度）
- $\Delta ZPE$: 振动频率计算（`IBRION=5`）
- $T\Delta S$: 气相熵（NIST/JANAF 或从振动配分函数）
- $\Delta G_{solvation}$: VASPsol 隐式溶剂修正（可选）

## 关联

- [[vasp_scf_accuracy_chain]] — SCF 精度底座
- [[vasp_neb_chain]] — 过渡态搜索
- [[vasp_vaspsol_implicit_solvent]] — 隐式溶剂
- [[vasp_adsorption_energy_abnormal]] — 吸附能异常排查
