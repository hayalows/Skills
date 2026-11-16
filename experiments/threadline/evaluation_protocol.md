# Independent evaluation protocol: Threadline vs. a minimal baseline

## Research question

When the **same model**, source facts, reader, genre and task length are held constant, does the Threadline procedure improve the quality of the prose for readers who do not know which prompt produced it?

**Do not use AI-detector scores as the outcome.** Prose can be useful and natural without resembling the distribution of one training corpus. Do not select texts because they appear human-authored to an automated detector.

## Study design

1. **Pre-register 12 neutral briefs** in `briefs_eval.json`: short messages, informational notices, emails, explainers, an opinion piece, a reflective long essay and a technical guide. Neither method may use a personal writing-style profile.
2. **Same facts** in both conditions. Give the baseline only a minimal instruction to write naturally and clearly; give the experimental condition the full Threadline workflow. Both receive the same verified facts, length targets and uncertainty declarations.
3. **Same generation model and settings**. Fix model release, system instructions, temperature where supported, generation budget, date, and safety settings. Generate at least three independent outputs per brief per condition. Use matched seed if supported but do not assume deterministic output. If model changes, rerun both arms.
4. **No prompt leakage in judging.** Shuffle labels A/B for each pair. Show evaluators the brief, factual source packet and the two texts, but neither prompt nor method name. Keep a separate answer key.
5. **Three independent readers** per pair. Use diverse readers appropriate for the task; at least some should have no interest in religious writing or creator marketing. Ask which version is easier to use and why. Prefer real task testing for practical documents.
6. **Read long pieces in thirds**: opening, middle, ending, and the complete piece. Track whether the middle adds substance or pads, whether the ending resolves rather than recaps, whether key concepts change meaning, and whether tone drifts.
7. **Do an expert accuracy check** independent of stylistic preference, with citations to the factual packet. Text that invents an experience, fact, source, result or quotation fails an accuracy gate regardless of prose score.
8. **Hold out authors and tasks.** Never revise the algorithm after seeing its blinded holdout results. A task family used to design diagnostics cannot be used as the only proof of improvement.
9. **Publish failures.** Include judged ties, cases where Threadline loses, and cross-genre differences. Pre-register the primary metric and use paired confidence intervals rather than a chosen percentage of improvement.

## Human scoring form

For each output, rate 1–5, where 1 is seriously inadequate, 3 acceptable but needs revision, and 5 excellent for this task.

| Dimension | Weight | Specific question |
|---|---:|---|
| Reader fit | 20% | Does the reader get the information or help needed at the right time? |
| Thought flow | 25% | Does each new idea follow from what has been established? |
| Grounding | 15% | Are examples and details concrete, relevant, and clearly real or hypothetical? |
| Factual discipline | 20% | Are claims supported, uncertainty fair, and sources/experience not invented? |
| Natural phrasing | 10% | Is the voice appropriate and speakable, without unearned stock wording or choppy cadence? |
| Ending | 10% | Does the ending suit the genre and resolve the reader's purpose? |

These are **test weights**, not experimentally validated components of naturalness. Judges should also make a simple blind preference: A / B / Tie, with one sentence explaining the choice. A factually failing output must be identified separately, not hidden by a high style score.

## Primary and secondary results

- **Primary:** within-brief blinded preference rate excluding ties, plus tie rate and a bootstrap 95% confidence interval over briefs. Count any factual-gate failures separately. Do not claim causal generalization beyond the tested model/tasks.
- **Secondary:** average paired human rubric difference by dimension and genre; hallucination rate; unsupported certainty; task completion; edit time required; reader recall if a controlled comprehension test is possible.
- **Diagnostic only:** Hemingway-like grade, formulaic phrase matches, sentence-length CV, repeated five-grams, paragraph recurrence, lexical cohesion. None independently decides the winner.

## Long-form stress test

For each method, generate a **fresh 4,000-word explanatory essay** and another **fresh 4,000-word reflective essay**, each with identical fact constraints. Mark the target as approximate and report actual word count. Ask blind readers to rate:

1. Opening: clear stakes and accurate setup, with no false scene or sensationalism.
2. Middle: each section adds evidence, an example, a serious objection or a consequence, rather than repeating the thesis.
3. Ending: makes a justified advance or reaches a usable conclusion, rather than summarizing the outline.
4. Whole: coherence over distance, concept consistency, real uncertainty, reader engagement and whether anything was repeated only to reach length.

A content-neutral word-count requirement must not lead to invented data. The model can say a shorter document is more justified when evidence is insufficient.

## Reproducibility and evaluation honesty

The included test program exercises the *software* without requesting a live LLM response. It therefore checks determinism of metrics, compiler correctness, and detection of deliberately planted problems. It cannot demonstrate improved prose quality. The independent, blinded A/B trial above is defined but **has not been run** within this deliverable. Any claimed improvement percentage before it is run would be fabricated.

The corpus includes prepared speeches and professional essays. Selection and interpretation may be biased by genre, public editorial review and webpage formatting. Further testing should use workplace writing, journalism, correspondence, procedural instructions and texts by readers with varied backgrounds.
