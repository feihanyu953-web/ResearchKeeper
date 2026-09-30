# VASP 吸附中间体 + CHE 自由能图模板

> record_type: template | scope: single_software | software: [VASP]

~~~yaml
record_id: tmpl-vasp-adsorbate-che-0004
record_type: template
scope: single_software
software:
  - VASP
topic: "金属 slab 上吸附中间体能量计算 + CHE 自由能图"
source_type: official_doc
source_ref: "https://www.vasp.at/wiki/IDIPOL"
version_or_doc_date: "VASP 6.x; checked 2026-05-24"
claim: >
  Pt/Ni/Co 类金属 slab 上 C/N/O/H 吸附质的吸附能计算 + CHE 自由能台阶图。
  三步走: 清洁 slab → 吸附中间体弛豫 → 气体分子参考态 → CHE 校正。
evidence_level: should
confidence: local_unverified
related_wiki:
  - computer_kb/wiki/concepts/vasp_adsorption_energy_chain.md
  - computer_kb/wiki/concepts/vasp_scf_accuracy_chain.md
related_records:
  - vasp-param-idipol-0159
  - vasp-param-ldipol-0230
  - vasp-param-isif-0180
  - vasp-param-ismear-0181
  - rel-vasp-adsorption-energy-chain-0005
  - rel-vasp-scf-precision-chain-0001
note: >
  Skeleton 级别模板。具体吸附位点 (top/bridge/hollow/fcc/hcp) 遍历策略和吸附质初始构型
  需用户补充。CHE 自由能校正的 ZPE/TS 值需从振动频率计算获得 (见 tmpl-vasp-vibrational-freq-0003)。
last_checked: 2026-05-24

applies_to:
  systems: [metal_slab, adsorbate_on_metal]
  metals: [Pt, Ni, Co, Cu, Pd, Ir, Ru, Rh, alloys]
  adsorbates: ["*H", "*O", "*OH", "*OOH", "*CO", "*COOH", "*HCOO", "*CHO", "*CH2O", "*N2", "*NH", "*NH2", "*NO", "*NOH"]
  tasks: [adsorption_energy, free_energy_diagram, che_thermochemistry]

hardware_profile: {}

prerequisites:
  - step: "Bulk 优化已完成 (获得 equilibrium lattice constant)"
    why: "Slab 的 in-plane lattice 来自 bulk"

  - step: "清洁 slab 优化完成 (ISIF=2/3)"
    why: "吸附能的三部分之一"

  - step: "确认 slab 模型: 层数、底层固定层数、真空层 ≥15 Å"
    why: "避免 slab-slab 周期相互作用影响吸附能"

