# Agent Engineering Workflow

[简体中文](README.md) · **English**

**Clear constraints, actionable steps, and verifiable outcomes for agent engineering tasks.**

A reusable set of guides for design, implementation, debugging, review, and multi-agent collaboration. Shared methods stay in this repository, project facts stay in each project, and personal configuration stays on your machine.

[Quick start](#quick-start) · [Guides](#guides) · [Local setup](#shared-content-and-local-setup) · [Maintenance](#validation-and-maintenance)

- **Read what you need** — Start with a task and load only the guides relevant to its current stage.
- **Keep responsibilities clear** — The current Root makes architectural decisions and accepts the final result. Workers execute bounded tasks and return evidence.
- **Use it across projects** — Ordinary tasks can use the current Root alone. Add other models and tools when needed.

## Quick start

1. Clone this repository into a location you intend to keep.
2. Read the rules. Replace `<WORKFLOW_REPO>` in the [global entry template](examples/en/global-AGENTS.md) with the repository's absolute path, then merge it into `~/.codex/AGENTS.md`. Preserve existing personal configuration.
3. The minimum setup uses only the current Root; OpenCode and additional models are optional. Before using other executors, record enabled services, permitted material, and constraints in the local entry. See `docs/en/model_profiles.md` for defaults. Host capabilities and permissions still apply.
4. Check that the shared entry is reachable. Validate each selected CLI and model with a small task that has a clear expected result. Installation does not prove model calls work. The current Root can handle ordinary tasks; if required independent review has no available reviewer, retain the acceptance gap under `docs/en/engineering.md`.
5. Start a new Codex session and verify that the global entry was loaded. If you set `CODEX_HOME`, use that location and check whether `AGENTS.override.md` takes precedence.

Keep personal paths in the local entry, outside this repository. Do not symlink the full repository AGENTS file into the global location: the local entry needs machine-specific information and must resolve guide references from their own directories. See the [official Codex loading rules](https://learn.chatgpt.com/docs/agent-configuration/agents-md).

After an update, inspect changes to model and permission semantics before using them in subsequent tasks. Updating documents does not dynamically reload host instructions or synchronize CLI configuration.

When upgrading from the old flat layout, shared guides have moved to `docs/` and the blank log template to `examples/`. The default machine entry still points to root `AGENTS.md`; update any direct references to `docs/model_profiles.md`, `docs/agent_selection.md`, and `examples/workflow_evolution_log.md`. Keep the actual private log location unchanged. For English guides, use the corresponding paths under `docs/en/` and `examples/en/`, as shown in the English template.

### Use it in a project

Open a new Codex session in the target project and verify setup with this read-only task:

> List the active global and project instruction sources. Read the shared AGENTS.md referenced by the local entry, verify that guide paths are reachable, and explain which guides this task needs. Do not modify files.

The result should identify the local entry, shared repository, and existing project rules without treating `<WORKFLOW_REPO>` as a real path. Fix local paths if the entry cannot be reached. Other CLIs need their own instruction-loading setup; do not assume they read Codex configuration.

Then describe the outcome and acceptance criteria: “Implement X and validate it,” “Find and fix the cause of X,” or “Review the current changes and report evidence.” The agent loads the relevant methods through the shared entry; you do not need to paste every guide into each task.

To establish the necessary conventions in an existing project:

> Follow the existing-project path in docs/en/project_workflow.md. Check this project's rules, requirements, build, and test entry points. Preserve existing conventions and fill the necessary gaps.

Projects maintain their concrete facts and constraints. Shared methods stay here. Skill activation follows the [Agent entry](docs/en/AGENTS.md#skill-use).

## Guides

Start at the [Agent entry](docs/en/AGENTS.md) and choose by task. You do not need to load every detailed rule at once.

| What you need to do | Guide |
| --- | --- |
| Choose process depth, evidence, and completion criteria | [Engineering principles](docs/en/engineering.md) |
| Make structural and architectural decisions | [Architecture and design](docs/en/design.md) |
| Implement a defined behavior or fix | [Implementation](docs/en/coding.md) |
| Investigate failures and establish causes | [Debugging](docs/en/debugging.md) |
| Check correctness and acceptance evidence | [Review](docs/en/review.md) |
| Onboard or maintain a project | [Project onboarding](docs/en/project_workflow.md) |
| Delegate, hand off, and recover from executor failures | [Agent collaboration](docs/en/agent_selection.md) |
| Select models and launch settings | [Model settings](docs/en/model_profiles.md) |
| Improve the workflow from observed problems | [Workflow improvement](docs/en/workflow_evolution.md) |

```text
.
├── README.md / README.en.md   # 中文 / English
├── AGENTS.md                 # Default agent entry
├── docs/                     # Chinese guides; English versions in en/
├── examples/                 # Local setup templates; English versions in en/
└── scripts/                  # Offline checks
```

## Shared content and local setup

Use the downloaded or cloned guides directly instead of maintaining a second local copy of their full text. Keep machine, account, and personal adaptations in the local entry and tool configuration outside the repository. Shared rules then have one maintenance source, with no separate local edition to merge on updates.

| Content | Public source | Local use |
| --- | --- | --- |
| General rules, task routing, and methods | `docs/en/AGENTS.md`, `docs/en/engineering.md`, and the specialist guides | Reference directly; maintain general improvements here |
| Default executor preferences | `docs/en/model_profiles.md`, `docs/en/agent_selection.md` | Optional defaults; record enabled or replacement models and permitted material locally |
| Global entry | `examples/en/global-AGENTS.md` | Replace placeholders and merge into `AGENTS.md` in Codex home |
| OpenCode role examples | `examples/en/opencode.json` | If using OpenCode, merge into effective configuration outside the repository and adapt paths and models |
| Review log template | `examples/en/workflow_evolution_log.md` | Copy outside the repository when needed; keep the source blank |
| Project constraints, build, and test entry points | Maintained by each project | Keep in that project's `AGENTS.md` or existing documentation |

Copy only templates that need a local instance. Do not put real machine paths, account status, credentials, or personal task records in public files. Paths such as `~/.codex` describe defaults; `<WORKFLOW_REPO>` is a manual replacement marker. Use the actual locations for your platform, `CODEX_HOME`, and tool configuration. Copying the entry does not require rewriting relative links in the shared guides.

## DeepSeek setup

<details>
<summary>Optional: configure a DeepSeek Worker through OpenCode</summary>

This integration is optional and is not required to use the shared documents.

The default integration uses the official DeepSeek API through a bounded OpenCode Worker. If OpenCode is needed on macOS, use its official Homebrew source:

```sh
brew install anomalyco/tap/opencode
opencode --version
```

Merge the [configuration example](examples/en/opencode.json) into `~/.config/opencode/opencode.json`. Compare existing JSON/JSONC configuration first; do not overwrite it. The example contains no credentials, defaults to `deepseek/deepseek-flash`, provides `workflow-review` and `workflow-edit`, and disables session sharing and automatic updates.

For use across projects, allow the shared repository's exact absolute path in the global and both roles' `permission.external_directory` settings in your **local configuration**; `<WORKFLOW_REPO>/*` illustrates the placeholder form. In the editing role, deny that same path in `permission.edit`, after the general Markdown allow rules. Keep real personal paths out of the public example. Root provides required guide entry points in the task; local `instructions` can also load the shared AGENTS file.

The default role is read-only. The editing role permits only Markdown edits. Both explicitly deny reads of `.env`, credential JSON, key files, and common credential directories, and disable shell, recursive delegation, and Skill tools. Root must define scope and tool permissions separately for tests. Project configuration may override global settings, so check effective configuration before delegating. These controls are not an OS sandbox. See [configuration merging](https://opencode.ai/docs/config/) and [permissions](https://opencode.ai/docs/permissions/).

### Enter an API key

Run this in your local terminal:

```sh
opencode auth login
```

Select **DeepSeek** and paste the API key into the interactive field. Alternatively, start `opencode`, enter `/connect`, and select DeepSeek. Do not put the key in command arguments, chat, AGENTS files, or a repository `.env`.

The default credential file is `~/.local/share/opencode/auth.json`. It is local file storage, not an encrypted vault. Restrict access after entering the key:

```sh
chmod 600 ~/.local/share/opencode/auth.json
opencode models deepseek
```

Use the actual credential path if you customize the XDG data directory. The model list proves only that metadata is visible. Validate a call with a minimal request:

```sh
opencode run --agent workflow-review --model deepseek/deepseek-flash \
  --format json 'Do not call any tools. Reply only READY.'
```

After this succeeds, use a non-sensitive document to check reading, result locations, and role permissions. Connectivity and task quality remain unverified before the key is entered. See the [official CLI documentation](https://opencode.ai/docs/cli/).

</details>

## Privacy and local records

- Keep real credentials, personal absolute paths, private task or schedule identifiers, account status, and personal history out of public files.
- The [review log](examples/en/workflow_evolution_log.md) is a blank template. Keep actual records outside the repository and register their location in the local entry.
- `.gitignore` helps exclude local state. Still inspect staged files and Git history before publishing; ignore rules are not a secret scanner.
- Recurring reviews require explicit scheduling by the user. This repository does not create automations, background services, or timers.

## Validation and maintenance

This project delivers shared documents and configuration templates; there is no product service to start. This README owns usage and scope, the guides under `docs/` own general policies, and root `AGENTS.md` provides the default maintenance entry. `examples/` contains templates to instantiate locally, avoiding separate local copies of the rule set.

With Python 3 installed, run the offline check from the repository root. No third-party dependencies or API credentials are required:

```sh
python3 scripts/check_docs.py
```

The [checker](scripts/check_docs.py) covers Markdown in the root, `docs/`, and `examples/`, plus JSON in `examples/`. It checks local links, anchors, fences, JSON syntax, bilingual file pairs, and common personal-path and credential patterns. It exits nonzero on failures. It is not a complete Markdown renderer or secret scanner, does not check external URLs, and does not read local configuration.

| Change | Required validation and evidence |
| --- | --- |
| Markdown and example JSON | Run the checker; inspect affected headings, tables, and rendered structure; review the diff |
| Setup steps or templates | Replace placeholders in a temporary directory outside the repository and check guide reachability; validate actual host loading and tool calls separately |
| Shell examples | Check syntax of affected blocks; record actual results when executing commands that depend on tools, permissions, or services |
| Model routing, permissions, or acceptance rules | Arrange independent review in addition to static checks; validate relevant behavior for runtime guarantees |
| Publication preparation | Inspect actual staged files and Git history for personal information; ignore rules and scripts do not replace human review |

Associate results with the version changed. Keep personal run logs and historical evidence outside the repository. Update each general rule at its authoritative source; users compare and merge template updates into local configuration without automatic overwrites. Static checks do not replace actual CLI/API or engineering-task validation. Completion follows `docs/en/engineering.md`.

Update both languages in the same rule change. Preserve existing anchors and technical identifiers. Use one language per task without loading the translation again. Write commit messages in English, for example `docs: improve navigation and add English translations`; do not automatically rewrite published history.
