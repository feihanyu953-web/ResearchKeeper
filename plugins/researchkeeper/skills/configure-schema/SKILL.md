---
name: configure-schema
description: Use when configuring a new, empty ResearchKeeper paper knowledge base from a built-in or approved custom schema.
disable-model-invocation: true
---

# Configure a first-installation schema

This skill only configures an explicit workspace with no paper knowledge
records. It does not migrate, replace, or roll back an existing knowledge
base.

1. Confirm `${CLAUDE_PLUGIN_ROOT}` and `${CLAUDE_PLUGIN_DATA}` are available.
2. Obtain the workspace path explicitly from the user.
3. Use the plugin wrapper to run `schema status --json` for that workspace.
   Stop if it reports `configured_nonempty` or `invalid`.
4. Run `schema list --json`, then ask whether to start from
   `generic-science` or `electrocatalysis`.
5. Ask for the research area and desired concrete modules. Preserve all seven
   semantic roles in the final proposal; users see the concrete module names.
6. Save the proposal outside the knowledge-base content directories and run
   `schema validate --proposal <file> --json`.
7. Show the exact module-to-file and module-to-role preview. Do not apply it
   until the user explicitly approves.
8. After approval, run
   `schema apply --proposal <file> --yes --json`, then run
   `schema status --json` and `doctor --json`.

Use `${CLAUDE_PLUGIN_ROOT}/bin/rsk` on POSIX and
`${CLAUDE_PLUGIN_ROOT}\bin\rsk.cmd` on Windows. Always pass the explicit
workspace. Schema configuration must not install dependencies, download a
model, create embeddings, or write vector knowledge indexes.
