# VASP records

> Source: VASP Wiki Category:INCAR_tag official category API.
>
> Batch type: index-level full import. Each record confirms an official INCAR tag page and source URL; definition/default/risk fields are not extracted page-by-page yet.

## vasp-incar-tag-index-2026-05-21

- source_type: official_doc
- source_ref: https://www.vasp.at/wiki/Category:INCAR_tag
- evidence_source: https://www.vasp.at/wiki/Category:INCAR_tag
- imported_count: 612  # 607 official VASP index records + 5 VASPsol extension records (0400-0404)
- import_scope: all pages returned by official Category:INCAR_tag API on 2026-05-21

~~~yaml
record_id: vasp-param-addgrid-0001
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ADDGRID"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ADDGRID
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ADDGRID" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ADDGRID"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-aexx-0002
record_type: parameter
scope: single_software
software:
  - VASP
topic: "AEXX"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/AEXX
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "AEXX" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "AEXX"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-aggac-0003
record_type: parameter
scope: single_software
software:
  - VASP
topic: "AGGAC"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/AGGAC
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "AGGAC" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "AGGAC"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-aggax-0004
record_type: parameter
scope: single_software
software:
  - VASP
topic: "AGGAX"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/AGGAX
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "AGGAX" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "AGGAX"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-aldac-0005
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ALDAC"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ALDAC
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ALDAC" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ALDAC"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-aldax-0006
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ALDAX"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ALDAX
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ALDAX" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ALDAX"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-algo-0007
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ALGO"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ALGO
version_or_doc_date: VASP Wiki; checked 2026-05-24
claim: "ALGO 选择电子步迭代算法，决定 SCF 收敛的速度和稳健性。"
evidence_level: should
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/vasp_scf_accuracy_chain.md
related_records:
  - vasp-param-ediff-0053
  - vasp-param-amix-0012
  - rel-vasp-scf-precision-chain-0001
note: "层级: VeryFast < Fast < Normal < All。越往后越稳健但每步更慢。默认 Normal 适合大多数场景。"
last_checked: 2026-05-24
parameter_name: "ALGO"
file_or_context: INCAR
definition: "电子步优化算法选择。确定从当前波函数迭代到自洽解的方法。"
default_behavior: "Normal (VASP 5.x 起默认)"
common_use:
  - {when: "几何优化/SCF 收敛", value: Normal, priority: should}
  - {when: "SCF 不收敛 (含 d 电子金属/界面)", value: All, priority: should}
  - {when: "大体系快速初筛", value: "VeryFast or Fast", priority: ok}
  - {when: "AIMD (每步仅需粗略收敛)", value: "Fast", priority: ok}
risk_if_misused:
  - "ALGO=VeryFast/Fast → 收敛不平滑 → 力可能不准 → 不适合力敏感计算"
  - "ALGO=All 最稳健但每步耗时明显增加"
parameter_relations:
  - target: AMIX
    example_status: needs_verification
    relation: coupled_accuracy
    desc: "ALGO=All 时 AMIX 可以更小 (0.1-0.2)"
  - target: EDIFF
    example_status: needs_verification
    relation: coupled_accuracy
    desc: "Fast 算法可能达不到标称 EDIFF 精度"
domain_guidance:
  - rule: "含 Pt/d-electron 金属 + interface water → ALGO=Normal 起步; 不收敛→All"
    example_status: needs_verification
    applies_to: {metals: [Pt, Ni, Co, Fe, Cu], interface: [metal_water]}
    value: "Normal→All (fallback)"
    reason: "d 电子 + 水界面 → SCF 收敛困难; All 用全对角化更稳健"
related_parameters:
  - AMIX
  - BMIX
  - EDIFF
~~~

~~~yaml
record_id: vasp-param-alpha-vdw-0008
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ALPHA VDW"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ALPHA_VDW
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ALPHA VDW" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ALPHA VDW"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-amggac-0009
record_type: parameter
scope: single_software
software:
  - VASP
topic: "AMGGAC"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/AMGGAC
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "AMGGAC" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "AMGGAC"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-amggax-0010
record_type: parameter
scope: single_software
software:
  - VASP
topic: "AMGGAX"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/AMGGAX
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "AMGGAX" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "AMGGAX"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-amin-0011
record_type: parameter
scope: single_software
software:
  - VASP
topic: "AMIN"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/AMIN
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "AMIN" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "AMIN"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-amix-0012
record_type: parameter
scope: single_software
software:
  - VASP
topic: "AMIX"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/AMIX
version_or_doc_date: VASP Wiki; checked 2026-05-24
claim: "AMIX 控制电荷密度混合中 Pulay mixing 的线性混合参数。SCF 不收敛时调低 AMIX 往往有效。"
evidence_level: should
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/vasp_scf_accuracy_chain.md
related_records:
  - vasp-param-algo-0007
  - vasp-param-bmix-0020
  - vasp-param-amix-mag-0013
note: "AMIX 降低 → 更保守的混合 → 更容易收敛但需要更多电子步。d 电子体系/界面水常常需要 AMIX=0.1-0.2。"
last_checked: 2026-05-24
parameter_name: "AMIX"
file_or_context: INCAR
definition: "电荷密度混合的线性混合比例。新密度 = (1-AMIX)×旧 + AMIX×新。值越小混合越保守。"
default_behavior: "AMIX=0.4 (VASP 默认; ALGO=All 时默认更小)"
common_use:
  - {when: "一般计算", value: 0.4 (默认), priority: ok}
  - {when: "含 d 电子金属 + 界面", value: 0.2, priority: should}
  - {when: "SCF 仍然不收敛", value: 0.1, priority: should}
  - {when: "AMIX=0.05", value: "极端保守，收敛极慢但几乎必收敛", priority: avoid}
risk_if_misused:
  - "AMIX 过大 (0.4+) + d 电子体系 → charge sloshing → SCF 不收敛"
  - "AMIX 过小 (0.05) → 收敛极慢 → 每个电子步进步极小"
parameter_relations:
  - target: BMIX
    example_status: needs_verification
    relation: coupled_accuracy
    desc: "AMIX 控制初始混合步长; BMIX 控制后续步的 mixing 历史权重"
  - target: AMIX_MAG
    example_status: needs_verification
    relation: coupled_accuracy
    desc: "磁性体系的磁矩混合参数; 需与 AMIX 同步降低"
  - target: ALGO
    example_status: needs_verification
    relation: coupled_accuracy
    desc: "ALGO=All 时内部已做阻尼，AMIX 可以设稍大"
domain_guidance:
  - rule: "Pt + water interface → AMIX 从 0.2 起步"
    example_status: needs_verification
    applies_to: {metals: [Pt, Ni, Co], interface: [metal_water]}
    value: 0.2
    reason: "d 电子 + 液态水 → 电荷密度振荡 → 需要保守混合"
related_parameters:
  - BMIX
  - AMIX_MAG
  - ALGO
~~~

~~~yaml
record_id: vasp-param-amix-mag-0013
record_type: parameter
scope: single_software
software:
  - VASP
topic: "AMIX_MAG"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/AMIX_MAG
version_or_doc_date: VASP Wiki; checked 2026-05-24
claim: "AMIX_MAG 控制磁矩密度混合的线性混合参数。SCF 不收敛时与 AMIX 同步降低。"
evidence_level: should
confidence: official
related_wiki: []
related_records: [vasp-param-amix-0012, vasp-param-bmix-mag-0021]
note: "磁性体系 (Ni/Co/Fe) SCF 不收敛时，AMIX_MAG 从 1.6→0.4-0.8，与 AMIX 同步。"
last_checked: 2026-05-24
parameter_name: "AMIX_MAG"
file_or_context: INCAR
definition: "磁矩密度混合的线性混合比例。值越小混合越保守但收敛越慢。"
default_behavior: "AMIX_MAG=1.6"
common_use:
  - {when: "正常磁性计算", value: 1.6, priority: ok}
  - {when: "磁性体系 SCF 不收敛", value: 0.4-0.8, priority: should}
risk_if_misused:
  - "AMIX_MAG 过大 + d 电子 → 磁矩振荡 → SCF 不收敛"
parameter_relations:
  - {example_status: needs_verification, target: AMIX, relation: coupled_accuracy, desc: "AMIX 和 AMIX_MAG 需同步降低"}
  - {example_status: needs_verification, target: BMIX_MAG, relation: coupled_accuracy}
domain_guidance:
  - {example_status: needs_verification, rule: "Ni/Co/Fe slab SCF 不收敛 → AMIX_MAG=0.8", value: 0.8}
related_parameters: [AMIX, BMIX_MAG]
~~~

~~~yaml
record_id: vasp-param-andersen-prob-0014
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ANDERSEN PROB"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ANDERSEN_PROB
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ANDERSEN PROB" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ANDERSEN PROB"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-antires-0015
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ANTIRES"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ANTIRES
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ANTIRES" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ANTIRES"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-apaco-0016
record_type: parameter
scope: single_software
software:
  - VASP
topic: "APACO"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/APACO
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "APACO" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "APACO"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-bandgap-0017
record_type: parameter
scope: single_software
software:
  - VASP
topic: "BANDGAP"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/BANDGAP
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "BANDGAP" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "BANDGAP"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-bext-0018
record_type: parameter
scope: single_software
software:
  - VASP
topic: "BEXT"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/BEXT
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "BEXT" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "BEXT"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-bexx-0019
record_type: parameter
scope: single_software
software:
  - VASP
topic: "BEXX"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/BEXX
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "BEXX" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "BEXX"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-bmix-0020
record_type: parameter
scope: single_software
software:
  - VASP
topic: "BMIX"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/BMIX
version_or_doc_date: VASP Wiki; checked 2026-05-24
claim: "BMIX 控制 Pulay mixing 中的剪切混合参数 (cutoff mixing)。与 AMIX 配合调节后续混合步的行为。"
evidence_level: should
confidence: official
related_wiki: [computer_kb/wiki/concepts/vasp_scf_accuracy_chain.md]
related_records:
  - vasp-param-amix-0012
  - rel-vasp-scf-precision-chain-0001
note: "BMIX 配合 AMIX 使用。SCF 不收敛时若已降 AMIX，可尝试同步调 BMIX (如 1.0→0.1)。"
last_checked: 2026-05-24
parameter_name: "BMIX"
file_or_context: INCAR
definition: "Pulay mixing 的 cutoff mixing 参数。控制混合中旧密度的贡献截断方式。"
default_behavior: "BMIX=1.0"
common_use:
  - {when: "一般计算", value: 1.0, priority: ok}
  - {when: "SCF 不收敛", value: "0.01-0.1", priority: should}
risk_if_misused:
  - "BMIX 过大 + d 电子体系 → 混合不稳定 → SCF 振荡"
parameter_relations:
  - {example_status: needs_verification, target: AMIX, relation: coupled_accuracy, desc: "AMIX 控制初始步; BMIX 控制后续步剪切"}
domain_guidance:
  - {example_status: needs_verification, rule: "d-electron metal + SCF 不收敛 → BMIX≤0.1", applies_to: {metals: [Pt, Ni, Co]}, value: 0.1}
related_parameters: [AMIX]
~~~

~~~yaml
record_id: vasp-param-bmix-mag-0021
record_type: parameter
scope: single_software
software:
  - VASP
topic: "BMIX_MAG"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/BMIX_MAG
version_or_doc_date: VASP Wiki; checked 2026-05-24
claim: "BMIX_MAG 控制磁矩密度混合的剪切参数。SCF 不收敛时与 AMIX_MAG 同步降低。"
evidence_level: check
confidence: official
related_wiki: []
related_records: [vasp-param-amix-mag-0013]
note: "磁性体系 SCF 不收敛时，与 AMIX_MAG 同步降低 BMIX_MAG。"
last_checked: 2026-05-24
parameter_name: "BMIX_MAG"
file_or_context: INCAR
definition: "磁性密度混合的剪切参数。"
default_behavior: "BMIX_MAG=1.0"
common_use:
  - {when: "正常磁性计算", value: 1.0, priority: ok}
  - {when: "SCF 不收敛", value: 0.1, priority: should}
parameter_relations:
  - {example_status: needs_verification, target: AMIX_MAG, relation: coupled_accuracy}
domain_guidance:
  - {example_status: needs_verification, rule: "Ni/Co/Fe slab SCF 不收敛 → BMIX_MAG=0.1"}
related_parameters: [AMIX_MAG]
~~~

~~~yaml
record_id: vasp-param-bparam-0022
record_type: parameter
scope: single_software
software:
  - VASP
topic: "BPARAM"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/BPARAM
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "BPARAM" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "BPARAM"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-bseelectron-0023
record_type: parameter
scope: single_software
software:
  - VASP
topic: "BSEELECTRON"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/BSEELECTRON
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "BSEELECTRON" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "BSEELECTRON"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-bsehole-0024
record_type: parameter
scope: single_software
software:
  - VASP
topic: "BSEHOLE"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/BSEHOLE
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "BSEHOLE" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "BSEHOLE"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-bseprec-0025
record_type: parameter
scope: single_software
software:
  - VASP
topic: "BSEPREC"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/BSEPREC
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "BSEPREC" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "BSEPREC"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ch-amplification-0026
record_type: parameter
scope: single_software
software:
  - VASP
topic: "CH AMPLIFICATION"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/CH_AMPLIFICATION
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "CH AMPLIFICATION" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "CH AMPLIFICATION"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ch-lspec-0027
record_type: parameter
scope: single_software
software:
  - VASP
topic: "CH LSPEC"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/CH_LSPEC
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "CH LSPEC" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "CH LSPEC"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ch-nedos-0028
record_type: parameter
scope: single_software
software:
  - VASP
topic: "CH NEDOS"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/CH_NEDOS
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "CH NEDOS" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "CH NEDOS"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ch-sigma-0029
record_type: parameter
scope: single_software
software:
  - VASP
topic: "CH SIGMA"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/CH_SIGMA
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "CH SIGMA" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "CH SIGMA"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-checkpoint-fd-0030
record_type: parameter
scope: single_software
software:
  - VASP
topic: "CHECKPOINT FD"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/CHECKPOINT_FD
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "CHECKPOINT FD" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "CHECKPOINT FD"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-cll-0031
record_type: parameter
scope: single_software
software:
  - VASP
topic: "CLL"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/CLL
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "CLL" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "CLL"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-cln-0032
record_type: parameter
scope: single_software
software:
  - VASP
topic: "CLN"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/CLN
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "CLN" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "CLN"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-clnt-0033
record_type: parameter
scope: single_software
software:
  - VASP
topic: "CLNT"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/CLNT
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "CLNT" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "CLNT"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-clz-0034
record_type: parameter
scope: single_software
software:
  - VASP
topic: "CLZ"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/CLZ
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "CLZ" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "CLZ"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-cmbj-0035
record_type: parameter
scope: single_software
software:
  - VASP
topic: "CMBJ"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/CMBJ
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "CMBJ" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "CMBJ"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-cmbja-0036
record_type: parameter
scope: single_software
software:
  - VASP
topic: "CMBJA"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/CMBJA
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "CMBJA" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "CMBJA"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-cmbjb-0037
record_type: parameter
scope: single_software
software:
  - VASP
topic: "CMBJB"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/CMBJB
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "CMBJB" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "CMBJB"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-cmbje-0038
record_type: parameter
scope: single_software
software:
  - VASP
topic: "CMBJE"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/CMBJE
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "CMBJE" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "CMBJE"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-construction-deg-threshold-0039
record_type: parameter
scope: single_software
software:
  - VASP
topic: "Construction:DEG THRESHOLD"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/Construction%3ADEG_THRESHOLD
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "Construction:DEG THRESHOLD" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "Construction:DEG THRESHOLD"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-construction-maxdis-0040
record_type: parameter
scope: single_software
software:
  - VASP
topic: "Construction:MAXDIS"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/Construction%3AMAXDIS
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "Construction:MAXDIS" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "Construction:MAXDIS"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-cparam-0041
record_type: parameter
scope: single_software
software:
  - VASP
topic: "CPARAM"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/CPARAM
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "CPARAM" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "CPARAM"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-cshift-0042
record_type: parameter
scope: single_software
software:
  - VASP
topic: "CSHIFT"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/CSHIFT
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "CSHIFT" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "CSHIFT"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-cutoff-mu-0043
record_type: parameter
scope: single_software
software:
  - VASP
topic: "CUTOFF MU"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/CUTOFF_MU
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "CUTOFF MU" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "CUTOFF MU"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-cutoff-sigma-0044
record_type: parameter
scope: single_software
software:
  - VASP
topic: "CUTOFF SIGMA"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/CUTOFF_SIGMA
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "CUTOFF SIGMA" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "CUTOFF SIGMA"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-cutoff-type-0045
record_type: parameter
scope: single_software
software:
  - VASP
topic: "CUTOFF TYPE"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/CUTOFF_TYPE
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "CUTOFF TYPE" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "CUTOFF TYPE"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-deper-0046
record_type: parameter
scope: single_software
software:
  - VASP
topic: "DEPER"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/DEPER
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "DEPER" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "DEPER"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-dftd4-model-0047
record_type: parameter
scope: single_software
software:
  - VASP
topic: "DFTD4 MODEL"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/DFTD4_MODEL
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "DFTD4 MODEL" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "DFTD4 MODEL"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-dftd4-xc-0048
record_type: parameter
scope: single_software
software:
  - VASP
topic: "DFTD4 XC"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/DFTD4_XC
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "DFTD4 XC" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "DFTD4 XC"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-dimer-dist-0049
record_type: parameter
scope: single_software
software:
  - VASP
topic: "DIMER DIST"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/DIMER_DIST
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "DIMER DIST" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "DIMER DIST"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-dipol-0050
record_type: parameter
scope: single_software
software:
  - VASP
topic: "DIPOL"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/DIPOL
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "DIPOL" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "DIPOL"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-dq-0051
record_type: parameter
scope: single_software
software:
  - VASP
topic: "DQ"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/DQ
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "DQ" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "DQ"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ebreak-0052
record_type: parameter
scope: single_software
software:
  - VASP
topic: "EBREAK"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/EBREAK
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "EBREAK" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "EBREAK"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ediff-0053
record_type: parameter
scope: single_software
software:
  - VASP
topic: "EDIFF"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/EDIFF
version_or_doc_date: VASP Wiki; checked 2026-05-24
claim: "EDIFF 控制电子步自洽收敛标准。当两步间总自由能变化 < EDIFF 时 SCF 停止。"
evidence_level: should
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/vasp_scf_accuracy_chain.md
related_records:
  - vasp-param-encut-0116
  - vasp-param-ediffg-0054
  - rel-vasp-scf-precision-chain-0001
note: "EDIFF 与 ENCUT 配合才有意义。ENCUT 低时紧 EDIFF 浪费计算。力收敛用 EDIFFG 而不是 EDIFF。"
last_checked: 2026-05-24
parameter_name: "EDIFF"
file_or_context: INCAR
definition: "电子步收敛标准 (eV)。总自由能在两步间变化 < |EDIFF| 判定为 SCF 收敛。"
default_behavior: "1E-4 eV (VASP 默认)"
common_use:
  - {when: "几何优化", value: "1E-6", priority: should}
  - {when: "AIMD 采样", value: "1E-5", priority: should}
  - {when: "快速初筛", value: "1E-4 (默认)", priority: ok}
  - {when: "声子/弹性常数", value: "1E-8", priority: should}
risk_if_misused:
  - "EDIFF=1E-6 配合 ENCUT=300 → 紧标准浪费在 incomplete basis set 上"
  - "EDIFF 太松 → 力不准确 → AIMD 轨迹不可信"
parameter_relations:
  - target: ENCUT
    example_status: needs_verification
    relation: coupled_accuracy
    desc: "先保证 ENCUT 够，再收紧 EDIFF"
  - target: EDIFFG
    example_status: needs_verification
    relation: "EDIFFG 控制力收敛 (eV/Å)，< 0 则力判据生效"
domain_guidance:
  - rule: "AIMD/力敏感 → EDIFF=1E-5"
    example_status: needs_verification
    applies_to: {tasks: [aimd, neb, phonon]}
    value: 1E-5
    reason: "平衡精度和速度; 配合 ENCUT≥400 使用"
related_parameters:
  - ENCUT
  - EDIFFG
~~~

~~~yaml
record_id: vasp-param-ediffg-0054
record_type: parameter
scope: single_software
software:
  - VASP
topic: "EDIFFG"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/EDIFFG
version_or_doc_date: VASP Wiki; checked 2026-05-24
claim: "EDIFFG 控制离子步力收敛标准。负值时激活力判据 (eV/Å)，正值退化为能量判据。"
evidence_level: should
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/vasp_neb_chain.md
related_records:
  - vasp-param-ediff-0053
  - vasp-param-images-0165
  - rel-vasp-neb-chain-0002
note: "NEB/CI-NEB 必须用负 EDIFFG 激活力收敛。-0.03 eV/Å 是常用起手值；更紧 -0.01 可提高 TS 精度。"
last_checked: 2026-05-24
parameter_name: "EDIFFG"
file_or_context: INCAR
definition: "离子步收敛标准。EDIFFG>0 → |E(i)-E(i-1)|<EDIFFG 收敛; EDIFFG<0 → max force < |EDIFFG| 收敛。"
default_behavior: "EDIFF×10 (正值，能量判据)"
common_use:
  - {when: "几何优化", value: "-0.03", priority: should}
  - {when: "CI-NEB TS 搜索", value: "-0.03", priority: should}
  - {when: "高精度 TS (声子验证用)", value: "-0.01", priority: should}
risk_if_misused:
  - "EDIFFG 用正值做力敏感计算 → 力可能未收敛 (< 1 eV/Å) 却判定为完成"
  - "EDIFFG 过紧 + 大体系 → NEB 每张图都要严格收敛 → 计算量爆炸"
parameter_relations:
  - target: IMAGES
    example_status: needs_verification
    relation: coupled_accuracy
  - target: EDIFF
    example_status: needs_verification
    relation: coupled_accuracy
    desc: "力收敛前先保证每步 SCF 收敛 (EDIFF)"
domain_guidance:
  - rule: "CI-NEB → EDIFFG=-0.03"
    example_status: needs_verification
    applies_to: {tasks: [neb, ci-neb]}
    value: -0.03
related_parameters:
  - EDIFF
  - IMAGES
~~~

~~~yaml
record_id: vasp-param-efermi-0055
record_type: parameter
scope: single_software
software:
  - VASP
topic: "EFERMI"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/EFERMI
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "EFERMI" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "EFERMI"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-efermi-nedos-0056
record_type: parameter
scope: single_software
software:
  - VASP
topic: "EFERMI NEDOS"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/EFERMI_NEDOS
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "EFERMI NEDOS" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "EFERMI NEDOS"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-efield-0057
record_type: parameter
scope: single_software
software:
  - VASP
topic: "EFIELD"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/EFIELD
version_or_doc_date: VASP Wiki; checked 2026-05-24
claim: "EFIELD 施加外部电场 (eV/Å)，用于模拟电化学界面偏压效应。需配合 IDIPOL。"
evidence_level: check
confidence: official
related_wiki: []
related_records: [vasp-param-idipol-0159, vasp-param-ldipol-0230]
note: "电化学模拟中 EFIELD 是粗粒度的偏压近似。更精确的电化学界面需隐式溶剂 (VASPsol) 或 explicit 离子。"
last_checked: 2026-05-24
parameter_name: "EFIELD"
file_or_context: INCAR
definition: "外加均匀电场 (eV/Å)，沿 IDIPOL 方向。"
default_behavior: "0.0 (无电场)"
common_use:
  - {when: "电化学界面偏压 proxy", value: "~0.1 eV/Å = ~1 V/Å (rough)", priority: check}
