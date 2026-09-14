<a id="engineering-review-guidelines-for-ai-agents"></a>

# Review

[简体中文](../review.md) · **English** · [Documentation](../../README.en.md#guides)

Review contracts and risks, then report findings with traceable evidence.

<details>
<summary>On this page</summary>

- [Scope and depth](#scope-and-depth)
- [Establish the contract and reconstruct affected behavior](#establish-the-contract-and-reconstruct-affected-behavior)
- [Audit implementation and cross-module flows](#audit-implementation-and-cross-module-flows)
- [Verify external semantics when correctness depends on them](#verify-external-semantics-when-correctness-depends-on-them)
- [Audit tests and choose independent validation](#audit-tests-and-choose-independent-validation)
- [Use runtime evidence for runtime claims](#use-runtime-evidence-for-runtime-claims)
- [Examine complexity without inventing findings](#examine-complexity-without-inventing-findings)
- [Classify and report findings](#classify-and-report-findings)
- [Review outcome and handoff](#review-outcome-and-handoff)

</details>

## Scope and depth

Follow the shared rules in [engineering.md](engineering.md). Review the change, design, module, or repository requested by the user at a depth proportionate to risk. The goal is a concrete assessment of correctness, affected contracts, and evidence gaps.

For a change review, start with the diff and trace affected callers, dependencies, and observable behavior. Inspect unchanged code when evaluating the change requires it; do not turn every review into a repository-wide audit. Distinguish issues introduced by the change from those that already existed. List unrelated findings separately unless they block the requested result.

For an explicitly requested repository audit or a broad structural change, reconstruct the relevant system and inspect important cross-module flows. For a design review, evaluate proposed contracts and assumptions without demanding runtime evidence from code that does not yet exist; state which validation it will require.

Use the sections below as a risk-driven workflow. Check the author's risk classification against failure consequence, impact reach, recovery, and uncertainty; do not equate a small or nonstructural change with low risk. A small review may combine steps and omit irrelevant checks. Changes involving ownership, concurrency, trust/authorization boundaries, persistent data, external effects, or compatibility require corresponding deeper analysis. Do not infer a defect merely from coding style, AI authorship, or the existence of an abstraction.

Default output should be concise: findings ordered by severity, important uncertainties, validation performed, and, when applicable, the review outcome. Use an extended report only when the requested audit depth warrants it.

## Establish the contract and reconstruct affected behavior

Use the [shared source rules](engineering.md#intended-behavior-and-source-authority) to establish the accepted contract independently of the patch. Even when documentation, implementation, and tests agree, check whether their interpretation shares an unsupported assumption.

Audit the acceptance baseline: does it cover affected guarantees, is the change justified, and which missing results would block acceptance? If no baseline was recorded, reconstruct one from the contract and risk and note unresolved decisions. Do not define success solely by passing tests.

Reconstruct enough of the system to explain:

- The result the change must establish and what must remain unchanged.
- Participating components, data/control flow, and externally observable effects.
- Resource ownership, lifetime dependencies, and state transitions.
- Threads, tasks, callbacks, and process boundaries on affected paths.
- Initialization, normal operation, shutdown, and relevant failure behavior.

Trace important end-to-end paths, for example:

```text
API → validation → state change → worker → storage/transport
    → completion/error → cleanup → external observation
```

Distinguish observed behavior from behavior predicted by static reasoning. Mark assumptions and unknown ordering rather than presenting them as measured facts.

List only invariants that affect the change. For example: a worker must not access a resource after it becomes invalid; accepted work must not be silently lost; cleanup responsibility must be defined; transitions must follow the accepted state model. Verify that each proposed invariant belongs to the contract; do not assume every system shares one ownership or recovery model.

## Audit implementation and cross-module flows

Check affected paths against the contract and invariants:

| Area | Review questions |
| --- | --- |
| Correctness | Are outputs, branches, preconditions, and state transitions correct for supported inputs? |
| Ownership | Who creates, owns, borrows, transfers, and destroys resources? Can a reference outlive its required lifetime? |
| Lifetime | What happens during partial initialization, reuse, shutdown, restart, and recreation? |
| Concurrency | What establishes execution order? Are shared state, locks, callbacks, cancellation, and task lifetimes coordinated? |
| Errors | Where do errors propagate? Can partial success be reported as full completion? Are retry, timeout, rollback, and cleanup semantics valid? |
| Resources | Can memory, threads, handles, sockets, files, registrations, or external state leak or remain stale? |
| Compatibility | Are supported callers, versions, configurations, data schemas, and protocol wire formats preserved or intentionally migrated? |
| Trust and sensitive data | Are validation, identity, authorization, and isolation enforced at the proper boundary? Can protected data leak through responses, errors, logs, caches, or external calls? |
| Data/protocol transition | Can supported old and new states and participants coexist or upgrade in the required order? What happens on interruption, repetition, rollback, or roll-forward? |
| Performance | Does the affected critical path add material copying, allocation, blocking, contention, or other measured cost? |

Look for cross-boundary failures: information lost during error conversion, ambiguous transfers of cleanup responsibility, state mutation before validation, or callbacks that continue after shutdown. Individual local functions may look plausible while their composition violates the contract.

Compare with relevant repository patterns. Identify duplicate cleanup, retry, serialization, configuration, or synchronization mechanisms, but report divergence as a defect only when it has a concrete consequence. An existing pattern may itself be unsuitable.

For an important defect fix, inspect why the original failure could occur, which invariant was violated, whether the fix acts at the responsible boundary, and whether the causal path remains possible. If the mechanism is unknown, recommend the necessary investigation under [debugging.md](debugging.md); do not call a workaround a validated root-cause fix.

<a id="check-external-semantics-where-correctness-depends-on-them"></a>

## Verify external semantics when correctness depends on them

Identify important assumptions about language behavior, library callbacks, cancellation, destruction, memory ordering, OS resources, protocols, databases, or device APIs. For subtle or uncertain assumptions, verify them with authoritative documentation, dependency source, or a focused experiment applicable to the installed version and configuration.

Repository comments and passing tests do not establish every upstream guarantee. Conversely, a generic current documentation page may not describe the version in use. Record relevant sources/versions and important limits. If verification is unavailable, keep conclusions that depend on the assumption qualified.

<a id="audit-the-tests-and-choose-independent-validation"></a>

## Audit tests and choose independent validation

Review existing tests as code. Determine which accepted behaviors they establish, where expected results come from, and which meaningful incorrect implementations they would reject.

A weak oracle copies a complex implementation or derives its expected result from the same code under test. A simple expression such as `a + b` can be a valid oracle when it follows from an independently defined contract. Syntactic similarity alone does not make a test circular; the issue is whether it shares an unverified assumption.

For important behavior, perform a thought-mutation check: would the tests fail if cleanup were removed, an error dropped, a transition skipped, synchronization omitted, or success returned without completing work? Record gaps that affect the outcome. Actual mutation testing is optional; it should be isolated, reversible, and justified by needed evidence.

For a reproducible fix, inspect the before/after regression evidence described in [coding.md](coding.md). Confirm that the unfixed failure targets the defect and that the post-fix run uses a comparable scenario. If comparison is unavailable, evaluate the stated reason and alternative causal evidence rather than inferring regression sensitivity from one passing test.

For test changes, determine whether the old expectation was wrong, an authorized behavior change superseded it, or a refactor changed only test setup. Look for weakened assertions, removed cases, retries, overly broad ranges, inflated timeouts, skipped flaky tests, and mocks that remove affected behavior. These require explanation rather than blanket rejection.

Derive additional scenarios from the contract and risk instead of merely copying the author's tests:

| Risk | Useful scenarios |
| --- | --- |
| Input boundaries | Null/empty, zero, extreme, duplicate, malformed, or unsupported input |
| Lifetime | Partial initialization, repeated close, recreation, active work during shutdown |
| Failure and recovery | Dependency unavailable, timeout after partial work, resource exhaustion, restart |
| Concurrency and timing | Simultaneous operations, delayed callback, cancellation, changed execution order |
| Distributed behavior | Loss, delay, duplication, reordering, partition, peer disappearance or restart |
| Compatibility | Supported old and new consumers, persisted data, external peers |
| Trust and isolation | Allowed and denied access, cross-user/tenant scenarios where applicable, protected data leaking through secondary outputs |
| Data transition | Existing records, old and new formats, interrupted or repeated conversion, supported recovery or roll-forward |

Choose scenarios that can change the review conclusion. Do not require an unrelated local change to cover every category.

## Use runtime evidence for runtime claims

Distinguish properties supported by static reasoning from those that require execution. Calling cleanup or setting an internal STOPPED flag may not establish that an OS resource disappeared or that a remote observer sees the expected state.

Run the smallest checks needed for the review: select builds, focused tests, integration checks, reproducers, or lifetime/stress runs as appropriate. Inspect processes, threads, descriptors, sockets, registrations, memory, logs, or timing only when they answer a concrete question.

Use sanitizers, race detectors, profilers, debuggers, and system tracing according to the suspected mechanism. One clean tool run does not establish that a defect is universally absent. Instrumentation can alter behavior; account for that when interpreting timing-sensitive results.

Report what actually ran and, when material, the version/environment and result. A proposed test is not an executed test. If necessary runtime evidence cannot be collected, state the missing prerequisite and its effect on the recommendation. Avoid unnecessary repeated testing once the relevant evidence is sufficient.

## Examine complexity without inventing findings

Inspect whether a new layer carries a responsibility or merely forwards calls; whether flags encode contradictory states; whether a fallback hides an internal defect; whether a compatibility branch serves a supported scenario; and whether comments promise guarantees the implementation does not provide.

Names such as Manager, Factory, Service, or Adapter are not findings by themselves. A finding requires a concrete cost or failure: duplicated authority, ambiguous cleanup, an incorrect dependency direction, unnecessary state, or an affected performance constraint.

For failure handling, ask what happens when an operation occurs twice, arrives late, happens partially, or never happens. Determine whether the required result is safe completion, clear failure, rollback, cleanup, or recovery. Do not impose recovery semantics the system never promised.

## Classify and report findings

A finding should identify the concrete problem, trigger, consequence, location, and supporting evidence. Suggest a repair direction and useful validation when they are not obvious. Avoid vague recommendations such as “add more tests” or “improve the architecture.”

Distinguish these dimensions:

| Dimension | Values and meaning |
| --- | --- |
| Severity | Critical: severe consequences such as data loss or widespread unavailability; High: material correctness/reliability impact under realistic conditions; Medium: limited impact or narrower triggers; Low: minor but concrete impact |
| Type | Implementation, architecture, contract, test/validation gap, or external semantics |
| Confidence | Verified, Reasonably Supported, or Uncertain, using the shared evidence definitions |
| Blocking | Yes or no, with a reason based on task acceptance criteria and project review rules |

Severity describes consequence and likelihood; uncertainty describes evidence. A validation gap may itself have high severity, while an uncertain concern cannot be presented as a confirmed defect. For a gap, explain which property remains unverified and why failure of that property matters. Keep speculative concerns without a concrete, evidence-supported scenario as open questions rather than padding the findings list.

A concise finding format is:

```text
[Severity] Title — file:line
Trigger and expected behavior; observed or predicted failure and consequence.
Evidence and confidence; type, and whether it blocks the requested result.
When useful, repair direction or missing validation.
```

Use the smallest relevant location. For a complex issue, include the reproduction sequence or cross-module path. If a failure comes from static inference, do not claim it was observed.

## Review outcome and handoff

For an implementation review that requires a recommendation, use:

| Outcome | Meaning |
| --- | --- |
| APPROVE | Relevant checks support the requested scope, with no remaining blocking finding or evidence gap |
| APPROVE WITH NON-BLOCKING FOLLOW-UPS | Current acceptance criteria are met; concrete follow-up items remain |
| REQUEST CHANGES | Evidence supports a defect or unmet requirement that blocks acceptance |
| INSUFFICIENT EVIDENCE | A necessary decision or validation is unavailable, so an acceptance conclusion cannot be established |

Approval applies only to the reviewed version and evidence; it is not a claim that no defect can exist. Align the result with the acceptance baseline and the review intensity required by risk. When scope includes migration or release, validate readiness and distinguish it from the operation actually having been performed. A recommendation does not merge or publish anything. For design reviews or informational audits, state the appropriate readiness assessment rather than forcing a merge recommendation.

List findings first, ordered by severity. Then state assumptions, important gaps, and validation performed. If there are no findings, say so explicitly and identify remaining limitations. A large audit may also need a system model, invariant assessment, test audit, and verified upstream dependencies; include them only when useful.

Route follow-up work under the shared guide: local defects to coding, structural defects to design, unknown causes to debugging, and disputed expectations to contract clarification. Preserve evidence and uncertainty in the handoff. Stop when the requested scope has been evaluated and important findings and gaps are clear; do not search unrelated areas merely to produce more findings.
