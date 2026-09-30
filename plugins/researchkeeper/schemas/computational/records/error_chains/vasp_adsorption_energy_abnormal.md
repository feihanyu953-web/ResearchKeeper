# VASP 吸附能异常诊断链 (skeleton)

> record_type: error_chain | scope: single_software | software: [VASP]

~~~yaml
record_id: errchain-vasp-adsorption-energy-abnormal-0004
record_type: error_chain
scope: single_software
software:
  - VASP
topic: "吸附能与文献/预期值差 >0.3 eV 或随 slab 层数漂移"
source_type: official_doc
source_ref: "https://www.vasp.at/wiki/IDIPOL"
version_or_doc_date: "VASP 6.x; checked 2026-05-24"
claim: "吸附能异常常见原因: IDIPOL 未开、三部分能量 ENCUT 不一致、slab 模型不合理、ISMEAR 不当。"
evidence_level: check
confidence: local_unverified
related_wiki:
  - computer_kb/wiki/errors/vasp_adsorption_energy_abnormal.md
related_records:
  - vasp-error-adsorption-energy-abnormal-0004
  - vasp-param-idipol-0159
  - vasp-param-encut-0116
  - vasp-param-ismear-0181
  - rel-vasp-adsorption-energy-chain-0005
note: "Skeleton 级别。吸附能判据依赖文献对比; 绝对误差来源需逐项排查。"
last_checked: 2026-05-24

exact_error: "Computed adsorption energy deviates >0.3 eV from expected/literature value (domain knowledge skeleton)"

diagnosis_chain:
  - level: 1
    question: "偶极校正是否开启 (asymmetric slab)?"
    check: "grep IDIPOL INCAR"
    action: "单侧吸附 slab → IDIPOL=3 + LDIPOL=.TRUE."
    root_cause: "异步 slab 产生虚假电场 → z 方向偶极导致能量艺术性偏移 → E_ads 系统偏差"
  - level: 2
    question: "E_slab+ads、E_slab、E_gas 三部分 ENCUT/PREC/k-points 是否完全一致？"
    check: "diff 三个计算的 INCAR 和 KPOINTS"
    action: "统一三部分 INCAR (除 ISMEAR/SIGMA)"
  - level: 3
    question: "ISMEAR 是否适合此体系？"
    check: "grep ISMEAR INCAR"
    action: "金属 slab → ISMEAR=0/1 (Gaussian/MP)；避免 ISMEAR=-3 (固定占据) 与 -5 (tetrahedron, k 点不足时)；ISMEAR=-1 (Fermi) 可用于金属但需密集 k 点"

parameter_root_cause:
  - parameter: IDIPOL
    issue: "偶极校正未开"
    record: vasp-param-idipol-0159
  - parameter: ENCUT
    issue: "三部分 ENCUT 不一致"
    record: vasp-param-encut-0116
  - parameter: ISMEAR
    issue: "固定占据 (-3) 或 tetrahedron (-5) 用于金属结构优化"
    record: vasp-param-ismear-0181

relations_involved:
  - rel-vasp-adsorption-energy-chain-0005
  - rel-vasp-scf-precision-chain-0001

fixes:
  - priority: 1
    action: "开启偶极校正: IDIPOL=3, LDIPOL=.TRUE."
    how: "INCAR: IDIPOL=3; LDIPOL=.TRUE."
    verified: false
    evidence_status: "domain_knowledge; not verified locally"
  - priority: 2
    action: "统一三部分 ENCUT/PREC/k-points"
    how: "复制同一个 INCAR (只改 ISMEAR/SIGMA for gas molecules)"
    verified: false
    evidence_status: "domain_knowledge; not verified locally"
  - priority: 3
    action: "ISMEAR=0 (Gaussian) + SIGMA=0.1 for metal slab"
    how: "INCAR: ISMEAR=0; SIGMA=0.1"
    verified: false
    evidence_status: "domain_knowledge; not verified locally"

unsafe_fixes:
  - action: "人为调 ENCUT 使吸附能'看起来对'"
    why_bad: "基组不完备性在三个计算中方向不同 → 吸附能可能碰巧对但机理结论全错"
  - action: "不加偶极校正靠 slab 增厚解决问题"
    why_bad: "slab 增厚不消除虚假电场，只减少其比例影响 → 吸附能仍含系统偏差"
~~~