risk_if_misused:
  - "不加 IDIPOL/LDIPOL → 电场可能引起 slab 间 spurious 相互作用"
~~~

~~~yaml
record_id: vasp-param-efield-pead-0058
record_type: parameter
scope: single_software
software:
  - VASP
topic: "EFIELD PEAD"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/EFIELD_PEAD
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "EFIELD PEAD" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "EFIELD PEAD"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-efor-0059
record_type: parameter
scope: single_software
software:
  - VASP
topic: "EFOR"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/EFOR
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "EFOR" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "EFOR"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-eint-0060
record_type: parameter
scope: single_software
software:
  - VASP
topic: "EINT"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/EINT
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "EINT" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "EINT"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-elph-decompose-0061
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ELPH DECOMPOSE"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ELPH_DECOMPOSE
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ELPH DECOMPOSE" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ELPH DECOMPOSE"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-elph-driver-0062
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ELPH DRIVER"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ELPH_DRIVER
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ELPH DRIVER" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ELPH DRIVER"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-elph-fermi-nedos-0063
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ELPH FERMI NEDOS"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ELPH_FERMI_NEDOS
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ELPH FERMI NEDOS" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ELPH FERMI NEDOS"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-elph-ignore-imag-phonons-0064
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ELPH IGNORE IMAG PHONONS"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ELPH_IGNORE_IMAG_PHONONS
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ELPH IGNORE IMAG PHONONS" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ELPH IGNORE IMAG PHONONS"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-elph-ismear-0065
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ELPH ISMEAR"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ELPH_ISMEAR
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ELPH ISMEAR" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ELPH ISMEAR"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-elph-kspacing-0066
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ELPH KSPACING"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ELPH_KSPACING
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ELPH KSPACING" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ELPH KSPACING"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-elph-lr-0067
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ELPH LR"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ELPH_LR
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ELPH LR" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ELPH LR"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-elph-mode-0068
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ELPH MODE"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ELPH_MODE
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ELPH MODE" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ELPH MODE"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-elph-nbands-0069
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ELPH NBANDS"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ELPH_NBANDS
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ELPH NBANDS" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ELPH NBANDS"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-elph-nbands-sum-0070
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ELPH NBANDS SUM"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ELPH_NBANDS_SUM
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ELPH NBANDS SUM" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ELPH NBANDS SUM"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-elph-pot-fft-mesh-0071
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ELPH POT FFT MESH"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ELPH_POT_FFT_MESH
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ELPH POT FFT MESH" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ELPH POT FFT MESH"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-elph-pot-generate-0072
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ELPH POT GENERATE"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ELPH_POT_GENERATE
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ELPH POT GENERATE" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ELPH POT GENERATE"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-elph-pot-lattice-0073
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ELPH POT LATTICE"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ELPH_POT_LATTICE
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ELPH POT LATTICE" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ELPH POT LATTICE"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-elph-prepare-0074
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ELPH PREPARE"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ELPH_PREPARE
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ELPH PREPARE" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ELPH PREPARE"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-elph-run-0075
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ELPH RUN"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ELPH_RUN
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ELPH RUN" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ELPH RUN"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-elph-scattering-approx-0076
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ELPH SCATTERING APPROX"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ELPH_SCATTERING_APPROX
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ELPH SCATTERING APPROX" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ELPH SCATTERING APPROX"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-elph-selfen-band-start-0077
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ELPH SELFEN BAND START"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ELPH_SELFEN_BAND_START
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ELPH SELFEN BAND START" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ELPH SELFEN BAND START"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-elph-selfen-band-stop-0078
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ELPH SELFEN BAND STOP"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ELPH_SELFEN_BAND_STOP
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ELPH SELFEN BAND STOP" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ELPH SELFEN BAND STOP"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-elph-selfen-broad-tol-0079
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ELPH SELFEN BROAD TOL"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ELPH_SELFEN_BROAD_TOL
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ELPH SELFEN BROAD TOL" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ELPH SELFEN BROAD TOL"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-elph-selfen-carrier-den-0080
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ELPH SELFEN CARRIER DEN"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ELPH_SELFEN_CARRIER_DEN
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ELPH SELFEN CARRIER DEN" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ELPH SELFEN CARRIER DEN"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-elph-selfen-carrier-den-range-0081
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ELPH SELFEN CARRIER DEN RANGE"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ELPH_SELFEN_CARRIER_DEN_RANGE
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ELPH SELFEN CARRIER DEN RANGE" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ELPH SELFEN CARRIER DEN RANGE"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-elph-selfen-carrier-per-cell-0082
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ELPH SELFEN CARRIER PER CELL"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ELPH_SELFEN_CARRIER_PER_CELL
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ELPH SELFEN CARRIER PER CELL" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ELPH SELFEN CARRIER PER CELL"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-elph-selfen-delta-0083
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ELPH SELFEN DELTA"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ELPH_SELFEN_DELTA
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ELPH SELFEN DELTA" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ELPH SELFEN DELTA"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-elph-selfen-dw-0084
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ELPH SELFEN DW"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ELPH_SELFEN_DW
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ELPH SELFEN DW" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ELPH SELFEN DW"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-elph-selfen-energy-window-0085
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ELPH SELFEN ENERGY WINDOW"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ELPH_SELFEN_ENERGY_WINDOW
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ELPH SELFEN ENERGY WINDOW" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ELPH SELFEN ENERGY WINDOW"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-elph-selfen-fan-0086
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ELPH SELFEN FAN"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ELPH_SELFEN_FAN
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ELPH SELFEN FAN" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ELPH SELFEN FAN"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-elph-selfen-g-skip-0087
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ELPH SELFEN G SKIP"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ELPH_SELFEN_G_SKIP
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ELPH SELFEN G SKIP" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ELPH SELFEN G SKIP"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-elph-selfen-gaps-0088
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ELPH SELFEN GAPS"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ELPH_SELFEN_GAPS
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ELPH SELFEN GAPS" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ELPH SELFEN GAPS"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-elph-selfen-ikpt-0089
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ELPH SELFEN IKPT"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ELPH_SELFEN_IKPT
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ELPH SELFEN IKPT" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ELPH SELFEN IKPT"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-elph-selfen-imag-skip-0090
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ELPH SELFEN IMAG SKIP"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ELPH_SELFEN_IMAG_SKIP
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ELPH SELFEN IMAG SKIP" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ELPH SELFEN IMAG SKIP"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-elph-selfen-kpts-0091
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ELPH SELFEN KPTS"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ELPH_SELFEN_KPTS
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ELPH SELFEN KPTS" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ELPH SELFEN KPTS"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-elph-selfen-mu-0092
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ELPH SELFEN MU"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ELPH_SELFEN_MU
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ELPH SELFEN MU" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ELPH SELFEN MU"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-elph-selfen-mu-range-0093
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ELPH SELFEN MU RANGE"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ELPH_SELFEN_MU_RANGE
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ELPH SELFEN MU RANGE" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ELPH SELFEN MU RANGE"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-elph-selfen-nw-0094
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ELPH SELFEN NW"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ELPH_SELFEN_NW
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ELPH SELFEN NW" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ELPH SELFEN NW"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-elph-selfen-static-0095
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ELPH SELFEN STATIC"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ELPH_SELFEN_STATIC
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ELPH SELFEN STATIC" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ELPH SELFEN STATIC"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-elph-selfen-temps-0096
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ELPH SELFEN TEMPS"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ELPH_SELFEN_TEMPS
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ELPH SELFEN TEMPS" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ELPH SELFEN TEMPS"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-elph-selfen-temps-range-0097
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ELPH SELFEN TEMPS RANGE"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ELPH_SELFEN_TEMPS_RANGE
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ELPH SELFEN TEMPS RANGE" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ELPH SELFEN TEMPS RANGE"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-elph-selfen-wrange-0098
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ELPH SELFEN WRANGE"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ELPH_SELFEN_WRANGE
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ELPH SELFEN WRANGE" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ELPH SELFEN WRANGE"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-elph-transport-0099
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ELPH TRANSPORT"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ELPH_TRANSPORT
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ELPH TRANSPORT" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ELPH TRANSPORT"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-elph-transport-dfermi-tol-0100
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ELPH TRANSPORT DFERMI TOL"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ELPH_TRANSPORT_DFERMI_TOL
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ELPH TRANSPORT DFERMI TOL" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ELPH TRANSPORT DFERMI TOL"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-elph-transport-driver-0101
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ELPH TRANSPORT DRIVER"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ELPH_TRANSPORT_DRIVER
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ELPH TRANSPORT DRIVER" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ELPH TRANSPORT DRIVER"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-elph-transport-emax-0102
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ELPH TRANSPORT EMAX"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ELPH_TRANSPORT_EMAX
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ELPH TRANSPORT EMAX" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ELPH TRANSPORT EMAX"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-elph-transport-emax-plot-0103
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ELPH TRANSPORT EMAX PLOT"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ELPH_TRANSPORT_EMAX_PLOT
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ELPH TRANSPORT EMAX PLOT" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ELPH TRANSPORT EMAX PLOT"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-elph-transport-emin-0104
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ELPH TRANSPORT EMIN"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ELPH_TRANSPORT_EMIN
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ELPH TRANSPORT EMIN" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ELPH TRANSPORT EMIN"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-elph-transport-emin-plot-0105
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ELPH TRANSPORT EMIN PLOT"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ELPH_TRANSPORT_EMIN_PLOT
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ELPH TRANSPORT EMIN PLOT" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ELPH TRANSPORT EMIN PLOT"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-elph-transport-nedos-plot-0106
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ELPH TRANSPORT NEDOS PLOT"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ELPH_TRANSPORT_NEDOS_PLOT
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ELPH TRANSPORT NEDOS PLOT" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ELPH TRANSPORT NEDOS PLOT"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-elph-useblas-0107
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ELPH USEBLAS"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ELPH_USEBLAS
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ELPH USEBLAS" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ELPH USEBLAS"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-elph-wf-cache-prefill-0108
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ELPH WF CACHE PREFILL"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ELPH_WF_CACHE_PREFILL
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ELPH WF CACHE PREFILL" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ELPH WF CACHE PREFILL"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-elph-wf-comm-opt-0109
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ELPH WF COMM OPT"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ELPH_WF_COMM_OPT
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ELPH WF COMM OPT" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ELPH WF COMM OPT"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-elph-wf-redistribute-0110
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ELPH WF REDISTRIBUTE"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ELPH_WF_REDISTRIBUTE
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ELPH WF REDISTRIBUTE" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ELPH WF REDISTRIBUTE"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-elph-write-hdf5vel-0111
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ELPH WRITE HDF5VEL"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ELPH_WRITE_HDF5VEL
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ELPH WRITE HDF5VEL" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ELPH WRITE HDF5VEL"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-elph-write-textvel-0112
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ELPH WRITE TEXTVEL"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ELPH_WRITE_TEXTVEL
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ELPH WRITE TEXTVEL" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ELPH WRITE TEXTVEL"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-emax-0113
record_type: parameter
scope: single_software
software:
  - VASP
topic: "EMAX"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/EMAX
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "EMAX" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "EMAX"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-emin-0114
record_type: parameter
scope: single_software
software:
  - VASP
topic: "EMIN"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/EMIN
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "EMIN" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "EMIN"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-enaug-0115
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ENAUG"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ENAUG
version_or_doc_date: VASP Wiki; checked 2026-05-24
claim: "ENAUG 控制 augmentation charge 的截断能。影响 PAW 球内电荷密度的精度。"
evidence_level: check
confidence: official
related_wiki: []
related_records: [vasp-param-encut-0116, vasp-param-addgrid-0001]
note: "通常不需手动调 (默认 ENAUG=ENCUT×1.5-2)。含难赝化元素 (O, N) 且 ADDGRID on 时一般足够。"
last_checked: 2026-05-24
parameter_name: "ENAUG"
file_or_context: INCAR
definition: "Augmentation charge 截断能 (eV)。控制 PAW 球内电荷密度的傅里叶展开精度。"
default_behavior: "max(ENCUT×1.5, ENMAX_aug)"
common_use:
  - {when: "一般计算", value: "默认 (不设)", priority: ok}
  - {when: "力不准 + 含难赝化元素", value: "ENCUT×2", priority: check}
risk_if_misused:
  - "ENAUG 过低 → PAW 球内电荷不准 → 力系统偏差"
parameter_relations:
  - {example_status: needs_verification, target: ENCUT, relation: overridden_by, desc: "默认 ENAUG≥1.5×ENCUT"}
  - {example_status: needs_verification, target: ADDGRID, relation: coupled_accuracy, desc: "ADDGRID 补 augmentation 细网格; ENAUG 补球内截断"}
related_parameters: [ENCUT, ADDGRID]
~~~

~~~yaml
record_id: vasp-param-encut-0116
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ENCUT"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ENCUT
version_or_doc_date: VASP Wiki; checked 2026-05-24
claim: "ENCUT 控制平面波基组的动能截断能。所有动能 ≤ ENCUT 的平面波纳入基组。"
evidence_level: should
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/vasp_scf_accuracy_chain.md
related_records:
  - vasp-param-prec-0530
  - vasp-param-ediff-0053
  - rel-vasp-scf-precision-chain-0001
note: "强烈建议每次计算都手动指定 ENCUT 以确保不同计算间基组一致。必须验证所研究物理量对 ENCUT 的收敛性。"
last_checked: 2026-05-24
parameter_name: "ENCUT"
file_or_context: INCAR
definition: "平面波截断能 (eV)，控制基组大小。截断能越大基组越完整，计算更准但更慢。"
default_behavior: "max(ENMAX) in POTCAR。不同 POTCAR 默认值可能不同，不推荐依赖默认值。"
common_use:
  - {when: "含 O 体系 (ENMAX_O ~300 eV)", value: "≥ 400 eV", priority: should}
  - {when: "含第一周期过渡金属", value: "≥ 400 eV", priority: should}
  - {when: "快速初筛/单点能量", value: "ENMAX × 1.0 (默认)", priority: ok}
  - {when: "准确能量差/声子/弹性常数", value: "≥ 500 eV", priority: should}
risk_if_misused:
  - "ENCUT 过低 → 基组不完整 → 能量和力系统偏低，Pulay stress 不可忽略"
  - "依赖 PREC 预设而不手动设 ENCUT → 不同 POTCAR 组合可能得到不同基组"
parameter_relations:
  - target: PREC
    example_status: needs_verification
    relation: overridden_by
    desc: "PREC≠Normal 自动覆盖手动 ENCUT 值"
  - target: EDIFF
    example_status: needs_verification
    relation: coupled_accuracy
    desc: "ENCUT 低则 EDIFF 再紧也浪费"
domain_guidance:
  - rule: "O 含体系 + AIMD/力敏感 → ENCUT ≥ 400"
    example_status: needs_verification
    applies_to: {metals: [Pt, Ni, Co, Cu, Pd, Ir], interface: [metal_water]}
    value: 400
    reason: "ENMAX_O ~300 eV × 1.3 = 390 → 取整 400"
related_parameters:
  - PREC
  - EDIFF
  - POTCAR
~~~

~~~yaml
record_id: vasp-param-encutfock-0117
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ENCUTFOCK"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ENCUTFOCK
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ENCUTFOCK" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ENCUTFOCK"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-encutgw-0118
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ENCUTGW"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ENCUTGW
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ENCUTGW" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ENCUTGW"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-encutgwsoft-0119
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ENCUTGWSOFT"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ENCUTGWSOFT
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ENCUTGWSOFT" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ENCUTGWSOFT"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-encutlr-0120
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ENCUTLR"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ENCUTLR
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ENCUTLR" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ENCUTLR"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-enini-0121
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ENINI"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ENINI
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ENINI" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ENINI"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-epsilon-0122
record_type: parameter
scope: single_software
software:
  - VASP
topic: "EPSILON"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/EPSILON
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "EPSILON" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "EPSILON"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-estop-0123
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ESTOP"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ESTOP
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ESTOP" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ESTOP"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-evenonly-0124
record_type: parameter
scope: single_software
software:
  - VASP
topic: "EVENONLY"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/EVENONLY
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "EVENONLY" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "EVENONLY"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-evenonlygw-0125
record_type: parameter
scope: single_software
software:
  - VASP
topic: "EVENONLYGW"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/EVENONLYGW
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "EVENONLYGW" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "EVENONLYGW"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ewald-cutoff-0126
record_type: parameter
scope: single_software
software:
  - VASP
topic: "EWALD CUTOFF"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/EWALD_CUTOFF
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "EWALD CUTOFF" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "EWALD CUTOFF"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-fbias-a-0127
record_type: parameter
scope: single_software
software:
  - VASP
topic: "FBIAS A"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/FBIAS_A
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "FBIAS A" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "FBIAS A"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-fbias-d-0128
record_type: parameter
scope: single_software
software:
  - VASP
topic: "FBIAS D"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/FBIAS_D
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "FBIAS D" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "FBIAS D"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-fbias-r0-0129
record_type: parameter
scope: single_software
software:
  - VASP
topic: "FBIAS R0"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/FBIAS_R0
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "FBIAS R0" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "FBIAS R0"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ferdo-0130
record_type: parameter
scope: single_software
software:
  - VASP
topic: "FERDO"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/FERDO
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "FERDO" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "FERDO"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ferwe-0131
record_type: parameter
scope: single_software
software:
  - VASP
topic: "FERWE"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/FERWE
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "FERWE" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "FERWE"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-findiff-0132
record_type: parameter
scope: single_software
software:
  - VASP
topic: "FINDIFF"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/FINDIFF
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "FINDIFF" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "FINDIFF"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-fmp-active-0133
record_type: parameter
scope: single_software
software:
  - VASP
topic: "FMP ACTIVE"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/FMP_ACTIVE
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "FMP ACTIVE" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "FMP ACTIVE"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-fmp-direction-0134
record_type: parameter
scope: single_software
software:
  - VASP
topic: "FMP DIRECTION"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/FMP_DIRECTION
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "FMP DIRECTION" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "FMP DIRECTION"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-fmp-period-0135
record_type: parameter
scope: single_software
software:
  - VASP
topic: "FMP PERIOD"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/FMP_PERIOD
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "FMP PERIOD" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "FMP PERIOD"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-fmp-snumber-0136
record_type: parameter
scope: single_software
software:
  - VASP
topic: "FMP SNUMBER"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/FMP_SNUMBER
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "FMP SNUMBER" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "FMP SNUMBER"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-fmp-swapnum-0137
record_type: parameter
scope: single_software
software:
  - VASP
topic: "FMP SWAPNUM"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/FMP_SWAPNUM
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "FMP SWAPNUM" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "FMP SWAPNUM"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-fockcorr-0138
record_type: parameter
scope: single_software
software:
  - VASP
topic: "FOCKCORR"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/FOCKCORR
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "FOCKCORR" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "FOCKCORR"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-gamma-vdw-0139
record_type: parameter
scope: single_software
software:
  - VASP
topic: "GAMMA VDW"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/GAMMA_VDW
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "GAMMA VDW" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "GAMMA VDW"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-gga-0140
record_type: parameter
scope: single_software
software:
  - VASP
topic: "GGA"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/GGA
version_or_doc_date: VASP Wiki; checked 2026-05-24
claim: "GGA 选择交换关联泛函类型。PE=默认 PBE; RP=RPBE; PS=PBEsol; 91=Perdew-Wang。"
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: "催化领域标准是 PBE (GGA=PE)。RPBE 改善吸附能但常需 D3 补充。PBEsol 对固体的晶格常数更准。"
last_checked: 2026-05-24
parameter_name: "GGA"
file_or_context: INCAR
definition: "GGA 交换关联泛函: PE=PBE; RP=RPBE; PS=PBEsol; RE=revPBE; AM=AM05。"
default_behavior: "PE (PBE)"
common_use:
  - {when: "催化计算标准", value: PE, priority: should}
  - {when: "吸附能/表面能修正", value: RP, priority: ok}
risk_if_misused:
  - "混用不同 GGA 的结果对比 (如 PBE vs RPBE) → 吸附能系统性差异可达 0.2 eV"
related_parameters: [IVDW]
domain_guidance:
  - {example_status: needs_verification, rule: "催化界面 → GGA=PE (PBE)", value: PE}
~~~

~~~yaml
record_id: vasp-param-gga-compat-0141
record_type: parameter
scope: single_software
software:
  - VASP
topic: "GGA COMPAT"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/GGA_COMPAT
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "GGA COMPAT" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "GGA COMPAT"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-hfalpha-0142
record_type: parameter
scope: single_software
software:
  - VASP
topic: "HFALPHA"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/HFALPHA
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "HFALPHA" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "HFALPHA"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-hflmax-0143
record_type: parameter
scope: single_software
software:
  - VASP
topic: "HFLMAX"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/HFLMAX
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "HFLMAX" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "HFLMAX"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-hfrcut-0144
record_type: parameter
scope: single_software
software:
  - VASP
topic: "HFRCUT"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/HFRCUT
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "HFRCUT" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "HFRCUT"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-hfscreen-0145
record_type: parameter
scope: single_software
software:
  - VASP
topic: "HFSCREEN"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/HFSCREEN
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "HFSCREEN" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "HFSCREEN"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-hills-bin-0146
record_type: parameter
scope: single_software
software:
  - VASP
topic: "HILLS BIN"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/HILLS_BIN
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "HILLS BIN" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "HILLS BIN"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-hills-h-0147
record_type: parameter
scope: single_software
software:
  - VASP
topic: "HILLS H"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/HILLS_H
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "HILLS H" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "HILLS H"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-hills-w-0148
record_type: parameter
scope: single_software
software:
  - VASP
topic: "HILLS W"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/HILLS_W
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "HILLS W" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "HILLS W"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-hitoler-0149
record_type: parameter
scope: single_software
software:
  - VASP
topic: "HITOLER"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/HITOLER
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "HITOLER" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "HITOLER"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-i-constrained-m-0150
record_type: parameter
scope: single_software
software:
  - VASP
topic: "I CONSTRAINED M"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/I_CONSTRAINED_M
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "I CONSTRAINED M" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "I CONSTRAINED M"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ialgo-0151
record_type: parameter
scope: single_software
software:
  - VASP
topic: "IALGO"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/IALGO
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "IALGO" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "IALGO"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-iall-in-one-0152
record_type: parameter
scope: single_software
software:
  - VASP
topic: "IALL IN ONE"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/IALL_IN_ONE
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "IALL IN ONE" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "IALL IN ONE"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-iband-0153
record_type: parameter
scope: single_software
software:
  - VASP
topic: "IBAND"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/IBAND
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "IBAND" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "IBAND"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ibrion-0154
record_type: parameter
scope: single_software
software:
  - VASP
