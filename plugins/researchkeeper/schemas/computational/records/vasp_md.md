# VASP MD/AIMD records

> Seed2 deep records for VASP molecular-dynamics and AIMD-related INCAR tags.
> Sources are the official VASP Wiki URLs recorded in each entry.
> These records are more detailed than the Seed1 full INCAR-tag index, but they are still software-layer facts, not paper-specific computational settings.

## seed2-vasp-md-aimd-2026-05-21

~~~yaml
record_id: vasp-md-param-ibrion-0001
record_type: parameter
scope: single_software
software:
  - VASP
topic: IBRION
source_type: official_doc
source_ref: https://www.vasp.at/wiki/IBRION
version_or_doc_date: VASP Wiki snapshot 2026-05-21
claim: IBRION determines how the crystal structure changes during the calculation; IBRION=0 is the molecular-dynamics mode used together with MD-related tags.
evidence_level: check
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/vasp_aimd_md_parameters.md
related_records:
  - vasp-md-param-mdalgo-0006
  - vasp-md-param-nsw-0002
  - vasp-md-param-potim-0003
note: Use this as the first routing tag for AIMD/MD; other values of IBRION route to relaxation, phonon, or related ionic-update algorithms.
last_checked: 2026-05-21
parameter_name: IBRION
file_or_context: INCAR
definition: Selects the ionic update algorithm; IBRION=0 selects molecular dynamics.
default_behavior: unknown
common_use:
  - AIMD
  - molecular dynamics
risk_if_misused:
  - Setting a non-MD IBRION value changes the run from MD to another ionic-update workflow.
parameter_relations:
  - {example_status: needs_verification, target: MDALGO, relation: prerequisite, desc: "IBRION=0 是 MDALGO 生效的前提"}
domain_guidance:
  - {example_status: needs_verification, rule: "AIMD→IBRION=0; 几何优化→2; NEB→1/3", applies_to: {tasks: [aimd, geometry_opt, neb]}, value: 0, reason: "IBRION=0 激活MD模式"}
related_parameters:
  - MDALGO
  - NSW
  - POTIM
~~~

~~~yaml
record_id: vasp-md-param-nsw-0002
record_type: parameter
scope: single_software
software:
  - VASP
topic: NSW
source_type: official_doc
source_ref: https://www.vasp.at/wiki/NSW
version_or_doc_date: VASP Wiki snapshot 2026-05-21
claim: NSW sets the maximum number of ionic steps; in MD it is the number of MD steps requested.
evidence_level: check
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/vasp_aimd_md_parameters.md
related_records:
  - vasp-md-param-ibrion-0001
  - vasp-md-param-potim-0003
note: For trajectory time accounting, combine NSW with POTIM; e.g. total nominal trajectory length is NSW times POTIM.
last_checked: 2026-05-21
parameter_name: NSW
file_or_context: INCAR
definition: Maximum number of ionic steps.
default_behavior: 0
common_use:
  - trajectory length control
  - relaxation step count
risk_if_misused:
  - NSW=0 produces no ionic/MD trajectory even when other MD tags are present.
  - Confusing NSW with physical time can hide that the trajectory is too short for sampling.
parameter_relations:
  - {example_status: needs_verification, target: POTIM, relation: mutually_constrained, desc: "NSW*POTIM=名义总时长"}
domain_guidance:
  - {example_status: needs_verification, rule: "AIMD采样 → NSW≥5000 (5ps@1fs)", applies_to: {tasks: [aimd_sampling]}, value: 5000, reason: "最小有意义 RDF 需 ~2 ps; 采样需 5-10 ps"}
related_parameters:
  - POTIM
  - IBRION
~~~

~~~yaml
record_id: vasp-md-param-potim-0003
record_type: parameter
scope: single_software
software:
  - VASP
topic: POTIM
source_type: official_doc
source_ref: https://www.vasp.at/wiki/POTIM
version_or_doc_date: VASP Wiki snapshot 2026-05-21
claim: POTIM sets the time step in molecular dynamics and the step width in ionic relaxations.
evidence_level: check
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/vasp_aimd_md_parameters.md
related_records:
  - vasp-md-param-nsw-0002
  - vasp-md-param-ibrion-0001
note: In VASP MD, POTIM is the time step used to convert the number of MD steps into trajectory time.
last_checked: 2026-05-21
parameter_name: POTIM
file_or_context: INCAR
definition: MD time step or ionic-relaxation step width.
default_behavior: unknown
common_use:
  - AIMD time step
  - ionic relaxation step width
risk_if_misused:
  - Too large a time step can destabilize MD trajectories or make thermostat behavior unphysical.
  - Too small a time step increases cost and may produce unnecessarily short sampled time.
parameter_relations:
  - {example_status: needs_verification, target: NSW, relation: mutually_constrained, desc: "POTIM*NSW=名义总时长"}
  - {example_status: needs_verification, target: TEBEG, relation: coupled_accuracy, desc: "高温+T含H→需更小POTIM"}
domain_guidance:
  - {example_status: needs_verification, rule: "含H→POTIM=0.5-1.0fs (保守0.5; 正常1.0)", applies_to: {systems: [metal_water_interface]}, value: "0.5-1.0 fs", reason: "轻元素H的OH高频模→≤1.0fs; 爆炸排查时降至0.5fs; 无H可用1-2fs"}
related_parameters:
  - NSW
  - MDALGO
~~~

~~~yaml
record_id: vasp-md-param-tebeg-0004
record_type: parameter
scope: single_software
software:
  - VASP
topic: TEBEG
source_type: official_doc
source_ref: https://www.vasp.at/wiki/TEBEG
version_or_doc_date: VASP Wiki snapshot 2026-05-21
claim: TEBEG sets the starting temperature in K for an ab-initio molecular dynamics run.
evidence_level: check
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/vasp_aimd_md_parameters.md
related_records:
  - vasp-md-param-teend-0005
  - vasp-md-param-mdalgo-0006
note: MDALGO documentation warns that TEBEG below 0.1 may be interpreted by parts of the code as structure optimization rather than MD.
last_checked: 2026-05-21
parameter_name: TEBEG
file_or_context: INCAR
definition: Starting temperature for AIMD and related routines.
default_behavior: 0
common_use:
  - AIMD initial target temperature
  - thermalization
risk_if_misused:
  - TEBEG close to zero can trigger structure-optimization assumptions in some MD contexts.
  - Not recording TEBEG/TEEND makes the thermal protocol hard to reproduce.
