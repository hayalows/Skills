# Writing style comparison

## Current result (18 November 2026): v3.0 "Original" is the active version

The [Kitchen Table Benchmark](../benchmarks/kitchen-table/README.md) tested every version blind, with isolated writers and judges.

| Version | Round one average (15 briefs, 3 judges) | Round one first places (of 45) | Held-out average (10 new briefs, 3 judges) | Held-out first places (of 30) |
| --- | ---: | ---: | ---: | ---: |
| **v3.0 Original** | **4.76** | **18** | **4.53** | **13** |
| v1.2 | 4.67 | 9 | 4.33 | 8 |
| v1.2.1 | 4.56 | 5 | 4.42 | 9 |
| v1.0 | 4.43 | 4 | not run | not run |
| v2.0 prototype | 4.38 | 4 | not run | not run |
| v1.1 | 3.96 | 5 | not run | not run |
| Iconka Writer | 3.52 | 0 | not run | not run |

Scores are AI editorial judgements out of 5, not Papa Kojo's own picks. His picks in the blind voting page outrank them. Older notes follow unchanged.

---

## Earlier record (16 November 2026): correct baseline and provenance

Status: 16 November 2026 (superseded on 18 November by v3.0). **At that time the official active style was v1.2 refined (skill package version 1.2.1).** Experimental v1.3 and v1.4 are not promoted to the active skill. The owner approved the *style* of the refined v1.2 Word of Wisdom sample, not a blind comparison of every version. The other editorial preferences remain provisional.

These are Flesch Reading Ease (FRE) estimates obtained by running the same experimental v1.4 checker on the saved text of each draft. Higher FRE means simpler sentences/words by the formula, not a percentage of naturalness. Scores can exceed 100. Each version's essay differs in wording and sometimes length; this is not a controlled human study.

| Version | Word of Wisdom FRE | 2027 budget FRE | Absa FRE | Three-topic mean FRE |
| --- | ---: | ---: | ---: | ---: |
| v1.0 | 79.2 | 67.5 | 68.6 | 71.8 |
| v1.1 | 100.7 | 99.3 | 94.3 | 98.1 |
| v1.2 original | 84.8 | 75.9 | 80.7 | 80.5 |
| **v1.2 refined, approved style** | **93.0** | **not tested** | **not tested** | **not comparable** |
| v1.3 draft | 94.3 | 92.7 | 93.1 | 93.4 |
| v1.4 experimental, final | 91.7 | 85.3 | 83.5 | 86.8 |

### Matched writing-task detail: Word of Wisdom

| Draft | Words | Reading ease | Grade estimate | Checker flags |
| --- | ---: | ---: | ---: | ---: |
| v1.2 original | 317 | 84.8 | 4.9 | 1 |
| **v1.2 refined, style approved** | **361** | **93.0** | **3.6** | **0** |
| v1.3 | 300 | 94.3 | 3.1 | 0 |
| v1.4 final | 360 | 91.7 | 3.9 | 0 |

The approved refined sample was checked separately on both the original v1.2 CLI and experimental v1.4 CLI: both returned 93.0 FRE, grade 3.6 and 0 flags. The difference between 93.0 and 91.7 is too small to establish a meaningful difference in real reader comfort.

**Historical correction:** An earlier overview quoted 85.1 as the mean FRE for v1.4. That value used its first Word of Wisdom draft (86.6). After the final essay was revised to 91.7, the correct mean of 91.7, 85.3 and 83.5 is **86.8**.

### Interpreting this

- The user specifically liked v1.2 refined because it felt personal and gave a sensitive thought room to develop.
- The user found v1.3 too hurried despite its high FRE score. Do not convert the prose into a rapid sequence of directives to reach 90.
- The v1.4 draft shows a useful experimental direction, but is not proven better than the approved refinement.
- Preserve factual integrity, real reader context, natural joined sentences and gentle pacing. Treat formula scores and checker flags as editorial signals, not an authorship verdict.
- Do not extrapolate refined v1.2 results to budget or Absa, as those refined essays were never tested.
- The four-way private writing blind lab is a separate application and dataset. This skill update does not change its candidate mapping, results or deployment.
