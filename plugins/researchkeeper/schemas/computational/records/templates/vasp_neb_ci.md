# VASP CI-NEB 过渡态搜索模板

> record_type: template | scope: single_software | software: [VASP]

~~~yaml
record_id: tmpl-vasp-neb-ci-0002
record_type: template
scope: single_software
software:
  - VASP
topic: "CI-NEB 过渡态搜索 + 振动频率验证"
source_type: official_doc
source_ref: "https://www.vasp.at/wiki/NEB"
version_or_doc_date: "VASP 6.x; checked 2026-05-24"
claim: "CI-NEB 搜索催化反应过渡态的 INCAR 模板，含力和 SCF 收敛、插点设置。"
evidence_level: should
confidence: local_unverified
related_wiki:
  - computer_kb/wiki/concepts/vasp_neb_chain.md
related_records:
  - vasp-param-images-0165
  - vasp-param-spring-0558
  - vasp-param-ediffg-0054
  - rel-vasp-neb-chain-0002
  - rel-vasp-scf-precision-chain-0001
note: "Skeleton 级别，基于领域经验。待目标运行环境完成 NEB 验证后升级 confidence。"
last_checked: 2026-05-24

applies_to:
  systems: [metal_slab_adsorbate, catalytic_reaction]
  metals: [Pt, Ni, Co, Cu, Pd, Ir, Ru]
  reactions: ["*H→TS", "*OH→TS", "*CO→TS", "C-N_coupling", "OER_steps", "ORR_steps"]

prerequisites:
  - step: "IS 和 FS 已分别几何优化"
    why: "NEB 需要两端结构"
  - step: "用 nebmake.pl 或 ASE 生成线性插值路径"
    why: "生成中间 IMAGES 张初始猜测结构"
  - step: "确认能垒 < 1.5 eV (否则需检查初始路径)"
    why: "过高能垒通常意味初始路径不合理"

parameters:
  - name: IMAGES
    value: 5
    record: vasp-param-images-0165
    reasoning: "5 张插点对简单反应足够; 复杂反应增至 7-9"
    source_type: official_doc
    source_ref: "https://www.vasp.at/wiki/IMAGES"

  - name: SPRING
    value: -5.0
    record: vasp-param-spring-0558
    reasoning: "-5.0 eV/Å² 是 NEB 通用起手值"
    source_type: official_doc
    source_ref: "https://www.vasp.at/wiki/SPRING"

  - name: LCLIMB
    value: ".TRUE."
    reasoning: "CI-NEB 精确收敛到鞍点"
    source_type: official_doc
    source_ref: "https://www.vasp.at/wiki/NEB"
    constraint: "需配合 EDIFFG<0"
    record: vasp-param-lclimb-0500

  - name: IBRION
    value: 1
    reasoning: "VASP 内置 NEB 用 IBRION=1"
    source_type: official_doc
    source_ref: "https://www.vasp.at/wiki/IBRION"
    record: vasp-param-ibrion-0154

  - name: EDIFFG
    value: -0.03
    record: vasp-param-ediffg-0054
    reasoning: "CI-NEB 力收敛: -0.03 eV/Å"
    source_type: official_doc
    source_ref: "https://www.vasp.at/wiki/EDIFFG"

  - name: ENCUT
    value: 400
    record: vasp-param-encut-0116
    reasoning: "与 SCF 精度链一致"
    source_type: official_doc
    source_ref: "https://www.vasp.at/wiki/ENCUT"

  - name: EDIFF
    value: 1E-5
    record: vasp-param-ediff-0053
    reasoning: "力敏感计算需要紧 SCF"
    source_type: official_doc
    source_ref: "https://www.vasp.at/wiki/EDIFF"

  - name: PREC
    value: Normal
    record: vasp-param-prec-0530
    reasoning: "手动控制 ENCUT/ADDGRID"
    source_type: official_doc
    source_ref: "https://www.vasp.at/wiki/PREC"

  - name: ADDGRID
    value: ".TRUE."
    record: vasp-param-addgrid-0001
    reasoning: "NEB 是力敏感计算"
    source_type: official_doc
    source_ref: "https://www.vasp.at/wiki/ADDGRID"

  - name: ISMEAR
    value: 0
    record: vasp-param-ismear-0181
    reasoning: "金属 slab"
    source_type: official_doc
    source_ref: "https://www.vasp.at/wiki/ISMEAR"

  - name: SIGMA
    value: 0.1
    record: vasp-param-sigma-0554
    reasoning: "平衡收敛与 energy accuracy"
    source_type: official_doc
    source_ref: "https://www.vasp.at/wiki/SIGMA"

generated_incar: |
  # CI-NEB | VASP 6.x
  IMAGES   = 5
  SPRING   = -5.0
  LCLIMB   = .TRUE.
  IBRION   = 1
  EDIFFG   = -0.03
  
  ENCUT    = 400
  PREC     = Normal
  EDIFF    = 1E-5
  ADDGRID  = .TRUE.
  ISMEAR   = 0
  SIGMA    = 0.1

critical_gotchas:
  - symptom: "NEB 最高能量点不够高 (能垒 < 0.1 eV)"
    cause: "初始路径直接穿越反应物/产物 (没经过中间态)"
    fix: "检查 IS 和 FS 的原子对应; 重做 nebmake"
  - symptom: "CI 点不停留在鞍点附近"
    cause: "EDIFFG 太松或 SPRING 太弱"
    fix: "EDIFFG=-0.03→-0.05"

success_criteria:
  - check: "所有插点力 < |EDIFFG|"
  - check: "能垒合理 (与实验或文献已知值 ±0.2 eV)"
  - check: "CI 点单频率虚频 (振动验证)"
  - check: "路径无 cusp 或 sudden jump"
~~~
