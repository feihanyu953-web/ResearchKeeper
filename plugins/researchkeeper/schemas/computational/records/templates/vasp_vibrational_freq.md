# VASP 振动频率计算模板

> record_type: template | scope: single_software | software: [VASP]

~~~yaml
record_id: tmpl-vasp-vibrational-freq-0003
record_type: template
scope: single_software
software:
  - VASP
topic: "振动频率计算 (IBRION=5/6) —— ZPE 校正和 TS 验证"
source_type: official_doc
source_ref: "https://www.vasp.at/wiki/IBRION"
version_or_doc_date: "VASP 6.x; checked 2026-05-24"
claim: "用有限差分 (IBRION=5) 或 DFPT (IBRION=7/8) 计算吸附质的振动频率，获取 ZPE 校正和 TS 虚频验证。"
evidence_level: should
confidence: local_unverified
related_wiki:
  - computer_kb/wiki/concepts/vasp_neb_chain.md
related_records:
  - vasp-param-ediff-0053
  - vasp-param-nfree-0455
  - vasp-param-prec-0530
note: "Skeleton 级别。吸附质振动通常只算吸附质的 3N 自由度 (固定 slab)。"
last_checked: 2026-05-24

applies_to:
  systems: [slab_adsorbate]
  tasks: [zpe_correction, ts_verification, free_energy_diagram]

prerequisites:
  - step: "吸附质已几何优化 (EDIFFG < 0)"
    why: "振动频率计算需在局域极小点进行"

parameters:
  - name: IBRION
    value: 5
    reasoning: "有限差分法计算 Hessian; IBRION=6 对称差分 (更准但 2× 位移)"
    source_type: official_doc
    source_ref: "https://www.vasp.at/wiki/IBRION"
    record: vasp-param-ibrion-0154

  - name: NFREE
    value: 2
    record: vasp-param-nfree-0455
    reasoning: "2 个位移方向 (IBRION=5 时有效)"
    source_type: official_doc
    source_ref: "https://www.vasp.at/wiki/NFREE"

  - name: POTIM
    value: 0.015
    reasoning: "有限差分位移步长 (Å); POTIM=0.015 可同时用于力收敛 stepsize"
    source_type: official_doc
    source_ref: "https://www.vasp.at/wiki/POTIM"
    record: vasp-param-potim-0529

  - name: EDIFF
    value: 1E-6
    record: vasp-param-ediff-0053
    reasoning: "频率计算需紧 SCF (比几何优化更紧)"
    source_type: official_doc
    source_ref: "https://www.vasp.at/wiki/EDIFF"

  - name: PREC
    value: Normal
    record: vasp-param-prec-0530
    reasoning: "频率对力精度敏感 → PREC=Normal + 手动 ENCUT 精确控制（PREC=Accurate 会覆盖手动 ENCUT，见 vasp-param-prec-0530）; 需要 ADDGRID/LASPH 精度时显式开启"
    source_type: official_doc
    source_ref: "https://www.vasp.at/wiki/PREC"

  - name: ENCUT
    value: 400
    record: vasp-param-encut-0116
    reasoning: "与 SCF 精度链一致"
    source_type: official_doc
    source_ref: "https://www.vasp.at/wiki/ENCUT"

  - name: ISMEAR
    value: 0
    record: vasp-param-ismear-0181
    reasoning: "金属 slab"
    source_type: official_doc
    source_ref: "https://www.vasp.at/wiki/ISMEAR"

  - name: SIGMA
    value: 0.1
    record: vasp-param-sigma-0554
    source_type: official_doc
    source_ref: "https://www.vasp.at/wiki/SIGMA"

generated_incar: |
  # Vibrational Frequency | VASP 6.x
  IBRION   = 5
  NFREE    = 2
  POTIM    = 0.015
  EDIFF    = 1E-6
  PREC     = Normal
  ENCUT    = 400
  ADDGRID  = .TRUE.
  LASPH    = .TRUE.
  ISMEAR   = 0
  SIGMA    = 0.1

critical_gotchas:
  - symptom: "出现多个虚频"
    cause: "几何优化未完全收敛 或 固定自由度不够"
    fix: "重新优化到 EDIFFG < -0.03"
  - symptom: "虚频不是沿反应坐标"
    cause: "TS 结构不是鞍点 (可能收敛到 wrong saddle)"
    fix: "重做 NEB 或调整初始 TS guess"

success_criteria:
  - check: "IS/FS: 所有频率 > 0 (无不合理虚频)"
  - check: "TS: 有且仅有一个虚频沿反应坐标"
  - check: "ZPE 校正量合理 (< 0.3 eV for *H; < 1.0 eV for *COOH)"
~~~
