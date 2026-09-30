# LAMMPS MD records

> Seed3 records for LAMMPS basic molecular-dynamics input commands and data flow.
> Sources are the official LAMMPS documentation URLs recorded in each entry.
> Scope: core MD script building blocks. `pair_style` specifics are documented at page level.

## seed3-lammps-md-basic-2026-05-21

~~~yaml
record_id: lammps-md-cmd-units-0001
record_type: command
scope: single_software
software:
  - LAMMPS
topic: units
source_type: official_doc
source_ref: https://docs.lammps.org/units.html
version_or_doc_date: LAMMPS docs release git info 30Mar2026; checked 2026-05-21
claim: The units command selects the unit system used by a LAMMPS simulation.
evidence_level: check
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/lammps_md_basics.md
related_records:
  - lammps-md-cmd-timestep-0012
  - lammps-md-cmd-velocity-0013
note: Unit style changes the physical meaning of time, distance, energy, temperature, pressure, and timestep values.
last_checked: 2026-05-21
command_name: units
file_or_context: LAMMPS input script
definition: Selects simulation units.
default_behavior: lj if not set before simulation box creation
common_use:
  - metal units for many atomistic materials simulations
  - real units for biomolecular or molecular force fields
risk_if_misused:
  - Pair coefficients, timestep, masses, and temperature damping constants become physically inconsistent if copied across unit styles.
related_parameters:
  - timestep
  - velocity
domain_guidance:
  - example_status: needs_verification
    rule: "金属/界面水 MD → units metal (eV, Å, ps, K)"
    applies_to: {systems: [metal_water_interface], tasks: [md]}
    value: metal
    reason: "metal units 与 VASP 输出单位一致; timestep 在 ps; 能量在 eV"
parameter_relations:
  - example_status: needs_verification
    target: timestep
    relation: prerequisite
    desc: "units 决定 timestep 的物理含义; metal 下 0.0005 = 0.5 fs"
~~~

~~~yaml
record_id: lammps-md-cmd-atom-style-0002
record_type: command
scope: single_software
software:
  - LAMMPS
topic: atom_style
source_type: official_doc
source_ref: https://docs.lammps.org/atom_style.html
version_or_doc_date: LAMMPS docs release git info 30Mar2026; checked 2026-05-21
claim: The atom_style command defines what per-atom attributes are stored and expected by LAMMPS.
evidence_level: check
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/lammps_md_basics.md
related_records:
  - lammps-md-cmd-read-data-0005
  - lammps-md-format-data-file-0025
note: Atom style must match the data file sections and the force field requirements.
last_checked: 2026-05-21
command_name: atom_style
file_or_context: LAMMPS input script
definition: Selects per-atom data model.
default_behavior: atomic
common_use:
  - atomic for simple atomic systems
  - charge for charged atom models
  - full for molecular topologies with bonds/angles/charges
risk_if_misused:
  - A data file with bonds, charges, or molecule IDs may fail or be misinterpreted under the wrong atom style.
related_parameters:
  - read_data
~~~

~~~yaml
record_id: lammps-md-cmd-boundary-0003
record_type: command
scope: single_software
software:
  - LAMMPS
topic: boundary
source_type: official_doc
source_ref: https://docs.lammps.org/boundary.html
version_or_doc_date: LAMMPS docs release git info 30Mar2026; checked 2026-05-21
claim: The boundary command sets the style of boundaries for the global simulation box in each dimension.
evidence_level: check
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/lammps_md_basics.md
related_records:
  - lammps-md-cmd-dimension-0004
  - lammps-md-cmd-create-box-0006
note: Boundary choices are part of the physical model; they are not a harmless output setting.
last_checked: 2026-05-21
command_name: boundary
file_or_context: LAMMPS input script
definition: Sets periodic, fixed, shrink-wrapped, or related boundary styles.
default_behavior: p p p
common_use:
  - periodic bulk systems
  - nonperiodic surfaces or slabs
risk_if_misused:
  - Wrong periodicity can change density, surface physics, pressure behavior, and atom loss behavior.
related_parameters:
  - dimension
  - create_box
~~~

~~~yaml
record_id: lammps-md-cmd-dimension-0004
record_type: command
scope: single_software
software:
  - LAMMPS
