# Long-form Natural Writing Benchmark 0.1

**Status (16 Nov 2026): prepared research protocol only.** Eight fresh prompts have been written and the matrix plans 96 **separate model calls**: 8 tasks × 4 versions × 3 independent runs. **No 96-run generation has occurred, and no blind human ratings or winning version exist yet.** This does not change the published v1.2.1 writing method, the six-way short-form blind-test site, or any private user result.

## Why it exists

The short-form approval of v1.2 refined covers a 361-word counselling example, not a 3,000-word essay. In the same 16 November conversation, the user tested a 3,052-word Divine Design essay and obtained **66.3 Flesch Reading Ease, grade 7.3, 227 sentences and 13.4 words/sentence** from Good Calculators. The shorter approved sample had **93.0 FRE, grade 3.6 and also 13.4 words/sentence**. The two texts differ in length and topic, so their 26.7-point FRE difference is **not** an isolated measure of long-form degradation or proof that v1.2.1 failed. The figures motivate stress testing of word choice, section pacing, argument, abstract language and religious terminology.

### Comparison versions and provenance

- `v1.2`: official GitHub commit `2f580c791524859b7454b1b92430b5c4e58c8dfa`.
- `v1.2.1`: official refined skill at pinned GitHub commit `a0f833c80a2048f69204147a3155d94880937a78`.
- `v1.3`: local uncommitted `papa-kojo-writing-style-v1.3-DRAFT.zip`, SHA256 in `tasks.json`.
- `v1.4`: local uncommitted `Papa-Kojo-Writing-Style-v1.4-Experimental-15-Essays.zip`, SHA256 in `tasks.json`.

**Do not silently substitute one version for another.** For independently generated candidates, extract or retrieve each pinned `SKILL.md` and its relevant references before running. The experimental archives are not a GitHub release or a voice approval.

## Research design

Eight original essays across faith, work, finance, design, mentoring, data interpretation and relationships. Six prompts are for development and two are sealed as held-out assessments until revisions are frozen. Each version receives **the same task wording and allowed facts** for each prompt, and each version gets **three independent, clean-context model invocations**.

Pre-register model name and exact configuration. Use the same model, temperature, top_p, context access, source material, and word-range requirements for all four versions. Do not feed one candidate's outputs or feedback into another's context. Store a distinct response ID, model settings and input prompt hash for every call. Change nothing in the skill between the three draws for a frozen evaluation. Independent provider requests matter; four role-played styles in a single AI conversation **do not qualify**.

- `LF01`–`LF06`: training/development of candidate guidance is permitted after scores are collected.
- `LF07`–`LF08`: untouched held-out tasks until the method and weights are frozen.
- Aim for three reviewers (owner, plus two natural-English readers) and leave the entire review version-blind. The author judges his own voice; general raters judge clarity and naturalness, not possession of his personal history.
- Use one consistent, permitted doctrine/reference corpus for all versions and check source quotations. Never insert invented personal memories, feelings, spiritual experiences, statistics or interview anecdotes.

## 13 editorial dimensions, 100 points

The long-form weights deliberately differ from the original 12-series general-writing rubric. Truth 15, reader 6, **natural voice 18**, reasoning 9, clarity 7, **emotional honesty 14**, detail 4, coherence 5, pacing 5, restraint 3, ending 2, genre 1, **sentence craft 11**. Natural voice + emotion + sentence craft = **43 points**. All use the sharper 0–4 anchors in `rubric.json`. These are *human ratings*, never automatically inferred.

Reviewers must quote real substrings of each draft and explain what they prove. At least one quoted span is required per dimension and two each for the three focus dimensions. A sampled sentence-level audit covers 30 sentences per essay, spread across its beginning, middle and end; shortlisted finalists require a full sentence pass. Important failures get marked independently even if the sentence was not sampled. Truth gates block scores where personal history, doctrine or source details are invented or materially altered.

Track 400-word readability windows, full-text FRE, syllables per word, sentence lengths, paragraph length, heading continuity, repeated points and factual source errors. A text averaging 90 FRE may have hard sections hidden inside the mean. **Readability is a diagnostic, not a point-scoring reward or a voice detector.** An accurate doctrinal term need not be replaced solely to chase grade 3.

## How to prepare and run

From this folder:

```bash
python3 longform_study.py prepare --study ./study_data
python3 longform_study.py audit --study ./study_data
python3 longform_study.py score --study ./study_data --reviews ./study_data/reviews.json
python3 tests_longform.py
```

`prepare` produces:
- `private_generation_requests.json`: the sealed version mapping, same brief, source pins, and three independent call requests per version;
- `reviewer_blind_manifest.json`: IDs and task references **without** version mapping;
- `status.json`: explicit zero generated/zero reviewed status;
- empty `drafts/` and `calls/` folders.

An operator must call a chosen model **separately for each request** and save `drafts/D0001.txt` plus `calls/D0001.json`. The call metadata must include `provider_response_id`, `independent_model_call: true`, `prompt_hash`, `version`, `model`, `temperature`, `top_p`. The script checks claimed provenance and settings, but cannot independently verify a provider's billing logs or whether the operator secretly reused a chat.

`audit` refuses a complete status when calls are missing, prompts differ, lengths leave the specified range or model settings differ. It records window-level diagnostic results **privately**. `score` only uses separately supplied, evidenced human ratings, validates exact quote matching and sentence audits, applies factual gates, and withholds a final winner.

Do not publish the private generation manifest or de-anonymized rating files. Retain them for audit, not for public GitHub. Neither `prepare` nor `audit` produces a human preference rate.

## Before revising v1.2.1

1. Establish which specific long-form failures are repeated across prompts and runs. Distinguish long academic vocabulary from necessary LDS doctrinal terms.
2. First try an **experimental long-form add-on** in `longform-writing-experiment.md`, without modifying the user's approved short advice style.
3. Validate the new approach on the reserved holdouts. Ask the author to choose blind against the approved baseline and to highlight the exact sentences they would change.
4. Accept an upgrade only if voice preference and argument quality improve **without** more false memories, factual errors, or weaker doctrine. A 90+ FRE score alone does not qualify.
5. Calculate uncertainty by **prompt** (the eight tasks are the independent units for topic generalisation), and report variation between independent runs. Do not treat all 96 texts as 96 unrelated prompt observations.

### Research references

- Xie et al. (2025), *TSTBench*: human-rated style, meaning preservation and fluency, with reproducible rubrics: https://pmc.ncbi.nlm.nih.gov/articles/PMC12191983/
- Mukherjee et al. (2025), *Evaluating Text Style Transfer Evaluation*: evaluation is multidimensional and needs comparison with human ratings: https://aclanthology.org/2025.naacl-srw.41/
- Pauli et al. (2025), *Mind the Style Gap*: superficially similar wording can hide meaning errors: https://aclanthology.org/2025.findings-emnlp.1175/

These studies informed the evaluation design. None experimentally verifies Papa Kojo's voice or the thresholds above.
