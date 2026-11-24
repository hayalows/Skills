# Adaptive readability

Original v3.0.2 base engine, retained unchanged for reproducibility. Original 3.0.3 uses the [voice-first review layer](voice-first-review.md) by default for substantial prose. Keep the voice and the thought-led composition gate from 3.0.1. The aim is to reduce the work a reader has to do to understand a real idea.

## Targets are guides, not pass marks

| Audience or form | Flesch Reading Ease target |
| --- | --- |
| Chat or comment | 85 to 100 |
| Personal or work message | 80 to 95 |
| Post | 75 to 90 |
| Personal essay or talk | 80 to 95 |
| Educational article | 70 to 90 |
| Formal prose | 60 to 80 |
| Technical or research prose | 50 to 75 |

Aim near Grade 4 to 6 for everyday prose. The audience and requested form come first. Do not add difficult words to lower an unusually high ease score. Below 100 words or five sentences, the tool reports a short sample: read it manually, and do not judge it by a grade. Required names, quotes and technical words may raise the grade.

## Workflow

1. Draft with Original's register, truth and composition rules. Establish the intended reader and protect names, numbers, source wording, necessary terms and required quotations. Save the first draft if tools are available.
2. Run the engine on prose, not headings, citations, tables or code. Choose the profile for the actual audience. Read the hardest paragraphs and windows; use sentence locations and review words to find the real cause. Keep the same dictionary mode and input scope when comparing drafts.
3. Revise only where the reader benefits. Replace a difficult word if a familiar one carries the same meaning. Put the actor next to the action. Explain a necessary term once, then use its established short name where clear. Split at a natural turn of thought, not merely because a sentence is long. Join related short sentences when the draft sounds rushed.
4. Compare the revision with the first draft and the best accepted draft so far. Review changed or missing literal numbers and protected terms, as well as claims, roles, ownership, order, evidence, qualifications, negations, uncertainty and emotional intent. The Python guard only checks literals; it cannot establish meaning. Reject any revision that loses a fact, a necessary detail or the user's voice. Review the composition gate again.
5. Make up to three targeted revision passes. Stop earlier when the writing reads easily, improvements are marginal, or another change would weaken the prose. Keep the best accepted draft even when its score is below target. When no Python is available, perform the same editorial review manually and do not invent scores.

## CLI

From the skill root, use the new review layer for writing and the frozen engine for historical comparisons:

```bash
python3 scripts/readability_review.py --profile educational --protect "National Identification Authority" < draft.txt
python3 scripts/readability_review.py --profile educational --before draft.txt --protect "National Identification Authority" < revised.txt
python3 tests/test_readability_review.py
```

The original commands remain supported:

```bash
python3 scripts/adaptive_readability.py --profile educational --protect "National Identification Authority" < draft.txt
python3 scripts/adaptive_readability.py --profile educational --protect "National Identification Authority" --before draft.txt < revised.txt
python3 scripts/original_check.py --register longform --composition-gate < revised.txt
python3 tests/test_adaptive_readability.py
```

Optional: install the cmudict package in an appropriate environment and pass `--dictionary cmu` to use its pronunciation entries with heuristic fallback. Do not install packages without the environment owner's permission where required. Pass `--easy-words path/to/wordlist.txt` with a suitable Dale-Chall list including inflections to enable an approximate Dale-Chall estimate. No such list is bundled; arbitrary easy-word lists do not produce a standard score. Use the same list and dictionary for any comparison. The engine works without either option.

The JSON report gives estimated Flesch ease and grade, SMOG for at least 30 sentences, optional Dale-Chall and unlisted-word percentage, average sentence length, syllables per word and polysyllable counts. It locates possible hard words and sentences, reports paragraph scores and overlapping windows of up to ten sentences with at least 100 words, and compares literal numbers and protected-term occurrences between drafts. The separate unprotected syllable ratio is a diagnostic, never a replacement for the raw Flesch score. The prior `reading_windows.py` remains available; `original_check.py` still checks rhythm and composition. A general word-frequency corpus is not bundled; optional easy-word membership is only a rough familiarity signal.

## What the numbers cannot tell us

The default pronunciation heuristic is approximate, particularly for Ghanaian names, acronyms, unusual words and contractions. Numbers are excluded from the alphabetic readability tokens but counted separately by the literal guard. Sentence splitting and short paragraph estimates are imperfect. Protected terms must be supplied by the editor, including exact spelling and case. Changed literal counts can be legitimate after an editorial check, for example introducing an abbreviation after the full name. No change in counts proves nothing about whether the facts or their relationships stayed true. Do not promise a Grade 5 result for every brief.

## Evaluation

Use fresh, matched briefs across everyday and technical forms. Preserve a frozen Original 3.0.1 baseline, compare both drafts with the same engine, and blind the labels for human reviewers. Record whole-text ease, difficult windows, preservation of factual meaning, natural flow and the user's actual preference. Record necessary exceptions separately. A higher ease score alone is not a win. Do not call a single side-by-side preference proof of superiority. Previous benchmark scores are historical and must not be compared across different tokenizers or dictionaries without rescoring both texts.