topic: dimension
source_type: official_doc
source_ref: https://docs.lammps.org/dimension.html
version_or_doc_date: LAMMPS docs release git info 30Mar2026; checked 2026-05-21
claim: The dimension command sets whether a LAMMPS simulation is two-dimensional or three-dimensional.
evidence_level: check
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/lammps_md_basics.md
related_records:
  - lammps-md-cmd-boundary-0003
note: Most atomistic materials MD workflows are 3D unless there is a deliberate 2D model.
last_checked: 2026-05-21
command_name: dimension
file_or_context: LAMMPS input script
definition: Sets simulation dimensionality.
default_behavior: 3
common_use:
  - 3D atomistic MD
  - specialized 2D simulations
risk_if_misused:
  - A wrong dimensionality changes allowed motion, box geometry, and physical interpretation.
related_parameters:
  - boundary
~~~

~~~yaml
record_id: lammps-md-cmd-read-data-0005
record_type: command
scope: single_software
software:
  - LAMMPS
topic: read_data
source_type: official_doc
source_ref: https://docs.lammps.org/read_data.html
version_or_doc_date: LAMMPS docs release git info 30Mar2026; checked 2026-05-21
claim: The read_data command reads a LAMMPS data file that defines the simulation box, atoms, and optionally topology and coefficients.
evidence_level: check
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/lammps_md_basics.md
related_records:
  - lammps-md-format-data-file-0025
  - lammps-md-cmd-atom-style-0002
note: Use read_data when the initial structure is provided in a data file; create_box/create_atoms workflows are a different construction route.
last_checked: 2026-05-21
command_name: read_data
file_or_context: LAMMPS input script + LAMMPS data file
definition: Reads system topology/coordinates and related setup from a data file.
default_behavior: no system is loaded until a box/atoms are created or read
common_use:
  - importing prepared MD structures
  - restarting from converted atomistic models
risk_if_misused:
  - Data file format, atom_style, atom types, and coefficient sections must be consistent.
related_parameters:
  - atom_style
  - write_data
~~~

~~~yaml
record_id: lammps-md-cmd-create-box-0006
record_type: command
scope: single_software
software:
  - LAMMPS
topic: create_box
source_type: official_doc
source_ref: https://docs.lammps.org/create_box.html
version_or_doc_date: LAMMPS docs release git info 30Mar2026; checked 2026-05-21
claim: The create_box command creates a simulation box for a LAMMPS system.
evidence_level: check
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/lammps_md_basics.md
related_records:
  - lammps-md-cmd-read-data-0005
  - lammps-md-cmd-boundary-0003
note: Usually paired with region/create_atoms style workflows rather than read_data.
last_checked: 2026-05-21
command_name: create_box
file_or_context: LAMMPS input script
definition: Creates the global simulation box.
default_behavior: absent unless explicitly called
common_use:
  - building simple systems inside LAMMPS
  - defining atom type count before create_atoms
risk_if_misused:
  - Box size, type count, and boundary style must match intended structure construction.
related_parameters:
  - boundary
  - dimension
~~~

~~~yaml
record_id: lammps-md-cmd-mass-0007
record_type: command
scope: single_software
software:
  - LAMMPS
topic: mass
source_type: official_doc
source_ref: https://docs.lammps.org/mass.html
version_or_doc_date: LAMMPS docs release git info 30Mar2026; checked 2026-05-21
claim: The mass command assigns mass to one or more atom types.
evidence_level: check
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/lammps_md_basics.md
related_records:
  - lammps-md-cmd-atom-style-0002
  - lammps-md-cmd-timestep-0012
note: Some pair styles can provide masses or require explicit masses; check the chosen force field documentation.
last_checked: 2026-05-21
command_name: mass
file_or_context: LAMMPS input script or data file
definition: Sets atom-type masses.
default_behavior: unset unless provided by data file, command, or potential-specific mechanism
common_use:
  - assigning element masses
  - checking converted data files
risk_if_misused:
  - Incorrect masses change dynamical timescales, velocities, and temperature interpretation.
related_parameters:
  - atom_style
  - timestep
~~~

~~~yaml
record_id: lammps-md-cmd-pair-style-0008
record_type: command
scope: single_software
software:
  - LAMMPS
