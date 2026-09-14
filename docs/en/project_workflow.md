# Project onboarding

[简体中文](../project_workflow.md) · **English** · [Documentation](../../README.md#guides)

Preserve project conventions; fill only the entry-point and evidence gaps the task needs.

## Purpose and triggers

This guide establishes, checks, and maintains project-specific rules. It stores no project's business facts and prescribes no directory tree. Shared policy lives in [engineering.md](engineering.md); delegation and evidence delivery follow [agent_selection.md](agent_selection.md).

Use it for a first entry with unknown readiness, an explicit request to establish or overhaul a workflow, or a rule, context, run, or acceptance gap that affects the current task. Reuse valid onboarding knowledge. Routine work fills only necessary gaps; a full inventory requires an explicit request.

Rule work needed by an authorized objective may proceed. Consultation or read-only review only reports. This guide does not expand file, network, data, or budget permission, require repeated confirmation, or automatically create or enable Skills.

## Shared preparation and sources

Identify project root, task scope, user changes, and team rules, then locate:

| Fact | Preferred source |
| --- | --- |
| Target behavior/constraints | Accepted requirements, project AGENTS, README, contracts, decisions |
| Current structure/paths | Relevant code, build/deploy configuration, architecture |
| Correctness checks | Test instructions, scripts, registration, CI, target environment |
| Work resumption | Issues, plans, investigations, internal documents, evidence indexes |

Use the [source rules](engineering.md#intended-behavior-and-source-authority) to separate contracts, descriptions, observations, and unknowns. Code, tests, and historical reports do not automatically define the correct contract. Do not invent performance, compatibility, recovery, or retention rules to fill a template.

Do not inspect unrelated directories, credentials, or operational data, or connect to a listed device without need. Record inaccessible entry points and their effect.

## New projects: build with the first increment

1. Define users, core scenarios, goals/non-goals, hard constraints, first result, and acceptance basis.
2. Root decides technical and structural tradeoffs. Workers organize sources, validate feasibility, and execute the choice; keep key open decisions explicit.
3. Establish one complete runnable, verifiable path plus necessary dependency, build, run, and check entry points.
4. As facts become established, write minimum project AGENTS, usage, and acceptance guidance; related sections may share a file.
5. Add constraints, checks, and knowledge by semantic impact; label unverified assumptions.

Do not prebuild a documentation tree, Skill collection, multi-Agent framework, or unused wrapper scripts. A requirements/design-only task does not establish a runnable project.

## Existing projects: baseline and minimal additions

1. Confirm local gap-filling versus an authorized workflow overhaul; preserve user changes and team conventions.
2. Locate rules, contracts, knowledge, and real paths; reuse existing owners.
3. Check test entry points, dependencies, registration, and versioned results. Separate old failures, environment issues, unrun checks, and new defects.
4. State what remains, what changes, where duplication returns, and key unknowns; proceed when existing authorization suffices.
5. Change incrementally and validate against project gates. Update affected documents and the same task record; leave out-of-scope governance as follow-up.

Do not move directories, rewrite architecture, or copy shared guides to fit a template. Do not promote accidental behavior to contract or remove it before compatibility impact is understood. Off-repository documentation, deployment boundaries, and confidentiality rules remain active.

## Responsibilities of project-level AGENTS

Keep project AGENTS short. Include only:

- authoritative locations for contracts, architecture, acceptance, and internal material;
- required business truths, ownership, state, and compatibility boundaries and their definitions;
- configuration, command, and acceptance entry points for changes;
- justified stricter requirements and project operating boundaries.

Do not copy shared delegation, model, risk, review, or completion policy. State its concrete project mapping. Detailed documents need no standard names; forward other CLIs to the same rules through their actual loading mechanisms.

Executors must reach the rules. Do not put personal paths in a team repository. Transfer across machines/CLIs through the [collaboration guide](agent_selection.md#minimum-task-brief-and-result). State inaccessible rules; do not claim they were loaded or inherited.

## Documentation and ongoing context

Each class of fact has one authoritative owner; other files link to it. Contracts, architecture, important decisions, ongoing task state, and runtime evidence may live in different approved repository or internal systems. Raw evidence needs a locatable, version-linked index.

For record and resumption rules, see [context management](engineering.md#context-management-and-resumption). Git history does not replace hypotheses, failed experiments, and next step in unfinished work. Short tasks need no new record; long tasks should not have duplicate records.

Locate internal material by approved identifier, version, or index. Credentials, sensitive operational data, and personal paths must not enter public/team repositories. Record only known leads and gaps for unknown internal locations; do not invent links or claim updates. Ask only when a gap blocks necessary work.

## Testing and acceptance

Map the [evidence](engineering.md#evidence-and-confidence) and [independent review](engineering.md#independent-review-policy) rules to affected scope, real check entry point, required environment, scenarios/expected criteria, and result location. Reuse existing documentation or CI when sufficient.

Verify dependencies, registration, paths, and commands, and run checks required by the objective. File presence, test registration, and historical green results do not prove the final version passed.

When needed, integration covers data setup, readiness, critical path, external state/log observation, cleanup, and repeatability. Distinguish local, target-platform, and real integration checks. Preserve required acceptance items and report unavailable environments. CI may live outside the repository; locate its entry point and versioned result.

Deliver evidence through [Minimum task brief and result](agent_selection.md#minimum-task-brief-and-result); do not build a complex logging system.

## Optional Skill capability guide

Identify candidates only from host-exposed names and descriptions. Installation, availability, explicit enablement, and validation are separate states. Under [Skill usage](AGENTS.md#skill-use), read or use a Skill only after an explicit user request. Creation/installation does not authorize related Skills, commits, or publication. Do not guess unconfirmed commands; keep personal paths and adaptation records local.

## Capturing and reporting repeated actions

### Trigger criteria

Trigger on actual repetition or recurrence of the same failure class, not a fixed count. Put principles in documentation and deterministic actions in scripts/CI. Consider a Skill only for a stable, reusable, judgment-requiring multi-step process.

### Reuse and placement

Extend an existing entry point before creating a parallel version or cosmetic wrapper. Without a user request, do not read, invoke, or follow SKILL.md. Place shared governance, project assets, and cross-project personal assets within existing boundaries. A Skill references authoritative rules; scripts hold mechanics. Do not copy all documentation or hard-code project paths.

### Delivery notes

For a material candidate, report recommended/not yet recommended, reason, scope, and location. A candidate does not authorize creation or installation. Once explicitly requested, complete capture without reconfirmation.

After creation/update, proactively give name, path, scenarios, explicit invocation example, actual validation, and limitations. Creation is not enablement; host discovery determines availability. Validate one representative and one out-of-scope scenario; never claim an unrun validation. Update or retire a stale entry point when the process changes.

## Ongoing maintenance and onboarding completion

Update owners by impact: behavior/compatibility updates contracts; structure updates architecture/decisions; build/configuration/test/environment updates entry points; ongoing work updates one record. Small nonsemantic changes need no new spec, ADR, or task file. Route recurring failure and stale entry points through [Workflow improvement](workflow_evolution.md).

Onboarding is complete only when, within this scope, sources and owners are locatable, rules reachable, run/validation prerequisites and results verified, ongoing records findable, and material gaps and next steps explicit. A gap blocking the current objective blocks completion.

Rule files do not prove the project runs. Completed onboarding does not mean product acceptance or publication. Report actual scope and evidence limits under the [completion criteria](engineering.md#persistent-records-and-completion).
