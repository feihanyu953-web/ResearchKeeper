# Error records

> Error/symptom records for VASP and LAMMPS calculation workflows.
> Sources are the official VASP and LAMMPS documentation URLs recorded in each entry.
> These records are official-doc troubleshooting routes; locally verified entries are explicitly marked with `confidence: local_verified` (e.g. vasp-error-aimd-temperature-runaway-0001).

~~~yaml
record_id: lammps-error-lost-atoms-0005
record_type: error
scope: single_software
software:
  - LAMMPS
topic: Lost atoms
source_type: official_doc
source_ref: https://docs.lammps.org/Errors_details.html#lost-atoms
version_or_doc_date: LAMMPS docs release git info 30Mar2026; checked 2026-05-22
claim: LAMMPS official error details include a `Lost atoms` section for simulations where atoms are lost.
evidence_level: check
confidence: official
related_wiki:
  - computer_kb/wiki/errors/lammps_lost_atoms.md
related_records:
  - lammps-md-cmd-run-0021
note: Lost atoms should first be treated as a stability/deployment problem, not ignored.
last_checked: 2026-05-22
exact_error: Lost atoms
symptom: LAMMPS reports atoms missing during a run.
likely_causes:
  - unstable initial geometry
  - timestep too large
  - bad forces from wrong potential or element mapping
  - nonperiodic boundary escape
diagnosis_steps:
  - inspect the first failing dump frames
  - reduce timestep and run a short smoke test
  - verify pair_coeff element mapping and units
fixes:
  - minimize or equilibrate more gently
  - reduce timestep
  - fix potential/model mapping
verified_on: official error route only; no local run verified
unsafe_fixes:
  - do not disable lost-atom checks to continue production runs
~~~

~~~yaml
record_id: lammps-error-non-numeric-instability-0006
record_type: error
scope: single_software
software:
  - LAMMPS
topic: Non-numeric atom coords or pressure or box dimensions - simulation unstable
source_type: official_doc
source_ref: https://docs.lammps.org/Errors_details.html#non-numeric-atom-coords-or-pressure-or-box-dimensions-simulation-unstable
version_or_doc_date: LAMMPS docs release git info 30Mar2026; checked 2026-05-22
claim: LAMMPS official error details include a non-numeric atom coordinates/pressure/box dimensions section indicating simulation instability.
evidence_level: check
confidence: official
related_wiki:
  - computer_kb/wiki/errors/lammps_non_numeric_instability.md
related_records: []
note: This is a serious MD stability failure and should stop the workflow until the cause is identified.
last_checked: 2026-05-22
exact_error: Non-numeric atom coords or pressure or box dimensions - simulation unstable
symptom: LAMMPS state becomes NaN/Inf or otherwise non-numeric.
likely_causes:
  - force explosion
  - timestep too large
  - bad initial structure
  - invalid potential/model mapping
diagnosis_steps:
  - inspect thermo output before failure
  - inspect dump frames for atom overlap or blow-up
  - rerun with shorter timestep and minimal output
fixes:
  - repair initial structure
  - reduce timestep
  - verify potential mapping and model validity
verified_on: official error route only; no local run verified
unsafe_fixes:
  - do not restart from a non-numeric trajectory state
~~~

~~~yaml
record_id: lammps-error-out-of-range-atoms-0007
record_type: error
scope: single_software
software:
  - LAMMPS
topic: Out of range atoms - cannot compute
source_type: official_doc
source_ref: https://docs.lammps.org/Errors_details.html#out-of-range-atoms-cannot-compute
version_or_doc_date: LAMMPS docs release git info 30Mar2026; checked 2026-05-22
claim: LAMMPS official error details include an `Out of range atoms - cannot compute` section.
evidence_level: check
confidence: official
related_wiki:
  - computer_kb/wiki/errors/lammps_out_of_range_atoms.md
related_records: []
note: This error often appears near unstable motion, bad communication, or neighbor-list issues and needs context from the log and dump.
last_checked: 2026-05-22
exact_error: Out of range atoms - cannot compute
symptom: LAMMPS cannot compute because atoms are outside the expected communication/neighbor range.
likely_causes:
  - atoms moved too far in one step
  - timestep too large
  - unstable forces
  - communication or neighbor settings not suitable
diagnosis_steps:
  - inspect velocity, timestep, and force scale
  - inspect dump immediately before failure
  - verify neighbor/communication settings
fixes:
  - reduce timestep
  - stabilize initial structure
  - adjust communication/neighbor setup if justified
verified_on: official error route only; no local run verified
unsafe_fixes:
  - do not only increase cutoffs if the underlying physics is exploding
~~~

