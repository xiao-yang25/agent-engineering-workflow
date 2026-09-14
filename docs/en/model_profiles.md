# Models and launch settings

[简体中文](../model_profiles.md) · **English** · [Documentation](../../README.md#guides)

## Default model selection

These are optional defaults, not capability rankings or proof of availability. Record enabled executors and permitted material in the local entry.

| Responsibility | Executor | Settings |
| --- | --- | --- |
| Architecture, decomposition, final acceptance | Current Root | Keep its model and settings |
| Investigation, research, independent review | Native Astra | `gpt-6-astra` / `low` |
| Implementation, complex fixes, tests | Native Sol | `gpt-5.6-sol` / `high` |
| Bounded small tasks, quick checks | Spark CLI | `gpt-5.3-codex-spark`; verify supported reasoning settings |
| Documents, batch analysis, low-risk execution | OpenCode DeepSeek Flash | Verify the local model ID, credentials, and actual requests |

## Selection and fallback

Choose by responsibility; do not create work to consume quota. Do not replace user-specified models without permission. Supply only necessary context, without requiring a uniform 1M window. See [availability fallback](agent_selection.md#queueing-and-availability-fallback) for cancellation and attempt limits.

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
