<a id="coding-guidelines-for-ai-agents"></a>

# Implementation

[简体中文](../coding.md) · **English** · [Documentation](../../README.en.md#guides)

Deliver a verified, coherent increment against an accepted contract.

<details>
<summary>On this page</summary>

- [Scope and minimum output](#scope-and-minimum-output)
- [Establish the implementation contract](#establish-the-implementation-contract)
- [Implement and validate coherent slices](#implement-and-validate-coherent-slices)
- [Choose evidence that tests the behavior](#choose-evidence-that-tests-the-behavior)
- [Change tests for a justified reason](#change-tests-for-a-justified-reason)
- [Keep ownership, state, and errors explicit](#keep-ownership-state-and-errors-explicit)
- [Control complexity and refactoring](#control-complexity-and-refactoring)
- [Keep performance evidence concrete](#keep-performance-evidence-concrete)
- [Completion and review handoff](#completion-and-review-handoff)

</details>

## Scope and minimum output

Follow the shared rules in [engineering.md](engineering.md). Use this guide when the required behavior and relevant architecture are sufficiently understood. Route failures with an unknown cause to [debugging.md](debugging.md), and unresolved structural decisions to [design.md](design.md).

Implement the smallest complete change that establishes the required behavior and preserves affected invariants. A complete change may span multiple files; a short diff does not automatically mean the fix is complete.

Before nontrivial work, briefly state the expected behavior, affected paths or invariants, planned changes, and validation. Reuse this statement across increments unless the plan changes materially. At completion, report what changed, what was validated against the final version, and any important limitations. Add architectural changes or intentionally retained technical debt only when relevant; do not produce a full report around every edit.

## Establish the implementation contract

Inspect affected code, callers, tests, repository conventions, and accepted designs. Identify:

- Conditions that must become true and conditions that must remain true.
- The end-to-end paths that will change and their observable effects.
- Accepted boundaries: public behavior, ownership, lifetime, state, concurrency, and dependencies.
- Evidence that distinguishes a correct implementation from a plausible but incorrect one.
- Non-goals that could expand the task if left implicit.

Use the shared risk assessment to select validation depth. Before implementation, establish acceptance scenarios, required evidence, and blocking gaps, and retain them throughout the coding loop. Revisit the baseline only when the contract explicitly changes or new evidence warrants it, and record the reason.

Define behavior without unnecessarily binding it to the current structure. For resource cleanup, “after close, the resource is unavailable and can be safely recreated” is a stronger behavioral requirement than “cleanup() was called.” An internal call count can still be useful when it is itself an accepted contract or part of a focused interaction check, but it does not establish every external effect.

As long as the contract remains unchanged, the organization of private helpers, local algorithms, and internal data structures can usually change. When an accepted architectural assumption fails, state the evidence and necessary boundary change, then use the shared architecture-change process. Do not quietly replace an ownership model or public contract to make implementation easier.

## Implement and validate coherent slices

Prefer completing one end-to-end behavior before building every manager, utility, and infrastructure layer without running any path. For example, first load one model, execute one request, return the result, and release resources. Then cover invalid input, reuse, or close behavior as needed.

Use this loop:

1. Choose one required behavior and identify affected invariants.
2. Define the expected result and an appropriate validation method.
3. Implement the smallest complete change using existing project patterns.
4. Run the smallest relevant build, analysis, test, or runtime check.
5. Inspect the diff and assess added complexity, ownership, state, and error flow.
6. Simplify or refactor within scope when there is a concrete benefit.
7. **If code changes after validation, rerun affected checks against the final version.** If a failure exposes a contract or design problem, return to the phase responsible for it.
8. Record important evidence and gaps; complete the slice when its result is confirmed.

Do not accumulate a large unvalidated subsystem. Do not repeat passing checks unless later changes or an unresolved evidence gap justify it. A local wording or formatting edit may require only focused manual inspection or a documentation check.

## Choose evidence that tests the behavior

Use the [shared evidence table](engineering.md#evidence-and-confidence) to select the smallest checks that establish the changed behavior. Internal flags or call counts alone do not establish external effects.

Derive expected results from accepted behavior, known mathematical results, protocol examples, independent reference data, or another appropriate oracle. A separate observer can verify an external effect but may still share a cache or mistaken assumption; inspect what it actually measures.

Avoid computing the expected value by invoking the implementation under test, and do not duplicate a complex algorithm with the same assumptions. A simple mathematical expression independently derived from the contract is a valid oracle. Independence concerns the source of the expected result, not whether its syntax differs from the implementation.

For important behavior, ask: **Which plausible but incorrect implementation would this check reject?** Useful thought mutations include skipping cleanup, returning success without doing the work, dropping an error, removing synchronization, reusing stale state, or invoking a callback twice. Use actual mutation or fault injection only when it adds necessary evidence and is safe and reversible.

For a reproducible defect fix, normally run the regression check on both the unfixed and fixed versions: it should fail because of the target defect before the fix and pass afterward. Environment setup failures, missing symbols, or unrelated failures do not establish that the test detects the defect. Keep the scenario and relevant environment comparable; use an isolated copy if needed to preserve user work. If this comparison is impractical or unreliable, record why and provide alternative evidence, such as a captured failure trace, controlled reproducer, or causal sequence analysis. A post-fix pass alone does not establish that the check is sensitive to the regression.

Select cases according to the affected behavior: normal input, meaningful boundaries, invalid input, partial failure, repetition, cancellation, concurrent operations, compatibility, and recovery, as relevant. Do not optimize only for test count or coverage percentage. Avoid low-value tests that merely restate unchanged implementation details.

## Change tests for a justified reason

A test failure is evidence to investigate, not an instruction to weaken the assertion. Before changing an expected result, determine which case applies:

- Accepted-contract evidence shows that the existing expectation is wrong.
- An authorized behavior change supersedes an expectation that was previously correct.
- Behavior remains unchanged, but test structure or a fixture must adapt to a legitimate refactor.

Briefly state the applicable reason, preserve coverage of supported behavior, and explain why the revised test still rejects important failures. Do not rewrite requirements to fit the patch.

Scrutinize changes that remove assertions, widen ranges, increase timeouts, add retries, skip flaky tests, delete failing cases, or use a mock to remove an affected dependency. These changes can be valid, but they need behavioral or environmental justification. Do not turn an expected failure into success merely to obtain green CI.

A test may encode an accepted executable specification or a mistaken assumption. Evaluate its authority using the shared source rules instead of treating every test as either absolute truth or worthless.

## Keep ownership, state, and errors explicit

If a change affects access control, a trust boundary, sensitive data, a stored-data format, or a protocol, implement the corresponding boundary and transition decisions from [design.md](design.md). Validation should include relevant denial/isolation, old/new compatibility, and interrupted-transition scenarios. Resolve missing decisions first rather than silently choosing access or recovery behavior; these checks do not authorize a deployment or data migration outside the task scope.

<a id="ownership-and-lifecycle"></a>

### Ownership and lifetime

When a change affects resources, inspect creators, owners, borrowers, cached references, callbacks, asynchronous activity, and cleanup responsibility. A new cached or asynchronous reference may extend the actual lifetime even when the nominal owner remains unchanged.

For shutdown, define when new work stops being accepted, how in-flight work completes, when worker threads and callbacks stop, and when dependents and owners become invalid. Check relevant cases such as partial initialization, repeated or concurrent close, close during work, cleanup failure, and resource recreation.

When needed, verify external cleanup with runtime evidence. An internal null pointer or STOPPED flag cannot establish that a thread exited, a socket closed, shared memory disappeared, or a remote peer no longer observes a registration.

### State and concurrency

Keep authority over state transitions clear. Use an explicit state model for mutually exclusive states and independent booleans for independent properties. Seven flags permit 128 combinations even if only a few are meaningful, so inspect invalid combinations rather than automatically adding another flag.

For each new concurrency element, define its owner, start/stop behavior, cancellation, shared state, synchronization, and lifetime dependencies. Review lock order, queue capacity and backpressure, callback ordering, and work that might continue after its owner becomes invalid. Adding a background worker thread can change the architecture even when it takes only a few lines.

### Error flow and fallback

Trace important errors from origin to caller. Identify cleanup responsibility, partial state, recovery policy, and whether retries are bounded and safe. Look for swallowed errors, lost context, success reported after partial failure, errors logged but not propagated when required, and errors propagated without cleanup.

Before adding a fallback, classify the failure: unsupported input, expected external failure, transient runtime failure, resource failure, internal invariant violation, or programming defect. Falling back from an unavailable GPU to CPU execution is valid only when that behavior is supported. Returning a default object for an impossible internal state may hide a defect.

A timeout, retry, or fallback needs a concrete failure class and an explicit result. It cannot conceal an unexplained race or disguise failure as success.

## Control complexity and refactoring

Assess material complexity introduced by the slice: states, flags, branches, abstractions, dependencies, ownership paths, locks, threads, queues, callbacks, retries, and configuration. Record significant additions and their reasons; do not enumerate every ordinary conditional in user-facing output.

Prefer locally clear authority over state, ownership responsibility, and invariants. Avoid scattering one rule across unrelated flags, callbacks, and helpers.

Repeated special cases are a prompt to reconsider the model. A third material exception in one subsystem is a useful warning, not a numeric rule that automatically requires redesign. Inspect whether the contract, state representation, or responsibility boundary is wrong.

Refactor only when doing so reduces reasoning cost, duplication, or ambiguity within task scope. Do not refactor merely to shorten a function, split a file, add an interface, or apply a pattern. When practical, separate a large refactor from a behavior change so regressions remain diagnosable. State the behavior to preserve and revalidate it after the refactor.

Inspect the final diff for unrelated formatting, opportunistic renames, speculative compatibility branches, unnecessary wrappers, duplicate mechanisms, and comments that promise guarantees the code does not establish. Remove only unrelated changes you introduced; preserve the user's existing edits. Record unrelated issues as follow-ups.

## Keep performance evidence concrete

On affected critical paths, inspect copies, allocations, serialization, locks, blocking I/O, context switches, device synchronization, and transfers. Identify material costs without automatically optimizing them.

Use measurements, hard requirements, known hardware constraints, or strong structural evidence to justify added complexity. Claims of actual latency, throughput, or memory improvements require comparable measurements. Record workload, environment, and meaningful variance rather than relying on one favorable run.

Do not add custom allocators, lock-free queues, caches, batching, zero-copy infrastructure, or asynchronous pipelines for hypothetical bottlenecks. When an expensive behavior conflicts with an established requirement, avoid unnecessarily fixing it into a stable API.

For an accepted material limitation, record its rationale and escalation trigger. For example, loading a model synchronously during startup may be acceptable; reassess when hot loading becomes a supported requirement. A possible future optimization does not require a new subsystem today.

## Completion and review handoff

Use the [shared completion rules](engineering.md#persistent-records-and-completion) to align the final behavior and evidence with the acceptance baseline. Inspect the final diff; report behavior changes, actual validation, and important gaps without repeating the full checklist.

Follow the [independent review policy](engineering.md#independent-review-policy). Read [review.md](review.md) when the user or rules require review. Hand off affected contracts, the patch, validation evidence, and known limitations; keep the author's confidence separate from evidence produced by independent checks.
