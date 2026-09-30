---
software: LAMMPS
category: concept
status: seed
seed: "P4"
records:
  - relations/lammps_md_fix_thermostat_chain.md
---

# LAMMPS thermostat and integration chain

> Facts trace to
> `computer_kb/records/relations/lammps_md_fix_thermostat_chain.md`.

## MD fix selection

| fix | Typical role | Damping consideration |
|---|---|---|
| `fix nve` | Production sampling without a thermostat | N/A |
| `fix nvt` | Temperature-controlled equilibration | Validate `Tdamp` relative to timestep |
| `fix npt` | Temperature/pressure-controlled equilibration | Validate both `Tdamp` and `Pdamp` |
| `fix langevin` | Stochastic thermostat | Smaller damping means stronger coupling |

Never apply incompatible time integrators to the same atom group. Treat
damping values as documented starting points and verify temperature,
energy, and ensemble behavior for the actual system.

## Related

- [[lammps_md_setup_chain]] — LAMMPS MD prerequisite command chain