related_parameters:
  - TEEND
  - MDALGO
  - RANDOM_SEED
~~~

~~~yaml
record_id: vasp-md-param-teend-0005
record_type: parameter
scope: single_software
software:
  - VASP
topic: TEEND
source_type: official_doc
source_ref: https://www.vasp.at/wiki/TEEND
version_or_doc_date: VASP Wiki snapshot 2026-05-21
claim: TEEND sets the final temperature in K for an ab-initio molecular-dynamics run.
evidence_level: check
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/vasp_aimd_md_parameters.md
related_records:
  - vasp-md-param-tebeg-0004
note: The official default is TEEND=TEBEG, which means no intentional temperature ramp unless TEEND differs from TEBEG.
last_checked: 2026-05-21
parameter_name: TEEND
file_or_context: INCAR
definition: Final temperature for AIMD.
default_behavior: TEBEG
common_use:
  - constant-temperature AIMD when equal to TEBEG
  - temperature ramp when different from TEBEG
risk_if_misused:
  - An unintended TEEND different from TEBEG changes the temperature protocol.
parameter_relations:
  - {example_status: needs_verification, target: TEBEG, relation: mutually_constrained, desc: "TEBEG+thermostat 共同决定采样温度"}
  - {example_status: needs_verification, target: POTIM, relation: mutually_constrained, desc: "高温+T轻元素→需更小timestep"}
domain_guidance:
  - {example_status: needs_verification, rule: "室温水界面→TEBEG=330K", applies_to: {systems: [metal_water_interface]}, value: 330, reason: "~330K模拟室温液态水; ±20K按目标调整"}
related_parameters:
  - TEBEG
  - MDALGO
~~~

~~~yaml
record_id: vasp-md-param-mdalgo-0006
record_type: parameter
scope: single_software
software:
  - VASP
topic: MDALGO
source_type: official_doc
source_ref: https://www.vasp.at/wiki/MDALGO
version_or_doc_date: VASP Wiki snapshot 2026-05-21
claim: MDALGO specifies the thermostat and lattice dynamics for molecular-dynamics calculations when IBRION=0.
evidence_level: check
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/vasp_aimd_md_parameters.md
related_records:
  - vasp-md-param-ibrion-0001
  - vasp-md-param-andersen-prob-0007
  - vasp-md-param-smass-0008
  - vasp-md-param-langevin-gamma-0009
  - vasp-md-param-nhc-nchains-0012
  - vasp-md-param-csvr-period-0016
note: "Official MDALGO page maps thermostat choices: Andersen, Nose-Hoover, Langevin, Nose-Hoover chain, CSVR, multiple Andersen thermostats, and deprecated VASP 5.x options."
last_checked: 2026-05-21
parameter_name: MDALGO
file_or_context: INCAR
definition: Selects thermostat and lattice-dynamics algorithm for MD.
default_behavior: 0
common_use:
  - NVE
  - NVT
  - NpT
  - NpH
  - constrained or biased MD
risk_if_misused:
  - Thermostat-specific required tags differ; selecting MDALGO without its companion tags can produce the wrong ensemble.
  - Deprecated MDALGO values may complicate trajectory post-processing.
related_parameters:
  - IBRION
  - ANDERSEN_PROB
  - SMASS
  - LANGEVIN_GAMMA
  - LANGEVIN_GAMMA_L
  - PMASS
  - NHC_NCHAINS
  - NHC_PERIOD
  - CSVR_PERIOD
~~~

~~~yaml
record_id: vasp-md-param-andersen-prob-0007
record_type: parameter
scope: single_software
software:
  - VASP
topic: ANDERSEN_PROB
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ANDERSEN_PROB
version_or_doc_date: VASP Wiki snapshot 2026-05-21
claim: ANDERSEN_PROB sets the collision probability for the Andersen thermostat.
evidence_level: check
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/vasp_aimd_md_parameters.md
related_records:
  - vasp-md-param-mdalgo-0006
note: Official MDALGO guidance states that MDALGO=1 requires an appropriate ANDERSEN_PROB; ANDERSEN_PROB=0.0 can be used for NVE after thermalization.
last_checked: 2026-05-21
parameter_name: ANDERSEN_PROB
file_or_context: INCAR
definition: Collision probability for the Andersen thermostat.
default_behavior: 0
common_use:
  - Andersen thermostat
  - NVE after thermalization when set to 0.0
risk_if_misused:
  - Nonzero collision probability changes dynamics by stochastic velocity reassignment.
related_parameters:
  - MDALGO
  - TEBEG
~~~

~~~yaml
record_id: vasp-md-param-smass-0008
record_type: parameter
scope: single_software
software:
  - VASP
topic: SMASS
source_type: official_doc
source_ref: https://www.vasp.at/wiki/SMASS
version_or_doc_date: VASP Wiki snapshot 2026-05-21
claim: SMASS controls the velocities during an ab-initio molecular-dynamics run and is used by the older Nose-Hoover thermostat implementation.
evidence_level: check
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/vasp_aimd_md_parameters.md
related_records:
  - vasp-md-param-mdalgo-0006
note: MDALGO page states MDALGO=2 requires an appropriate SMASS; MDALGO=0 is deprecated and SMASS=-3 samples NVE in that older route.
last_checked: 2026-05-21
parameter_name: SMASS
file_or_context: INCAR
definition: Controls velocities in AIMD, including thermostat mass/frequency behavior for Nose-Hoover-style MD.
default_behavior: unknown
common_use:
  - Nose-Hoover thermostat
  - legacy NVE/NVT controls
risk_if_misused:
  - Inappropriate thermostat mass can lead to poor temperature coupling or nonphysical oscillations.
  - Deprecated MDALGO=0 plus SMASS settings should be documented carefully for post-processing.
parameter_relations:
  - {example_status: needs_verification, target: MDALGO, relation: prerequisite, desc: "MDALGO=2 时 SMASS 必须指定; SMASS=0→NVE"}
domain_guidance:
  - {example_status: needs_verification, rule: "100-500 原子体系 → SMASS~0.5-3.0", applies_to: {systems: [metal_water_interface]}, value: "~1.0-2.0", reason: "SMASS 取 POTIM 的 1-3 倍是经验起手值"}
related_parameters:
  - MDALGO
  - TEBEG
  - TEEND
~~~

~~~yaml
record_id: vasp-md-param-langevin-gamma-0009
record_type: parameter
scope: single_software
software:
  - VASP