~~~yaml
record_id: lammps-error-unrecognized-style-package-0008
record_type: error
scope: single_software
software:
  - LAMMPS
topic: Unrecognized style or package not enabled
source_type: official_doc
source_ref: https://docs.lammps.org/Errors_details.html#unrecognized-style
version_or_doc_date: LAMMPS docs release git info 30Mar2026; checked 2026-05-22
claim: LAMMPS official error details include an `Unrecognized ... style ...` section, relevant when a requested style is not available in the current LAMMPS build.
evidence_level: check
confidence: official
related_wiki:
  - computer_kb/wiki/errors/lammps_unrecognized_style_package.md
related_records: []
note: For custom potential deployment, this commonly points to missing potential integration, missing package, or incompatible LAMMPS build.
last_checked: 2026-05-22
exact_error: Unrecognized ... style ...
symptom: LAMMPS does not recognize a requested pair_style or other command.
likely_causes:
  - package not built/enabled
  - wrong executable or environment
  - incompatible build options
diagnosis_steps:
  - check LAMMPS build packages and executable
  - check selected potential deployment route
  - test minimal input with the target style
fixes:
  - use a LAMMPS build with required package/integration
  - switch to a route supported by the installed build
verified_on: official error route only; no local run verified
unsafe_fixes:
  - do not assume a command in docs is available in the local binary
~~~

~~~yaml
record_id: lammps-error-energy-stress-not-tallied-0009
record_type: error
scope: single_software
software:
  - LAMMPS
topic: Energy or stress was not tallied by pair style
source_type: official_doc
source_ref: https://docs.lammps.org/Errors_details.html#energy-or-stress-was-not-tallied-by-pair-style
version_or_doc_date: LAMMPS docs release git info 30Mar2026; checked 2026-05-22
claim: LAMMPS official error details include an `Energy or stress was not tallied by pair style` section.
evidence_level: check
confidence: official
related_wiki:
  - computer_kb/wiki/errors/lammps_energy_stress_not_tallied.md
related_records: []
note: This matters when thermo output, pressure, stress, or minimization expects quantities not provided by the pair style/configuration.
last_checked: 2026-05-22
exact_error: Energy or stress was not tallied by pair style
symptom: A requested quantity cannot be computed because the pair style did not tally it.
likely_causes:
  - thermo/minimization/compute requests incompatible with pair style output
  - pair style option or model route does not provide requested stress/energy
diagnosis_steps:
  - simplify thermo_style and computes
  - check pair_style documentation and model capabilities
  - test energy/force-only first
fixes:
  - request only supported quantities
  - use a route/model that supports required stress/virial output
verified_on: official error route only; no local run verified
unsafe_fixes:
  - do not report stress/pressure from a route that does not support it
~~~

## p1-vasp-scf-not-converge-2026-05-24

~~~yaml
record_id: vasp-error-scf-not-converge-0001
record_type: error
scope: single_software
software:
  - VASP
topic: SCF convergence not achieved within NELM steps
source_type: official_doc
source_ref: "https://www.vasp.at/wiki/Category:Electronic_minimization"
version_or_doc_date: "VASP 6.x; checked 2026-05-24"
claim: "VASP SCF 在 NELM 步内不收敛，常见于含 d 电子金属 + 界面水体系。"
evidence_level: check
confidence: local_unverified
related_wiki:
  - computer_kb/wiki/errors/vasp_scf_not_converge.md
related_records:
  - vasp-param-algo-0007
  - vasp-param-amix-0012
  - vasp-param-amix-mag-0013
  - rel-vasp-scf-precision-chain-0001
  - errchain-vasp-scf-not-converge-0001
note: "Skeleton 级别。对应 error_chain: errchain-vasp-scf-not-converge-0001。待实测 AIMD 后升级 confidence。"
last_checked: 2026-05-24
exact_error: "WARNING: SCF convergence not achieved within NELM=60 steps"
symptom: "SCF 在 60 步内不收敛 | 含 d 电子金属 + 界面水常见"
likely_causes:
  - "ALGO 不够稳健"
  - "AMIX/AMIX_MAG 过大 -> charge sloshing"
diagnosis_steps:
  - "ALGO=Normal -> All"
  - "AMIX 0.4->0.2 / AMIX_MAG 1.6->0.8"
fixes:
  - "ALGO = All"
  - "AMIX = 0.2; AMIX_MAG = 0.8"
verified_on: "skeleton; 实测待补"
unsafe_fixes:
  - "ISMEAR=2 + 大 SIGMA 强制收敛"
~~~

## p2-vasp-neb-not-converge-2026-05-24

