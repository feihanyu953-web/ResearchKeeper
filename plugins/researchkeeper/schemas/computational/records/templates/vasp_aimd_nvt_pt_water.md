# VASP AIMD NVT 采样模板 (Pt/水界面)

> record_type: template | scope: single_software | software: [VASP]

~~~yaml
record_id: tmpl-vasp-aimd-nvt-pt-water-0001
record_type: template
scope: single_software
software:
  - VASP
topic: "Pt(111)/水界面 AIMD NVT 采样"
source_type: official_doc
source_ref: "https://www.vasp.at/wiki/Category:Molecular_dynamics"
version_or_doc_date: "VASP 6.x; checked 2026-05-24"
claim: >
  Pt(111)/水界面 AIMD NVT 采样的 VASP INCAR 模板。
  覆盖 thermostat/ensemble、SCF 精度、输出控制。
evidence_level: should
confidence: local_unverified
related_wiki:
  - computer_kb/wiki/concepts/vasp_aimd_md_parameters.md
  - computer_kb/wiki/concepts/vasp_scf_accuracy_chain.md
related_records:
  - vasp-md-param-ibrion-0001
  - vasp-md-param-mdalgo-0006
  - vasp-md-param-isif-0017
  - vasp-md-param-potim-0003
  - vasp-md-param-nsw-0002
  - vasp-md-param-tebeg-0004
  - vasp-md-param-langevin-gamma-0009
  - rel-vasp-scf-precision-chain-0001
note: >
  模板参数基于领域经验，待目标运行环境完成 AIMD 验证后升级 confidence 为 local_verified 和 source_type 为 local_verified。
  当前 confidence: local_unverified。
last_checked: 2026-05-24

applies_to:
  systems: [metal_water_interface, metal_ion_water]
  metals: [Pt, Ni, Co, Cu, Pd, Ir, Ru, alloys]
  tasks: [aimd_sampling]
  water_model: [explicit_solvent, liquid_water, interfacial_water]
  temperature: [300-400 K]

hardware_profile: {}

prerequisites:
  - step: "Slab 几何优化已完成"
    why: "AIMD 需要从优化后的结构出发"
  - step: "确认超胞尺寸足够容纳水层 + 真空层"
    why: "Pt(111) 3×3 或 4×4 超胞，真空层 ≥ 15 Å"
  - step: "确认 POTCAR 对应元素 (Pt_pv, O, H)"
    why: "Pt_pv 包含 d 电子; O 的 ENMAX ~300 eV → ENCUT ≥ 400"

