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
| **v3.0.1 Original** | **24 Nov 2026** | **Thought-led composition, mandatory semantic review, single-occurrence candidate detection and an optional CLI review gate. Retains Original as the default.** | **Main `SKILL.md`** |
| **v3.0.2 Original** | **24 Nov 2026** | **Adaptive readability analysis, audience targets, local difficulty reports, protected terms and literal before/after review.** | **Main `SKILL.md`** |
| **v3.0.3 Original** | **24 Nov 2026** | **Voice-first review, dictionary-first dual estimates, target tolerance, tail-aware reading windows and scope review.** | **Main `SKILL.md`** |
| **v3.0.4 Original** | **24 Nov 2026** | **One-person conversation, concrete shared examples, register-aware advisory checker and protection against repeated invitations.** | **Main `SKILL.md`** |
| **v3.0.5 Original** | **24 Nov 2026** | **Thought-specific structure, cross-draft scaffold review, optional batch diagnostics.** | **Main `SKILL.md`** |
| **v3.0.6 Original** | **24 Nov 2026** | **Earned attention, whole-piece arc review, essential personal-context gate and bounded approval-based learning.** | **Main `SKILL.md`** |
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

## Original maintenance update (3.0.1)

The previous checker looked for at least three narrow list matches in longer registers. It could miss one forced sequence or coordinated full clauses. The new checker reports likely enumerations from the first occurrence across registers and identifies repeated list patterns and adjacent repeated openings. Legitimate lists remain valid. The workflow requires a separate meaning-based review and does not promise that automatic checks can detect every artificial pattern. Previous benchmark results belong to the historical versions; this maintenance update needs fresh blind evaluation before any new superiority claim.

## Original maintenance update (3.0.2)

The user preferred 3.0.1 in a side-by-side historical essay comparison and requested easier reading without sacrificing voice. That preference is one calibration observation, not a blind study or approval of the essay's factual claims. This update adds an independent Python readability engine and a bounded editorial revision workflow. The composition checker and its version remain unchanged. Older versions and past scores are not recalculated. New blind evaluation is still needed to establish broader gains.

## Original maintenance update (3.0.3)

The 30-task single-model pilot suggested that the added 3.0.2 editing pass improved readability, while estimator choice changed exact target hit rates. This motivates using both estimates, tolerating small boundary differences, retaining natural easy text, and prioritising the reader's grasp of the concept. Close to Speech informed the least-edit rule. The frozen 3.0.2 scoring engine and prior versions are unchanged. The new layer adds diagnostic coverage and editorial instructions; it does not establish that 3.0.3 prose wins against 3.0.2 without a new held-out comparison and actual user judgments.

## Original maintenance update (3.0.4)

The user approved the overall style of On Staying Curious (3.0.3) while identifying two detached example openings that did not sound like him. This patch records the scoped correction and adds a conversational review alongside, rather than replacing, the existing composition and readability tools. Harry Dry's published craft advice informs reader involvement and concrete detail, not personal voice evidence. The new tests exercise surface detection and exceptions. A fresh targeted draft comparison is a development test, not proof of general voice improvement.

## Original maintenance update (3.0.5)

The user identified cross-essay repetition of previously approved conversational openings and structure. Add thought-specific planning and a bounded batch review, with an optional standalone diagnostic for repeated phrase families and locations. Preserve prior tools, voice rules and the independent checker. Harry Dry and Dan Koe inform general craft only. The ten-pair pilot is development evidence, not independent blind validation or proof of unique authorship.

## Original maintenance update (3.0.6)

The user preferred an intellectual-curiosity opening connecting map building with a deeper question. He asked for interesting beginnings, substantive middles, natural endings and a focused question when his essential personal perspective is missing. Add a single integrated craft guide and an optional opening/closing overlap diagnostic. Ogilvy, Dry, Koe and Hormozi inform craft, not personal voice. No autonomous learning or promise of infinite uniqueness. Existing scoring engines and 3.0.5 batch review are frozen. Paired development examples are not independent preference evidence.