topic: "IBRION"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/IBRION
version_or_doc_date: VASP Wiki; checked 2026-05-24
claim: "IBRION 选择离子更新算法。0=MD; 1=准牛顿(RMM-DIIS); 2=共轭梯度; 3=阻尼MD(NEB); 5/6=振动频率。"
evidence_level: should
confidence: official
related_wiki: []
related_records: [vasp-param-potim-0529, vasp-param-nsw-0485, vasp-param-ediffg-0054, vasp-md-param-ibrion-0001]
note: "几何优化常用 IBRION=2 (CG,robust); NEB 用 IBRION=1 (VASP 内置) 或 IBRION=3 (VTST); 频率用 IBRION=5/6。"
last_checked: 2026-05-24
parameter_name: "IBRION"
file_or_context: INCAR
definition: "离子更新算法: 0=MD; 1=RMM-DIIS; 2=CG; 3=damped MD; 5=HF difference; 6=sym HF difference; 7/8=DFPT。"
default_behavior: "IBRION=-1 (不移动离子)"
common_use:
  - {when: "几何优化 (slab)", value: 2, priority: should}
  - {when: "NEB (VASP 内置)", value: 1, priority: must}
  - {when: "AIMD", value: 0, priority: must}
  - {when: "振动频率 (有限差分)", value: 5, priority: should}
risk_if_misused:
  - "IBRION=0 (MD) 设了非零 POTIM → 运行 MD 非几何优化"
parameter_relations:
  - {example_status: needs_verification, target: POTIM, relation: mutually_constrained}
  - {example_status: needs_verification, target: EDIFFG, relation: coupled_accuracy, desc: "几何优化需力收敛"}
domain_guidance:
  - {example_status: needs_verification, rule: "NEB→IBRION=1/3; 几何优化→2; 频率→5/6", applies_to: {tasks: [geometry_opt, neb, vibrational_freq]}}
related_parameters: [POTIM, NSW, EDIFFG]
~~~

~~~yaml
record_id: vasp-param-ibse-0155
record_type: parameter
scope: single_software
software:
  - VASP
topic: "IBSE"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/IBSE
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "IBSE" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "IBSE"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-icharg-0156
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ICHARG"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ICHARG
version_or_doc_date: VASP Wiki; checked 2026-05-24
claim: "ICHARG 控制初始电荷密度和波函数的获取方式。ICHARG=11 常用于 DOS 计算 (读 CHGCAR)。"
evidence_level: check
confidence: official
related_wiki: []
related_records: [vasp-param-lcharg-0219, vasp-param-lwave-0342]
note: "AIMD 从 CHGCAR/WAVECAR 续跑时需设 ICHARG=1 (读 CHGCAR)。"
last_checked: 2026-05-24
parameter_name: "ICHARG"
file_or_context: INCAR
definition: "初始电荷密度获取方式: 0=初猜; 1=读 CHGCAR; 2=原子叠加; 11=读 CHGCAR 固定电荷 (DOS 用)。"
default_behavior: "ICHARG=2 (IF ICHARG not set and no WAVECAR) or 0 (from WAVECAR)"
common_use:
  - {when: "从 scratch 开始", value: 2, priority: ok}
  - {when: "续跑 MD (重启)", value: 1, priority: should}
risk_if_misused:
  - "ICHARG=11 用于结构优化/MD → 力不正确 (电荷固定)"
domain_guidance:
  - example_status: needs_verification
    rule: "DOS/Bader 分析 → SCF (ICHARG=2) → 存 CHGCAR → non-SCF (ICHARG=11)"
    applies_to: {tasks: [dos, pdos, bader_charge, electronic_structure]}
    value: "2 (SCF) → 11 (non-SCF DOS)"
    reason: "ICHARG=11 读 CHGCAR 固定电荷密度，非自洽快速出 DOS/Bader"
parameter_relations:
  - example_status: needs_verification
    target: LORBIT
    relation: prerequisite
    desc: "ICHARG=11 (non-SCF) 是 PDOS 计算的正确模式; SCF 模式下 LORBIT 也可以但效率低"
~~~

~~~yaml
record_id: vasp-param-ichibare-0157
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ICHIBARE"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ICHIBARE
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ICHIBARE" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ICHIBARE"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-icorelevel-0158
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ICORELEVEL"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ICORELEVEL
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ICORELEVEL" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ICORELEVEL"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-idipol-0159
record_type: parameter
scope: single_software
software:
  - VASP
topic: "IDIPOL"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/IDIPOL
version_or_doc_date: VASP Wiki; checked 2026-05-24
claim: "IDIPOL 控制偶极校正方向。Slab 计算必需 (通常 IDIPOL=3 沿 z 方向)。"
evidence_level: should
confidence: official
related_wiki: []
related_records: [vasp-param-ldipol-0230]
note: "非对称 slab (吸附仅在一侧) 必须开偶极校正。IDIPOL=3 沿 z；配合 LDIPOL=.TRUE.。"
last_checked: 2026-05-24
parameter_name: "IDIPOL"
file_or_context: INCAR
definition: "偶极校正方向: 1=x; 2=y; 3=z; 4=all。"
default_behavior: "0 (无偶极校正)"
common_use:
  - {when: "Slab 计算 (非对称)", value: 3, priority: should}
  - {when: "Bulk 计算", value: 0, priority: ok}
risk_if_misused:
  - "非对称 slab 不开偶极校正 → 虚假偶极-偶极相互作用 → 功函数/吸附能不准"
domain_guidance:
  - example_status: needs_verification
    rule: "单侧吸附质/slab → IDIPOL=3 + LDIPOL=.TRUE."
    applies_to: {systems: [metal_slab_asymmetric], tasks: [adsorption_energy, work_function]}
    value: 3
    reason: "全方向 (3) 偶极校正消除 slab 法向虚假电场"
parameter_relations:
  - example_status: needs_verification
    target: LDIPOL
    relation: requires_companion
    desc: "IDIPOL 选定校正方向后需 LDIPOL 指定偶极中心"
~~~

~~~yaml
record_id: vasp-param-iepsilon-0160
record_type: parameter
scope: single_software
software:
  - VASP
topic: "IEPSILON"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/IEPSILON
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "IEPSILON" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "IEPSILON"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ifc-asr-0161
record_type: parameter
scope: single_software
software:
  - VASP
topic: "IFC ASR"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/IFC_ASR
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "IFC ASR" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "IFC ASR"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ifc-lr-0162
record_type: parameter
scope: single_software
software:
  - VASP
topic: "IFC LR"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/IFC_LR
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "IFC LR" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "IFC LR"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-igpar-0163
record_type: parameter
scope: single_software
software:
  - VASP
topic: "IGPAR"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/IGPAR
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "IGPAR" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "IGPAR"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-image-n-0164
record_type: parameter
scope: single_software
software:
  - VASP
topic: "IMAGE N"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/IMAGE_N
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "IMAGE N" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "IMAGE N"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-images-0165
record_type: parameter
scope: single_software
software:
  - VASP
topic: "IMAGES"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/IMAGES
version_or_doc_date: VASP Wiki; checked 2026-05-24
claim: "IMAGES 设定 NEB 计算中初始和最终结构之间的中间插点数量。"
evidence_level: should
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/vasp_neb_chain.md
related_records:
  - vasp-param-spring-0558
  - vasp-param-ediffg-0054
  - rel-vasp-neb-chain-0002
note: "插点越多路径分辨率越高但计算量线性增加。5-7 是简单反应的常用起手值。"
last_checked: 2026-05-24
parameter_name: "IMAGES"
file_or_context: INCAR
definition: "NEB 中间插点数量 (不含 IS 和 FS)。每张插点一个独立的 VASP 计算。"
default_behavior: "0 (不执行 NEB)"
common_use:
  - {when: "简单键断裂/形成 (如 *H → TS)", value: "3-5", priority: should}
  - {when: "复杂反应 (如 C-N 偶联)", value: "7-9", priority: should}
  - {when: "粗略 scan", value: "3", priority: ok}
risk_if_misused:
  - "过少 → 路径分辨率不够 → 可能漏掉真正的 TS"
  - "过多 → 计算量线性增加; 且与 SPRING 的配合需调整"
parameter_relations:
  - target: SPRING
    example_status: needs_verification
    relation: mutually_constrained
    desc: "插点多需更强弹簧约束"
  - target: EDIFFG
    example_status: needs_verification
    relation: coupled_accuracy
    desc: "路径分辨率 (IMAGES) 与力精度 (EDIFFG) 共同决定 TS 准确性"
domain_guidance:
  - rule: "催化表面反应 → IMAGES=5 起手"
    example_status: needs_verification
    applies_to: {systems: [metal_slab_adsorbate]}
    value: 5
    reason: "5 点足够分辨典型反应路径的曲率"
related_parameters:
  - SPRING
  - EDIFFG
~~~

~~~yaml
record_id: vasp-param-imix-0166
record_type: parameter
scope: single_software
software:
  - VASP
topic: "IMIX"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/IMIX
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "IMIX" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "IMIX"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-increm-0167
record_type: parameter
scope: single_software
software:
  - VASP
topic: "INCREM"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/INCREM
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "INCREM" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "INCREM"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-inimix-0168
record_type: parameter
scope: single_software
software:
  - VASP
topic: "INIMIX"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/INIMIX
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "INIMIX" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "INIMIX"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-iniwav-0169
record_type: parameter
scope: single_software
software:
  - VASP
topic: "INIWAV"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/INIWAV
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "INIWAV" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "INIWAV"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-inmrprint-0170
record_type: parameter
scope: single_software
software:
  - VASP
topic: "INMRPRINT"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/INMRPRINT
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "INMRPRINT" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "INMRPRINT"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-interactive-0171
record_type: parameter
scope: single_software
software:
  - VASP
topic: "INTERACTIVE"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/INTERACTIVE
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "INTERACTIVE" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "INTERACTIVE"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ipead-0172
record_type: parameter
scope: single_software
software:
  - VASP
topic: "IPEAD"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/IPEAD
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "IPEAD" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "IPEAD"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-irc-delta0-0173
record_type: parameter
scope: single_software
software:
  - VASP
topic: "IRC DELTA0"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/IRC_DELTA0
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "IRC DELTA0" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "IRC DELTA0"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-irc-direction-0174
record_type: parameter
scope: single_software
software:
  - VASP
topic: "IRC DIRECTION"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/IRC_DIRECTION
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "IRC DIRECTION" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "IRC DIRECTION"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-irc-maxstep-0175
record_type: parameter
scope: single_software
software:
  - VASP
topic: "IRC MAXSTEP"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/IRC_MAXSTEP
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "IRC MAXSTEP" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "IRC MAXSTEP"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-irc-minstep-0176
record_type: parameter
scope: single_software
software:
  - VASP
topic: "IRC MINSTEP"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/IRC_MINSTEP
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "IRC MINSTEP" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "IRC MINSTEP"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-irc-stop-0177
record_type: parameter
scope: single_software
software:
  - VASP
topic: "IRC STOP"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/IRC_STOP
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "IRC STOP" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "IRC STOP"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-irc-vnorm0-0178
record_type: parameter
scope: single_software
software:
  - VASP
topic: "IRC VNORM0"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/IRC_VNORM0
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "IRC VNORM0" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "IRC VNORM0"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-isearch-0179
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ISEARCH"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ISEARCH
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ISEARCH" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ISEARCH"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-isif-0180
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ISIF"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ISIF
version_or_doc_date: VASP Wiki; checked 2026-05-24
claim: "ISIF 控制 cell 形状/体积/离子位置是否松弛。Slab 优化: ISIF=2 (仅离子); bulk: ISIF=3。"
evidence_level: should
confidence: official
related_wiki: []
related_records: [vasp-param-ibrion-0154, vasp-md-param-isif-0017, rel-vasp-md-thermostat-chain-0004]
note: "Slab 计算通常 ISIF=2 (固定 cell 仅松弛离子)。AIMD 中 ISIF 与 MDALGO 有互斥约束。"
last_checked: 2026-05-24
parameter_name: "ISIF"
file_or_context: INCAR
definition: "松弛自由度: 0-7。控制 cell shape/volume 和离子位置的松弛耦合。"
default_behavior: "ISIF=0 (POTIM=0) or ISIF=2 (IBRION>=1)"
common_use:
  - {when: "Slab 几何优化 (固定 cell)", value: 2, priority: should}
  - {when: "Bulk 优化 (全松弛)", value: 3, priority: should}
  - {when: "单点能/SCF", value: 0, priority: ok}
  - {when: "NEB (固定 cell)", value: 2, priority: should}
risk_if_misused:
  - "Slab 用 ISIF=3 → cell z 方向过度收缩 → 真空层塌缩"
  - "AIMD 中 ISIF=3+MDALGO=3 且缺 companion tags → cell 自由度不完整"
parameter_relations:
  - {example_status: needs_verification, target: MDALGO, relation: mutually_exclusive, desc: "MDALGO=3+ISIF=3→NpT需额外参数"}
domain_guidance:
  - {example_status: needs_verification, rule: "Slab→ISIF=2; Bulk→ISIF=3; MD NVT→ISIF≤2"}
related_parameters: [IBRION]
~~~

~~~yaml
record_id: vasp-param-ismear-0181
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ISMEAR"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ISMEAR
version_or_doc_date: VASP Wiki; checked 2026-05-24
claim: "ISMEAR 选择布里渊区积分中的展宽方法，决定 Fermi 面附近的电子占据方式。"
evidence_level: must
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/vasp_scf_accuracy_chain.md
related_records:
  - vasp-param-sigma-0554
note: "ISMEAR 选择直接影响总能量准确性。金属: ISMEAR=1/2 (MP) 或 0 (Gaussian) + 小 SIGMA；绝缘体/半导体: ISMEAR=0 (Gaussian) + 小 SIGMA、-5 (tetrahedron) 或 -3 (固定占据)。"
last_checked: 2026-05-24
parameter_name: "ISMEAR"
file_or_context: INCAR
definition: "展宽方法: -5=tetrahedron+Blöchl 校正; -4=tetrahedron (仅 DOS); -3=无展宽 (固定占据); -1=Fermi smearing; 0=Gaussian smearing; 1=MP 一阶; 2=MP 二阶; >2=MP N 阶。"
default_behavior: "ISMEAR=1 (VASP 默认 MP first-order)"
common_use:
  - {when: "金属 slab (Pt/Ni/Cu...)", value: 0, priority: should}
  - {when: "绝缘体/半导体 + 准确能量", value: -5 or 0, priority: should}
  - {when: "AIMD of metals", value: 0, priority: should}
  - {when: "绝缘体 + 小 k 点 (< 4 点)", value: 0, priority: ok}
risk_if_misused:
  - "ISMEAR=2 用于金属 → 总能量有系统性误差 (entropy term)"
  - "ISMEAR=-1 用于金属 + 少 k 点 → 可能不收敛 (需密集 k 点)"
  - "ISMEAR=1 默认可能不适合所有体系 → 必须按体系类型选择"
parameter_relations:
  - target: SIGMA
    example_status: needs_verification
    relation: requires_companion
    desc: "ISMEAR≥0 需要配合 SIGMA 设定展宽宽度"
domain_guidance:
  - rule: "Pt slab + AIMD → ISMEAR=0, SIGMA=0.1"
    example_status: needs_verification
    applies_to: {metals: [Pt, Ni, Co, Cu], tasks: [aimd, geometry_opt]}
    value: 0
    reason: "Gaussian smearing (ISMEAR=0) 适合金属; SIGMA=0.1 足够小不引入显著 entropy error"
related_parameters:
  - SIGMA
~~~

~~~yaml
record_id: vasp-param-ispin-0182
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ISPIN"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ISPIN
version_or_doc_date: VASP Wiki; checked 2026-05-24
claim: "ISPIN 控制自旋极化。ISPIN=2 启用 collinear 自旋 (磁性体系必须)。"
evidence_level: must
confidence: official
related_wiki: []
related_records:
  - vasp-param-magmom-0353
note: "含 Ni/Co/Fe/Mn 等磁性元素时 ISPIN=2 是必须的。Pt 金属一般 ISPIN=1 (无磁性) 即可。"
last_checked: 2026-05-24
parameter_name: "ISPIN"
file_or_context: INCAR
definition: "自旋极化开关: 1=非自旋; 2=collinear 自旋。"
default_behavior: "ISPIN=1"
common_use:
  - {when: "非磁性 (Pt/Pd/Cu/纯水)", value: 1, priority: should}
  - {when: "磁性元素 (Ni/Co/Fe/Mn)", value: 2, priority: must}
risk_if_misused:
  - "磁性体系用 ISPIN=1 → 磁矩被抑制 → 能量/结构偏差大"
  - "非磁性体系用 ISPIN=2 → 增加计算量无精度收益"
parameter_relations:
  - {example_status: needs_verification, target: MAGMOM, relation: requires_companion, desc: "ISPIN=2 需配合 MAGMOM 指定初始磁矩"}
domain_guidance:
  - {example_status: needs_verification, rule: "Pt → ISPIN=1; Ni/Co/Fe → ISPIN=2", applies_to: {metals: [Pt, Pd, Cu, Ni, Co, Fe]}}
related_parameters: [MAGMOM]
~~~

~~~yaml
record_id: vasp-param-istart-0183
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ISTART"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ISTART
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ISTART" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ISTART"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-isym-0184
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ISYM"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ISYM
version_or_doc_date: VASP Wiki; checked 2026-05-24
claim: "ISYM 控制对称性分析。ISYM=2 启用对称性; ISYM=0 关闭 (AIMD 需关)。"
evidence_level: should
confidence: official
related_wiki: []
related_records: []
note: "AIMD 必须 ISYM=0 (每步结构无对称性)。几何优化可 ISYM=2 加速。"
last_checked: 2026-05-24
parameter_name: "ISYM"
file_or_context: INCAR
definition: "对称性开关: -1/0=关; 1/2=开; 3=开+强制对称化力。"
default_behavior: "ISYM=2"
common_use:
  - {when: "几何优化 (slab)", value: 2, priority: should}
  - {when: "AIMD", value: 0, priority: must}
  - {when: "NEB/过渡态", value: 0, priority: must}
risk_if_misused:
  - "AIMD 中 ISYM≠0 → 每步强加对称性 → 动力学不物理"
domain_guidance:
  - {example_status: needs_verification, rule: "AIMD/NEB → ISYM=0", value: 0}
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ivdw-0185
record_type: parameter
scope: single_software
software:
  - VASP
topic: "IVDW"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/IVDW
version_or_doc_date: VASP Wiki; checked 2026-05-24
claim: "IVDW 控制范德华色散校正方法。催化界面建议 D3 (IVDW=11) 或 dDsC (IVDW=4)。"
evidence_level: should
confidence: official
related_wiki: []
related_records: [vasp-param-gga-0140]
note: "IVDW=11 (Grimme D3) + Becke-Johnson damping 是催化领域标准。水-金属界面范德华力对吸附能影响 ~0.1-0.3 eV。"
last_checked: 2026-05-24
parameter_name: "IVDW"
file_or_context: INCAR
definition: "范德华校正: 0=off; 1=DFT-D2; 10=DFT-D3; 11=D3(BJ); 12=D3(BJM); 4=dDsC; 2=TS。"
default_behavior: "0 (no vdW)"
common_use:
  - {when: "催化界面 (金属+水/吸附质)", value: 11, priority: should}
  - {when: "仅金属 slab (无吸附)", value: 0, priority: ok}
risk_if_misused:
  - "有吸附质但不开 IVDW → 吸附能偏弱 → 自由能图不准"
domain_guidance:
  - {example_status: needs_verification, rule: "界面水/吸附质体系 → IVDW=11 (D3BJ)", value: 11}
~~~

~~~yaml
record_id: vasp-param-ivdw-nl-0186
record_type: parameter
scope: single_software
software:
  - VASP
topic: "IVDW NL"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/IVDW_NL
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "IVDW NL" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "IVDW NL"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-iwavpr-0187
record_type: parameter
scope: single_software
software:
  - VASP
topic: "IWAVPR"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/IWAVPR
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "IWAVPR" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "IWAVPR"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-k-multiply-0188
record_type: parameter
scope: single_software
software:
  - VASP
topic: "K MULTIPLY"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/K_MULTIPLY
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "K MULTIPLY" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "K MULTIPLY"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-kblock-0189
record_type: parameter
scope: single_software
software:
  - VASP
topic: "KBLOCK"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/KBLOCK
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "KBLOCK" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "KBLOCK"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-kernel-truncation-factor-0190
record_type: parameter
scope: single_software
software:
  - VASP
topic: "KERNEL TRUNCATION/FACTOR"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/KERNEL_TRUNCATION%2FFACTOR
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "KERNEL TRUNCATION/FACTOR" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "KERNEL TRUNCATION/FACTOR"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-kernel-truncation-idimensionality-0191
record_type: parameter
scope: single_software
software:
  - VASP
topic: "KERNEL TRUNCATION/IDIMENSIONALITY"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/KERNEL_TRUNCATION%2FIDIMENSIONALITY
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "KERNEL TRUNCATION/IDIMENSIONALITY" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "KERNEL TRUNCATION/IDIMENSIONALITY"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-kernel-truncation-ipad-0192
record_type: parameter
scope: single_software
software:
  - VASP
topic: "KERNEL TRUNCATION/IPAD"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/KERNEL_TRUNCATION%2FIPAD
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "KERNEL TRUNCATION/IPAD" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "KERNEL TRUNCATION/IPAD"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-kernel-truncation-isurface-0193
record_type: parameter
scope: single_software
software:
  - VASP
topic: "KERNEL TRUNCATION/ISURFACE"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/KERNEL_TRUNCATION%2FISURFACE
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "KERNEL TRUNCATION/ISURFACE" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "KERNEL TRUNCATION/ISURFACE"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-kernel-truncation-lcoarsen-0194
record_type: parameter
scope: single_software
software:
  - VASP
topic: "KERNEL TRUNCATION/LCOARSEN"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/KERNEL_TRUNCATION%2FLCOARSEN
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "KERNEL TRUNCATION/LCOARSEN" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "KERNEL TRUNCATION/LCOARSEN"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-kernel-truncation-ltruncate-0195
record_type: parameter
scope: single_software
software:
  - VASP
topic: "KERNEL TRUNCATION/LTRUNCATE"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/KERNEL_TRUNCATION%2FLTRUNCATE
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "KERNEL TRUNCATION/LTRUNCATE" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "KERNEL TRUNCATION/LTRUNCATE"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-kgamma-0196
record_type: parameter
scope: single_software
software:
  - VASP
topic: "KGAMMA"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/KGAMMA
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "KGAMMA" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "KGAMMA"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-kpar-0197
record_type: parameter
scope: single_software
software:
  - VASP
topic: "KPAR"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/KPAR
version_or_doc_date: VASP Wiki; checked 2026-05-24
claim: "KPAR 控制 k 点并行化。将 k 点分配给多个 MPI rank 组并行计算。"
evidence_level: check
confidence: official
related_wiki: []
related_records:
  - vasp-param-ncore-0446
note: "KPAR 应整除总 k 点数。KPAR × NCORE ≤ 总核数。对 slab 计算 (k 点少) KPAR 效果有限。"
last_checked: 2026-05-24
parameter_name: "KPAR"
file_or_context: INCAR
definition: "k 点并行数。将 k 点分成 KPAR 组，每组独立对角化。"
default_behavior: "KPAR=1"
common_use:
  - {when: "多 k 点 bulk 计算", value: "=k 点数", priority: should}
  - {when: "Γ-only slab 计算", value: 1, priority: ok}
risk_if_misused:
  - "KPAR > 总 k 点数 → 浪费资源"
parameter_relations:
  - {example_status: needs_verification, target: NCORE, relation: mutually_constrained, desc: "KPAR × NCORE ≤ 总核数"}
domain_guidance:
  - {example_status: needs_verification, rule: "Slab Γ-point → KPAR=1 (无 k 点并行收益)"}
