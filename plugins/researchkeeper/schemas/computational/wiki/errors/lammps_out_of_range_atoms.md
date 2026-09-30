---
software: LAMMPS
category: error
status: seed
seed: 9
records: errors.md
---

# LAMMPS Out of range atoms

> Facts: `lammps-error-out-of-range-atoms-0007`.

## Signature

`Out of range atoms - cannot compute`

## Quick Judgment

Often appears near unstable motion, communication, or neighbor-list problems. Diagnose physical instability before only changing communication settings.

## Check Order

1. Inspect timestep, velocity, and force scale.
2. Inspect dump frames immediately before failure.
3. Check neighbor and communication settings.
4. Reduce timestep and repair geometry if atoms move too far.

## Source

`https://docs.lammps.org/Errors_details.html#out-of-range-atoms-cannot-compute`
## Obsidian Links

- [[lammps_md_basics]]
