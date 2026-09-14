<a id="architecture-and-design-guidelines-for-ai-agents"></a>

# Architecture and design

[简体中文](../design.md) · **English** · [Documentation](../../README.en.md#guides)

Define behavior, boundaries, and tradeoffs before implementation.

<details>
<summary>On this page</summary>

- [Scope and minimum output](#scope-and-minimum-output)
- [Establish priorities and requirements](#establish-priorities-and-requirements)
- [Identify constraints and reversibility](#identify-constraints-and-reversibility)
- [Resolve feasibility with bounded experiments](#resolve-feasibility-with-bounded-experiments)
- [Build the minimal architecture](#build-the-minimal-architecture)
- [Describe affected boundaries](#describe-affected-boundaries)
- [Evaluate performance and reliability](#evaluate-performance-and-reliability)
- [Test likely changes and simplify](#test-likely-changes-and-simplify)
- [Record decisions, challenge, and hand off](#record-decisions-challenge-and-hand-off)

</details>

## Scope and minimum output

Follow the shared rules in [engineering.md](engineering.md). This guide applies to structural changes, costly-to-reverse decisions, and behavioral changes with important design tradeoffs. Local implementation adjustments do not require a full design process.

Design the smallest system that meets current requirements while preserving only the necessary boundaries for well-supported future changes. Balance delivery speed, simplicity, reliability, performance, and maintainability according to the project's actual priorities.

For a focused decision, a short note is sufficient:

- The problem, required result, and non-goals.
- Relevant constraints and assumptions.
- The chosen approach, affected contracts, and key invariants.
- Important alternatives, tradeoffs, and open questions.
- Validation required before treating the result as established.

Use the shared risk assessment and acceptance baseline to determine how much evidence each boundary needs. A structural change alone does not determine validation intensity.

For a new subsystem or broad structural change, add the relevant component, data-flow, ownership, failure, and performance views described below. Omit inapplicable sections and reuse accepted design material. Do not invent future scenarios or rejected alternatives merely to fill a template.

## Establish priorities and requirements

Before dividing modules or choosing patterns, identify who uses the system, the problem to solve, primary inputs and outputs, the project's current stage, and observable success criteria.

State priorities explicitly when they materially affect decisions. An early product may prioritize delivery speed after meeting correctness and hard constraints; a robotics control path may prioritize deterministic latency and lifetime safety. Derive priorities from accepted goals and constraints and resolve material ambiguity instead of silently inventing them.

Group requirements into three categories:

| Group | Criterion | Design action |
| --- | --- | --- |
| Implement now | Required for the current result | Include an end-to-end implementation and validation path |
| Preserve a boundary now | A concrete, likely future change would otherwise incur high support cost | Introduce only the smallest justified boundary; defer functionality |
| Defer entirely | A low-confidence or distant possibility | Record only when useful; add no current complexity |

For example, if an accepted near-term roadmap includes another inference backend, a small runtime boundary may isolate backend-specific behavior. That does not establish a need for a plugin registry, dynamic loader, or several unused backends. Without a credible change requirement, using the current backend directly may be sufficient.

List non-goals explicitly when they could expand task scope. Deferred capabilities can remain future considerations without being implemented now.

## Identify constraints and reversibility

Inspect existing repository patterns and accepted decisions before proposing a new structure. Look for ownership conventions, error models, API shapes, resource management, thread use, configuration, and testing practices.

Distinguish known constraints, assumptions to verify, and future possibilities. Relevant constraints may include:

| Area | Questions |
| --- | --- |
| Behavior | Which inputs, outputs, compatibility, and deployment modes are required? |
| Performance | Which latency, throughput, jitter, startup, memory, or resource limits apply? |
| Environment | Which operating systems, languages, hardware, compilers, framework versions, and deployment platforms are supported? |
| Reliability | What failure, cleanup, restart, recovery, or availability behavior is required? |
| Delivery | Which schedule, engineering effort, and operational complexity are acceptable? |

Match design effort to the cost of reversal. Private names, helpers, and local organization are usually easy to change. Public APIs, ownership and lifetime contracts, concurrency models, process boundaries, persistent-data schemas, protocol wire formats, and externally consumed data representations usually are not.

Judge reversibility by consumer and persistence impact, not by size or syntax. CLI arguments and small configuration formats become compatibility boundaries when scripts, users, stored data, or deployments depend on them. An internal detail can also be expensive to change when coupling is widespread.

## Resolve feasibility with bounded experiments

If a design choice depends on behavior that existing evidence cannot establish, run a small experiment before fixing the architecture. Examples include checking a dependency's cancellation behavior or measuring whether a proposed data path meets a resource budget. This does not require a complete design or an existing defect.

State the question, assumption to verify, smallest experiment, relevant environment, evidence required to accept or reject an approach, and stopping rule. Bound the effort to the decision and honor any stated time or resource budget. Keep the experiment isolated and reversible; do not change public contracts, production state, or dependencies beyond existing authorization.

Conclude “supported,” “rejected,” or “inconclusive,” and explain the design impact. A successful microbenchmark or simulation establishes only the tested property under its conditions. If inconclusive, identify the next discriminating step or missing prerequisite rather than expanding the prototype indefinitely. Experimental code may become a deliverable only after a clear implementation decision and the normal coding, validation, and review checks; experimental success does not automatically accept it.

## Build the minimal architecture

First show one complete path that delivers current value, for example:

```text
Input → validation → execution → result → resource release
```

Prefer few components, direct data flow, clear dependency direction, explicit ownership, and small public contracts. A coherent design may span several files; minimizing file count is not the goal.

Each abstraction should isolate a concrete concern, such as independent change, ownership, lifetime, failure isolation, performance, an external dependency, or a meaningful testing seam. Inspect which complexity it hides or which invariant it guarantees. One implementation does not automatically make an interface unnecessary, and several classes do not automatically require a framework.

Use a pattern only when it solves a problem. Correctness and hard constraints determine the approach; within them, use repository consistency and simplicity to guide selection. A concrete rationale can justify departing from an existing pattern, but record the impact instead of silently introducing a second framework.

## Describe affected boundaries

For material structural work, use views that expose the actual risks. A small design can combine them in prose or one diagram.

### Components and data flow

Show who depends on whom and trace important end-to-end paths. Where relevant, identify validation, transformation, serialization, copying, ownership transfer, context switches, and externally visible effects.

Define contracts at stable boundaries: inputs, outputs, preconditions, errors, supported versions, and compatibility expectations. Do not let correctness depend on undefined behavior between components.

<a id="ownership-and-lifecycle"></a>

### Ownership and lifetime

For important resources, identify who creates, owns, borrows, transfers, and destroys them. Include asynchronous references and cached handles. Define which dependent activity must stop before a resource becomes invalid.

A shutdown order may be:

```text
Reject new work → handle in-flight work according to policy
→ stop and join workers → release dependent resources → destroy owner
```

The actual order must follow the system's dependency relationships. Specify cancellation, partial-initialization cleanup, repeated close, cleanup failure, and recreation when they are supported behaviors. A component diagram alone cannot establish lifetime safety.

### State, concurrency, and errors

When state or concurrency is involved, define:

- Valid states and transitions, including partial failure and recovery.
- Authority over state changes and handling of repeated or late events.
- Who owns, starts, stops, and cancels each task or thread.
- Shared state, synchronization, lock order, and callback lifetime.
- Queue semantics, capacity, backpressure, and shutdown behavior.
- Error flow, cleanup responsibility, and whether retries are bounded and safe.

Inspect what happens when initialization fails midway, a dependency disappears, a callback arrives during shutdown, or an operation times out after partial success. Require recovery only when the contract requires it; do not turn a programming error into apparently successful fallback behavior.

Concurrency must meet a concrete need. Do not add threads or asynchronous execution merely because an architectural style uses them by default.

### Trust boundaries and sensitive data

When a change accepts untrusted input, changes identity or authorization, or handles sensitive data, identify the participants, protected operations or data, and where trust changes. Define input validation and the identity, authorization, or user/tenant isolation required by the contract. Identify intentionally public operations; do not add authentication merely because input comes from outside. Where relevant, trace protected data through outputs, errors, logs, caches, and external calls.

Include relevant accepted/rejected input scenarios and, when access restrictions apply, allowed/denied operations in the acceptance baseline. Inspect the boundary that actually enforces the restriction: client-side controls or happy-path tests alone cannot establish an intended access restriction. Perform these minimum checks even without a separate security guide; do not demand a full threat model for unrelated changes.

### Persistent data and protocol transitions

When a change alters the representation or interpretation of stored data, compatibility of persisted configuration, or a protocol, identify existing states and supported readers, writers, or peers. Define supported upgrade order, any necessary mixed-version period, conversion or backfill behavior, and what happens if conversion is interrupted or repeated midway. Ordinary reads and writes under an unchanged contract require relevant correctness and failure checks, not a migration plan.

Explain how incomplete conversion is detected and how rollback, restore, or roll-forward recovers it. Do not assume that rolling back application code restores altered data. Use suitable fixtures or an isolated environment to validate supported old and new states and representative interrupted conversions. State irreversible steps and required decisions before execution. If deployment is outside task scope, hand off these requirements and report implementation validation; do not claim that migration or release occurred.

## Evaluate performance and reliability

Clarify performance requirements before choosing an optimization. Identify workload, target metric, environment, critical path, and measurement method. Distinguish estimated budgets from measured results.

For example, an end-to-end latency target may be divided into budgets for request handling, preprocessing, data transfer, execution, and postprocessing. Validate the total under expected load; a budget table does not establish that the target has been met.

Inspect likely dominant costs: copying, allocation, blocking operations, serialization, contention, context switches, and device synchronization. Support design choices with measurement, known hardware constraints, or strong structural evidence. Claims of actual improvement require measurements.

Without a concrete need, avoid lock-free structures, custom allocators, caches, batching, zero-copy mechanisms, or distributed execution. At the same time, if a credible requirement needs another memory or execution model, do not unnecessarily fix an expensive representation into a stable API.

Evaluate reliability through explicit failure scenarios and outcomes: safe completion under policy, clear failure, rollback, cleanup, or recovery. Identify what must be observed at runtime to distinguish these outcomes.

## Test likely changes and simplify

If preparing for future change is justified, choose a small set of concrete scenarios, usually no more than three to five. Zero is appropriate when no future requirement is supported.

For each scenario, identify affected modules and whether public APIs, ownership, state, data representation, or concurrency must change. If a likely scenario would force a broad rewrite, consider preserving a small boundary now. Do not automatically prepare for a costly but remote scenario.

Before finalizing, perform a simplification check proportionate to the design:

- Could a service be a local module, or a factory be direct construction?
- Does a layer apply policy, manage ownership, transform, or isolate, or does it only forward calls?
- Does the proposed interface isolate a real concern?
- Are plugin mechanisms, distributed coordination, general DAG execution, or dynamic configuration actually required?
- Does every optimization have evidence or a hard constraint behind it?

Remove unsupported complexity from the proposal. This is review of the task's design, not authorization to clean up unrelated parts of the repository.

For important decisions, compare the chosen approach with realistic alternatives, including a simpler approach where practical. Explain actual tradeoffs rather than listing elaborate patterns that were never candidates.

## Record decisions, challenge, and hand off

Following the shared guide, reuse an existing design record or ADR for important decisions. Record intentionally retained limitations, rationale, and concrete reconsideration triggers. For example, a mutex for infrequent registry updates may be acceptable until profiling shows contention or concurrent loading becomes a supported requirement.

Follow the [shared independent review policy](engineering.md#independent-review-policy); seek early challenge when it can resolve important design uncertainty. Focus on unsupported assumptions, unclear ownership, costly reversals, unavoidable bottlenecks, partial failures, and unnecessary complexity. Evaluate findings before redesigning the approach. Design review evaluates readiness; it does not replace any review required for the final implementation.

A design is ready for implementation when behavior, scope, hard constraints, chosen structure, relevant invariants, and validation strategy are sufficiently clear, with no open issue preventing safe progress. Future implementation details and nonblocking questions may remain open.

Hand accepted decisions, affected contracts, important assumptions, limitations, and validation expectations to [coding.md](coding.md). Revisit the design when implementation or runtime evidence invalidates an assumption; do not treat the document as permanently correct.