topic: pair_style
source_type: official_doc
source_ref: https://docs.lammps.org/pair_style.html
version_or_doc_date: LAMMPS docs release git info 30Mar2026; checked 2026-05-21
claim: The pair_style command sets the formula or model used to compute pairwise or many-body nonbonded interactions.
evidence_level: check
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/lammps_md_basics.md
related_records:
  - lammps-md-cmd-pair-coeff-0009
note: Specific pair styles have their own syntax, units expectations, package requirements, and coefficient rules.
last_checked: 2026-05-21
command_name: pair_style
file_or_context: LAMMPS input script
definition: Selects interatomic potential style.
default_behavior: none
common_use:
  - classical force fields
  - many-body potentials
risk_if_misused:
  - Choosing the wrong potential style invalidates forces and energies.
  - Style-specific unit and element mapping requirements must be checked.
related_parameters:
  - pair_coeff
~~~

~~~yaml
record_id: lammps-md-cmd-pair-coeff-0009
record_type: command
scope: single_software
software:
  - LAMMPS
topic: pair_coeff
source_type: official_doc
source_ref: https://docs.lammps.org/pair_coeff.html
version_or_doc_date: LAMMPS docs release git info 30Mar2026; checked 2026-05-21
claim: The pair_coeff command sets coefficients for the selected pair_style.
evidence_level: check
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/lammps_md_basics.md
related_records:
  - lammps-md-cmd-pair-style-0008
note: Syntax and required arguments are pair_style-specific.
last_checked: 2026-05-21
command_name: pair_coeff
file_or_context: LAMMPS input script
definition: Assigns potential coefficients or model files for atom-type interactions.
default_behavior: unset until specified or read from data/restart where applicable
common_use:
  - assigning epsilon/sigma for LJ
  - assigning element mapping for many-body potentials
  - pointing to model files
risk_if_misused:
  - Wrong atom-type mapping or coefficients can produce plausible-looking but physically wrong trajectories.
related_parameters:
  - pair_style
~~~

~~~yaml
record_id: lammps-md-cmd-neighbor-0010
record_type: command
scope: single_software
software:
  - LAMMPS
topic: neighbor
source_type: official_doc
source_ref: https://docs.lammps.org/neighbor.html
version_or_doc_date: LAMMPS docs release git info 30Mar2026; checked 2026-05-21
claim: The neighbor command sets parameters for building neighbor lists, including the skin distance.
evidence_level: check
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/lammps_md_basics.md
related_records:
  - lammps-md-cmd-neigh-modify-0011
note: Neighbor settings affect performance and whether interactions are safely captured between rebuilds.
last_checked: 2026-05-21
command_name: neighbor
file_or_context: LAMMPS input script
definition: Configures neighbor-list build style and skin.
default_behavior: style/bin with default skin depending on units
common_use:
  - tuning neighbor list performance
  - stabilizing high-temperature or fast-moving systems
risk_if_misused:
  - Too small a skin or too infrequent rebuild can miss interactions.
  - Too large a skin can slow simulations.
related_parameters:
  - neigh_modify
  - timestep
~~~

~~~yaml
record_id: lammps-md-cmd-neigh-modify-0011
record_type: command
scope: single_software
software:
  - LAMMPS
topic: neigh_modify
source_type: official_doc
source_ref: https://docs.lammps.org/neigh_modify.html
version_or_doc_date: LAMMPS docs release git info 30Mar2026; checked 2026-05-21
claim: The neigh_modify command sets options that affect how and when neighbor lists are built.
evidence_level: check
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/lammps_md_basics.md
related_records:
  - lammps-md-cmd-neighbor-0010
note: Commonly used to control delay/every/check behavior for neighbor-list rebuilding.
last_checked: 2026-05-21
command_name: neigh_modify
file_or_context: LAMMPS input script
definition: Modifies neighbor-list build behavior.
default_behavior: LAMMPS defaults depend on command options and simulation state
common_use:
  - controlling rebuild frequency
  - checking neighbor-list safety/performance tradeoffs
risk_if_misused:
  - Overly delayed neighbor rebuilds can cause inaccurate forces or lost atoms in dynamic systems.
related_parameters:
  - neighbor
  - timestep
~~~

~~~yaml
record_id: lammps-md-cmd-timestep-0012
record_type: command
scope: single_software
software:
  - LAMMPS
