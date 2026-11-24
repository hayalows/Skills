# Voice-first review

Introduced in Original 3.0.3; retained in 3.0.4. Apply the [one-person conversation review](one-person-conversation.md) alongside it. The aim is clear thought in the user's natural language. Python gives evidence about reading effort; an editor decides what belongs on the page.

## Keep what already works

When rewriting the user's words, retain a strong line, the emotional intention and the way the user addresses this reader. Correct dictation errors and awkward joins without replacing familiar phrasing just for variety. In new writing, use the relevant approved samples and actual voice evidence. Do not manufacture a first-person experience or opinion. A personal note can be very short; a technical argument can need a longer explanation.

For difficult ideas, first say what happens in plain language. Explain the reason or consequence. Use one concrete example if it helps this reader; make it hypothetical when not supplied as fact. Introduce a necessary technical term at the point where it helps, explain it, then use it consistently. Avoid compulsory analogies, particularly if the reader already understands the mechanism. Check where an analogy stops being accurate. Do not trade precision for a simpler word.

## Review a substantial draft

1. Keep the first draft and make a private inventory of claims, actors, dates, numbers, source wording, commitments, qualifications and the intended tone. Identify any words or exact phrases that must remain.
2. Run `scripts/readability_review.py` with the audience profile. Auto mode uses CMU pronunciation data if installed and reports the heuristic estimate as a second view; otherwise it reports an explicit heuristic fallback. No package installation is required. Examine the hardest windows, including the end, and note estimator disagreement. Use the same mode for all comparisons.
3. Revise a specific difficulty rather than rewriting the whole piece. Prefer a familiar verb, a clearer subject or a concrete explanation. Read the surrounding sentences aloud and preserve connected thoughts. If the draft is already easy and natural, leave it alone. Check whether short sentences are accumulating or paragraphs are starting in the same way.
4. Compare with the original and the best accepted draft using `--before` and `--protect` for names and terms, and `--require` for exact phrases that must remain. Review numeric and literal changes, changes in certainty/negation/role cues, and any missing required phrase. These signals do not prove or disprove semantic equivalence. Read the actual sentences against the brief. Confirm the same actor, action, cause, limit, scope, evidence and emotional intent. Check that the explanation is technically sound and that the reader has everything required.
5. Read as the intended reader and as the user. Ask whether the candidate is easier to grasp, whether it sounds speakable and whether every detail still contributes. Run the thought-led composition review, register checker and, for longform and posts, the one-person conversation checker after revisions. Do not add questions or reader address merely to clear a flag. Do not accept a candidate that loses necessary meaning, voice or fit even if the score rises. Make no more than three targeted passes; stop when another would add little or make the writing worse. If the tools are unavailable, carry out the editorial checks manually and do not report invented measurements.

For short messages, comments and captions, use manual clarity, reader fit and tone review. The formulas on samples below 100 words or five sentences are diagnostics only.

## Interpret the report

Everyday long prose aims at a reading ease of 80 to 95 and estimated Grade 4 to 6, where the assignment permits. Use the specific audience profile from the [readability guide](adaptive-readability.md) for other forms. A score up to two points below the lower audience threshold is near target. An easy score above the range is not a reason to make a draft harder. A high grade despite adequate ease in long form is a prompt to review, not a hard fail. The exact 80 to 95 / Grade 4 to 6 indicator is retained for strict historical comparisons, separate from editorial acceptance.

A difference of at least five ease points or a different audience status across estimators prompts a check of pronunciation, acronyms or unusual names. CMU is not ground truth for every Ghanaian word. The ten-sentence windows overlap and include the tail; short windows are local cues rather than reliable grades. The five hardest windows are ranked for review, not compulsory edits. A run of five short sentences triggers a rhythm review. Keep exact names, quotations and technical distinctions regardless of scores.

## Example of the decision

Suppose a technical draft says a backup may restore data that was saved before an accidental deletion. Do not change it to a claim that a backup will restore everything. Explain what was saved and why testing a restore matters. A slightly harder sentence can be the right choice if it preserves the actual limit.

## Evidence and evaluation

The 3.0.2 pilot is development evidence, not a held-out test for 3.0.3. Use new briefs covering short and substantial writing, and essays of 1,000 words or more. Freeze the briefs and version commits, let each version draft independently, score with the same frozen base engine in both modes and the same length/fact requirements. Include passages needing precise technical language and good original notes that should barely change. Use the [Kitchen Table benchmark](../benchmarks/kitchen-table/README.md) blind-packet and judging workflow. Report score distribution, paired gains, missed facts, natural flow, register fit and actual user preference separately. Require no loss of necessary facts. Prefer the version the user consistently chooses across unseen tasks, not the one with the highest formula score. No claim of proven superiority before those results exist.
