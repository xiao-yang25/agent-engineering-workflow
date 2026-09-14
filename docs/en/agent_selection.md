# Agent collaboration

[简体中文](../agent_selection.md) · **English** · [Documentation](../../README.en.md#guides)

Bound responsibilities and pass context so execution and acceptance have clear owners.

<details>
<summary>On this page</summary>

- [Single Root and executors](#single-root-and-executors)
- [Delegation choices](#delegation-choices)
- [Work packages and parallelism](#work-packages-and-parallelism)
- [Minimum task brief and result](#minimum-task-brief-and-result)
- [Queueing and availability fallback](#queueing-and-availability-fallback)
- [Conducting independent review](#conducting-independent-review)
- [Failures and escalation](#failures-and-escalation)
- [CLIs, permissions, and records](#clis-permissions-and-records)
- [Stop conditions](#stop-conditions)

</details>

This document defines delegation, handoffs, isolation, and fallback behavior. Risk and independent review triggers are defined in [engineering.md](engineering.md#independent-review-policy); model preferences are in [model_profiles.md](model_profiles.md). This document is not a scheduler and grants no additional permissions.

## Single Root and executors

- The Agent opened by the user is the sole Root. It owns requirements, architecture tradeoffs, task decomposition, and final acceptance. Keep its current model; do not start another Root.
- Workers perform bounded investigation, implementation, testing, documentation, and review, and return evidence that can be located and inspected.
- Executors explicitly enabled by the user may continue working within existing authorization. Cloning a repository, installing a CLI, or seeing a model does not authorize sending project material to a service.
- Delegation grants no additional permission to install software, sign in, increase budgets, change global configuration, commit, or publish. A refusal must not be bypassed by changing models or disabling approval checks.

## Delegation choices

Base the decision on the size, risk, and independence of the whole task, rather than mechanically triggering delegation from file counts or action counts.

- Prefer a Worker with the matching role for a substantial investigation, implementation, or complete validation package that can be delegated coherently. The Root handles decisions and verifies the evidence.
- The Root may complete simple, low-risk, well-bounded work that has no independence requirement. Reading across multiple files does not by itself require delegation.
- Independent review required by the rules must be a separate assessment in a fresh context; Root self-review is not a substitute.
- Do not fragment work merely to demonstrate collaboration, or complete the whole task in the Root and then add ceremonial delegation. Run work in parallel only when it can proceed independently and provides a real benefit.
- Use one Worker by default. The host's concurrency limit and available isolation constrain the count. If write isolation is unreliable, run Workers sequentially.

## Work packages and parallelism

- The Root provides the objective, file scope, exclusions, accepted contract, acceptance scenarios, and delivery format. One Worker may carry a tightly related investigation, implementation, and self-test through to completion.
- Provide the working directory and applicable rule entry points, and verify that they are reachable. Do not assume that native Agents, CLIs, or remote executors inherit the same context. Send only necessary material, never the full conversation or credentials.
- Parallel writes use isolated copies or worktrees. Tests must also isolate ports, data, processes, and logs. Do not clean up resources owned by other tasks.
- Workers do not delegate recursively, start a Root, commit, push, merge, or change global configuration on their own. Return new evidence that would change the contract to the Root for a decision.
- Tool permissions and read-only prompts are not an OS sandbox. File, shell, network, and logging side effects from external CLIs remain subject to the task's authorization.

## Minimum task brief and result

A Worker returns its conclusions, change locations, checks actually run, and unresolved issues.

| Item | Minimum requirement |
| --- | --- |
| Subject | Commit plus uncommitted diff, or a snapshot/hash; relevant environment versions when needed |
| Execution | Actual commands, results, exit codes, and environment; mark unknown fields explicitly |
| Raw results | A locatable report or log; keep sensitive evidence in an approved private location |
| Acceptance mapping | Corresponding acceptance items, gaps, limitations, and the version reviewed |

The Root checks critical paths and the final diff and reuses sufficient evidence. Add checks when evidence is missing or conflicting, the version changed, or risk requires them. Report the actual CLI/model and reasoning setting; request parameters alone do not prove that the service applied them.

## Queueing and availability fallback

- Distinguish an unavailable model, missing entry point, authentication or quota failure, permission refusal, explicit queueing, and an ordinarily slow response.
- Replace a request only after it has ended or its cancellation is confirmed. A timeout or lack of output does not prove that background work stopped. If uncertain, retain the session identifier and query it instead of starting a duplicate.
- Choose an authorized, available substitute that can perform the same role; do not poll every model in a fixed order. Allow at most two availability substitutions for each subtask, and do not make pointless requests when the candidates share the same failure.
- Do not retry the same entry point after its quota is exhausted. Spark CLI is separate from the native model menu; do not claim it is unsupported without checking. Do not probe DeepSeek without credentials.
- After substitutions are exhausted, a capable Root continues with ordinary execution. If required independent review is unavailable, retain the acceptance gap instead of claiming complete acceptance.
- Do not use fallback behavior to bypass permission, data disclosure, or budget limits. Request user input only when a required permission, decision, or irreplaceable capability is missing.

## Conducting independent review

- The Reviewer uses a fresh context and receives the problem, contract, patch, acceptance criteria, and actual evidence, without the author's reasoning or self-evaluation. A different model alone is not sufficient for independence.
- Select Astra / low or an eligible substitute according to the model table. The Root verifies important findings and retains the final decision.
- Use two rounds by default: initial review and post-fix review. Continue necessary fixes while issues remain, and state the scope and reason for any additional review. A final version that was not rechecked cannot be marked as passed.
- If independent review is unavailable, continue useful self-checks and state the limitation. Record an exception if the user accepts the residual risk.

## Failures and escalation

Resolve tool, scope, context, and validation prerequisites first. Adjust the model or reasoning effort only when there is concrete evidence of insufficient quality; do not silently change settings chosen by the user. State the reason and acceptance requirement for each escalation. Limit a subtask to two escalations, then have the Root reassess. Quality escalation and availability fallback cannot be used to bypass each other's limits.

## CLIs, permissions, and records

Use only installed, configured, and authorized entry points. After an upgrade, verify parameters against the help output. Record model visibility, request success, and task success separately. Do not guess context capacity. Keep run records and usage data locally; mark unknown token counts, costs, or settings as unknown.

## Stop conditions

Stop when acceptance is met; do not prolong a task merely to add Workers. Preserve required gaps, and do not claim that cancellation, configuration, or validation succeeded when it did not.
