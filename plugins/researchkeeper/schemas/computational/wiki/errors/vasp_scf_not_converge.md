---
software: VASP
category: error
status: seed
seed: "P1"
records:
  - error_chains/vasp_scf_not_converge.md
  - errors.md  # vasp-error-scf-not-converge-0001
---

# VASP SCF 不收敛排查

> 展示层排查教程 (skeleton)。事实追溯到 `computer_kb/records/error_chains/vasp_scf_not_converge.md`。

## 症状

VASP 输出: `WARNING: SCF convergence not achieved within NELM=60 steps`

常见于 Pt/水界面等含 d 电子金属的复杂体系。

## 排查顺序

### 第一步：检查体系

含 Pt/Ni/Co/Fe/Cu + O/H → d 电子体系的电荷密度收敛困难是正常的。

### 第二步：升级算法

```
INCAR: ALGO = All
```

`ALGO=Normal` 不够稳健时升级到 `All`（全对角化）。

### 第三步：降低混合参数

```
INCAR: AMIX = 0.2
INCAR: AMIX_MAG = 0.8
```

d 电子体系电荷密度振荡（charge sloshing）→ 需要更保守的混合。

### 第四步（治标）：增加迭代步数

```
INCAR: NELM = 100
```

注意：这只是增加每步电子步次数上限，不解决收敛困难的根源。

## 不要做的事

- ❌ `ISMEAR=2 + SIGMA=0.5` 强制收敛：entropy error 可能 >50 meV/atom
- ❌ 不管不收敛继续跑 MD：轨迹无物理意义

## 关联资源

- [[vasp_scf_accuracy_chain]] — SCF 精度金字塔
- [[vasp_aimd_md_parameters]] — VASP AIMD/MD 参数组