topic: timestep
source_type: official_doc
source_ref: https://docs.lammps.org/timestep.html
version_or_doc_date: LAMMPS docs release git info 30Mar2026; checked 2026-05-21
claim: The timestep command sets the size of the MD timestep.
evidence_level: check
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/lammps_md_basics.md
related_records:
  - lammps-md-cmd-units-0001
  - lammps-md-cmd-run-0021
note: Physical timestep units depend on the selected units style.
last_checked: 2026-05-21
command_name: timestep
file_or_context: LAMMPS input script
definition: Sets MD integration timestep.
default_behavior: default value depends on units style
common_use:
  - MD stability control
  - trajectory time accounting
risk_if_misused:
  - Too large a timestep can destabilize dynamics or lose atoms.
  - Copying timestep values across units styles is unsafe.
related_parameters:
  - units
  - run
domain_guidance:
  - example_status: needs_verification
    rule: "含 H 水体系 → timestep=0.5 fs (0.0005 ps)"
    applies_to: {systems: [metal_water_interface], tasks: [md]}
    value: 0.0005
    reason: "轻元素 (H) 高频 O-H 伸缩模 (~3500 cm⁻¹) → timestep ≤ 0.5 fs; 纯金属界面可用 1.0 fs"
parameter_relations:
  - example_status: needs_verification
    target: units
    relation: prerequisite
    desc: "timestep 物理含义由 units 决定; metal 下单位为 ps"
  - example_status: needs_verification
    target: fix
    relation: mutually_constrained
    desc: "timestep 决定 Tdamp 选择 (Tdamp ~ 100×timestep)"
~~~

~~~yaml
record_id: lammps-md-cmd-velocity-0013
record_type: command
scope: single_software
software:
  - LAMMPS
topic: velocity
source_type: official_doc
source_ref: https://docs.lammps.org/velocity.html
version_or_doc_date: LAMMPS docs release git info 30Mar2026; checked 2026-05-21
claim: The velocity command sets or changes atom velocities.
evidence_level: check
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/lammps_md_basics.md
related_records:
  - lammps-md-cmd-units-0001
  - lammps-md-cmd-fix-nvt-npt-nph-0015
note: Velocity creation often uses a target temperature and random seed; record the seed for reproducibility.
last_checked: 2026-05-21
command_name: velocity
file_or_context: LAMMPS input script
definition: Creates, sets, scales, ramps, or zeros velocities.
default_behavior: velocities are whatever is read, created, or initialized by other commands
common_use:
  - initial temperature assignment
  - removing drift or rotation
risk_if_misused:
  - Missing or undocumented seeds make initial conditions non-reproducible.
  - Velocity temperature must be consistent with units and target ensemble.
related_parameters:
  - units
  - fix nvt
  - fix langevin
~~~

~~~yaml
record_id: lammps-md-cmd-fix-nve-0014
record_type: command
scope: single_software
software:
  - LAMMPS
topic: fix nve
source_type: official_doc
source_ref: https://docs.lammps.org/fix_nve.html
version_or_doc_date: LAMMPS docs release git info 30Mar2026; checked 2026-05-21
claim: The fix nve command performs constant NVE time integration.
evidence_level: check
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/lammps_md_basics.md
related_records:
  - lammps-md-cmd-timestep-0012
  - lammps-md-cmd-run-0021
note: NVE integrates equations of motion without thermostat/barostat control.
last_checked: 2026-05-21
command_name: fix nve
file_or_context: LAMMPS input script
definition: Applies NVE time integration to a group of atoms.
default_behavior: no integration fix exists until specified
common_use:
  - production NVE after equilibration
  - integration combined with separate thermostats such as fix langevin
risk_if_misused:
  - Running without any integration fix means atoms will not be time-integrated.
  - Combining multiple integration fixes on the same atoms can double-integrate motion.
related_parameters:
  - timestep
  - run
~~~

~~~yaml
record_id: lammps-md-cmd-fix-nvt-npt-nph-0015
record_type: command
scope: single_software
software:
  - LAMMPS
