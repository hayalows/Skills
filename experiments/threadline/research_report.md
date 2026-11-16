# What makes prose feel natural? An independent research and prototype report

**Date:** 16 November 2026  
**Method:** full-page source retrieval and structural analysis using the user's **secondary Firecrawl account**, cross-genre close reading of selected texts, review of public model-writing guidance and research literature, and offline implementation/testing.  
**Deliverable:** `Threadline 0.1`, a model-neutral writing procedure with executable prompt compilation, text diagnostics and a proposed blind A/B experiment.  
**Independence:** no personal writing profile, previous writing-skill versions or earlier benchmark passages were used as design material. The demo topics were selected independently of those earlier tests.

## Executive finding

The evidence does not support one reliable rule such as “write at Grade 4,” “use 12-word sentences,” “sound conversational,” or “put a story in the first paragraph.” Human prose remains natural across a wide range of lengths and registers because the writer develops a point with the reader in mind. The reader can tell why a detail appears, how it changes what came before, and what they should understand or do next. Clarity matters; so do grounded examples, meaningful qualifications, factual restraint and a fitting ending.

This is a **working synthesis**, not a newly established law of psycholinguistics. Several individual components have research support, and several were observed in selected human-written material. The resulting pipeline itself still needs a controlled human evaluation.

## What was actually read

The secondary Firecrawl connection successfully retrieved and analyzed **70 complete general conference transcript pages** from the Church's official April and October 2026 collections, the most recent two conferences at the time of the study. Four were primarily administrative or ceremonial materials (April 2026 Introduction, Closing Remarks, Church Auditing Department Report, and Solemn Assembly); they were excluded from the descriptive analysis of substantive addresses. That leaves **66 substantive talks**: 35 in October and 31 in April. The full per-talk register, title, month, URL and approximate language measurements are in `sources_conference_2026.csv`.

Additional complete, accessible sources retrieved:

- **Seven Dan Koe essays** (including *I'm begging you to write more essays*, *The writing habit that saved my brain*, *How To Think Originally*, *You don't need a niche, you need a point of view*, and *HUMAN 3.0*).
- **Seven Paul Graham essays** (*Write Simply*, *Write Like You Talk*, *Writes and Write-Nots*, *Succinctness is Power*, *Good Writing*, *How to Write Usefully*, and *How to Do Great Work*).
- **Five full BYU devotional transcript pages** from 2026: Dallin H. Oaks, Jeffrey S. Bednar, Neil L. Andersen, Patrick Kearon and Shayla Bott.

Two other Dan Koe pages exposed only paywalled previews. A Ross Douthat BYU forum page lacked a full transcript at the retrieved location. Those three **were not counted as full readings**. See `sources_other.csv` for exact access status and links. None of the copyrighted full texts is redistributed in this archive.

### How the reading was analyzed

For each conference transcript, the available complete page was examined from its opening through the final paragraph. Site navigation and media placeholders were separated, and approximate token, paragraph and sentence measurements were extracted. Selected talks were then examined more closely at their opening, midpoint and ending to understand their argumentative movement and example use. This is a combined **programmatic full-text review and qualitative interpretation**, not a claim of having conducted a formal literary coding study with multiple independent researchers.

A complication is that paragraphs are inferred from scraped Markdown, and automatic sentence boundaries sometimes misread abbreviations, quotations and citations. Those metrics are descriptive, not exact editorial statistics or optimized targets.

## Quantitative observations from 66 substantive conference talks

| Property | Observed value |
|---|---:|
| Approximate words per substantive talk | 873–1,659 |
| Median words per talk | 1,254.5 |
| Unweighted mean of talk-level average sentence lengths | 17.39 words |
| Median talk-level average sentence length | 17.05 words |
| Range of talk-level average sentence lengths | 11.7–25.7 words |
| Median scraped paragraph count | 25 |
| Median within-talk sentence-length coefficient of variation | 0.56 |

