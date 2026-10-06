# Workflow improvement

[简体中文](../workflow_evolution.md) · **English** · [Documentation](../../README.md#guides)

Use recurring-problem evidence for verifiable, reversible improvement.

## Goals and boundaries

- Reuse existing entry points, guides, and Codex scheduling. Do not promise model self-training or create a framework, directory, or scheduler.
- Periodic review does not change project code/configuration. It uses only authorized evidence; project issues stay in their task.

## 1. Event-driven records within a task

- Repeated failure, correction, lost context, delegation environment/quota failure, validation gaps, or repeated operations trigger a record.
- Reuse original task records and artifacts; do not create a parallel ledger.
- The private local log stores only task ID plus file/line or log anchor, not source text. See the [template](../../examples/en/workflow_evolution_log.md).
- Weekly review is suggested. The user chooses enablement and time; do not duplicate an existing schedule.

## 2. Review inputs and coverage

- Read prior scope/open items, changed guides, current-task evidence, and logged project evidence currently authorized.
- Do not scan private conversations, codebases, or credentials. Mark inaccessible evidence as insufficient coverage; do not claim universal health.
- Stop without a change when there is no new evidence or definite problem. Timestamps, cursors, and this mechanism's backups are not problem evidence.

## 3. Review checklist

- Check conflicting/duplicate/stale rules, repeated recovery, delegation fit, validation strength, and Skill/SOP candidates.
- Use only exposed Skill metadata. Without a request, do not read or invoke SKILL.md.
- Do not browse trends automatically. Verify primary sources only for a concrete technical question and record the date.

## 4. Improvement loop

- Evidence → root cause → smallest correction → save before/diff → validate → log observe/keep/revise/roll back.
- Fix tool/validation gaps or duplication. Check tools, context, rules, and validation before blaming models.
- Address at most three evidence-backed small problems per round; preserve the rest. Review prior pending-observation items before starting a new problem.

## 5. Automatic-change scope and proposal scope

- Within existing authorization, automatic changes are limited to nonsemantic Markdown typo/format fixes, stale links with confirmed targets, and duplicate-text consolidation that loses no constraint.
- Files are limited to user-authorized Markdown in the global entry and shared-guide directory. Do not add/relax permission or change this mechanism's authorization, limits, or schedule.
- Give a concrete reviewable proposal for substantive rules, model/quota policy, permission, acceptance, Skill enablement, new Skills, script installation, and code. When targeted authorization exists, implement within it without expansion.
- Save the baseline, then recheck content/hash immediately before writing. If it changed, reread and merge or retain the proposal; do not overwrite user or other-task changes.
- If permission is denied, stop that write, record the gap, and continue independent work. Do not bypass refusal.

## 6. Validation and rollback

- For documentation, check links, anchors, diff, and each changed constraint's owner.
- For authorized semantic changes, revisit the target historical failure and a representative success. If replay is impossible, state substitute evidence and limits; do not fabricate results or lower gates.
- Static checks do not prove efficiency improvement. Without task evidence, mark the change under observation and decide from later evidence.
- Roll back only this mechanism's changes after confirming the file has not changed since. If it has, propose; do not overwrite.

### Small regression set from real tasks

Maintain reusable successful artifacts and methods in the original project or task. Cases here assess workflow changes; one success does not establish improvement, and project assets are not copied into the private index.

- Select a few representative cases from the current task or logged evidence that remains authorized: the target historical failure and successful scenarios that must keep working. Cover the current change first; do not scan other tasks to fill a quota. Reuse the private log and original task records for the index; keep personal cases out of the public repository.
- Link each case to original evidence and its version, and define inputs/prerequisites, expected outcomes, acceptance entry points, and applicability limits. Verify actual artifacts or final state; an Agent's completion claim alone is not a passing result.
- Save a baseline before the change and compare the same cases under the same acceptance criteria afterward. Record guide/model/environment versions and differences that affect comparability. Adjust one main factor at a time where possible; do not attribute a result to one change when its effect cannot be isolated.
- For key cases affected by randomness, set the repeat count in advance within existing authorization and budget, and record every attempt rather than selecting successes. Replay remains subject to host permissions and operation limits. If safe replay or comparable conditions are unavailable, state substitute evidence and gaps, and keep the change under observation.
- Revise cases and criteria only for changed requirements, contracts, or new evidence; retain the reason and old-version reference. Do not remove failing cases or relax criteria to improve scores. Decide to keep, revise, or roll back from actual results; case count, static checks, or one success alone cannot prove overall improvement.

## 7. Log contents

- Each item contains date, actual coverage, issue source, location and before/diff index, validation, and decision or next observation.
- With no issue, update only review time and scope; add no empty entry.
- Do not invent token, time, or percentage savings.

## 8. Delegation and review

- Delegate under [agent_selection.md](agent_selection.md); Root retains final decision.
- Judge the whole review workload and do not split work to evade rules. Independent review still follows [engineering.md](engineering.md#independent-review-policy).

## Scheduling and runtime prerequisites

The user must explicitly authorize the first schedule. Codex automation configuration owns timing and enablement; editing files does not change it. Scheduler records are authoritative, and successful creation does not prove future runs were validated. If automation is unavailable, the user may request a review in the current task. Do not add a system timer or background process silently.