topic: fix nvt/npt/nph
source_type: official_doc
source_ref: https://docs.lammps.org/fix_nh.html
version_or_doc_date: LAMMPS docs release git info 30Mar2026; checked 2026-05-21
claim: The fix nvt, fix npt, and fix nph commands implement Nose-Hoover thermostat and/or barostat time integration.
evidence_level: check
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/lammps_md_basics.md
related_records:
  - lammps-md-cmd-timestep-0012
  - lammps-md-cmd-velocity-0013
note: Choose NVT for thermostat only, NPT for thermostat plus pressure control, and NPH for pressure control without thermostat.
last_checked: 2026-05-21
command_name: fix nvt / fix npt / fix nph
file_or_context: LAMMPS input script
definition: Nose-Hoover family thermostat/barostat integration fixes.
default_behavior: no thermostat/barostat integration fix exists until specified
common_use:
  - NVT equilibration
  - NPT density/pressure equilibration
  - NPH dynamics
risk_if_misused:
  - Damping constants are in time units of the selected unit style.
  - Applying barostat to inappropriate boundary/box conditions can be physically wrong.
related_parameters:
  - units
  - timestep
  - velocity
domain_guidance:
  - example_status: needs_verification
    rule: "production (after equilibration) → fix nve; equilibration → fix nvt"
    applies_to: {systems: [metal_water_interface], tasks: [md]}
    value: "nvt (equilibration) → nve (production)"
    reason: "NVT for 温控 equilibration (20-50 ps); NVE for 无人工 thermostat 效应的 production sampling"
  - example_status: needs_verification
    rule: "Nose-Hoover Tdamp ~ 100 × timestep (0.05 ps for 0.5 fs ts)"
    applies_to: {tasks: [md_nvt]}
    value: 0.05
    reason: "Tdamp 太小 → over-coupling + 人工振荡; 太大 → 温度漂移"
parameter_relations:
  - example_status: needs_verification
    target: timestep
    relation: mutually_constrained
    desc: "Tdamp 需要与 timestep 匹配; Tdamp ~ 100 × timestep"
~~~

~~~yaml
record_id: lammps-md-cmd-fix-langevin-0016
record_type: command
scope: single_software
software:
  - LAMMPS
topic: fix langevin
source_type: official_doc
source_ref: https://docs.lammps.org/fix_langevin.html
version_or_doc_date: LAMMPS docs release git info 30Mar2026; checked 2026-05-21
claim: The fix langevin command applies Langevin thermostat forces to atoms.
evidence_level: check
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/lammps_md_basics.md
related_records:
  - lammps-md-cmd-fix-nve-0014
  - lammps-md-cmd-velocity-0013
note: Langevin thermostatting is not itself a complete integrator for positions; it is often combined with an integration fix such as fix nve.
last_checked: 2026-05-21
command_name: fix langevin
file_or_context: LAMMPS input script
definition: Adds stochastic/damping thermostat forces.
default_behavior: no Langevin thermostat unless specified
common_use:
  - stochastic temperature control
  - thermostat plus fix nve integration
risk_if_misused:
  - Forgetting the integration fix can leave thermostat forces without proper time integration.
  - Damping and seed choices affect dynamics and reproducibility.
related_parameters:
  - fix nve
  - velocity
  - timestep
~~~

~~~yaml
record_id: lammps-md-cmd-thermo-0017
record_type: command
scope: single_software
software:
  - LAMMPS
topic: thermo
source_type: official_doc
source_ref: https://docs.lammps.org/thermo.html
version_or_doc_date: LAMMPS docs release git info 30Mar2026; checked 2026-05-21
claim: The thermo command sets how often thermodynamic info is printed.
evidence_level: check
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/lammps_md_basics.md
related_records:
  - lammps-md-cmd-thermo-style-0018
note: Thermo cadence affects monitoring and log size, not physical dynamics.
last_checked: 2026-05-21
command_name: thermo
file_or_context: LAMMPS input script / log output
definition: Sets thermo output interval in timesteps.
default_behavior: 0 or LAMMPS default depending on context; check current docs for exact behavior
common_use:
  - printing temperature, energy, pressure during runs
  - detecting drift or instability
risk_if_misused:
  - Too sparse output can hide early instability; too frequent output can slow runs and bloat logs.
related_parameters:
  - thermo_style
  - run
~~~

~~~yaml
record_id: lammps-md-cmd-thermo-style-0018
record_type: command
scope: single_software
software:
  - LAMMPS
