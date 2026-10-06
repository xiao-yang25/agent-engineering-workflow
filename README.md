# Agent Engineering Workflow

[简体中文](README.zh-CN.md) · **English**

Engineering guides for agent-driven design, implementation, debugging, and review. Load by task; accept results through evidence.

## Quick start

1. Clone into a stable location. Replace `<WORKFLOW_REPO>` in the copyable body of the [entry template](examples/en/global-AGENTS.md) with the repository's absolute path.
2. Merge it into `~/.codex/AGENTS.md`, preserving existing rules. Use your actual `CODEX_HOME` if customized, and check for an overriding `AGENTS.override.md`.
3. Open a new session in your project. Ask the agent to list loaded rules and verify guide reachability, then describe the task and acceptance criteria.

Ordinary tasks can use the current Root alone. Authorize and validate extra models before use; self-review cannot replace required independent review. Other CLIs need their own rule-loading setup. [Loading rules](https://learn.chatgpt.com/docs/agent-configuration/agents-md)

## Working with the agent

For a simple task, a natural-language request is enough. For complex tasks, add the information below as needed; a full template is not required every time.

- **Start a task:** Explain the purpose, desired outcome, and completion criteria. Provide key materials or an example result, along with important tradeoffs and the permitted scope of operations.
- **Correct course:** Identify specific omissions or deviations and say whether the original goal still applies. Explicitly update any changed goals or constraints.
- **Accept the result:** Try the deliverable in its intended use and judge whether it solves the original problem. The agent performs the work and checks, and reports evidence and gaps; the user need not repeat all validation.
- **Maintain continuity:** Keep lasting personal preferences in the private entry and business constraints in the project; state one-task exceptions in the current task. Reuse one maintained location for each fact. See [documentation and ongoing context](docs/en/project_workflow.md#documentation-and-ongoing-context).

See the [human practices guide](docs/en/user_practices.md) for research, ways to approach delivery/learning/exploration, and their mapping to the existing workflow.

## Guides

| Topic | Documents |
| --- | --- |
| Human practices | [Working with AI](docs/en/user_practices.md) |
| Rules and acceptance | [Agent entry](docs/en/AGENTS.md) · [Engineering principles](docs/en/engineering.md) |
| Daily development | [Design](docs/en/design.md) · [Implementation](docs/en/coding.md) · [Debugging](docs/en/debugging.md) · [Review](docs/en/review.md) |
| Projects and collaboration | [Project onboarding](docs/en/project_workflow.md) · [Agent collaboration](docs/en/agent_selection.md) |
| Execution and improvement | [Model settings](docs/en/model_profiles.md) · [Workflow improvement](docs/en/workflow_evolution.md) |

## Shared content and local setup

`docs/` holds shared guides, `examples/` holds templates, and `scripts/` holds checks. English versions live in each directory's `en/` subdirectory.

Reference the shared text directly; copy only templates that need local adaptation. Keep personal paths, credentials, enabled-service status, and actual logs outside the repository. Project constraints and test commands belong to each project. Resolve references from each guide's directory; do not copy or symlink the full guide set into the global entry.

After updates, compare and merge local templates, then start a new session. Updates do not overwrite configuration or enable schedules. Older root-level guides moved to `docs/`, and the log template to `examples/`; update direct references while keeping the actual private log location unchanged.

<a id="deepseek-setup"></a>

Model routing and optional tool setup: [Astra, 6.1 Sol, Luna, and DeepSeek / OpenCode](docs/en/model_profiles.md).

<a id="privacy-and-local-records"></a>

## Validation and maintenance

```sh
python3 scripts/check_docs.py
python3 -B -m unittest discover -s scripts -p 'test_*.py'
```

Checks cover links, anchors, fences, JSON, bilingual pairs, and common sensitive-data patterns. They do not replace full secret scanning, actual tool calls, or human review. See the [maintenance steps](docs/en/AGENTS.md#public-repository-maintenance).

Update both languages together and write commit messages in English. Inspect staged files and history for personal information even after checks pass. Do not automatically rewrite published history.
