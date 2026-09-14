# Agent collaboration

[简体中文](../agent_selection.md) · **English** · [Documentation](../../README.md#guides)

This file defines delegation, isolation, and fallback. Review triggers live in [engineering.md](engineering.md#independent-review-policy); models are in [model_profiles.md](model_profiles.md). It grants no permission and is not a scheduler.

## Single Root and executors

- The current Agent is the sole Root. Keep its model. It owns requirements, architecture tradeoffs, decomposition, and final acceptance; start no other Root.
- Workers perform bounded work and return evidence.
- Enabled executors remain within existing authorization. A clone, installed CLI, or visible model does not authorize data disclosure.
- Delegation does not authorize installation, sign-in, budget increases, global changes, commits, or publication; do not bypass refusal.

## Delegation choices

- Choose by whole-task size, risk, and independence. Prefer a matching Worker for a substantial package; Root decides and verifies evidence.
- Root may do simple low-risk work without an independence need. Cross-file reading does not require delegation.
- Required independent review must be a separate assessment in a fresh context; Root self-review is not a substitute.
- Do not fragment work or delegate ceremonially afterward. Default to one Worker. Parallelize only independent, useful work; serialize writes without reliable isolation.

## Work packages and parallelism

- Root supplies objective, scope, exclusions, contract, acceptance, directory, rules, and delivery format, and verifies access.
- Send only necessary material, never the full conversation or credentials. Do not assume executors inherit context.
- Parallel writes use isolated copies/worktrees. Tests isolate ports, data, processes, and logs. Do not clean others' resources.
- Workers do not recursively delegate, start a Root, commit/push/merge, or change global configuration. Return contract-changing evidence to Root.
- Tool prompts are not an OS sandbox. External CLI side effects remain within authorization.

## Minimum task brief and result

Workers return conclusions, changes, checks, and unresolved items. Include commit+diff or snapshot/hash, needed environment, actual commands/results/exit codes, locatable raw results, and acceptance items/gaps/limits/version. Mark unknowns; keep sensitive evidence in an allowed private location.

Root checks critical paths and final diff; add checks when evidence or version changes. Record actual CLI/model/reasoning; request parameters do not prove application.

## Queueing and availability fallback

- Distinguish invisibility, missing entry point, authentication/quota, permission refusal, queueing, and slowness.
- Replace only after the request ends or cancellation is confirmed. Timeout/silence does not prove termination. Retain and query its ID; do not duplicate work.
- Allow at most two availability substitutions per subtask. Choose an authorized executor by role; do not poll fixed lists or repeat shared failures.
- Do not retry after quota exhaustion. Do not claim Spark is unsupported without checking or probe DeepSeek without credentials.
- After substitutions, Root executes. If independent review is unavailable, retain the gap.
- Fallback must not bypass permission, data disclosure, or budgets. Ask only for a missing required permission, decision, or capability.

## Conducting independent review

- Reviewer uses a fresh context with problem, contract, patch, acceptance, and evidence, without author reasoning/self-evaluation. A different model is not independence.
- Select a Reviewer from the model table. Root verifies material findings and retains the final decision.
- Default to initial and post-fix review. Continue fixes and explain extra rounds. An unrechecked final version cannot pass.
- If independent review is unavailable, continue self-checks and state the limit. Record an exception when the user accepts residual risk.

## Failures and escalation

Resolve tool, scope, context, and validation prerequisites first. Change model/reasoning only for concrete quality evidence; state reason and acceptance, and do not silently alter user settings. Allow at most two quality escalations per subtask, then Root reassesses. The two limits cannot bypass each other.

## CLIs, permissions, and records

Use only installed, configured, authorized entry points; verify parameters after upgrades. Record model visibility, request success, and task success separately. Do not guess capacity, tokens, cost, or settings. Keep records local.

## Stop conditions

Stop at acceptance; do not extend work to add Workers. Preserve gaps and do not claim false success.
