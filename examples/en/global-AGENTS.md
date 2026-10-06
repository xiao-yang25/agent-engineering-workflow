# Local agent entry

[简体中文](../global-AGENTS.md) · **English** · [Documentation](../../README.md#guides)

Before use, replace `<WORKFLOW_REPO>` in the copyable body below with the cloned repository's absolute path. This is a manual replacement marker, not an automatically expanded variable. Preserve existing personal rules when merging into `~/.codex/AGENTS.md`.

If you customize `CODEX_HOME`, merge into `AGENTS.md` in that directory. Fill in machine-specific information only in the copy outside the repository. Reference the original shared guides directly; do not copy or modify the entire rule set.

Merge only the Markdown block below into the local entry; leave repository navigation here. Replace `<WORKFLOW_REPO>` in the block and verify the resulting absolute references.

```markdown
# Local agent entry

Shared repository: `<WORKFLOW_REPO>`.

- At task start, read `<WORKFLOW_REPO>/docs/en/AGENTS.md`, then follow its task routing to the required guides. Resolve nested references relative to each guide's directory, not the business project or this local entry.
- Keep the current Root model. Root owns architectural tradeoffs and final acceptance.
- Enabled personal executors: to be filled in by the user. Specify permitted material, services, and budget boundaries when enabling them. This template does not authorize sending project material to services.
- Without additional executors, the current Root handles ordinary tasks. If required independent review has no available executor, retain the acceptance gap explicitly; do not treat self-review as independent review.
- Default model preferences: `<WORKFLOW_REPO>/docs/en/model_profiles.md`. Delegation: `<WORKFLOW_REPO>/docs/en/agent_selection.md`. Record personal overrides here rather than account status in the public template.
- Activate Skills only at the user's explicit request, unless higher-priority instructions require otherwise.
- Private review log: choose a location outside the repository. You may copy the blank template from `<WORKFLOW_REPO>/examples/en/workflow_evolution_log.md`. Do not claim scheduling is enabled without configuring it.
- Do not store API keys here. If an entry is unreachable, report the specific gap and continue work that does not depend on it.
```