topic: thermo_style
source_type: official_doc
source_ref: https://docs.lammps.org/thermo_style.html
version_or_doc_date: LAMMPS docs release git info 30Mar2026; checked 2026-05-21
claim: The thermo_style command selects what thermodynamic quantities are printed.
evidence_level: check
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/lammps_md_basics.md
related_records:
  - lammps-md-cmd-thermo-0017
note: Include quantities needed to diagnose the target ensemble, such as temp, press, pe, ke, etotal, vol, density, and cell dimensions when relevant.
last_checked: 2026-05-21
command_name: thermo_style
file_or_context: LAMMPS input script / log output
definition: Controls fields in thermo output.
default_behavior: default style if not set
common_use:
  - custom MD diagnostics
  - ensemble monitoring
risk_if_misused:
  - Missing diagnostic fields makes it harder to detect pressure, temperature, or energy drift.
related_parameters:
  - thermo
~~~

~~~yaml
record_id: lammps-md-cmd-dump-0019
record_type: command
scope: single_software
software:
  - LAMMPS
topic: dump
source_type: official_doc
source_ref: https://docs.lammps.org/dump.html
version_or_doc_date: LAMMPS docs release git info 30Mar2026; checked 2026-05-21
claim: The dump command writes atom snapshots or other per-atom data to files during a simulation.
evidence_level: check
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/lammps_md_basics.md
related_records:
  - lammps-md-cmd-dump-modify-0020
note: Dump style and fields should match downstream analysis needs.
last_checked: 2026-05-21
command_name: dump
file_or_context: LAMMPS input script / trajectory output
definition: Defines trajectory/per-atom output.
default_behavior: no trajectory dump unless specified
common_use:
  - writing atom coordinates
  - writing velocities or forces for analysis
risk_if_misused:
  - Missing image flags, element names, velocities, or forces can block later analysis.
  - Too frequent dumps can dominate storage.
related_parameters:
  - dump_modify
~~~

~~~yaml
record_id: lammps-md-cmd-dump-modify-0020
record_type: command
scope: single_software
software:
  - LAMMPS
topic: dump_modify
source_type: official_doc
source_ref: https://docs.lammps.org/dump_modify.html
version_or_doc_date: LAMMPS docs release git info 30Mar2026; checked 2026-05-21
claim: The dump_modify command modifies parameters of a previously defined dump.
evidence_level: check
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/lammps_md_basics.md
related_records:
  - lammps-md-cmd-dump-0019
note: Commonly used to control sorting, element labels, wrapping/unwrapping, and output formatting.
last_checked: 2026-05-21
command_name: dump_modify
file_or_context: LAMMPS input script / trajectory output
definition: Changes behavior or metadata of a dump.
default_behavior: dump-style-specific defaults
common_use:
  - adding element labels
  - controlling sorting/wrapping
risk_if_misused:
  - Wrong wrapping or missing element mapping can make visualization and diffusion analysis misleading.
related_parameters:
  - dump
~~~

~~~yaml
record_id: lammps-md-cmd-run-0021
record_type: command
scope: single_software
software:
  - LAMMPS
topic: run
source_type: official_doc
source_ref: https://docs.lammps.org/run.html
version_or_doc_date: LAMMPS docs release git info 30Mar2026; checked 2026-05-21
claim: The run command runs dynamics for a specified number of timesteps.
evidence_level: check
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/lammps_md_basics.md
related_records:
  - lammps-md-cmd-timestep-0012
  - lammps-md-cmd-fix-nve-0014
note: Physical trajectory time is run steps times timestep, interpreted under the active units style.
last_checked: 2026-05-21
command_name: run
file_or_context: LAMMPS input script
definition: Advances the simulation by N timesteps.
default_behavior: no dynamics run until called
common_use:
  - equilibration
  - production MD
risk_if_misused:
  - A run command without suitable integration fixes may not propagate atoms as intended.
  - Step count alone is not a physical time unless timestep and units are known.
related_parameters:
  - timestep
  - fix nve
  - fix nvt
~~~

~~~yaml
record_id: lammps-md-cmd-minimize-0022
record_type: command
scope: single_software
software:
  - LAMMPS
