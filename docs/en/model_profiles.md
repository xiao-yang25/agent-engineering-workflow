# Models and launch settings

[简体中文](../model_profiles.md) · **English** · [Documentation](../../README.en.md#guides)

Choose authorized executors by responsibility and verify actual launch capabilities.

<details>
<summary>On this page</summary>

- [Default model selection](#default-model-selection)
- [Selection and fallback](#selection-and-fallback)
- [Native Agents](#native-agents)
- [Spark CLI](#spark-cli)
- [DeepSeek Flash / OpenCode](#deepseek-flash--opencode)

</details>

These are adaptable routing defaults, not a capability ranking or proof of account availability. The user confirms executors and the allowed data scope at the local entry point. See [Agent collaboration](agent_selection.md) for the mechanism.

## Default model selection

| Role | Preferred executor | Settings and entry point |
| --- | --- | --- |
| Requirements, architecture tradeoffs, decomposition, and final acceptance | Current Root | Keep the current model and settings |
| Cross-file investigation, solution research, and independent review | Astra | `gpt-6-astra`, `low`; native sub-Agent |
| Implementation, complex fixes, testing, and failure analysis | Sol | `gpt-5.6-sol`, `high`; native sub-Agent |
| Small, clearly bounded changes and quick checks | Spark | `gpt-5.3-codex-spark`; Codex CLI, using settings that are actually supported |
| Documentation, batch analysis, and low-risk execution | DeepSeek Flash | OpenCode CLI; choose an explicit model ID locally and validate it after entering credentials |

Verify model identifiers against the entry points actually exposed by the host, and do not replace a user-selected model without permission. Spark has no fixed reasoning effort here; check the supported values before launch and record the choice. Do not impose a uniform 1M-token context; provide only necessary material.

## Selection and fallback

Prefer Sol for complex implementation and Astra for investigation and independent assessment. Spark is suitable for clearly bounded small tasks, and a configured DeepSeek instance may handle batch documentation. For fallback, choose an available executor capable of the same role instead of polling a fixed sequence or creating work merely to consume quota. Permission, cancellation, and attempt limits are defined in [Availability fallback](agent_selection.md#queueing-and-availability-fallback).

## Native Agents

At launch, request the model and reasoning effort listed in the table, and provide a bounded task plus the applicable rule entry points. If the host does not expose the model or does not support overriding the setting, report the limitation and fall back by role. Do not start another Root.

## Spark CLI

First verify `codex exec --help` and model support. Read-only example:

```sh
codex exec --model gpt-5.3-codex-spark \
  --sandbox read-only --skip-git-repo-check --ephemeral \
  --cd /absolute/project/path \
  'Act as a Worker on the bounded task. Return evidence without recursive delegation or file changes.'
```

The example uses the CLI's default reasoning setting. When setting it explicitly, pass only a verified supported value for `model_reasoning_effort`. For write tasks, select `workspace-write` only when authorized; do not disable the sandbox automatically. The command does not change the current Root or global configuration.

## DeepSeek Flash / OpenCode

Use OpenCode as a bounded Worker entry point, without adding a custom harness or background scheduler. First verify `opencode run --help`, `opencode models deepseek`, and the configuration. Model visibility and successful authentication do not replace task validation.

DeepSeek announced V4.1-Flash in September 2026. The older `deepseek-v4-flash` is a temporary compatibility route, not a pinned version. Use the ID exposed by the current service and CLI, and store it in the local configuration. [Official announcement](https://www.deepseek.com/en/news/deepseek-v4-1-flash/)

Use the [OpenCode configuration example](../../examples/en/opencode.json). After confirming the model, invoke it with:

```sh
opencode run --agent workflow-review --format json \
  --dir /absolute/project/path \
  'Review the specified documents in read-only mode. Return locations and evidence, and do not delegate recursively.'
```

The example provides roles for read-only documentation review and bounded editing; it disables shell access, recursive delegation, and implicit Skill use. When tests or other tools are needed, the Root configures specific permissions for the task rather than allowing everything. The permission configuration is not an OS sandbox.

Enter the API key locally with `opencode auth login`. By default it is stored in `~/.local/share/opencode/auth.json` (or the configured XDG directory), never in the repository, AGENTS, command arguments, or task prompts. See the [setup instructions](../../README.en.md#deepseek-setup).

Official references: [CLI](https://opencode.ai/docs/cli/), [permissions](https://opencode.ai/docs/permissions/), and [configuration](https://opencode.ai/docs/config/). The presence of documentation does not prove that the CLI is installed locally or that the API has been validated.
