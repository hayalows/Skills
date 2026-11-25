---
name: behavioral-interaction-design
description: "Design or audit ethical product interactions that help people start, make progress, enjoy a task, or return for a goal they chose. Use for first-use activation, onboarding drop-off, emotional design, microcopy, progress and feedback, curiosity, playful moments, voluntary challenges, gamification, defaults, and retention tied to recurring user value. Based on Stephen P. Anderson's Seductive Interaction Design. Use broader UX guidance for general layout, design systems, and full product flows."
routing:
  roles: [specialist, supporting]
  category: interaction-design
---

# Behavioral Interaction Design

Use this skill to improve a specific moment where the user needs a clearer path, a reason to act, or feedback that helps them get better. Treat each behavioral mechanism as a hypothesis about this audience and context.

## 1. Set a behavioral target

Write down the person, entry moment, current behavior, desired action, condition for success, and the benefit they would recognize. Separate the business metric from the user outcome. Define the cadence as one action, a bounded series, or an ongoing behavior. For reductions and cessation, measure the reduction itself and offer a path to stop using the intervention.

Write a concrete target such as “A returning learner resumes the next unfinished lesson from the saved position after opening a series.” An event such as opening the app is exposure. Completion requires a state change or another credible outcome signal.

If evidence is thin, label the diagnosis as a hypothesis. Read product evidence first when available, including task observations, event definitions, support reports, and the actual interface. Preserve the difference between what people say, what you observe, and what you infer.

## 2. Fix the base experience

Trace the ordinary path and one plausible failure or interruption. Check that the task works, feedback is reliable, the next action is clear, and people can recover. Distinguish functional, reliable, usable, convenient, pleasurable, and meaningful qualities. Use these as lenses. People assign meaning themselves and can value imperfect tools.

Classify the proposal provisionally as an expected basic, a performance improvement, a pleasant extra, or something the audience may be indifferent to. Test that classification with people who use the product. Prioritize a broken basic over a new extra. Keep the expected basics, user context, and cost of failure visible in the decision.

## 3. Diagnose the moment

| Evidence at the point of action | First intervention to consider |
| --- | --- |
| People want to act and miss the entry point | Place a prompt in context. Give it an action label and make it dismissible when optional. |
| People start and stall at a decision or step | Remove unnecessary work, offer a safe reversible suggestion, or give a smaller first step. |
| People can act and see little reason to | Show the immediate value, offer a useful sample, or ask what would make the task worth doing. |
| People act and cannot tell what happened | Give accurate state, next action, and recovery. Add progress only when there is a reliable denominator. |
| People want to improve and have reached a plateau | Try a skill-appropriate challenge with actionable feedback and a meaningful endpoint. |
| The task works and could feel warmer or more personal | Try optional humor, expression, a fitting visual cue, or a small gift of useful information. |

Check prompt, ability, and motivation at the same moment. Prompt only when the user can act and plausibly wants to. Where data suggests multiple barriers, compare a simpler-path option against the proposed motivational change. If intent is absent, take that seriously.

## 4. Specify and challenge one intervention

Read [mechanisms.md](references/mechanisms.md) for pattern selection and failure modes. Write the trigger, interface change, normal and fallback states, exact success feedback, control for skipping or reversing, and what the interface does on repeat exposure. Role-play the task aloud to spot premature requests and steps that can wait. For high-stakes, irreversible, or stressful actions, lead with plain information and user control. Keep the shortest safe route visible.

Reject fabricated urgency, fake activity, hidden material terms, misleading progress, pressure after refusal, and rewards that exploit uncertainty. Make paid add-ons, sharing, sensitive disclosure, and recurring commitments explicit choices. Preserve keyboard and touch access, meaningful labels, reduced-motion support where relevant, and a quiet path through the task. Treat delight as optional when it competes with clarity, dignity, privacy, or performance.

## 5. Test the mechanism and decide

Read [evaluation.md](references/evaluation.md) for decision rules, metric definitions, and test design. Compare with the existing path or a simpler variant. Pick one primary user outcome, one diagnostic event, and the safeguards that matter. Check first-use and repeat behavior if novelty could explain the result. Stop or revert on a serious harm signal even if business conversion improves.

Deliver a short interaction brief, audit finding, or experiment plan with:

- Observed moment, evidence, and confidence.
- User goal, chosen behavior, and business interest.
- Selected mechanism, exact interaction, and why a simpler option would or would not answer the problem.
- Consent, accessibility, reversibility, and failure handling.
- Outcome, denominator, window, comparison, and ship or stop rule.
- Relevant source IDs and remaining uncertainty.

## References

- [Mechanisms](references/mechanisms.md) for interventions, safe defaults, and failure modes.
- [Evaluation](references/evaluation.md) for audits, measurement, experiments, and handoff.
- [Worked cases](references/worked-cases.md) for example specs across learning, navigation, checkout, support, and professional tools.
- [Source map](references/sources.md) for all 25 chapters, the interlude, PDF locators, and research context.

When Product Design OS is available, use it for the overall flow, accessibility, resilience, and handoff. Apply this skill to the particular moment that needs behavioral analysis.