~~~yaml
record_id: vasp-error-neb-not-converge-0002
record_type: error
scope: single_software
software:
  - VASP
topic: NEB path not converged / CI-NEB saddle point not found
source_type: official_doc
source_ref: "https://www.vasp.at/wiki/NEB"
version_or_doc_date: "VASP 6.x; checked 2026-05-24"
claim: "NEB 不收敛常见原因: 初始路径不合理/SPRING不合适/插点SCF失败。"
evidence_level: check
confidence: local_unverified
related_wiki:
  - computer_kb/wiki/concepts/vasp_neb_chain.md
related_records:
  - vasp-param-spring-0558
  - vasp-param-images-0165
  - rel-vasp-neb-chain-0002
  - errchain-vasp-neb-not-converge-0002
note: "Skeleton。对应 error_chain: errchain-vasp-neb-not-converge-0002。"
last_checked: 2026-05-24
exact_error: "NEB not converged"
symptom: "NEB 力未收敛到 EDIFFG 或 CI 点不是鞍点"
likely_causes:
  - "初始路径不合理"
  - "SPRING 太弱"
  - "某插点 SCF 失败"
diagnosis_steps:
  - "检查初始路径 IS->FS 平滑性"
  - "SPRING=-5.0->-8.0"
  - "确保每张图 SCF 收敛"
fixes:
  - "加强弹簧 / 减少插点 / 修初始路径"
verified_on: "skeleton; 实测待补"
unsafe_fixes:
  - "EDIFFG=-0.1 强制早停"
~~~

## p3-vasp-md-atom-explosion-2026-05-24

~~~yaml
record_id: vasp-error-md-atom-explosion-0003
record_type: error
scope: single_software
software:
  - VASP
topic: AIMD ion-step explosion / atom飞出超胞
source_type: official_doc
source_ref: "https://www.vasp.at/wiki/MDALGO"
version_or_doc_date: "VASP 6.x; checked 2026-05-24"
claim: "AIMD 离子步爆炸常见原因: POTIM过大/初始结构重叠/thermostat未设好。"
evidence_level: check
confidence: local_unverified
related_wiki:
  - computer_kb/wiki/errors/vasp_md_atom_explosion.md
related_records:
  - vasp-md-param-potim-0003
  - rel-vasp-md-thermostat-chain-0004
  - errchain-vasp-md-atom-explosion-0003
note: "Skeleton。待实测 AIMD 后升级。"
last_checked: 2026-05-24
exact_error: "total energy 突然跳跃 > 100 eV 或离子位移 > 0.5 A/step"
symptom: "AIMD 首步或几步内原子飞出超胞"
likely_causes:
  - "POTIM 过大"
  - "初始结构重叠"
  - "thermostat companion tag 缺失"
diagnosis_steps:
  - "检查初始结构最短原子间距"
  - "POTIM 减半"
  - "先 minimize 再 MD"
fixes:
  - "POTIM<=0.5 fs (含H) | 先几何优化"
verified_on: "skeleton"
unsafe_fixes:
  - "盲目加大 thermostat coupling"
~~~

## p4-vasp-adsorption-energy-abnormal-2026-05-24

~~~yaml
record_id: vasp-error-adsorption-energy-abnormal-0004
record_type: error
scope: single_software
software:
  - VASP
topic: "吸附能异常: 与文献差>0.3 eV 或随 slab 层数漂移"
source_type: official_doc
source_ref: "https://www.vasp.at/wiki/IDIPOL"
version_or_doc_date: VASP 6.x; checked 2026-05-24
claim: "吸附能计算异常最常见原因: 偶极校正未开、三部分能量计算参数不一致、ISMEAR 不合适。"
evidence_level: check
confidence: local_unverified
related_wiki:
  - computer_kb/wiki/errors/vasp_adsorption_energy_abnormal.md
related_records:
  - vasp-param-idipol-0159
  - vasp-param-encut-0116
  - vasp-param-ismear-0181
note: "Skeleton 级别。吸附能异常的具体数值阈值依赖文献对比。"
last_checked: 2026-05-24
exact_error: "Adsorption energy differs >0.3 eV from expected/literature (skeleton; no log yet)"
symptom: "E_ads 与文献值差 >0.3 eV; 或 E_ads 随 slab 层数持续漂移 (>0.05 eV/layer)"
likely_causes:
  - IDIPOL 偶极校正未开 (asymmetric slab)
  - E_slab+ads / E_slab / E_gas 三部分 ENCUT/PREC/k-points 不一致
  - ISMEAR=-3 (固定占据) 或 -5 (tetrahedron) 错误用于金属 slab 结构优化
  - slab 层数不够 (收敛需 >=4 layers for Pt(111))