related_parameters: [NCORE]
~~~

~~~yaml
record_id: vasp-param-kpoint-bse-0198
record_type: parameter
scope: single_software
software:
  - VASP
topic: "KPOINT BSE"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/KPOINT_BSE
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "KPOINT BSE" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "KPOINT BSE"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-kpoints-opt-mode-0199
record_type: parameter
scope: single_software
software:
  - VASP
topic: "KPOINTS OPT MODE"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/KPOINTS_OPT_MODE
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "KPOINTS OPT MODE" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "KPOINTS OPT MODE"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-kpoints-opt-nkbatch-0200
record_type: parameter
scope: single_software
software:
  - VASP
topic: "KPOINTS OPT NKBATCH"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/KPOINTS_OPT_NKBATCH
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "KPOINTS OPT NKBATCH" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "KPOINTS OPT NKBATCH"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-kpuse-0201
record_type: parameter
scope: single_software
software:
  - VASP
topic: "KPUSE"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/KPUSE
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "KPUSE" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "KPUSE"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-kspacing-0202
record_type: parameter
scope: single_software
software:
  - VASP
topic: "KSPACING"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/KSPACING
version_or_doc_date: VASP Wiki; checked 2026-05-24
claim: "KSPACING 以倒空间间距 (Å⁻¹) 自动生成 k 点网格，替代手动 KPOINTS 文件。"
evidence_level: should
confidence: official
related_wiki: []
related_records:
  - vasp-param-isif-0180
note: "KSPACING=0.3 对应 ~14 Å 实空间间距，适合大多数 slab 计算。更密 k 点需更小 KSPACING。"
last_checked: 2026-05-24
parameter_name: "KSPACING"
file_or_context: INCAR
definition: "倒空间 k 点间距 (Å⁻¹)。值越小网格越密。"
default_behavior: "0.5 (VASP 默认; 较稀疏)"
common_use:
  - {when: "Slab 几何优化", value: 0.3, priority: should}
  - {when: "精确能量/声子", value: 0.15-0.20, priority: should}
  - {when: "AIMD (对 k 点要求较低)", value: 0.4-0.5, priority: ok}
risk_if_misused:
  - "KSPACING 太大 → k 点不够 → 总能量/力不收敛"
parameter_relations:
  - {example_status: needs_verification, target: ISMEAR, relation: mutually_constrained, desc: "KSPACING 小 (多 k 点) → ISMEAR=0/1 也准; KSPACING 大 → 需更注意 ISMEAR 选择"}
domain_guidance:
  - {example_status: needs_verification, rule: "Pt(111) 3×3 → KSPACING=0.3", value: 0.3, reason: "平衡精度和计算量"}
related_parameters: [ISMEAR, SIGMA]
~~~

~~~yaml
record_id: vasp-param-kspacing-opt-0203
record_type: parameter
scope: single_software
software:
  - VASP
topic: "KSPACING OPT"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/KSPACING_OPT
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "KSPACING OPT" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "KSPACING OPT"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ladder-0204
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LADDER"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LADDER
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LADDER" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LADDER"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-laechg-0205
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LAECHG"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LAECHG
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LAECHG" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LAECHG"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lall-in-one-0206
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LALL IN ONE"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LALL_IN_ONE
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LALL IN ONE" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LALL IN ONE"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lambda-0207
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LAMBDA"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LAMBDA
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LAMBDA" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LAMBDA"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lanczosthr-0208
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LANCZOSTHR"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LANCZOSTHR
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LANCZOSTHR" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LANCZOSTHR"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-langevin-gamma-0209
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LANGEVIN GAMMA"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LANGEVIN_GAMMA
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LANGEVIN GAMMA" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LANGEVIN GAMMA"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-langevin-gamma-l-0210
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LANGEVIN GAMMA L"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LANGEVIN_GAMMA_L
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LANGEVIN GAMMA L" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LANGEVIN GAMMA L"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lasph-0211
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LASPH"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LASPH
version_or_doc_date: VASP Wiki; checked 2026-05-24
claim: "LASPH 控制是否在 PAW 球内包含非球对称的电荷密度和势的贡献，对力准确性重要。"
evidence_level: should
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/vasp_scf_accuracy_chain.md
related_records:
  - vasp-param-addgrid-0001
  - rel-vasp-scf-precision-chain-0001
note: "LASPH 与 ADDGRID 互补: ADDGRID 补径向精度，LASPH 补角向精度。力敏感计算建议双双开启。"
last_checked: 2026-05-24
parameter_name: "LASPH"
file_or_context: INCAR
definition: "非球对称 PAW 贡献开关。.TRUE. 时在 PAW 球内包括 l-dependent 的非球对称项，对方的方向性精度重要。"
default_behavior: "LASPH=.FALSE. (VASP 默认)"
common_use:
  - {when: "力敏感计算 (AIMD/NEB/声子)", value: ".TRUE.", priority: should}
  - {when: "仅需能量 (SCF 初筛)", value: ".FALSE.", priority: ok}
  - {when: "sp 元素纯体系", value: ".FALSE.", priority: ok}
risk_if_misused:
  - "LASPH=.FALSE. + AIMD/NEB → 力有方向性系统偏差 → 轨迹/路径不准"
  - "计算开销 ~5-10%，对能量影响很小"
parameter_relations:
  - target: ADDGRID
    example_status: needs_verification
    relation: coupled_accuracy
    desc: "ADDGRID 径向 + LASPH 角向 = 完整 PAW 力精度"
domain_guidance:
  - rule: "d-electron metal + 力敏感 → LASPH=.TRUE."
    example_status: needs_verification
    applies_to: {metals: [Pt, Ni, Co, Fe, Cu, Pd], tasks: [aimd, neb, phonon]}
    value: ".TRUE."
    reason: "d 电子有显著的非球对称性; AIMD/NEB 力方向精度关键"
related_parameters:
  - ADDGRID
~~~

~~~yaml
record_id: vasp-param-lasync-0212
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LASYNC"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LASYNC
version_or_doc_date: VASP Wiki; checked 2026-05-24
claim: "LASYNC 控制异步 IO。LASYNC=.TRUE. 在 AIMD 可显著减少 IO 等待。"
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: "AIMD 推荐 LASYNC=.TRUE. 以减少每步 OUTCAR/OSZICAR 写等 IO bottleneck。"
last_checked: 2026-05-24
parameter_name: "LASYNC"
file_or_context: INCAR
definition: "异步 IO 开关。.TRUE. 时 VASP 不等待磁盘写入即继续计算。"
default_behavior: "LASYNC=.FALSE."
common_use:
  - {when: "AIMD", value: ".TRUE.", priority: should}
  - {when: "SCF/几何优化", value: ".FALSE.", priority: ok}
risk_if_misused:
  - "LASYNC=.TRUE. + 异常退出 → 最后几步输出可能丢失"
~~~

~~~yaml
record_id: vasp-param-lattice-constraints-0213
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LATTICE CONSTRAINTS"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LATTICE_CONSTRAINTS
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LATTICE CONSTRAINTS" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LATTICE CONSTRAINTS"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lberry-0214
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LBERRY"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LBERRY
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LBERRY" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LBERRY"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lblueout-0215
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LBLUEOUT"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LBLUEOUT
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LBLUEOUT" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LBLUEOUT"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lbone-0216
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LBONE"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LBONE
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LBONE" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LBONE"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lcalceps-0217
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LCALCEPS"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LCALCEPS
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LCALCEPS" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LCALCEPS"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lcalcpol-0218
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LCALCPOL"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LCALCPOL
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LCALCPOL" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LCALCPOL"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lcharg-0219
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LCHARG"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LCHARG
version_or_doc_date: VASP Wiki; checked 2026-05-24
claim: "LCHARG 控制是否写出 CHGCAR 文件。AIMD 可关以省 IO。"
evidence_level: check
confidence: official
related_wiki: []
related_records: [vasp-param-lwave-0342]
note: "AIMD 每步写 CHGCAR 会大量增加 IO 开销。推荐 AIMD 设 LCHARG=.FALSE.。"
last_checked: 2026-05-24
parameter_name: "LCHARG"
file_or_context: INCAR
definition: "是否写 CHGCAR (电荷密度文件)。"
default_behavior: "LCHARG=.TRUE."
common_use:
  - {when: "SCF/几何优化", value: ".TRUE.", priority: ok}
  - {when: "AIMD", value: ".FALSE.", priority: should}
risk_if_misused:
  - "AIMD 开 LCHARG → 每步写大文件 → IO bottleneck"
~~~

~~~yaml
record_id: vasp-param-lchargh5-0220
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LCHARGH5"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LCHARGH5
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LCHARGH5" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LCHARGH5"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lchimag-0221
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LCHIMAG"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LCHIMAG
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LCHIMAG" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LCHIMAG"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lcorr-0222
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LCORR"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LCORR
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LCORR" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LCORR"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

# ── VTST extension tag (not in VASP Wiki Category:INCAR_tag) ──

~~~yaml
record_id: vasp-param-lclimb-0500
record_type: parameter
scope: single_software
software:
  - VASP
topic: LCLIMB
source_type: official_doc
source_ref: "https://theory.cm.utexas.edu/vtsttools/neb.html"
version_or_doc_date: "VTST; checked 2026-05-24"
claim: "CI-NEB 开关——激活后最高能量点向鞍点精确爬升。VTST 扩展标签，非标准 VASP INCAR 标签。"
evidence_level: should
confidence: local_unverified
related_wiki:
  - computer_kb/wiki/concepts/vasp_neb_chain.md
related_records:
  - vasp-param-images-0165
  - vasp-param-ediffg-0054
note: "LCLIMB 不在 VASP Wiki Category:INCAR_tag 标准索引中。属 VTST (VASP Transition State Theory) 工具包扩展。需在编译时链接 VTST。"
last_checked: 2026-05-24
parameter_name: "LCLIMB"
file_or_context: INCAR (VTST)
definition: "Climbing Image NEB 开关。.TRUE. 时最高能量中间点不受弹簧力约束，向鞍点精确爬升。"
default_behavior: ".FALSE. (标准 NEB)"
common_use:
  - CI-NEB transition state search
risk_if_misused:
  - "LCLIMB=.TRUE. 需配合紧力收敛标准 (EDIFFG ≤ -0.03)，否则鞍点不准"
domain_guidance:
  - example_status: needs_verification
    rule: "TS search → LCLIMB=.TRUE. + EDIFFG=-0.03 to -0.05"
    applies_to: {tasks: [ts_search, ci-neb]}
    value: ".TRUE."
    reason: "CI-NEB 精确收敛鞍点; EDIFFG 紧保证鞍点力收敛"
parameter_relations:
  - example_status: needs_verification
    target: EDIFFG
    relation: requires_companion
    desc: "LCLIMB=.TRUE. 时 EDIFFG 必须设为负值 (≤ -0.03)"
related_parameters:
  - EDIFFG
  - IMAGES
  - SPRING
~~~

~~~yaml
record_id: vasp-param-ldau-0223
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LDAU"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LDAU
version_or_doc_date: VASP Wiki; checked 2026-05-24
claim: "LDAU 是 DFT+U 总开关。LDAU=.TRUE. 激活 Hubbard U 校正。"
evidence_level: should
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/vasp_dft_plus_u_guide.md
related_records:
  - vasp-param-ldautype-0227
  - vasp-param-ldaul-0225
  - vasp-param-ldauu-0228
  - rel-vasp-dft-plus-u-0003
note: "只设 LDAU=.TRUE. 不设 LDAUL/LDAUU → 所有元素 U=0 → +U 不生效。LDAUTYPE=2 (Dudarev) 最常用。"
last_checked: 2026-05-24
parameter_name: "LDAU"
file_or_context: INCAR
definition: "DFT+U 总开关。.TRUE. 激活 Hubbard 模型校正选定原子的 d/f 电子强关联。"
default_behavior: ".FALSE. (VASP 默认)"
common_use:
  - {when: "3d TM 氧化物/氢氧化物 (NiO/CoO/FeO)", value: ".TRUE.", priority: should}
  - {when: "金属 Ni/Co/Fe slab (金属态)", value: "可设 .TRUE. 但 U 值一般较小", priority: ok}
  - {when: "Pt/Pd/Cu 金属 slab", value: ".FALSE. (d band 填满/近满)", priority: ok}
risk_if_misused:
  - "开了 LDAU=.TRUE. 但 LDAUL/LDAUU 未配 → U=0 无效果"
  - "金属体系不必要的 +U → 可能过度局域化 d 电子 → 带结构/吸附能偏差"
parameter_relations:
  - target: LDAUL
    example_status: needs_verification
    relation: requires_companion
  - target: LDAUU
    example_status: needs_verification
    relation: requires_companion
  - target: LDAUTYPE
    example_status: needs_verification
    relation: overrides
    desc: "LDAUTYPE 决定 U 的双重计数方式"
domain_guidance:
  - rule: "Ni/Co/Fe 氧化物/氢氧化物 → LDAU=.TRUE."
    example_status: needs_verification
  - rule: "Pt/Pd 金属 → LDAU=.FALSE."
    example_status: needs_verification
related_parameters:
  - LDAUL
  - LDAUU
  - LDAUTYPE
~~~

~~~yaml
record_id: vasp-param-ldauj-0224
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LDAUJ"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LDAUJ
version_or_doc_date: VASP Wiki; checked 2026-05-24
claim: "LDAUJ 设定每个原子种类的 Hund 耦合 J 值 (eV)。Dudarev (LDAUTYPE=2) 时 J 对结果影响小。"
evidence_level: check
confidence: official
related_wiki: []
related_records: [vasp-param-ldauu-0228, vasp-param-ldautype-0227, rel-vasp-dft-plus-u-0003]
note: "LDAUTYPE=2 时 U_eff=U-J → J 值不影响 U_eff 只要 U-J 一致。通常设 J=1.0。"
last_checked: 2026-05-24
parameter_name: "LDAUJ"
file_or_context: INCAR
definition: "每个原子种类的 Hund J (eV)，按 POSCAR 原子种类排列。"
default_behavior: "LDAUJ=1.0"
common_use:
  - {when: "Dudarev +U (LDAUTYPE=2)", value: 1.0, priority: ok}
parameter_relations:
  - {example_status: needs_verification, target: LDAUU, relation: mutually_constrained, desc: "U_eff = LDAUU - LDAUJ"}
  - {example_status: needs_verification, target: LDAUTYPE, relation: overridden_by, desc: "LDAUTYPE=2 时只用 U_eff"}
related_parameters: [LDAUU, LDAUTYPE]
~~~

~~~yaml
record_id: vasp-param-ldaul-0225
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LDAUL"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LDAUL
version_or_doc_date: VASP Wiki; checked 2026-05-24
claim: "LDAUL 指定每个原子种类加 U 的轨道量子数: 2=d; 3=f; -1=不加U。"
evidence_level: must
confidence: official
related_wiki: []
related_records: [vasp-param-ldau-0223, vasp-param-ldauu-0228, rel-vasp-dft-plus-u-0003]
note: "必须为每个原子种类指定。按 POSCAR 中 atom types 顺序排列。LDAUL=-1 表示该元素不加 U。"
last_checked: 2026-05-24
parameter_name: "LDAUL"
file_or_context: INCAR
definition: "每个原子种类的轨道角动量量子数: -1=off; 0=s; 1=p; 2=d; 3=f。"
default_behavior: "LDAUL=-1*NTYP (全部不加U)"
common_use:
  - {when: "3d TM (Ni/Co/Fe) +U", value: "2 for TM, -1 for O/H", priority: must}
  - {when: "4f rare-earth", value: "3 for f-element", priority: must}
risk_if_misused:
  - "LDAUL 设错 → 给不需要 U 的元素加了 U → 结果偏差大"
  - "LDAUL 设为 -1 但 LDAUU 非零 → U 值被忽略 (浪费)"
parameter_relations:
  - {example_status: needs_verification, target: LDAUU, relation: requires_companion, desc: "LDAUL=2 需配合 LDAUU"}
related_parameters: [LDAU, LDAUU]
~~~

~~~yaml
record_id: vasp-param-ldauprint-0226
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LDAUPRINT"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LDAUPRINT
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LDAUPRINT" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LDAUPRINT"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ldautype-0227
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LDAUTYPE"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LDAUTYPE
version_or_doc_date: VASP Wiki; checked 2026-05-24
claim: "LDAUTYPE 选择 DFT+U 的双重计数修正方式。2=Dudarev (最常用, U_eff=U-J)。"
evidence_level: should
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/vasp_dft_plus_u_guide.md
related_records:
  - vasp-param-ldau-0223
  - vasp-param-ldauu-0228
  - rel-vasp-dft-plus-u-0003
note: "LDAUTYPE=2 (Dudarev) 是催化领域最常用，只需设 U_eff。LDAUTYPE=1 (Liechtenstein) 需独立设 U 和 J。"
last_checked: 2026-05-24
parameter_name: "LDAUTYPE"
file_or_context: INCAR
definition: "双计数修正方案: 1=Liechtenstein; 2=Dudarev (旋转不变); 4=fully localized limit。"
default_behavior: "LDAUTYPE=2 (VASP 默认)"
common_use:
  - {when: "催化 DFT+U 计算", value: 2, priority: should}
risk_if_misused:
  - "LDAUTYPE=1 需分别指定 U 和 J (较复杂)"
  - "LDAUTYPE=2 中 U_eff=U-J → 只需设 LDAUU 作为 U_eff"
parameter_relations:
  - target: LDAUJ
    example_status: needs_verification
    relation: overrides
    desc: "LDAUTYPE=2 时 LDAUJ 对结果影响很小 (U_eff=U-J)"
domain_guidance:
  - rule: "催化计算 → LDAUTYPE=2"
    example_status: needs_verification
    value: 2
related_parameters:
  - LDAU
  - LDAUU
  - LDAUJ
~~~

~~~yaml
record_id: vasp-param-ldauu-0228
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LDAUU"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LDAUU
version_or_doc_date: VASP Wiki; checked 2026-05-24
claim: "LDAUU 设定每个原子种类的有效 Hubbard U 值 (eV)。LDAUTYPE=2 时即 U_eff。"
evidence_level: check
confidence: local_unverified
related_wiki:
  - computer_kb/wiki/concepts/vasp_dft_plus_u_guide.md
related_records:
  - vasp-param-ldau-0223
  - vasp-param-ldaul-0225
  - rel-vasp-dft-plus-u-0003
note: "U 值选取没有通用标准——不同泛函/价态/配位的有效 U 不同。必须做 U 扫描验证。以下为文献常见范围。"
last_checked: 2026-05-24
parameter_name: "LDAUU"
file_or_context: INCAR
definition: "每个原子种类的 Hubbard U 值 (eV)。LDAUTYPE=2 时 U_eff = LDAUU - LDAUJ。"
default_behavior: "0.0 eV (不加 U)"
common_use:
  - {when: "Ni 氧化物/氢氧化物 (PBE)", value: "U_eff = 3.5-6.0 (文献范围)", priority: check}
  - {when: "Co 氧化物 (PBE)", value: "U_eff = 3.0-4.0", priority: check}
  - {when: "Fe 氧化物 (PBE)", value: "U_eff = 4.0-5.0", priority: check}
  - {when: "Mn 氧化物 (PBE)", value: "U_eff = 3.5-5.0", priority: check}
risk_if_misused:
  - "U 值过大 → 过度局域化 → 带隙虚高/吸附能偏差"
  - "U 值过小 → +U 几乎无效果"
  - "不同泛函 (PBE/SCAN) 的有效 U 不同，不可直接照搬"
parameter_relations:
  - target: LDAUTYPE
    example_status: needs_verification
    relation: overrides
    desc: "Dudarev 时 U_eff=U-J; Liechtenstein 时 U 和 J 独立"
  - target: LDAUL
    example_status: needs_verification
    relation: requires_companion
    desc: "LDAUL 指定哪个轨道加 U"
domain_guidance:
  - rule: "Ni(OH)₂/NiOOH → 需做 U=3.5/4.5/5.5 扫描"
    example_status: needs_verification
  - rule: "Pt/Pd 金属 → 不加 U"
    example_status: needs_verification
related_parameters:
  - LDAUJ
  - LDAUL
  - LDAUTYPE
~~~

~~~yaml
record_id: vasp-param-ldiag-0229
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LDIAG"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LDIAG
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LDIAG" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LDIAG"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ldipol-0230
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LDIPOL"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LDIPOL
version_or_doc_date: VASP Wiki; checked 2026-05-24
claim: "LDIPOL 激活偶极校正。LDIPOL=.TRUE. 需配合 IDIPOL 指定校正方向。"
evidence_level: should
confidence: official
related_wiki: []
related_records: [vasp-param-idipol-0159]
note: "LDIPOL=.TRUE.+IDIPOL=3 是 slab 计算的标准偶极校正设置。"
last_checked: 2026-05-24
parameter_name: "LDIPOL"
file_or_context: INCAR
definition: "偶极校正开关。"
default_behavior: "LDIPOL=.FALSE."
common_use:
  - {when: "非对称 slab", value: ".TRUE.", priority: should}
related_parameters: [IDIPOL]
~~~

