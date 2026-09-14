# Project onboarding

[简体中文](../project_workflow.md) · **English** · [Documentation](../../README.en.md#guides)

Preserve project conventions and fill only the entry-point and evidence gaps the task needs.

<details>
<summary>On this page</summary>

- [Purpose and triggers](#purpose-and-triggers)
- [Shared preparation and sources](#shared-preparation-and-sources)
- [New projects: build with the first increment](#new-projects-build-with-the-first-increment)
- [Existing projects: baseline and minimal additions](#existing-projects-baseline-and-minimal-additions)
- [Responsibilities of project-level AGENTS](#responsibilities-of-project-level-agents)
- [Documentation and ongoing context](#documentation-and-ongoing-context)
- [Testing and acceptance](#testing-and-acceptance)
- [Optional Skill capability guide](#optional-skill-capability-guide)
- [Capturing and reporting repeated actions](#capturing-and-reporting-repeated-actions)
- [Ongoing maintenance and onboarding completion](#ongoing-maintenance-and-onboarding-completion)

</details>

## Purpose and triggers

This guide defines how to establish, inspect, and maintain a system of project-specific rules. It does not store business facts for individual projects or prescribe a uniform directory tree.
Shared engineering policy is defined in [engineering.md](engineering.md). Execution delegation and evidence delivery follow [agent_selection.md](agent_selection.md); do not duplicate those rules in each project.

Use this guide as needed when:

- Entering a project for the first time, before confirming that its rules, context, and validation entry points are sufficient for the current objective.
- The user explicitly asks to establish a system for a new project or improve the rules and workflow of an existing one.
- Development reveals a missing or stale project constraint, document, run entry point, or acceptance entry point that affects the current task.

Reuse existing knowledge when a project has already been onboarded and its entry points remain valid; do not repeat a repository-wide inventory for every task.
During routine development, fill only the gaps required by the current task. Expand into a more complete system inventory and cleanup only when the user explicitly requests an overall overhaul.
When establishing rules is necessary support for an authorized project objective, proceed within that authorization. For pure consultation or read-only review, report findings and proposed changes without modifying the project as a side effect.
This guide does not expand file, network, data, or budget permissions. It does not require repeated confirmation for already authorized steps, or automatically enable or create Skills.

## Shared preparation and sources

First identify the project root, task scope, existing user changes, and applicable team rules. Within the relevant scope, inspect:

| Fact to establish | Preferred sources |
| --- | --- |
| Target behavior and constraints | Accepted requirements, project AGENTS, README, interface contracts, and design decisions |
| Current structure and execution paths | Relevant code, build configuration, deployment conventions, and existing architecture documentation |
| How correctness is checked | Test instructions, scripts, test registration, CI, and any required target environment |
| How unfinished work continues | Existing issues, plans, investigation records, internal documentation, and evidence indexes |

Use the [source authority rules](engineering.md#intended-behavior-and-source-authority) to distinguish accepted contracts, implementation descriptions, observational evidence, and unknowns.
Existing code, tests, or historical reports do not automatically become the correct contract. When sources conflict, first establish the intended behavior. Do not rewrite rules merely to make the implementation appear correct.
Performance thresholds, compatibility scope, failure-recovery semantics, and data-retention rules need accepted support; do not invent them merely to complete a template.
There is no need to inspect unrelated directories, credentials, or operational data, or to connect to a device merely because the documentation lists it. If a necessary entry point is inaccessible, record the gap and its effect on the current task.

## New projects: build with the first increment

1. Clarify the users, core scenarios, goals and non-goals, hard constraints, first deliverable, and the basis for accepting it.
2. The Root decides the necessary technical and structural tradeoffs. Workers organize source material, validate feasibility, and execute a chosen approach. Keep unresolved key decisions explicit.
3. Establish one complete, runnable, verifiable path first, along with the necessary dependency setup, build, run, and check entry points. Do not accumulate infrastructure that cannot yet be validated.
4. As facts are established, write the minimum project AGENTS, usage guidance, and acceptance instructions. Related sections may share one file; each category does not require a separate document.
5. In later increments, add constraints, checks, and knowledge according to their semantic impact. Keep unverified assumptions labeled. Apply the shared engineering rules to completion of the first increment.

The initial rules can be brief. Do not prebuild a complete documentation tree, a Skill collection, a multi-Agent framework, or script wrappers with no practical use.
If the task asks only for requirements or a design proposal, deliver that proposal and the items still to validate; do not claim to have established a runnable project.

## Existing projects: baseline and minimal additions

First confirm the onboarding scope: a local addition needed by a routine task, or the project-system overhaul requested by the user. Both preserve user changes and existing team conventions.

1. Locate the existing rules, contracts, and knowledge entry points, and trace the real paths involved in the objective. Reuse existing files when they can serve the required role.
2. Check the relevant validation baseline, including existing check entry points, dependencies, test inventory, and any obtainable version-specific results. Distinguish pre-existing failures, environment problems, checks not run, and issues introduced by the current change.
3. Briefly state what remains, what needs to be added, where duplicate content should return to its authoritative location, and which key unknowns must be resolved. Continue when existing authorization is sufficient; do not turn this step into a fixed approval gate.
4. Make the necessary changes incrementally, and validate them against the affected behavior and the project's acceptance rules. Preserve justified stricter project requirements; adopting the shared workflow must not weaken a gate.
5. Update the documents and task record actually affected, retaining evidence and gaps. Treat broader governance work outside the current task as follow-up work.

Do not move directories, rewrite architecture, or copy the shared guides merely to fit a template. Historical accidental behavior cannot be promoted directly to a contract or removed arbitrarily before its compatibility impact is understood.
Off-repository internal documentation, deployment boundaries, and data-confidentiality agreements remain in effect; onboarding does not require moving them into the code repository.

## Responsibilities of project-level AGENTS

Project AGENTS should be concise and provide project-specific differences, necessary durable constraints, and concrete entry points:

- Where requirements and product contracts, architecture, test acceptance criteria, and internal material are maintained.
- Which business truths, ownership rules, state boundaries, or compatibility boundaries must be honored, and where their full definitions live.
- How a concrete change maps to its configuration, commands, and acceptance requirements; link to an existing detailed mapping when available.
- Stricter project requirements, operating boundaries, and other project differences that executors need to know.

Do not copy the delegation, model, risk, review-method, and completion-state rules already defined by the global and shared guides into project text.
Record how shared principles apply to the project, such as which sources a configuration change must update and which check it must run, rather than explaining general testing principles again.
Detailed documents do not need standardized filenames. When existing entry points work, connect them with brief navigation in the project AGENTS and avoid maintaining two copies of the rules. Forward entry points for other CLIs to the same rules according to their actual loading mechanisms; do not assume every filename is discovered automatically.

The shared entry point must be accessible to the actual executor. Do not copy personal-directory paths directly into a team repository. For rule transfer across machines, offline environments, or other CLIs, follow the [collaboration guide](agent_selection.md#minimum-task-brief-and-result).
If necessary rules cannot be accessed, state the limitation. Do not assume Codex and a Worker automatically read the same files, or claim they were loaded when they were not.

## Documentation and ongoing context

Every fact has one clear authoritative maintenance location, and other files only refer to it. That location may be a repository file or an internal system allowed by the project; different documents may own different categories of information.

| Information | Maintenance approach |
| --- | --- |
| Product and interface contracts | Reuse accepted requirements, README content, or interface documentation to state target behavior |
| Current architecture | Reuse architecture documentation or the README to reflect current boundaries and important paths |
| Important decisions | Record only decisions worth retaining under the shared rules, using existing design documents or ADRs |
| Ongoing task status | Reuse one task record containing the current objective, confirmed decisions and evidence, open items, and next step |
| Runtime and operational evidence | Store raw results in an allowed location and provide a locatable, version-linked index |

For record update timing, output control, compaction, and resumption checks, see [Context management and resumption](engineering.md#context-management-and-resumption).
Git history does not replace the hypotheses, failed experiments, and next step of an unfinished investigation. Short tasks do not need a new progress file; long tasks should not maintain several overlapping records.
Locate internal material through approved document identifiers, versions, or indexes. Do not put real credentials, sensitive operational data, or personal workspace paths into public or team repositories.
If an internal location has not been provided, state the known lead and gap in an allowed task record or delivery note. Do not invent links or claim that internal documentation was updated. Ask for the missing information only when the gap blocks necessary work on the current task.

## Testing and acceptance

Follow the [evidence rules](engineering.md#evidence-and-confidence) and [independent review policy](engineering.md#independent-review-policy). The project maps them to executable checks rather than redefining shared policy:

| Affected scope | Actual check entry point | Required environment | Scenarios and expected criteria | Result location |
| --- | --- | --- | --- | --- |
| Fill in for the relevant module or contract | Existing command, test target, or controlled operation | Required dependencies, configuration, and platform | Results that distinguish correct from incorrect behavior | Corresponding run report or internal record |

This is an information structure, not a requirement to create a separate table file. Reuse existing test documentation and CI when they already express these relationships.
Check test dependencies and registration, paths, and commands, and actually run the checks required for the current objective. A file's presence does not prove it can run, test registration does not prove CI ran it, and a historical green result does not prove the final version passed.
When needed, a real integration scenario provides a repeatable minimum loop: prepare dependencies and test data; start the system and confirm readiness; exercise the critical user path; observe output and any necessary database state, logs, or traces; clean up resources from this run; and confirm it can run again. Reuse existing entry points; do not require every project to add a browser, database, or uniform wrapper script.
Distinguish quick local checks, target-platform validation, and real integration scenarios. The first cannot replace behavior unique to the others. When an environment is unavailable, report the impact rather than removing a required acceptance item.
CI may be maintained outside the repository. Locate its entry point and version-linked result; do not infer that CI is absent because the repository has no configuration, or claim that it ran successfully merely because configuration exists.
Deliver evidence with links to the version, environment, and raw results according to [Minimum task brief and result](agent_selection.md#minimum-task-brief-and-result); do not create a complex logging system for this purpose.

## Optional Skill capability guide

Identify design, implementation, review, handoff, or SOP capabilities only from names and descriptions exposed by the current host. Do not assume the user has installed any personal Skill. Installation, availability, explicit enablement, and actual validation are distinct states.

Follow [Skill usage and conflict handling](AGENTS.md#skill-use): read or use a Skill only after the user explicitly requests it, unless a higher-priority instruction requires otherwise. Creating or installing a Skill does not automatically authorize using related Skills, committing, or publishing. Do not provide guessed commands when no entry point has been confirmed. Keep personal installation paths and adaptation records in local configuration.

## Capturing and reporting repeated actions

### Trigger criteria

Use actual repetition or recurrence of the same class of failure as the trigger; do not create a Skill mechanically after a fixed number of occurrences. Once triggered, route by the nature of the action: explain principles and methods in documentation; put deterministic actions in scripts or CI so they do not depend on memory at execution time; consider a Skill only for a stable, reusable, multi-step process that requires judgment.

### Reuse and placement

Prefer an existing entry point and extend it only when it is insufficient. Do not create a parallel version or add a wrapper merely to standardize command appearance. Exposed names and descriptions may be used to identify candidates; unless requested by the user, do not read, invoke, or follow a `SKILL.md`. Follow existing placement boundaries: put general governance in the shared guide directory, project-specific assets in an existing approved project location, and assets that truly apply across projects in a personal shared location.

A Skill's body defines when it applies, the required judgments, and its steps, while referring to authoritative rules. Put mechanical operations in scripts and load reference material only as needed. Do not copy the entire documentation set or hard-code project paths.

### Delivery notes

When a candidate offers a material benefit, include “recommended” or “not recommended yet,” the reason, its scope, and its intended location in the delivery note. Do not repeat an empty prompt for every task when no real candidate exists. A candidate does not authorize its automatic creation or installation. Once the user explicitly asks to capture it, complete that work under the authorization without asking again.

After creating or updating it, proactively provide its name, path, applicable scenarios, an explicit invocation example, actual validation results, and known limitations. Creation does not mean enablement; the host's discovery result determines whether it can be invoked. Validate at least one representative scenario and one out-of-scope boundary, with error cases proportional to actual risk. Do not claim validation if it was never run. Update or retire a stale entry point when the process changes.

## Ongoing maintenance and onboarding completion

During development, update authoritative locations according to actual impact: behavior or compatibility changes update the contract; structural changes update architecture or the necessary decision record; build, configuration, test, and environment changes update the corresponding entry points and check mapping; ongoing work updates the same task record.
Small changes with no semantic impact do not require a new spec, ADR, or task document. Consolidate duplicate rules into the authoritative location without removing justified project differences.
When repeated failures, repeated correction, or stale entry points appear, use [Workflow improvement](workflow_evolution.md) to record evidence and make the smallest correction. That guide owns periodic review, permitted automated changes, and observation or rollback; every small task does not need a formal retrospective.

Judge onboarding completion against the scope of this task: the basis and owners can be located, necessary rules are accessible to executors, relevant run and validation prerequisites and check results have been verified, ongoing work can find its record, and material gaps plus their next steps are explicit.
Onboarding cannot be called complete while a gap that blocks the current objective remains unresolved. Long-term items that do not block the current scope may be left as explicit follow-up work.
Creating rule files does not mean the project runs. Completing onboarding also does not mean that the product passed acceptance or was published. Follow the [shared completion criteria](engineering.md#persistent-records-and-completion) in the final delivery, stating the scope actually completed and the limits of the evidence.
