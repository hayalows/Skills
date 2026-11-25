# Evidence-first evaluation contract (v1.2)

## Lock the rubric

Before generating or inspecting the candidate, record a run ID, brief, immutable source revision or fixture, allowed actions, criteria, weights, minimums, methods, owner and expected evidence. The rubric is a decision aid, not a claim that all relevant quality has been captured. A generic starting point is correctness 30%, completeness 25%, evidence 20%, practical usefulness 15%, reliability and safety 10%. Adapt to the actual task before evaluation. Required truth, safety, consent, factual integrity and scope gates cannot be averaged away.

For objective facts, executable tests and arithmetic, use a deterministic check against actual inputs or a verified source. Use a human rating for personal preference; a model cannot establish the owner's preference. A model may assess subjective craft using explicit anchors, excerpts, rationale and limitations. Separate independent model calls from same-model simulation. A source citation is a pointer, not proof; inspect the claim at that reference. A trusted host must bind each observation to the current candidate, criterion and run, and check its authenticity. Never accept worker-authored test receipts or evaluator self-assertions as trusted records.

## Compute, do not guess

Each criterion carries a score 0–100 or unknown, weight, source, method, evidence and any required floor. The total is the weighted sum only if every criterion is assessed. Unknown contributes a range from zero to its full weight, not a fabricated value. Report weighted coverage and evidence types separately from the score. A 100 is limited to the frozen rubric, not a claim of perfect work or high statistical confidence. Report uncertainty qualitatively or from actual measured sampling; do not invent confidence percentages. For deterministic checks, use binary pass/fail and split graded subchecks if useful. Editorial ratings are subjective and must be labelled. Never round a borderline score into passing.

Default pass: at least 85/100, full coverage and all mandatory floors met. Missing evidence is unverified, even if an optimistic score could pass. A fabricated source, unauthorized effect, false execution claim, materially missing requirement or unresolved safety concern blocks acceptance. Required model gates need real independence if used; objective proof requires a suitable objective verifier. A rubric should explicitly include all material gates. An optional improvement is not a blocker. If a critic returns an apparent blocker, inspect it and adjudicate before a real release; the reference runner's optional critic callback is deliberately non-authoritative. To make adversarial review a programmatic gate, register a trusted verifier as a mandatory criterion with a suitable floor.

## Repair and compare

Route the actual failing requirements, not the overall score, to the worker. Retest all criteria with identical inputs, or start a separately identified run if the task or rubric changes. Track candidate history, including failures and unknowns. Never hide regressions. Preserve a best reviewed candidate as inspectable data, never as permission to ship. Do not repair missing proof by rewriting a claim into a pass. If a run is incomplete, escalate or return a safe, clearly labelled partial.

A controlled fault injection demonstrates detection/wiring. It does not prove increased model ability. For model comparisons, freeze fresh tasks, isolate generation calls, blind judges where possible, use the same settings, record call IDs and actual costs, include ordinary/simple baselines, and separate development cases from held-out cases. For model-based evaluation, compare against real human judgements when they matter. Report task-level results, coverage, disagreement, latency, actual spend, sample size and uncertainty; leave absent values unknown. Do not combine synthetic deterministic checks with LLM preference rates.

## Logs and consent

Record run ID, version, pinned sources, rubric, tool observations, criterion evidence and provenance, round scores, blockers, repairs, outcome, approval scope and measured time/cost if available. Do not expose private candidates, credentials or raw approval payloads in public logs. A weekly review identifies one recurrent failure, proposes a measurable change and compares with the baseline on fresh and regression tasks. Changes to a live workflow need approval. Never schedule, spend or publish just because a score passes.