~~~yaml
record_id: vasp-param-ldisentangled-0231
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LDISENTANGLED"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LDISENTANGLED
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LDISENTANGLED" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LDISENTANGLED"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ldmatrix-0232
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LDMATRIX"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LDMATRIX
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LDMATRIX" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LDMATRIX"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ldownsample-0233
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LDOWNSAMPLE"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LDOWNSAMPLE
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LDOWNSAMPLE" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LDOWNSAMPLE"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lefg-0234
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LEFG"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LEFG
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LEFG" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LEFG"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lelf-0235
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LELF"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LELF
version_or_doc_date: VASP Wiki; checked 2026-05-24
claim: "LELF 控制是否写出 ELFCAR (电子局域函数)。用于化学键分析。"
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: "ELF 分析可视化共价键和孤对电子。催化界面中用于分析吸附键性质。"
last_checked: 2026-05-24
parameter_name: "LELF"
file_or_context: INCAR
definition: "是否写 ELFCAR (电子局域函数)。"
default_behavior: "LELF=.FALSE."
common_use:
  - {when: "化学键/电子结构可视化", value: ".TRUE.", priority: ok}
  - {when: "仅能量", value: ".FALSE.", priority: ok}
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lepsilon-0236
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LEPSILON"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LEPSILON
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LEPSILON" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LEPSILON"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lfinite-temperature-0237
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LFINITE TEMPERATURE"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LFINITE_TEMPERATURE
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LFINITE TEMPERATURE" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LFINITE TEMPERATURE"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lfockace-0238
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LFOCKACE"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LFOCKACE
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LFOCKACE" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LFOCKACE"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lfockaedft-0239
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LFOCKAEDFT"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LFOCKAEDFT
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LFOCKAEDFT" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LFOCKAEDFT"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lfockstd-0240
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LFOCKSTD"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LFOCKSTD
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LFOCKSTD" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LFOCKSTD"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lfxc-0241
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LFXC"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LFXC
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LFXC" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LFXC"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lh5-0242
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LH5"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LH5
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LH5" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LH5"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lhartree-0243
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LHARTREE"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LHARTREE
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LHARTREE" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LHARTREE"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lhfcalc-0244
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LHFCALC"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LHFCALC
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LHFCALC" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LHFCALC"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lhyperfine-0245
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LHYPERFINE"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LHYPERFINE
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LHYPERFINE" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LHYPERFINE"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-libmbd-alpha-0246
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LIBMBD ALPHA"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LIBMBD_ALPHA
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LIBMBD ALPHA" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LIBMBD ALPHA"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-libmbd-c6au-0247
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LIBMBD C6AU"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LIBMBD_C6AU
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LIBMBD C6AU" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LIBMBD C6AU"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-libmbd-k-grid-0248
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LIBMBD K GRID"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LIBMBD_K_GRID
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LIBMBD K GRID" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LIBMBD K GRID"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-libmbd-k-grid-shift-0249
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LIBMBD K GRID SHIFT"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LIBMBD_K_GRID_SHIFT
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LIBMBD K GRID SHIFT" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LIBMBD K GRID SHIFT"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-libmbd-mbd-a-0250
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LIBMBD MBD A"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LIBMBD_MBD_A
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LIBMBD MBD A" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LIBMBD MBD A"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-libmbd-mbd-beta-0251
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LIBMBD MBD BETA"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LIBMBD_MBD_BETA
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LIBMBD MBD BETA" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LIBMBD MBD BETA"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-libmbd-method-0252
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LIBMBD METHOD"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LIBMBD_METHOD
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LIBMBD METHOD" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LIBMBD METHOD"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-libmbd-n-omega-grid-0253
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LIBMBD N OMEGA GRID"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LIBMBD_N_OMEGA_GRID
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LIBMBD N OMEGA GRID" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LIBMBD N OMEGA GRID"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-libmbd-parallel-mode-0254
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LIBMBD PARALLEL MODE"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LIBMBD_PARALLEL_MODE
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LIBMBD PARALLEL MODE" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LIBMBD PARALLEL MODE"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-libmbd-r0au-0255
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LIBMBD R0AU"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LIBMBD_R0AU
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LIBMBD R0AU" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LIBMBD R0AU"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-libmbd-ts-d-0256
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LIBMBD TS D"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LIBMBD_TS_D
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LIBMBD TS D" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LIBMBD TS D"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-libmbd-ts-sr-0257
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LIBMBD TS SR"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LIBMBD_TS_SR
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LIBMBD TS SR" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LIBMBD TS SR"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-libmbd-vdw-params-kind-0258
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LIBMBD VDW PARAMS KIND"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LIBMBD_VDW_PARAMS_KIND
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LIBMBD VDW PARAMS KIND" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LIBMBD VDW PARAMS KIND"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-libmbd-xc-0259
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LIBMBD XC"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LIBMBD_XC
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LIBMBD XC" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LIBMBD XC"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-libxc1-0260
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LIBXC1"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LIBXC1
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LIBXC1" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LIBXC1"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-libxc1-pn-0261
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LIBXC1 Pn"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LIBXC1_Pn
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LIBXC1 Pn" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LIBXC1 Pn"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-libxc2-0262
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LIBXC2"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LIBXC2
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LIBXC2" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LIBXC2"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-libxc2-pn-0263
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LIBXC2 Pn"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LIBXC2_Pn
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LIBXC2 Pn" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LIBXC2 Pn"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lkpoints-opt-0264
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LKPOINTS OPT"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LKPOINTS_OPT
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LKPOINTS OPT" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LKPOINTS OPT"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lkpoints-wan-0265
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LKPOINTS WAN"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LKPOINTS_WAN
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LKPOINTS WAN" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LKPOINTS WAN"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lkproj-0266
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LKPROJ"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LKPROJ
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LKPROJ" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LKPROJ"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-llraug-0267
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LLRAUG"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LLRAUG
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LLRAUG" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LLRAUG"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lmaxfock-0268
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LMAXFOCK"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LMAXFOCK
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LMAXFOCK" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LMAXFOCK"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lmaxmix-0269
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LMAXMIX"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LMAXMIX
version_or_doc_date: VASP Wiki; checked 2026-05-24
claim: "LMAXMIX 控制电荷密度混合的最大角量子数。d/f 电子体系需 ≥ 4。"
evidence_level: should
confidence: official
related_wiki: []
related_records: [vasp-param-amix-0012]
note: "含 d 电子 (Pt/Ni/Co) 设 LMAXMIX=4; 含 f 电子设 LMAXMIX=6。对 SCF 收敛有显著影响。"
last_checked: 2026-05-24
parameter_name: "LMAXMIX"
file_or_context: INCAR
definition: "电荷密度混合中考虑的最大 L 通道。LMAXMIX=2 仅含 s/p，LMAXMIX=4 含 d，LMAXMIX=6 含 f。"
default_behavior: "LMAXMIX=2"
common_use:
  - {when: "sp 元素体系", value: 2, priority: ok}
  - {when: "d 电子金属 (Pt/Ni/Co/Cu)", value: 4, priority: must}
  - {when: "f 电子 (Ce/U 等)", value: 6, priority: must}
risk_if_misused:
  - "含 d 电子但 LMAXMIX=2 → d 通道不参与混合 → SCF 收敛困难"
parameter_relations: [{example_status: needs_verification, target: AMIX, relation: coupled_accuracy}]
domain_guidance: [{example_status: needs_verification, rule: "Pt/Ni/Co → LMAXMIX=4", value: 4, reason: "d 电子参与电荷密度混合"}]
related_parameters: [AMIX]
~~~

~~~yaml
record_id: vasp-param-lmaxpaw-0270
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LMAXPAW"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LMAXPAW
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LMAXPAW" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LMAXPAW"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lmaxtau-0271
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LMAXTAU"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LMAXTAU
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LMAXTAU" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LMAXTAU"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lmixtau-0272
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LMIXTAU"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LMIXTAU
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LMIXTAU" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LMIXTAU"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lmodelhf-0273
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LMODELHF"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LMODELHF
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LMODELHF" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LMODELHF"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lmono-0274
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LMONO"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LMONO
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LMONO" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LMONO"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lmp2lt-0275
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LMP2LT"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LMP2LT
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LMP2LT" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LMP2LT"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lnabla-0276
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LNABLA"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LNABLA
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LNABLA" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LNABLA"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lnicsall-0277
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LNICSALL"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LNICSALL
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LNICSALL" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LNICSALL"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lnmr-sym-red-0278
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LNMR SYM RED"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LNMR_SYM_RED
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LNMR SYM RED" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LNMR SYM RED"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lnmrcar-0279
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LNMRCAR"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LNMRCAR
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LNMRCAR" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LNMRCAR"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lnmrleg-0280
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LNMRLEG"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LNMRLEG
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LNMRLEG" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LNMRLEG"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lnmrshield-0281
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LNMRSHIELD"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LNMRSHIELD
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LNMRSHIELD" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LNMRSHIELD"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lnoaugxc-0282
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LNOAUGXC"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LNOAUGXC
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LNOAUGXC" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LNOAUGXC"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lnoncollinear-0283
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LNONCOLLINEAR"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LNONCOLLINEAR
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LNONCOLLINEAR" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LNONCOLLINEAR"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-locproj-0284
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LOCPROJ"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LOCPROJ
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LOCPROJ" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LOCPROJ"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-loptics-0285
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LOPTICS"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LOPTICS
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LOPTICS" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LOPTICS"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lorbit-0286
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LORBIT"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LORBIT
version_or_doc_date: VASP Wiki; checked 2026-05-24
claim: "LORBIT 控制 PROCAR/PDOS 输出。LORBIT=11 输出元素和轨道分解的 PDOS (含 spd 投影)。"
evidence_level: check
confidence: official
related_wiki: []
related_records: [vasp-param-rwigs-0544]
note: "LORBIT=10/11 均使用 PAW 投影，不依赖 RWIGS。LORBIT=11 额外输出相位因子。"
last_checked: 2026-05-24
parameter_name: "LORBIT"
file_or_context: INCAR
definition: "局域投影开关: 0-5 控制 PROCAR; 10-12 控制 PDOS (LM 分解)。"
default_behavior: "LORBIT=0 (无投影)"
common_use:
  - {when: "PDOS/d-band center 分析", value: 11, priority: should}
  - {when: "仅总 DOS", value: 10, priority: ok}
  - {when: "仅能量", value: 0, priority: ok}
risk_if_misused:
  - "LORBIT≥10 使用 PAW 投影 → 不依赖 RWIGS; LORBIT<10 需要手动设 RWIGS"
domain_guidance:
  - example_status: needs_verification
    rule: "PDOS/d-band center → LORBIT=11 (lm-decomposed + phase)"
    applies_to: {tasks: [pdos, d_band_center, electronic_structure]}
    value: 11
    reason: "LORBIT=11 输出完整 lm 分解 PROCAR; 不依赖 RWIGS"
parameter_relations:
  - example_status: needs_verification
    target: NEDOS
    relation: coupled_accuracy
    desc: "LORBIT 提供投影 → NEDOS 决定能量轴分辨率 → 共同决定 d-band center 精度"
  - example_status: needs_verification
    target: ICHARG
    relation: prerequisite
    desc: "ICHARG=11 (non-SCF) 是 PDOS 高效模式; LORBIT≥10 在此模式下输出完整 PROCAR"
~~~

~~~yaml
record_id: vasp-param-lorbmom-0287
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LORBMOM"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LORBMOM
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LORBMOM" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LORBMOM"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lpard-0288
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LPARD"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LPARD
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LPARD" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LPARD"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lpardh5-0289
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LPARDH5"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LPARDH5
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LPARDH5" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LPARDH5"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lpead-0290
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LPEAD"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LPEAD
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LPEAD" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LPEAD"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lphon-dispersion-0291
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LPHON DISPERSION"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LPHON_DISPERSION
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LPHON DISPERSION" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LPHON DISPERSION"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lphon-polar-0292
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LPHON POLAR"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LPHON_POLAR
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LPHON POLAR" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LPHON POLAR"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lphon-read-force-constants-0293
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LPHON READ FORCE CONSTANTS"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LPHON_READ_FORCE_CONSTANTS
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LPHON READ FORCE CONSTANTS" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LPHON READ FORCE CONSTANTS"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lplane-0294
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LPLANE"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LPLANE
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LPLANE" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LPLANE"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lposnics-0295
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LPOSNICS"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LPOSNICS
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LPOSNICS" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LPOSNICS"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lreal-0296
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LREAL"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LREAL
version_or_doc_date: VASP Wiki; checked 2026-05-24
claim: "LREAL 控制 PAW 投影在实空间还是倒空间进行。实空间投影更快但小超胞有精度损失。"
evidence_level: should
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/vasp_scf_accuracy_chain.md
related_records:
  - vasp-param-prec-0530
  - vasp-param-addgrid-0001
  - rel-vasp-scf-precision-chain-0001
note: "大体系 (>10 Å 超胞) 用 Auto 有显著加速; 小体系用 .FALSE. 保证精度。PREC=High 强制 .FALSE.。"
last_checked: 2026-05-24
parameter_name: "LREAL"
file_or_context: INCAR
definition: "PAW 非局域部分投影方式: .FALSE.=倒空间投影(准); Auto=实空间投影(快); O=自动切换。"
default_behavior: "LREAL=.FALSE. (VASP 默认; PREC 可覆盖)"
common_use:
  - {when: "小超胞 (<10Å) + 精确力", value: ".FALSE.", priority: should}
  - {when: "大 slab (>15Å) + AIMD", value: Auto, priority: should}
  - {when: "快速测试", value: Auto, priority: ok}
risk_if_misused:
  - "LREAL=Auto + 小超胞 (<10Å) → 投影网格太稀疏 → 力不准"
  - "LREAL=.FALSE. + 大体系 (>200 原子) → 极慢"
parameter_relations:
  - target: PREC
    example_status: needs_verification
    relation: overridden_by
    desc: "PREC=High 强制 LREAL=.FALSE."
domain_guidance:
  - rule: "Pt(111) 3×3 ~15Å + AIMD → LREAL=Auto"
    example_status: needs_verification
    applies_to: {systems: [metal_water_slab > 15Å], tasks: [aimd]}
    value: Auto
    reason: "超胞足够大 → 实空间投影精度足够 + 加速显著"
related_parameters:
  - PREC
  - ADDGRID
~~~

~~~yaml
record_id: vasp-param-lrhfcalc-0297
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LRHFCALC"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LRHFCALC
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LRHFCALC" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LRHFCALC"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lrpa-0298
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LRPA"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LRPA
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LRPA" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LRPA"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lrpaforce-0299
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LRPAFORCE"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LRPAFORCE
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LRPAFORCE" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LRPAFORCE"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lscaaware-0300
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LSCAAWARE"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LSCAAWARE
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LSCAAWARE" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LSCAAWARE"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lscalapack-0301
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LSCALAPACK"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LSCALAPACK
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LSCALAPACK" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LSCALAPACK"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lscaler0-0302
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LSCALER0"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LSCALER0
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LSCALER0" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LSCALER0"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lscalu-0303
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LSCALU"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LSCALU
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LSCALU" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LSCALU"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lscdm-0304
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LSCDM"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LSCDM
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LSCDM" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LSCDM"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lsck-0305
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LSCK"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LSCK
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LSCK" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LSCK"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lscrpa-0306
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LSCRPA"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LSCRPA
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LSCRPA" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LSCRPA"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lscsgrad-0307
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LSCSGRAD"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LSCSGRAD
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LSCSGRAD" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LSCSGRAD"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lselfenergy-0308
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LSELFENERGY"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LSELFENERGY
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LSELFENERGY" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LSELFENERGY"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lsepb-0309
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LSEPB"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LSEPB
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LSEPB" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LSEPB"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lsepk-0310
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LSEPK"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LSEPK
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LSEPK" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LSEPK"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lsfbxc-0311
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LSFBXC"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LSFBXC
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LSFBXC" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LSFBXC"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lsingles-0312
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LSINGLES"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LSINGLES
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LSINGLES" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LSINGLES"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lsmp2lt-0313
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LSMP2LT"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LSMP2LT
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LSMP2LT" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LSMP2LT"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lsorbit-0314
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LSORBIT"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LSORBIT
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LSORBIT" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LSORBIT"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lsoshift-0315
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LSOSHIFT"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LSOSHIFT
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LSOSHIFT" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LSOSHIFT"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lspectral-0316
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LSPECTRAL"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LSPECTRAL
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LSPECTRAL" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LSPECTRAL"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lspectralgw-0317
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LSPECTRALGW"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LSPECTRALGW
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LSPECTRALGW" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LSPECTRALGW"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lspin-vdw-0318
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LSPIN VDW"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LSPIN_VDW
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LSPIN VDW" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LSPIN VDW"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lspiral-0319
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LSPIRAL"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LSPIRAL
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LSPIRAL" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LSPIRAL"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lsubrot-0320
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LSUBROT"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LSUBROT
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LSUBROT" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LSUBROT"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lsynch5-0321
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LSYNCH5"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LSYNCH5
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LSYNCH5" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LSYNCH5"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ltau-0322
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LTAU"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LTAU
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LTAU" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LTAU"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ltboundlibxc-0323
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LTBOUNDLIBXC"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LTBOUNDLIBXC
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LTBOUNDLIBXC" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LTBOUNDLIBXC"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ltemper-0324
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LTEMPER"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LTEMPER
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LTEMPER" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LTEMPER"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lthomas-0325
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LTHOMAS"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LTHOMAS
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LTHOMAS" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LTHOMAS"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ltriplet-0326
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LTRIPLET"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LTRIPLET
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LTRIPLET" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LTRIPLET"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ltssurf-0327
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LTSSURF"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LTSSURF
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LTSSURF" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LTSSURF"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ltwo-center-0328
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LTWO CENTER"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LTWO_CENTER
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LTWO CENTER" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LTWO CENTER"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-luse-vdw-0329
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LUSE VDW"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LUSE_VDW
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LUSE VDW" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LUSE VDW"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lusenccl-0330
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LUSENCCL"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LUSENCCL
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LUSENCCL" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LUSENCCL"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lvacpotav-0331
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LVACPOTAV"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LVACPOTAV
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LVACPOTAV" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LVACPOTAV"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lvdw-ewald-0332
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LVDW EWALD"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LVDW_EWALD
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LVDW EWALD" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LVDW EWALD"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lvdw-onecell-0333
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LVDW ONECELL"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LVDW_ONECELL
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LVDW ONECELL" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LVDW ONECELL"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lvdwexpansion-0334
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LVDWEXPANSION"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LVDWEXPANSION
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LVDWEXPANSION" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LVDWEXPANSION"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lvdwscs-0335
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LVDWSCS"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LVDWSCS
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LVDWSCS" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LVDWSCS"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lvgvappl-0336
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LVGVAPPL"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LVGVAPPL
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LVGVAPPL" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LVGVAPPL"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lvgvcalc-0337
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LVGVCALC"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LVGVCALC
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LVGVCALC" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LVGVCALC"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lvhar-0338
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LVHAR"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LVHAR
version_or_doc_date: VASP Wiki; checked 2026-05-24
claim: "LVHAR 控制是否写出 LOCPOT (局域电势) 文件。用于功函数/Bader charge 分析。"
evidence_level: check
confidence: official
related_wiki: []
related_records: [vasp-param-lvtot-0339]
note: "LVHAR 写 LOCPOT 含离子势 + Hartree 势。功函数分析需 LVHAR=.TRUE. + 真空层。"
last_checked: 2026-05-24
parameter_name: "LVHAR"
file_or_context: INCAR
definition: "是否写 LOCPOT 文件。含局域静电势 (无 XC 势)。"
default_behavior: "LVHAR=.FALSE."
common_use:
  - {when: "功函数/界面 dipole 分析", value: ".TRUE.", priority: should}
  - {when: "仅能量", value: ".FALSE.", priority: ok}
related_parameters: [LVTOT]
~~~

~~~yaml
record_id: vasp-param-lvtot-0339
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LVTOT"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LVTOT
version_or_doc_date: VASP Wiki; checked 2026-05-24
claim: "LVTOT 控制是否写出 LOCPOT 含 XC 势。与 LVHAR 类似但包含交换关联势贡献。"
evidence_level: check
confidence: official
related_wiki: []
related_records: [vasp-param-lvhar-0338]
note: "LVTOT 写 LOCPOT 含 XC 势。功函数/电子结构分析可用 LVHAR 或 LVTOT。"
last_checked: 2026-05-24
parameter_name: "LVTOT"
file_or_context: INCAR
definition: "是否写 LOCPOT (含 XC 势)。"
default_behavior: "LVTOT=.FALSE."
common_use:
  - {when: "功函数/静电势分析", value: ".TRUE.", priority: should}
related_parameters: [LVHAR]
~~~

~~~yaml
record_id: vasp-param-lwannier90-0340
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LWANNIER90"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LWANNIER90
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LWANNIER90" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LWANNIER90"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lwannier90-run-0341
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LWANNIER90 RUN"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LWANNIER90_RUN
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LWANNIER90 RUN" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LWANNIER90 RUN"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lwave-0342
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LWAVE"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LWAVE
version_or_doc_date: VASP Wiki; checked 2026-05-24
claim: "LWAVE 控制是否写出 WAVECAR。AIMD 可关以省 IO 和磁盘。"
evidence_level: check
confidence: official
related_wiki: []
related_records: [vasp-param-lcharg-0219]
note: "AIMD 每步写 WAVECAR 是大文件 (~GB)。推荐 AIMD 设 LWAVE=.FALSE.。需续跑时最后一步写。"
last_checked: 2026-05-24
parameter_name: "LWAVE"
file_or_context: INCAR
definition: "是否写 WAVECAR (波函数文件)。"
default_behavior: "LWAVE=.TRUE."
common_use:
  - {when: "SCF/几何优化 (方便续跑)", value: ".TRUE.", priority: ok}
  - {when: "AIMD", value: ".FALSE.", priority: should}
risk_if_misused:
  - "AIMD 开 LWAVE → 每步 GB 级 IO → 严重拖慢"
~~~

~~~yaml
record_id: vasp-param-lwaveh5-0343
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LWAVEH5"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LWAVEH5
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LWAVEH5" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LWAVEH5"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lweighted-0344
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LWEIGHTED"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LWEIGHTED
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LWEIGHTED" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LWEIGHTED"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lwrite-mmn-amn-0345
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LWRITE MMN AMN"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LWRITE_MMN_AMN
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LWRITE MMN AMN" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LWRITE MMN AMN"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lwrite-spn-0346
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LWRITE SPN"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LWRITE_SPN
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LWRITE SPN" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LWRITE SPN"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lwrite-unk-0347
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LWRITE UNK"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LWRITE_UNK
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LWRITE UNK" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LWRITE UNK"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lwrite-wanproj-0348
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LWRITE WANPROJ"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LWRITE_WANPROJ
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LWRITE WANPROJ" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LWRITE WANPROJ"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lwrt-augmented-density-0349
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LWRT AUGMENTED DENSITY"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LWRT_AUGMENTED_DENSITY
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LWRT AUGMENTED DENSITY" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LWRT AUGMENTED DENSITY"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lzeroz-0350
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LZEROZ"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LZEROZ
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LZEROZ" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LZEROZ"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-lzora-0351
record_type: parameter
scope: single_software
software:
  - VASP
topic: "LZORA"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LZORA
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "LZORA" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "LZORA"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-m-constr-0352
record_type: parameter
scope: single_software
software:
  - VASP
topic: "M CONSTR"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/M_CONSTR
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "M CONSTR" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "M CONSTR"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-magmom-0353
record_type: parameter
scope: single_software
software:
  - VASP
topic: "MAGMOM"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/MAGMOM
version_or_doc_date: VASP Wiki; checked 2026-05-24
claim: "MAGMOM 设定每个原子的初始磁矩 (μB)。ISPIN=2 时必须配合。"
evidence_level: should
confidence: official
related_wiki: []
related_records:
  - vasp-param-ispin-0182
note: "初始磁矩只需合理 guess。Ni 3d⁸ → 2.0 μB; Co 3d⁷ → 2.5-3.0 μB; Fe 3d⁶ → 4.0 μB。VASP 会自动收敛到正确基态磁矩。"
last_checked: 2026-05-24
parameter_name: "MAGMOM"
file_or_context: INCAR
definition: "每个原子的初始磁矩 (Bohr magnetons); 按 POSCAR 中 atom types 排列。"
default_behavior: "NIONS×1.0"
common_use:
  - {when: "Ni slab", value: "Ni: 2.0*N_atoms", priority: should}
  - {when: "非磁性原子", value: "0.5*N_atoms (small starting value)", priority: ok}
risk_if_misused:
  - "初始磁矩设为 0 → 可能收敛到非磁性解 (即使真正的基态是磁性)"
parameter_relations:
  - {example_status: needs_verification, target: ISPIN, relation: prerequisite, desc: "ISPIN=2 时 MAGMOM 才有意义"}
domain_guidance:
  - {example_status: needs_verification, rule: "Ni→2.0; Co→2.5; Fe→4.0; Pt/Pd/Cu→0.5 or ISPIN=1"}
related_parameters: [ISPIN]
~~~

~~~yaml
record_id: vasp-param-maxmem-0354
record_type: parameter
scope: single_software
software:
  - VASP
topic: "MAXMEM"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/MAXMEM
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "MAXMEM" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "MAXMEM"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-maxmix-0355
record_type: parameter
scope: single_software
software:
  - VASP
topic: "MAXMIX"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/MAXMIX
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "MAXMIX" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "MAXMIX"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-mdalgo-0356
record_type: parameter
scope: single_software
software:
  - VASP
topic: "MDALGO"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/MDALGO
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "MDALGO" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "MDALGO"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-metagga-0357
record_type: parameter
scope: single_software
software:
  - VASP
