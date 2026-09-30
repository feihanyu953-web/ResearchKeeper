# VASP MD 离子步爆炸诊断链 (skeleton)

> record_type: error_chain | scope: single_software | software: [VASP]

~~~yaml
record_id: errchain-vasp-md-atom-explosion-0003
record_type: error_chain
scope: single_software
software:
  - VASP
topic: "AIMD 离子步爆炸 (max force > 100 eV/Å 或原子飞出超胞)"
source_type: official_doc
source_ref: "https://www.vasp.at/wiki/MDALGO"
version_or_doc_date: "VASP 6.x; checked 2026-05-24"
claim: "VASP AIMD 第一步或几步内原子爆炸的常见原因: POTIM 过大、初始结构重叠、thermostat 未设置好。"
evidence_level: check
confidence: local_unverified
related_wiki:
  - computer_kb/wiki/errors/vasp_md_atom_explosion.md
related_records:
  - vasp-error-md-atom-explosion-0003
  - vasp-md-param-potim-0003
  - vasp-md-param-mdalgo-0006
  - rel-vasp-md-thermostat-chain-0004
note: "Skeleton 级别。待目标运行环境复现并保存 OUTCAR 后升级。"
last_checked: 2026-05-24
exact_error: "离子步位移 > 0.5 Å/step 或 total energy 突然跳跃 > 100 eV (skeleton)"

diagnosis_chain:
  - level: 1
    question: "初始结构是否有原子过近 (d < 0.5 Å)？"
    check: "用 ASE/VESTA 检查最短原子间距"
    action: "若有过近原子对 → 重构初始结构; 先做 minimize"
    root_cause: "初始原子重叠 → 第一步力极大 → 加速过猛"

  - level: 2
    question: "POTIM 是否过大？"
    check: "grep POTIM INCAR"
    action: "含 H → POTIM≤0.5 fs; 无 H → ≤1.0 fs"
    root_cause: "timestep 过大 + 轻元素 (H) → 核运动超过谐振区"

  - level: 3
    question: "thermostat 是否正常工作？"
    check: "OSZICAR 中 T 是否在目标值附近？"
    action: "NVT: 确认 MDALGO + companion tag 设置完整"

parameter_root_cause:
  - parameter: POTIM
    issue: "timestep 过大"
    record: vasp-md-param-potim-0003
  - parameter: MDALGO
    issue: "companion tag 缺失"
    record: vasp-md-param-mdalgo-0006

relations_involved:
  - rel-vasp-md-thermostat-chain-0004

fixes:
  - priority: 1
    action: "POTIM 减半"
    verified: false
    evidence_status: "domain_knowledge"
  - priority: 2
    action: "先 minimize (IBRION=2) 再 MD"
    verified: false
    evidence_status: "domain_knowledge; not verified locally"

unsafe_fixes:
  - action: "增大 SMASS/LANGEVIN_GAMMA 来'压住'爆炸"
    why_bad: "掩盖根本问题 (结构重叠/timestep过大); 过强的 thermostat 篡改动力学"
~~~
