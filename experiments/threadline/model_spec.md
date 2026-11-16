# Threadline 0.1: a task-first model for natural prose

**Status:** research prototype, independently developed; no personal style profile, previous writing-skill version, or hidden user preferences used in its construction. This is a **writing procedure + executable diagnostics + optional LLM prompt compiler**, not a trained neural network. The word “model” refers to a repeatable design model, not new model weights.

## The central claim

A reader experiences writing through the sequence of answers, expectations, examples and qualifications. Naturalness is therefore less about a detectable surface pattern and more about whether the writer's next thought follows intelligibly from the last one, with language that suits the task. Short sentences can help, but an entire document made only of short sentences can also become choppy.

The prototype's operational model is:

\[
\text{Useful prose} = f(\text{reader fit},\ \text{thought continuity},\ \text{warranted specificity},\ \text{epistemic honesty},\ \text{genre fit},\ \text{effective cadence})
\]

This is an **architecture**, not a numerically validated equation. There is no defensible universal weight for each component yet.

## Pipeline: nine steps

1. **Task frame.** Define the reader, what they already know, the purpose, the output type, the core point, verified facts and meaningful unknowns. If facts are unavailable, preserve uncertainty instead of inventing proof.
2. **Reasoning map.** Sketch the minimum argument that meets the reader's need. Use edges such as `reason`, `example`, `mechanism`, `effect`, `qualification`, `counterargument`, `response`, `next action`. The map changes by genre and may not be linear.
3. **Entry point.** Choose an opening that belongs to the purpose. A factual answer can start with the answer. A reflective essay may begin with a scene or observation. Do not invent a personal anecdote to simulate humanity.
4. **Paragraph contribution.** Every paragraph should change the reader's understanding somehow. Check what was established before, what is new, and why the new material belongs there. A transition must express a true logical relationship, not serve as decoration.
5. **Evidence and concrete detail.** Use actual reported observations, named mechanisms or clearly labeled hypotheticals. Treat quotations and numerical claims as facts requiring support. Specificity must never be purchased with fabrication.
6. **Cadence.** Vary syntax when the thought demands it. Use short sentences for direct actions or emphasis; use longer ones to express genuine dependency or contrast. No universal sentence length or arbitrary burstiness target.
7. **Calibration.** Match confidence, emotion, technical depth, first-person presence and formality to what is actually known and appropriate for the task. Do not exaggerate a writer's expertise or emotional experience.
8. **Exit point.** End where the reader can act, answer the question, see the implication or recognize an earned return to an earlier idea. Avoid automatic summary slogans and forced calls to action.
9. **Independent evaluation.** Before trusting the result, apply a human-facing rubric, source checking and reader testing. Diagnostics are only prompts for inspection; an LLM self-score is not proof.

## Distinctions learned from the reading

- **Coherence versus readability.** Readability formulas tend to depend on surface features such as word and sentence length. Research on cohesion adds discourse-level relations, prior knowledge and other properties. They are complementary rather than competing single-number answers.
- **Variation versus randomness.** The source talks vary substantially in average sentence length. Mimicking random variation would destroy meaning; cadence follows thought, genre, emphasis and intended reader.
- **Concrete illustration versus compulsory storytelling.** The October 2026 talk *The Ninety and Ten* threads a race anecdote through its message. Other talks begin with straightforward claims, rhetorical questions or scriptural framing. No single opening wins across genres.
- **Human voice versus a formula.** Dan Koe uses direct claims, extended explanatory sections and strong rhetorical framing. Paul Graham tends toward tightly revised, conversational arguments. Prepared devotionals often use narrative, formal testimony and audience address. Each is a distinct genre, not a universal template.
- **Sincerity versus manufacture.** Personal experience makes a passage real only when it is real. A model that invents such experience is *less* trustworthy, however fluent it sounds.
- **Closing the loop versus recap.** A callback is useful when it changes the meaning of an earlier image or argument; repeating all prior headings is not.

## The manuscript representation

A long essay can use a lightweight outline with records such as:

```json
{
  "node_id": "P04",
  "reader_question": "Why would this method work?",
  "new_contribution": "Mechanism: the user can choose a known option instead of guessing a label",
  "relation_to_previous": "explanation",
  "verified_evidence": [],
  "uncertainty": "The impact has not been tested",
  "next_reader_question": "What might go wrong?"
}
```

The graph is maintained as an editorial plan rather than exposed in the finished prose. Long pieces need a section-by-section main argument and must keep the important nouns and claims legible across distance. This matters more than artificially inserting a connective word between paragraphs.

## Evaluation hierarchy

**Mandatory gates** (failure blocks approval): fact support, meaning preservation in revision, requested content, honesty about uncertainty, no invented personal events or quotations.

**Reader-facing dimensions**, rated 1–5 by blind evaluators: reader fit, explanatory flow, grounded detail, factual discipline, natural phrasing, ending. The evaluation protocol provides a concrete rubric and paired analysis. Weights are pre-registered for tests; weights are not assumed to be universal.

**Static diagnostics**, never automatic rejection criteria: approximate readability, sentence-length distribution, duplicated paragraphs, repeated five-word spans, repeated openings, stock-phrase candidates, absolute language, local lexical recurrence. An apparent failure might be a legitimate quotation, argument, poem, legal text or rhetorical refrain.

## Why no 'human-likeness probability'?

Text-detector statistics such as perplexity and burstiness are neither stable definitions of quality nor reliable certificates of human authorship. Writing well is not the same as evading detection. This model targets comprehension, accurate reasoning and appropriate expression, and allows different genres to look different.

## Long-form specific checks

For writing longer than about 700 words, the CLI audits thirds separately. Compare the opening, middle and ending for sentence-load shifts, repeated sequences and recurring content words. These do not measure semantic drift directly. The full evaluation protocol also asks human judges to assess the three sections separately, plus the work as a whole.

## Source basis, limitations and falsifiability

See `sources_conference_2026.csv`, `sources_other.csv`, and `research_report.md`. Corpus was not used to fit model weights. No user writing style was injected. The prototype should be revised if blinded readers systematically prefer generic baseline writing or if its diagnostic flags produce high false-positive rates on unfamiliar genres.
