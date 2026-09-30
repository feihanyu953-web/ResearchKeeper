---
software: LAMMPS
category: error
status: seed
seed: 9
records: errors.md
---

# LAMMPS unrecognized style / package not enabled

> Facts: `lammps-error-unrecognized-style-package-0008`.

## Signature

`Unrecognized ... style ...`

## Quick Judgment

For custom potential deployment, this often means the local LAMMPS binary lacks the requested style/package/integration.

## Check Order

1. Check which LAMMPS executable is actually used.
2. Check enabled packages/build information.
3. Confirm the required package is enabled for the requested pair style.
4. Test a minimal input with only the target pair style.

## Source

`https://docs.lammps.org/Errors_details.html#unrecognized-style`
## Obsidian Links

- [[lammps_command_index]]