topic: LANGEVIN_GAMMA
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LANGEVIN_GAMMA
version_or_doc_date: VASP Wiki snapshot 2026-05-21
claim: LANGEVIN_GAMMA specifies friction coefficients in ps^-1 for atomic degrees of freedom when using a Langevin thermostat.
evidence_level: check
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/vasp_aimd_md_parameters.md
related_records:
  - vasp-md-param-mdalgo-0006
  - vasp-md-param-langevin-gamma-l-0010
note: Official MDALGO guidance requires friction coefficients for all POSCAR species to enable the Langevin thermostat.
last_checked: 2026-05-21
parameter_name: LANGEVIN_GAMMA
file_or_context: INCAR
definition: Atomic friction coefficients for Langevin dynamics.
default_behavior: NTYP x 0
common_use:
  - Langevin NVT
  - Langevin NpT with ISIF=3
risk_if_misused:
  - Zero or missing coefficients can fail to apply the intended thermostat to species.
  - Species ordering must match POSCAR atom types.
parameter_relations:
  - {example_status: needs_verification, target: MDALGO, relation: prerequisite, desc: "MDALGO=3 时 LANGEVIN_GAMMA 必须指定"}
  - {example_status: needs_verification, target: LANGEVIN_GAMMA_L, relation: coupled_accuracy, desc: "NpT (ISIF=3) 需额外指定 LANGEVIN_GAMMA_L"}
domain_guidance:
  - {example_status: needs_verification, rule: "Pt/水界面 → {H:10.0, O:5.0, Pt:1.0} ps-1", applies_to: {systems: [metal_water_interface], metals: [Pt, Ni, Co]}, value: {H:10.0, O:5.0, metal:1.0}, reason: "轻元素H需强摩擦耦合 (~10 ps-1); 重金属弱耦合 (~1 ps-1)"}
related_parameters:
  - MDALGO
  - LANGEVIN_GAMMA_L
  - PMASS
  - ISIF
~~~

~~~yaml
record_id: vasp-md-param-langevin-gamma-l-0010
record_type: parameter
scope: single_software
software:
  - VASP
topic: LANGEVIN_GAMMA_L
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LANGEVIN_GAMMA_L
version_or_doc_date: VASP Wiki snapshot 2026-05-21
claim: LANGEVIN_GAMMA_L specifies the friction coefficient in ps^-1 for lattice degrees of freedom in Parrinello-Rahman dynamics.
evidence_level: check
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/vasp_aimd_md_parameters.md
related_records:
  - vasp-md-param-langevin-gamma-0009
  - vasp-md-param-pmass-0011
note: Used with MDALGO=3 and ISIF=3 for Langevin NpT lattice dynamics.
last_checked: 2026-05-21
parameter_name: LANGEVIN_GAMMA_L
file_or_context: INCAR
definition: Lattice friction coefficient for Langevin Parrinello-Rahman dynamics.
default_behavior: 0
common_use:
  - Langevin NpT
  - lattice dynamics
risk_if_misused:
  - Omitting lattice friction while enabling lattice dynamics can produce an unintended ensemble/control setup.
parameter_relations:
  - {example_status: needs_verification, target: LANGEVIN_GAMMA, relation: coupled_accuracy, desc: 'NpT需LANGEVIN_GAMMA+LANGEVIN_GAMMA_L同时指定'}
domain_guidance:
  - {example_status: needs_verification, rule: 'Langevin NpT→LANGEVIN_GAMMA_L~1-5 ps-1', value: '~3.0', reason: 'cell自由度的摩擦系数一般小于原子自由度'}
related_parameters:
  - MDALGO
  - LANGEVIN_GAMMA
  - PMASS
  - ISIF
~~~

~~~yaml
record_id: vasp-md-param-pmass-0011
record_type: parameter
scope: single_software
software:
  - VASP
topic: PMASS
source_type: official_doc
source_ref: https://www.vasp.at/wiki/PMASS
version_or_doc_date: VASP Wiki snapshot 2026-05-21
claim: PMASS assigns a fictitious mass in amu to lattice degrees of freedom in Parrinello-Rahman dynamics.
evidence_level: check
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/vasp_aimd_md_parameters.md
related_records:
  - vasp-md-param-mdalgo-0006
  - vasp-md-param-langevin-gamma-l-0010
note: Official MDALGO guidance lists PMASS as required for Langevin NpT with ISIF=3.
last_checked: 2026-05-21
parameter_name: PMASS
file_or_context: INCAR
definition: Fictitious mass for lattice degrees of freedom.
default_behavior: 1000
common_use:
  - Parrinello-Rahman lattice dynamics
  - Langevin NpT
risk_if_misused:
  - Poorly chosen lattice mass can distort volume/cell fluctuations or make pressure control unstable.
related_parameters:
  - MDALGO
  - ISIF
  - LANGEVIN_GAMMA_L
  - PSTRESS
~~~

~~~yaml
record_id: vasp-md-param-nhc-nchains-0012
record_type: parameter
scope: single_software
software:
  - VASP
topic: NHC_NCHAINS
source_type: official_doc
source_ref: https://www.vasp.at/wiki/NHC_NCHAINS
version_or_doc_date: VASP Wiki snapshot 2026-05-21
claim: NHC_NCHAINS sets the length of the Nose-Hoover chain.
evidence_level: check
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/vasp_aimd_md_parameters.md
related_records:
  - vasp-md-param-mdalgo-0006
  - vasp-md-param-nhc-period-0015
note: MDALGO=4 Nose-Hoover chain thermostat requires choosing NHC_NCHAINS and NHC_PERIOD.
last_checked: 2026-05-21
parameter_name: NHC_NCHAINS
file_or_context: INCAR
definition: Length of the Nose-Hoover thermostat chain.
default_behavior: 0
common_use:
  - Nose-Hoover chain NVT
risk_if_misused:
  - Leaving the chain length at a value incompatible with the intended thermostat can prevent the intended NHC control.
related_parameters:
  - MDALGO
  - NHC_PERIOD
  - NHC_NRESPA
  - NHC_NS
~~~

~~~yaml
record_id: vasp-md-param-nhc-nrespa-0013
record_type: parameter
scope: single_software
software:
  - VASP
topic: NHC_NRESPA
source_type: official_doc
source_ref: https://www.vasp.at/wiki/NHC_NRESPA
version_or_doc_date: VASP Wiki snapshot 2026-05-21
claim: NHC_NRESPA sets the number of subdivisions of the integration step used in propagation of Nose-Hoover chain thermostat variables.
evidence_level: check
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/vasp_aimd_md_parameters.md
related_records:
  - vasp-md-param-nhc-nchains-0012