topic: "METAGGA"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/METAGGA
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "METAGGA" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "METAGGA"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-minrot-0358
record_type: parameter
scope: single_software
software:
  - VASP
topic: "MINROT"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/MINROT
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "MINROT" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "MINROT"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-mixpre-0359
record_type: parameter
scope: single_software
software:
  - VASP
topic: "MIXPRE"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/MIXPRE
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "MIXPRE" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "MIXPRE"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ml-afilt2-0360
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ML AFILT2"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ML_AFILT2
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ML AFILT2" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ML AFILT2"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ml-calgo-0361
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ML CALGO"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ML_CALGO
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ML CALGO" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ML CALGO"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ml-cdoub-0362
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ML CDOUB"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ML_CDOUB
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ML CDOUB" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ML CDOUB"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ml-csig-0363
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ML CSIG"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ML_CSIG
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ML CSIG" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ML CSIG"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ml-cslope-0364
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ML CSLOPE"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ML_CSLOPE
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ML CSLOPE" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ML CSLOPE"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ml-ctifor-0365
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ML CTIFOR"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ML_CTIFOR
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ML CTIFOR" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ML CTIFOR"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ml-cx-0366
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ML CX"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ML_CX
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ML CX" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ML CX"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ml-desc-type-0367
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ML DESC TYPE"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ML_DESC_TYPE
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ML DESC TYPE" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ML DESC TYPE"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ml-eatom-ref-0368
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ML EATOM REF"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ML_EATOM_REF
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ML EATOM REF" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ML EATOM REF"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ml-emppot-rcut-0369
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ML EMPPOT RCUT"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ML_EMPPOT_RCUT
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ML EMPPOT RCUT" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ML EMPPOT RCUT"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ml-eps-low-0370
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ML EPS LOW"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ML_EPS_LOW
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ML EPS LOW" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ML EPS LOW"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ml-eps-reg-0371
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ML EPS REG"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ML_EPS_REG
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ML EPS REG" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ML EPS REG"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ml-estblock-0372
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ML ESTBLOCK"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ML_ESTBLOCK
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ML ESTBLOCK" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ML ESTBLOCK"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ml-grace-model-0373
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ML GRACE MODEL"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ML_GRACE_MODEL
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ML GRACE MODEL" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ML GRACE MODEL"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ml-iafilt2-0374
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ML IAFILT2"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ML_IAFILT2
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ML IAFILT2" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ML IAFILT2"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ml-ialgo-linreg-0375
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ML IALGO LINREG"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ML_IALGO_LINREG
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ML IALGO LINREG" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ML IALGO LINREG"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ml-icouple-0376
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ML ICOUPLE"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ML_ICOUPLE
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ML ICOUPLE" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ML ICOUPLE"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ml-icriteria-0377
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ML ICRITERIA"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ML_ICRITERIA
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ML ICRITERIA" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ML ICRITERIA"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ml-ireg-0378
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ML IREG"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ML_IREG
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ML IREG" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ML IREG"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ml-iscale-toten-0379
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ML ISCALE TOTEN"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ML_ISCALE_TOTEN
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ML ISCALE TOTEN" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ML ISCALE TOTEN"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ml-istart-0380
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ML ISTART"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ML_ISTART
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ML ISTART" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ML ISTART"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ml-iweight-0381
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ML IWEIGHT"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ML_IWEIGHT
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ML IWEIGHT" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ML IWEIGHT"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ml-lafilt2-0382
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ML LAFILT2"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ML_LAFILT2
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ML LAFILT2" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ML LAFILT2"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ml-lbasis-discard-0383
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ML LBASIS DISCARD"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ML_LBASIS_DISCARD
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ML LBASIS DISCARD" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ML LBASIS DISCARD"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ml-lcouple-0384
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ML LCOUPLE"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ML_LCOUPLE
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ML LCOUPLE" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ML LCOUPLE"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ml-leatom-0385
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ML LEATOM"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ML_LEATOM
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ML LEATOM" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ML LEATOM"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ml-lemppot-0386
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ML LEMPPOT"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ML_LEMPPOT
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ML LEMPPOT" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ML LEMPPOT"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ml-lerr-0387
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ML LERR"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ML_LERR
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ML LERR" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ML LERR"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ml-lfast-0388
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ML LFAST"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ML_LFAST
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ML LFAST" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ML LFAST"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ml-lheat-0389
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ML LHEAT"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ML_LHEAT
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ML LHEAT" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ML LHEAT"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ml-lib-0390
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ML LIB"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ML_LIB
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ML LIB" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ML LIB"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ml-lmax2-0391
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ML LMAX2"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ML_LMAX2
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ML LMAX2" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ML LMAX2"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ml-lsparsdes-0393
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ML LSPARSDES"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ML_LSPARSDES
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ML LSPARSDES" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ML LSPARSDES"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ml-luse-names-0394
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ML LUSE NAMES"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ML_LUSE_NAMES
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ML LUSE NAMES" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ML LUSE NAMES"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ml-mb-0395
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ML MB"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ML_MB
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ML MB" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ML MB"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ml-mb-min-0396
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ML MB MIN"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ML_MB_MIN
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ML MB MIN" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ML MB MIN"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ml-mconf-0397
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ML MCONF"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ML_MCONF
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ML MCONF" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ML MCONF"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ml-mconf-new-0398
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ML MCONF NEW"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ML_MCONF_NEW
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ML MCONF NEW" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ML MCONF NEW"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ml-mhis-0399
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ML MHIS"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ML_MHIS
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ML MHIS" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ML MHIS"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ml-mode-0400
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ML MODE"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ML_MODE
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ML MODE" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ML MODE"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ml-mopot-dm-0401
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ML MOPOT DM"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ML_MOPOT_DM
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ML MOPOT DM" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ML MOPOT DM"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ml-mopot-ijm-0402
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ML MOPOT IJM"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ML_MOPOT_IJM
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ML MOPOT IJM" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ML MOPOT IJM"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ml-mopot-nm-0403
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ML MOPOT NM"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ML_MOPOT_NM
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ML MOPOT NM" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ML MOPOT NM"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ml-mopot-rkm-0404
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ML MOPOT RKM"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ML_MOPOT_RKM
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ML MOPOT RKM" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ML MOPOT RKM"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ml-mopot-rm-0405
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ML MOPOT RM"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ML_MOPOT_RM
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ML MOPOT RM" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ML MOPOT RM"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ml-mrb1-0406
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ML MRB1"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ML_MRB1
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ML MRB1" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ML MRB1"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ml-mrb2-0407
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ML MRB2"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ML_MRB2
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ML MRB2" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ML MRB2"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ml-natom-coupled-0408
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ML NATOM COUPLED"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ML_NATOM_COUPLED
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ML NATOM COUPLED" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ML NATOM COUPLED"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ml-ncshmem-0409
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ML NCSHMEM"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ML_NCSHMEM
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ML NCSHMEM" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ML NCSHMEM"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ml-nhyp-0410
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ML NHYP"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ML_NHYP
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ML NHYP" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ML NHYP"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ml-nmdint-0411
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ML NMDINT"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ML_NMDINT
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ML NMDINT" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ML NMDINT"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ml-nrank-sparsdes-0412
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ML NRANK SPARSDES"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ML_NRANK_SPARSDES
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ML NRANK SPARSDES" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ML NRANK SPARSDES"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ml-outblock-0413
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ML OUTBLOCK"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ML_OUTBLOCK
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ML OUTBLOCK" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ML OUTBLOCK"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ml-output-mode-0414
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ML OUTPUT MODE"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ML_OUTPUT_MODE
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ML OUTPUT MODE" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ML OUTPUT MODE"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ml-rcouple-0415
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ML RCOUPLE"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ML_RCOUPLE
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ML RCOUPLE" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ML RCOUPLE"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ml-rcut1-0416
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ML RCUT1"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ML_RCUT1
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ML RCUT1" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ML RCUT1"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ml-rcut2-0417
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ML RCUT2"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ML_RCUT2
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ML RCUT2" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ML RCUT2"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ml-rdes-sparsdes-0418
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ML RDES SPARSDES"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ML_RDES_SPARSDES
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ML RDES SPARSDES" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ML RDES SPARSDES"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ml-sclc-ctifor-0419
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ML SCLC CTIFOR"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ML_SCLC_CTIFOR
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ML SCLC CTIFOR" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ML SCLC CTIFOR"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ml-sigv0-0420
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ML SIGV0"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ML_SIGV0
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ML SIGV0" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ML SIGV0"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ml-sigw0-0421
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ML SIGW0"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ML_SIGW0
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ML SIGW0" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ML SIGW0"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ml-sion1-0422
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ML SION1"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ML_SION1
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ML SION1" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ML SION1"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ml-sion2-0423
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ML SION2"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ML_SION2
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ML SION2" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ML SION2"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ml-srpot-b0-0424
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ML SRPOT B0"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ML_SRPOT_B0
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ML SRPOT B0" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ML SRPOT B0"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ml-srpot-n0-0425
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ML SRPOT N0"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ML_SRPOT_N0
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ML SRPOT N0" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ML SRPOT N0"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ml-srpot-s0-0426
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ML SRPOT S0"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ML_SRPOT_S0
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ML SRPOT S0" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ML SRPOT S0"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ml-type-0427
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ML TYPE"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ML_TYPE
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ML TYPE" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ML TYPE"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ml-w1-0428
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ML W1"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ML_W1
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ML W1" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ML W1"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ml-wtifor-0429
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ML WTIFOR"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ML_WTIFOR
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ML WTIFOR" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ML WTIFOR"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ml-wtoten-0430
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ML WTOTEN"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ML_WTOTEN
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ML WTOTEN" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ML WTOTEN"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ml-wtsif-0431
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ML WTSIF"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ML_WTSIF
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ML WTSIF" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ML WTSIF"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-naturalo-0432
record_type: parameter
scope: single_software
software:
  - VASP
topic: "NATURALO"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/NATURALO
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "NATURALO" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "NATURALO"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-nbands-0433
record_type: parameter
scope: single_software
software:
  - VASP
topic: "NBANDS"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/NBANDS
version_or_doc_date: VASP Wiki; checked 2026-05-24
claim: "NBANDS 手动设定能带数。通常不需设 (VASP 自动)。DOS/光学计算时可增大。"
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: "DOS 计算需足够空带 → NBANDS 设为默认值 × 1.5。金属 slab 通常不需手动设。"
last_checked: 2026-05-24
parameter_name: "NBANDS"
file_or_context: INCAR
definition: "总能带数 (占据+空带)。"
default_behavior: "自动 (基于电子数和展宽)"
common_use:
  - {when: "一般 SCF", value: "默认 (不设)", priority: ok}
  - {when: "DOS/光学 (需更多空带)", value: "默认×1.5", priority: should}
  - {when: "AIMD", value: "默认 (不设)", priority: ok}
risk_if_misused:
  - "NBANDS 过大 → 每电子步对角化代价增大"
~~~

~~~yaml
record_id: vasp-param-nbands-wave-0434
record_type: parameter
scope: single_software
software:
  - VASP
topic: "NBANDS WAVE"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/NBANDS_WAVE
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "NBANDS WAVE" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "NBANDS WAVE"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-nbandsexact-0435
record_type: parameter
scope: single_software
software:
  - VASP
topic: "NBANDSEXACT"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/NBANDSEXACT
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "NBANDSEXACT" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "NBANDSEXACT"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-nbandsgw-0436
record_type: parameter
scope: single_software
software:
  - VASP
topic: "NBANDSGW"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/NBANDSGW
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "NBANDSGW" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "NBANDSGW"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-nbandso-0437
record_type: parameter
scope: single_software
software:
  - VASP
topic: "NBANDSO"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/NBANDSO
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "NBANDSO" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "NBANDSO"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-nbandsv-0438
record_type: parameter
scope: single_software
software:
  - VASP
topic: "NBANDSV"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/NBANDSV
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "NBANDSV" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "NBANDSV"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-nblk-0439
record_type: parameter
scope: single_software
software:
  - VASP
topic: "NBLK"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/NBLK
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "NBLK" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "NBLK"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-nblock-0440
record_type: parameter
scope: single_software
software:
  - VASP
topic: "NBLOCK"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/NBLOCK
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "NBLOCK" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "NBLOCK"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-nblock-fock-0441
record_type: parameter
scope: single_software
software:
  - VASP
topic: "NBLOCK FOCK"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/NBLOCK_FOCK
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "NBLOCK FOCK" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "NBLOCK FOCK"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-nbmod-0442
record_type: parameter
scope: single_software
software:
  - VASP
topic: "NBMOD"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/NBMOD
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "NBMOD" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "NBMOD"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-nbseblocko-0443
record_type: parameter
scope: single_software
software:
  - VASP
topic: "NBSEBLOCKO"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/NBSEBLOCKO
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "NBSEBLOCKO" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "NBSEBLOCKO"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-nbseblockv-0444
record_type: parameter
scope: single_software
software:
  - VASP
topic: "NBSEBLOCKV"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/NBSEBLOCKV
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "NBSEBLOCKV" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "NBSEBLOCKV"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-nbseeig-0445
record_type: parameter
scope: single_software
software:
  - VASP
topic: "NBSEEIG"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/NBSEEIG
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "NBSEEIG" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "NBSEEIG"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ncore-0446
record_type: parameter
scope: single_software
software:
  - VASP
topic: "NCORE"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/NCORE
version_or_doc_date: VASP Wiki; checked 2026-05-24
claim: "NCORE 控制每个 band 的 MPI 并行核心数。影响内存和并行效率。"
evidence_level: check
confidence: official
related_wiki: []
related_records: [vasp-param-kpar-0197]
note: "NCORE 应整除总核数。AIMD 大体系建议 NCORE=4-8。NCORE×KPAR≤总核数。"
last_checked: 2026-05-24
parameter_name: "NCORE"
file_or_context: INCAR
definition: "每个 band 的并行核心数。控制 band-level 和 FFT-level 并行分配。"
default_behavior: "NCORE=1"
common_use:
  - {when: "单节点 (32-64 核)", value: 4, priority: should}
  - {when: "多节点 (>100 核)", value: 8, priority: should}
parameter_relations:
  - {example_status: needs_verification, target: KPAR, relation: mutually_constrained, desc: "NCORE × KPAR ≤ 总核数"}
related_parameters: [KPAR]
~~~

~~~yaml
record_id: vasp-param-ncore-in-image1-0447
record_type: parameter
scope: single_software
software:
  - VASP
topic: "NCORE IN IMAGE1"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/NCORE_IN_IMAGE1
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "NCORE IN IMAGE1" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "NCORE IN IMAGE1"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ncrpa-bands-0448
record_type: parameter
scope: single_software
software:
  - VASP
topic: "NCRPA BANDS"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/NCRPA_BANDS
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "NCRPA BANDS" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "NCRPA BANDS"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-nedos-0449
record_type: parameter
scope: single_software
software:
  - VASP
topic: "NEDOS"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/NEDOS
version_or_doc_date: VASP Wiki; checked 2026-05-24
claim: "NEDOS 控制 DOS 计算的能量网格点数。越大 DOS 曲线越平滑。"
evidence_level: check
confidence: official
related_wiki: []
related_records: [vasp-param-lorbit-0286]
note: "NEDOS=1000-3000 常用。d-band center 分析需足够 NEDOS (~2000) 以保证精度。"
last_checked: 2026-05-24
parameter_name: "NEDOS"
file_or_context: INCAR
definition: "DOS 能量网格点数。"
default_behavior: "NEDOS=301"
common_use:
  - {when: "快速 DOS", value: 301, priority: ok}
  - {when: "d-band center / 精细 DOS", value: 2000, priority: should}
risk_if_misused:
  - "NEDOS 过小 → DOS 锯齿 → d-band center 不准"
domain_guidance:
  - example_status: needs_verification
    rule: "d-band center 精度要求 (<0.02 eV) → NEDOS≥2000"
    applies_to: {tasks: [d_band_center, pdos, dos]}
    value: 2000
    reason: "NEDOS=301 (默认) → d-band center 离散误差 ~0.1 eV; NEDOS=2000 → <0.01 eV"
parameter_relations:
  - example_status: needs_verification
    target: LORBIT
    relation: coupled_accuracy
    desc: "NEDOS 决定能量轴分辨率 → PDOS 投影的质量受 NEDOS 制约"
  - example_status: needs_verification
    target: EMIN
    relation: mutually_constrained
    desc: "NEDOS 和 EMIN/EMAX 窗口共同决定了能量网格密度 ΔE = (EMAX−EMIN)/NEDOS"
~~~

~~~yaml
record_id: vasp-param-nelect-0450
record_type: parameter
scope: single_software
software:
  - VASP
topic: "NELECT"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/NELECT
version_or_doc_date: VASP Wiki; checked 2026-05-24
claim: "NELECT 手动设定总电子数。带电 slab 或氧化还原计算时用于加减电子。"
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: "电化学 CHE 模型中常需带电 slab。NELECT=默认+1 表示加一个电子 (负电荷)。"
last_checked: 2026-05-24
parameter_name: "NELECT"
file_or_context: INCAR
definition: "体系总电子数。默认值=各 POTCAR 价电子之和。"
default_behavior: "价电子总数"
common_use:
  - {when: "中性 slab", value: "默认 (不设)", priority: ok}
  - {when: "带电 slab (CHE)", value: "默认±N (N=电子数变化)", priority: check}
risk_if_misused:
  - "NELECT 设错 → 体系带电/放电量不对 → 能量-电压关系错误"
~~~

~~~yaml
record_id: vasp-param-nelm-0451
record_type: parameter
scope: single_software
software:
  - VASP
topic: "NELM"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/NELM
version_or_doc_date: VASP Wiki; checked 2026-05-24
claim: "NELM 设定每个电子步最大 SCF 迭代次数。达到仍未收敛则判定不收敛。"
evidence_level: should
confidence: official
related_wiki: [computer_kb/wiki/concepts/vasp_scf_accuracy_chain.md]
related_records:
  - vasp-param-nelmin-0454
  - vasp-param-ediff-0053
note: "NELM=60 是默认值。增加 NELM 治标不治本——应先解决收敛难的根本原因 (ALGO/AMIX)。"
last_checked: 2026-05-24
parameter_name: "NELM"
file_or_context: INCAR
definition: "每电子步最大 SCF 迭代次数上限。"
default_behavior: "NELM=60"
common_use:
  - {when: "正常计算", value: 60, priority: should}
  - {when: "难收敛体系 (d 电子+界面)", value: 100, priority: ok}
risk_if_misused:
  - "单纯增大 NELM 而不修 ALGO/AMIX → 60→100 步仍可能不收敛"
parameter_relations:
  - {example_status: needs_verification, target: NELMIN, relation: prerequisite, desc: "NELM ≥ NELMIN; 前 NELMIN 步不做收敛检查"}
domain_guidance:
  - {example_status: needs_verification, rule: "Pt/水 AIMD → NELM=60 起步 (每步仅需粗略收敛)", value: 60}
related_parameters: [NELMIN, EDIFF]
~~~

~~~yaml
record_id: vasp-param-nelmdl-0452
record_type: parameter
scope: single_software
software:
  - VASP
topic: "NELMDL"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/NELMDL
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "NELMDL" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "NELMDL"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-nelmgw-0453
record_type: parameter
scope: single_software
software:
  - VASP
topic: "NELMGW"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/NELMGW
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "NELMGW" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "NELMGW"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-nelmin-0454
record_type: parameter
scope: single_software
software:
  - VASP
topic: "NELMIN"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/NELMIN
version_or_doc_date: VASP Wiki; checked 2026-05-24
claim: "NELMIN 设定每电子步最少 SCF 迭代次数 (前 NELMIN 步不做收敛检查)。"
evidence_level: check
confidence: official
related_wiki: []
related_records: [vasp-param-nelm-0451]
note: "AIMD 每步通常不需要 NELMIN 限制; 几何优化第一步可能需要更多步稳定 initial wavefunction。"
last_checked: 2026-05-24
parameter_name: "NELMIN"
file_or_context: INCAR
definition: "每电子步最小 SCF 迭代步数。"
default_behavior: "NELMIN=2"
common_use:
  - {when: "一般计算", value: 2, priority: ok}
  - {when: "AIMD (每步 SCF 快速)", value: 2, priority: should}
risk_if_misused:
  - "NELMIN 过大 → 每步固定多跑迭代 → AIMD 耗时增加"
parameter_relations: [{example_status: needs_verification, target: NELM, relation: prerequisite}]
related_parameters: [NELM]
~~~

~~~yaml
record_id: vasp-param-nfree-0455
record_type: parameter
scope: single_software
software:
  - VASP
topic: "NFREE"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/NFREE
version_or_doc_date: VASP Wiki; checked 2026-05-24
claim: "NFREE 控制 IBRION=5 有限差分计算 Hessian 时每个离子的位移方向数。"
evidence_level: should
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/vasp_neb_chain.md
related_records:
  - vasp-param-ediff-0053
note: "NFREE=2 是常用默认值。IBRION=6 用对称差分自动算双向。"
last_checked: 2026-05-24
parameter_name: "NFREE"
file_or_context: INCAR
definition: "有限差分 Hessian 的位移方向数 (IBRION=5 生效)。值越大 Hessian 越准但位移次数线性增加。"
default_behavior: "NFREE=2 (VASP 默认)"
common_use:
  - {when: "一般振动频率", value: 2, priority: should}
risk_if_misused:
  - "NFREE 过小 + 低频软模 → Hessian 不准"
  - "NFREE 过大 + 大体系 → 计算量爆炸 (每离子每个方向一次 SCF)"
parameter_relations:
  - target: IBRION
    example_status: needs_verification
    relation: prerequisite
    desc: "只在 IBRION=5 时生效"
domain_guidance:
  - example_status: needs_verification
    rule: "NFREE=2 默认值足够大多数催化吸附质振动分析"
    value: 2
    reason: "默认值足够大多数催化吸附质振动分析"
related_parameters:
  - IBRION
~~~

~~~yaml
record_id: vasp-param-ngx-0456
record_type: parameter
scope: single_software
software:
  - VASP
topic: "NGX"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/NGX
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "NGX" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "NGX"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ngxf-0457
record_type: parameter
scope: single_software
software:
  - VASP
topic: "NGXF"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/NGXF
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "NGXF" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "NGXF"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ngy-0458
record_type: parameter
scope: single_software
software:
  - VASP
topic: "NGY"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/NGY
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "NGY" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "NGY"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ngyf-0459
record_type: parameter
scope: single_software
software:
  - VASP
topic: "NGYF"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/NGYF
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "NGYF" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "NGYF"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ngyromag-0460
record_type: parameter
scope: single_software
software:
  - VASP
topic: "NGYROMAG"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/NGYROMAG
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "NGYROMAG" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "NGYROMAG"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ngz-0461
record_type: parameter
scope: single_software
software:
  - VASP
topic: "NGZ"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/NGZ
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "NGZ" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "NGZ"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ngzf-0462
record_type: parameter
scope: single_software
software:
  - VASP
topic: "NGZF"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/NGZF
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "NGZF" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "NGZF"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-nhc-nchains-0463
record_type: parameter
scope: single_software
software:
  - VASP
topic: "NHC NCHAINS"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/NHC_NCHAINS
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "NHC NCHAINS" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "NHC NCHAINS"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-nhc-nrespa-0464
record_type: parameter
scope: single_software
software:
  - VASP
