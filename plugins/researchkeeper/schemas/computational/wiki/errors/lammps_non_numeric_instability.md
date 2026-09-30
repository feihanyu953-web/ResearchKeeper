---
software: LAMMPS
category: error
status: seed
seed: 9
records: errors.md
---

# LAMMPS non-numeric instability

> Facts: `lammps-error-non-numeric-instability-0006`.

## Signature

`Non-numeric atom coords or pressure or box dimensions - simulation unstable`

## Quick Judgment

The run has become numerically unstable. Stop and inspect the last good frames and thermo output.

## Check Order

1. Inspect thermo output before failure.
2. Check dump frames for overlap or force explosion.
3. Reduce timestep and simplify the run.
4. Verify model/pair-style/element mapping.

## Source

`https://docs.lammps.org/Errors_details.html#non-numeric-atom-coords-or-pressure-or-box-dimensions-simulation-unstable`
## Obsidian Links

- [[lammps_md_basics]]
