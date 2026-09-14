<a id="architecture-and-design-guidelines-for-ai-agents"></a>

# Architecture and design

[简体中文](../design.md) · **English** · [Documentation](../../README.md#guides)

Define behavior, boundaries, and tradeoffs before implementation.

## Scope and minimum output

Follow [engineering.md](engineering.md). Use this guide for structural changes, costly-to-reverse decisions, and behavioral changes with material tradeoffs. Local implementation changes need no full design process.

Design the smallest system that meets current needs. Preserve boundaries only for supported future changes. A focused note states:

- problem, required result, and non-goals;
- constraints, assumptions, and chosen approach;
- affected contracts and key invariants;
- realistic alternatives, tradeoffs, and open questions;
- validation required to establish the result.

For a new subsystem or broad structural change, add only relevant component, data-flow, ownership, failure, and performance views. Do not invent scenarios to fill a template.

## Establish priorities and requirements

Identify users, the problem, inputs and outputs, project stage, and observable success criteria. When priorities affect a decision, derive and state them from accepted goals and constraints; do not invent them silently.

| Group | Action |
| --- | --- |
| Implement now | Deliver the current result and its end-to-end validation |
| Preserve a boundary now | Add the smallest boundary for a concrete, likely change that would otherwise be costly |
| Defer entirely | Add no complexity for a remote or low-confidence possibility |

State non-goals when they could expand scope.

## Identify constraints and reversibility

Inspect accepted decisions and repository patterns for ownership, errors, APIs, resources, threads, configuration, and testing. Separate known constraints, assumptions to verify, and future possibilities. Cover relevant behavior, performance, environment, reliability, and delivery limits.

Judge reversal cost by consumer and persistence impact. Public APIs, ownership/lifetime contracts, concurrency models, process boundaries, persistent schemas, protocol formats, and externally consumed representations are usually costly. A small option or CLI flag is also a compatibility boundary when consumers depend on it.

## Resolve feasibility with bounded experiments

When a design depends on unverified behavior, run a small, isolated, reversible experiment first. State the question, hypothesis, environment, minimum experiment, decision evidence, and stopping rule. Respect existing budgets and authorization; do not change public contracts, production state, or dependencies.

Conclude supported, rejected, or inconclusive and explain the design effect. An experiment proves only the tested property under its conditions. For an inconclusive result, name the next discriminating step. Experimental code becomes deliverable only after normal implementation, validation, and review.

## Build the minimal architecture

Start with one complete value path: input, validation, execution, result, resource release. Prefer few components, direct flow, clear dependency direction, explicit ownership, and small public contracts.

Every abstraction must isolate a concrete change, ownership, lifetime, failure, performance, external dependency, or test boundary. Use a pattern only when it solves the problem. A departure from repository patterns needs a specific reason and must not create a second framework silently.

## Describe affected boundaries

Use only views that expose real risk. A small design may combine them in prose or one diagram.

### Components and data flow

Show dependencies and important end-to-end paths. Mark validation, transformation, serialization, copying, ownership transfer, context switches, and external effects. At stable boundaries define inputs, outputs, preconditions, errors, versions, and compatibility expectations.

<a id="ownership-and-lifecycle"></a>

### Ownership and lifetime

For important resources, state who creates, owns, borrows, transfers, and destroys them, including async references and cached handles. Define which activity must stop before invalidation and the shutdown order. Cover cancellation, partial initialization, repeated close, cleanup failure, and recreation when supported. A component diagram does not establish lifetime safety.

### State, concurrency, and errors

Define valid states and transitions, mutation authority, duplicate and late events, task/thread start-stop-cancel ownership, shared state and lock order, callback lifetime, queue capacity/backpressure/shutdown, error and cleanup responsibility, and whether retries are bounded and safe.

Check partial initialization, disappearing dependencies, callbacks during shutdown, and timeout after partial success. Implement only contracted recovery; do not hide programming errors behind fallback behavior. Concurrency needs a concrete requirement.

### Trust boundaries and sensitive data

For untrusted input, identity/authorization, or sensitive data, identify actors, protected objects, and trust changes. Define input validation, identity, authorization, and user/tenant isolation. Trace protected data through outputs, errors, logs, caches, and external calls. Validate allowed and denied cases at the enforcing boundary. External input alone does not require new authentication; apply only the relevant minimum security analysis.

### Persistent data and protocol transitions

When persistent representation, configuration compatibility, or a protocol changes, identify existing states and supported participants. Define upgrade order, mixed-version operation, conversion/backfill, interruption, repetition, and recovery. Rolling back application code does not prove data recovery.

Validate supported old/new states and interrupted transitions in isolation. Identify irreversible steps before execution. If deployment is out of scope, hand off requirements and implementation evidence; do not claim migration or release occurred.

## Evaluate performance and reliability

Before optimizing, define workload, metric, environment, critical path, and measurement method. Separate estimates from measurements. Check copying, allocation, blocking, serialization, contention, context switches, and device synchronization. Claims of improvement require comparable measurements.

Without a concrete need, avoid lock-free structures, custom allocators, caching, batching, zero-copy mechanisms, and distributed execution. Evaluate reliability with explicit failure scenarios and outcomes: safe completion, clear failure, rollback, cleanup, or recovery. Define runtime observations that distinguish them.

## Test likely changes and simplify

Choose only a few supported future scenarios, usually at most three to five; zero is valid. Ask whether they force changes to public APIs, ownership, state, data representation, or concurrency. Preserve only a small boundary when justified.

Before finalizing, remove layers without responsibility, unsupported interfaces/plugin mechanisms/dynamic configuration, and optimizations without measurements. Compare realistic alternatives, including a simpler one when practical. This check does not authorize unrelated cleanup.

## Record decisions, challenge, and hand off

Reuse an existing design record or ADR. Record important decisions, retained limits, rationale, and concrete reconsideration triggers. Apply the [independent review policy](engineering.md#independent-review-policy) to unsupported assumptions, ownership, costly boundaries, bottlenecks, partial failures, and complexity. Design review does not replace review of the final implementation.

Proceed to implementation when behavior, scope, hard constraints, structure, invariants, and validation are clear enough and no open issue blocks safe progress. Hand accepted decisions, contracts, assumptions, limits, and validation expectations to [coding.md](coding.md). Return to design when new evidence invalidates an assumption.
