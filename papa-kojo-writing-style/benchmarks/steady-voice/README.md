# Verify Steady Voice on fresh writing

Use this protocol with [the blind packet tool](../fresh-read/blind.py). Keep the task author separate from the person writing the skill. Freeze the skill and tasks by hash before generation. Give each generator only the assigned version, its references and the same briefs. Use the same model and settings for all competitors within a round.

Include short edits, client logistics, evidence-led applications, a missing fact that requires a question, a technical explanation and longer reflection. Set exact constraints before generation. Score exact quotations, word ranges and required numbers with a deterministic check. Check who did what and whether plans, estimates and commitments stayed distinct. Exact matching can confirm a number is present. It cannot confirm it belongs to the right person, date or denominator.

Ask judges to assess fidelity before comparing voice, naturalness, reader fit and paragraph flow. Give every judge aliases and no version labels or past results. Reverse the presentation order and let judges tie drafts. Average the occupied ranks for ties. For direct comparisons count wins, losses and ties over judge decisions and note disagreement by brief. A different model family and multiple generations per brief give a stronger follow-up. Papa's choices on anonymous samples remain the direct test of personal voice.

Use [reading windows](../../scripts/reading_windows.py) on longer text as a sign of reading effort. Keep the grade separate from voice and fidelity. For long essays, sample early, middle and ending passages. For five words or a short message, use a comprehension and speak-aloud check.

This is prompt distillation. It composes useful behaviours from earlier skills. Model weights are untouched. A detector answers an authorship classification question. This benchmark asks whether the text is faithful, clear and natural for a given reader.

## Research

- [Paul Graham, Write Like You Talk](https://paulgraham.com/talk.html) for the spoken revision pass.
- [George Orwell, Politics and the English Language](https://www.orwellfoundation.com/the-orwell-foundation/orwell/essays-and-other-works/politics-and-the-english-language/) for checking that plain words still convey a concrete thought.
- [Mir et al., Evaluating Style Transfer for Text](https://aclanthology.org/N19-1049/) for distinct naturalness and preservation judgements.
- [Alva-Manchego et al., ASSET](https://aclanthology.org/2020.acl-main.424/) for allowing several valid ways to simplify.
- [Pangram technical overview](https://www.pangram.com/blog/pangram-4-technical) and [Liang et al. on detector bias](https://doi.org/10.1016/j.patter.2023.100779) for treating detector outputs as separate from personal voice. The Liang paper examined earlier detectors.
