# Kitchen Table Benchmark

A blind test of every version of Papa Kojo's writing skill on jobs none of them had seen. It was built on 18 November 2026 to decide whether v3.0 "Original" was worth the upgrade.

The name comes from the skill's main test: would this read naturally if he said it across a kitchen table to the person it is for?

## How it works

1. **Fresh briefs, frozen first.** [round-1/briefs.md](round-1/briefs.md) holds 15 jobs across WhatsApp, comments, emails, posts, a newsletter, a church talk, an essay, a cover letter, a rewrite and a humanise task. They were written and locked before v3.0 existed, so v3.0 could not be tuned to them.
2. **Isolated writers.** Each version wrote all 15 pieces in its own session. A writer could read only its own skill folder and the briefs.
3. **Blind judges.** Three judges scored all 105 drafts with the letters shuffled differently for every brief and every judge. Two more judges ran a head-to-head of v3.0 against v1.2.1. They used [rubric.md](rubric.md): eight scores from 1 to 5 (human, voice, flow, clarity, fit, person, truth, habits) and a ranking per brief. The rubric gives his real comments as evidence and does not reward or punish contractions by themselves.
4. **Frozen automatic checks.** [metrics.py](metrics.py) counts readability, contractions, avoid-words, em dashes, Wikipedia-style AI habits and numbers that were not in the brief. It was written before v3.0 and is separate from v3.0's own checker.
5. **Held-out round.** Round one showed where v3.0 was weak. After general fixes, a second set of 10 new briefs ([held-out/briefs.md](held-out/briefs.md)) was frozen and v3.0 was tested again against the two strongest older versions, with three new blind judges.

## Results

### Round one: all seven versions, 15 briefs, 3 judges

| Version | Average (of 5) | Ranked first (of 45) | Average rank (of 7) |
| --- | ---: | ---: | ---: |
| **v3.0 Original** | **4.76** | **18** | **2.42** |
| v1.2 | 4.67 | 9 | 2.69 |
| v1.2.1 | 4.56 | 5 | 3.47 |
| v1.0 | 4.43 | 4 | 3.89 |
| v2.0 prototype | 4.38 | 4 | 4.07 |
| v1.1 | 3.96 | 5 | 4.84 |
| Iconka Writer | 3.52 | 0 | 6.62 |

v3.0 had the best score on human, voice, fit, person, truth and habits. v1.2 had slightly better flow (4.89 against 4.82). Head-to-head, two separate judges preferred v3.0 over v1.2.1 in 17 of 30 rankings (average 4.59 against 4.40).

### Held-out round: 10 new briefs, 3 new judges

| Version | Average (of 5) | Ranked first (of 30) | Average rank (of 3) |
| --- | ---: | ---: | ---: |
| **v3.0 Original** | **4.53** | **13** | **1.83** |
| v1.2.1 | 4.42 | 9 | 2.00 |
| v1.2 | 4.33 | 8 | 2.17 |

By majority of judges, v3.0 won the WhatsApp reply, the newsletter, the client reply and the caption. v1.2.1 won the email, the church talk and the rewrite. v1.2 won the LinkedIn comment and the LinkedIn post. The birthday apology was split three ways.

Full scores, notes and answer keys are in `round-1/judging/` and `held-out/judging/`. All drafts are in the `drafts/` folders.

## What the judges caught in v3.0

These became fixes in [revision-recipes.md](../../references/revision-recipes.md):

- soft reversals ("The money was made. It is just stuck.");
- small borrowed experiences ("I had to hunt for an email");
- neat maxim endings and moral-ish closes after an invitation;
- three parallel scenes used for rhythm;
- general claims about people that the brief never gave ("A friend is often the first to hear").

## Limits, plainly

- **The judges were AI models, not Papa Kojo.** On the held-out LinkedIn comment they marked down "Well deserved, brother. More wins ahead." as stacked fragments, but those are his own real phrases. Only his picks can settle "sounds like me". Use the blind voting page for that.
- Each version wrote each brief once, so chance plays a part. Treat gaps under about 0.1 as ties.
- The held-out round tested v3.0 after fixes from round one, so round one is not a clean test of the final v3.0; the held-out round is.
- One person built both the skill and the benchmark. Writers and judges ran isolated and blind to reduce that bias, but not remove it.

## Run it again

```bash
python3 metrics.py round-1/drafts round-1/briefs.md
python3 blind.py pack --briefs round-1/briefs.md --drafts round-1/drafts --out /tmp/pack --tag J1 --seed 101
python3 blind.py score --judging round-1/judging --tags J1,J2,J3
python3 blind.py score --judging held-out/judging --tags K1,K2,K3
```

To test a new version: freeze new briefs first, run each version in a separate session that can see only its own skill folder, pack blind packets, give each judge only `rubric.md` and its packet, then score.
