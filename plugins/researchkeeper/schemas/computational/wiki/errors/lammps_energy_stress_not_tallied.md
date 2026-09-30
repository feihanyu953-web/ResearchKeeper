---
software: LAMMPS
category: error
status: seed
seed: 9
records: errors.md
---

# LAMMPS energy or stress not tallied

> Facts: `lammps-error-energy-stress-not-tallied-0009`.

## Signature

`Energy or stress was not tallied by pair style`

## Quick Judgment

The requested thermo/compute/minimization quantity is not being provided by the active pair style or route.

## Check Order

1. Simplify `thermo_style` and computes.
2. Check whether the chosen LAMMPS route supports the requested stress/virial.
3. Test energy/force output first.
4. Do not report unsupported stress/pressure quantities.

## Source

`https://docs.lammps.org/Errors_details.html#energy-or-stress-was-not-tallied-by-pair-style`
## Obsidian Links

- [[lammps_md_basics]] — LAMMPS MD 基础命令组
- [[lammps_non_numeric_instability]] — 数值不稳定报错
- [[lammps_out_of_range_atoms]] — out-of-range atoms 报错


