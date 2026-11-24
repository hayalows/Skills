# Thought-specific shape (Original 3.0.5)

The user noticed that otherwise natural essays could keep introducing examples with the same phrase and follow much the same order. His approval of a phrase is permission to use it where it fits, not evidence that it belongs in every piece. Retain the same voice, truth rules, register and plain language. Let the substance choose the shape. Do not promise absolute uniqueness or try to evade authorship detection.

## Before drafting
- Identify the reader's need, the central thought and the exact facts or limits that matter. Find what is worth saying about this particular subject. What detail or consequence could make the thought clear? If the brief contains no experience, do not invent one.
- Consider a second plausible way to develop the point when useful. Choose by explanatory value, not randomness or a prescribed menu. A concrete fact may lead naturally to a reason; a question may need an answer first; an observation may develop into a reflection. These are possibilities, not mandatory patterns. There need not be an example, objection, lesson, personal anecdote, question or concluding moral.
- Choose formatting from the form and reader. A short reflection may need no headings; a long explanation may need them. Keep mandatory genre conventions. Do not alter a necessary format just to make pieces look different.

## While drafting

Use [earned attention](earned-attention.md) to find an honest reason to begin, develop and finish. Keep the opening tied to the actual thought; a preferred technique is never a required phrase. Ask for a missing essential personal perspective before drafting.
Harry Dry's [conversational guide](https://marketingexamples.com/copywriting/conversational/) and [copywriting tips](https://marketingexamples.com/copywriting/tips/) inform ordinary words, reader involvement, specificity and connected sentences. Dan Koe's [writing guide](https://thedankoe.com/letters/learn-this-skill-if-you-want-to-survive-the-next-10-years/) and [article on articulating ideas](https://letters.thedankoe.com/p/how-to-articulate-yourself-intelligently) inform choosing an angle and developing an idea with relevant reasoning or evidence. These are general craft lessons, not authority over the user's voice. Do not import their sales templates, signature hooks, ideological claims, autobiographical stories or manufactured conflict. A topic can be simple and still worth writing about.

Read each sentence as if speaking to the actual reader. Use a shared invitation only when it helps. If a real example is useful, often its detail can follow directly from the preceding thought. Do not replace every invitation with a new stock phrase, cycle synonyms or force questions. Preserve familiar language if it carries meaning. Different topics can legitimately need similar wording.

## Review multiple pieces together
When asked for a set, make a temporary private note of each piece's main idea, opening, development, evidence/example (if needed) and ending. Compare comparable registers, not a formal letter with a personal essay. Notice when the same rhetorical sequence repeats across pieces, especially an opening followed by a shared example in the second paragraph and a predictable qualification or lesson at the end. Read the actual paragraphs and ask whether the common move is necessary; revise the weaker pieces by reconsidering the idea's development, not by merely switching phrases. If only one piece is requested, compare against earlier relevant drafts only when they are already available or explicitly supplied; otherwise review that draft alone. Do not claim access to an unseen writing history. Do not store private drafts in this public repository.

Optional advisory batch review:
```bash
python3 scripts/batch_shape_review.py essay1.txt essay2.txt essay3.txt
```
The tool reports phrase families, their location, repeated four-word paragraph openings and distributions of paragraph counts and opening modes. Its default cross-document thresholds (at least three drafts and 40% of the batch) are review triggers, not empirical quality cutoffs or prohibitions. Conditional sentences, common words, genre requirements and useful examples may repeat. It cannot identify all semantic equivalents or rhetorical sequences; inspect the meaning yourself. Do not maximise entropy, sentence-length variation, unique words or low similarity. Do not change good writing to clear flags.

Keep the v3.0.4 readability and composition reviews. The voice-first rule and truth firewall take priority. No additional rewrite quota. Use the existing bound of three targeted revision passes across all checks. For brief messages skip batch analysis unless the repeated pattern actually matters. With no Python, compare drafts manually. Do not report invented measurements.

## Evaluation
A development pilot in [benchmarks/shape-pilot](../benchmarks/shape-pilot/README.md) compares ten brief-matched initial drafts written with the v3.0.4 guidance and targeted thought-specific revisions in one model session. That is not an independent blind generation study. Freeze new briefs, references and evaluator for a future separate-session test, score factual preservation, clarity, natural pace and user preference separately from scaffold counts. Do not infer voice quality from diversity statistics.