topic: "NHC NRESPA"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/NHC_NRESPA
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "NHC NRESPA" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "NHC NRESPA"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-nhc-ns-0465
record_type: parameter
scope: single_software
software:
  - VASP
topic: "NHC NS"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/NHC_NS
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "NHC NS" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "NHC NS"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-nics-0466
record_type: parameter
scope: single_software
software:
  - VASP
topic: "NICS"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/NICS
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "NICS" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "NICS"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-nkred-0467
record_type: parameter
scope: single_software
software:
  - VASP
topic: "NKRED"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/NKRED
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "NKRED" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "NKRED"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-nkredx-0468
record_type: parameter
scope: single_software
software:
  - VASP
topic: "NKREDX"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/NKREDX
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "NKREDX" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "NKREDX"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-nkredy-0469
record_type: parameter
scope: single_software
software:
  - VASP
topic: "NKREDY"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/NKREDY
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "NKREDY" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "NKREDY"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-nkredz-0470
record_type: parameter
scope: single_software
software:
  - VASP
topic: "NKREDZ"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/NKREDZ
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "NKREDZ" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "NKREDZ"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-nlspline-0471
record_type: parameter
scope: single_software
software:
  - VASP
topic: "NLSPLINE"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/NLSPLINE
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "NLSPLINE" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "NLSPLINE"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-nmaxfockae-and-lmaxfockae-0472
record_type: parameter
scope: single_software
software:
  - VASP
topic: "NMAXFOCKAE and LMAXFOCKAE"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/NMAXFOCKAE_and_LMAXFOCKAE
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "NMAXFOCKAE and LMAXFOCKAE" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "NMAXFOCKAE and LMAXFOCKAE"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-nmrcar-magres-0473
record_type: parameter
scope: single_software
software:
  - VASP
topic: "NMRCAR.magres"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/NMRCAR.magres
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "NMRCAR.magres" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "NMRCAR.magres"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-nomega-0474
record_type: parameter
scope: single_software
software:
  - VASP
topic: "NOMEGA"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/NOMEGA
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "NOMEGA" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "NOMEGA"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-nomega-dump-0475
record_type: parameter
scope: single_software
software:
  - VASP
topic: "NOMEGA DUMP"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/NOMEGA_DUMP
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "NOMEGA DUMP" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "NOMEGA DUMP"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-nomegapar-0476
record_type: parameter
scope: single_software
software:
  - VASP
topic: "NOMEGAPAR"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/NOMEGAPAR
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "NOMEGAPAR" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "NOMEGAPAR"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-nomegar-0477
record_type: parameter
scope: single_software
software:
  - VASP
topic: "NOMEGAR"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/NOMEGAR
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "NOMEGAR" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "NOMEGAR"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-npaco-0478
record_type: parameter
scope: single_software
software:
  - VASP
topic: "NPACO"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/NPACO
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "NPACO" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "NPACO"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-npar-0479
record_type: parameter
scope: single_software
software:
  - VASP
topic: "NPAR"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/NPAR
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "NPAR" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "NPAR"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-nppstr-0480
record_type: parameter
scope: single_software
software:
  - VASP
topic: "NPPSTR"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/NPPSTR
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "NPPSTR" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "NPPSTR"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-nrmm-0481
record_type: parameter
scope: single_software
software:
  - VASP
topic: "NRMM"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/NRMM
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "NRMM" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "NRMM"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-nsim-0482
record_type: parameter
scope: single_software
software:
  - VASP
topic: "NSIM"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/NSIM
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "NSIM" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "NSIM"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-nstorb-0483
record_type: parameter
scope: single_software
software:
  - VASP
topic: "NSTORB"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/NSTORB
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "NSTORB" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "NSTORB"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-nsubsys-0484
record_type: parameter
scope: single_software
software:
  - VASP
topic: "NSUBSYS"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/NSUBSYS
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "NSUBSYS" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "NSUBSYS"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-nsw-0485
record_type: parameter
scope: single_software
software:
  - VASP
topic: "NSW"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/NSW
version_or_doc_date: VASP Wiki; checked 2026-05-24
claim: "NSW 设定最大离子步数。几何优化: 50-200; AIMD: 5000+; NEB: 取决于插点数+收敛。"
evidence_level: should
confidence: official
related_wiki: []
related_records: [vasp-param-ibrion-0154, vasp-param-potim-0529, vasp-md-param-nsw-0002]
note: "NSW×POTIM=名义模拟时长(MD)/优化上限。NEB中 NSW=100-200 通常足够。"
last_checked: 2026-05-24
parameter_name: "NSW"
file_or_context: INCAR
definition: "最大离子步数。"
default_behavior: "NSW=1"
common_use:
  - {when: "几何优化 (slab)", value: 100, priority: should}
  - {when: "NEB (每图)", value: 100, priority: should}
  - {when: "AIMD (5 ps)", value: 5000, priority: should}
risk_if_misused:
  - "NSW 太小 → 优化/MD 未完成即停止"
parameter_relations:
  - {example_status: needs_verification, target: POTIM, relation: mutually_constrained, desc: "NSW×POTIM=名义持续时间"}
domain_guidance:
  - {example_status: needs_verification, rule: "Slab 几何优化→NSW=100; NEB→NSW=100-200"}
related_parameters: [POTIM, IBRION]
~~~

~~~yaml
record_id: vasp-param-ntarget-states-0486
record_type: parameter
scope: single_software
software:
  - VASP
topic: "NTARGET STATES"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/NTARGET_STATES
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "NTARGET STATES" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "NTARGET STATES"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ntaupar-0487
record_type: parameter
scope: single_software
software:
  - VASP
topic: "NTAUPAR"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/NTAUPAR
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "NTAUPAR" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "NTAUPAR"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ntemper-0488
record_type: parameter
scope: single_software
software:
  - VASP
topic: "NTEMPER"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/NTEMPER
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "NTEMPER" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "NTEMPER"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-nucind-0489
record_type: parameter
scope: single_software
software:
  - VASP
topic: "NUCIND"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/NUCIND
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "NUCIND" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "NUCIND"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-num-wann-0490
record_type: parameter
scope: single_software
software:
  - VASP
topic: "NUM WANN"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/NUM_WANN
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "NUM WANN" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "NUM WANN"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-nupdown-0491
record_type: parameter
scope: single_software
software:
  - VASP
topic: "NUPDOWN"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/NUPDOWN
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "NUPDOWN" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "NUPDOWN"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-nwrite-0492
record_type: parameter
scope: single_software
software:
  - VASP
topic: "NWRITE"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/NWRITE
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "NWRITE" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "NWRITE"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-oddonly-0493
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ODDONLY"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ODDONLY
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ODDONLY" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ODDONLY"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-oddonlygw-0494
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ODDONLYGW"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ODDONLYGW
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ODDONLYGW" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ODDONLYGW"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ofield-a-0495
record_type: parameter
scope: single_software
software:
  - VASP
topic: "OFIELD A"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/OFIELD_A
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "OFIELD A" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "OFIELD A"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ofield-kappa-0496
record_type: parameter
scope: single_software
software:
  - VASP
topic: "OFIELD KAPPA"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/OFIELD_KAPPA
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "OFIELD KAPPA" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "OFIELD KAPPA"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ofield-q6-far-0497
record_type: parameter
scope: single_software
software:
  - VASP
topic: "OFIELD Q6 FAR"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/OFIELD_Q6_FAR
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "OFIELD Q6 FAR" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "OFIELD Q6 FAR"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ofield-q6-near-0498
record_type: parameter
scope: single_software
software:
  - VASP
topic: "OFIELD Q6 NEAR"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/OFIELD_Q6_NEAR
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "OFIELD Q6 NEAR" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "OFIELD Q6 NEAR"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-omegamax-0499
record_type: parameter
scope: single_software
software:
  - VASP
topic: "OMEGAMAX"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/OMEGAMAX
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "OMEGAMAX" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "OMEGAMAX"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-omegamin-0500
record_type: parameter
scope: single_software
software:
  - VASP
topic: "OMEGAMIN"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/OMEGAMIN
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "OMEGAMIN" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "OMEGAMIN"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-omegatl-0501
record_type: parameter
scope: single_software
software:
  - VASP
topic: "OMEGATL"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/OMEGATL
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "OMEGATL" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "OMEGATL"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-param1-0502
record_type: parameter
scope: single_software
software:
  - VASP
topic: "PARAM1"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/PARAM1
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "PARAM1" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "PARAM1"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-param2-0503
record_type: parameter
scope: single_software
software:
  - VASP
topic: "PARAM2"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/PARAM2
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "PARAM2" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "PARAM2"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-pflat-0504
record_type: parameter
scope: single_software
software:
  - VASP
topic: "PFLAT"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/PFLAT
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "PFLAT" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "PFLAT"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-phon-born-charges-0505
record_type: parameter
scope: single_software
software:
  - VASP
topic: "PHON BORN CHARGES"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/PHON_BORN_CHARGES
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "PHON BORN CHARGES" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "PHON BORN CHARGES"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-phon-dielectric-0506
record_type: parameter
scope: single_software
software:
  - VASP
topic: "PHON DIELECTRIC"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/PHON_DIELECTRIC
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "PHON DIELECTRIC" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "PHON DIELECTRIC"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-phon-dos-0507
record_type: parameter
scope: single_software
software:
  - VASP
topic: "PHON DOS"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/PHON_DOS
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "PHON DOS" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "PHON DOS"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-phon-g-cutoff-0508
record_type: parameter
scope: single_software
software:
  - VASP
topic: "PHON G CUTOFF"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/PHON_G_CUTOFF
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "PHON G CUTOFF" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "PHON G CUTOFF"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-phon-lbose-0509
record_type: parameter
scope: single_software
software:
  - VASP
topic: "PHON LBOSE"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/PHON_LBOSE
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "PHON LBOSE" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "PHON LBOSE"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-phon-lmc-0510
record_type: parameter
scope: single_software
software:
  - VASP
topic: "PHON LMC"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/PHON_LMC
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "PHON LMC" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "PHON LMC"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-phon-nedos-0511
record_type: parameter
scope: single_software
software:
  - VASP
topic: "PHON NEDOS"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/PHON_NEDOS
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "PHON NEDOS" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "PHON NEDOS"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-phon-nstruct-0512
record_type: parameter
scope: single_software
software:
  - VASP
topic: "PHON NSTRUCT"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/PHON_NSTRUCT
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "PHON NSTRUCT" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "PHON NSTRUCT"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-phon-nwrite-0513
record_type: parameter
scope: single_software
software:
  - VASP
topic: "PHON NWRITE"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/PHON_NWRITE
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "PHON NWRITE" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "PHON NWRITE"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-phon-sigma-0514
record_type: parameter
scope: single_software
software:
  - VASP
topic: "PHON SIGMA"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/PHON_SIGMA
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "PHON SIGMA" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "PHON SIGMA"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-phon-tlist-0515
record_type: parameter
scope: single_software
software:
  - VASP
topic: "PHON TLIST"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/PHON_TLIST
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "PHON TLIST" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "PHON TLIST"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-plevel-0516
record_type: parameter
scope: single_software
software:
  - VASP
topic: "PLEVEL"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/PLEVEL
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "PLEVEL" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "PLEVEL"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-plugins-force-and-stress-0517
record_type: parameter
scope: single_software
software:
  - VASP
topic: "PLUGINS/FORCE AND STRESS"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/PLUGINS%2FFORCE_AND_STRESS
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "PLUGINS/FORCE AND STRESS" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "PLUGINS/FORCE AND STRESS"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-plugins-local-potential-0518
record_type: parameter
scope: single_software
software:
  - VASP
topic: "PLUGINS/LOCAL POTENTIAL"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/PLUGINS%2FLOCAL_POTENTIAL
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "PLUGINS/LOCAL POTENTIAL" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "PLUGINS/LOCAL POTENTIAL"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-plugins-machine-learning-0519
record_type: parameter
scope: single_software
software:
  - VASP
topic: "PLUGINS/MACHINE LEARNING"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/PLUGINS%2FMACHINE_LEARNING
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "PLUGINS/MACHINE LEARNING" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "PLUGINS/MACHINE LEARNING"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-plugins-ml-mode-0520
record_type: parameter
scope: single_software
software:
  - VASP
topic: "PLUGINS/ML MODE"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/PLUGINS%2FML_MODE
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "PLUGINS/ML MODE" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "PLUGINS/ML MODE"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-plugins-ml-outblock-0521
record_type: parameter
scope: single_software
software:
  - VASP
topic: "PLUGINS/ML OUTBLOCK"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/PLUGINS%2FML_OUTBLOCK
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "PLUGINS/ML OUTBLOCK" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "PLUGINS/ML OUTBLOCK"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-plugins-ml-output-mode-0522
record_type: parameter
scope: single_software
software:
  - VASP
topic: "PLUGINS/ML OUTPUT MODE"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/PLUGINS%2FML_OUTPUT_MODE
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "PLUGINS/ML OUTPUT MODE" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "PLUGINS/ML OUTPUT MODE"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-plugins-neighbor-cutoff-0523
record_type: parameter
scope: single_software
software:
  - VASP
topic: "PLUGINS/NEIGHBOR CUTOFF"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/PLUGINS%2FNEIGHBOR_CUTOFF
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "PLUGINS/NEIGHBOR CUTOFF" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "PLUGINS/NEIGHBOR CUTOFF"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-plugins-occupancies-0524
record_type: parameter
scope: single_software
software:
  - VASP
topic: "PLUGINS/OCCUPANCIES"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/PLUGINS%2FOCCUPANCIES
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "PLUGINS/OCCUPANCIES" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "PLUGINS/OCCUPANCIES"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-plugins-structure-0525
record_type: parameter
scope: single_software
software:
  - VASP
topic: "PLUGINS/STRUCTURE"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/PLUGINS%2FSTRUCTURE
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "PLUGINS/STRUCTURE" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "PLUGINS/STRUCTURE"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-pmass-0526
record_type: parameter
scope: single_software
software:
  - VASP
topic: "PMASS"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/PMASS
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "PMASS" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "PMASS"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-pomass-0527
record_type: parameter
scope: single_software
software:
  - VASP
topic: "POMASS"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/POMASS
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "POMASS" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "POMASS"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-posnics-0528
record_type: parameter
scope: single_software
software:
  - VASP
topic: "POSNICS"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/POSNICS
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "POSNICS" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "POSNICS"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-potim-0529
record_type: parameter
scope: single_software
software:
  - VASP
topic: "POTIM"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/POTIM
version_or_doc_date: VASP Wiki; checked 2026-05-24
claim: "POTIM 控制离子步步长: MD=时间步(fs); 几何优化=初始步长; 振动频率=位移步长(Å)。"
evidence_level: should
confidence: official
related_wiki: []
related_records: [vasp-param-ibrion-0154, vasp-param-nsw-0485, vasp-md-param-potim-0003]
note: "几何优化默认 POTIM=0.5。NEB 中 POTIM 控制每图离子松弛步长。MD 中 POTIM 是时间步。"
last_checked: 2026-05-24
parameter_name: "POTIM"
file_or_context: INCAR
definition: "离子步步长: MD=fs; Relax=初始步长(自动调整); 频率=位移 Å。"
default_behavior: "POTIM=0.5 (IBRION=1/2)"
common_use:
  - {when: "几何优化", value: 0.5, priority: ok}
  - {when: "AIMD (含 H)", value: 0.5-1.0, priority: should}
  - {when: "振动频率位移", value: 0.015, priority: should}
risk_if_misused:
  - "MD 中 POTIM 过大 → 离子爆炸"
  - "频率中 POTIM 过大/过小 → 非简谐区/Hessian 噪声"
parameter_relations:
  - {example_status: needs_verification, target: NSW, relation: mutually_constrained, desc: "NSW×POTIM=名义时长"}
  - {example_status: needs_verification, target: IBRION, relation: prerequisite, desc: "IBRION 决定 POTIM 的物理含义"}
domain_guidance:
  - {example_status: needs_verification, rule: "几何优化→POTIM=0.5; AIMD(含H)→0.5-1.0; 频率→0.015"}
related_parameters: [NSW, IBRION]
~~~

~~~yaml
record_id: vasp-param-prec-0530
record_type: parameter
scope: single_software
software:
  - VASP
topic: "PREC"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/PREC
version_or_doc_date: VASP Wiki; checked 2026-05-24
claim: "PREC 是精度预设参数，批量控制 ENCUT/LREAL/ADDGRID 等参数的默认值。"
evidence_level: should
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/vasp_scf_accuracy_chain.md
related_records:
  - vasp-param-encut-0116
  - vasp-param-addgrid-0001
  - vasp-param-lreal-0296
  - rel-vasp-scf-precision-chain-0001
note: "PREC 是便捷预设但不够透明。强烈推荐用 PREC=Normal + 手动逐个设其他参数。"
last_checked: 2026-05-24
parameter_name: "PREC"
file_or_context: INCAR
definition: "精度预设级别 (Normal/Accurate/High)，自动调整多个精度相关参数的默认值。"
default_behavior: |
  PREC=Normal  → ADDGRID=.FALSE., LREAL=.TRUE., ENCUT=max(ENMAX)
  PREC=Accurate → ADDGRID=.TRUE.,  LREAL=.TRUE., ENCUT=max(ENMAX×1.3)
  PREC=High     → ADDGRID=.TRUE.,  LREAL=.FALSE., ENCUT=max(ENMAX×1.3)
common_use:
  - {when: "需精确控制每个参数", value: Normal, priority: should}
  - {when: "快速计算不想手动调参", value: Accurate, priority: ok}
risk_if_misused:
  - "PREC=Accurate 自动覆盖手动 ENCUT → 你的 ENCUT 值可能被忽略"
  - "PREC=High + 大体系 → LREAL=.FALSE. 导致极慢"
parameter_relations:
  - target: ENCUT
    example_status: needs_verification
    relation: overrides
    desc: "PREC≠Normal 自动覆盖手动 ENCUT"
  - target: ADDGRID
    example_status: needs_verification
    relation: overrides
    desc: "PREC≥Accurate 自动开启 ADDGRID"
  - target: LREAL
    example_status: needs_verification
    relation: overrides
    desc: "PREC=High 强制 LREAL=.FALSE."
domain_guidance:
  - rule: "需要精确控制 ENCUT → PREC=Normal"
    example_status: needs_verification
    applies_to: {tasks: [aimd]}
    value: Normal
    reason: "手动 ENCUT+ADDGRID+LASPH 更透明"
related_parameters:
  - ENCUT
  - ADDGRID
  - LREAL
~~~

~~~yaml
record_id: vasp-param-precfock-0531
record_type: parameter
scope: single_software
software:
  - VASP
topic: "PRECFOCK"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/PRECFOCK
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "PRECFOCK" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "PRECFOCK"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-profiling-0532
record_type: parameter
scope: single_software
software:
  - VASP
topic: "Profiling"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/Profiling
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "Profiling" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "Profiling"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-proutine-0533
record_type: parameter
scope: single_software
software:
  - VASP
topic: "PROUTINE"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/PROUTINE
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "PROUTINE" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "PROUTINE"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-pstress-0534
record_type: parameter
scope: single_software
software:
  - VASP
topic: "PSTRESS"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/PSTRESS
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "PSTRESS" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "PSTRESS"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-psubsys-0535
record_type: parameter
scope: single_software
software:
  - VASP
topic: "PSUBSYS"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/PSUBSYS
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "PSUBSYS" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "PSUBSYS"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-pthreshold-0536
record_type: parameter
scope: single_software
software:
  - VASP
topic: "PTHRESHOLD"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/PTHRESHOLD
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "PTHRESHOLD" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "PTHRESHOLD"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-qmaxfockae-0537
record_type: parameter
scope: single_software
software:
  - VASP
topic: "QMAXFOCKAE"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/QMAXFOCKAE
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "QMAXFOCKAE" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "QMAXFOCKAE"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-qspiral-0538
record_type: parameter
scope: single_software
software:
  - VASP
topic: "QSPIRAL"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/QSPIRAL
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "QSPIRAL" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "QSPIRAL"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-quad-efg-0539
record_type: parameter
scope: single_software
software:
  - VASP
topic: "QUAD EFG"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/QUAD_EFG
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "QUAD EFG" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "QUAD EFG"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-random-generator-0540
record_type: parameter
scope: single_software
software:
  - VASP
topic: "RANDOM GENERATOR"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/RANDOM_GENERATOR
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "RANDOM GENERATOR" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "RANDOM GENERATOR"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-random-seed-0541
record_type: parameter
scope: single_software
software:
  - VASP
topic: "RANDOM SEED"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/RANDOM_SEED
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "RANDOM SEED" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "RANDOM SEED"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-ropt-0542
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ROPT"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ROPT
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ROPT" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ROPT"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-rsmbj-0543
record_type: parameter
scope: single_software
software:
  - VASP
topic: "RSMBJ"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/RSMBJ
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "RSMBJ" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "RSMBJ"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-rwigs-0544
record_type: parameter
scope: single_software
software:
  - VASP
topic: "RWIGS"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/RWIGS
version_or_doc_date: VASP Wiki; checked 2026-05-24
claim: "RWIGS 设定每个原子种类的 Wigner-Seitz 半径 (Å)。仅在 LORBIT<10 的旧投影方法中用于 PDOS; LORBIT≥10 使用 PAW 投影不依赖 RWIGS。Bader charge 分析需要。"
evidence_level: check
confidence: official
related_wiki: []
related_records: [vasp-param-lorbit-0286]
note: "LORBIT≥10 (PAW projection) 不需要 RWIGS; LORBIT<10 旧方法才需要。Bader 分析需专门的 Bader 程序处理 CHGCAR。"
last_checked: 2026-05-24
parameter_name: "RWIGS"
file_or_context: INCAR
definition: "每个原子种类的 Wigner-Seitz 半径 (Å)，按 POSCAR 原子种类排列。"
default_behavior: "来自 POTCAR 的原子半径"
common_use:
  - {when: "Bader charge 分析", value: "POTCAR 默认值", priority: ok}
  - {when: "LORBIT<10 PDOS 投影", value: "POTCAR 默认值", priority: ok}
  - {when: "LORBIT≥10 PDOS 投影", value: "不需要 (PAW projection)", priority: ok}
risk_if_misused:
  - "LORBIT≥10 时 RWIGS 被 PAW 投影忽略——设置与否不影响 PDOS"
  - "RWIGS 过小 → Bader 积分球体积不足 → 电荷不准; 过大 → 原子球重叠"
related_parameters: [LORBIT]
~~~

~~~yaml
record_id: vasp-param-saxis-0545
record_type: parameter
scope: single_software
software:
  - VASP
topic: "SAXIS"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/SAXIS
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "SAXIS" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "SAXIS"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-scalee-0546
record_type: parameter
scope: single_software
software:
  - VASP
topic: "SCALEE"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/SCALEE
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "SCALEE" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "SCALEE"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-scissor-0547
record_type: parameter
scope: single_software
software:
  - VASP
topic: "SCISSOR"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/SCISSOR
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "SCISSOR" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "SCISSOR"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-scsrad-0548
record_type: parameter
scope: single_software
software:
  - VASP
topic: "SCSRAD"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/SCSRAD
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "SCSRAD" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "SCSRAD"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-sdftd3-damping-0549
record_type: parameter
scope: single_software
software:
  - VASP
topic: "SDFTD3 DAMPING"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/SDFTD3_DAMPING
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "SDFTD3 DAMPING" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "SDFTD3 DAMPING"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-sdftd3-xc-0550
record_type: parameter
scope: single_software
software:
  - VASP
