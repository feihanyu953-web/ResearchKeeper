---
software: VASP
category: error
status: seed
seed: "P2"
records:
  - error_chains/vasp_neb_not_converge.md
  - errors.md  # vasp-error-neb-not-converge-0002
---

# NEB 不收敛排查

> 事实追溯到 `computer_kb/records/error_chains/vasp_neb_not_converge.md`。

## 症状

NEB 路径不平滑或多张图力未收敛到 EDIFFG。

## 排查

### 1. 初始路径是否合理
检查 POSCAR/00-0N 中 IS→FS 过渡是否平滑。不平滑→重做 nebmake。

### 2. SPRING 是否太弱
OUTCAR 中各图位移过大→SPRING=-5.0→-8.0。

### 3. 某插点 SCF 先崩
检查各 OUTCAR 是否有 "reached required accuracy"。

## 不要做

EDIFFG=-0.1 强制早停→TS 能量不可信。

## 关联

- [[vasp_neb_chain]] — NEB 参数链
- [[vasp_scf_accuracy_chain]] — SCF 精度链
