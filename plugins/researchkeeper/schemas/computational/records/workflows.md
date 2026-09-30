# Workflow records

> Cross-software workflow records for practical computation routes.
> Sources are the official VASP and LAMMPS documentation URLs recorded in each entry.
> These records describe workflow checkpoints and evidence routing. They are not local runtime validation unless `local_status` says so.

## seed12-vasp-aimd-andersen-cascade-2026-05-26

~~~yaml
record_id: vasp-md-workflow-andersen-cascade-0042
record_type: workflow
scope: single_software
software:
  - VASP
topic: AIMD Andersen 三级热化工作流
source_type: local_verified
source_ref: local VASP 5.4.4 verification; scheduler job IDs 32617-32625, run dirs scf/, aimd/, phase2_nh/ (evidence details in computer_kb/wiki/errors/aimd_temperature_runaway.md §6)
version_or_doc_date: VASP 5.4.4; verified 2026-05-26
claim: 对于经典力场→DFT AIMD 过渡，必须用三级热化级联：Phase 1 Andersen 暴力热化 (MDALGO=1, ANDERSEN_PROB=0.2, NSW=~200) → Phase 2 Nosé-Hoover 平衡 (MDALGO=2, SMASS=0.5, NSW=~500) → Phase 3 Nosé-Hoover 生产 (MDALGO=2, SMASS=0, NSW=500+)。每一段从上一段 CONTCAR 续跑。
evidence_level: must
confidence: local_verified
related_wiki:
  - computer_kb/wiki/errors/aimd_temperature_runaway.md
related_records:
  - vasp-error-aimd-temperature-runaway-0001
  - vasp-md-param-mdalgo-0006
  - vasp-md-param-andersen-prob-0007
  - vasp-md-param-smass-0008
note: 109 原子 Pt(100)/H₂O/Na⁺/OH⁻/NH₃ 体系本地验证。更大体系可降低 ANDERSEN_PROB 至 0.1；更小体系可增至 0.3。
last_checked: 2026-05-26
goal: 让经典力场预平衡构型安全过渡到 DFT AIMD NVT，避免温度失控和 MD blowup
inputs:
  - 经典力场预平衡后的 POSCAR (如 LAMMPS SPC/E)
  - 标准电子结构参数 (ENCUT, EDIFF, KPOINTS, POTCAR)
outputs:
  - Phase 1 CONTCAR (~200 步 Andersen 热化后，温度已稳定在目标值)
  - Phase 2 CONTCAR (~500 步 Nosé-Hoover 平衡后)
  - Phase 3 CONTCAR + XDATCAR (生产段数据)
steps:
  - Phase 1: INCAR 设 MDALGO=1, ANDERSEN_PROB=0.2, NSW=200, TEBEG=TEEND=330。Andersen 每步以概率 0.2 重设各原子速度为 Maxwell-Boltzmann 分布，打破力→动能正反馈
  - 检查 Phase 1 完成后的 OUTCAR 温度：应稳定在 330±50K。若均值偏高 (>400K) 延长 NSW
  - Phase 2: cp CONTCAR POSCAR (保留 WAVECAR), 改 MDALGO=2, SMASS=0.5, NSW=500, 移除 ANDERSEN_PROB。Nosé-Hoover 做 NVT 平衡
  - 检查 Phase 2 完成后的温度分布和力 RMS。力 RMS 应在 0.5-2 eV/Å 范围内
  - Phase 3: cp CONTCAR POSCAR, MDALGO=2, SMASS=0, NSW=500+。Nosé-Hoover 生产
checkpoints:
  - Phase 1 温度应在 ~13 步内从峰值 (500-1000K) 降至 330K 附近
  - Phase 1 未发生 MD blowup
  - Phase 2 力 RMS 逐步下降，无温度偏移
  - Phase 3 温度稳定在目标值 ±60K
failure_links:
  - vasp-error-aimd-temperature-runaway-0001
  - vasp-md-param-mdalgo-0006
local_status: local_verified
~~~

## Obsidian Links





- [[lammps_md_basics]]
- [[aimd_temperature_runaway]]

