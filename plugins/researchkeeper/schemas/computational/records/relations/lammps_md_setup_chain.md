# LAMMPS MD 前置设置命令链：units → atom_style → timestep → fix

> record_type: relation | scope: single_software | software: [LAMMPS]

~~~yaml
record_id: rel-lammps-md-setup-chain-0001
record_type: relation
scope: single_software
software:
  - LAMMPS
topic: "LAMMPS MD 输入脚本前置命令链: units/atom_style/boundary/read_data/timestep/velocity/neighbor 的命令顺序与一致性"
source_type: official_doc
source_ref: "https://docs.lammps.org/units.html"
version_or_doc_date: "LAMMPS 30Mar2026; checked 2026-05-24"
claim: >
  LAMMPS 输入脚本的前置命令有严格顺序约束和单位一致性要求。
  units 决定了 timestep、mass、温度、压力的物理含义。atom_style 决定 per-atom 属性的存储和后续命令可用的属性。
  neighbor 命令控制 Verlet 列表构建——在 fix nvt/npt 中 neighbor 设置直接影响 MD 性能和稳定性。
evidence_level: should
confidence: local_unverified
related_wiki:
  - computer_kb/wiki/concepts/lammps_md_setup_chain.md
related_records:
  - lammps-md-cmd-units-0001
  - lammps-md-cmd-atom-style-0002
  - lammps-md-cmd-boundary-0003
  - lammps-md-cmd-read-data-0005
  - lammps-md-cmd-mass-0007
  - lammps-md-cmd-timestep-0012
  - lammps-md-cmd-velocity-0013
  - lammps-md-cmd-neighbor-0010
  - lammps-md-cmd-neigh-modify-0011
note: "基于 LAMMPS 官方文档。pair_style 相关约束见官方页面。"
last_checked: 2026-05-24

relation_type: prerequisite
relation_basis:
  - official_cross_ref
  - official_category
  - domain_knowledge

parameters:
  - name: units
    role: "全局单位系统——所有后续物理量的解释基准"
    constraint: "metal units for atomistic materials (eV, Å, ps, K, bar)"
    record: lammps-md-cmd-units-0001

  - name: atom_style
    role: "per-atom 属性存储格式——决定后续命令可用哪些原子属性"
    constraint: "atomic for simple systems; charge for ionic/coulomb; full for biomolecular"
    record: lammps-md-cmd-atom-style-0002

  - name: boundary
    role: "周期性边界条件——决定体系维度和盒子类型"
    constraint: "p p p for bulk 3D periodic; p p f for slab (z free)"
    record: lammps-md-cmd-boundary-0003

  - name: read_data
    role: "从 data 文件读取原子坐标、盒子、拓扑、力场参数"
    constraint: "data 文件格式必须与 atom_style 匹配"
    record: lammps-md-cmd-read-data-0005

  - name: mass
    role: "设置原子质量——fix nvt/npt 需要质量做 thermostat/pressure coupling"
    constraint: "metal units: grams/mole; real units: amu"
    record: lammps-md-cmd-mass-0007

  - name: timestep
    role: "MD 时间步长——金属体系推荐 0.5 fs"
    constraint: "metal units: ps; 0.0005 ps = 0.5 fs"
    record: lammps-md-cmd-timestep-0012

  - name: velocity
    role: "初始速度——create 从温度分布产生; set 固定特定原子速度"
    constraint: "create 在 fix nvt/npt 之前调用"
    record: lammps-md-cmd-velocity-0013

  - name: neighbor
    role: "Verlet 邻居列表参数——skin distance + rebuild frequency"
    constraint: "skin ≥ 2.0 Å; neigh_modify every 1 delay 0 for stability"
    record: lammps-md-cmd-neighbor-0010

relation_rules:
  - id: L1
    type: prerequisite
    from: units
    to: "timestep, mass, pair_coeff, velocity"
    detail: "所有带物理单位的后续命令按 units 的解释执行。metal vs real → timestep 数值差 1000×"
    decision: "metallic/界面水体系 → units metal; timestep=0.0005 (0.5 fs)"
    consequence: "units 错误 → 所有物理量量纲全错 → 模拟无意义"

  - id: L2
    type: prerequisite
    from: atom_style
    to: read_data
    detail: "data 文件必须与 atom_style 匹配。如 data 文件有 charges 但 atom_style=atomic → 报错或静默丢弃"
    decision: "atom_style atomic (charges embedded in potential model)"
    consequence: "data 与 atom_style 不匹配 → 报错或电荷被静默丢弃 → 力场错误"

  - id: L3
    type: mutually_constrained
    from: timestep
    to: "fix nvt/npt/nve"
    detail: "timestep 决定了每步位移和温度波动。过大的 timestep + 高频模 (水 O-H) → 能量漂移或原子飞出"
    decision: "含显式水: timestep=0.5 fs; 纯金属固液界面: 0.5-1.0 fs"
    consequence: "timestep 过大 → 高频模能量漂移或原子飞出；过小 → 总步数膨胀"

  - id: L4
    type: requires_companion
    from: neighbor
    to: neigh_modify
    detail: "neighbor 设置 skin distance; neigh_modify 控制 rebuild 策略。MD 中两者需配套"
    decision: "neighbor 2.0 bin; neigh_modify every 1 delay 0 check yes"
    consequence: "skin 太小或 rebuild 不及时 → 邻居列表过期 → 力缺失或错误"

  - id: L5
    type: mutually_constrained
    from: velocity
    to: "fix nvt temperature"
    detail: "velocity create 的温度参数与 fix nvt 的 Tstart/Tstop 应一致——否则第一步产生温度冲激"
    decision: "velocity create 温度 = fix nvt Tstart; 不要在 velocity 中使用过高随机数种子偏离"
    consequence: "两者温度不一致 → 第一步温度冲激 → 能量突变"

failure_signatures:
  - symptom: "LAMMPS 报 'Illegal atom_style command' 在 data 文件读取时"
    likely: "atom_style 与 data 文件不匹配"
  - symptom: "温度第一步剧烈振荡 (> 200 K jump)"
    likely: "velocity create 温度与 fix nvt Tstart 不一致"
  - symptom: "总能量持续漂移 (NVE drift > 1 meV/atom/ps)"
    likely: "timestep 过大 或 neighbor skin 不够"
~~~