diagnosis_steps:
  - 检查 INCAR 是否有 IDIPOL=3 + LDIPOL=.TRUE.
  - diff 三部分计算的 INCAR 和 KPOINTS
  - 检查 ISMEAR 是否适合金属体系
  - slab 收敛性: 用 4/5/6 layers 测试 E_ads 收敛
fixes:
  - "开启偶极校正: IDIPOL=3 + LDIPOL=.TRUE."
  - "统一三部分 ENCUT/PREC/k-points"
  - "ISMEAR=0 + SIGMA=0.1 for metal slab"
verified_on: "skeleton"
unsafe_fixes:
  - "人为调参数让吸附能'看起来对'——机理结论全不可信"
~~~

## p5-vasp-dos-dband-abnormal-2026-05-24

~~~yaml
record_id: vasp-error-dos-dband-abnormal-0005
record_type: error
scope: single_software
software:
  - VASP
topic: "DOS/d-band 计算异常: d-band center 偏差>0.2 eV 或 PDOS 数据缺失"
source_type: official_doc
source_ref: "https://www.vasp.at/wiki/LORBIT"
version_or_doc_date: VASP 6.x; checked 2026-05-24
claim: "DOS 质量问题的常见原因: ICHARG 设置不当、LORBIT 不够、NEDOS 太粗、ISMEAR 不匹配。"
evidence_level: check
confidence: local_unverified
related_wiki:
  - computer_kb/wiki/errors/vasp_dos_dband_abnormal.md
related_records:
  - vasp-param-icharg-0156
  - vasp-param-lorbit-0286
  - vasp-param-nedos-0449
note: "Skeleton 级别。d-band center 和 Bader charge 依赖外部 post-processing。"
last_checked: 2026-05-24
exact_error: "d-band center differs >0.2 eV from literature OR PDOS data missing (skeleton)"
symptom: "d-band center 与文献差 >0.2 eV; Bader charge 总和 != 总电子数; PROCAR 只有 spd 无 lm 分解"
likely_causes:
  - ICHARG=11 但缺少前一步 SCF 输出的 CHGCAR
  - LORBIT<10 (PROCAR 无 lm-decomposed 输出)
  - NEDOS=301 (默认) -> d-band center 离散误差 ~0.1 eV
  - ISMEAR=-5 (tetrahedron) 但 k-mesh 不够 (需要 >=4x4x1)
diagnosis_steps:
  - 确认 non-SCF 前有 CHGCAR
  - grep LORBIT INCAR -> <10 则升级
  - grep NEDOS INCAR -> <2000 则升级
  - ISMEAR=-5 需要检查 k 点密度
fixes:
  - "ICHARG=2 SCF -> CHGCAR -> ICHARG=11 non-SCF"
  - "LORBIT=11 + NEDOS=2000"
  - "ISMEAR=-5 for DOS (tetrahedron) if k-mesh >=4x4x1"
verified_on: "skeleton"
unsafe_fixes:
  - "LORBIT<10 + 调 RWIGS 凑 Bader charge——伪科学调参"
~~~

## p7-lammps-md-energy-nan-2026-05-24

~~~yaml
record_id: lammps-error-energy-nan-0007
record_type: error
scope: single_software
software:
  - LAMMPS
topic: "LAMMPS MD 中 total energy 突然变为 NaN 或 Inf"
source_type: official_doc
source_ref: "https://docs.lammps.org/Errors.html"
version_or_doc_date: LAMMPS 30Mar2026; checked 2026-05-24
claim: "MD 能量 NaN 的最常见原因: timestep 过大、初始结构重叠、pair_coeff 不合理。"
evidence_level: check
confidence: local_unverified
related_wiki:
  - computer_kb/wiki/errors/lammps_md_energy_nan.md
related_records:
  - lammps-md-cmd-timestep-0012
  - lammps-md-cmd-pair-coeff-0009
note: "Skeleton 级别。真实 LAMMPS NaN 通常伴随具体错误信息。"
last_checked: 2026-05-24
exact_error: "Non-numeric atom coord/velocity (skeleton)"
symptom: "thermo 输出中 total energy 突然 = NaN 或 Inf; 模拟中断"
likely_causes:
  - timestep 过大 (H 含体系 >1.0 fs)
  - 初始结构原子重叠 (d < 0.5 A)
  - pair_coeff 中 model 文件路径不存在或元素映射错误
diagnosis_steps:
  - 检查 timestep 值和单位 (metal: ps)
  - 用 ASE/VMD 检查初始结构最短原子距离
  - 确认 pair_coeff 中 model 文件可读; 元素顺序与 data 文件一致