The speaker with a higher average sentence length is not thereby a poorer writer. Different topics carry different conceptual loads. A formal doctrinal explanation, a short personal incident, a tribute and an action-oriented invitation need different sentence structures. No sensible naturalness model should force them into the same statistical pattern.

Sentence-length CV measures variation relative to the average sentence length. Its range in this set is a useful descriptive observation; **it is not a human-authorship detector** or a target to imitate. Artificially injecting short sentences to raise the CV could harm the prose.

## Twelve close readings: mechanisms, not recipes

1. [**The Ninety and Ten**, October 2026](https://www.churchofjesuschrist.org/study/general-conference/2026/10/28dunn?lang=eng): Elder Michael A. Dunn's talk develops an endurance-race episode, explains why the friend's support matters, then uses the memory again near the ending. The detail isn't decoration: it carries the same idea across a long distance in the text.
2. [**Best Days and Worst Days**, April 2026](https://www.churchofjesuschrist.org/study/general-conference/2026/04/42freeman?lang=eng): Emily Belle Freeman begins with family wedding preparations and an abrupt return of illness. The later analysis has personal stakes rather than an abstract introduction. A model should never create this sort of episode without a supplied factual basis.
3. [**O Be Wise**, October 2026](https://www.churchofjesuschrist.org/study/general-conference/2026/10/19christofferson?lang=eng): D. Todd Christofferson frames the address with a scriptural reference and brings the text back at the end. This is a genuine thematic return rather than a compulsory summary.
4. [**Jesus Lives to Lift**, October 2026](https://www.churchofjesuschrist.org/study/general-conference/2026/10/27kearon?lang=eng): Patrick Kearon uses a light opening, aviation imagery and recurring questions. The shifts serve the organizing image. A rigid “always begin with the thesis” rule would miss what the opening does.
5. [**Divine Appointments**, October 2026](https://www.churchofjesuschrist.org/study/general-conference/2026/10/22farnes?lang=eng): a specific remembered Saturday becomes a way of considering attention to others. The movement is event → reflection → implication.
6. [**The Sculpting of Our Souls**, October 2026](https://www.churchofjesuschrist.org/study/general-conference/2026/10/13runia?lang=eng): an everyday habit of fixing objects creates a recurring interpretive image, later tested against more serious events. A motif can organize a longer argument, but only if it earns its place.
7. [**Love All; Love Each**, April 2026](https://www.churchofjesuschrist.org/study/general-conference/2026/04/27causse?lang=eng): begins with a journalist's question and develops the difference between a general principle and its application to an individual. A clear distinction can sustain an essay without a constant stream of anecdotes.
8. [**Lost Luggage, Redeemed Souls**, April 2026](https://www.churchofjesuschrist.org/study/general-conference/2026/04/23stevenson?lang=eng): begins with a familiar travel frustration, then moves from the tangible situation into a wider meaning. What matters is that the analogy remains intelligible when it is extended.
9. [**You Are Good Enough to Teach**, October 2026](https://www.churchofjesuschrist.org/study/general-conference/2026/10/58reid?lang=eng): opens with personal inadequacy and uses comparatively short paragraphs. The text moves through vulnerability without making every paragraph sound the same.
10. [**A Higher and Holier Fast**, October 2026](https://www.churchofjesuschrist.org/study/general-conference/2026/10/17soares?lang=eng): its measured average sentence length is among the longest in the sample. That illustrates why one numerical style rule would flatten different voices and subjects.
11. [**Christ-Centered Unity**, October 2026](https://www.churchofjesuschrist.org/study/general-conference/2026/10/51uchtdorf?lang=eng): begins simply and develops distinctions about the reasons groups unite. Not every address requires a dramatic hook.
12. [**Love Like Jesus**, October 2026](https://www.churchofjesuschrist.org/study/general-conference/2026/10/210rasband?lang=eng): explicitly addresses readers or listeners dealing with difficult family relationships. The opening is natural for the situation because it makes the intended reader visible immediately.

**Correction and attribution note:** Titles and links are from the official transcript pages. The first talk is by Elder Michael A. Dunn; the rhetorical analysis is about its structure, not a claim that its specific words should become a reusable template. All these prepared talks contain faith-specific convention and editorial shaping that shouldn't be exported unchanged to unrelated genres.

## What the essayists contribute

[Dan Koe's publicly accessible essays](https://thedankoe.com/letters/) often make a strong claim early, divide complex ideas into sections, address the reader directly and revisit a central question from several angles. *I'm begging you to write more essays* and *The writing habit that saved my brain* discuss writing itself as a way to develop thoughts. *How To Think Originally* and *You don't need a niche, you need a point of view* illustrate the use of a defined intellectual position as the thread through a piece. These are helpful examples of how a writer maintains direction over thousands of words. They also belong to a creator-marketing setting with deliberate attention hooks and invitations. Those elements will not suit a formal decision note or a hospital information sheet without adaptation.

[Paul Graham's *Write Simply*](https://paulgraham.com/simply.html) and [*Write Like You Talk*](https://paulgraham.com/talk.html) place unusual importance on whether wording creates unnecessary work for the reader. His [*How to Write Usefully*](https://paulgraham.com/useful.html), [*Good Writing*](https://paulgraham.com/goodwriting.html) and [*How to Do Great Work*](https://paulgraham.com/greatwork.html) also model writing as thinking and revision rather than word decoration. Graham's older website puts text into HTML tables and line breaks; automated paragraph counts from Firecrawl's Markdown are therefore not reliable across these pages, so no misleading cross-author paragraph-length comparison was made.

The five [BYU Speeches](https://speeches.byu.edu/talks/) transcripts demonstrate how a sustained address can combine practical context, argument, sacred texts and personal reflection. The site introduces boilerplate and privacy controls around the body, so its raw scraped word count is not a trustworthy article-only measure. Their rhetorical role is qualitative rather than statistical.

## What the tooling and science contribute

### Hemingway and Flesch-style readability

[Hemingway's official help](https://beta.hemingwayapp.com/help.html) explains its reading-grade approach using the **Automated Readability Index (ARI)**, which is based on characters per word and words per sentence. The grade is a rough indicator of difficulty. Similar readability formulas, including Flesch and Flesch–Kincaid measures, can help reveal dense surface wording, but they do not identify whether an essay develops its claim, stays honest or ends in a satisfying way. A model that lowers a score by breaking everything into fragments can defeat the purpose of prose.

Threadline therefore reports an **approximate ARI diagnostic**, never a single naturalness grade. The code also reports sentence variation, repeated word sequences and recurring phrasing. These diagnostics point an editor to passages requiring judgment, not automatic replacements.

### Cohesion and reader knowledge

[Coh-Metrix](https://pubmed.ncbi.nlm.nih.gov/15354684/) was designed to examine many levels of language and discourse rather than rely only on word length and sentence length. Studies summarized in [McNamara's cohesion publications](https://soletlab.asu.edu/cohesion-publications/) and the [text cohesion/genre/prior-knowledge study](https://iejee.com/index.php/iejee/article/view/222) support a qualified point: a reader's prior knowledge interacts with the amount and kind of connective explanation needed. A document for experienced engineers should not read like an introductory FAQ; a document for beginners should not skip the concepts needed to understand its next step.

The practical implication is to specify what readers already know, then keep meaningful reasons, references and qualifications visible. Simply adding “furthermore,” “moreover,” or “therefore” is not the same as constructing a logical relation.

### Narrative and concrete cases

[Green and Brock's narrative transportation research](https://pubmed.ncbi.nlm.nih.gov/11079236/) studies how involvement in stories can shape responses to narratives. It does **not** prove that every effective document needs a story. We use it only to support a limited design choice: specific, truthful episodes may help readers follow and care about a claim when the genre permits them. The task frame explicitly forbids invented personal anecdotes.

### Reader testing

The [Digital.gov principles of plain language](https://digital.gov/guides/plain-language/principles) make the audience and actual comprehension central, and recommend testing written communication with its intended readers. This is the right final authority for practical writing. A grade metric is a weak proxy for whether someone can use a service or understand a decision.

### What OpenAI and Anthropic publicly say

[OpenAI's prompt-engineering guide](https://developers.openai.com/api/docs/guides/prompt-engineering) recommends clear instructions, context, examples when appropriate and repeatable evaluation because outputs vary. [Anthropic's prompting guidance](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) likewise recommends direct communication, relevant varied examples, and matching format to the actual task. These are published **control and evaluation practices**, not disclosures of any company's private internal prose-generation algorithms. Their advice is useful for how Threadline is implemented; it does not independently validate Threadline.

## The resulting independent algorithm

The best generalization is an editorial **thought-thread model**:

1. Begin with the reader's need and the point the text can support.
2. Build a causal and explanatory sequence with authentic facts and stated unknowns.
3. Choose scenes, examples, questions or definitions only when they help the sequence.
4. Check that new paragraphs add understanding rather than new wording alone.
5. Match sentence design and tone to genre, thought and reader knowledge; avoid a mandatory “human-like” surface pattern.
6. End when the reader's need has been met, with a callback only when the argument earns it.
7. Check factual integrity and evaluate with independent readers.

The formal nine-stage process is in `model_spec.md`. Its runnable implementation and the neutral example brief are in `threadline.py` and `example_brief.json`.

## What was actually tested

**Completed:** Thirteen Python unit tests passed. A constructed deliberately formulaic text triggered five types of diagnostic warning; a constructed grounded museum description triggered none of those five. The CLI successfully generated a standalone prompt using the new method, a baseline prompt with matching input facts and a 12-brief A/B packet. It can also inspect a long document in opening, middle and ending sections and detect repeated paragraphs. These are direct checks of working software and the intended editorial constraints.

**Not completed:** A live multi-model drafting test, an independent reader panel and the paired 4,000-word essay preference study. The program supports prompt export to different AI models and an optional OpenAI API call, but no paid API was used. There is **no justified numerical improvement claim** for naturalness yet. The needed blind evaluation and its data protocol are included in `evaluation_protocol.md`.

## Major limitations and possible failure modes

- **Genre sampling bias:** 66 of the substantive full-text sources are prepared religious speeches. They show variety within a genre, not a universal sample of human writing. Dan Koe and Paul Graham represent only two additional authorial styles.
- **Edited speeches:** Some addresses may involve ghostwriting, speech preparation, transcription or professional editing. The study does not claim to know the production history of each sentence.
- **Web extraction:** page navigation, quotation marks, scripture links, footnotes and HTML tables can distort simple regex measures. The analysis avoids claiming more precision than the method supports.
- **Automation limits:** lexical recurrence can miss synonyms and conceptual continuity; sentence-length variation can be intentionally uniform; common phrases can sometimes be exactly right. The diagnostic is intentionally non-authoritative.
- **Evaluation design:** The model's prompt has more editorial guidance than the baseline. If it improves a task, the effect might come from greater detail, not one specific feature. Ablation tests should remove one component at a time, with controls for prompt length, and check whether the gain remains.
- **No proof of causality or human authorship:** the corpus is observational. The implementation cannot establish that a text was written by a human and is not intended to do so.

## Next scientific test

Run `run_blind_ab.py` with the 12 fixed briefs, the same available model and three repetitions per brief. Judge matched pairs without revealing their prompt conditions. Test factual errors separately and record what readers can actually do with the text. For the two 4,000-word cases, score opening, middle and ending separately. Do not tune on the holdout. Only then estimate a preference difference and uncertainty interval. A disappointing result would be useful: it would show where the algorithm needs a narrower scope or fewer rules.

## Final position

The strongest basis for more natural writing is not a catalogue of expressions that seem human. It is disciplined attention to what the reader needs, what the writer can actually support, and why each part follows the previous part. The runnable prototype puts those considerations before surface editing. Its mechanism is now explicit and testable, but its improvement over simpler prompts is an **unverified hypothesis** until real comparative outputs have been judged independently.
