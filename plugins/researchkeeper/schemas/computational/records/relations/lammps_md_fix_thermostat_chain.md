# LAMMPS fix nvt/npt/langevin thermostat chain

> record_type: relation | scope: single_software | software: [LAMMPS]

~~~yaml
record_id: rel-lammps-md-fix-thermostat-chain-0003
record_type: relation
scope: single_software
software:
  - LAMMPS
topic: "fix nvt/npt/langevin thermostat/barostat chain"
source_type: official_doc
source_ref: "https://docs.lammps.org/fix_nh.html"
version_or_doc_date: "LAMMPS 30Mar2026; checked 2026-05-24"
claim: >
  fix nvt/npt/nve are core LAMMPS time integrators. Thermostat and
  barostat damping must be chosen relative to the timestep: values that
  are too small over-couple the dynamics, while values that are too large
  respond too slowly.
evidence_level: should
confidence: local_unverified
related_wiki:
  - computer_kb/wiki/concepts/lammps_md_fix_thermostat_chain.md
related_records:
  - lammps-md-cmd-fix-nve-0014
  - lammps-md-cmd-fix-nvt-npt-nph-0015
  - lammps-md-cmd-fix-langevin-0016
  - lammps-md-cmd-timestep-0012
  - lammps-md-cmd-thermo-0017
  - lammps-md-cmd-thermo-style-0018
  - lammps-md-cmd-dump-0019
note: >
  This record covers only LAMMPS-native integration, thermostat,
  thermodynamic-output, and trajectory-output relationships.
last_checked: 2026-05-24

relation_type: requires_companion
relation_basis:
  - official_cross_ref
  - physical_constraint
  - domain_knowledge

parameters:
  - name: fix nve
    role: "microcanonical integration without a thermostat or barostat"
    constraint: "use after equilibration when energy conservation is verified"
    record: lammps-md-cmd-fix-nve-0014

  - name: fix nvt
    role: "canonical integration with a Nose-Hoover thermostat"
    constraint: "start with Tdamp near 100 times the timestep, then validate"
    record: lammps-md-cmd-fix-nvt-npt-nph-0015

  - name: fix npt
    role: "isothermal-isobaric integration with thermostat and barostat"
    constraint: "validate Tdamp and Pdamp against the simulated material"
    record: lammps-md-cmd-fix-nvt-npt-nph-0015

  - name: fix langevin
    role: "stochastic thermostat using friction and random forces"
    constraint: "smaller damping values mean stronger coupling"
    record: lammps-md-cmd-fix-langevin-0016

  - name: timestep
    role: "integration step controlling the damping-time scale"
    constraint: "damping constants must be meaningfully larger than one step"
    record: lammps-md-cmd-timestep-0012

  - name: thermo
    role: "thermodynamic scalar-output frequency"
    constraint: "choose enough resolution for diagnosis without excessive I/O"
    record: lammps-md-cmd-thermo-0017

  - name: dump
    role: "atomic trajectory output"
    constraint: "choose enough resolution for analysis without excessive I/O"
    record: lammps-md-cmd-dump-0019

relation_rules:
  - id: F1
    type: prerequisite
    from: timestep
    to: "Tdamp (fix nvt)"
    detail: "Tdamp determines thermostat response relative to one MD step."
    decision: "Use an official-documentation starting point and validate."
    consequence: "Too small can over-couple; too large can allow drift."

  - id: F2
    type: mutually_constrained
    from: thermo
    to: dump
    detail: "Scalar and coordinate output intervals are independent I/O costs."
    decision: "Select both from the diagnostic and analysis requirements."
    consequence: "thermo 间隔过小 → 日志 IO 开销大；dump 间隔过小 → 轨迹文件膨胀"

  - id: F3
    type: mutually_exclusive
    from: fix nve
    to: fix nvt
    detail: "Do not apply NVE and NVT integrators to the same group together."
    decision: "Equilibrate with an approved thermostat; use NVE only after validation."
    consequence: "同一 group 同时施加 NVE 与 NVT → 积分器冲突 → 能量/温度行为未定义"

failure_signatures:
  - symptom: "large periodic temperature oscillation under Nose-Hoover NVT"
    likely: "thermostat damping is too short for the selected timestep/system"
  - symptom: "systematic NVE temperature or total-energy drift"
    likely: "timestep, force model, or initial state requires revalidation"
~~~