fixes:
  - "timestep 减半: 0.5 -> 0.25 fs"
  - "先 minimize + 短 NVE 测试 (100 steps)"
  - "检查 ML model 文件路径和元素列表"
verified_on: "skeleton"
unsafe_fixes:
  - "fix langevin 强 damping + ignore lost atoms——治标不治本"
~~~

## seed11-vasp-aimd-temperature-runaway-2026-05-26

~~~yaml
record_id: vasp-error-aimd-temperature-runaway-0001
record_type: error
scope: single_software
software:
  - VASP
topic: AIMD NVT 温度失控与 blowup
source_type: local_verified
source_ref: local VASP 5.4.4 verification; scheduler job IDs 32617-32625, run dirs scf/, aimd/, phase2_nh/ (evidence details in computer_kb/wiki/errors/aimd_temperature_runaway.md §6)
version_or_doc_date: VASP 5.4.4; verified 2026-05-26
claim: 当 AIMD 从经典力场预平衡构型启动时，SPC/E->PBE-D3 势能面落差导致前几步产生巨大局部力 (RMS 70+ eV/A)，Nose-Hoover (MDALGO=2/4) 和 Langevin (MDALGO=3) 恒温器均无法有效处理，导致温度飙升或 MD blowup。正确方案是先用 Andersen (MDALGO=1, ANDERSEN_PROB=0.2) 做暴力热化，再用 Nose-Hoover 平衡。
evidence_level: must
confidence: local_verified
related_wiki:
  - computer_kb/wiki/errors/aimd_temperature_runaway.md
related_records:
  - vasp-md-workflow-andersen-cascade-0042
note: 本记录为 Pt(100)/25H2O/Na+/OH-/NH3 体系本地验证。SMASS=-1 是 velocity scaling 的判断亦由 VASP Wiki NBLOCK 页面印证 ("NBLOCK controls how often the kinetic energy is scaled if SMASS=-1")，见 https://www.vasp.at/wiki/NBLOCK。适用于其他经典力场->DFT AIMD 过渡场景。
last_checked: 2026-05-26
exact_error: "temperature 从 ~2000K 持续上升至 80000+ K (OUTCAR 显示 temperature******** 或 97,000 K)"
symptom: AIMD NVT 运行中温度失控，连续上升不收敛至 TEBEG，最终 MD blowup 导致原子飞出/重叠
likely_causes:
  - 经典力场预平衡构型在 DFT 势能面上有巨大残余力 (RMS 10-70+ eV/A)
  - Nose-Hoover 是全局恒温器，凭总动能间接控温，局部力尖峰无法即时响应
  - Langevin 随机力分量在力场混乱时加剧扰动，反而加速崩溃
  - SMASS=-1 只是 velocity scaling (Berendsen-like)，不产生正则系综
  - IBRION=2 CG 弛豫在水体系中会拉断化学键 (NH3 解体，H 游离)
diagnosis_steps:
  - 检查 OUTCAR 中 'temperature' 行：若首步即 >1000K 或持续上升，判为热化失败
  - 检查 'FORCES: max atom, RMS'：初始 RMS>10 eV/A 说明力失配严重
  - 确认恒温器类型：MDALGO=1(Andersen)/2(Nose-Hoover)/3(Langevin)/4(NHC)
  - 若使用 SMASS=-1：这不是恒温器，切换到正值或换 Andersen
  - 若力 RMS >50 eV/A 且 Langevin：停掉，换 Andersen
fixes:
  - Phase 1: Andersen 热化 (MDALGO=1, ANDERSEN_PROB=0.2, NSW=200)
  - Phase 2: Nose-Hoover 平衡 (MDALGO=2, SMASS=0.5, NSW=500)
  - Phase 3: Nose-Hoover 生产 (MDALGO=2, SMASS=0, NSW=500+)
verified_on: Pt(100) 3x3 + 25H2O + Na+ + OH- + NH3, 109 atoms, VASP 5.4.4, 56-core CPU
unsafe_fixes:
  - 不要用 IBRION=2 CG 弛豫替代热化——会破坏水分子/NH3 结构
  - 不要加大 Langevin 摩擦系数 (gamma) 试图硬压——随机力更大更不稳定
  - 不要延长 Nose-Hoover 步数等收敛——SMASS=-1 本就不产生 NVT
~~~

## Obsidian Links

- [[lammps_lost_atoms]]
- [[lammps_non_numeric_instability]]
- [[lammps_out_of_range_atoms]]
- [[lammps_unrecognized_style_package]]
- [[lammps_energy_stress_not_tallied]]
- [[aimd_temperature_runaway]]
