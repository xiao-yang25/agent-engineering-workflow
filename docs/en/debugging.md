<a id="debugging-guidelines-for-ai-agents"></a>

# Debugging

[简体中文](../debugging.md) · **English** · [Documentation](../../README.md#guides)

## Scope and minimum output

Follow [engineering.md](engineering.md). Use this guide when a failure exists but its mechanism is unknown. Establish evidence that distinguishes alternative explanations before using the cause to guide a fix; a patch that removes the symptom does not by itself establish root cause. Match investigation depth to risk and uncertainty, and do not invent hypotheses or reports after direct evidence is sufficient.

Reuse one concise record: symptom, environment, best reproducer, observations, hypotheses, evidence limits, and next experiment. First state the evidence needed for the next decision, then complete the fix acceptance baseline when the mechanism is clear. Explain changes to required evidence; a failure or unavailable environment does not lower the bar.

## Establish the symptom and preserve evidence

Use the [shared statement and confidence rules](engineering.md#evidence-and-confidence) to separate expected behavior, observation, and interpretation; record known triggers, frequency, environment, and impact. Before restarting, terminating, resetting, or changing code in a way that destroys failure state, preserve relevant evidence: for a crash, core/thread/stack/preceding errors; for a hang, all threads, waits, locks/resources, process tree, and CPU; for a leak, actual resource counts and lifetimes; for network/distributed failure, local and peer state, protocol events, timestamps, and versions; for performance regression, comparable metrics, workload, profiles, distributions, and utilization.

An authorized mitigation may precede causal understanding during an incident, but preserve evidence where practical, label it as mitigation, verify the immediate effect, and retain the unresolved-cause status. Service recovery does not establish a root-cause fix.

## Build and compare reproducers

Record build, dependency, configuration, input, hardware/OS, load, topology, timing, and startup/shutdown dimensions only when they reproduce or distinguish the failure. Incrementally raise frequency, remove irrelevant components, simplify input, and control suspected interleavings while confirming the original mechanism remains. Compare passing and failing cases; bisect revisions or reduce configuration only when the pass/fail boundary is reliable.

Success in an intermittent run does not establish that a candidate revision is good. Define the verdict rule and retain inconclusive results. When reproduction is impossible, use preserved traces, crash evidence, dependency semantics, and static causal reasoning; state missing runtime evidence and lower confidence accordingly. Do not fabricate a reproducer or repeat inconclusive runs indefinitely.

## Construct a failure model

Model relevant data/control flow, state transitions, ownership, resources, threads/tasks, and external systems. For timing failures, reconstruct an event timeline and mark each event observed, inferred, or unknown; account for clock differences across distributed observations.

Distinguish root cause (the defect permitting the mechanism), trigger, amplifier, and symptom. Several defects may contribute jointly. Trace backward from the symptom through violated invariants and the first invalid state; the last error need not identify the first defect.

## Form and distinguish hypotheses

While alternatives remain viable, keep a small set of plausible hypotheses ranked by consistency with observations, explanatory power, unsupported premises, and test cost. Priority is not confidence. For each, record supporting evidence, contrary evidence/limits, and the next discriminating check. Seek evidence that could weaken the leading explanation; negative results apply only within their coverage. Explicitly reject or revise a contradicted hypothesis instead of reinterpreting every result to preserve it.

## Run purposeful experiments

Record the question, hypothesis, intervention, prediction, observation, and interpretation. Prefer checks producing different outcomes under competing explanations, and change one causal variable where practical. If several variables must change, label the result exploratory and do not attribute it to one variable without follow-up evidence.

Separate observational instrumentation, a diagnostic intervention that deliberately changes timing/fault/configuration, and a candidate fix still requiring validation. Logs, breakpoints, sanitizers, extra locks, or sleeps may change timing, layout, cache behavior, and I/O; symptom disappearance is only a clue. Use a tool to answer a concrete question such as failure location, memory/race evidence on executed paths, bottleneck, system block, protocol arrival, or state after a controlled fault.

Run a destructive experiment only in an appropriate environment and within task authorization. Keep interventions reversible and separate from production changes, and preserve user edits when reverting. Do not retain a sleep, disabled cache, or diagnostic mutation merely because it suppresses the symptom. When experiments no longer distinguish explanations, revisit the reproducer, observations, and model; avoid broad refactors or random patch accumulation while the mechanism remains unknown.

## Apply failure-specific checks when relevant

| Category | Focus |
| --- | --- |
| Concurrency/state machine | Overlap, shared state, order, synchronization, cancellation, shutdown, transition authority, late/repeated events, invalid states |
| Ownership/lifetime | Creation, borrowing, cached/asynchronous references, cleanup, dependency order, partial initialization, repeated destruction |
| Distributed/network | Local, remote, cached, and eventual state; loss, delay, duplication, reordering, partition, restart, version, and clock |
| Resource leak | Actual resources across lifecycles; distinguish retained/deferred cleanup from contract-violating non-release |
| Performance regression | Comparable baseline, workload, environment, distribution, throughput, utilization, and measured bottleneck |
| Crash/hang | First invalid state, preceding errors, primary/secondary relation; what each participant awaits, who can progress, and wait cycles |

A performance cause requires measurements distinguishing CPU/GPU, memory bandwidth, allocation, contention, I/O, and synchronization; code that looks expensive is not a root cause. Capture hang state before termination where practical; a larger timeout does not explain circular waiting. An internal null pointer does not establish release of the underlying resource.

## Root-cause gate and investigation outcomes

Before using an explanation to justify a fix, establish to the confidence required by risk: the violated contract/invariant; condition or defect permitting the invalid state; event sequence connecting it to the symptom; supporting evidence and material alternatives; why the change interrupts the mechanism; and evidence limits, including reproduction limits. Apply the [shared confidence rules](engineering.md#evidence-and-confidence). If uncertainty remains, continue investigation or label the work experimental; do not claim root-cause repair is complete.

- **Root cause sufficiently established:** Evidence supports the next action; hand off to coding, design, contract clarification, or external-dependency work.
- **Investigation blocked / insufficient evidence:** A specific observation, permission, environment, or decision is missing; report facts, the gap, and the next useful experiment, and continue independent work that remains possible.
- **Fix validated:** Implementation and required regression/mechanism checks are complete; review under the shared guide and evaluate task completion.

Do not exit while useful authorized investigation remains, or repeat the same experiment when it cannot supply missing information. Blocked does not mean resolved; when the task requires a fix, a root-cause handoff does not mean complete. A handoff includes symptom/expectation, reproducer or evidence, causal sequence, confidence and alternatives, affected invariants, and required repair direction. Route implementation defects to [coding.md](coding.md) and ownership or architecture-model changes to [design.md](design.md).

## Validate the fix and neighboring invariants

A fix needs evidence proportionate to the claim: **regression evidence** that the original failure scenario now meets expectations in the relevant environment, and **mechanism evidence** that the change prevents or correctly handles the identified causal path within stated assumptions. For a reproducible defect, use the comparable unfixed-fail/fixed-pass check in [coding.md](coding.md#choose-evidence-that-tests-the-behavior). If reliable comparison is unavailable, state its limits and alternative evidence and decide whether the acceptance baseline is met.

Limited successful runs do not strongly exclude a low-frequency defect. Improve the reproducer, induce the relevant interleaving, or strengthen mechanism evidence, recording workload, run count, and limits. When it resolves remaining uncertainty without affecting user work, isolated A/B/A validation is optional; withdrawing the fix must be safe, and diagnostic mutations must then be removed before final-version validation.

Scrutinize the failure class, boundary, and remaining state of sleeps, retries, timeouts, larger buffers, ignored errors, and defaults; none replaces an explanation of an unknown cause. Expand to cleanup, synchronization, latency, memory, compatibility, error propagation, retry, and recovery checks only when the fix affects them or a gap remains. Finally report the fix, causal reasoning, checks actually run against the final version, and remaining uncertainty. Use [review.md](review.md) when required. Call a fix validated only when acceptance criteria are met; otherwise separate implemented code from missing evidence or blockers.
