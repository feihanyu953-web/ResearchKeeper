# VASP SCF 不收敛诊断链 (skeleton)

> record_type: error_chain | scope: single_software | software: [VASP]
> 骨架级别，待目标运行环境完成 AIMD 验证后升级

~~~yaml
record_id: errchain-vasp-scf-not-converge-0001
record_type: error_chain
scope: single_software
software:
  - VASP
topic: "VASP SCF 在 NELM=60 步内不收敛"
source_type: official_doc
source_ref: "https://www.vasp.at/wiki/Category:Electronic_minimization"
version_or_doc_date: "VASP 6.x; checked 2026-05-24"
claim: >
  VASP SCF 在 60 步内未收敛，常见于含 d 电子金属 + 界面水体系。
  根因可能为 ALGO 不合适、AMIX 过大、或 ENCUT 不够。
evidence_level: check
confidence: local_unverified
related_wiki:
  - computer_kb/wiki/errors/vasp_scf_not_converge.md
related_records:
  - vasp-error-scf-not-converge-0001
  - vasp-param-algo-0007
  - vasp-param-amix-0012
  - vasp-param-amix-mag-0013
  - rel-vasp-scf-precision-chain-0001
note: >
  骨架级别，基于领域经验和官方文档。尚未在目标运行环境复现并保存完整 SC 不收敛日志。
  待目标运行环境完成 AIMD 验证后升级 confidence + 补充 exact_error。
last_checked: 2026-05-24

exact_error: "WARNING: SCF convergence not achieved within NELM=60 steps (domain knowledge skeleton; no local log yet)"

diagnosis_chain:
  - level: 1
    question: "体系是否含 d 电子过渡金属 + 界面水？"
    check: "检查 POSCAR 元素列表"
    action: "含 Pt/Ni/Co/Fe/Cu + O/H → 收敛困难是常见的"

  - level: 2
    question: "ALGO 设置是什么？"
    check: "grep ALGO INCAR"
    action: "ALGO=Normal → 尝试改为 All"
    root_cause: "d 电子体系的电荷密度对迭代算法敏感; All 用全对角化更稳健"

  - level: 3
    question: "AMIX/AMIX_MAG 是否太大？"
    check: "grep AMIX INCAR"
    action: "AMIX=0.4 → 降至 0.2; AMIX_MAG=1.6 → 降至 0.8"

parameter_root_cause:
  - parameter: ALGO
    issue: "Normal 可能不够稳健"
    record: vasp-param-algo-0007
  - parameter: AMIX
    issue: "0.4 可能过大 → charge sloshing"
    record: vasp-param-amix-0012
  - parameter: AMIX_MAG
    issue: "与 AMIX 同步调低"
    record: vasp-param-amix-mag-0013

relations_involved:
  - rel-vasp-scf-precision-chain-0001

fixes:
  - priority: 1
    action: "ALGO=Normal → All"
    how: "INCAR: ALGO = All"
    verified: false
    evidence_status: "domain_knowledge; not verified locally yet"
  - priority: 2
    action: "AMIX=0.4→0.2, AMIX_MAG=1.6→0.8"
    how: "INCAR: AMIX = 0.2; AMIX_MAG = 0.8"
    verified: false
    evidence_status: "domain_knowledge; not verified locally yet"
  - priority: 3
    action: "增加 NELM 到 100 (治标不治本)"
    how: "INCAR: NELM = 100"
    verified: false
    evidence_status: "domain_knowledge"

unsafe_fixes:
  - action: "ISMEAR=2 + 大 SIGMA=0.5 强制收敛"
    why_bad: "entropy error 可能 > 50 meV/atom → 总能量和力都不可信"
  - action: "不管不收敛强行继续 MD"
    why_bad: "每步的力和能量不可靠 → MD 轨迹无意义"

verified_on:
  environment: "skeleton (not verified locally)"
  hardware: "unknown"
  evidence_path: []
  evidence_note: "待目标运行环境复现 SCF 不收敛并保存 OUTCAR/OSZICAR 后回填"
  verification_date: 2026-05-24
~~~
