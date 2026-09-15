# Models and launch settings

[简体中文](../model_profiles.md) · **English** · [Documentation](../../README.md#guides)

## Default model selection

These are selection recommendations to validate on real tasks, not capability rankings or proof of availability. Record enabled executors and permitted material in the local entry. The current Root keeps the user's model and reasoning settings and owns architecture, decomposition, and final acceptance; the table does not switch Root automatically.

| Work | Suggested executor and settings |
| --- | --- |
| Architecture, complex understanding, core implementation, root-cause analysis | Astra / `gpt-6-astra` / `high`; architectural decisions stay with the current Root |
| Difficult races, lifetimes, major design tradeoffs | Astra / `xhigh`; major tradeoffs stay with the current Root |
| Ordinary implementation, fixes, tests with a clear contract | Sol / `gpt-5.6-sol` / `high` |
| Bounded investigation, ordinary implementation, batch work, supplementary review | OpenCode DeepSeek V4.1 Flash; verify the local model ID and actual requests |
| Locating information, mechanical edits, quick checks | Astra / `low`, or Spark CLI / `gpt-5.3-codex-spark` |
| High-risk independent review | Astra / `high` in a fresh context |
| A specific, persistent reasoning bottleneck | Astra / `max` when warranted |

## Selection and fallback

Choose by uncertainty, affected boundaries, and the cost of error, not file type or quota consumption. Sol and DeepSeek may overlap; choose by task acceptance results. For now, DeepSeek must not be the sole reviewer of a high-risk change. Select other independent reviewers by risk from authorized executors.

Supply only necessary context, without requiring a uniform 1M window. Do not replace user-specified models or reasoning settings without permission. See [Agent collaboration](agent_selection.md) for cancellation, fallback, and escalation. Evaluate routing on comparable tasks using rework, omissions, total time, and actual usage; do not claim efficiency gains without task evidence. Keep records local.

## Native Agents

Pass the listed model and reasoning settings, a bounded task, and rule entry points. If unsupported, report the limitation and fall back by role. Do not start another Root.

## Spark CLI

Verify `codex exec --help` and model support. This example uses default reasoning; explicit `model_reasoning_effort` values must be verified as supported:

```sh
codex exec --model gpt-5.3-codex-spark \
  --sandbox read-only --skip-git-repo-check --ephemeral \
  --cd /absolute/project/path \
  'Act as a Worker on the bounded task. Return evidence without recursive delegation or file changes.'
```

Use `workspace-write` only for authorized write tasks. Do not disable the sandbox or change the current Root or global configuration.

## DeepSeek Flash / OpenCode

The current official API name for V4.1 Flash is `deepseek-flash` ([model details](https://api-docs.deepseek.com/quick_start/pricing/)); use the provider/model ID actually available in OpenCode. Verify capability, service availability, and tool permissions separately. Code implementation or tests require the corresponding existing write/execution authorization; this routing does not expand example permissions.

Set this up only if selected; do not add a harness or background scheduler. Check `opencode run --help`, configuration, and current service model IDs. Do not treat an alias as a pinned version. On macOS:

```sh
brew install anomalyco/tap/opencode
opencode --version
```

Compare and merge the [example](../../examples/en/opencode.json) into local `~/.config/opencode/opencode.json`, preserving existing JSON/JSONC configuration. It defaults to read-only review with a separate Markdown-only editing role. Sharing, automatic updates, shell, recursive delegation, and implicit Skills are disabled; common credential reads are denied. Root must bound permissions for tests or extra tools rather than allow everything.

For cross-project use, allow the shared repository's exact path (`<WORKFLOW_REPO>/*`) in local global and both roles' `permission.external_directory`. Deny that path in the editing role's `permission.edit`, after general Markdown allow rules. Root provides required guides; local `instructions` may also load the shared entry. Project configuration can override global settings, so check effective permissions before delegation. These controls are not an OS sandbox.

```sh
opencode auth login
```

Select DeepSeek and enter the key interactively; `/connect` is an alternative. Never put keys in chat, command arguments, AGENTS, or the repository. Credentials default to `~/.local/share/opencode/auth.json`, which is not an encrypted vault. Use the actual path for a custom XDG directory:

```sh
chmod 600 ~/.local/share/opencode/auth.json
opencode models deepseek
opencode run --agent workflow-review --model deepseek/deepseek-flash \
  --format json 'Do not call any tools. Reply only READY.'
```

Do not probe without credentials. Verify installation, visible metadata, successful requests, and task results separately. After the minimal request succeeds, check document reading, locations, and role permissions with non-sensitive material:

```sh
opencode run --agent workflow-review --format json \
  --dir /absolute/project/path \
  'Review the specified documents in read-only mode. Return locations and evidence, and do not delegate recursively.'
```

Official references: [CLI](https://opencode.ai/docs/cli/) · [permissions](https://opencode.ai/docs/permissions/) · [configuration](https://opencode.ai/docs/config/).
