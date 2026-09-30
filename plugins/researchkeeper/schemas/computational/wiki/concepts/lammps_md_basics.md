---
software: LAMMPS
category: concept
status: seed
seed: 3
records: lammps_md.md
---

# LAMMPS MD 基础命令组

> 展示层页面。关键事实追溯到 `computer_kb/records/lammps_md.md`；各记录保留可公开访问的官方来源 URL。

## 1. 最小 MD 输入脚本路线

LAMMPS MD 脚本通常可以按下面的骨架理解：

| 阶段 | 命令 | records |
|---|---|---|
| 初始化物理单位与原子数据模型 | `units`; `atom_style`; `dimension`; `boundary` | `lammps-md-cmd-units-0001`; `lammps-md-cmd-atom-style-0002`; `lammps-md-cmd-dimension-0004`; `lammps-md-cmd-boundary-0003` |
| 建立体系 | `read_data` 或 `create_box` 路线 | `lammps-md-cmd-read-data-0005`; `lammps-md-cmd-create-box-0006`; `lammps-md-format-data-file-0025` |
| 势函数与质量 | `mass`; `pair_style`; `pair_coeff` | `lammps-md-cmd-mass-0007`; `lammps-md-cmd-pair-style-0008`; `lammps-md-cmd-pair-coeff-0009` |
| 邻居表 | `neighbor`; `neigh_modify` | `lammps-md-cmd-neighbor-0010`; `lammps-md-cmd-neigh-modify-0011` |
| 时间与初速度 | `timestep`; `velocity` | `lammps-md-cmd-timestep-0012`; `lammps-md-cmd-velocity-0013` |
| 积分与温压控制 | `fix nve`; `fix nvt/npt/nph`; `fix langevin` | `lammps-md-cmd-fix-nve-0014`; `lammps-md-cmd-fix-nvt-npt-nph-0015`; `lammps-md-cmd-fix-langevin-0016` |
| 输出监控 | `thermo`; `thermo_style`; `dump`; `dump_modify` | `lammps-md-cmd-thermo-0017`; `lammps-md-cmd-thermo-style-0018`; `lammps-md-cmd-dump-0019`; `lammps-md-cmd-dump-modify-0020` |
| 运行与保存 | `minimize`; `run`; `reset_timestep`; `write_data` | `lammps-md-cmd-minimize-0022`; `lammps-md-cmd-run-0021`; `lammps-md-cmd-reset-timestep-0023`; `lammps-md-cmd-write-data-0024` |

这个页面只沉淀 LAMMPS 官方命令层知识，命令级 `pair_style` 细节见官方文档。

## 2. 初始化不是装饰项

| 命令 | 为什么重要 | records |
|---|---|---|
| `units` | 决定时间、能量、距离、压力、温度等物理量的单位；直接影响 `timestep`、速度、势参数和 damping 常数解释 | `lammps-md-cmd-units-0001` |
| `atom_style` | 决定每个原子需要哪些属性；必须和 data file、拓扑、势函数需求一致 | `lammps-md-cmd-atom-style-0002` |
| `boundary` | 决定周期/非周期边界；会改变压力、表面模型和 atom loss 行为 | `lammps-md-cmd-boundary-0003` |
| `dimension` | 区分 2D/3D 模型；绝大多数真实材料 MD 是 3D | `lammps-md-cmd-dimension-0004` |

不要把 `units metal` 下的 timestep、damping 常数或势参数直接搬到 `units real`，反过来也一样。

## 3. 读结构与势函数

| 命令 / 文件 | 检查点 | records |
|---|---|---|
| `read_data` | data file 的 header、atom type、box、Atoms section、Coeffs section 是否和 `atom_style`/势函数一致 | `lammps-md-cmd-read-data-0005`; `lammps-md-format-data-file-0025` |
| `create_box` | 如果不是读 data file，要确认 region、atom type 数和后续建原子流程 | `lammps-md-cmd-create-box-0006` |
| `mass` | 检查质量是否由 data file、命令或势函数机制提供 | `lammps-md-cmd-mass-0007` |
| `pair_style` | 选定 interatomic potential 类型 | `lammps-md-cmd-pair-style-0008` |
| `pair_coeff` | 检查 atom type 映射、模型文件、元素顺序、参数单位 | `lammps-md-cmd-pair-coeff-0009` |

