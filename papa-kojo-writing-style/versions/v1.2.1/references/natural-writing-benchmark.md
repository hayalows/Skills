# Natural Writing Evidence Suite 0.1: reusable benchmark

**Status:** experimentally defined, tested in one six-version evaluation on 16 November 2026. This is a benchmark design, **not** an independently validated measure of authorship or a certification of human-sounding writing. Its author was also the first evaluator. Never market its scores as objective quality.

## Why this is different from a readability checker
### Long-form extension: new evidence requirements

The original 18 samples across three shorter writing tasks did **not** establish performance on a 3,000-word essay. The user tested a Divine Design essay at **66.3 Flesch Reading Ease, Grade 7.3, 3,052 words**, against the shorter approved refined v1.2 calibration at **93.0 FRE, Grade 3.6, 361 words**. These are different texts, so the difference is not a causal length estimate.

The new [long-form suite](../benchmarks/longform/README.md) specifies eight longer writing prompts, matched across four versions (v1.2, v1.2.1, v1.3, v1.4) and three isolated model invocations each. Human reviewers use a sharper 13-series rubric, must quote the specific text behind their ratings, and audit 30 sentences from the beginning, middle and end. **Natural personal voice (18), emotional honesty (14) and sentence craft (11) together receive 43/100**; factual safeguards remain a blocking gate. Scores stay pending until real model runs and blind reviews exist. Do not add these scores to the original 100-point total, and do not imply that 96 completed essays already exist.


Flesch Reading Ease is an estimate of word and sentence complexity. It cannot tell whether a statement was invented, who the reader is, if someone sounds rushed, or if a point feels genuine. The scoring suite therefore has **12 editorial series** and separate hard gates. The existing `voice_check.py` provides *diagnostic metrics only* and does **not** contribute points to the 100-point editorial total.

## The 12 series and 100-point total

| Series | Weight | Core question |
| --- | ---: | --- |
| Truth and agency | 15 | Does every event, belief and feeling have permission or honest framing? |
| Reader and relationship | 10 | Would the intended reader feel correctly addressed? |
| Natural spoken voice | 15 | Does this sound like a person who means it? |
| Reasoning and depth | 10 | Does the thought advance, not merely repeat? |
| Clarity and comprehension | 10 | Can the reader explain the point back correctly? |
| Emotional precision and care | 10 | Is emotion earned rather than advertised? |
| Specificity and evidence | 8 | Is detail grounded and doing useful work? |
| Transitions and coherence | 6 | Does every paragraph follow from the previous one? |
| Pacing and rhythm | 5 | Does the text give important thoughts enough space? |
| Restraint and template resistance | 5 | Does it avoid predictable AI-like construction without banning grammar? |
| Ending and useful outcome | 4 | Does it stop in a way that serves the reader? |
| Genre and format | 2 | Would it work where it will actually appear? |
| **Total** | **100** | |

Each series has **four observable diagnostic questions**, recorded in `benchmark_config.json`. A trained reviewer rates the whole series on a 0–4 scale, with a short explanation citing words or decisions in the text. 0 means a material failure, 1 weak, 2 mixed, 3 strong, 4 excellent for the specific task. The software computes:

`overall = Σ(series_weight × series_rating / 4)`

No automated style rules secretly contribute to that overall score. A half-point change in a 15-point series can matter more than a difference of 10 Flesch points; this is a deliberate editorial value choice and must be open to revision after human validation.

## Hard gates

A verified material falsehood, fabricated personal experience/quote, or major failure to obey the brief yields **no valid overall score**, not an average with a small penalty. A draft whose facts or source authority have not been checked is explicitly **unverified**. One reviewer flag is sufficient to block scoring until the issue is resolved. Do not assign a perfect truth score because prose sounds confident.

Do not change a writer's actual words to satisfy a scanner. Mark quotation boundaries, examples and historical references. A conscientious reader can use contractions, a short sentence or a question without being penalized.

## Expert lenses: these are interpretations, not judges

Eight named **craft lenses** are alternative weighted views of the *same 12 human scores*, supported by the source catalogue. They are **not** eight independent evaluations, author endorsements, tests against their original writing, or measured imitation scores.

