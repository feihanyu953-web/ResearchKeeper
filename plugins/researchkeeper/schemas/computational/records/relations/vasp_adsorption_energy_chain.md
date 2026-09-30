# VASP 吸附能计算与自由能图参数链

> record_type: relation | scope: single_software | software: [VASP]

~~~yaml
record_id: rel-vasp-adsorption-energy-chain-0005
record_type: relation
scope: single_software
software:
  - VASP
topic: "吸附能 + 自由能图参数联动: IDIPOL/LDIPOL/ISIF/ISMEAR + CHE 自由能校正"
source_type: official_doc
source_ref: "https://www.vasp.at/wiki/IDIPOL"
version_or_doc_date: "VASP 6.x; checked 2026-05-24"
claim: >
  吸附能计算 (E_ads = E_slab+ads - E_slab - E_gas) 要求三部分能量在相同精度下计算。
  不对称 slab (有吸附面/背面差异) 必须开偶极校正 (IDIPOL/LDIPOL)。
  CHE 自由能校正 (ΔG = ΔE + ΔZPE - TΔS) 对每一步中间体施加一致的参考态处理。
evidence_level: should
confidence: local_unverified
related_wiki:
  - computer_kb/wiki/concepts/vasp_adsorption_energy_chain.md
related_records:
  - vasp-param-idipol-0159
  - vasp-param-ldipol-0230
  - vasp-param-isif-0180
  - vasp-param-ismear-0181
  - vasp-param-sigma-0554
  - vasp-param-encut-0116
  - vasp-param-ediff-0053
  - vasp-param-prec-0530
  - vasp-param-lvtot-0339
  - rel-vasp-scf-precision-chain-0001
note: >
  覆盖 Pt(111)/Ni(111)/Co(0001) 类金属 slab 上 C/N/O/H 吸附质 + 电化学界面 CHE 自由能图。
  VASPsol 隐式溶剂（如需要电场/偏压效应）由单独 template 覆盖。
last_checked: 2026-05-24

relation_type: coupled_accuracy
relation_basis:
  - official_cross_ref
  - physical_constraint
  - domain_knowledge

parameters:
  - name: IDIPOL
    role: "偶极校正开关——不对称 slab 必须开启"
    constraint: "吸附质在单侧 → IDIPOL=3 (全方向校正)"
    record: vasp-param-idipol-0159

  - name: LDIPOL
    role: "偶极校正方向——需与 slab 法向对齐"
    constraint: "slab 在 z 方向 → LDIPOL=.TRUE."
    record: vasp-param-ldipol-0230

  - name: ISIF
    role: "cell 自由度——吸附质弛豫 vs slab 弛豫"
    constraint: "吸附质弛豫 ISIF=2; 清洁 slab 优化 ISIF=3 if bulk lattice known"
    record: vasp-param-isif-0180

  - name: ISMEAR
    role: "smearing 方法——金属 slab 用 MP (ISMEAR=1) 或 Gaussian (ISMEAR=0)"
    constraint: "ISMEAR=0 (Gaussian) for total energy; SIGMA=0.1"
    record: vasp-param-ismear-0181

  - name: SIGMA
    role: "smearing 宽度——平衡精度和收敛性"
    constraint: "0.1 eV for metal slabs with ~100 atoms"
    record: vasp-param-sigma-0554

  - name: ENCUT
    role: "基组截断——三部分能量必须一致"
    constraint: "≥400 eV for O-containing systems; 三部分全用同一个 ENCUT"
    record: vasp-param-encut-0116

  - name: LVTOT
    role: "局域电势输出——用于 work function 和界面偶极分析"
    constraint: ".TRUE. for work function; 配合 IDIPOL"
    record: vasp-param-lvtot-0339

relation_rules:
  - id: R1
    type: requires_companion
    from: "不对称 slab (单侧吸附)"
    to: IDIPOL
    detail: "仅有单侧吸附的 slab 失去 z 方向镜面对称 → 周期性边界条件产生虚假电场 → 能量/力被艺术性修正"
    decision: "IDIPOL=3 + LDIPOL=.TRUE. for z-direction slab"
    consequence: "不开偶极校正 → 吸附能误差可达 0.1-0.3 eV"

  - id: R2
    type: requires_companion
    from: IDIPOL
    to: LDIPOL
    detail: "IDIPOL 选择校正维度（1/2/3=x/y/z），LDIPOL 指定偶极中心"
    decision: "slab 法向 z → IDIPOL=3, LDIPOL=.TRUE."
    consequence: "IDIPOL 与 LDIPOL 不配套 → 偶极校正不完整或报错"

  - id: R3
    type: coupled_accuracy
    from: ENCUT
    to: "E_ads"
    detail: "E_ads = E_slab+ads − E_slab − E_gas。三项必须用完全相同的 ENCUT/PREC/k-points，否则减法中基组不完备性不抵消"
    decision: "统一 ENCUT≥400, PREC=Normal (手动控 ENCUT), 相同 KPOINTS 文件"
    consequence: "三项 ENCUT 不一致 → 吸附能误差 > 0.1 eV"

  - id: R4
    type: mutually_constrained
    from: ISMEAR
    to: SIGMA
    detail: "entropy term (TS) 对金属 slab 总能有贡献。SIGMA 过大熵修正高估; 过小 SCF 收敛困难"
    decision: "ISMEAR=0 (Gaussian) + SIGMA=0.1 eV; 金属 slab 结构优化避免无展宽方法 (-3) 与 tetrahedron (-5)"
    consequence: "金属用固定占据/无展宽方法 → 部分占据处理错误 → 总能量错误"

  - id: R5
    type: coupled_accuracy
    from: "CHE reference"
    to: "gas-phase molecules"
    detail: "CHE 自由能校正: ΔG = ΔE_DFT + ΔZPE − TΔS。ΔE_DFT 用 slab 同精度。气体分子计算: 仅 Γ 点, ENCUT 同 slab, ISMEAR=0, SIGMA=0.001 (近分子)"
    decision: "气体分子放 15×15×15 Å 盒子; ISMEAR=0; SIGMA=0.001; IBRION=2; NSW=50 (for ZPE)"
    consequence: "气体盒子太小 → 分子间相互作用污染 ΔE；SIGMA 与 slab 不一致 → 熵项误差"

  - id: R6
    type: requires_companion
    from: "work function analysis"
    to: LVTOT
    detail: "LVTOT=.TRUE. 输出 LOCPOT → 提取真空能级 → work function = E_vac − E_fermi"
    decision: "需同时开 IDIPOL 保证真空能级不被虚假电场偏移"
    consequence: "缺 IDIPOL → 真空能级被虚假电场偏移 → work function 误差"

failure_signatures:
  - symptom: "吸附能依赖 slab 厚度(应收敛但未收敛)"
    likely: "ENCUT 不够 或 IDIPOL 未开"
  - symptom: "清洁 slab 能量与文献差异 > 0.2 eV"
    likely: "ISMEAR/SIGMA 设置与参考文献不一致"
  - symptom: "CHE 自由能图台阶高度与文献趋势不符"
    likely: "气体分子参考态能量计算方式不同 (盒子大小/SIGMA/ISMEAR)"
  - symptom: "work function 超预期变化 (>0.5 eV)"
    likely: "IDIPOL 未开 或 LVTOT 未配合"
~~~
