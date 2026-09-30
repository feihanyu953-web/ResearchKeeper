---
software: VASP
category: concept
status: seed
seed: "P3"
records:
  - relations/vasp_md_thermostat_chain.md
---

# VASP MD Thermostat 选择指南

> 事实追溯到 `computer_kb/records/relations/vasp_md_thermostat_chain.md`。

## 六种 MDALGO 对照

| MDALGO | Thermostat | 关键 Companion Tag | 推荐场景 |
|---|---|---|---|
| 1 | Andersen | ANDERSEN_PROB | 基础 NVT, 简单体系 |
| 2 | Nosé-Hoover | SMASS | NVT/NVE, 非遍历性问题少的体系 |
| 3 | Langevin | LANGEVIN_GAMMA | 液体界面 / Pt-水 AIMD（已平衡体系推荐） |
| 4 | Nosé-Hoover chain | NHC_NCHAINS, NHC_PERIOD | 大体系, 避免 NH 遍历性问题 |
| 5 | CSVR (Bussi) | CSVR_PERIOD | 替代 NH, 更好的遍历性 |
| 13 | Multiple Andersen | NSUBSYS, TSUBSYS, PSUBSYS | 多温度区域 |

## Pt/水界面推荐: MDALGO=3 (Langevin)

理由: 液态水有高频 O-H 伸缩模 (~3500 cm⁻¹)，Nosé-Hoover 单链容易遇到遍历性问题。
Langevin 的随机力 + 摩擦力自然处理高频模。

**边界（必须遵守）**：经典力场→DFT AIMD 过渡场景（如 LAMMPS SPC/E 预平衡构型起步）**禁用 Langevin**——初始力尖峰下随机力会加剧失稳（本地验证: 温度失控至 97,000 K, 见 [[aimd_temperature_runaway]] 与 computer_kb/records/errors.md vasp-error-aimd-temperature-runaway-0001）。该场景必须先用 Andersen 热化 (MDALGO=1, ANDERSEN_PROB=0.2) 再切换恒温器（见 computer_kb/records/workflows.md vasp-md-workflow-andersen-cascade-0042）。Langevin 推荐仅适用于已平衡体系。

```fortran
MDALGO = 3
ISIF    = 2
LANGEVIN_GAMMA = 10.0 5.0 1.0  ! H O Pt (ps⁻¹)
```

## ISIF 快速检查

| 目标 | ISIF |
|---|---|
| NVT (固定 cell) | ≤ 2 |
| NpT (灵活 cell) | 3 + LANGEVIN_GAMMA_L + PMASS |

## 关联

- [[vasp_aimd_md_parameters]] — VASP AIMD/MD 参数总览
