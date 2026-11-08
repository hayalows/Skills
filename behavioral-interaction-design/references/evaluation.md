# Evaluate a behavioral design

## Audit one moment

1. Name the surface, person, device, intent, and point of failure. Record a screenshot or state description, observed behavior, and consequence when available.
2. Map entry, available actions, state after action, error, back, exit, and re-entry. Include the cost of doing nothing and any effect on other people.
3. Classify the barrier as missing value, low ability, weak prompt, ambiguous feedback, or broken basics. Give the strongest competing explanation. Assign severity by user impact and confidence by the quality of evidence.
4. Choose a simpler repair and, where useful, one behavioral variant. Describe exactly what changes and how a user can skip it. Use concept tests for intent and comprehension, walkthroughs for missing states, and behavior data or experiments for impact.
5. Review costs and safeguards. Check total price or material terms, consent, access parity, interruption, text equivalents, keyboard interaction, reduced motion, retry, and dismissal as applicable. Use the current accessibility standard for the target surface. [R18–R19]

## Set outcome, diagnostics, and guardrails

| Target | Primary outcome | Diagnostic | Guardrail |
| --- | --- | --- | --- |
| First useful action | Eligible people completing the meaningful action within the agreed window | First-step starts and drop-off by step | Errors, forced permission, inappropriate disclosure |
| Better decisions | Eligible people choosing an option and accurately understanding what it costs or does | Comparison opened, material terms viewed | Regret, cancellation, hidden lower-cost paths |
| Learning or mastery | Eligible learners demonstrating the target skill at a defined interval | Challenge acceptance, attempts, use of hints | Accessibility gap, unfair difficulty, decline in voluntary practice |
| Useful return | People with a recurring goal completing the next relevant action | Prompt shown, resume selected, progress restored | Opt-outs, repeated dismissal, pressure, lost work |
| Useful delight | People who receive and voluntarily use a helpful extra | Viewed, dismissed, saved, or shared | Task delay, embarrassment, motion or performance regressions |

Define eligibility before exposure. Separate exposure, action, and verified success. Use a stable assignment unit, commonly a person or account when they can return on multiple devices. Deduplicate retries and test tracking on both branches. Distinguish intent-to-treat estimates from the behavior of people who elected to use a feature. Use only data needed for the decision. If the question is completion among all first-time starters, assign at the first start and include people who never return. If the question is what happens after a return, assign at that return and state the narrower population.

A useful metric includes numerator, denominator, window, segments, exclusions, and the change that would matter. Example: eligible signed-in learners who resume and complete the intended lesson within seven days, divided by all eligible signed-in learners assigned at a series return. Check that the lesson was the intended next one and that completion came from a reliable signal. Use a comprehension or practice outcome for any claim about learning.

## Choose a test and a decision rule

- For low traffic or an early concept, run task walkthroughs with plausible users on representative devices. Ask them what they expect before action and what happened afterward. Include an opt-out and an interruption. Use observations to find defects and refine the hypothesis.
- For a causal estimate with adequate traffic, randomize concurrent variants, choose sample size and duration from baseline, meaningful effect, and uncertainty, and write the decision rule before launch. Avoid simultaneous changes that prevent interpretation. Check assignment, event duplication, sample imbalance, and major channel or segment differences.
- Where repeat behavior matters, compare new and returning people and define a later window before interpreting an early spike. Use a holdout or persistence check when practical.
- Ship when the relevant user outcome meets the agreed decision threshold, important harms stay within bounds, and implementation passes accessibility and resilience checks. Iterate when the diagnostic changes and the outcome remains uncertain. Stop when agency, safety, or task quality worsens materially. A qualitative test supports a design judgment, while an adequately designed experiment can support a causal estimate.

## Handoff fields

Provide the observed issue, hypothesis, exact microcopy and interactions, trigger eligibility, state diagram or table when useful, repeat policy, cancellation, state persistence, data collection, accessibility behavior, test cases, evidence IDs, and the accountable decision. If metrics or sample size are unknown, ask the team to fill in the missing quantities before exposure. Keep example thresholds explicitly hypothetical.
