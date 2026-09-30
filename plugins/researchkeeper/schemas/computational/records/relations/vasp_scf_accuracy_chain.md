# VASP SCF 精度链：ENCUT → EDIFF → PREC → ADDGRID → LASPH

> record_type: relation | scope: single_software | software: [VASP]

~~~yaml
record_id: rel-vasp-scf-precision-chain-0001
record_type: relation
scope: single_software
software:
  - VASP
topic: "SCF 精度金字塔：ENCUT/EDIFF/PREC/ADDGRID/LASPH/ALGO/LREAL 联动"
source_type: official_doc
source_ref: "https://www.vasp.at/wiki/Category:INCAR_tag"
version_or_doc_date: "VASP 6.x Wiki; checked 2026-05-24"
claim: >
  SCF 收敛精度由 ENCUT/EDIFF/PREC/ADDGRID/LASPH/ALGO/LREAL 七个参数共同决定。
  底层（ENCUT/PREC）决定基组完整性，上层（EDIFF）决定基组上能跑多精确。
  ADDGRID/LASPH 补充力精度，ALGO 决定电子步算法，LREAL 决定投影方式。
evidence_level: should
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/vasp_scf_accuracy_chain.md
related_records:
  - vasp-param-encut-0116
  - vasp-param-ediff-0053
  - vasp-param-prec-0530
  - vasp-param-algo-0007
  - vasp-param-addgrid-0001
  - vasp-param-lasph-0211
  - vasp-param-lreal-0296
note: >
  Tier 2 关系规则。VASP Wiki 每页底部的 "Related tags" 提供了参数间交叉引用骨架。
  以下规则在官方骨架基础上补充了决策逻辑和失效症状。
last_checked: 2026-05-24

relation_type: coupled_accuracy
relation_basis:
  - official_cross_ref
  - physical_constraint
  - domain_knowledge

parameters:
  - name: ENCUT
    role: "基组完整性——平面波截断能"
    constraint: "≥ ENMAX × 1.3 for O-containing systems (ENMAX_O≈300 eV → ENCUT ≥ 400)"
    record: vasp-param-encut-0116

  - name: PREC
    role: "精度预设——批量覆盖 ENCUT/LREAL/ADDGRID 默认值"
    constraint: "Normal=手动控制; Accurate/High=自动调高但不透明"
    record: vasp-param-prec-0530

  - name: EDIFF
    role: "电子步收敛标准"
    constraint: "ENCUT=400 时 1E-5 足够; 1E-6 仅在有软模/声子时必要"
    record: vasp-param-ediff-0053

  - name: ALGO
    role: "电子步迭代算法"
    constraint: "VeryFast→Fast→Normal→All 依次更稳健但更慢"
    record: vasp-param-algo-0007

  - name: ADDGRID
    role: "augmentation 细网格——补 PAW 球内力精度"
    constraint: "含 d 电子金属 + 力敏感 → 必须开启"
    record: vasp-param-addgrid-0001

  - name: LASPH
    role: "非球对称 PAW 贡献"
    constraint: "与 ADDGRID 互补; 力敏感计算建议双双开启"
    record: vasp-param-lasph-0211

  - name: LREAL
    role: "PAW 投影方式"
    constraint: "大体系(>10Å)用 Auto 加速; 小体系用 .FALSE. 保精度"
    record: vasp-param-lreal-0296

relation_rules:
  - id: R1
    type: overrides
    from: PREC
    to: ENCUT
    detail: "PREC=Accurate/High 时 VASP 自动将 ENCUT 设为 ENMAX×1.3 (或更高)，覆盖手动值"
    decision: "需要精确控制 ENCUT → 使用 PREC=Normal + 手动指定 ENCUT"
    consequence: "PREC≠Normal 时 INCAR 中的 ENCUT 值可能被忽略"

  - id: R2
    type: coupled_accuracy
    from: ENCUT
    to: EDIFF
    detail: "不完整基组上跑紧 EDIFF 是自欺欺人。先保证 ENCUT 够，再收紧 EDIFF"
    decision: "ENCUT=400 → EDIFF=1E-5 合理; ENCUT=300 → EDIFF 再紧也白搭"
    consequence: "ENCUT 不足时收紧 EDIFF → 收敛到不完整基组解，能量差噪声"

  - id: R3
    type: coupled_accuracy
    from: ADDGRID
    to: LASPH
    detail: "ADDGRID 补 PAW 球内径向精度，LASPH 补角向精度。只开一个力方向仍有盲区"
    decision: "力敏感计算 (AIMD/NEB/声子) → ADDGRID=.TRUE. + LASPH=.TRUE."
    consequence: "只开一个 → 力方向盲区 → AIMD/NEB 力误差"

  - id: R4
    type: prerequisite
    from: system_size
    to: LREAL
    detail: "LREAL=Auto 在实空间投影 PAW，超胞边长 < 10 Å 时投影误差不可忽略"
    decision: "超胞 < 10Å → LREAL=.FALSE.; 大 slab → LREAL=Auto"
    consequence: "小超胞用 LREAL=Auto → 投影误差 → 力/能量偏差"

  - id: R5
    type: coupled_accuracy
    from: ALGO
    to: EDIFF
    detail: "ALGO=VeryFast/Fast 时电子步收敛可能不够平滑，EDIFF 达不到标称精度"
    decision: "力敏感或能量差计算 → ALGO=Normal 起步; SCF 不收敛 → ALGO=All"
    consequence: "ALGO=VeryFast + 紧 EDIFF → 实际达不到标称精度 → 能量差噪声"

failure_signatures:
  - symptom: "SCF 在 60 步内收敛但力不准"
    likely: "ADDGRID=.FALSE. 或 LASPH=.FALSE."
  - symptom: "不同 ENCUT 能量差 > 10 meV/atom"
    likely: "ENCUT 过低，基组不完整"
  - symptom: "小超胞 (~10Å) 力突然不准"
    likely: "LREAL=Auto 投影误差"
  - symptom: "SCF 收敛但不同 PREC 结果差异大"
    likely: "PREC=Accurate 自动改 ENCUT/LREAL 未察觉"
~~~