note: This is an integration-control parameter for the Nose-Hoover chain thermostat.
last_checked: 2026-05-21
parameter_name: NHC_NRESPA
file_or_context: INCAR
definition: RESPA subdivisions for propagating thermostat variables.
default_behavior: 1
common_use:
  - Nose-Hoover chain thermostat integration
risk_if_misused:
  - Changing thermostat integration subdivisions can affect stability and should be reported for reproducibility.
related_parameters:
  - MDALGO
  - NHC_NCHAINS
  - NHC_NS
  - NHC_PERIOD
~~~

~~~yaml
record_id: vasp-md-param-nhc-ns-0014
record_type: parameter
scope: single_software
software:
  - VASP
topic: NHC_NS
source_type: official_doc
source_ref: https://www.vasp.at/wiki/NHC_NS
version_or_doc_date: VASP Wiki snapshot 2026-05-21
claim: NHC_NS sets the number of subdivisions of each RESPA step used in propagating Nose-Hoover chain thermostat variables.
evidence_level: check
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/vasp_aimd_md_parameters.md
related_records:
  - vasp-md-param-nhc-nchains-0012
note: This is a Nose-Hoover chain thermostat integration-control parameter.
last_checked: 2026-05-21
parameter_name: NHC_NS
file_or_context: INCAR
definition: Subdivisions of each RESPA step for NHC thermostat propagation.
default_behavior: unknown
common_use:
  - Nose-Hoover chain thermostat integration
risk_if_misused:
  - Undocumented changes alter thermostat integration details and reduce reproducibility.
related_parameters:
  - MDALGO
  - NHC_NCHAINS
  - NHC_NRESPA
  - NHC_PERIOD
~~~

~~~yaml
record_id: vasp-md-param-nhc-period-0015
record_type: parameter
scope: single_software
software:
  - VASP
topic: NHC_PERIOD
source_type: official_doc
source_ref: https://www.vasp.at/wiki/NHC_PERIOD
version_or_doc_date: VASP Wiki snapshot 2026-05-21
claim: NHC_PERIOD sets the time scale of the Nose-Hoover chain thermostat in terms of the number of MD steps.
evidence_level: check
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/vasp_aimd_md_parameters.md
related_records:
  - vasp-md-param-nhc-nchains-0012
note: MDALGO=4 requires an appropriate NHC_PERIOD.
last_checked: 2026-05-21
parameter_name: NHC_PERIOD
file_or_context: INCAR
definition: Nose-Hoover chain thermostat time scale in MD steps.
default_behavior: 40
common_use:
  - Nose-Hoover chain NVT
risk_if_misused:
  - Too aggressive or too weak thermostat period can affect temperature control and dynamics.
related_parameters:
  - MDALGO
  - NHC_NCHAINS
~~~

~~~yaml
record_id: vasp-md-param-csvr-period-0016
record_type: parameter
scope: single_software
software:
  - VASP
topic: CSVR_PERIOD
source_type: official_doc
source_ref: https://www.vasp.at/wiki/CSVR_PERIOD
version_or_doc_date: VASP Wiki snapshot 2026-05-21
claim: CSVR_PERIOD sets the time scale of the CSVR thermostat in terms of the number of MD steps.
evidence_level: check
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/vasp_aimd_md_parameters.md
related_records:
  - vasp-md-param-mdalgo-0006
note: Official MDALGO documentation states that MDALGO=5 uses CSVR and is available as of VASP 6.4.3.
last_checked: 2026-05-21
parameter_name: CSVR_PERIOD
file_or_context: INCAR
definition: CSVR thermostat time scale in MD steps.
default_behavior: 0
common_use:
  - CSVR NVT
risk_if_misused:
  - Using MDALGO=5 in versions before VASP 6.4.3 is not supported by the official documentation.
  - A zero/default period should be checked before relying on CSVR thermostat behavior.
related_parameters:
  - MDALGO
  - TEBEG
~~~

~~~yaml
record_id: vasp-md-param-isif-0017
record_type: parameter
scope: single_software
software:
  - VASP
topic: ISIF
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ISIF
version_or_doc_date: VASP Wiki snapshot 2026-05-21
claim: ISIF determines whether the stress tensor is calculated and which ionic/cell degrees of freedom are varied.
evidence_level: check
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/vasp_aimd_md_parameters.md
related_records:
  - vasp-md-param-mdalgo-0006
  - vasp-md-param-pmass-0011
note: MDALGO documentation states Langevin NVT should fix cell shape and volume with ISIF<=2, while Langevin NpT uses ISIF=3 with lattice friction and PMASS.
last_checked: 2026-05-21
parameter_name: ISIF
file_or_context: INCAR
definition: Controls stress calculation and ionic/cell degrees of freedom.
default_behavior: unknown
common_use:
  - fixed-cell NVT
  - variable-cell NpT
risk_if_misused:
  - Wrong ISIF changes the ensemble by allowing or preventing lattice dynamics.
  - MDALGO page notes fixed-volume variable-shape and fixed-shape variable-volume Langevin dynamics are not currently available for ISIF=4 or ISIF=7.
parameter_relations:
  - {example_status: needs_verification, target: MDALGO, relation: mutually_constrained, desc: "MDALGO=3+ISIF=3→Langevin NpT需额外参数(LANGEVIN_GAMMA_L+PMASS)"}
  - {example_status: needs_verification, target: LANGEVIN_GAMMA_L, relation: requires_companion, desc: "ISIF=3+NpT需要LANGEVIN_GAMMA_L"}
domain_guidance:
  - {example_status: needs_verification, rule: "AIMD NVT→ISIF≤2; NpT→ISIF=3", applies_to: {tasks: [aimd_sampling]}, value: 2, reason: "NVT固定cell; NpT需配LANGEVIN_GAMMA_L+PMASS"}
related_parameters:
  - MDALGO
  - LANGEVIN_GAMMA
  - LANGEVIN_GAMMA_L
  - PMASS
  - PSTRESS
~~~

~~~yaml
record_id: vasp-md-param-pstress-0018
record_type: parameter
scope: single_software
software:
  - VASP
topic: PSTRESS
source_type: official_doc
source_ref: https://www.vasp.at/wiki/PSTRESS
version_or_doc_date: VASP Wiki snapshot 2026-05-21
claim: PSTRESS sets external pressure in kB or adds corrections to the stress tensor.
evidence_level: check
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/vasp_aimd_md_parameters.md
related_records:
  - vasp-md-param-isif-0017
  - vasp-md-param-pmass-0011
