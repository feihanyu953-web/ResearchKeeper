---
software: VASP
category: error
status: seed
seed: "P1"
records:
  - records/error_chains/vasp_adsorption_energy_abnormal.md
  - records/errors.md  # vasp-error-adsorption-energy-abnormal-0004
---

# VASP 吸附能异常排查

> 事实追溯到 `computer_kb/records/error_chains/vasp_adsorption_energy_abnormal.md`。

## 常见症状

- E_ads 与文献差 >0.3 eV
- E_ads 随 slab 层数漂移 (>0.05 eV/layer)
- CHE 自由能图与实验 overpotential 差 >0.3V

## 排查三连

1. **偶极校正**: `grep IDIPOL INCAR` → 不对称 slab 必须 IDIPOL=3 + LDIPOL=.TRUE.
2. **参数一致性**: `diff` 三部分计算的 INCAR/KPOINTS → ENCUT/PREC/k 点必须完全相同
3. **ISMEAR**: 金属 slab 避免 ISMEAR=-3 (固定占据) 与 -5 (tetrahedron)；ISMEAR=-1 (Fermi) 可用于金属但需密集 k 点

## 关联

- [[vasp_scf_not_converge]] — SCF 不收敛常伴随吸附能问题
- [[vasp_adsorption_energy_chain]] — 参数链参考
- [[vasp_neb_not_converge]] — TS 搜索失败也可能来自吸附能不准
