---
software: VASP
category: concept
status: seed
seed: "P1"
records:
  - relations/vasp_scf_accuracy_chain.md
---

# VASP SCF 精度金字塔

> 展示层概念页。事实追溯到 `computer_kb/records/relations/vasp_scf_accuracy_chain.md`。

## 金字塔结构

```
        EDIFF (收敛标准)
        /    \
     ALGO    AMIX/BMIX
      /        \
  ADDGRID    LASPH (力精度)
      \        /
    ENCUT ← → PREC (基组完整性)
        |
      LREAL (投影方式)
```

## 关键关系

| 参数 | 角色 | 与谁联动 |
|---|---|---|
| ENCUT | 基组大小 | PREC 可覆盖; 与 EDIFF 共同决定精度 |
| PREC | 精度预设 | 覆盖 ENCUT/ADDGRID/LREAL 默认值 |
| EDIFF | 电子步收敛 | ENCUT 够了再收紧才有意义 |
| ALGO | 迭代算法 | 不收敛时升级到 All |
| AMIX | 电荷混合 | 与 ALGO 联动; d 电子体系需 < 0.2 |
| ADDGRID | Finer augmentation grid | 与 LASPH 互补保证力精度 |
| LASPH | 非球对称 PAW | 与 ADDGRID 互补 |
| LREAL | 投影方式 | 大体系 Auto; 小体系 .FALSE. |
| ISMEAR/SIGMA | 展宽 | 金属: Gaussian (0) 或 MP (1/2); 绝缘体: Gaussian (0)+小 SIGMA 或 tetrahedron (-5) |

## 适用于 Pt/水界面的推荐起点

| 参数 | 推荐值 | 理由 |
|---|---|---|
| ENCUT | 400 | O ENMAX~300 × 1.3 |
| PREC | Normal | 手动控制精度 |
| EDIFF | 1E-5 | 力敏感 → 不能太松 |
| ALGO | Normal | 起步; 不收敛→All |
| AMIX | 0.2 | d 电子 + 水 → 低混合 |
| ADDGRID | .TRUE. | 力精度 |
| LASPH | .TRUE. | 力精度 |
| LREAL | Auto | 超胞 ~15Å |
| ISMEAR | 0 | 金属 |
| SIGMA | 0.1 | 平衡收敛与准确性 |

## 关联资源

- [[vasp_aimd_md_parameters]] — VASP AIMD/MD 参数组
- [[vasp_dft_plus_u_guide]] — DFT+U 选取指南
