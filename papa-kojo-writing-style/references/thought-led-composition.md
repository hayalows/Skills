# Thought-led composition

Original 3.0.1, 24 November 2026. Applies to all registers. The correction comes from the user's preference for the second version of a reflective dawn essay.

## The rule

Let the thought determine the structure. Never add an example, adjective, observation or argument solely to complete a rhythm, fill a paragraph or make a sentence sound balanced.

Use the detail that explains the point. Develop its cause, effect or significance before adding another. A second detail is useful when it changes what the reader understands. If three or more details are necessary, keep them. Do not turn this into a rule of two, a fixed sentence length or a ban on lists.

## Drafting and delivery gate

Before drafting, name the point in ordinary speech and identify the reason or example that best carries it. Do not plan a fixed number of examples.

Before delivery, perform this review even for short writing:

- Read every coordinated sequence of examples, adjectives, descriptions, actions or clauses. If one item disappeared, what meaning, fact or useful nuance would be lost? If nothing would be lost, cut it. If the items explain one another, express the connection rather than flattening them into a list.
- Read across sentences and paragraphs. Look for repeated openings, parallel examples, mechanical symmetry and a final moral added because the piece feels as if it needs one. Preserve genuine emphasis, required information and natural rhythm.
- Check the point again after revision. Do not remove a needed fact, real objection, technical distinction, exact quotation or practical instruction merely to satisfy a pattern check. Do not invent a stance or personal memory to improve the prose.
- When Python is available, run the register-aware checker with the composition gate. Review the reported locations and rerun after edits. If a candidate is necessary, keep it and note the reason in the editorial review rather than altering the truth to obtain a zero exit status. When code is unavailable, do the review manually. No tool result replaces this editorial step.

## Calibration

First dawn draft (assistant-written, not approved for style):

> The air is cool, the streets are quiet, and you can hear the birds from a distance.

Revised dawn draft (assistant-written, explicitly preferred for style; not a personal memory):

> The air is still cool, and in the quiet of the morning, even the sound of a bird outside becomes something worth listening to.

The first gathers observations in a familiar three-part rhythm. In the second, the quiet gives the bird's sound its significance. The change is in how the thought develops, not merely the number of commas or items.

A fresh finance illustration: if a person's salary rises 10% while their cost of living rises 15%, explain what happens to their purchasing power before moving to another example. This is an illustrative case, not a claim about the user's income or personal beliefs.

A required list such as "Bring your ID, receipt and signed form" is already useful as written. The checker may flag it for review; the correct decision is to keep all three requirements. A conditional sentence such as "When prices rise, people save less and buy less" has an introductory clause followed by two related actions; it does not need a third action.

## Technical limits

The checker finds surface candidates rather than judging thought or intent. It handles many Oxford-comma and non-Oxford lists, coordinated clauses, and repeated two-word sentence openings. It cannot reliably parse every sentence, judge the necessity of an example, distinguish every natural list from padding, or establish authorship. Some natural writing will be flagged and some forced patterns will be missed. The editor must assess redundancy and meaning. Report results as candidate detection, never as proof of natural voice or guaranteed prevention.

The optional flag `--composition-gate` returns exit status 2 when composition review candidates remain, while still printing its normal text or JSON report. Normal CLI use remains advisory. A necessary flagged sequence can be retained after review; do not add filler or remove facts to satisfy the gate.
