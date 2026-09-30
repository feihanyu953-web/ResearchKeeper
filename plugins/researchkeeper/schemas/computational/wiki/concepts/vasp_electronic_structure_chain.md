---
software: VASP
category: concept
status: seed
seed: "P2"
records:
  - relations/vasp_electronic_structure_chain.md
  - templates/vasp_dos_pdos_bader.md
---

# VASP 电子结构分析：DOS/PDOS/d-band/Bader

> 事实追溯到 `computer_kb/records/relations/vasp_electronic_structure_chain.md` 和 `computer_kb/records/templates/vasp_dos_pdos_bader.md`。

## 两步法

```
Step 1: SCF static → CHGCAR + LOCPOT
Step 2: ICHARG=11 + LORBIT=11 + NEDOS=2000 → DOSCAR + PROCAR
```

## d-band center

$$\varepsilon_d = \frac{\int E \cdot \rho_d(E) dE}{\int \rho_d(E) dE}$$

- NEDOS=301 → 离散误差 ~0.1 eV
- NEDOS=2000 → <0.01 eV
- VASP 不内建输出 ε_d，需 VASPKIT/pymatgen 后处理

## Bader Charge

- 外部 Bader 程序分析 CHGCAR
- CHGCAR 网格够细 (NGXF/Y/Z ≥ 2×default) 才能保证 Bader 表面平滑
- `LAECHG=.TRUE.` 输出 AECCAR0/1/2 供 all-electron Bader

## Work Function

$$\Phi = E_{vac} - E_{Fermi}$$

- LVTOT=.TRUE. → LOCPOT → z-profile → E_vac
- IDIPOL=3 保证真空能级平坦

## 关联

- [[vasp_scf_accuracy_chain]] — SCF 精度底座
- [[vasp_adsorption_energy_chain]] — 吸附能 → d-band 描述符
- [[vasp_dft_plus_u_guide]] — DFT+U 选取指南
- [[vasp_dos_dband_abnormal]] — DOS/d-band 异常排查
