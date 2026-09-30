---
software: VASP
category: concept
status: seed
seed: "P1"
records:
  - templates/vasp_vaspsol_implicit_solvent.md
  - records/vasp.md  # vasp-param-lsol-0400
---

# VASPsol 隐式溶剂

> 事实追溯到 `computer_kb/records/templates/vasp_vaspsol_implicit_solvent.md` 和 VASPsol seed records。

## VASPsol 是什么

Hennig group 开发的 VASP patch，用 **Poisson-Boltzmann 连续介质模型**模拟溶剂（水/乙腈/甲醇）对电子结构的影响。

## 核心参数

| 参数 | 水 (默认) | 说明 |
|---|---|---|
| `LSOL` | .TRUE. | 激活隐式溶剂 |
| `EB_K` | 78.4 | Bulk 介电常数 |
| `TAU_K` | 0.0 | 表面张力 (通常保持 0) |
| `NC_K` | 0.0 | 离子浓度截止 (纯水=0) |
| `LAMBDA_D_K` | 3.04 Å | Debye 屏蔽长度 (1M 1:1) |

## 适用场景 vs 限制

| 适用 | 不适用 |
|---|---|
| 初始 screening 溶剂效应 | 第一水合层的 specific H-bond |
| CHE 自由能图溶剂修正 | 界面水取向/网络效应 |
| 偏压/带电界面粗粒度建模 | 取代显式水 AIMD |

## Debye 长度公式

$$\lambda_D (\AA) = \frac{3.04}{\sqrt{c[M]}} \quad \text{(1:1 electrolyte, 298 K)}$$

## 关联

- [[vasp_adsorption_energy_chain]] — CHE + 溶剂化修正
- [[vasp_scf_accuracy_chain]] — LSOL 下 SCF 收敛更困难