parameters:
  - name: ENCUT
    value: 400
    record: vasp-param-encut-0116
    reasoning: "O 含体系 ENMAX×1.3; 三部分能量统一使用同一 ENCUT"
    source_type: official_doc
    source_ref: "https://www.vasp.at/wiki/ENCUT"

  - name: PREC
    value: Normal
    record: vasp-param-prec-0530
    reasoning: "手动控 ENCUT 而非被 Accurate 覆盖"
    source_type: official_doc
    source_ref: "https://www.vasp.at/wiki/PREC"

  - name: EDIFF
    value: 1E-5
    record: vasp-param-ediff-0053
    reasoning: "配合 ENCUT=400; 吸附能差 < 0.01 eV 需要 EDIFF≤1E-5"
    source_type: official_doc
    source_ref: "https://www.vasp.at/wiki/EDIFF"

  - name: ISMEAR
    value: 0
    record: vasp-param-ismear-0181
    reasoning: "Gaussian smearing for metal slab total energy"
    source_type: official_doc
    source_ref: "https://www.vasp.at/wiki/ISMEAR"

  - name: SIGMA
    value: 0.1
    record: vasp-param-sigma-0554
    reasoning: "0.1 eV for metal slabs ~100 atoms"
    source_type: official_doc
    source_ref: "https://www.vasp.at/wiki/SIGMA"

  - name: IDIPOL
    value: 3
    record: vasp-param-idipol-0159
    reasoning: "单侧吸附 slab 必开偶极校正; 全方向 (3) 最安全"
    source_type: official_doc
    source_ref: "https://www.vasp.at/wiki/IDIPOL"

  - name: LDIPOL
    value: ".TRUE."
    record: vasp-param-ldipol-0230
    reasoning: "配合 IDIPOL=3"
    source_type: official_doc
    source_ref: "https://www.vasp.at/wiki/LDIPOL"

  - name: ISIF
    value: 2
    record: vasp-param-isif-0180
    reasoning: "吸附质弛豫 + 底层固定; cell 不变"
    source_type: official_doc
    source_ref: "https://www.vasp.at/wiki/ISIF"

  - name: IBRION
    value: 2
    record: vasp-param-ibrion-0154
    reasoning: "共轭梯度弛豫 (吸附质到局部极小)"
    source_type: official_doc
    source_ref: "https://www.vasp.at/wiki/IBRION"

  - name: NSW
    value: 100
    record: vasp-param-nsw-0485
    reasoning: "吸附质弛豫 ~50 步通常收敛; 100 安全"
    source_type: official_doc
    source_ref: "https://www.vasp.at/wiki/NSW"

  - name: EDIFFG
    value: -0.03
    record: vasp-param-ediffg-0054
    reasoning: "0.03 eV/Å 力收敛标准 for 吸附质弛豫"
    source_type: official_doc
    source_ref: "https://www.vasp.at/wiki/EDIFFG"

  - name: ADDGRID
    value: ".TRUE."
    record: vasp-param-addgrid-0001
    reasoning: "力敏感 + d 电子金属; 保证弛豫后的结构到位"
    source_type: official_doc
    source_ref: "https://www.vasp.at/wiki/ADDGRID"

  - name: LASPH
    value: ".TRUE."
    record: vasp-param-lasph-0211
    reasoning: "与 ADDGRID 互补; 力方向性精度"
    source_type: official_doc
    source_ref: "https://www.vasp.at/wiki/LASPH"

  - name: ISYM
    value: 0
    record: vasp-param-isym-0184
    reasoning: "吸附质弛豫时关对称性 (让吸附质自由移动)"
    source_type: official_doc
    source_ref: "https://www.vasp.at/wiki/ISYM"

  - name: IVDW
    value: 11
    record: vasp-param-ivdw-0185
    reasoning: "D3BJ 色散校正——含 C/O 大吸附质的范德华作用不可忽略"
    source_type: official_doc
    source_ref: "https://www.vasp.at/wiki/IVDW"

generated_incar: |
  # VASP Slab + Adsorbate | CHE free energy diagram
  ENCUT    = 400
  PREC     = Normal
  EDIFF    = 1E-5
  ISMEAR   = 0
  SIGMA    = 0.1
  IDIPOL   = 3
  LDIPOL   = .TRUE.
  ISIF     = 2
  IBRION   = 2
  NSW      = 100
  EDIFFG   = -0.03
  ADDGRID  = .TRUE.
  LASPH    = .TRUE.
  ISYM     = 0
  IVDW     = 11

# Gas-phase molecule reference:
# Same ENCUT/PREC/EDIFF
# ISMEAR=0; SIGMA=0.001 (molecule-like)
# IBRION=2; NSW=50
# 15x15x15 Å box; Gamma-only k-points

critical_gotchas:
  - symptom: "E_slab+ads − E_slab − E_gas 三部分能量不对应"
    cause: "ENCUT/PREC/k-points 不一致"
    fix: "统一所有三个计算的 INCAR (除 ISMEAR/SIGMA)"
    reference: rel-vasp-adsorption-energy-chain-0005
  - symptom: "吸附能随 slab 层数漂移 (>0.1 eV)"
    cause: "底层固定不够或少层 slab 未收敛"
    fix: "固定 ≥2 底层; slab ≥4 layers for Pt(111)"
  - symptom: "CHE 自由能图与实验 overpotential 差 >0.3V"
    cause: "ZPE/TS 校正项缺失或使用了不一致的气相参考"
    fix: "从振动频率算 ZPE; 用 NIST/JANAF 气相熵; 检查溶剂校正"

success_criteria:
  - check: "每个中间体弛豫 EDIFFG=−0.03 力收敛"
  - check: "三部分 ENCUT 一致"
  - check: "清洁 slab 层间距 ≈ bulk reference (Pt: 2.27 Å)"
  - check: "CHE 台阶图离起始步 monotonic; 无负斜率 (违反物理)"
  - check: "吸附能绝对值 < 5 eV (超出需检查是否化学吸附变解离)"
~~~
