# One-person conversation

Original 3.0.4. The user approved the overall style of the 3.0.3 essay On Staying Curious but corrected the illustrative openings. His preferred direction is to talk through an example with one person rather than announce it as an abrupt instruction. This is a scoped preference, not a ban on ordinary verbs.

## Draft from the relationship

Before an example, ask what the reader has just understood and what they need to see next. Continue the thought. If a shared example helps, use a natural invitation such as "let us take a small shop for example", a conditional such as "if you earn...", a first-person conditional such as "if I want to...", or simply state the example. Use "let us" when it sounds like him; use contractions according to the register. No quota for reader address, invitations, questions or examples. A preferred phrase is not a default: compare comparable drafts with the [thought-specific shape review](thought-specific-shape.md) where available. Retain natural wording rather than rotating through alternatives. A genuine question should help the reader reason or invite a real answer. Do not require a question as a hook or an ending.

Use concrete, familiar details that show how the idea works. One example can carry a paragraph. Follow it through to a consequence before adding another. Preserve uncertainty and distinguish a hypothetical example from a lived event. Do not invent details to make a scene vivid. A technical term may remain when precision requires it.

Harry Dry's [My Guide to Conversational Copywriting](https://marketingexamples.com/copywriting/conversational) and [17 Tips for Great Copywriting](https://marketingexamples.com/copywriting/tips/) inform the general techniques of involving the reader, ordinary language, concrete examples and sentence-to-sentence flow. They are craft references, not samples of the user's voice. Do not import advertising fragments, sales hooks, forced rhythm or a different author's persona into personal essays.

## Review example openings

The examples below are invented calibration cases, not new autobiographical claims.

| Candidate | Possible revision |
| --- | --- |
| Take a farmer who needs money for seed. | Let us take a farmer for example. He may need to buy seed before he can earn anything from his crops. |
| Say I want to get better at design. | If I want to get better at design, for example, I could study one good poster and work out why it works. |
| Consider a hypothetical scenario involving late payment. | If a client pays you a month late, you may have to cover the cost of the work yourself in the meantime. |

These are possible moves, not substitutions. A real instruction such as "Take your ID to the bank" needs no invitation. In formal writing, "consider" may be appropriate. Do not alter exact quotes. Preserve the user’s own strong lines.

## Python review

Run after drafting and after readability revisions in the actual register:

```bash
python3 scripts/conversation_check.py --register longform --review-gate < draft.txt
python3 scripts/original_check.py --register longform --composition-gate < draft.txt
python3 scripts/readability_review.py --profile longform < draft.txt
python3 tests/test_conversation_check.py
```

The conversation checker is deliberately narrow: it reviews likely detached illustrative openings in longform and posts, nearby repetitions of invitations, and runs of three questions. Common quoted and code spans are excluded. Sentence positions refer to the remaining prose. It does not parse full syntax, detect all variants, know whether a question is sincere, or distinguish every real instruction from an example. Other registers receive no automatic flags. A gate exit of 2 means review, not failure. Keep a necessary phrase after checking its purpose. If tools are unavailable, review manually. Do not chase a zero score.

## Evaluate

Keep the 3.0.3 baseline and frozen readability tools. Test fresh briefs across reflection, finance, educational writing and practical messages, including cases that need no example and genuine imperatives that must remain. Compare example framing, reader fit, factual meaning, pacing and readability. Include independent blind preferences when available. A zero-flag draft or higher Flesch score is not proof of the user's voice. No permanent promotion of generated samples as personal voice evidence without approval.
