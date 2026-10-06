# Producing explanation artifacts

[简体中文](../explanation_artifacts.md) · **English** · [Documentation](../../README.md#guides)

Use this guide to explain engineering mechanisms, tradeoffs, or validation results. Load it as needed when producing text, diagrams/images, interactive HTML, or explanatory video. [engineering.md](engineering.md#expression-and-delivery) owns general presentation and evidence requirements. These methods and examples neither require several forms on every task nor establish that a production tool is installed or usable.

## Establish the explanation goal

Reuse the task's audience, prior knowledge, question to understand or decide, sources, and acceptance criteria. Fill only missing information and help select under the [clarification principles](engineering.md#clarifying-the-task-with-the-user). Replace “looks good” with a checkable goal, such as “identify how retry waits grow and which elapsed time the diagram excludes.”

| Understanding needed | Preferred form | Basis |
| --- | --- | --- |
| One conclusion, step, or condition | Clear text and numerical examples | Direct explanation with little production effort |
| Compare options | Table | Compare the same dimensions |
| Relationships, data flow, or spatial position | Diagram/image | See objects and relationships together |
| Change parameters and observe consequences | Interactive HTML | Explore scenarios directly |
| Continuous change or a derivation in steps | Explanatory video | Time or motion aids understanding |

Select by the need for understanding. Start with a sample and expand through feedback when useful; honor an explicitly requested form and explain material feasibility gaps. Tools, installation, external data transfer, and Skills follow existing authorization. Use available capabilities without silently introducing services or dependencies.

## Clear text and ASD-STE100 principles

Use clear subjects and actions, keep each sentence focused on one main idea where practical, order steps explicitly, and use consistent terms. Preserve conditions, negation, exceptions, units, and uncertainty. Define necessary technical terms rather than deleting material mechanisms to simplify the text.

| Vague expression | More actionable expression |
| --- | --- |
| “Take appropriate action when necessary.” | “Record a failure when a request times out. Retry only requests covered by the accepted retry rules.” |
| “The operation should be performed prior to proceeding.” | “Save the file before you continue.” |

A rewrite cannot add rules absent from the original. The timeout and retry behavior in the first row applies only if the project contract accepts it. Compare facts, conditions, and references before and after rewriting, then check whether the intended reader can act or understand.

ASD-STE100 is an English standard with writing rules and a controlled dictionary. This workflow borrows clarity principles; ordinary rewrites and Chinese text are not claimed to comply. For an explicit compliance task, obtain the applicable edition, check its rules and dictionary, and report coverage and gaps. A prompt or automated checker alone does not establish complete compliance.

## Diagrams and images

1. Identify objects, relationships, directions, and the question the image answers. Prefer editable Mermaid, SVG, or existing project tools for technical relationships. Use spatial illustrations, photographs, or other imagery where needed; decorative images cannot replace technical relationships.
2. Make a minimal diagram first. State whether arrows represent calls, data, control, or time, and use a legend when mixing them. Supply verifiable text, numbers, and formulas; check text and relationships in generated images individually.
3. Render and inspect labels, overlap, direction, legends, units, and contrast at the actual viewing size. Distinguish important categories beyond color and include a short text explanation. Scientific data plots use actual data and reproducible plotting methods.
4. Retain editable sources and the final image. Identify illustration, measurement, or inference and link to data and versions. Critical relationships must not depend solely on a low-resolution image.

For “does a successful commit establish a successful deployment?”, show local commit, remote receipt, build, and deployment states separately, with an observation source for each. Mark a step complete only when it actually occurred and has evidence.

## Interactive HTML

1. Define the model, parameters, ranges, units, defaults, and expected results, including simplifications and excluded scenarios. Verify calculations before designing controls. Interaction cannot turn an unverified assumption into a fact.
2. Use existing web capabilities. A simple model can use one HTML/CSS/JavaScript page with SVG. Label inputs visibly, show units, and provide reset. Keep controls, current results, and explanations understandable together; do not convey important states through color alone.
3. Run the actual page and operate its key controls. Check defaults, boundaries, invalid inputs, reset, and result updates. Verify material calculations against independent numerical criteria. Check keyboard operation, viewing sizes, and relevant browser errors. Source inspection alone does not pass interaction acceptance.
4. Deliver an openable page and sources with operating instructions, dependencies, and coverage gaps. If offline use is required, test with the network disconnected; a saved file alone does not establish offline operation.

A bounded example explains exponential backoff. The wait before retry k is d × 2^(k−1). With n retries and no cap or jitter, total waiting is d × (2^n−1). Allow d from 0.5 to 2 seconds and integer n from 0 to 4. Fixed criteria include 0 for n=0 and 7 seconds for d=1, n=3. Show individual and cumulative waits, stating that request execution, timeouts, caps, and jitter are excluded. This teaching model establishes neither the real service's retry behavior nor whether retrying is appropriate.

## Custom explanatory video

Establish the audience, mechanism to understand, duration, and deliverable. Suggest a duration when it is unspecified and does not block production. When drawing on 3Blue1Brown's approach to derivations, give each scene one explanatory step, align object changes with narration, and allow time to read the conclusion. Mathematical animation may use an available Manim Community setup or existing project tools; a visual style does not guarantee effectiveness.

1. Build an outline from verified text or a model, stating the conclusion, conditions, and example. Correct the content before making animation.
2. Prepare a short storyboard with each segment's visuals, narration/captions, numbers or formulas, duration, and transition. If content or form is uncertain, preview a representative segment before producing the entire explanation.
3. Produce the agreed storyboard, check motion, layout, and pacing in inexpensive previews, then export the final file. Create and verify narration and captions as the deliverable requires.
4. Play the final video. Check the complete explanatory sequence, key frames, transitions, formulas, narration/caption consistency, and readability. Listen to any audio track. Successful rendering establishes file generation, not explanation correctness or audience understanding.
5. Deliver the video and reusable scripts/sources, adding a text summary, sources, and limits as needed. Record actual tool versions and checks. State gaps if rendering, playback, or audio review is unavailable; do not claim complete acceptance.

The retry example can use this storyboard: one failure and model boundaries → waits of 1, 2, and 4 seconds appear → cumulative waiting reaches 7 seconds → compare changed parameters and restate excluded time. Formulas and narration use the same symbols, units, and results; animation reveals accumulation in steps. Do not imply that all failures should be retried.

## Production and delivery evidence

Reuse the original task record for the explanation goal, source/data locations and versions, material assumptions, source files, final artifact, and actual checks. File generation, correct presentation, correct model calculations, verified system behavior, and human understanding are different conclusions; report according to evidence. Add no fixed question, restatement, or publication-approval ritual. For learning tasks, optionally ask the user to predict a parameter change or explain the mechanism to determine whether the explanation needs adjustment.

Shared guides retain reusable methods. Artifacts and personal material remain in locations permitted by the original task; producing an explanation does not move them into this public repository. Assess stable repeated steps with evidence of missed checks under the [capture rules](project_workflow.md#capturing-and-reporting-repeated-actions). Creating or enabling a Skill still requires an explicit request.

## References and limits

These primary sources describe methods or tool entry points, not automatic activation. This guide synthesizes them with the workflow; it offers no experimental proof that changing a presentation form always improves outcomes.

- [Official ASD-STE100 explanation](https://www.asd-ste100.org/faq.html): writing rules and the controlled dictionary. A public summary appeared in earlier search results; direct access on 2026-10-06 returned 403. The full formal standard has not been verified.
- [Anthropic: Building effective agents](https://www.anthropic.com/engineering/building-effective-agents): task discussion, autonomous execution, environmental feedback, and adding complexity as needed. Methods are not measurements of this workflow's effectiveness. Checked on 2026-10-06; tool examples need verification in the actual environment.
- [3Blue1Brown: Manim production demo](https://www.3blue1brown.com/lessons/manim-demo/) and [the author's tool explanation](https://www.3blue1brown.com/about/): an animation production example and differences between the original and Community versions. They do not verify the current tool setup. Checked on 2026-10-06.
- [Manim Community Quickstart](https://docs.manim.community/en/stable/tutorials/quickstart.html): Scene, preview, and rendering entry points. Check dependencies and invocation for the actual version. Checked on 2026-10-06; not installed or run in this task.
