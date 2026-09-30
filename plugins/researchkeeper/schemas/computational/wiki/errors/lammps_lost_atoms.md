---
software: LAMMPS
category: error
status: seed
seed: 9
records: errors.md
---

# LAMMPS Lost atoms

> Facts: `lammps-error-lost-atoms-0005`.

## Signature

`Lost atoms`

## Quick Judgment

For MD, treat this as a stability/deployment failure first: check timestep, structure, potential mapping, and boundary behavior.

## Check Order

1. Inspect dump frames immediately before failure.
2. Reduce timestep and run a short smoke test.
3. Verify `pair_coeff` element mapping and units.
4. Do not disable lost-atom checks for production.

## Source

`https://docs.lammps.org/Errors_details.html#lost-atoms`
## Obsidian Links

- [[lammps_md_basics]]
