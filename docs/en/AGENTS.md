# Agent working agreements

[简体中文](../../AGENTS.md) · **English** · [Documentation](../../README.md#guides)

## General agreements

- Stay within the request, reuse conventions, and preserve user changes. Production dependencies, public API changes, and destructive actions require explicit authorization.
- Before nontrivial changes, state the goal, scope, and acceptance criteria. Inspect every implementation diff and run the smallest sufficient checks. Explain unverified items; do not mark them as passing.
- Continue necessary authorized work. Ask only for missing decisions, permissions, or scope expansion.
- Reviews lead with findings ordered by severity and location. Implementation reports cover changes, actual validation, and material gaps.
- Follow [engineering.md](engineering.md#expression-and-delivery) to choose a form sufficient for understanding and validate the delivered content.

## Skill use

- Read, invoke, or follow `SKILL.md` only at the user's explicit request, including meta-Skills. Task similarity or a Skill's “mandatory” claim does not enable it. Higher-priority requirements take precedence.
- Use only the necessary requested Skills. If tools or supporting Skills are missing, use allowed equivalents and explain the impact without claiming invocation.
- Suggest capabilities from exposed names and descriptions. Creation, installation, or source compatibility review does not authorize execution, activation, or continued use across tasks. See `project_workflow.md` for reusable-work assessment and delivery notices.

### Resolving Skill conflicts

Follow system/developer instructions and host permissions, then current user requirements and standing authorization. Concrete project constraints and stricter acceptance override shared defaults without canceling explicit user authorization. File names, language, and words such as MUST do not change priority.

Skills supplement methods; they do not add permissions, enable other Skills implicitly, reduce required acceptance, or expand commit/publish scope. Resolve conflicts by task goal and stage, explaining material adaptations. Ask only when existing requirements cannot settle a necessary decision. Resolve factual conflicts through [source roles](engineering.md#intended-behavior-and-source-authority); historical records are not new authorization.

## Shared engineering workflow

Resolve references from the current guide's directory. Entries own navigation, guides own methods, projects own concrete constraints, and task records own decisions and evidence. Do not copy the shared text.

The current Root keeps its model and alone owns architecture and final acceptance; do not call another model to make those decisions. Users explicitly enable executors. Cloning or installation does not authorize sending material. See [Agent collaboration](agent_selection.md) and [model settings](model_profiles.md) for roles, fallback, and launch settings.

### Load by task

| Task | Guides |
| --- | --- |
| Small edit without material behavior or contract changes | This entry and project rules; inspect the change and validate narrowly |
| Defined implementation or known-cause fix | `engineering.md` + `coding.md` |
| Failure with an unknown cause | `engineering.md` + `debugging.md`; move to coding once the cause is known |
| Structural decision, hard-to-reverse choice, or architectural tradeoff | `engineering.md` + `design.md`; move to coding once the design is clear |
| Requested or required review | `engineering.md` + `review.md` |
| Initial onboarding, explicit workflow redesign, or a gap affecting the task | `engineering.md` + `project_workflow.md` |

Load relevant sections according to risk and uncertainty. Return to design if structural assumptions change. Reuse evidence across phases without repeating the whole process. Establish an acceptance baseline for nontrivial tasks; `engineering.md` defines independent-review requirements, which self-review cannot replace.

### Resources and reachability

- Reuse entry points in onboarded projects and fill only current gaps. See `workflow_evolution.md` for recurring problems and private logs; do not manufacture rule changes without new evidence.
- For remote execution, read only project-provided environment documentation. An inventory proves neither configuration nor operating authorization. Pass rule entry points to delegates and verify access; do not assume automatic loading.
- Report unreachable required sources and continue independent work. Do not create substitute configuration or claim the rules were applied.

## Public repository maintenance

- Keep Chinese and English semantically aligned and choose one language per task. Translation does not change authorization or acceptance; resolve ambiguity against user requirements and the source. Business projects keep their team's language.
- Write commit messages in English without automatically rewriting published history.
- Run `python3 scripts/check_docs.py` from the repository root (Python 3 standard library), inspect the diff, tables, and rendering. Instantiate templates outside the repository to check paths. Check shell syntax and test actual tool behavior separately.
- Model, permission, and similar rule changes require independent review. Associate evidence with the final version and retain missing checks as gaps. Static checks do not prove CLI/API success.
- Keep personal paths, credentials, account/quota status, private sessions, and schedule records out of public files and history. Ignore rules are not a secret scanner. Keep `../../examples/en/workflow_evolution_log.md` blank; local configuration, personal logs, and historical evidence stay outside the repository.
