<a id="coding-guidelines-for-ai-agents"></a>

# Implementation

[简体中文](../coding.md) · **English** · [Documentation](../../README.md#guides)

## Scope and minimum output

Follow [engineering.md](engineering.md). Use this guide when behavior and architecture are sufficiently clear; route an unknown failure mechanism to [debugging.md](debugging.md) and an unresolved structural choice to [design.md](design.md). Implement the smallest complete change that preserves affected invariants. Complete may span files; a short diff does not establish a complete fix.

Before nontrivial work, state expected behavior, affected paths/invariants, changes, and validation; reuse this unless the plan materially changes. At completion, report the change, final-version checks, and material limitations.

## Establish the implementation contract

Inspect code, callers, tests, project conventions, and accepted designs. Identify conditions to change and preserve; end-to-end paths and effects; behavior and ownership/lifetime/state/concurrency/dependency boundaries; evidence that rejects a plausible wrong implementation; and non-goals.

Before implementation, use the [shared risk and evidence rules](engineering.md#evidence-and-confidence) to establish acceptance scenarios, required evidence, and blocking gaps. Change this baseline only for an explicit contract change or new evidence, and record why. State behavior independently of internal structure. An internal call can evidence an accepted contract or focused interaction, but not every external effect. Private implementation may change while the contract holds. If an architectural assumption fails, use the [shared architecture-change process](engineering.md#scope-and-architecture-changes); do not silently change a public contract or ownership model for implementation convenience.

## Implement and validate coherent slices

Complete one end-to-end behavior at a time: select its invariants, define the result and validation, implement the smallest complete change with project patterns, run the smallest relevant check, inspect the diff and complexity/ownership/state/error flow, and simplify within scope only for a concrete benefit. Return to the responsible phase if a failure exposes a contract or design problem.

**If code changes after validation, rerun affected checks against the final version.** Do not accumulate a large unvalidated subsystem or repeat passing checks without a later change or evidence gap. Local wording or formatting may need only focused manual or documentation checks.

## Choose evidence that tests the behavior

Use the [shared evidence rules](engineering.md#evidence-and-confidence) to select the smallest checks. Derive expectations from contracts, known mathematics, protocol examples, or independent data, not the implementation under test or its assumptions. A check should reject a plausible wrong implementation; an internal flag, call count, or observer sharing a cache cannot alone establish an external effect.

For a reproducible defect, normally run a comparable unfixed-fail/fixed-pass regression. Setup, missing-symbol, or unrelated failures do not establish sensitivity. When comparison is unreliable, explain why and provide a failure trace, controlled reproducer, or causal sequence. Select normal, boundary, invalid, partial-failure, repeated, cancellation, concurrent, compatibility, and recovery cases as relevant; counts and coverage do not replace behavioral evidence. Use mutation or fault injection only when necessary, safe, and reversible.

## Change tests for a justified reason

A failing test is evidence to investigate, not an instruction to weaken its assertion. Change an expectation only because accepted-contract evidence shows it was wrong, an authorized behavior change replaced the former contract, or behavior remains unchanged while the test structure or fixture adapts to a legitimate refactor. State the reason, preserve supported behavior, and ensure the revised test still rejects material faults.

Removing assertions or failing cases, widening ranges, increasing timeouts or retries, skipping flaky tests, or mocking away an affected dependency requires behavioral or environmental grounds; green CI alone is insufficient. Use the [shared source rules](engineering.md#intended-behavior-and-source-authority) to decide whether a test carries an accepted specification.

## Keep ownership, state, and errors explicit

Changes to access control, trust boundaries, sensitive data, stored formats, or protocols must implement the boundary and transition decisions in [design.md](design.md), with relevant denial/isolation, old/new compatibility, interruption, and recovery validation. Resolve missing decisions first. These checks do not authorize deployment or migration outside task scope.

<a id="ownership-and-lifecycle"></a>

### Ownership and lifetime

For resource changes, inspect creators, owners, borrowers, cached/asynchronous references, callbacks, and cleanup responsibility. Define when shutdown stops accepting work, finishes in-flight work, stops threads/callbacks, and invalidates dependencies. Check relevant partial initialization, repeated/concurrent close, close during work, cleanup failure, and recreation. When needed, prove external cleanup with runtime observation; a null pointer or `STOPPED` flag does not establish that a thread, socket, shared-memory object, or remote registration ended.

### State and concurrency

Keep authority over state transitions clear. Use an explicit model for mutually exclusive states and independent booleans only for independent properties; inspect invalid combinations. For each concurrency element, define owner, start/stop, cancellation, shared state, synchronization, and lifetime dependencies, and inspect lock order, queue capacity/backpressure, callback order, and work after owner invalidation. A few lines can still create an architectural change.

### Error flow and fallback

Trace material errors from origin to caller and define cleanup, partial state, recovery, and bounded safe retry. Inspect swallowed errors, lost context, success after partial failure, log-only handling where propagation is required, and propagation without cleanup. Before fallback, distinguish unsupported input, expected external failure, transient runtime failure, resource failure, internal invariant violation, and programming defect. A timeout, retry, or fallback needs a concrete failure class and explicit result; it cannot hide an unknown race or disguise failure as success.

## Control complexity and refactoring

Assess added state, abstractions, dependencies, ownership, concurrency, retries, and configuration, and justify material complexity. Repeated special cases prompt inspection of the contract, state, or responsibility boundary; a third material exception is a warning, not an automatic redesign rule.

Refactor only to reduce reasoning cost, duplication, or ambiguity within scope. Separate a large refactor from behavior changes where practical, then revalidate preserved behavior. Remove from the final diff only unrelated formatting, opportunistic renames, speculative compatibility branches, excess wrappers/duplicate mechanisms, and comments beyond guarantees that you introduced. Preserve user edits and only record unrelated issues.

## Keep performance evidence concrete

As relevant, inspect critical-path copies, allocations, serialization, locks, blocking I/O, device synchronization, and transfers without automatically optimizing. Complexity requires measurements, hard requirements, hardware constraints, or strong structural evidence. Performance claims require comparable measurements with workload, environment, and variance. Do not add custom allocators, lock-free queues, caches, batching, zero-copy infrastructure, or asynchronous pipelines for hypothetical bottlenecks. Record the rationale and escalation trigger for an accepted material limitation.

## Completion and review handoff

Under the [shared completion rules](engineering.md#persistent-records-and-completion), compare final behavior and evidence with every acceptance-baseline item. Inspect the final diff and report behavior, actual validation, and material gaps. Apply the [independent review policy](engineering.md#independent-review-policy); when review is required, read [review.md](review.md) and hand off affected contracts, patch, evidence, and limitations, separating author confidence from independent evidence.
