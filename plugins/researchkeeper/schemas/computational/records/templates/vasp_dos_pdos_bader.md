# VASP DOS/PDOS/d-band/Bader 电子结构分析模板

> record_type: template | scope: single_software | software: [VASP]

~~~yaml
record_id: tmpl-vasp-dos-pdos-bader-0005
record_type: template
scope: single_software
software:
  - VASP
topic: "金属 slab + 吸附质体系的 DOS/PDOS/d-band center + Bader charge + work function 计算"
source_type: official_doc
source_ref: "https://www.vasp.at/wiki/LORBIT"
version_or_doc_date: "VASP 6.x; checked 2026-05-24"
claim: >
  三步走: (1) SCF static → CHGCAR, (2) ICHARG=11 non-SCF → DOSCAR+PROCAR,
  (3) post-processing → d-band center + PDOS plot + Bader charge + work function.
evidence_level: should
confidence: local_unverified
related_wiki:
  - computer_kb/wiki/concepts/vasp_electronic_structure_chain.md
related_records:
  - vasp-param-icharg-0156
  - vasp-param-lorbit-0286
  - vasp-param-nedos-0449
  - vasp-param-emin-0114
  - vasp-param-emax-0113
  - vasp-param-rwigs-0544
  - vasp-param-lvtot-0339
  - rel-vasp-electronic-structure-chain-0006
note: >
  Skeleton 级别。d-band center 和 PDOS 的后处理 (VASPKIT/pymatgen) 不在本模板中。
  Bader charge 需外部 Henkelman Bader 程序。
  work function 从 LOCPOT z-profile 提取。
last_checked: 2026-05-24

applies_to:
  systems: [metal_slab, adsorbate_on_metal, metal_water_interface]
  metals: [Pt, Ni, Co, Cu, Pd, Ir, Ru, Rh]
  tasks: [electronic_structure, dos, pdos, d_band_center, bader_charge, work_function]

hardware_profile: {}

prerequisites:
  - step: "已完成 SCF 弛豫 (自洽计算)"
    why: "需要 CHGCAR 作为 ICHARG=11 的输入; 需要 CONTCAR 作为晶体结构"
  - step: "准备 VASPKIT/pymatgen (DOS 后处理) 和 Bader 程序 (charge 分析)"
    why: "VASP 本身不输出 d-band center 或 Bader charge——需外部 post-process"

parameters:
  # ── Step 1: SCF static (produce CHGCAR) ──
  - name: ICHARG
    value: 2
    record: vasp-param-icharg-0156
    reasoning: "自洽 SCF → 输出 CHGCAR (standard)"
    source_type: official_doc
    source_ref: "https://www.vasp.at/wiki/ICHARG"

  - name: LVTOT
    value: ".TRUE."
    record: vasp-param-lvtot-0339
    reasoning: "输出 LOCPOT for work function; 在 SCF step 中设置"
    source_type: official_doc
    source_ref: "https://www.vasp.at/wiki/LVTOT"

  - name: IDIPOL
    value: 3
    record: vasp-param-idipol-0159
    reasoning: "work function 需要偶极校正; 在 SCF step 中设置"
    source_type: official_doc
    source_ref: "https://www.vasp.at/wiki/IDIPOL"

  - name: LDIPOL
    value: ".TRUE."
    record: vasp-param-ldipol-0230
    reasoning: "配合 IDIPOL"
    source_type: official_doc
    source_ref: "https://www.vasp.at/wiki/LDIPOL"

  # ── INCAR overrides for Step 2: Non-SCF DOS ──
  - name: ICHARG
    value: 11
    record: vasp-param-icharg-0156
    reasoning: "读取 CHGCAR + non-SCF → 快速出 DOS (不改电荷密度)"
    source_type: official_doc
    source_ref: "https://www.vasp.at/wiki/ICHARG"

  - name: LORBIT
    value: 11
    record: vasp-param-lorbit-0286
    reasoning: "LORBIT=11: lm-decomposed + phase factors → PDOS 完整; 不依赖 RWIGS"
    source_type: official_doc
    source_ref: "https://www.vasp.at/wiki/LORBIT"

  - name: NEDOS
    value: 2000
    record: vasp-param-nedos-0449
    reasoning: "d-band center < 0.01 eV 数值收敛需要 NEDOS≥2000"
    source_type: official_doc
    source_ref: "https://www.vasp.at/wiki/NEDOS"

  - name: EMIN
    value: -15
    record: vasp-param-emin-0114
    reasoning: "覆盖 Pt 5d band (~-8 to +3 eV) + 额外 margin"
    source_type: official_doc
    source_ref: "https://www.vasp.at/wiki/EMIN"

  - name: EMAX
    value: 10
    record: vasp-param-emax-0113
    reasoning: "覆盖 antibonding 区域 up to E_fermi+5 eV"
    source_type: official_doc
    source_ref: "https://www.vasp.at/wiki/EMAX"

generated_incar_step1: |
  # Step 1: SCF static + CHGCAR + LOCPOT (reuse relaxed CONTCAR as POSCAR)
  ICHARG   = 2
  LVTOT    = .TRUE.
  IDIPOL   = 3
  LDIPOL   = .TRUE.
  # (keep all other params from relaxation INCAR: ENCUT/PREC/EDIFF/ISMEAR/SIGMA)

generated_incar_step2: |
  # Step 2: Non-SCF DOS (copy CHGCAR from Step 1)
  ICHARG   = 11
  LORBIT   = 11
  NEDOS    = 2000
  EMIN     = -15
  EMAX     = 10
  ISMEAR   = -5        # tetrahedron method for accurate DOS
  SIGMA    = 0.05       # small if ISMEAR != -5
  # (keep ENCUT/PREC/EDIFF from Step 1)

critical_gotchas:
  - symptom: "DOSCAR 中 E_fermi 位置不对"
    cause: "ISMEAR=-5 (tetrahedron) 需要至少 4 k-points per direction"
    fix: "若 k-mesh < 4×4×1 → ISMEAR=0, SIGMA=0.05"
  - symptom: "PDOS 只有 spd 没有 d_xy/d_z2 等轨道分解"
    cause: "LORBIT<10 或 PROCAR 未开启"
    fix: "LORBIT=11"
  - symptom: "Bader charge 在某些原子上出现异常大 (>2 e⁻)"
    cause: "CHGCAR 网格太粗 → Bader 表面不平滑"
    fix: "增大 NGXF/NGYF/NGZF (INCAR: NGXF=2×default) 或使用 LAECHG=.TRUE. 输出 AECCAR0/1/2"
  - symptom: "d-band center 与文献差 >0.2 eV"
    cause: "NEDOS 不够 或 EMIN/EMAX 截断位置不同"
    fix: "NEDOS 3000; 确保 EMIN 完全覆盖 d 带"

success_criteria:
  - check: "DOSCAR 中 E_fermi 在带中 (金属 slab)"
  - check: "PDOS 的 d 带形状与文献一致"
  - check: "d-band center 对 NEDOS 的变化 < 0.02 eV (NEDOS=2000 vs 3000)"
  - check: "Bader charge 总和 = 体系总电子数 (误差 < 0.1 e⁻)"
  - check: "work function 顶底真空能级差 < 0.1 eV (IDIPOL 校正有效)"
~~~