note: MDALGO documentation lists PSTRESS as optional for Langevin NpT.
last_checked: 2026-05-21
parameter_name: PSTRESS
file_or_context: INCAR
definition: External pressure or stress-tensor correction.
default_behavior: 0
common_use:
  - NpT pressure target/correction
  - stress corrections
risk_if_misused:
  - Unintended nonzero pressure changes cell dynamics and pressure interpretation.
related_parameters:
  - ISIF
  - MDALGO
  - PMASS
~~~

~~~yaml
record_id: vasp-md-param-lattice-constraints-0019
record_type: parameter
scope: single_software
software:
  - VASP
topic: LATTICE_CONSTRAINTS
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LATTICE_CONSTRAINTS
version_or_doc_date: VASP Wiki snapshot 2026-05-21
claim: LATTICE_CONSTRAINTS sets three Boolean controls to selectively allow changes in lattice vectors.
evidence_level: check
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/vasp_aimd_md_parameters.md
related_records:
  - vasp-md-param-isif-0017
note: Use only when explicit lattice-vector constraints are part of the intended cell-dynamics protocol.
last_checked: 2026-05-21
parameter_name: LATTICE_CONSTRAINTS
file_or_context: INCAR
definition: Boolean controls for selective lattice-vector changes.
default_behavior: unknown
common_use:
  - constrained cell dynamics
  - anisotropic lattice constraints
risk_if_misused:
  - Hidden lattice constraints can make the sampled ensemble differ from the intended one.
related_parameters:
  - ISIF
  - MDALGO
~~~

~~~yaml
record_id: vasp-md-param-nsubsys-0020
record_type: parameter
scope: single_software
software:
  - VASP
topic: NSUBSYS
source_type: official_doc
source_ref: https://www.vasp.at/wiki/NSUBSYS
version_or_doc_date: VASP Wiki snapshot 2026-05-21
claim: NSUBSYS defines atomic subsystems in calculations with multiple Andersen thermostats.
evidence_level: check
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/vasp_aimd_md_parameters.md
related_records:
  - vasp-md-param-mdalgo-0006
  - vasp-md-param-tsubsys-0021
  - vasp-md-param-psubsys-0022
note: Official MDALGO documentation states that up to three user-defined atomic subsystems can be coupled with independent Andersen thermostats and requires NSUBSYS, TSUBSYS, and PSUBSYS.
last_checked: 2026-05-21
parameter_name: NSUBSYS
file_or_context: INCAR
definition: Defines atom counts/subsystems for multiple Andersen thermostats.
default_behavior: unknown
common_use:
  - multiple Andersen thermostats
  - subsystem thermal control
risk_if_misused:
  - POSCAR atom ordering must match subsystem definitions; otherwise thermostat assignment can target the wrong atoms.
related_parameters:
  - MDALGO
  - TSUBSYS
  - PSUBSYS
~~~

~~~yaml
record_id: vasp-md-param-tsubsys-0021
record_type: parameter
scope: single_software
software:
  - VASP
topic: TSUBSYS
source_type: official_doc
source_ref: https://www.vasp.at/wiki/TSUBSYS
version_or_doc_date: VASP Wiki snapshot 2026-05-21
claim: TSUBSYS sets temperatures for atomic subsystems in multiple Andersen thermostat calculations.
evidence_level: check
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/vasp_aimd_md_parameters.md
related_records:
  - vasp-md-param-nsubsys-0020
  - vasp-md-param-psubsys-0022
note: Requires consistent subsystem definition with NSUBSYS and collision probabilities with PSUBSYS.
last_checked: 2026-05-21
parameter_name: TSUBSYS
file_or_context: INCAR
definition: Subsystem temperatures for multiple Andersen thermostats.
default_behavior: unknown
common_use:
  - subsystem temperature control
risk_if_misused:
  - Wrong subsystem temperatures change heat-flow or thermalization assumptions.
related_parameters:
  - MDALGO
  - NSUBSYS
  - PSUBSYS
~~~

~~~yaml
record_id: vasp-md-param-psubsys-0022
record_type: parameter
scope: single_software
software:
  - VASP
topic: PSUBSYS
source_type: official_doc
source_ref: https://www.vasp.at/wiki/PSUBSYS
version_or_doc_date: VASP Wiki snapshot 2026-05-21
claim: PSUBSYS sets collision probabilities for atoms in each atomic subsystem in multiple Andersen thermostat calculations.
evidence_level: check
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/vasp_aimd_md_parameters.md
related_records:
  - vasp-md-param-nsubsys-0020
  - vasp-md-param-tsubsys-0021
note: This is the subsystem-level analogue of ANDERSEN_PROB for the multiple-Andersen-thermostat route.
last_checked: 2026-05-21
parameter_name: PSUBSYS
file_or_context: INCAR
definition: Collision probabilities for subsystem Andersen thermostats.
default_behavior: unknown
common_use:
  - multiple Andersen thermostats
risk_if_misused:
  - Inconsistent PSUBSYS values can overcouple or undercouple subsystems.
related_parameters:
  - MDALGO
  - NSUBSYS
  - TSUBSYS
  - ANDERSEN_PROB
~~~

~~~yaml
record_id: vasp-md-param-nblock-0023
record_type: parameter
scope: single_software
software:
  - VASP
topic: NBLOCK
source_type: official_doc
source_ref: https://www.vasp.at/wiki/NBLOCK
version_or_doc_date: VASP Wiki snapshot 2026-05-21
claim: After NBLOCK ionic steps, the pair-correlation function and DOS are calculated.
evidence_level: check
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/vasp_aimd_md_parameters.md
related_records:
  - vasp-md-param-kblock-0024
  - vasp-md-param-apaco-0025
  - vasp-md-param-npaco-0026
note: Output control for MD analysis files such as PCDAT/DOSCAR.
last_checked: 2026-05-21
parameter_name: NBLOCK
file_or_context: INCAR
definition: Interval in ionic steps for pair-correlation and DOS evaluation.
default_behavior: 1
common_use:
  - MD pair-correlation output
  - DOS output cadence
risk_if_misused:
  - Too frequent analysis output increases file size/cost; too sparse output reduces temporal resolution.
related_parameters:
  - KBLOCK
  - APACO
  - NPACO
~~~

~~~yaml
record_id: vasp-md-param-kblock-0024
record_type: parameter
scope: single_software
software:
  - VASP
