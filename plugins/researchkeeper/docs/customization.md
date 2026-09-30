# Customizing the First-Install Schema

Use `/researchkeeper:configure-schema` during first installation of an empty
paper knowledge base. ResearchKeeper includes `generic-science` and
`electrocatalysis`; the assistant may also prepare a custom proposal for the
user to review.

Every concrete module maps to one stable semantic role: `literature`,
`entities`, `methods`, `conditions`, `results`, `relations`, or `claims`.
Only selected concrete modules and their files are materialized.

The Claude Code skill previews a proposal, asks for explicit approval, then
runs the canonical CLI:

```text
schema validate --workspace <workspace> --proposal <proposal> --json
schema apply --workspace <workspace> --proposal <proposal> --yes --json
schema status --workspace <workspace> --json
```

Module definitions require `name`, `display`, `file`, `role`, `description`,
`trigger_keywords`, `extract_rules`, and `audit_focus`. Module names and files
must be unique safe relative names. The final proposal must cover all seven
roles and contain exactly one module with the `literature` role.

Applying the same proposal to the same empty workspace is byte-idempotent.
A conflicting proposal or any real knowledge record fails closed. RSK-6 does
not migrate an existing knowledge base and does not provide schema
generations or rollback.
