# VASP NEB/CI-NEB 参数链

> record_type: relation | scope: single_software | software: [VASP]

~~~yaml
record_id: rel-vasp-neb-chain-0002
record_type: relation
scope: single_software
software:
  - VASP
topic: "NEB/CI-NEB 参数联动: IMAGES/SPRING/LCLIMB/EDIFFG/IBRION"
source_type: official_doc
source_ref: "https://www.vasp.at/wiki/IMAGES"
version_or_doc_date: "VASP 6.x; checked 2026-05-24"
claim: >
  NEB 搜过渡态的收敛由 IMAGES/SPRING/EDIFFG 共同决定。
  CI-NEB (LCLIMB=.TRUE.) 精确收敛到鞍点需配合更紧的力收敛标准。
evidence_level: should
confidence: local_unverified
related_wiki:
  - computer_kb/wiki/concepts/vasp_neb_chain.md
related_records:
  - vasp-param-images-0165
  - vasp-param-spring-0558
  - vasp-param-ediffg-0054
note: "LCLIMB 属 VTST 扩展标签（见 vasp-param-lclimb-0500）。ICHAIN 标签尚未在 VASP Wiki Category:INCAR_tag 中定位，待确认后补充。"
last_checked: 2026-05-24

relation_type: coupled_accuracy
relation_basis:
  - domain_knowledge
  - physical_constraint

parameters:
  - name: IMAGES
    role: "插点数量——决定路径分辨率"
    constraint: "3-7 for simple reactions; 7-15 for complex"
    record: vasp-param-images-0165
  - name: SPRING
    role: "弹簧常数——控制插点间距均匀性"
    constraint: "-5.0 eV/Å² typical; 绝对值过小路径松弛不足"
    record: vasp-param-spring-0558
  - name: LCLIMB
    role: "CI-NEB 开关——精确收敛到鞍点"
    constraint: ".TRUE. 启用 CI; 需配合 EDIFFG < -0.03"
    record: vasp-param-lclimb-0500
  - name: EDIFFG
    role: "力收敛标准——负值激活力判据"
    constraint: "CI-NEB 推荐 -0.03 to -0.05 eV/Å"
    record: vasp-param-ediffg-0054
  - name: IBRION
    role: "NEB 模式需设为特定值"
    constraint: "IBRION=1 for NEB (VASP 内置); VTST 用 IBRION=3"
    record: vasp-param-ibrion-0154

relation_rules:
  - id: R1
    type: coupled_accuracy
    from: IMAGES
    to: EDIFFG
    detail: "插点越多路径分辨率越高，但每个点的力收敛仍需 EDIFFG 保证"
    decision: "CI-NEB: IMAGES=5-7 + EDIFFG=-0.03 是常用起手组合"
    consequence: "插点过少 → 路径分辨率低；EDIFFG 过松 → 力未收敛"

  - id: R2
    type: requires_companion
    from: LCLIMB
    to: EDIFFG
    detail: "CI-NEB 激活后最高能量点不感受弹簧力，向鞍点精确爬升，需要紧力标准"
    decision: "LCLIMB=.TRUE. → EDIFFG ≤ -0.03"
    consequence: "LCLIMB 开启但 EDIFFG 过松 → 爬升不精确 → 鞍点能量虚高"

  - id: R3
    type: mutually_constrained
    from: SPRING
    to: IMAGES
    detail: "弹簧太弱 + 插点太多 → 路径松弛漂移; 弹簧太强 → 切向力分量受影响"
    decision: "SPRING=-5.0 + IMAGES=5-7 经验安全组合"
    consequence: "弹簧过弱 + 插点多 → 路径松弛漂移；过强 → 切向力分量受扰"

failure_signatures:
  - symptom: "NEB 路径不平滑，若干点 '堆积' 在两端"
    likely: "SPRING 绝对值太小 (如 -1.0)"
  - symptom: "CI-NEB 最高点不停留在鞍点附近"
    likely: "EDIFFG 不够紧 (如 -0.1)"
  - symptom: "NEB 中途报错不收敛"
    likely: "某张插图的 SCF 不收敛 → 先检查 ENCUT/ALGO"
~~~
