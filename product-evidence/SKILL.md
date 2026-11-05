---
name: product-evidence
description: "Plan or assess evidence for a product decision using task-based usability benchmarks, instrumentation checks, controlled experiments, or staged rollout criteria. Use when comparing before/after product outcomes, testing a design hypothesis, diagnosing an apparent metric change, or deciding whether measured evidence supports shipping. Skip ordinary visual polish and audits that only need expert observations."
---
# Product Evidence

Turn a product claim into a testable decision. Keep the evidence method proportionate to traffic, access, risk, and the consequence of a wrong call.

1. **Frame the claim.** Name the user, realistic task, baseline, proposed change, decision owner, and decision date. Specify one primary outcome, the smallest improvement worth acting on, and guardrails for important harms. Record the unit of measurement, population, denominator, and success/failure definitions.
2. **Pick the method.** Use an expert walkthrough to catch obvious defects, representative task tests to learn where users struggle, production telemetry for observed patterns, and a controlled comparison for causal claims where feasible. Use a staged rollout with explicit stop signals when the question is operational safety. Match the strength of the claim to the method.
3. **Check the measurement.** Before interpreting movement, trace sample events through collection and reporting. Check duplicate events, missing paths, event changes, denominators, exposure, and date windows. For experiments, define assignment unit, duration, stopping rules and guardrails before launch. Check assignment imbalance and contamination before trusting effects.
4. **Run the smallest credible comparison.** Keep tasks, conditions, and success criteria comparable. Use realistic inputs and examine mobile, accessibility and slow connections where relevant. For search or ranking, separate tuning and holdout cases, include difficult slices and report failures alongside aggregate results. Keep participant and analytics data within the approved scope.
5. **Make a bounded call.** Show baseline, result, sample size, uncertainty, guardrails and plausible alternate explanations. State ship, iterate, stop, or insufficient evidence. A design can still ship for a clearly stated reason when uplift remains unmeasured. Apply host release rules and user authorization separately.

Read [Decision records and examples](references/methods.md) for comparisons, experiment planning, and low-traffic cases. Use Product Design OS for design decisions and Website UX Audit for expert diagnosis. Bring this skill in when measuring the outcome changes the next action.
