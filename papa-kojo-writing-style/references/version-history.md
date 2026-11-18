# Version history

Every version of Papa Kojo's writing skill, what it tried, and where it lives now. Benchmark numbers are in [voice-benchmarks.md](voice-benchmarks.md).

| Version | Date | Idea | Where it lives |
| --- | --- | --- | --- |
| Iconka Writer | March 2026 | First voice skill in his Claude account: Grade 5 English, Sugarman, Ogilvy and Halbert copy rules, a long ban list, a fixed biography. | His Claude account (separate skill) |
| v1.0 | 26 Sep 2026 | Repo version: truth rules, form table, calm tone. | Git commit `46db3f8` |
| v1.1 | 16 Nov 2026 | Anti-AI-tell rules, idea dice, first real LinkedIn comments as evidence. | Git commit `e1260b1` |
| v1.2 | 16 Nov 2026 | Context first; AI tells treated as review signals, not bans; tested CLI tools. | Git commit `ca5abb6` |
| v1.2.1 ("v1.2 refined") | 16 Nov 2026 | v1.2 calibrated to the one essay he approved for style; long-form and evidence benchmarks. | [versions/v1.2.1](../versions/v1.2.1/README.md), and commit `049d7fc` |
| v1.3, v1.4 | Nov 2026 | Experimental drafts only. v1.3 felt too fast; v1.4 was never promoted. No skill file was saved. | Writing Blind Lab drafts |
| v2.0 prototype | 16 Nov 2026 | Voice bank, Grade 5, full forms, one-line plan, flow rule. Won a blind round against v1.2 but was never pushed. | Report from that session only |
| **v3.0 "Original"** | **18 Nov 2026** | **His words first, a register dial, say-it-first drafting, presence on the page, fix recipes, register-aware checker.** | **Main `SKILL.md`** |
| v3.1 “Close to Speech” | 18 Nov 2026 | Preserve strong original lines, ask for essential evidence, and check reading difficulty in windows. | [Selectable version](../versions/v3.1-close-to-speech/SKILL.md) |
| Steady Voice | 18 Nov 2026 | Prioritise factual scope, register and clear prose in the same editing pass. | [Selectable version](../versions/steady-voice/SKILL.md) |

## What v3.0 keeps from each

- From **v1.0 and v1.2**: the strict truth rules and the idea that AI habits are prompts to review, not proof.
- From **v1.1**: real LinkedIn comments as evidence, and the Ghana detail that helps rather than decorates.
- From **v1.2.1**: the approved essay as the pace calibration, contractions in personal writing, "do not chase a score", and both existing benchmarks.
- From **v2.0 prototype**: the voice bank, "each paragraph answers the question the last one raised", and the humanise method.
- From **Iconka Writer**: Grade 5 ease and the habit of reading the reader before writing.

## What v3.0 fixes

- **Contraction fights.** v1.2 said "use contractions", v2.0 said "full forms". His approved essay uses them and he asks for full forms in some places. The register dial now decides.
- **Clean but empty writing.** Earlier versions focused on removing habits. v3.0 also asks for a person on the page.
- **Habits that slipped through in tests.** Soft flips, label lines ("The reason is often simple."), moral endings and sales-template questions now each have a named fix and a checker flag.
- **Too fast or too even.** The checker flags runs of tiny sentences and paragraphs that all match.
