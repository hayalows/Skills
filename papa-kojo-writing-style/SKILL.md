---
name: papa-kojo-writing-style
description: Write, diagnose, rewrite or refine prose in Papa Kojo Mensah's (Iconka's) own voice. Use for his messages, LinkedIn posts, captions, essays, scripts, brand copy, applications and church talks, or when asked to "sound like me", simplify, humanize or critique a draft. Plain, thoughtful, warm language; strong factual integrity; fewer stock AI patterns. Skip code, factual answers, exact quotations and minor spelling fixes unless voice work is requested.
version: 1.2
updated: 2026-11-16
---

# Papa Kojo Writing Style v1.2

A real point, for a real reader, in words Papa Kojo would plausibly say. He wants a calm, natural, clear voice. Simple words can carry a serious idea. **Meaning and truth outrank every style score and random suggestion.**

Read [voice-profile.md](references/voice-profile.md) once per writing task. For longer reflective content, or when a draft seems machine-made, also read [anti-slop.md](references/anti-slop.md). Treat [craft-sources.md](references/craft-sources.md) as influences, never as evidence of his personal voice.

## Evidence and instruction order

1. Current request, reader, form, length and explicit corrections.
2. His approved examples for that type of writing, if any; then his own relevant original writing.
3. His explicit voice preferences in the profile; only then broader writing techniques.

An AI draft remains an AI draft until he approves it. A recent correction overrides an older general habit within its scope. Do not silently treat examples written by an assistant as proof of how he writes. Retrieve additional original samples only when they would materially help; never require a connector for a routine message.

## Choose the task mode

| Mode | Result |
| --- | --- |
| Write | Finished copy from the supplied facts and purpose. |
| Rewrite | Improved copy first, same meaning, certainty and emotional intent. |
| Diagnose | Specific weaknesses and their effect, without rewriting. |
| Diagnose and rewrite | Brief diagnosis followed by revised copy. |
| Learn | Apply a correction; record its scope. Persist only through an authorized update. |

For a clear brief, write immediately. Ask at most one question only when the missing detail would materially change the result. Do not invent it instead.

## Writing method

1. **Know the reader.** Who is reading, what do they know, why are they reading and what do they need to do or understand? A job recruiter, friend, client and church group have different needs.
2. **Preserve the claim.** Keep names, dates, numbers, roles, ownership, sequence and level of confidence. Distinguish planned, started, approved and completed work. Do not turn "helped" into "led", guesses into facts or a team result into a personal win. Never invent a memory, belief, emotional response, conversation, personal anecdote, quote, achievement or testimonial.
3. **Find the point.** State the idea in plain language. Make the next sentence add a reason, fact, implication, useful example or honest limit. For a substantial piece, explain the cause and consequence and acknowledge a real complication. Use hypothetical scenes only when clearly marked and needed.
4. **Open where the reader is.** A direct request, grounded fact, everyday object, or specific observation can work. No compulsory hook, surprise turn or "Most people..." formula. Prefer one relevant example over several decorative ones.
5. **Write how he would speak.** Common words, active verbs, natural contractions and connected paragraphs. "Grade 3" is a target for ease, not a rule to make every piece childlike. A CV, financial explanation or technical application may need precise terms. Short and long sentences can coexist; do not force a word-count rhythm.
6. **Keep the tone steady.** Thoughtful, calm, considerate, sometimes curious. Warmth can be quiet. Use "I think" or "maybe" only if that is his actual stance. Never force Twi, pidgin, local colour, praise, hype or a motivational ending.
7. **Finish the job.** A message may need an answer or simple ask. An essay may need a considered conclusion. Stop when the reader has what they need; don't add a final lesson by habit. Read aloud and repair anything that feels staged.

## Naturalness without a new formula

Read [anti-slop.md](references/anti-slop.md) for examples of stock AI moves: repeated "not X but Y" reversals, sweeping openings, label-and-reveal lines, symmetrical triples, stacked fragments, canned endings and abstract praise. **These are editing signals, not universal grammar bans.** Judge whether a pattern serves the user's actual meaning. Keep true technical distinctions and faithful quotations. Follow Papa Kojo's explicit banned-word and no-em-dash preferences in [voice-profile.md](references/voice-profile.md); never change a required exact quote.

Original writing may contain fragments or an exclamation mark in a friendly comment. That can be natural. Don't "clean" the person out of the prose. For reflective writing, work toward thoughts that become clear through a real cause and concrete consequence rather than a dramatic reveal.

## Tools: optional, meaningful, inspectable

**Idea dice:** For a post, essay, script or reflective caption where the brief permits more than one sound approach, optionally run:

```bash
python3 scripts/voice_dice.py --format linkedin --topic "small daily spending" --seed 7
```

Omit `--seed` for fresh suggestions; use `--json` for tools. The dice offers entry, explanation, rhythm and ending ideas. Its picture field uses only relevant topic domains and can be `none`. `--domains money,football` permits only those domains; `--quote` merely signals that the brief contains a real quotation. **Never force a selected image, format, point or random structure onto the job.** The tool deliberately skips email, WhatsApp, comments, applications and rewrites. It cannot make different outputs guaranteed or identify the user's voice.

**Voice checker:** For substantial drafts or when asked to test naturalness:

```bash
python3 scripts/voice_check.py --format reflective < draft.txt
python3 scripts/voice_check.py --format comment --json < draft.txt
```

It estimates readability, sentence range and selected stock patterns. `--format` adapts advice for casual and professional contexts. Flags mean **review**, never "AI detected", "failed" or "voice approved". The grade formula is rough, especially with Ghanaian names, abbreviations and technical terms. Don't chase grade 3, sentence variance or a zero-flag score at the cost of meaning. Read the draft aloud, compare it with the brief and revise only material problems.

## Adapt to the form

| Form | Practical shape |
| --- | --- |
| WhatsApp, short message, comment | Get to the point. Keep the relationship and warmth. A natural fragment or emoji may fit if the user has used one. |
| Email | Purpose early, necessary context, specific ask; sign off only when fitting. |
| LinkedIn, caption, X | One supported observation; reason and consequence when space allows. Don't force a fixed word count or engagement question. |
| CV, application, profile | Match the actual role using verified examples and numbers. Keep professional terms when needed. No invented impact. |
| Brand copy | The reader's real problem, practical change, evidence and one sensible next step. No fake urgency. |
| Essay | Let the idea develop through causes, implications, evidence and a meaningful objection. No compulsory three-act template. |
| Church talk | Verified scriptures and teachings, speakable application, sincere invitation. No borrowed testimony or authority. |
| Video script | Spoken transitions, one thought per section, honest timing estimate; avoid theatrical hooks. |
| Apology, condolence, thanks | Acknowledge the actual situation directly and kindly. No moral lesson unless asked. |

For shared projects use "we" when accurate. For platform copy check limits, dates, links and eligibility in the actual brief. When facts are sparse, don't pad with invented detail; narrow the claim or ask one material question.

## Quality gate and learning

Before sending: Does it say what was intended? Are claims verifiable? Does one thought lead to the next? Would he say this to this reader? Does the ending belong? What would a reader misunderstand? Preserve facts first, then improve rhythm and clarity. Never add a signature flourish solely to look human.

The CLI [end-to-end acceptance checks](tests/cli_e2e.py) cover supported tool behavior:

```bash
python3 tests/cli_e2e.py
```

They prove CLI contracts and sample cases, **not** his approval or human-level voice matching. For a stronger voice evaluation, collect several user-approved examples across forms, compare anonymous drafts against those examples and record his choices without promoting unapproved AI text into the reference set. Apply corrections to the relevant format rather than every future piece.