topic: KBLOCK
source_type: official_doc
source_ref: https://www.vasp.at/wiki/KBLOCK
version_or_doc_date: VASP Wiki snapshot 2026-05-21
claim: After KBLOCK times NBLOCK ionic steps, the averaged pair-correlation function and DOS are written to PCDAT and DOSCAR.
evidence_level: check
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/vasp_aimd_md_parameters.md
related_records:
  - vasp-md-param-nblock-0023
note: This controls aggregation/output cadence rather than the MD integrator itself.
last_checked: 2026-05-21
parameter_name: KBLOCK
file_or_context: INCAR
definition: Multiplicative block interval for averaged PCDAT/DOSCAR output.
default_behavior: NSW
common_use:
  - averaged pair-correlation output
  - averaged DOS output
risk_if_misused:
  - Large KBLOCK can delay useful diagnostics until very late in the run.
related_parameters:
  - NBLOCK
  - NSW
~~~

~~~yaml
record_id: vasp-md-param-apaco-0025
record_type: parameter
scope: single_software
software:
  - VASP
topic: APACO
source_type: official_doc
source_ref: https://www.vasp.at/wiki/APACO
version_or_doc_date: VASP Wiki snapshot 2026-05-21
claim: APACO sets the maximum distance in Angstrom for evaluating the pair-correlation function.
evidence_level: check
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/vasp_aimd_md_parameters.md
related_records:
  - vasp-md-param-npaco-0026
  - vasp-md-param-nblock-0023
note: Pair-correlation analysis parameter for MD post-processing output.
last_checked: 2026-05-21
parameter_name: APACO
file_or_context: INCAR
definition: Maximum pair-correlation distance.
default_behavior: 10
common_use:
  - pair-correlation function output
  - PCDAT setup
risk_if_misused:
  - Too small a cutoff can miss relevant pair distances; too large can waste bins and obscure resolution.
related_parameters:
  - NPACO
  - NBLOCK
~~~

~~~yaml
record_id: vasp-md-param-npaco-0026
record_type: parameter
scope: single_software
software:
  - VASP
topic: NPACO
source_type: official_doc
source_ref: https://www.vasp.at/wiki/NPACO
version_or_doc_date: VASP Wiki snapshot 2026-05-21
claim: NPACO sets the number of slots in the pair-correlation function written to PCDAT.
evidence_level: check
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/vasp_aimd_md_parameters.md
related_records:
  - vasp-md-param-apaco-0025
note: Pair-correlation binning parameter.
last_checked: 2026-05-21
parameter_name: NPACO
file_or_context: INCAR
definition: Number of pair-correlation bins/slots.
default_behavior: 256
common_use:
  - pair-correlation function resolution
risk_if_misused:
  - Too few slots reduce pair-correlation resolution; too many can increase noise/file size.
related_parameters:
  - APACO
  - NBLOCK
~~~

~~~yaml
record_id: vasp-md-param-random-seed-0027
record_type: parameter
scope: single_software
software:
  - VASP
topic: RANDOM_SEED
source_type: official_doc
source_ref: https://www.vasp.at/wiki/RANDOM_SEED
version_or_doc_date: VASP Wiki snapshot 2026-05-21
claim: RANDOM_SEED specifies the seed of the random-number generator.
evidence_level: check
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/vasp_aimd_md_parameters.md
related_records:
  - vasp-md-param-tebeg-0004
  - vasp-md-param-mdalgo-0006
note: The official default is based on the system clock, so exact stochastic reproducibility requires explicit seed recording.
last_checked: 2026-05-21
parameter_name: RANDOM_SEED
file_or_context: INCAR
definition: Random-number generator seed.
default_behavior: based on the system clock
common_use:
  - stochastic thermostat reproducibility
  - random velocities
risk_if_misused:
  - Leaving the seed implicit can make stochastic MD runs non-reproducible.
domain_guidance:
  - {example_status: needs_verification, rule: "可复现 AIMD → 固定 RANDOM_SEED", applies_to: {tasks: [aimd_sampling]}, value: "12345", reason: "固定seed保证随机初速度可复现"}
related_parameters:
  - MDALGO
  - TEBEG
~~~

~~~yaml
record_id: vasp-md-param-velocity-0028
record_type: parameter
scope: single_software
software:
  - VASP
topic: VELOCITY
source_type: official_doc
source_ref: https://www.vasp.at/wiki/VELOCITY
version_or_doc_date: VASP Wiki snapshot 2026-05-21
claim: VELOCITY determines whether ionic velocities are written to the vaspout.h5 file during an MD run.
evidence_level: check
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/vasp_aimd_md_parameters.md
related_records:
  - vasp-md-param-ibrion-0001
note: This is output control; it does not by itself define the thermostat or ensemble.
last_checked: 2026-05-21
parameter_name: VELOCITY
file_or_context: INCAR
definition: Controls whether ionic velocities are written to vaspout.h5.
default_behavior: .false.
common_use:
  - MD velocity output
  - trajectory analysis
risk_if_misused:
  - Not writing velocities can block downstream kinetic/velocity-correlation analysis.
domain_guidance:
  - {example_status: needs_verification, rule: "AIMD→VELOCITY=.TRUE. (保存速度用于后处理)", applies_to: {tasks: [aimd_sampling]}, value: ".TRUE.", reason: "速度用于计算VAC/扩散系数"}
related_parameters:
  - IBRION
  - NSW
~~~

~~~yaml
record_id: vasp-md-param-pomass-0029
record_type: parameter
scope: single_software
software:
  - VASP
topic: POMASS
source_type: official_doc
source_ref: https://www.vasp.at/wiki/POMASS
version_or_doc_date: VASP Wiki snapshot 2026-05-21
claim: POMASS is an array of atomic masses in atomic units; by default values are read from POTCAR.
evidence_level: check
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/vasp_aimd_md_parameters.md
related_records:
  - vasp-md-param-potim-0003
note: Relevant to MD because atomic masses enter ionic dynamics; changes must be explicit and justified.
last_checked: 2026-05-21
parameter_name: POMASS
file_or_context: INCAR / POTCAR
definition: Atomic masses used for ionic dynamics.
default_behavior: values read from POTCAR
common_use:
  - isotope-mass changes
  - ionic dynamics
risk_if_misused:
  - Changing masses changes vibrational and dynamical timescales.
related_parameters:
  - POTIM
~~~

~~~yaml
record_id: vasp-md-param-iconst-0030
record_type: file_format
scope: single_software
software:
  - VASP
