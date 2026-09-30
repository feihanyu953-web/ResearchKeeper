# VASP VASPsol 隐式溶剂模板

> record_type: template | scope: single_software | software: [VASP]

~~~yaml
record_id: tmpl-vasp-vaspsol-implicit-0006
record_type: template
scope: single_software
software:
  - VASP
topic: "VASPsol 隐式溶剂 (implicit solvent) 参数设置——界面水/电化学界面"
source_type: official_repo
source_ref: "https://github.com/henniggroup/VASPsol"
version_or_doc_date: "VASPsol 1.0; checked 2026-05-24"
claim: >
  VASPsol 是 VASP 的隐式溶剂扩展 (Hennig group)，用 Poisson-Boltzmann 连续介质模型
  模拟水溶剂对电子结构的影响。适用于 Pt/Ni/Co 界面水体系的初始 screening
  和带偏压的 CHE 计算。注意: VASPsol 是 continuum 模型——不能取代显式水层的 AIMD。
evidence_level: should
confidence: local_unverified
related_wiki:
  - computer_kb/wiki/concepts/vasp_vaspsol_implicit_solvent.md
related_records:
  - vasp-param-lsol-0400
  - vasp-param-eb-k-0401
  - vasp-param-tau-k-0402
  - vasp-param-nc-k-0403
  - vasp-param-lambda-d-k-0404
  - vasp-param-idipol-0159
note: >
  VASPsol 标签不在 VASP Wiki Category:INCAR_tag 标准索引中，属 VASPsol patch 扩展。
  使用前需确认 VASP 编译时已链接 VASPsol (VASP.5.4+ / 6.x 支持)。
  Skeleton 级别; 具体介电常数 (ε_b) 和 Debye 屏蔽长度值需按溶剂体系选择。
last_checked: 2026-05-24

applies_to:
  systems: [metal_water_interface, metal_electrolyte, electrochemical_interface]
  tasks: [implicit_solvent, che_with_solvation, potential_dependent_energy, initial_screening]
  solvents: [water, acetonitrile, methanol]
  metals: [Pt, Ni, Co, Cu, Pd, Ir, Au]

hardware_profile: {}

prerequisites:
  - step: "确认 VASP 编译包含 VASPsol patch"
    why: "LSOL 标签仅在 VASPsol-linked VASP 中有效"
  - step: "已完成 slab 或 slab+adsorbate 的 vacuum SCF 弛豫"
    why: "VASPsol 通常加在已弛豫的结构上做单点能修正"

parameters:
  - name: LSOL
    value: ".TRUE."
    record: vasp-param-lsol-0400
    reasoning: "激活隐式溶剂"
    source_type: official_repo
    source_ref: "https://github.com/henniggroup/VASPsol"

  - name: EB_K
    value: 78.4
    record: vasp-param-eb-k-0401
    reasoning: "水的 bulk 相对介电常数 ε_b=78.4 (298 K); 乙腈=37.5; 甲醇=32.7"
    source_type: official_repo
    source_ref: "https://github.com/henniggroup/VASPsol"

  - name: TAU_K
    value: 0.0
    record: vasp-param-tau-k-0402
    reasoning: "表面张力参数 τ=0 (默认)。非零值引入 cavitation 能量——对带电界面可能有影响但数值不确定"
    source_type: official_repo
    source_ref: "https://github.com/henniggroup/VASPsol"

  - name: NC_K
    value: 0.0
    record: vasp-param-nc-k-0403
    reasoning: "补偿电荷密度截止 (0=自动)。电解质离子浓度建模时设为与离子强度匹配的非零值"
    source_type: official_repo
    source_ref: "https://github.com/henniggroup/VASPsol"

  - name: LAMBDA_D_K
    value: 3.04
    record: vasp-param-lambda-d-k-0404
    reasoning: "Debye 屏蔽长度 (Å)——1:1 电解质 1M ≈ 3.04 Å (水, 298 K)。纯水设大值 (如 10) 或 0 (无屏蔽)"
    source_type: official_repo
    source_ref: "https://github.com/henniggroup/VASPsol"

generated_incar: |
  # VASPsol implicit water solvent
  LSOL        = .TRUE.
  EB_K        = 78.4       # dielectric constant of water
  TAU_K       = 0.0        # surface tension (default)
  NC_K        = 0.0        # ion concentration (0 = pure water)
  LAMBDA_D_K  = 3.04       # Debye screening length (Å)
  # Keep all other slab params: ENCUT, PREC, EDIFF, ISMEAR, SIGMA, IDIPOL

critical_gotchas:
  - symptom: "VASP 报错 'LSOL not recognized'"
    cause: "VASP 未编译 VASPsol patch"
    fix: "重新编译 VASP with VASPsol; 或改用显式水层 AIMD"
  - symptom: "Eb_k 值下的吸附能与实验 hydration energy 差 >0.3 eV"
    cause: "VASPsol 是 continuum 模型——不能捕捉第一水合层的 specific interactions"
    fix: "补充显式水层 AIMD + thermodynamic integration; VASPsol 仅作 screening"
  - symptom: "SCF 在 LSOL=.TRUE. 下更难收敛"
    cause: "溶剂电荷响应对 SC 迭代的阻尼需求更高"
    fix: "ALGO=All; AMIX=0.2→0.1; AMIX_MAG=0.8→0.4; NELM=100"
  - symptom: "LAMBDA_D_K 与 electrolyte 浓度不匹配 → 屏蔽过度/不足"
    cause: "1:1 electrolyte: λ_D (Å) = 3.04/√(c[M])"
    fix: "重新计算 λ_D 匹配实际浓度"

success_criteria:
  - check: "LSOL 生效: OUTCAR 中包含 'VASPsol' 或 'solvation' 相关信息"
  - check: "溶剂化能 (E_solvated − E_vacuum) 数量级合理 (水合能 ~0.1-0.5 eV for small adsorbates)"
  - check: "SCF 在 LSOL=.TRUE. 下收敛 (NELM ≤ 100)"
  - check: "无真空层残留 (VASPsol 填充真空区域——溶剂体在 slab 上方形成连续介质)"
~~~