parameters:
  - name: IBRION
    value: 0
    record: vasp-md-param-ibrion-0001
    reasoning: "MD 模式"
    source_type: official_doc
    source_ref: "https://www.vasp.at/wiki/IBRION"

  - name: MDALGO
    value: 3
    record: vasp-md-param-mdalgo-0006
    reasoning: "Langevin NVT——随机热浴适合液体界面，避免 Nosé-Hoover 对水高频模的遍历性问题"
    source_type: official_doc
    source_ref: "https://www.vasp.at/wiki/MDALGO"

  - name: ISIF
    value: 2
    record: vasp-md-param-isif-0017
    reasoning: "固定 cell 体积; Langevin NVT 要求 ISIF ≤ 2"
    source_type: official_doc
    source_ref: "https://www.vasp.at/wiki/ISIF"
    constraint: "必须 ≤ 2 when MDALGO=3 (NVT)"

  - name: LANGEVIN_GAMMA
    value: "{H: 10.0, O: 5.0, Pt: 1.0}"
    record: vasp-md-param-langevin-gamma-0009
    reasoning: "元素特异的摩擦系数; 轻元素 H 需更强耦合 (10 ps⁻¹)"
    source_type: official_doc
    source_ref: "https://www.vasp.at/wiki/LANGEVIN_GAMMA"
    constraint: "每个元素一个值，单位为 ps⁻¹"

  - name: POTIM
    value: 1.0
    record: vasp-md-param-potim-0003
    reasoning: "1 fs 对含 H 体系在 T ≤ 400K 安全"
    source_type: official_doc
    source_ref: "https://www.vasp.at/wiki/POTIM"
    constraint: "验证: 前 100 步最大离子步位移 < 0.1 Å; 超则减半至 0.5"

  - name: NSW
    value: 5000
    record: vasp-md-param-nsw-0002
    reasoning: "5 ps at 1 fs; 最小有意义 RDF 需要 ≥ 2 ps"
    source_type: official_doc
    source_ref: "https://www.vasp.at/wiki/NSW"

  - name: TEBEG
    value: 330
    record: vasp-md-param-tebeg-0004
    reasoning: "~330 K 室温液态水; ±20 K 按目标调整"
    source_type: official_doc
    source_ref: "https://www.vasp.at/wiki/TEBEG"

  - name: ENCUT
    value: 400
    record: vasp-param-encut-0116
    reasoning: "30% above ENMAX of O (~300 eV for PBE POTCAR)"
    source_type: official_doc
    source_ref: "https://www.vasp.at/wiki/ENCUT"

  - name: PREC
    value: Normal
    record: vasp-param-prec-0530
    reasoning: "Normal + 手动 ENCUT=400 给出可预测的基组; Accurate 会覆盖 ENCUT"
    source_type: official_doc
    source_ref: "https://www.vasp.at/wiki/PREC"

  - name: EDIFF
    value: 1E-5
    record: vasp-param-ediff-0053
    reasoning: "配合 ENCUT=400 的合理精度"
    source_type: official_doc
    source_ref: "https://www.vasp.at/wiki/EDIFF"

  - name: ADDGRID
    value: ".TRUE."
    record: vasp-param-addgrid-0001
    reasoning: "力准确对 AIMD 采样至关重要; Pt 是 5d TM 需细网格"
    source_type: official_doc
    source_ref: "https://www.vasp.at/wiki/ADDGRID"

  - name: LASPH
    value: ".TRUE."
    record: vasp-param-lasph-0211
    reasoning: "与 ADDGRID 互补保证 PAW 球内力方向性精度"
    source_type: official_doc
    source_ref: "https://www.vasp.at/wiki/LASPH"

  - name: LREAL
    value: Auto
    record: vasp-param-lreal-0296
    reasoning: "大超胞 (~15Å) 用实空间投影加速"
    source_type: official_doc
    source_ref: "https://www.vasp.at/wiki/LREAL"

  - name: ALGO
    value: Normal
    record: vasp-param-algo-0007
    reasoning: "稳健的默认算法; 不收敛时升级到 All"
    source_type: official_doc
    source_ref: "https://www.vasp.at/wiki/ALGO"

  - name: ISMEAR
    value: 0
    record: vasp-param-ismear-0181
    reasoning: "Gaussian smearing for MD of metallic systems; SIGMA 配合"
    source_type: official_doc
    source_ref: "https://www.vasp.at/wiki/ISMEAR"

  - name: SIGMA
    value: 0.1
    record: vasp-param-sigma-0554
    reasoning: "0.1 eV smearing 适合金属 slab + MD"
    source_type: official_doc
    source_ref: "https://www.vasp.at/wiki/SIGMA"

  - name: NELM
    value: 60
    record: vasp-param-nelm-0451
    reasoning: "AIMD 每步默认电子步上限"
    source_type: official_doc
    source_ref: "https://www.vasp.at/wiki/NELM"

  - name: RANDOM_SEED
    value: "基于系统时钟"
    record: vasp-md-param-random-seed-0027
    reasoning: "MD 初速度随机性"
    source_type: official_doc
    source_ref: "https://www.vasp.at/wiki/RANDOM_SEED"

generated_incar: |
  # VASP AIMD NVT | Pt(111)/water
  IBRION   = 0
  MDALGO   = 3
  ISIF     = 2
  LANGEVIN_GAMMA = 10.0 5.0 1.0
  POTIM    = 1.0
  NSW      = 5000
  TEBEG    = 330
  
  ENCUT    = 400
  PREC     = Normal
  EDIFF    = 1E-5
  ADDGRID  = .TRUE.
  LASPH    = .TRUE.
  LREAL    = Auto
  ALGO     = Normal
  ISMEAR   = 0
  SIGMA    = 0.1
  NELM     = 60

critical_gotchas:
  - symptom: "SCF 在 MD 步中不收敛"
    cause: "电子步迭代不足"
    fix: "ALGO=Normal → All; 或 AMIX=0.4→0.2"
    reference: rel-vasp-scf-precision-chain-0001
  - symptom: "离子步爆炸 (max force > 100 eV/Å)"
    cause: "POTIM 过大 或 初始结构不合理"
    fix: "POTIM 减半 (0.5 fs); 检查初始原子间距"
  - symptom: "温度漂移 > ±50 K"
    cause: "LANGEVIN_GAMMA 不合适（仅限已平衡体系的采样阶段微调）"
    fix: "平衡后采样阶段: 调大 H 的 γ (如 10→15); 调小 Pt 的 γ。禁用场景: 经典力场→DFT 过渡热化阶段——该场景加大 γ 会加剧失稳（must+local_verified: vasp-error-aimd-temperature-runaway-0001），须先用 Andersen (MDALGO=1) 热化"
    reference: vasp-error-aimd-temperature-runaway-0001

success_criteria:
  - check: "SCF 每步在 60 次迭代内收敛"
  - check: "温度在目标 ±20 K 内波动 (平衡后)"
  - check: "Pt(111) 层间距 ≈ 2.27 Å (fcc bulk reference)"
  - check: "水 O-H 键长 RDF 第一峰 0.97 ± 0.02 Å"
  - check: "最大离子受力 < 10 eV/Å (无原子爆炸)"
~~~
