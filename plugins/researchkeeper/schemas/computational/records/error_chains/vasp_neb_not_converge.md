# VASP NEB 不收敛诊断链 (skeleton)

> record_type: error_chain | scope: single_software | software: [VASP]

~~~yaml
record_id: errchain-vasp-neb-not-converge-0002
record_type: error_chain
scope: single_software
software:
  - VASP
topic: "NEB 路径不收敛或 CI-NEB 鞍点未找到"
source_type: official_doc
source_ref: "https://www.vasp.at/wiki/NEB"
version_or_doc_date: "VASP 6.x; checked 2026-05-24"
claim: "NEB 不收敛的常见原因: 初始路径不合理、SPRING 不合适、EDIFFG 太松或某插点 SCF 先崩。"
evidence_level: check
confidence: local_unverified
related_wiki:
  - computer_kb/wiki/errors/vasp_neb_not_converge.md
related_records:
  - vasp-error-neb-not-converge-0002
  - vasp-param-images-0165
  - vasp-param-spring-0558
  - vasp-param-ediffg-0054
  - rel-vasp-neb-chain-0002
note: "Skeleton 级别，基于领域经验。待目标运行环境完成 NEB 验证后升级。"
last_checked: 2026-05-24
exact_error: "NEB not converged / CI-NEB did not find a saddle point (domain knowledge skeleton)"

diagnosis_chain:
  - level: 1
    question: "初始路径是否合理？"
    check: "查看 POSCAR/00-0N 中各图是否 IS→FS 平滑过渡"
    action: "重做 nebmake; 或手动调整不合理插点"
  - level: 2
    question: "SPRING 是否太弱？"
    check: "检查 OUTCAR 中各图原子位移是否过大"
    action: "SPRING=-5.0→-8.0 加强弹簧约束"
    root_cause: "SPRING 不足 → 插点漂移 → 路径歧化"
  - level: 3
    question: "某插点是否 SCF 先不收敛？"
    check: "检查各 OUTCAR 是否都有 'reached required accuracy'"
    action: "同 SCF 不收敛排查: ALGO→All / AMIX↓"

parameter_root_cause:
  - parameter: SPRING
    issue: "弹簧太弱"
    record: vasp-param-spring-0558
  - parameter: IMAGES
    issue: "插点太多或太少"
    record: vasp-param-images-0165

relations_involved:
  - rel-vasp-neb-chain-0002
  - rel-vasp-scf-precision-chain-0001

fixes:
  - priority: 1
    action: "加强弹簧: SPRING=-5.0→-8.0"
    verified: false
    evidence_status: "domain_knowledge; not verified locally"
  - priority: 2
    action: "减少插点: IMAGES=7→5"
    verified: false
    evidence_status: "domain_knowledge; not verified locally"
  - priority: 3
    action: "确保每张图的 SCF 收敛 (ALGO=All/AMIX↓)"
    verified: false
    evidence_status: "domain_knowledge; not verified locally"

unsafe_fixes:
  - action: "EDIFFG=-0.1 强制早停—— TS 可能不准"
    why_bad: "松弛的力收敛→ TS 能量/结构不可信"
~~~
