# VASP DOS/d-band 计算异常诊断链 (skeleton)

> record_type: error_chain | scope: single_software | software: [VASP]

~~~yaml
record_id: errchain-vasp-dos-dband-abnormal-0005
record_type: error_chain
scope: single_software
software:
  - VASP
topic: "DOS/PDOS 输出异常: d-band center 偏差 >0.2 eV、E_fermi 位置错误、Bader charge 不合理"
source_type: official_doc
source_ref: "https://www.vasp.at/wiki/LORBIT"
version_or_doc_date: "VASP 6.x; checked 2026-05-24"
claim: >
  DOS 质量问题的常见原因: ICHARG 设置不当导致重复 SCF、LORBIT 不够、NEDOS 太粗、ISMEAR 选错。
  Bader charge 异常: CHGCAR 网格太粗或未做 all-electron charge 校正。
evidence_level: check
confidence: local_unverified
related_wiki:
  - computer_kb/wiki/errors/vasp_dos_dband_abnormal.md
related_records:
  - vasp-error-dos-dband-abnormal-0005
  - vasp-param-icharg-0156
  - vasp-param-lorbit-0286
  - vasp-param-nedos-0449
  - vasp-param-rwigs-0544
  - rel-vasp-electronic-structure-chain-0006
note: "Skeleton 级别。d-band center 和 Bader charge 依赖外部 post-processing——排查也包括后处理步骤。"
last_checked: 2026-05-24

exact_error: "d-band center differs >0.2 eV from literature OR Bader charge sum ≠ total electrons (domain knowledge skeleton)"

diagnosis_chain:
  - level: 1
    question: "ICHARG=11 时是否有 CHGCAR？"
    check: "ls CHGCAR in calculation directory"
    action: "先跑 SCF static (ICHARG=2 / default) → 输出 CHGCAR → 再 non-SCF DOS"
    root_cause: "没有 CHGCAR 则 ICHARG=11 做不了 non-SCF 计算"
  - level: 2
    question: "LORBIT 是否 ≥10？"
    check: "grep LORBIT INCAR"
    action: "LORBIT=11 for lm-decomposed PROCAR"
  - level: 3
    question: "NEDOS 是否 ≥2000？"
    check: "grep NEDOS INCAR"
    action: "NEDOS=2000→3000 if d-band sharp"
    root_cause: "NEDOS=301 (默认) → d-band center 离散误差 ~0.1 eV"

parameter_root_cause:
  - parameter: ICHARG
    issue: "缺少先验 SCF 计算的 CHGCAR"
    record: vasp-param-icharg-0156
  - parameter: LORBIT
    issue: "LORBIT<10 → PROCAR 无 lm 分解"
    record: vasp-param-lorbit-0286
  - parameter: NEDOS
    issue: "网格太粗 → d-band center 数值不准"
    record: vasp-param-nedos-0449

relations_involved:
  - rel-vasp-electronic-structure-chain-0006

fixes:
  - priority: 1
    action: "确保 non-SCF 前有 CHGCAR (ICHARG=2 SCF → CHGCAR)"
    how: "Step1: default ICHARG SCF; Step2: cp CHGCAR → ICHARG=11 non-SCF"
    verified: false
    evidence_status: "domain_knowledge; not verified locally"
  - priority: 2
    action: "LORBIT=11 + NEDOS=2000"
    how: "INCAR: LORBIT=11; NEDOS=2000"
    verified: false
    evidence_status: "domain_knowledge; not verified locally"
  - priority: 3
    action: "ISMEAR=-5 (tetrahedron) for DOS + 4×4×1 k-mesh minimum"
    how: "INCAR: ISMEAR=-5; KPOINTS 4×4×1"
    verified: false
    evidence_status: "domain_knowledge; not verified locally"

unsafe_fixes:
  - action: "LORBIT<10 + 调 RWIGS 凑 Bader charge —— 'parameter tuning'"
    why_bad: "RWIGS 应来自元素共价/离子半径标准值，不应该作为可调参数"
  - action: "用 ISMEAR=0 + 大 SIGMA=0.5 → 让 DOS 看起来'平滑'"
    why_bad: "smearing 引入的展宽掩盖真实电子结构特征 (如 van Hove singularities)"
~~~