topic: minimize
source_type: official_doc
source_ref: https://docs.lammps.org/minimize.html
version_or_doc_date: LAMMPS docs release git info 30Mar2026; checked 2026-05-21
claim: The minimize command performs energy minimization of the system.
evidence_level: check
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/lammps_md_basics.md
related_records:
  - lammps-md-cmd-run-0021
  - lammps-md-cmd-neighbor-0010
note: Often used before MD to relax bad contacts, but minimization is not a substitute for thermal equilibration.
last_checked: 2026-05-21
command_name: minimize
file_or_context: LAMMPS input script
definition: Minimizes potential energy according to specified tolerances and iteration limits.
default_behavior: no minimization until called
common_use:
  - removing bad contacts
  - preparing initial structures before MD
risk_if_misused:
  - Skipping minimization for overlapping structures can lead to huge forces or lost atoms.
  - Overinterpreting minimized structures as thermally equilibrated is wrong.
related_parameters:
  - run
  - neighbor
~~~

~~~yaml
record_id: lammps-md-cmd-reset-timestep-0023
record_type: command
scope: single_software
software:
  - LAMMPS
topic: reset_timestep
source_type: official_doc
source_ref: https://docs.lammps.org/reset_timestep.html
version_or_doc_date: LAMMPS docs release git info 30Mar2026; checked 2026-05-21
claim: The reset_timestep command resets the current timestep counter.
evidence_level: check
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/lammps_md_basics.md
related_records:
  - lammps-md-cmd-run-0021
note: Useful for restarting logical time after setup/equilibration, but it changes trajectory step numbering.
last_checked: 2026-05-21
command_name: reset_timestep
file_or_context: LAMMPS input script / trajectory metadata
definition: Resets timestep numbering.
default_behavior: timestep counter continues from current state
common_use:
  - setting production run step count to 0
  - simplifying output indexing
risk_if_misused:
  - Resetting steps can confuse concatenated trajectories and time-series analysis if not documented.
related_parameters:
  - run
  - dump
~~~

~~~yaml
record_id: lammps-md-cmd-write-data-0024
record_type: command
scope: single_software
software:
  - LAMMPS
topic: write_data
source_type: official_doc
source_ref: https://docs.lammps.org/write_data.html
version_or_doc_date: LAMMPS docs release git info 30Mar2026; checked 2026-05-21
claim: The write_data command writes the current system state to a LAMMPS data file.
evidence_level: check
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/lammps_md_basics.md
related_records:
  - lammps-md-cmd-read-data-0005
  - lammps-md-format-data-file-0025
note: Useful for preserving prepared, minimized, or equilibrated structures for later runs.
last_checked: 2026-05-21
command_name: write_data
file_or_context: LAMMPS input script / LAMMPS data file
definition: Writes system configuration to a data file.
default_behavior: no data file written unless called
common_use:
  - exporting prepared systems
  - checkpointing structure/topology in data format
risk_if_misused:
  - Data files may not preserve all dynamic state that a restart file would preserve.
related_parameters:
  - read_data
~~~

~~~yaml
record_id: lammps-md-format-data-file-0025
record_type: file_format
scope: single_software
software:
  - LAMMPS
topic: LAMMPS data file
source_type: official_doc
source_ref: https://docs.lammps.org/2001/data_format.html
version_or_doc_date: LAMMPS data format documentation page; checked 2026-05-21
claim: A LAMMPS data file read by read_data contains basic information about system size, initial coordinates, molecular topology, and optional force-field coefficients.
evidence_level: check
confidence: official
related_wiki:
  - computer_kb/wiki/concepts/lammps_md_basics.md
related_records:
  - lammps-md-cmd-read-data-0005
  - lammps-md-cmd-write-data-0024
note: This page is an official LAMMPS data-format reference and is older-style documentation; use it together with current read_data/write_data docs.
last_checked: 2026-05-21
file_or_context: LAMMPS data file
definition: Structure/topology/coefficient file format consumed by read_data.
default_behavior: no data file exists unless provided or written
common_use:
  - importing atomic coordinates
  - storing topology and type definitions
risk_if_misused:
  - Header counts, atom style, sections, atom IDs, image flags, and coefficients must match the intended simulation model.
related_parameters:
  - read_data
  - atom_style
  - write_data
~~~

## Obsidian Links

- [[lammps_md_basics]]
- [[lammps_command_index]]


- [[lammps_lost_atoms]]

