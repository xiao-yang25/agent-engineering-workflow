<a id="debugging-guidelines-for-ai-agents"></a>

# Debugging

[简体中文](../debugging.md) · **English** · [Documentation](../../README.en.md#guides)

Use discriminating experiments to establish the cause, then verify the fix.

<details>
<summary>On this page</summary>

- [Scope and minimum output](#scope-and-minimum-output)
- [Establish the symptom and preserve evidence](#establish-the-symptom-and-preserve-evidence)
- [Build and compare reproducers](#build-and-compare-reproducers)
- [Construct a failure model](#construct-a-failure-model)
- [Form and distinguish hypotheses](#form-and-distinguish-hypotheses)
- [Run purposeful experiments](#run-purposeful-experiments)
- [Apply failure-specific checks when relevant](#apply-failure-specific-checks-when-relevant)
- [Root-cause gate and investigation outcomes](#root-cause-gate-and-investigation-outcomes)
- [Validate the fix and neighboring invariants](#validate-the-fix-and-neighboring-invariants)

</details>

## Scope and minimum output

Follow the shared rules in [engineering.md](engineering.md). Use this guide when a failure exists but its causal mechanism is not sufficiently understood, especially for intermittent, concurrent, lifetime, distributed, or performance problems.

Build an evidence-supported explanation, use it to guide the fix, and distinguish a fix from symptom suppression. A patch that makes a failure disappear is useful evidence, but it does not by itself explain why the system failed.

Match investigation depth to uncertainty and risk. A deterministic local defect may need only a reproducer and a short causal explanation. A complex failure may require a timeline, competing hypotheses, and multiple experiments. Do not invent extra hypotheses or reports once direct evidence establishes the relevant mechanism.

Keep one concise record throughout the work: symptom, environment, best reproducer, observations, hypotheses, evidence limits, and next experiment. Reuse it for progress updates and handoffs instead of maintaining overlapping reports. Use the shared risk assessment to judge the consequences and reach of the failure, and state the evidence needed for the next decision. Complete the fix's acceptance baseline as the mechanism becomes clear, and state any change to required evidence explicitly.

## Establish the symptom and preserve evidence

Describe expected and observed behavior before choosing a cause. When known, include trigger conditions, frequency, environment, and impact. Use the shared statement types and confidence levels to separate observations from interpretations.

For example:

```text
Expected: destroying Service removes its discovery registration.
Observed: in 1 out of 100 shutdowns, a remote observer still sees it after 5 seconds.
Environment: release build, multithreaded lifetime test.
Hypothesis: worker shutdown may overlap registry cleanup.
```

This observation does not determine whether the cause is a worker-thread race, asynchronous cleanup, or an observer cache.

Preserve valuable failure state before restarting, terminating, resetting, or applying a change that would destroy that state. Select evidence according to the failure:

| Failure | Useful state |
| --- | --- |
| Crash | Core dump, failing thread and instruction, call stacks, relevant memory, preceding errors |
| Hang | Call stacks for all threads, wait states, lock/resource ownership, process tree, CPU use |
| Resource leak | Counts and lifetimes of handles, descriptors, memory, threads, registrations, or device resources |
| Network/distributed failure | Local and peer state, protocol events, packet capture, routes, timestamps, versions |
| Performance regression | Baseline and regressed metrics, workload, profiles, latency distribution, resource utilization |

If an ongoing incident requires an authorized mitigation before the cause is known, preserve available evidence when practical and label the action as mitigation. Verify its immediate effect and record that the cause remains unresolved. Service recovery does not establish that the root cause has been fixed.

## Build and compare reproducers

Progressively make the failure controllable by recording the build, dependency versions, configuration, input, hardware/OS, load, topology, timing, and relevant startup/shutdown order. Record only dimensions that help reproduce or distinguish the failure.

Improve the reproducer incrementally: increase frequency, remove irrelevant components, simplify input, and then control the suspected interleaving where possible. A synchronization barrier may expose a race more reliably than many uncontrolled repetitions. Verify that simplification or amplification preserves the original failure mechanism rather than creating a different defect.

Compare passing and failing cases. Useful differences include revisions, dependency versions, compiler flags, debug/release builds, machines, configurations, inputs, loads, and execution order. When the pass/fail boundary is reliable, use regression bisection or reduce the configuration or components incrementally.

Intermittent-failure verdicts can mislead a bisection. State how a candidate revision is classified, and preserve inconclusive results instead of treating every successful run as proof that the revision is good.

When reproduction is impossible, use preserved traces, crash evidence, dependency semantics, and static causal reasoning. State the missing runtime evidence and limit confidence accordingly; do not fabricate a reproducer or repeat inconclusive runs indefinitely.

## Construct a failure model

Model the relevant data/control flow, state transitions, ownership, resources, threads/tasks, and external systems. For timing-sensitive failures, reconstruct an event timeline and mark each event as observed, inferred, or unknown. Account for clock differences when combining distributed observations.

For example:

```text
T0 observed: shutdown begins
T1 observed: stop requested
T2 observed: registry destruction begins
T3 unknown:  worker accesses registry
T4 observed: worker exits
```

This timeline identifies a window in which invalid access could occur, but does not prove that T3 actually happened.

Distinguish causal roles:

| Role | Meaning | Example |
| --- | --- | --- |
| Root cause | The defect that permits the failure mechanism | Worker lifetime is not coordinated with registry lifetime |
| Trigger | The condition that activates one occurrence | Worker wakes during shutdown |
| Amplifier | A condition that raises probability or impact | Load widens the overlap window |
| Symptom | The observed consequence | Invalid access, crash, or stale external state |

Several defects may jointly produce a failure. Do not force every incident into one cause. Trace backward from the final symptom to the violated invariant: an allocation failure may expose a defect in an error path, which corrupts state and eventually causes a shutdown hang. The last error message does not necessarily identify the first defect.

## Form and distinguish hypotheses

Keep a small set of plausible explanations while alternatives remain viable. Rank them by consistency with observations, explanatory power, unsupported assumptions, and test cost. Priority is not confidence.

Use a table when it makes the investigation clearer:

| Hypothesis | Supporting evidence | Contrary evidence or limitation | Next discriminating check |
| --- | --- | --- | --- |
| Worker accesses invalid registry state | Worker may still be alive after cleanup begins | Invalid access has not been captured; this is an evidence gap | Capture access ordering or induce the suspected overlap |
| Observer returns stale cached state | Only the remote observer reports the registration remains | Local cleanup still needs verification | Compare local resource state with the result from a fresh observer |

Seek evidence that could weaken the leading explanation. Record negative results and their coverage: a stable descriptor count limits a descriptor-leak hypothesis for that workload, but does not exclude every resource leak.

When evidence contradicts a hypothesis, reject or revise it explicitly. Do not reinterpret every result to preserve the original guess.

## Run purposeful experiments

For a meaningful experiment, record the question, hypothesis under test, intervention, predicted result, observed result, and interpretation. A few lines suffice for a simple experiment.

Prefer observations or interventions that produce different outcomes under competing explanations. Change one causal variable where practical. If several variables must change, label the result exploratory; without follow-up evidence, avoid attributing the effect to any one change.

Classify debugging changes:

| Change | Purpose |
| --- | --- |
| Observational instrumentation | Capture state without intentionally changing semantics, such as traces or counters |
| Diagnostic intervention | Deliberately change timing, ordering, faults, or configuration to test a hypothesis |
| Candidate fix | Implement a proposed correction whose effect still requires validation |

Instrumentation may change timing, scheduling, allocation, memory layout, cache behavior, and I/O. Logs, breakpoints, sanitizers, extra locks, or sleeps may make a defect disappear. Treat that as a clue, not proof that the original behavior is correct.

Use tools to answer specific questions:

| Tool or method | Example question |
| --- | --- |
| Debugger, call stack, core dump | Where did execution fail or stop making progress? |
| Memory sanitizer | Is a detectable invalid access or lifetime violation occurring? |
| Race detector | Is there a detectable data race on an executed path? |
| Profiler | Where is time spent under the workload that exhibits the regression? |
| System tracing | Which operation blocks or fails? |
| Packet/protocol capture | Did the expected event reach the relevant peer? |
| Controlled fault injection | Does this partial failure, delay, duplication, or reordering produce the predicted state? |

Run destructive experiments only in an appropriate environment and within task authorization. Keep interventions reversible and separate from production changes. Preserve user edits when reverting experiments. Do not retain a diagnostic sleep, disabled cache, or mutation in the final patch merely because it suppresses the symptom.

If experiments stop distinguishing explanations, reconsider the reproducer, observations, and model. Avoid broad refactors or random patch accumulation while the mechanism remains unclear.

## Apply failure-specific checks when relevant

| Failure category | Focus |
| --- | --- |
| Concurrency | Which operations overlap, what state they share, required ordering, synchronization, callback/task lifetime, cancellation, and shutdown |
| State machine | Valid, transitional, and failed states; authority over transitions; repeated or late events; partial transitions; conflicting flags |
| Ownership/lifetime | Creation, borrowing, cached/asynchronous references, cleanup responsibility, dependency order, partial initialization, repeated destruction |
| Distributed/network | Local, remote, cached, and eventual state; loss, delay, duplication, reordering, partitions, restarts, version or clock differences |
| Resource leak | Actual resources across repeated lifecycles; distinguish retained caches or deferred cleanup from resources no longer released as required |
| Performance regression | Comparable baseline, workload, and environment; latency distribution, throughput, utilization, and measured bottlenecks |
| Crash | The first invalid state, ownership/lifetime, preceding errors, and whether the failure is primary or secondary |
| Hang/deadlock | What each blocked participant awaits, who can make progress, and whether the wait relation forms a cycle |

For performance work, use measurement to distinguish CPU/GPU work, memory bandwidth, allocation, contention, I/O, and synchronization. “This code looks expensive” is not an established performance root cause.

For hangs, capture state before termination when practical. A timeout may be required behavior, but increasing it cannot explain an unexpected circular wait. For leaks, an internal null pointer does not establish that the underlying resource was released.

## Root-cause gate and investigation outcomes

Before using a candidate explanation as the basis for a fix, establish to the confidence required by risk:

- The violated contract or invariant.
- The condition or defect that permits the invalid state.
- The event sequence connecting it to the observed symptom.
- Supporting evidence and important alternatives considered.
- Why the proposed change interrupts the mechanism.
- Important evidence limits, including reproduction limits.

Apply the [shared confidence definitions](engineering.md#evidence-and-confidence) to causal claims. State discriminating evidence and remaining alternatives. An uncertain explanation requires further investigation or work explicitly labeled as an experiment, rather than a claim that root-cause repair is complete.

Choose a clear outcome:

| Outcome | Condition | Next step |
| --- | --- | --- |
| Root cause sufficiently established | Evidence supports the causal explanation with enough confidence for the next action | Hand off to coding, design, contract clarification, or external-dependency work |
| Investigation blocked / insufficient evidence | A specific observation, access capability, environment, or decision is missing and prevents useful progress | Report known facts, the missing prerequisite, and the next useful experiment; continue independent work where possible |
| Fix validated | Implementation and required regression/mechanism checks are complete | Review under the shared guide and evaluate task completion |

Do not exit early with “insufficient evidence” while useful authorized investigation remains. Do not keep repeating the same inconclusive experiment when it cannot supply the missing information. A blocked investigation does not mean the failure is resolved; if the task also requires implementation, a root-cause handoff does not mean the task is complete.

A concise handoff includes the symptom and expected behavior, reproducer or captured evidence, causal sequence, confidence and alternatives, affected invariants, and required repair direction. Route implementation defects to [coding.md](coding.md) and changes to ownership or architectural models to [design.md](design.md). Resolve invalid requirements, tests, or upstream assumptions at their respective boundaries.

## Validate the fix and neighboring invariants

Use both regression and mechanism evidence, at a depth proportionate to the claim:

- **Regression evidence:** The original failure scenario now meets expected behavior in the relevant environment.
- **Mechanism evidence:** Within the stated assumptions, the change prevents or correctly handles the causal path identified by the investigation.

For a reproducible defect, use the before/after regression check defined in [coding.md](coding.md): the unfixed version fails because of the target defect, and the fixed version passes under comparable conditions. This is the comparison normally performed first. The A/B/A method below is an optional, stronger intervention when it can resolve remaining uncertainty. If a reliable comparison is unavailable, state the limitation and alternative evidence, and assess whether they satisfy the acceptance baseline.

For example, stopping and joining a worker before destroying a registry can establish the required lifetime order, provided the shutdown protocol allows the worker to exit. Check neighboring properties such as deadlock freedom, shutdown latency, cancellation, and error cleanup rather than merely turning a crash into a hang.

A defect that occurs once every 10,000 runs is not strongly excluded by 100 successful runs. Improve the reproducer, induce the relevant interleaving, or strengthen mechanism evidence. Record workload, run count, and limitations; do not claim from limited testing that the defect is universally absent.

When practical, use isolated A/B/A validation: reproduce with the original code, apply the candidate fix, then temporarily withdraw the change that targets the causal mechanism and check that the failure returns. This strengthens evidence that the change matters, but still requires a causal explanation. Do not use this method if withdrawal is unsafe or would interfere with user work. Remove diagnostic mutations afterward and validate the final version.

Scrutinize sleeps, retries, timeouts, larger buffers, ignored errors, and default values. Ask which failure class they handle, why any boundary is reasonable, what state remains, and whether slower or repeated execution can still fail. These mechanisms can be valid contract behavior, but cannot replace an explanation of an unknown cause.

Recheck relevant neighboring invariants: resource cleanup, synchronization, latency, memory, compatibility, error propagation, retry semantics, and recovery. Expand the test scope only when the fix affects those properties or a gap remains.

Finally, summarize the fix, causal reasoning, checks actually run against the final version, and remaining uncertainty. Use [review.md](review.md) when review is required. Report a fix as validated only when the task's acceptance criteria are met; otherwise, distinguish implemented code from missing validation or remaining blockers.