topic: ICONST
source_type: official_doc
source_ref: https://www.vasp.at/wiki/ICONST
version_or_doc_date: VASP Wiki snapshot 2026-05-21
claim: ICONST is the VASP input file used for constrained molecular dynamics and monitoring geometric parameters.
evidence_level: check
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/vasp_aimd_md_parameters.md
related_records:
  - vasp-md-param-mdalgo-0006
  - vasp-md-param-value-max-0037
  - vasp-md-param-value-min-0038
note: Recorded as file_format rather than INCAR parameter because ICONST is a separate input file.
last_checked: 2026-05-21
file_or_context: ICONST
definition: Constraint/collective-variable input file for constrained or monitored MD workflows.
default_behavior: absent unless provided
common_use:
  - constrained molecular dynamics
  - monitoring geometric parameters
risk_if_misused:
  - Inconsistent constraints can make the sampled dynamics differ from intended physical coordinates.
related_parameters:
  - MDALGO
  - VALUE_MAX
  - VALUE_MIN
~~~

~~~yaml
record_id: vasp-md-param-interactive-0031
record_type: parameter
scope: single_software
software:
  - VASP
topic: INTERACTIVE
source_type: official_doc
source_ref: https://www.vasp.at/wiki/INTERACTIVE
version_or_doc_date: VASP Wiki snapshot 2026-05-21
claim: INTERACTIVE selects the use of interactive mode.
evidence_level: check
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/vasp_aimd_md_parameters.md
related_records: []
note: Included because the official Molecular dynamics category lists it; use only when an interactive workflow is intended.
last_checked: 2026-05-21
parameter_name: INTERACTIVE
file_or_context: INCAR
definition: Enables interactive mode.
default_behavior: .FALSE.
common_use:
  - interactive VASP workflows
risk_if_misused:
  - Accidental interactive mode can be inappropriate for batch HPC jobs.
related_parameters: []
~~~

~~~yaml
record_id: vasp-md-param-iwavpr-0032
record_type: parameter
scope: single_software
software:
  - VASP
topic: IWAVPR
source_type: official_doc
source_ref: https://www.vasp.at/wiki/IWAVPR
version_or_doc_date: VASP Wiki snapshot 2026-05-21
claim: IWAVPR determines how orbitals and/or charge densities are predicted between ionic steps.
evidence_level: check
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/vasp_aimd_md_parameters.md
related_records:
  - vasp-md-param-ibrion-0001
note: Included because the official Molecular dynamics category lists it; it affects electronic extrapolation/prediction during ionic motion.
last_checked: 2026-05-21
parameter_name: IWAVPR
file_or_context: INCAR
definition: Controls wavefunction/charge prediction between ionic configurations.
default_behavior: unknown
common_use:
  - ionic-step wavefunction prediction
  - MD electronic convergence support
risk_if_misused:
  - Poor prediction choices can affect electronic convergence behavior during MD.
related_parameters:
  - IBRION
~~~

~~~yaml
record_id: vasp-md-param-lrpaforce-0033
record_type: parameter
scope: single_software
software:
  - VASP
topic: LRPAFORCE
source_type: official_doc
source_ref: https://www.vasp.at/wiki/LRPAFORCE
version_or_doc_date: VASP Wiki snapshot 2026-05-21
claim: LRPAFORCE=.TRUE. calculates forces in the random-phase approximation.
evidence_level: check
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/vasp_aimd_md_parameters.md
related_records: []
note: Included because the official Molecular dynamics category lists it; this is a specialized force-evaluation setting, not a generic AIMD default.
last_checked: 2026-05-21
parameter_name: LRPAFORCE
file_or_context: INCAR
definition: Enables RPA force calculations.
default_behavior: unknown
common_use:
  - RPA forces
risk_if_misused:
  - Treating specialized RPA-force settings as ordinary AIMD defaults can make workflows unnecessarily expensive or inappropriate.
related_parameters: []
~~~

~~~yaml
record_id: vasp-md-param-nfree-0034
record_type: parameter
scope: single_software
software:
  - VASP
topic: NFREE
source_type: official_doc
source_ref: https://www.vasp.at/wiki/NFREE
version_or_doc_date: VASP Wiki snapshot 2026-05-21
claim: Depending on IBRION, NFREE specifies either remembered ionic-convergence history steps or the number of ionic displacements in frozen-phonon calculations.
evidence_level: check
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/vasp_aimd_md_parameters.md
related_records:
  - vasp-md-param-ibrion-0001
note: Included because the official Molecular dynamics category lists it; its meaning depends on IBRION and should not be generalized.
last_checked: 2026-05-21
parameter_name: NFREE
file_or_context: INCAR
definition: IBRION-dependent history/displacement count.
default_behavior: unknown
common_use:
  - ionic convergence history
  - frozen phonons
risk_if_misused:
  - Applying an NFREE interpretation from one IBRION mode to another can be wrong.
related_parameters:
  - IBRION
~~~

~~~yaml
record_id: vasp-md-param-fmp-active-0035
record_type: parameter
scope: single_software
software:
  - VASP
topic: FMP_ACTIVE
source_type: official_doc
source_ref: https://www.vasp.at/wiki/FMP_ACTIVE
version_or_doc_date: VASP Wiki snapshot 2026-05-21
claim: FMP_ACTIVE selects which POSCAR atom types participate in swapping within the Müller-Plathe method.
evidence_level: check
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/vasp_aimd_md_parameters.md
related_records:
  - vasp-md-param-fmp-direction-0036
  - vasp-md-param-fmp-period-0039
note: Advanced MD sampling/transport parameter; not part of ordinary equilibrium AIMD unless Müller-Plathe heat-flux setup is intended.
last_checked: 2026-05-21
parameter_name: FMP_ACTIVE
file_or_context: INCAR
definition: Atom-type participation mask for Müller-Plathe swapping.
default_behavior: unknown
common_use:
  - Müller-Plathe method
  - thermal-gradient simulations
risk_if_misused:
  - Wrong atom-type selection changes which atoms carry imposed heat flux.
related_parameters:
  - FMP_DIRECTION
  - FMP_PERIOD
  - FMP_SNUMBER
  - FMP_SWAPNUM
~~~

~~~yaml
record_id: vasp-md-param-fmp-direction-0036
record_type: parameter
scope: single_software
software:
  - VASP
