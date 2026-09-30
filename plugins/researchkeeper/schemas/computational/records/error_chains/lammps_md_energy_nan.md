# LAMMPS MD 能量 NaN/发散诊断链

> record_type: error_chain | scope: single_software | software: [LAMMPS]

~~~yaml
record_id: errchain-lammps-md-energy-nan-0007
record_type: error_chain
scope: single_software
software:
  - LAMMPS
topic: "LAMMPS MD 中 total energy 突然变为 NaN 或无限大"
source_type: official_doc
source_ref: "https://docs.lammps.org/Errors.html"
version_or_doc_date: "LAMMPS 30Mar2026; checked 2026-05-24"
claim: >
  LAMMPS MD 能量 NaN/Inf 最常见原因: timestep 过大、初始结构重叠、pair_coeff 不合理。
evidence_level: check
confidence: local_unverified
related_wiki:
  - computer_kb/wiki/errors/lammps_md_energy_nan.md
related_records:
  - lammps-error-energy-nan-0007
  - lammps-md-cmd-timestep-0012
  - lammps-md-cmd-pair-style-0008
  - lammps-md-cmd-pair-coeff-0009
  - rel-lammps-md-setup-chain-0001
note: "Skeleton 级别。真实 LAMMPS 的 NaN 通常伴随特定错误信息。待目标运行环境复现后补充 exact_error。"
last_checked: 2026-05-24

exact_error: "ERROR on proc N: Non-numeric atom coord/velocity - simulation unstable (skeleton; adapted from known LAMMPS errors)"

diagnosis_chain:
  - level: 1
    question: "timestep 是否过大？"
    check: "grep timestep in.lammps; 确认单位 (metal: ps; real: fs)"
    action: "metal units 下 0.0005 ps = 0.5 fs; 尝试降至 0.00025"
    root_cause: "timestep 过大 + 轻元素 (H) → 核运动跨越多个势能极小值 → 力爆炸"
  - level: 2
    question: "初始结构中是否有非物理原子重叠 (d < 0.5 Å)？"
    check: "用 ASE/VMD 检查 initial structure 最短原子间距"
    action: "若有过近原子对 → 先 minimize; 或重构初始结构"
    root_cause: "原子重叠 → 第一步力极大 (1e3-1e6 eV/Å) → 速度 → 位移 → 飞散"
  - level: 3
    question: "pair_coeff 参数是否正确？"
    check: "检查 model 文件是否存在; 元素列表与 data 文件是否一致"
    action: "pair_coeff * * <correct_model_path> <correct_element_order>"

parameter_root_cause:
  - parameter: timestep
    issue: "过大 → 动力学不稳定"
    record: lammps-md-cmd-timestep-0012
  - parameter: pair_coeff
    issue: "ML model 路径错误或元素映射错误"
    record: lammps-md-cmd-pair-coeff-0009

relations_involved:
  - rel-lammps-md-setup-chain-0001
fixes:
  - priority: 1
    action: "timestep 减半: 0.0005 → 0.00025 ps (0.5 → 0.25 fs)"
    how: "INCAR/LAMMPS input: timestep 0.00025"
    verified: false
    evidence_status: "domain_knowledge"
  - priority: 2
    action: "先 minimize + short NVE (100 steps) 测试稳定性"
    how: "minimize 1e-4 1e-6 1000 10000; run 100"
    verified: false
    evidence_status: "domain_knowledge; not verified locally"

unsafe_fixes:
  - action: "加 fix langevin 强 damping 压住爆炸——治标不治本"
    why_bad: "过大的 damping 把所有动力学篡改为 overdamped → MD 不是物理的"
  - action: "设置 'thermo_modify lost ignore' 忽略丢失原子"
    why_bad: "丢失原子 = 物理上原子已飞出模拟盒子 = 轨迹无意义; 不可能通过忽略修复"
~~~
