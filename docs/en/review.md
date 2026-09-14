<a id="engineering-review-guidelines-for-ai-agents"></a>

# Review

[简体中文](../review.md) · **English** · [Documentation](../../README.md#guides)

Review contracts and risks; report traceable findings and evidence.

## Scope and depth

Follow [engineering.md](engineering.md). Review the requested change, design, module, or repository in proportion to risk. For a change, start with the diff and trace affected callers, dependencies, and observable behavior. Inspect unchanged code when needed, without turning every review into a repository audit. Separate introduced from pre-existing issues.

For a design review, assess contracts, assumptions, and required validation; do not demand runtime evidence from code that does not exist. Ownership, concurrency, trust/authorization, persistent data, external effects, and compatibility require corresponding depth. Small size, a nonstructural change, style, AI authorship, or an abstraction alone proves neither low risk nor a defect.

Default output is concise: findings ordered by severity, material uncertainty, validation performed, and an outcome when applicable.

## Establish the contract and reconstruct affected behavior

Use the [source rules](engineering.md#intended-behavior-and-source-authority) to establish the contract independently of the patch. Check whether the acceptance baseline covers affected guarantees and which missing results block acceptance. Reconstruct it from contract and risk when absent; passing tests alone do not define success.

Build enough of the system model to explain required and unchanged results, components and data/control flow, external effects, resources and lifetime, state transitions, thread/task/callback/process boundaries, and initialization, operation, shutdown, and relevant failure behavior.

Separate observation from static inference; label assumptions and unknown ordering. List only invariants that belong to the contract and affect the change. Do not impose one ownership or recovery model on every system.

## Audit implementation and cross-module flows

Check the contract across:

| Area | Core question |
| --- | --- |
| Correctness | Are supported inputs, outputs, branches, preconditions, and transitions correct? |
| Ownership/lifetime | Are creation, borrowing, transfer, destruction, partial initialization, shutdown, and recreation safe? |
| Concurrency | Are ordering, shared state, locks, callbacks, cancellation, and task lifetimes coordinated? |
| Errors/resources | Are partial success, retry, timeout, rollback, cleanup, resources, and external state handled correctly? |
| Compatibility/transition | Are callers, versions, configuration, schemas, protocols, upgrades, interruption, and recovery supported? |
| Trust/data | Are validation, identity, authorization, isolation, and leaks through output, errors, logs, caches, or calls handled? |
| Performance | Does the critical path add material copying, allocation, blocking, or contention? |

Trace information lost across boundaries, transferred cleanup responsibility, state mutation before validation, and callbacks after shutdown. Divergence from a repository pattern is a finding only when it has a concrete consequence; the existing pattern may also be wrong.

For a material fix, verify the original mechanism, violated invariant, responsible boundary, and whether the causal path remains. If the mechanism is unknown, route necessary work to [debugging.md](debugging.md); do not call a workaround a root-cause fix.

<a id="check-external-semantics-where-correctness-depends-on-them"></a>

## Verify external semantics when correctness depends on them

Identify critical assumptions about language behavior, callbacks, cancellation/destruction, memory ordering, OS resources, protocols, databases, or device APIs. For subtle or uncertain claims, verify against authoritative material, dependency source, or a focused experiment for the actual version and configuration. Record source, version, and limits; qualify conclusions when verification is unavailable.

<a id="audit-the-tests-and-choose-independent-validation"></a>

## Audit tests and choose independent validation

Review tests as code: which contract they establish, where the expected result comes from, and whether they reject meaningful wrong implementations. An oracle must not copy a complex implementation or share its unverified assumption.

For important behavior, ask whether tests fail if cleanup is removed, errors are dropped, transitions or synchronization are skipped, or success is returned before completion. Run mutation testing only when needed, isolated and reversible.

For a reproducible fix, inspect comparable before/after evidence under [coding.md](coding.md). Test changes must explain whether the old expectation was wrong, an authorized behavior replaced it, or only setup changed. Check weakened assertions, removed cases, retries, wider ranges/timeouts, skipped flaky tests, and mocks that remove affected behavior.

Choose scenarios from contract and risk that can change the conclusion: boundaries, lifetime, failures, concurrency, distributed behavior, compatibility, trust/isolation, and data transitions. Unrelated changes need not cover every category.

## Use runtime evidence for runtime claims

Runtime claims require runtime evidence. An internal STOPPED flag does not prove OS-resource release or remote observation. Select the smallest relevant build, test, integration check, reproducer, lifetime/stress run, or resource observation.

Use sanitizers, race detectors, profilers, debuggers, and tracing for the suspected mechanism. One clean run does not prove universal absence; instrumentation may change timing.

Report what ran, the result, and material version/environment details. A proposed test was not executed. If required runtime evidence is unavailable, state the prerequisite and its effect on the outcome.

## Examine complexity without inventing findings

Check whether a layer owns a responsibility, flags encode contradictory state, fallback hides a defect, compatibility code serves a supported case, or comments promise unsupported guarantees. A name or pattern is not a finding. Identify a concrete consequence such as duplicate authority, ambiguous cleanup, wrong dependency direction, needless state, or performance impact.

Ask what happens when an operation repeats, arrives late, happens partly, or never occurs. Require only the contracted outcome: safe completion, clear failure, rollback, cleanup, or recovery.

## Classify and report findings

Each finding states the concrete problem, trigger, consequence, smallest location, and evidence. Add a repair direction and validation when useful. Avoid vague requests for “more tests” or “better architecture.”

| Dimension | Values |
| --- | --- |
| Severity | Critical / High / Medium / Low, by consequence and realistic likelihood |
| Type | Implementation, architecture, contract, test/validation gap, external semantics |
| Confidence | Verified / Reasonably Supported / Uncertain, using shared definitions |
| Blocking | Yes/no, with acceptance and project-rule rationale |

Severity is not confidence. A validation gap may be severe; an uncertain concern is not a confirmed defect. Put speculation without a concrete evidence-backed scenario under open questions. Do not report a statically inferred failure as observed.

## Review outcome and handoff

| Outcome | Meaning |
| --- | --- |
| APPROVE | No blocking finding or evidence gap remains in the reviewed scope |
| APPROVE WITH NON-BLOCKING FOLLOW-UPS | Acceptance is met; concrete nonblocking work remains |
| REQUEST CHANGES | An evidenced defect or unmet requirement blocks acceptance |
| INSUFFICIENT EVIDENCE | A required decision or validation is missing |

The outcome applies only to the reviewed version and evidence. Readiness does not mean migration or release occurred; a recommendation does not merge or publish. Give an appropriate readiness assessment for design reviews and informational audits.

List findings first by severity, then assumptions, material gaps, executed validation, and outcome. If there are no findings, say so and identify limitations. Preserve evidence and uncertainty in handoff: local defects to coding, structural defects to design, unknown causes to debugging, disputed expectations to contract clarification. Stop after the requested scope and material gaps are clear; do not search unrelated areas to manufacture findings.
