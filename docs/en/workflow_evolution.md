# Workflow improvement

[简体中文](../workflow_evolution.md) · **English** · [Documentation](../../README.en.md#guides)

Use evidence from recurring problems to make verifiable, reversible improvements.

<details>
<summary>On this page</summary>

- [Goals and boundaries](#goals-and-boundaries)
- [1. Event-driven records within a task](#1-event-driven-records-within-a-task)
- [2. Review inputs and coverage](#2-review-inputs-and-coverage)
- [3. Review checklist](#3-review-checklist)
- [4. Improvement loop](#4-improvement-loop)
- [5. Automatic-change scope and proposal scope](#5-automatic-change-scope-and-proposal-scope)
- [6. Validation and rollback](#6-validation-and-rollback)
- [7. Log contents](#7-log-contents)
- [8. Delegation and review](#8-delegation-and-review)
- [Scheduling and runtime prerequisites](#scheduling-and-runtime-prerequisites)

</details>

## Goals and boundaries

- Add a lightweight, evidence-driven mechanism for improvement during tasks and for periodic review to the existing `.codex/AGENTS.md` + `shared guide directory` system.
- Do not promise model self-training or build a new framework, directory, or scheduling system. Reuse the existing files and Codex scheduling.
- Periodic review does not change project-specific code or configuration. It refers only to task evidence within the current scope that is allowed to be accessed. Address project-specific issues only in an authorized task for that project.

## 1. Event-driven records within a task

- Triggering events: repeated failures, manual corrections, lost context, delegation environment or quota failures, validation gaps, and repeated operations.
- When an event occurs, first reuse records and artifacts from the original task instead of creating a parallel ledger.
- Write only a locatable summary (task identifier + file/line or log anchor) to the private local review log. See the [log template](../../examples/en/workflow_evolution_log.md). Do not copy the source text.
- Weekly review is suggested. The user decides whether to enable it and when it runs; do not create a duplicate schedule when one already exists.

## 2. Review inputs and coverage

- Read the last review time, scope, and open items in the log; the global entry guide and any guides changed in this round; evidence from the current task; and project-task evidence explicitly registered in the log that is currently authorized for access.
- Do not scan all private conversations, traverse entire codebases, or read credentials.
- Record inaccessible evidence as “insufficient coverage” in the log; do not claim that all projects are healthy.
- If there is no new evidence and no definite problem such as a stale link, stop without manufacturing a periodic change. Changes to log timestamps, the review cursor, or backup files created by this mechanism are not new problem evidence.

## 3. Review checklist

- Conflicting, duplicate, or stale rules, including references to files, anchors, or tools that no longer exist.
- Repeated work during context restoration, such as reconstructing or restating the same information several times.
- Whether executor selection and delegation reflected task size, risk, and independence.
- Whether validation actually proved the objective or merely performed a procedural check.
- The applicability of existing Skills and candidates for recurring SOPs.
- Use only exposed Skill metadata. Unless the user requests it, do not read or invoke `SKILL.md`.
- Periodic review does not automatically browse for trends. Verify primary sources only when a concrete technical question arises, and include the verification date in the conclusion.

## 4. Improvement loop

- Process: problem evidence → root cause → choose the smallest correction → save the before state and diff → validate → record “observe / keep / revise / roll back” in the log.
- Prefer fixing real tool or validation gaps, or removing duplicate rules, over adding slogan-like constraints.
- Do not attribute every execution failure to model capability. Check tools, context, rules, and validation design first.
- Address at most three small, evidence-backed problems in each round. Preserve the rest unchanged.
- Before starting a new problem, revisit items marked “pending observation” in the previous round.

## 5. Automatic-change scope and proposal scope

- Automatic changes are allowed only when they are within existing authorization and are limited to non-semantic documentation typos and formatting, stale links whose intended targets are confirmed, and consolidation of duplicate text without losing any constraint.
- Automatic changes are limited to Markdown documents in the global entry point and shared guide directory explicitly authorized by the user; update the log as defined by this guide. Do not use this mechanism to add or relax its own authorization, or to change the authorization, limits, or schedule of the mechanism itself.
- Provide a “concrete, reviewable proposal” only for substantive rules, model routing and quota policy, permission, acceptance, or Skill-enablement mechanisms, new Skills, script installation, and code changes. If targeted authorization already exists, implement within that scope without expanding it.
- Save the target baseline before editing, then recheck its content or hash immediately before writing. If the file changes in the meantime, stop the write and either reread and merge or preserve the proposal; do not overwrite new changes from the user or another task.
- Request permissions through the host mechanism when needed. If denied, stop that write, record the concrete gap, and continue work that does not depend on the permission. Do not bypass the denial.

## 6. Validation and rollback

- Documentation changes: check links and anchors, inspect the diff, and confirm that the owner of every changed constraint remains clear.
- Authorized semantic workflow changes: first revisit the historical failure they address and check a representative successful scenario. If no replayable record exists, state the substitute validation and its limitations. Do not fabricate replay results or lower existing mandatory acceptance standards.
- Static documentation checks alone do not establish improved development efficiency. Without real task evidence, mark the change “under observation” and use the next relevant evidence to decide whether to keep or roll it back.
- Rollback may revert only changes made by this mechanism, and only after confirming that the target file has not been changed since. If it has changed, provide a proposal instead of overwriting the user's newer work.

## 7. Log contents

- Each entry contains only the date, actual coverage, source of the issue, change location and an index to the before state or diff, validation evidence, and the decision or next observation step.
- If no issue was found in the round, update only the last review time and scope; do not add an empty log entry.
- Do not invent token savings, time savings, or percentages of any kind.

## 8. Delegation and review

- Follow the role division in [agent_selection.md](agent_selection.md) for delegation. The Root retains final decision authority.
- Base delegation on the actual workload of the review as a whole; do not split it into small operations to evade the rules. Simple, low-risk work may be completed directly. Independent review is still triggered according to [engineering.md](engineering.md#independent-review-policy).

## Scheduling and runtime prerequisites

A weekly review is suggested; the user must explicitly authorize scheduling the first one. Codex automation configuration owns the schedule and its enabled state. Editing files does not change the schedule. Actual scheduler records are authoritative for run results; successful creation does not prove that every future run has been validated. If automation is unavailable, the user may request “review according to workflow_evolution.md” within an existing task. Do not quietly add a system timer or background process.