- **Harry Dry:** reader language, specific and pictureable claims, plainspoken clarity.
- **Alex Hormozi:** explain the reader's problem, cause, evidence, practical outcome.
- **Gary Vaynerchuk:** authenticity, first-hand stance, responsibility and directness.
- **Russell Brunson:** narrative reasoning, emotional context, stepwise understanding. **Do not force a sales funnel onto a personal letter.**
- **Paul Graham:** conversational wording, hard thinking, precise simplicity.
- **Ann Handley:** recognizable individual voice, reader care and human asides.
- **James Clear:** clear examples, causal logic and useful action.
- **Zadie Smith lens via Austin Kleon:** inner perspective and honesty; this is a secondary interpretation, not a direct measurement of Smith's literary voice.

For the lens names and exact weights, see `benchmark_config.json`. The 100-point editorial total remains the controlling score. **Never add or average the eight lens scores into that total**: doing so would count the same ratings nine times.

## Evaluation process and proof levels

1. Lock the brief and format. Define reader, relationship, purpose, length range, allowed facts and ethical limits.
2. Capture source version at an immutable Git commit. Use a **fresh writing prompt** for every round; do not train a candidate on an answer it will later be assessed against.
3. Produce outputs under the same model/settings where possible. Using a single assistant to simulate multiple skills is **not** an independent multi-model comparison. Record that limitation.
4. Randomize labels **before** the reader ratings and hide skill versions. Do not tell evaluators which is the approved baseline.
5. Obtain at least three reviewers, including the owner and two people who can judge natural English. Every reviewer records each of the 12 0–4 scores, evidence for low scores, and truth gate flags.
6. Include a paraphrase exercise (one reader explains the main point in their own words), a read-aloud comfort rating, a forced-choice authenticity pick, and one task-specific check. These are separate instruments, not silent additions to the 100-point total.
7. Compute mean scores by genre, report spread, agreement and meaningful dissent. Keep the input records and scripts. Avoid declaring a win if it vanishes when one task or evaluator is left out.
8. Audit gate failures and badly scored passages. Change a skill only after the user approves the proposed principle; rerun old and unseen tasks, then compare blind.

**Promotion rule:** For an official style change, aim for a positive paired preference from the owner and an improvement across at least two different genres without truth-gate regressions. The 90+ Flesch target is optional; a real reader's comprehension and the owner's voice preference matter more.

## Robustness and fairness checks

- **Leave-one-genre-out:** if the leader changes, report that the rank is fragile.
- **Weight sensitivity:** vary series weights by ±20%, normalize to 100, measure rank stability. This checks dependence on arbitrary weights, not accuracy of the human ratings.
- **Rater agreement:** compare scores by reviewer and report per-series disagreements. Two reviewers alone do not prove reliability; use multiple raters and investigate disagreements.
- **Genre balance:** compare one-to-one counsel, reflective essay, LinkedIn, email, comments and professional writing. Avoid letting a 360-word essay dominate a 90-word message by word count.
- **Evidence confidence:** source only user-approved authentic writing for style calibration. AI-generated approved *style* samples must be labelled as such. Source the budget or technical facts independently.
- **Ethical language:** do not add mental-health claims, medical advice or other sensitive personal history as stylistic filler.

## CLI contract

```sh
python3 scripts/benchmark_score.py --config references/benchmark_config.json --input /path/to/editorial-scorecards.json --output /path/to/benchmark-results.json
python3 tests/benchmark_cli_e2e.py
```

`bench_cli.py` is only an aggregator of supplied ratings. It rejects missing series, out-of-range ratings, duplicate reviewer/draft pairs and invalid weights; it blocks total scores for unverified material claims. It outputs rating provenance, individual series, expert-lens projections and aggregate editorial totals. It does not read Firecrawl or mutate GitHub. The baseline `voice_check.py` should be used separately on every sample.

**Scope of this trial:** 6 candidate versions × 3 writing tasks = 18 distinct samples. All were written or organised by the same assistant and all editorial scores were set by that same assistant, **without independent blind judges**. This trial can check the mechanics, surface differences and suggest a shortlist. It cannot prove any one version sounds like Papa Kojo or is better than a skilled human writer.