topic: "SDFTD3 XC"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/SDFTD3_XC
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "SDFTD3 XC" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "SDFTD3 XC"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-shakemaxiter-0551
record_type: parameter
scope: single_software
software:
  - VASP
topic: "SHAKEMAXITER"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/SHAKEMAXITER
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "SHAKEMAXITER" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "SHAKEMAXITER"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-shaketol-0552
record_type: parameter
scope: single_software
software:
  - VASP
topic: "SHAKETOL"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/SHAKETOL
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "SHAKETOL" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "SHAKETOL"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-shaketolsoft-0553
record_type: parameter
scope: single_software
software:
  - VASP
topic: "SHAKETOLSOFT"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/SHAKETOLSOFT
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "SHAKETOLSOFT" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "SHAKETOLSOFT"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-sigma-0554
record_type: parameter
scope: single_software
software:
  - VASP
topic: "SIGMA"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/SIGMA
version_or_doc_date: VASP Wiki; checked 2026-05-24
claim: "SIGMA 设定 ISMEAR≥0 时的展宽宽度 (eV)。宽度越大 SCF 越易收敛但总能量含更多 entropy。"
evidence_level: should
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/vasp_scf_accuracy_chain.md
related_records:
  - vasp-param-ismear-0181
note: "金属体系: SIGMA=0.1 eV 是常用平衡值。绝缘体: SIGMA 可设更小 (0.05) 或直接用 tetrahedron method。"
last_checked: 2026-05-24
parameter_name: "SIGMA"
file_or_context: INCAR
definition: "展宽宽度 (eV)。控制 ISMEAR=0/1/2 时 Fermi 面附近电子的部分占据范围。"
default_behavior: "SIGMA=0.2 (VASP 默认)"
common_use:
  - {when: "金属 slab (Pt/Ni/Cu) + 力敏感", value: 0.1, priority: should}
  - {when: "快速初筛 + 仅能量", value: 0.2 (默认), priority: ok}
  - {when: "绝缘体 + Gaussian", value: 0.05, priority: should}
risk_if_misused:
  - "SIGMA 过大 (>0.2) → entropy term 大 → 总能量不准 → 吸附能/自由能图系统偏差"
  - "SIGMA 过小 (<0.05) + 金属 → SCF 不收敛 → 更小的 SIGMA 需要更密的 k 点"
parameter_relations:
  - target: ISMEAR
    example_status: needs_verification
    relation: prerequisite
    desc: "SIGMA 只在 ISMEAR≥0 时生效"
  - target: k 点密度
    example_status: needs_verification
    relation: mutually_constrained
    desc: "SIGMA↓ → 需要更高的 k 点密度以消除 entropy error"
domain_guidance:
  - rule: "Pt slab + AIMD/几何优化 → SIGMA=0.1"
    example_status: needs_verification
    applies_to: {metals: [Pt, Ni, Co, Cu], tasks: [aimd, geometry_opt, neb]}
    value: 0.1
    reason: "足够小控制 entropy error < 1 meV/atom; 足够大保证金属 SCF 收敛"
related_parameters:
  - ISMEAR
  - KPOINTS
~~~

~~~yaml
record_id: vasp-param-smass-0555
record_type: parameter
scope: single_software
software:
  - VASP
topic: "SMASS"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/SMASS
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "SMASS" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "SMASS"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-smbj-0556
record_type: parameter
scope: single_software
software:
  - VASP
topic: "SMBJ"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/SMBJ
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "SMBJ" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "SMBJ"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-smearings-0557
record_type: parameter
scope: single_software
software:
  - VASP
topic: "SMEARINGS"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/SMEARINGS
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "SMEARINGS" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "SMEARINGS"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-spring-0558
record_type: parameter
scope: single_software
software:
  - VASP
topic: "SPRING"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/SPRING
version_or_doc_date: VASP Wiki; checked 2026-05-24
claim: "SPRING 控制 NEB 计算中相邻插点之间的虚拟弹簧常数，维持路径均匀分布。"
evidence_level: should
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/vasp_neb_chain.md
related_records:
  - vasp-param-images-0165
  - rel-vasp-neb-chain-0002
note: "负值常用 (-5.0 eV/Å²)。绝对值太小 → 路径漂移; 太大 → 切向力被干扰。"
last_checked: 2026-05-24
parameter_name: "SPRING"
file_or_context: INCAR
definition: "NEB 虚拟弹簧常数 (eV/Å²)。负值表示能量加权弹簧力。"
default_behavior: "-5.0 eV/Å² (VASP 默认)"
common_use:
  - {when: "一般 NEB/CI-NEB", value: "-5.0", priority: should}
  - {when: "路径不平滑 (插点聚类)", value: "-3.0 → -8.0", priority: ok}
risk_if_misused:
  - "绝对值太小 → 插点向两端'堆积'，TS 附近分辨率降低"
  - "绝对值太大 → 弹簧力干扰切向力 → TS 位置不准"
parameter_relations:
  - target: IMAGES
    example_status: needs_verification
    relation: mutually_constrained
domain_guidance:
  - rule: "催化 NEB → SPRING=-5.0 起点"
    example_status: needs_verification
    value: -5.0
related_parameters:
  - IMAGES
~~~

~~~yaml
record_id: vasp-param-spring-k-0559
record_type: parameter
scope: single_software
software:
  - VASP
topic: "SPRING K"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/SPRING_K
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "SPRING K" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "SPRING K"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-spring-r0-0560
record_type: parameter
scope: single_software
software:
  - VASP
topic: "SPRING R0"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/SPRING_R0
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "SPRING R0" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "SPRING R0"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-spring-v0-0561
record_type: parameter
scope: single_software
software:
  - VASP
topic: "SPRING V0"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/SPRING_V0
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "SPRING V0" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "SPRING V0"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-step-max-0562
record_type: parameter
scope: single_software
software:
  - VASP
topic: "STEP MAX"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/STEP_MAX
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "STEP MAX" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "STEP MAX"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-step-size-0563
record_type: parameter
scope: single_software
software:
  - VASP
topic: "STEP SIZE"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/STEP_SIZE
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "STEP SIZE" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "STEP SIZE"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-stop-on-0564
record_type: parameter
scope: single_software
software:
  - VASP
topic: "STOP ON"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/STOP_ON
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "STOP ON" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "STOP ON"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-symprec-0565
record_type: parameter
scope: single_software
software:
  - VASP
topic: "SYMPREC"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/SYMPREC
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "SYMPREC" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "SYMPREC"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-system-0566
record_type: parameter
scope: single_software
software:
  - VASP
topic: "SYSTEM"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/SYSTEM
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "SYSTEM" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "SYSTEM"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-tebeg-0567
record_type: parameter
scope: single_software
software:
  - VASP
topic: "TEBEG"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/TEBEG
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "TEBEG" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "TEBEG"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-teend-0568
record_type: parameter
scope: single_software
software:
  - VASP
topic: "TEEND"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/TEEND
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "TEEND" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "TEEND"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-tilambda-0569
record_type: parameter
scope: single_software
software:
  - VASP
topic: "TILAMBDA"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/TILAMBDA
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "TILAMBDA" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "TILAMBDA"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-time-0570
record_type: parameter
scope: single_software
software:
  - VASP
topic: "TIME"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/TIME
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "TIME" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "TIME"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-transport-nedos-0571
record_type: parameter
scope: single_software
software:
  - VASP
topic: "TRANSPORT NEDOS"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/TRANSPORT_NEDOS
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "TRANSPORT NEDOS" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "TRANSPORT NEDOS"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-transport-relaxation-time-0572
record_type: parameter
scope: single_software
software:
  - VASP
topic: "TRANSPORT RELAXATION TIME"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/TRANSPORT_RELAXATION_TIME
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "TRANSPORT RELAXATION TIME" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "TRANSPORT RELAXATION TIME"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-tsubsys-0573
record_type: parameter
scope: single_software
software:
  - VASP
topic: "TSUBSYS"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/TSUBSYS
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "TSUBSYS" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "TSUBSYS"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-vacpotflat-0574
record_type: parameter
scope: single_software
software:
  - VASP
topic: "VACPOTFLAT"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/VACPOTFLAT
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "VACPOTFLAT" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "VACPOTFLAT"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-value-max-0575
record_type: parameter
scope: single_software
software:
  - VASP
topic: "VALUE MAX"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/VALUE_MAX
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "VALUE MAX" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "VALUE MAX"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-value-min-0576
record_type: parameter
scope: single_software
software:
  - VASP
topic: "VALUE MIN"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/VALUE_MIN
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "VALUE MIN" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "VALUE MIN"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-vca-0577
record_type: parameter
scope: single_software
software:
  - VASP
topic: "VCA"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/VCA
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "VCA" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "VCA"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-vcaimages-0578
record_type: parameter
scope: single_software
software:
  - VASP
topic: "VCAIMAGES"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/VCAIMAGES
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "VCAIMAGES" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "VCAIMAGES"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-vcutoff-0579
record_type: parameter
scope: single_software
software:
  - VASP
topic: "VCUTOFF"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/VCUTOFF
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "VCUTOFF" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "VCUTOFF"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-vdw-a1-0580
record_type: parameter
scope: single_software
software:
  - VASP
topic: "VDW A1"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/VDW_A1
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "VDW A1" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "VDW A1"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-vdw-a2-0581
record_type: parameter
scope: single_software
software:
  - VASP
topic: "VDW A2"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/VDW_A2
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "VDW A2" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "VDW A2"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-vdw-alpha-0582
record_type: parameter
scope: single_software
software:
  - VASP
topic: "VDW ALPHA"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/VDW_ALPHA
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "VDW ALPHA" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "VDW ALPHA"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-vdw-beta-0583
record_type: parameter
scope: single_software
software:
  - VASP
topic: "VDW BETA"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/VDW_BETA
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "VDW BETA" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "VDW BETA"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-vdw-c6-0584
record_type: parameter
scope: single_software
software:
  - VASP
topic: "VDW C6"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/VDW_C6
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "VDW C6" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "VDW C6"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-vdw-c6au-0585
record_type: parameter
scope: single_software
software:
  - VASP
topic: "VDW C6AU"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/VDW_C6AU
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "VDW C6AU" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "VDW C6AU"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-vdw-cnradius-0586
record_type: parameter
scope: single_software
software:
  - VASP
topic: "VDW CNRADIUS"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/VDW_CNRADIUS
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "VDW CNRADIUS" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "VDW CNRADIUS"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-vdw-d-0587
record_type: parameter
scope: single_software
software:
  - VASP
topic: "VDW D"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/VDW_D
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "VDW D" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "VDW D"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-vdw-r0-0588
record_type: parameter
scope: single_software
software:
  - VASP
topic: "VDW R0"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/VDW_R0
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "VDW R0" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "VDW R0"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-vdw-r0au-0589
record_type: parameter
scope: single_software
software:
  - VASP
topic: "VDW R0AU"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/VDW_R0AU
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "VDW R0AU" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "VDW R0AU"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-vdw-radius-0590
record_type: parameter
scope: single_software
software:
  - VASP
topic: "VDW RADIUS"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/VDW_RADIUS
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "VDW RADIUS" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "VDW RADIUS"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-vdw-s6-0591
record_type: parameter
scope: single_software
software:
  - VASP
topic: "VDW S6"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/VDW_S6
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "VDW S6" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "VDW S6"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-vdw-s8-0592
record_type: parameter
scope: single_software
software:
  - VASP
topic: "VDW S8"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/VDW_S8
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "VDW S8" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "VDW S8"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-vdw-s9-0593
record_type: parameter
scope: single_software
software:
  - VASP
topic: "VDW S9"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/VDW_S9
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "VDW S9" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "VDW S9"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-vdw-sr-0594
record_type: parameter
scope: single_software
software:
  - VASP
topic: "VDW SR"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/VDW_SR
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "VDW SR" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "VDW SR"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-vdw-sr8-0595
record_type: parameter
scope: single_software
software:
  - VASP
topic: "VDW SR8"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/VDW_SR8
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "VDW SR8" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "VDW SR8"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-velocity-0596
record_type: parameter
scope: single_software
software:
  - VASP
topic: "VELOCITY"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/VELOCITY
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "VELOCITY" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "VELOCITY"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-voskown-0597
record_type: parameter
scope: single_software
software:
  - VASP
topic: "VOSKOWN"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/VOSKOWN
version_or_doc_date: VASP Wiki; checked 2026-05-24
claim: "VOSKOWN 控制 Vosko-Wilk-Nusair 插值 (GGA 的关联能)。VOSKOWN=1 通常推荐。"
evidence_level: check
confidence: official
related_wiki: []
related_records: [vasp-param-gga-0140]
note: "VOSKOWN=1 是 VASP 默认，VOSKOWN=0 用 PW91 关联插值。一般不需改。"
last_checked: 2026-05-24
parameter_name: "VOSKOWN"
file_or_context: INCAR
definition: "VWN 插值选择: 0=PW91; 1=VWN。"
default_behavior: "VOSKOWN=1"
common_use:
  - {when: "标准 PBE 计算", value: 1, priority: ok}
related_parameters: [GGA]
~~~

~~~yaml
record_id: vasp-param-wannier90-win-0598
record_type: parameter
scope: single_software
software:
  - VASP
topic: "WANNIER90 WIN"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/WANNIER90_WIN
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "WANNIER90 WIN" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "WANNIER90 WIN"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-wc-0599
record_type: parameter
scope: single_software
software:
  - VASP
topic: "WC"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/WC
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "WC" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "WC"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-weimin-0600
record_type: parameter
scope: single_software
software:
  - VASP
topic: "WEIMIN"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/WEIMIN
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "WEIMIN" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "WEIMIN"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-wrt-density-0601
record_type: parameter
scope: single_software
software:
  - VASP
topic: "WRT DENSITY"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/WRT_DENSITY
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "WRT DENSITY" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "WRT DENSITY"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-wrt-nmrcur-0602
record_type: parameter
scope: single_software
software:
  - VASP
topic: "WRT NMRCUR"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/WRT_NMRCUR
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "WRT NMRCUR" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "WRT NMRCUR"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-wrt-potential-0603
record_type: parameter
scope: single_software
software:
  - VASP
topic: "WRT POTENTIAL"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/WRT_POTENTIAL
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "WRT POTENTIAL" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "WRT POTENTIAL"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-xc-0604
record_type: parameter
scope: single_software
software:
  - VASP
topic: "XC"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/XC
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "XC" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "XC"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-xc-c-0605
record_type: parameter
scope: single_software
software:
  - VASP
topic: "XC C"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/XC_C
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "XC C" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "XC C"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-xcm-pn-0606
record_type: parameter
scope: single_software
software:
  - VASP
topic: "XCm Pn"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/XCm_Pn
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "XCm Pn" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "XCm Pn"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

~~~yaml
record_id: vasp-param-zab-vdw-0607
record_type: parameter
scope: single_software
software:
  - VASP
topic: "ZAB VDW"
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ZAB_VDW
version_or_doc_date: VASP Wiki category snapshot 2026-05-21
claim: Official VASP Wiki lists "ZAB VDW" as an INCAR tag page.
evidence_level: check
confidence: official
related_wiki: []
related_records: []
note: Index-level import. This only confirms that the tag belongs to the official INCAR tag category; definition/default/risk_if_misused still require page-level extraction before use.
last_checked: 2026-05-21
parameter_name: "ZAB VDW"
file_or_context: INCAR
definition: Index-level import; official definition not extracted yet
default_behavior: unknown
common_use: []
risk_if_misused:
  - Index-level import; specific risks require page-level official documentation extraction
related_parameters: []
~~~

# ── VASPsol Extension Tags (not in VASP Wiki Category:INCAR_tag) ──

~~~yaml
record_id: vasp-param-lsol-0400
record_type: parameter
scope: single_software
software:
  - VASP
topic: LSOL
source_type: official_repo
source_ref: "https://github.com/henniggroup/VASPsol"
version_or_doc_date: "VASPsol 1.0; checked 2026-05-24"
claim: "VASPsol 隐式溶剂开关。.TRUE. 激活 Poisson-Boltzmann 连续介质溶剂模型。VASPsol patch 扩展标签。"
evidence_level: should
confidence: local_unverified
related_wiki:
  - computer_kb/wiki/concepts/vasp_vaspsol_implicit_solvent.md
related_records:
  - vasp-param-eb-k-0401
  - vasp-param-tau-k-0402
note: "VASPsol 扩展标签。需 VASP 编译时链接 VASPsol。continuum 模型不能取代显式水层 AIMD。"
last_checked: 2026-05-24
parameter_name: "LSOL"
file_or_context: INCAR (VASPsol)
definition: "Implicit solvation model开关。.TRUE. 时在真空区域填充 continuum 溶剂 (Poisson-Boltzmann)。"
default_behavior: ".FALSE. (vacuum)"
common_use:
  - implicit water solvent for electrochemical interfaces
risk_if_misused:
  - "SCF 在 LSOL=.TRUE. 下更难收敛 → ALGO=All + AMIX↓"
domain_guidance:
  - example_status: needs_verification
    rule: "电化学界面 screening → LSOL=.TRUE. + EB_K=78.4 (water)"
    applies_to: {systems: [metal_water_interface]}
    value: ".TRUE."
    reason: "隐式溶剂给出 continuum solvation 修正; explicit water AIMD 做最终验证"
parameter_relations:
  - example_status: needs_verification
    target: EB_K
    relation: requires_companion
    desc: "LSOL 需配合 EB_K (介电常数) 定义溶剂类型"
related_parameters: [EB_K, TAU_K, NC_K]
~~~

~~~yaml
record_id: vasp-param-eb-k-0401
record_type: parameter
scope: single_software
software:
  - VASP
topic: EB_K
source_type: official_repo
source_ref: "https://github.com/henniggroup/VASPsol"
version_or_doc_date: "VASPsol 1.0; checked 2026-05-24"
claim: "Bulk 溶剂相对介电常数 ε_b。水=78.4 (298 K); 乙腈=37.5; 甲醇=32.7。VASPsol 扩展标签。"
evidence_level: should
confidence: local_unverified
related_wiki:
  - computer_kb/wiki/concepts/vasp_vaspsol_implicit_solvent.md
related_records:
  - vasp-param-lsol-0400
note: "VASPsol 扩展标签。ε_b 直接决定溶剂极化响应强度——错误值导致溶剂化能系统偏差。"
last_checked: 2026-05-24
parameter_name: "EB_K"
file_or_context: INCAR (VASPsol)
definition: "Bulk solvent relative dielectric constant. Controls the polarization response of the continuum."
default_behavior: "78.4 (water, VASPsol default)"
common_use:
  - implicit water solvent (78.4)
  - non-aqueous solvent screening
risk_if_misused:
  - "错误的 ε_b → 溶剂化能系统偏差 → 后续 CHE 自由能图偏离"
domain_guidance:
  - example_status: needs_verification
    rule: "aqueous electrochemistry → EB_K=78.4"
    applies_to: {systems: [metal_water_interface]}
    value: 78.4
    reason: "水的 bulk 介电常数 at 298 K"
related_parameters: [LSOL, TAU_K]
~~~

~~~yaml
record_id: vasp-param-tau-k-0402
record_type: parameter
scope: single_software
software:
  - VASP
topic: TAU_K
source_type: official_repo
source_ref: "https://github.com/henniggroup/VASPsol"
version_or_doc_date: "VASPsol 1.0; checked 2026-05-24"
claim: "VASPsol 表面张力参数 τ (cavitation energy)。0=关闭。VASPsol 扩展标签。"
evidence_level: check
confidence: local_unverified
related_wiki:
  - computer_kb/wiki/concepts/vasp_vaspsol_implicit_solvent.md
note: "VASPsol 扩展标签。τ 引入 cavitation 能量——对带电界面可能有影响但数值不确定。一般保持 0。"
last_checked: 2026-05-24
parameter_name: "TAU_K"
file_or_context: INCAR (VASPsol)
definition: "Surface tension parameter for cavitation energy in the solvent model."
default_behavior: "0.0 (off)"
common_use: []
risk_if_misused:
  - "错误 TAU_K 引入虚假 cavitation 能量"
related_parameters: [LSOL]
~~~

~~~yaml
record_id: vasp-param-nc-k-0403
record_type: parameter
scope: single_software
software:
  - VASP
topic: NC_K
source_type: official_repo
source_ref: "https://github.com/henniggroup/VASPsol"
version_or_doc_date: "VASPsol 1.0; checked 2026-05-24"
claim: "VASPsol 补偿电荷密度截止参数。0=自动。非零值对应电解质离子浓度。VASPsol 扩展标签。"
evidence_level: check
confidence: local_unverified
related_wiki:
  - computer_kb/wiki/concepts/vasp_vaspsol_implicit_solvent.md
related_records:
  - vasp-param-lsol-0400
  - vasp-param-lambda-d-k-0404
note: "VASPsol 扩展标签。NC_K 配合 LAMBDA_D_K 定义电解质静电屏蔽。纯水设 0。"
last_checked: 2026-05-24
parameter_name: "NC_K"
file_or_context: INCAR (VASPsol)
definition: "Compensating charge density cutoff for ionic strength in Poisson-Boltzmann model."
default_behavior: "0.0 (auto / pure solvent)"
common_use:
  - electrolyte screening (set non-zero with LAMBDA_D_K)
risk_if_misused:
  - "NC_K 与 LAMBDA_D_K 不匹配 → 屏蔽效应不物理"
related_parameters: [LSOL, LAMBDA_D_K]
~~~

~~~yaml
record_id: vasp-param-lambda-d-k-0404
record_type: parameter
scope: single_software
software:
  - VASP
topic: LAMBDA_D_K
source_type: official_repo
source_ref: "https://github.com/henniggroup/VASPsol"
version_or_doc_date: "VASPsol 1.0; checked 2026-05-24"
claim: "VASPsol Debye 屏蔽长度 (Å)。λ_D = 3.04/√(c[M]) for 1:1 electrolyte at 298 K。VASPsol 扩展标签。"
evidence_level: check
confidence: local_unverified
related_wiki:
  - computer_kb/wiki/concepts/vasp_vaspsol_implicit_solvent.md
related_records:
  - vasp-param-lsol-0400
  - vasp-param-nc-k-0403
note: "VASPsol 扩展标签。1M→3.04 Å; 0.1M→9.6 Å; 纯水设 10 或 0。"
last_checked: 2026-05-24
parameter_name: "LAMBDA_D_K"
file_or_context: INCAR (VASPsol)
definition: "Debye screening length for electrolyte ions (Å)."
default_behavior: "3.04 Å (1M 1:1 electrolyte)"
common_use:
  - electrolyte electrostatic screening
  - EDL modeling in continuum approximation
risk_if_misused:
  - "λ_D 与实验浓度不匹配 → 屏蔽过度/不足 → 界面电场失真"
domain_guidance:
  - example_status: needs_verification
    rule: "1M 1:1 electrolyte → λ_D=3.04 Å; 0.1M → 9.6; pure water → 10 or 0"
    applies_to: {systems: [metal_electrolyte_interface]}
    value: "3.04 (1M); 9.6 (0.1M); 0/10 (pure water)"
    reason: "λ_D = 3.04/√(c[M]) for 1:1 electrolyte at 298 K"
related_parameters: [LSOL, NC_K]
~~~

## Obsidian Links

- [[vasp_aimd_md_parameters]]

