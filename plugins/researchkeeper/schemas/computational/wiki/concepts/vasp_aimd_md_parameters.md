---
software: VASP
category: concept
status: seed
seed: 2
records: vasp_md.md
---

# VASP AIMD/MD 参数组

> 展示层页面。关键事实追溯到 `computer_kb/records/vasp_md.md`；各记录保留可公开访问的官方来源 URL。

## 1. 最小路由

VASP 的 AIMD/MD 设置先看三层：

| 问题 | 先查参数 | records |
|---|---|---|
| 这是不是 MD 任务 | `IBRION=0` | `vasp-md-param-ibrion-0001` |
| 轨迹有多长 | `NSW × POTIM` | `vasp-md-param-nsw-0002`; `vasp-md-param-potim-0003` |
| 采样什么 ensemble / thermostat | `MDALGO` + companion tags | `vasp-md-param-mdalgo-0006` |

`NSW × POTIM` 只给名义总时长；是否足够采样仍要看体系、温控方式、平衡段、结构弛豫和后处理目标。

## 2. 温度与初速度

| 用途 | 参数 | records |
|---|---|---|
| 初始温度 | `TEBEG` | `vasp-md-param-tebeg-0004` |
| 最终温度 | `TEEND` | `vasp-md-param-teend-0005` |
| 随机数种子 | `RANDOM_SEED` | `vasp-md-param-random-seed-0027` |
| 速度输出 | `VELOCITY` | `vasp-md-param-velocity-0028` |
| 原子质量 | `POMASS` | `vasp-md-param-pomass-0029` |

如果 `TEEND=TEBEG`，通常表示没有刻意设置温度 ramp。需要可复现的随机初速度或随机 thermostat 行为时，不能只依赖系统时钟默认 seed。

## 3. thermostat / ensemble

| 目标 | 关键参数 | records |
|---|---|---|
| Andersen thermostat | `MDALGO=1`; `ANDERSEN_PROB` | `vasp-md-param-mdalgo-0006`; `vasp-md-param-andersen-prob-0007` |
| Nose-Hoover thermostat | `MDALGO=2`; `SMASS` | `vasp-md-param-mdalgo-0006`; `vasp-md-param-smass-0008` |
| Langevin NVT | `MDALGO=3`; `LANGEVIN_GAMMA`; fixed cell via `ISIF<=2` | `vasp-md-param-langevin-gamma-0009`; `vasp-md-param-isif-0017` |
| Langevin NpT | `MDALGO=3`; `ISIF=3`; `LANGEVIN_GAMMA`; `LANGEVIN_GAMMA_L`; `PMASS`; optional `PSTRESS` | `vasp-md-param-langevin-gamma-0009`; `vasp-md-param-langevin-gamma-l-0010`; `vasp-md-param-pmass-0011`; `vasp-md-param-pstress-0018` |
| Nose-Hoover chain | `MDALGO=4`; `NHC_NCHAINS`; `NHC_PERIOD`; optional integration controls | `vasp-md-param-nhc-nchains-0012`; `vasp-md-param-nhc-period-0015`; `vasp-md-param-nhc-nrespa-0013`; `vasp-md-param-nhc-ns-0014` |
| CSVR | `MDALGO=5`; `CSVR_PERIOD` | `vasp-md-param-csvr-period-0016` |
| Multiple Andersen thermostats | `MDALGO=13`; `NSUBSYS`; `TSUBSYS`; `PSUBSYS` | `vasp-md-param-nsubsys-0020`; `vasp-md-param-tsubsys-0021`; `vasp-md-param-psubsys-0022` |

注意：`MDALGO` 不是孤立参数。每个 thermostat 都有 companion tags；只写 `MDALGO` 而不写对应参数，容易造成“以为自己在做某个 ensemble，实际设置不完整”的问题。

## 4. cell / pressure

| 用途 | 参数 | records |
|---|---|---|
| 是否允许 cell 变化 | `ISIF` | `vasp-md-param-isif-0017` |
| 外压或 stress correction | `PSTRESS` | `vasp-md-param-pstress-0018` |
| 晶格向量选择性约束 | `LATTICE_CONSTRAINTS` | `vasp-md-param-lattice-constraints-0019` |
| 晶格自由度 fictitious mass | `PMASS` | `vasp-md-param-pmass-0011` |

在回答具体计算设置时，`ISIF` 要和 `MDALGO` 一起读。官方 MDALGO 页面说明 Langevin NVT 与 Langevin NpT 的 cell 自由度设置不同。

## 5. 输出与在线分析

| 用途 | 参数 | records |
|---|---|---|
| pair-correlation / DOS 计算间隔 | `NBLOCK` | `vasp-md-param-nblock-0023` |
| 平均 PCDAT/DOSCAR 写出间隔 | `KBLOCK` | `vasp-md-param-kblock-0024` |
| pair-correlation 最大距离 | `APACO` | `vasp-md-param-apaco-0025` |
| pair-correlation bin 数 | `NPACO` | `vasp-md-param-npaco-0026` |

这些参数主要影响输出与在线分析，不等同于 thermostat 或 ensemble 选择。

## 6. 约束与高级采样

| 用途 | 参数 / 文件 | records |
|---|---|---|
| 约束或几何参数监控 | `ICONST` | `vasp-md-param-iconst-0030` |
| 几何参数上/下限 | `VALUE_MAX`; `VALUE_MIN` | `vasp-md-param-value-max-0037`; `vasp-md-param-value-min-0038` |
| Müller-Plathe 方法参与原子类型 | `FMP_ACTIVE` | `vasp-md-param-fmp-active-0035` |
| 温度梯度方向 | `FMP_DIRECTION` | `vasp-md-param-fmp-direction-0036` |
| 交换周期 / slab 数 / 每次交换对数 | `FMP_PERIOD`; `FMP_SNUMBER`; `FMP_SWAPNUM` | `vasp-md-param-fmp-period-0039`; `vasp-md-param-fmp-snumber-0040`; `vasp-md-param-fmp-swapnum-0041` |

FMP 和约束类参数属于高级 MD workflow。没有明确热输运、约束坐标或几何监控目标时，不应把它们当作常规 AIMD 默认项。

## 7. 边界项

| 参数 | 为什么放在 Seed2 | records |
|---|---|---|
| `INTERACTIVE` | VASP 官方 Molecular dynamics 分类列出；与交互式运行有关 | `vasp-md-param-interactive-0031` |
| `IWAVPR` | 官方 MD 分类列出；影响离子步之间波函数/电荷预测 | `vasp-md-param-iwavpr-0032` |
| `LRPAFORCE` | 官方 MD 分类列出；RPA force 专项设置 | `vasp-md-param-lrpaforce-0033` |
| `NFREE` | 官方 MD 分类列出；含义依赖 `IBRION` | `vasp-md-param-nfree-0034` |

这些不是普通 AIMD 入门默认项。实际回答时要根据当前任务判断是否需要展开。
## Obsidian Links


- [[aimd_temperature_runaway]] — AIMD 温度失控与 blowup
- [[vasp_md_atom_explosion]] — AIMD 离子步爆炸排查
- [[vasp_md_thermostat_guide]] — VASP MD thermostat 选择指南