`pair_style` 和 `pair_coeff` 是一组，不能只看其中一个。很多真实错误不是脚本语法错，而是 atom type 到元素/模型的映射错。

## 4. 邻居表与时间步

| 命令 | 检查点 | records |
|---|---|---|
| `neighbor` | skin 太小可能漏相互作用，太大可能慢 | `lammps-md-cmd-neighbor-0010` |
| `neigh_modify` | rebuild 频率、delay/every/check 设置要和体系速度、温度、时间步匹配 | `lammps-md-cmd-neigh-modify-0011` |
| `timestep` | 物理时间单位由 `units` 决定；`run steps × timestep` 才是轨迹名义时长 | `lammps-md-cmd-timestep-0012`; `lammps-md-cmd-run-0021` |

排查 lost atoms、能量爆炸、温度异常时，优先一起看 `timestep`、初始结构重叠、neighbor/rebuild 设置和势函数映射。

## 5. 积分与 thermostat/barostat

| 目标 | 命令 | records |
|---|---|---|
| NVE 积分 | `fix nve` | `lammps-md-cmd-fix-nve-0014` |
| Nose-Hoover NVT/NPT/NPH | `fix nvt`; `fix npt`; `fix nph` | `lammps-md-cmd-fix-nvt-npt-nph-0015` |
| Langevin thermostat | `fix langevin` 通常配合积分 fix，例如 `fix nve` | `lammps-md-cmd-fix-langevin-0016`; `lammps-md-cmd-fix-nve-0014` |
| 初速度 | `velocity` | `lammps-md-cmd-velocity-0013` |

常见边界：`fix langevin` 加的是随机/阻尼 thermostat forces，不应把它当成完整位置积分器；通常还要有 `fix nve` 这类积分 fix。`fix npt` 的压力控制也必须和边界、box 自由度、体系物理问题匹配。

## 6. 输出与可复现性

| 命令 | 用途 | records |
|---|---|---|
| `thermo` | 控制 log 里热力学信息输出频率 | `lammps-md-cmd-thermo-0017` |
| `thermo_style` | 决定输出哪些量，例如温度、压力、能量、体积、box 尺寸 | `lammps-md-cmd-thermo-style-0018` |
| `dump` | 输出轨迹/原子级数据 | `lammps-md-cmd-dump-0019` |
| `dump_modify` | 调整 dump，例如元素名、排序、wrap/unwrap 等 | `lammps-md-cmd-dump-modify-0020` |
| `reset_timestep` | 改变 timestep 编号，常用于 production 前归零 | `lammps-md-cmd-reset-timestep-0023` |
| `write_data` | 保存当前结构/拓扑到 data file | `lammps-md-cmd-write-data-0024` |

如果目标是扩散、RDF、界面水取向等分析，dump 字段不能只输出 `x y z`。是否需要 `vx vy vz`、`fx fy fz`、image flags、element label，要按后处理目标提前定。

## 7. 最小审查清单

回答 LAMMPS MD 设置问题时，至少检查：

1. `units` 与势函数文件、时间步、thermostat damping 是否一致。
2. `atom_style` 与 data file 是否一致。
3. `pair_style` / `pair_coeff` 的 atom type 或元素映射是否明确。
4. 是否存在一个真正的时间积分 fix。
5. thermostat/barostat 是否和目标 ensemble 一致。
6. `run × timestep` 是否给出足够的物理时间。
7. `thermo_style` 与 `dump` 是否支持后续诊断和分析。
## Obsidian Links

- [[lammps_command_index]]


- [[lammps_lost_atoms]]
- [[lammps_energy_stress_not_tallied]] — energy/stress 未统计报错
- [[lammps_non_numeric_instability]]
- [[lammps_out_of_range_atoms]]

