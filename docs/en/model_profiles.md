# Models and launch settings

[简体中文](../model_profiles.md) · **English** · [Documentation](../../README.md#guides)

## Default model selection

These are selection recommendations to validate on real tasks, not capability rankings or proof of availability. Record enabled executors and permitted material in the local entry. The current Root keeps the user's model and reasoning settings and owns architecture, decomposition, and final acceptance; the table does not switch Root automatically.

| Work | Suggested executor and settings |
| --- | --- |
| Everyday engineering Root, clear-contract implementation, fixes, tests | 6.1 Sol / `gpt-6.1-sol` / `high`; use `medium` when the task is small and easy to check |
| Complex cross-file implementation, ordinary root-cause investigation, independent review | 6.1 Sol / `gpt-6.1-sol` / `high`; raise to `xhigh` only for a concrete reasoning bottleneck |
| Highly ambiguous work, difficult races, major and hard-to-reverse architecture choices | Astra / `gpt-6-astra` / `high`–`xhigh`; architectural decisions stay with the current Root |
| Bounded investigation, ordinary implementation, batch work, supplementary review | OpenCode DeepSeek V4.1 Flash; verify the local model ID and actual requests |
| Clear, repetitive, high-volume discovery, extraction, or mechanical transformation | Luna / `gpt-6-luna` / `high` as an optional efficiency candidate; use 6.1 Sol when hidden constraints or conflicts matter |
| High-risk independent review | Astra / `high` in a fresh context |
| A specific, persistent reasoning bottleneck with sufficient evidence | Use `max` on the current model when warranted; keep Astra as the candidate for hard-to-reverse decisions |

## Selection and fallback

This routing uses the [OpenAI model guide](https://learn.chatgpt.com/docs/models) and [model selection guidance](https://developers.openai.com/api/docs/guides/model-selection) as a starting point for this workflow. 6.1 Sol is the default candidate for the everyday Root, complex coding, and multi-step workers; Luna is an optional efficiency candidate for clear, repetitive, batch-verifiable work. The Root may use 6.1 Sol for architecture and final acceptance; the role name does not require an automatic Astra upgrade. Identically named reasoning levels are not equivalent across generations: do not mechanically retain old levels or default to `max`. Distinguish API defaults from Codex recommendations; actual models and levels depend on the host and account.

During migration, prefer 6.1 Sol for the implementation role previously assigned to `gpt-5.6-sol`, and 6 Luna for clear, repetitive bounded tasks. `gpt-5.6-luna` / `high` can still handle a clearly scoped documentation edit, extraction, or mechanical transformation, but treat it as a verified compatibility fallback rather than the new default. Verify model visibility and client support separately; this does not establish universal replacement or lower latency. DeepSeek may continue its listed work; a new release does not automatically disable it. Keep Astra as the candidate for complex decisions and high-risk review.

Use reasoning levels progressively: `low` for small, clear, easy-to-check changes; `medium` for routine implementation and known-cause fixes; `high` for cross-file logic, boundary checks, and independent review; `xhigh` when states, assumptions, or constraints interact; and `max` only for a concrete reasoning bottleneck with sufficient evidence. Ultra involves parallel subagents with independently verifiable work; it is not simply deeper single-agent reasoning. Select speed separately: Standard is the starting point, and Fast is for cases where shorter waiting justifies higher usage.

Choose by uncertainty, affected boundaries, and the cost of error, not file type or quota consumption. Sol and DeepSeek may overlap; choose by task acceptance results. For now, DeepSeek must not be the sole reviewer of a high-risk change. Select other independent reviewers by risk from authorized executors.

Supply only necessary context, without requiring a uniform 1M window. Do not replace user-specified models or reasoning settings without permission. See [Agent collaboration](agent_selection.md) for cancellation, fallback, and escalation. Evaluate routing on comparable tasks using rework, omissions, total time, and actual usage; do not claim efficiency gains without task evidence. Keep records local.

## Native Agents

Pass the listed model and reasoning settings, a bounded task, and rule entry points. If unsupported, report the limitation and fall back by role. Do not start another Root.

## Sol / Luna CLI

First verify `codex exec --help` and host model support. These read-only Worker examples do not change the current Root or global settings. Verify successful requests and actual task quality separately:

```sh
codex exec --model gpt-6.1-sol -c 'model_reasoning_effort="medium"' \
  --sandbox read-only --ephemeral --cd /absolute/project/path \
  'As a Worker, analyze the specified problem read-only. Return locations, evidence, and open issues without recursive delegation or file changes.'

codex exec --model gpt-6-luna -c 'model_reasoning_effort="high"' \
  --sandbox read-only --ephemeral --cd /absolute/project/path \
  'As a Worker, extract the requested information from the specified files. Return evidence in the agreed format without recursive delegation or file changes.'
```

For actual delegation, supply the goal, scope, acceptance criteria, and rule entry points from the [execution package](agent_selection.md#work-packages-and-parallelism). Use `workspace-write` for write tasks only with existing authorization. Model visibility does not authorize enabling it, and these examples do not prove service availability.

The old Spark CLI example is removed: GPT-5.3-Codex-Spark retired from Codex CLI, the desktop app, and the IDE on 2026-09-14. For a fast, bounded worker, first verify an available 6 Luna or 6.1 Sol. Use `workspace-write` only for an authorized write task; do not disable the sandbox or change the current Root or global configuration.

## DeepSeek Flash / OpenCode

The current official API name for V4.1 Flash is `deepseek-flash` ([model details](https://api-docs.deepseek.com/quick_start/pricing/)); use the provider/model ID actually available in OpenCode. Verify capability, service availability, and tool permissions separately. Code implementation or tests require the corresponding existing write/execution authorization; this routing does not expand example permissions.

Set this up only if selected; do not add a harness or background scheduler. Check `opencode run --help`, configuration, and current service model IDs. Do not treat an alias as a pinned version. On macOS:

```sh
brew install anomalyco/tap/opencode
opencode --version
```

Compare and merge the [example](../../examples/en/opencode.json) into local `~/.config/opencode/opencode.json`, preserving existing JSON/JSONC configuration. It defaults to read-only review with a separate Markdown-only editing role. Sharing, automatic updates, shell, content search (`grep`), recursive delegation, and implicit Skills are disabled; direct `read` access to common credential paths is denied. Path denials for `read` do not protect other content-reading channels. If search is needed, enable it only within a screened task copy without sensitive material; file-path denial rules cannot simply be copied to `grep`, which authorizes query regexes. Root must bound permissions for tests or extra tools rather than allow everything.

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

Do not probe without credentials. Verify installation, visible metadata, successful requests, and task results separately. After the minimal request succeeds, check document reading, locations, and role permissions with non-sensitive material. Use synthetic markers to check both roles’ read and search restrictions for allowed documents and forbidden files, recording the installed version, effective configuration, and results. Never test with real credentials; static configuration checks do not establish runtime enforcement:

```sh
opencode run --agent workflow-review --format json \
  --dir /absolute/project/path \
  'Review the specified documents in read-only mode. Return locations and evidence, and do not delegate recursively.'
```

Official references: [CLI](https://opencode.ai/docs/cli/) · [permissions](https://opencode.ai/docs/permissions/) · [configuration](https://opencode.ai/docs/config/).
