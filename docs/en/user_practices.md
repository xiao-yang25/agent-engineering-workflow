# Working with AI: a guide for people

[简体中文](../user_practices.md) · **English** · [Documentation](../../README.md#guides)

For people using agents on engineering tasks, focusing on task definition, context, authorization, execution, correction, acceptance, and reuse. Select advice by task; a simple request can be stated directly. Existing guides continue to define engineering responsibilities, authorization, and acceptance. This guide adds no mandatory process.

## Sources and applicability

Sources checked on 2026-10-05. Research findings, engineering experience, and personal views are distinguished below. The subsequent practices synthesize these with this workflow; their effects require evidence from real tasks.

| Primary source | Supported insight | Limits |
| --- | --- | --- |
| [Dell’Acqua et al.: Jagged Technological Frontier](https://www.hbs.edu/ris/Publication%20Files/dell-acqua-et-al-2026-navigating-the-jagged-technological-frontier_5c589c8c-fbb5-458f-b285-c944746cd717.pdf), 2026 publication | In the consultant experiment, effects varied by task; more persuasive outputs could coexist with lower correctness | GPT-4 and selected consulting tasks do not predict current-model or personal productivity |
| [Microsoft Research: GenAI and critical thinking](https://www.microsoft.com/en-us/research/publication/the-impact-of-generative-ai-on-critical-thinking-self-reported-reductions-in-cognitive-effort-and-confidence-effects-from-a-survey-of-knowledge-workers/), 2025 | A survey of 319 knowledge workers associated higher AI confidence with less critical thinking; human work shifted toward verification, integration, and task stewardship | Self-reports support associations, not a causal claim of long-term skill decline |
| [Anthropic: AI assistance and coding skill formation](https://www.anthropic.com/research/AI-assistance-coding-skills), 2026-01-29 | A short learning experiment with 52 mostly junior engineers found lower mastery in the AI group; comprehension-oriented use patterns were associated with better learning | Immediate testing does not establish long-term effects; the pattern analysis is not causal, and the setup differs from agentic work |
| [Karpathy: Sequoia Ascent 2026](https://karpathy.bearblog.dev/sequoia-ascent-2026/), 2026-04-30 | Emphasizes human understanding, engineering judgment, and verification when delegating work | Personal views in an AI-edited summary and transcript checked by the author, not an effectiveness experiment |
| [METR: Task Substitution and Uplift](https://metr.org/blog/2026-05-08-task-substitution-and-uplift/), 2026-05-08 | Speedup on old tasks, speedup on new tasks, and growth in output value are distinct measures | A conceptual analysis with assumptions; cheaply generated new artifacts do not automatically add value |
| [Anthropic: Context Engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents), 2025-09-29 | Recommends sufficient relevant context, representative examples, and source entry points loaded as needed | Engineering experience does not prove that a prompt format or shorter context is always better |
| [Anthropic: Agent Evals](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents), 2026-01-09 | Distinguishes execution records from final environment state and recommends regression cases with attention to run variability | Evaluation methods do not replace domain-specific acceptance criteria |

## Human work habits

1. **Choose a worthwhile problem first.** State whom the result serves, the next decision, and how completion will be judged. Prioritize even when generation is cheap; omit artifacts without a practical use.
2. **Distinguish delivery, learning, and exploration.** Delegate fuller increments for familiar work you can assess. When learning unfamiliar mechanisms, request explanations, examples, and feedback, then explain them yourself or do a small exercise. For exploration, request options, evidence, unknowns, and the next experiment. A task may have several goals; state them as needed.
3. **Provide usable context and room to execute.** Supply key files, constraints, versions, positive/negative examples, and priorities. Reference existing entry points for stable information and update one-task exceptions in the current task. Fill gaps as they emerge; a perfect initial prompt is unnecessary.
4. **Match delegation to acceptance capability.** Delegate a complete assessable outcome when you can judge it. For unfamiliar or hard-to-verify work, establish a verification method or obtain appropriate review first. Human purpose, business tradeoffs, and authorization complement Root's engineering judgment and final acceptance; existing collaboration rules define responsibilities.
5. **Check material conclusions actively.** For important decisions, ask about conditions, counterexamples, and evidence that would change the conclusion, then inspect original sources or actual state. Agreement across model responses still needs evidence. Correct specific omissions and say whether the original goal remains valid.
6. **Plan parallelism around attention.** Complete an assessable increment, then increase parallel work according to independence and your review capacity. Preserve stable goals and respond to necessary decisions promptly. The agent continues within existing authorization; collaboration rules define the limits.
7. **Learn from actual outcomes.** Try the real usage path at acceptance. Revisit decisions needing your involvement, steps suitable for continued delegation, and rework caused by goal or context gaps. Return reusable cases and evidence indexes to original records. Compare quality, observed time, human corrections, and rework; keep unknowns when data is insufficient.

## Mapping to the existing workflow

“Covered” means the guide defines an agreement, not that every real task has followed it.

| Human concern | Existing workflow entry | Useful human action |
| --- | --- | --- |
| Goals, tradeoffs, completion | [Process depth](engineering.md#select-process-depth), [acceptance evidence](engineering.md#evidence-and-confidence) | State purpose and delivery/learning/exploration goals; simple tasks need no mandatory form |
| Context and continuity | [Context management](engineering.md#context-management-and-resumption), [project records](project_workflow.md#documentation-and-ongoing-context) | Point to authoritative material and explicitly update goals; reuse records instead of adding a memory store |
| Delegation and review capacity | [Agent collaboration](agent_selection.md) | Assign assessable outcomes; increase parallelism only as results can be accepted promptly, without expanding executor authorization |
| Source checks and counterexamples | [Source authority](engineering.md#intended-behavior-and-source-authority), [independent review](engineering.md#independent-review-policy) | Check assumptions at important tradeoffs; counterexample discussion does not replace required independent review |
| Understanding and presentation | [Expression and delivery](engineering.md#expression-and-delivery) | Request explanations, diagrams, or interaction that aid understanding; check whether you can explain the key mechanism |
| Whether improvement works | [Real-task regression set](workflow_evolution.md#small-regression-set-from-real-tasks) | Register real corrections and successes in the existing private index and observe outcomes and rework; add no universal score or automatic collection now |

Try three actions first: state the main goal at the start, verify a key fact or counterexample at an important decision, and revisit a real cause of rework after delivery. Use them as needed; add no fixed-count confirmation, explanation, or retrospective gates. Do not add rules without new evidence.

## Working through a task

For a new project, clarify goals/non-goals, hard constraints, key approaches and technology choices, stage outcomes, acceptance, and available material as needed. Distinguish accepted decisions, assumptions to validate, and details the agent can handle autonomously. Use bounded experiments for unknown feasibility; implementation need not wait until every detail has been discussed. Reuse the existing design and project-onboarding guides.

- **Start:** State purpose, outcome, key materials, acceptance, and permitted scope. Add tradeoffs and learning goals for complex or unfamiliar work.
- **During:** Let the agent continue authorized work. Respond to necessary decisions and correct concrete deviations; say whether a change supplements or replaces the original goal.
- **Delivery:** Inspect artifacts, key validation, and unverified items, and try the intended usage. The agent remains responsible for required validation; the user need not repeat every check.
- **Continuity:** Retain important decisions, unfinished work, and evidence entry points. Handle recurring problems through the existing workflow improvement mechanism.

## Questions and context

A complete specification is not required upfront. The agent should locate existing material first, then help fill gaps affecting the next step under the [clarification principles](engineering.md#clarifying-the-task-with-the-user). These are optional prompts, not questions to answer on every task.

| Aspect | Useful context or questions |
| --- | --- |
| Purpose and boundary | Who uses this and in what situation? What is the first outcome? What is explicitly outside this task? |
| Constraints and tradeoffs | What must remain compatible? Which matters most: time, cost, or maintenance? Which choices should you recommend and explain? |
| Material and examples | Which files are authoritative? Is there a preferred result, unacceptable counterexample, or existing failure? |
| Acceptance and scope | How can I try or verify the result? What may you change and execute? Which decisions need me? |
| Understanding and continuity | Which explanation form helps? What is assumed? Which decisions and evidence does the next phase need? |

Example requests and corrections:

- **Start:** “The first version is for my own use. Complete one usable scenario first. Read the existing material, identify decisions that are genuinely missing, and recommend options; handle other details autonomously within the permitted scope.”
- **Tradeoffs:** “Compare two realistic approaches, recommend one, and explain its costs and what evidence would change your recommendation.”
- **Understanding:** “I do not understand this retry mechanism. Start with a numerical example; if interaction would help, make an explanation with adjustable parameters.”
- **Correction:** “The result omits the offline scenario, and the original goal still applies. Add boundary validation and explain which conclusions need to change.”

## Discussing concrete results

- For an unclear goal, start with a minimal sketch or usable sample and narrow the requirement through feedback. This does not automatically approve full implementation or publication.
- Use positive examples and counterexamples to show quality differences, identifying whether they concern content, behavior, or presentation. Do not leave the agent to guess what “more professional” or “better looking” means.
- Inspect a short tradeoff summary for important choices. If repeated corrections make no progress, ask the agent to compare competing hypotheses and propose the next discriminating experiment, reusing existing design and debugging methods.
- At delivery, request a usable entry point, key validation, and limits. Select explanation artifacts under the [production guide](explanation_artifacts.md); they cannot replace product acceptance.

## Reusing successful examples

Start with a verified artifact and retain the inputs, key decisions, corrections, acceptance evidence, versions, and applicability needed for reuse. Keep location indexes for the original process rather than copying whole conversations. Artifact acceptance does not establish an efficient collaboration method, and one success does not establish reliable gains. Maintain artifacts and methods in the original project or task. Register cases comparing workflow changes only in the existing private index under the [regression rules](workflow_evolution.md#small-regression-set-from-real-tasks); do not create a separate case library.

## Choosing the workflow's form

| Content | Suitable carrier | Basis for adding a mechanism |
| --- | --- | --- |
| Human methods and tradeoffs | README and this guide | Read as needed for human understanding |
| Engineering constraints and methods | Short entry point and specialist guides | Entry navigation and on-demand text; one maintained location per rule |
| Stable repeatable actions with decidable outcomes | Existing scripts, tests, or CI | Automate for evidenced repetition or missed checks, and verify execution |
| Progress, decisions, runtime evidence | Original task records and permitted private indexes | Locate current state, versions, and open items |
| Stable reusable multistep work requiring judgment | Optional Skill | Assess under [capture rules](project_workflow.md#capturing-and-reporting-repeated-actions); create or enable only on explicit request |

The current form can remain “document entry points + executable checks + task evidence.” Documents express principles for review, the host enforces actual permissions, and real execution supplies check results. Evaluate a platform or extra tool only when the current carrier has a concrete gap. This guide changes no models, authorization, schedules, or project configuration.
