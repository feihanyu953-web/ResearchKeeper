# VASP MD thermostat/ensemble 联动链

> record_type: relation | scope: single_software | software: [VASP]

~~~yaml
record_id: rel-vasp-md-thermostat-chain-0004
record_type: relation
scope: single_software
software:
  - VASP
topic: "MDALGO thermostat 选择 → companion tags 强制依赖 → ISIF 配合"
source_type: official_doc
source_ref: "https://www.vasp.at/wiki/MDALGO"
version_or_doc_date: "VASP 6.x; checked 2026-05-24"
claim: >
  MDALGO 每个取值对应一组强制配套参数（companion tags），且与 ISIF 有互斥约束。
  选错或遗漏 companion tag 会导致 MD 行为不符合预期（NVE 而非 NVT 等）。
evidence_level: should
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/vasp_aimd_md_parameters.md
  - computer_kb/wiki/concepts/vasp_md_thermostat_guide.md
related_records:
  - vasp-md-param-mdalgo-0006
  - vasp-md-param-isif-0017
  - vasp-md-param-smass-0008
  - vasp-md-param-langevin-gamma-0009
  - vasp-md-param-langevin-gamma-l-0010
  - vasp-md-param-pmass-0011
  - vasp-md-param-andersen-prob-0007
  - vasp-md-param-nhc-nchains-0012
  - vasp-md-param-nhc-period-0015
  - vasp-md-param-csvr-period-0016
  - vasp-md-param-potim-0003
  - vasp-md-param-nsw-0002
  - vasp-md-param-tebeg-0004
note: "companion tag 规则来自 VASP Wiki MDALGO 页面。Pt/水界面的具体推荐值(LANGEVIN_GAMMA等)基于领域经验,待本地实测验证。"
last_checked: 2026-05-24

relation_type: requires_companion
relation_basis:
  - official_cross_ref
  - domain_knowledge

parameters:
  - {name: MDALGO, role: "thermostat/ensemble 选择器", record: vasp-md-param-mdalgo-0006}
  - {name: ISIF, role: "cell 自由度控制", record: vasp-md-param-isif-0017}
  - {name: ANDERSEN_PROB, role: "Andersen碰撞概率", record: vasp-md-param-andersen-prob-0007}
  - {name: SMASS, role: "NH热浴耦合质量", record: vasp-md-param-smass-0008}
  - {name: LANGEVIN_GAMMA, role: "Langevin摩擦系数", record: vasp-md-param-langevin-gamma-0009}
  - {name: LANGEVIN_GAMMA_L, role: "cell自由度Langevin摩擦", record: vasp-md-param-langevin-gamma-l-0010}
  - {name: PMASS, role: "cell fictitious mass", record: vasp-md-param-pmass-0011}
  - {name: NHC_NCHAINS, role: "NH chain长度", record: vasp-md-param-nhc-nchains-0012}
  - {name: NHC_PERIOD, role: "NH chain周期", record: vasp-md-param-nhc-period-0015}
  - {name: CSVR_PERIOD, role: "CSVR耦合周期", record: vasp-md-param-csvr-period-0016}
  - {name: POTIM, role: "timestep/步长", record: vasp-md-param-potim-0003}
  - {name: NSW, role: "最大步数", record: vasp-md-param-nsw-0002}
  - {name: TEBEG, role: "初始温度", record: vasp-md-param-tebeg-0004}

relation_rules:
  - id: M1
    type: requires_companion
    from: "MDALGO=1"
    to: ANDERSEN_PROB
    detail: "Andersen thermostat 需指定碰撞概率"
    decision: "ANDERSEN_PROB ≈ 0.1-0.2 (每步每个原子碰撞概率)"
    consequence: "概率过小 → 热化慢；过大 → 随机扰动过大"

  - id: M2
    type: requires_companion
    from: "MDALGO=2"
    to: SMASS
    detail: "Nosé-Hoover 需指定热浴耦合质量"
    decision: "SMASS ~ 0.5-3.0 for 100-500 atoms; SMASS=0 → NVE"
    consequence: "SMASS 不合适 → 温度振荡或过阻尼；SMASS=0 → 退化为 NVE"

  - id: M3
    type: requires_companion
    from: "MDALGO=3"
    to: LANGEVIN_GAMMA
    detail: "Langevin 需每个元素指定摩擦系数"
    decision: "{H: 10.0, O: 5.0, Pt: 1.0} ps⁻¹ for Pt/water"
    consequence: "缺 LANGEVIN_GAMMA → MD 行为未定义"

  - id: M4
    type: mutually_constrained
    from: "MDALGO=3"
    to: "ISIF"
    detail: "Langevin NVT (ISIF≤2+MDALGO=3) vs Langevin NpT (ISIF=3+MDALGO=3+LANGEVIN_GAMMA_L+PMASS) 是两套不同设置,不是互斥"
    decision: "NVT: MDALGO=3+ISIF≤2+LANGEVIN_GAMMA; NpT: MDALGO=3+ISIF=3+LANGEVIN_GAMMA_L+PMASS"
    consequence: "NpT缺LANGEVIN_GAMMA_L/PMASS → cell自由度不完整"

  - id: M5
    type: requires_companion
    from: "MDALGO=4"
    to: "NHC_NCHAINS + NHC_PERIOD"
    detail: "Nosé-Hoover chain 需指定链长和周期"
    decision: "NCHAINS=3-5 (典型值); PERIOD~50-100×POTIM"
    consequence: "缺 NHC_NCHAINS/NHC_PERIOD → 链热浴行为未定义或报错"

  - id: M6
    type: requires_companion
    from: "MDALGO=5"
    to: CSVR_PERIOD
    detail: "CSVR (Bussi) thermostat 需指定耦合周期"
    decision: "CSVR_PERIOD~50-100×POTIM"
    consequence: "缺 CSVR_PERIOD → 耦合周期未定义 → 恒温行为异常"

  - id: M7
    type: mutually_constrained
    from: POTIM
    to: NSW
    detail: "POTIM × NSW = 名义总模拟时长"
    decision: "按目标模拟时长反推: 5 ps = 5000 × 1 fs (POTIM=1.0)"
    consequence: "NSW 不足 → 采样时长不够；过大 → 计算浪费"

  - id: M8
    type: coupled_accuracy
    from: TEBEG
    to: POTIM
    detail: "轻元素 (H) 在高温 (>400K) 下需更小 timestep → POTIM 减至 0.5 fs; 日常室温 1.0 fs 通常可接受"
    decision: ">400K 含 H 体系 → POTIM=0.5 fs; 室温 → 1.0 fs"
    consequence: "高温大 timestep → 温度漂移或能量不守恒"

failure_signatures:
  - symptom: "MD 表现 NVE (温度漂移) 而非 NVT"
    likely: "MDALGO 设了但 companion tag 缺失或不对"
  - symptom: "温度漂移 > 50 K"
    likely: "thermostat coupling 太弱"
  - symptom: "cell 意外变化"
    likely: "ISIF 与 MDALGO 组合不正确"
  - symptom: "离子步爆炸"
    likely: "POTIM 过大或初始结构重叠"
~~~
