# VASP 电子结构分析参数链：DOS/PDOS/d-band/Bader

> record_type: relation | scope: single_software | software: [VASP]

~~~yaml
record_id: rel-vasp-electronic-structure-chain-0006
record_type: relation
scope: single_software
software:
  - VASP
topic: "DOS/PDOS/d-band center/Bader charge/work function 参数联动: LORBIT/NEDOS/EMIN/EMAX/ICHARG/RWIGS"
source_type: official_doc
source_ref: "https://www.vasp.at/wiki/LORBIT"
version_or_doc_date: "VASP 6.x; checked 2026-05-24"
claim: >
  PDOS (投影态密度) 和 d-band center 需要 LORBIT≥10+NEDOS≥2000+ICHARG=11 的正确组合。
  Bader charge 需要正确的 RWIGS + LORBIT 设置。
  work function 需要 LVTOT + IDIPOL。
evidence_level: should
confidence: local_unverified
related_wiki:
  - computer_kb/wiki/concepts/vasp_electronic_structure_chain.md
related_records:
  - vasp-param-lorbit-0286
  - vasp-param-nedos-0449
  - vasp-param-emin-0114
  - vasp-param-emax-0113
  - vasp-param-icharg-0156
  - vasp-param-rwigs-0544
  - vasp-param-lvtot-0339
  - vasp-param-lvhar-0338
  - vasp-param-idipol-0159
  - rel-vasp-scf-precision-chain-0001
note: >
  d-band center 从 PDOS 数据的 post-processing 得到（非 VASP 内建输出）。
  Bader charge 需外部 Bader 程序处理 CHGCAR。
  RWIGS 仅在使用 LORBIT<10 时 VASP 内部需要；LORBIT≥10 时 VASP 用 PAW 投影真实空间波函数，不依赖 RWIGS。
last_checked: 2026-05-24

relation_type: coupled_accuracy
relation_basis:
  - official_cross_ref
  - physical_constraint
  - domain_knowledge

parameters:
  - name: ICHARG
    role: "电荷密度初始化——控制是否从 CHGCAR 读取"
    constraint: "ICHARG=11: 读取 CHGCAR + 非自洽 DOS 计算"
    record: vasp-param-icharg-0156

  - name: LORBIT
    role: "投影波函数——决定 PROCAR 输出和 PDOS 可用性"
    constraint: "LORBIT≥10 输出 lm-decomposed PROCAR; LORBIT=11 含相位因子"
    record: vasp-param-lorbit-0286

  - name: NEDOS
    role: "DOS 能量网格点数——决定 d-band center 数值精度"
    constraint: "NEDOS≥2000 for d-band center < 0.05 eV precision"
    record: vasp-param-nedos-0449

  - name: EMIN
    role: "DOS 能量范围下限"
    constraint: "-15 to -10 eV for Pt-group d-band (E_fermi - 10 eV)"
    record: vasp-param-emin-0114

  - name: EMAX
    role: "DOS 能量范围上限"
    constraint: "5 to 10 eV (E_fermi + 5 eV)"
    record: vasp-param-emax-0113

  - name: RWIGS
    role: "Wigner-Seitz 半径——Bader charge 的原子体积参考; LORBIT<10 时需要"
    constraint: "每元素一个值 (Å); LORBIT≥10 时可不设"
    record: vasp-param-rwigs-0544

  - name: LVTOT
    role: "局域电势——work function 计算"
    constraint: ".TRUE. 输出 LOCPOT"
    record: vasp-param-lvtot-0339

  - name: LVHAR
    role: "Hartree 势——替代 work function 提取 (不含 XC)"
    constraint: ".TRUE. 输出 LOCPOT 的 Hartree-only 部分"
    record: vasp-param-lvhar-0338

relation_rules:
  - id: R1
    type: prerequisite
    from: "prior SCF run (self-consistent)"
    to: ICHARG
    detail: "非自洽 DOS 计算 (ICHARG=11) 必须先跑一次自洽 SCF 获得 CHGCAR"
    decision: "Step 1: SCF self-consistent (ICHARG=2 or default) → 输出 CHGCAR; Step 2: ICHARG=11 + LORBIT≥10 + NEDOS≥2000 → 输出 DOSCAR+PROCAR"
    consequence: "没有 CHGCAR 则 ICHARG=11 无法运行"

  - id: R2
    type: requires_companion
    from: "PDOS 需求"
    to: LORBIT
    detail: "p4vasp/VASPKIT/pymatgen 出 PDOS 图需要 LORBIT≥10"
    decision: "LORBIT=10 (lm-decomposed, 不含相位) or 11 (含相位因子)"
    consequence: "LORBIT<10 → PROCAR 只有 spd 分解没 lm-decomposed → PDOS 无法分轨道"

  - id: R3
    type: coupled_accuracy
    from: NEDOS
    to: "d-band center"
    detail: "d-band center ε_d = ∫ E·ρ_d(E)dE / ∫ ρ_d(E)dE。数值积分精度依赖 NEDOS。NEDOS=301 (默认) → ε_d 离散误差 ~0.1 eV; NEDOS=2000 → <0.01 eV"
    decision: "NEDOS=2000 起步; 若 d-band 锐利 (>3 eV/Å²) → NEDOS=3000"
    consequence: "NEDOS 不足 → ε_d 离散误差 ~0.1 eV；NEDOS=2000 → <0.01 eV"

  - id: R4
    type: mutually_constrained
    from: EMIN
    to: EMAX
    detail: "d-band center 积分区间必须覆盖整个 d 带 (>5 eV below/above Fermi)"
    decision: "Pt/Ni/Co: EMIN=-10, EMAX=5; sp 元素 (C/N/O): EMIN=-20, EMAX=10"
    consequence: "积分区间未覆盖整个 d 带 → ε_d 系统性偏移"

  - id: R5
    type: mutually_exclusive
    from: LORBIT
    to: RWIGS
    detail: "LORBIT≥10 使用 PAW 投影到真实空间波函数计算 PDOS——不依赖 RWIGS。LORBIT<10 的旧方法需要 RWIGS 定义原子球半径"
    decision: "现代做法: LORBIT=11 (直接跳过 RWIGS); 如果必须用 LORBIT<10 → 设置 RWIGS (每元素)"
    consequence: "LORBIT<10 且未设 RWIGS → PDOS 分解错误或缺失"

  - id: R6
    type: requires_companion
    from: "work function"
    to: "LVTOT + IDIPOL"
    detail: "work function = E_vac − E_fermi。E_vac 从 LOCPOT 的 z-profile 读取。IDIPOL 保证真空能级平坦"
    decision: "LVTOT=.TRUE. + IDIPOL=3 → LOCPOT 输出 → VASPKIT/pymatgen 提取 work function"
    consequence: "缺 IDIPOL → 真空能级不平坦 → work function 误差"

failure_signatures:
  - symptom: "PDOS 图在 E_fermi 处无 DOS 值"
    likely: "NEDOS 太粗 (如 301) → E_fermi 落在网格间"
  - symptom: "d-band center 计算值与文献差 > 0.2 eV"
    likely: "NEDOS 不足 或 EMIN/EMAX 截断位置不同"
  - symptom: "Bader charge 总和 ≠ 总电子数"
    likely: "CHGCAR 网格太粗 (NGXF/NGYF/NGZF 不够) 或 RWIGS 设置不当"
  - symptom: "work function 不对称 (顶/底真空不同)"
    likely: "IDIPOL 未开"
~~~