topic: FMP_DIRECTION
source_type: official_doc
source_ref: https://www.vasp.at/wiki/FMP_DIRECTION
version_or_doc_date: VASP Wiki snapshot 2026-05-21
claim: FMP_DIRECTION selects the lattice-vector direction along which the temperature gradient is created in the Müller-Plathe method.
evidence_level: check
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/vasp_aimd_md_parameters.md
related_records:
  - vasp-md-param-fmp-active-0035
note: Direction must match the intended heat-flow geometry.
last_checked: 2026-05-21
parameter_name: FMP_DIRECTION
file_or_context: INCAR
definition: Lattice-vector direction for Müller-Plathe temperature gradient.
default_behavior: unknown
common_use:
  - Müller-Plathe method
  - thermal transport
risk_if_misused:
  - Choosing the wrong direction imposes the thermal gradient along the wrong cell vector.
related_parameters:
  - FMP_ACTIVE
  - FMP_SNUMBER
~~~

~~~yaml
record_id: vasp-md-param-value-max-0037
record_type: parameter
scope: single_software
software:
  - VASP
topic: VALUE_MAX
source_type: official_doc
source_ref: https://www.vasp.at/wiki/VALUE_MAX
version_or_doc_date: VASP Wiki snapshot 2026-05-21
claim: VALUE_MAX sets upper limits for monitoring geometric parameters.
evidence_level: check
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/vasp_aimd_md_parameters.md
related_records:
  - vasp-md-param-iconst-0030
  - vasp-md-param-value-min-0038
note: Used with constrained/monitored MD workflows that rely on ICONST-defined geometric parameters.
last_checked: 2026-05-21
parameter_name: VALUE_MAX
file_or_context: INCAR
definition: Upper limits for monitored geometric parameters.
default_behavior: unknown
common_use:
  - constrained MD
  - geometry monitoring
risk_if_misused:
  - Incorrect bounds can trigger unintended monitoring or constraint behavior.
related_parameters:
  - VALUE_MIN
  - MDALGO
~~~

~~~yaml
record_id: vasp-md-param-value-min-0038
record_type: parameter
scope: single_software
software:
  - VASP
topic: VALUE_MIN
source_type: official_doc
source_ref: https://www.vasp.at/wiki/VALUE_MIN
version_or_doc_date: VASP Wiki snapshot 2026-05-21
claim: VALUE_MIN sets lower limits for monitoring geometric parameters.
evidence_level: check
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/vasp_aimd_md_parameters.md
related_records:
  - vasp-md-param-iconst-0030
  - vasp-md-param-value-max-0037
note: Used with constrained/monitored MD workflows that rely on ICONST-defined geometric parameters.
last_checked: 2026-05-21
parameter_name: VALUE_MIN
file_or_context: INCAR
definition: Lower limits for monitored geometric parameters.
default_behavior: unknown
common_use:
  - constrained MD
  - geometry monitoring
risk_if_misused:
  - Incorrect bounds can trigger unintended monitoring or constraint behavior.
related_parameters:
  - VALUE_MAX
  - MDALGO
~~~

~~~yaml
record_id: vasp-md-param-fmp-period-0039
record_type: parameter
scope: single_software
software:
  - VASP
topic: FMP_PERIOD
source_type: official_doc
source_ref: https://www.vasp.at/wiki/FMP_PERIOD
version_or_doc_date: VASP Wiki snapshot 2026-05-21
claim: FMP_PERIOD sets the number of time steps between two swapping events in the Müller-Plathe method.
evidence_level: check
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/vasp_aimd_md_parameters.md
related_records:
  - vasp-md-param-fmp-active-0035
note: Advanced heat-flux/transport MD parameter.
last_checked: 2026-05-21
parameter_name: FMP_PERIOD
file_or_context: INCAR
definition: Time-step interval between Müller-Plathe swapping events.
default_behavior: 10
common_use:
  - Müller-Plathe method
  - thermal transport
risk_if_misused:
  - Too frequent swapping may strongly perturb dynamics; too infrequent swapping may not establish the intended gradient.
related_parameters:
  - FMP_ACTIVE
  - FMP_DIRECTION
  - FMP_SNUMBER
  - FMP_SWAPNUM
~~~

~~~yaml
record_id: vasp-md-param-fmp-snumber-0040
record_type: parameter
scope: single_software
software:
  - VASP
topic: FMP_SNUMBER
source_type: official_doc
source_ref: https://www.vasp.at/wiki/FMP_SNUMBER
version_or_doc_date: VASP Wiki snapshot 2026-05-21
claim: FMP_SNUMBER sets the number of slabs perpendicular to the temperature gradient in the Müller-Plathe method.
evidence_level: check
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/vasp_aimd_md_parameters.md
related_records:
  - vasp-md-param-fmp-direction-0036
note: Spatial discretization parameter for the imposed temperature-gradient setup.
last_checked: 2026-05-21
parameter_name: FMP_SNUMBER
file_or_context: INCAR
definition: Number of slabs perpendicular to the FMP temperature gradient.
default_behavior: 10
common_use:
  - Müller-Plathe method
  - thermal-gradient binning
risk_if_misused:
  - Too few slabs reduce gradient resolution; too many slabs can make per-slab statistics noisy.
related_parameters:
  - FMP_ACTIVE
  - FMP_DIRECTION
  - FMP_PERIOD
  - FMP_SWAPNUM
~~~

~~~yaml
record_id: vasp-md-param-fmp-swapnum-0041
record_type: parameter
scope: single_software
software:
  - VASP
topic: FMP_SWAPNUM
source_type: official_doc
source_ref: https://www.vasp.at/wiki/FMP_SWAPNUM
version_or_doc_date: VASP Wiki snapshot 2026-05-21
claim: FMP_SWAPNUM sets the number of pairs exchanged in a single swapping event in the Müller-Plathe method.
evidence_level: check
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/vasp_aimd_md_parameters.md
related_records:
  - vasp-md-param-fmp-active-0035
note: Controls strength of each imposed swapping event.
last_checked: 2026-05-21
parameter_name: FMP_SWAPNUM
file_or_context: INCAR
definition: Number of exchanged pairs per Müller-Plathe swap.
default_behavior: 1
common_use:
  - Müller-Plathe method
  - heat-flux control
risk_if_misused:
  - Exchanging too many pairs can overdrive the nonequilibrium perturbation.
related_parameters:
  - FMP_ACTIVE
  - FMP_DIRECTION
  - FMP_PERIOD
  - FMP_SNUMBER
~~~
## Obsidian Links

- [[vasp_aimd_md_parameters]]

