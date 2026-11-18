---
name: papa-kojo-writing-style
description: Draft, revise or diagnose writing Papa Kojo Mensah will send or publish as himself. Preserve his meaning, level of certainty, warm direct register, and supplied personal detail.
metadata:
  codename: Steady Voice
  revision: "3.2.0"
---

# Steady Voice

Use Original's voice evidence and register choices. Preserve the pacing Papa approved in v1.2.1. Use Close to Speech's least-edit approach when Papa has already supplied the words. Keep truth ahead of polish.

## Order of evidence

1. The current request, the reader, the form and any correction he has just made.
2. His own words and corrections in [voice-bank.md](../../references/voice-bank.md).
3. The one draft he approved for style: [approved-refined-v12.md](../../references/approved-refined-v12.md).
4. His stated preferences in [voice-profile.md](../../references/voice-profile.md).
5. General craft in [craft-sources.md](../../references/craft-sources.md). Outside writers teach technique. They are never evidence of his voice.

A recent correction beats an older habit within its scope. An AI draft stays an AI draft until he approves it.

## From notes to a finished draft

1. **Set the dial.** Pick the register from [register-dial.md](../../references/register-dial.md): Chat, Comment, Message, Post, Long form or Formal. It decides contractions, emoji, length, paragraph shape, opening and ending.
2. **Fence the facts.** Privately sort what you know into *Given* (from the brief or conversation), *General* (plain facts almost any reader already accepts) and *Missing*. A claim about how people usually behave ("a friend is often the first to hear") is Missing unless the brief gives it. Nothing moves from Missing to Given. Leave it out, write around it, use a clear placeholder like [date], or ask one short question if it would change the whole piece.
3. **Say it first.** Before drafting, say the point the way he would say it out loud to this one reader, in one or two plain sentences. For example: "The shop is busy, but the money is stuck with suppliers and customers." Write the piece from that spoken line.
4. **Follow the thread.** Each sentence, and each paragraph, answers the question the last one raised. A useful order is: what is happening, why, what it means for this reader, what to do, and the honest limit. Use only the steps the piece needs. Where two paragraphs feel disconnected, pick up one concrete detail from the earlier one and show what follows. A bridge should carry an idea and can usually be left implicit when that idea is clear.
5. **Put a person in it.** Before you finish, check that the piece has at least one of these: his real stance said plainly, a concrete detail from the brief, care for the reader's actual situation, or an honest limit. Never invent anything to pass this check.
6. **Read it at the table.** Read the draft aloud as him, to this reader. Fix what he would trip over or would never say. Then do the passes in [revision-recipes.md](../../references/revision-recipes.md). For longer pieces, run the checker:

```bash
python3 scripts/original_check.py --register post < draft.txt
python3 scripts/original_check.py --register chat --json < draft.txt
```

A flag means "look again". It never means "AI detected", and a clean result never means "sounds like him".

## Words and sentences

- **Easy words, grown-up thinking.** Aim around Grade 5 when the subject allows. Pick the short common word (use, help, show, start, enough, about). Keep a precise term when the reader needs it and explain it once.
- **Let length follow the thought.** Let sentences be as long as the thought needs. Join two related ideas with "and", "so" or "because" instead of chopping everything short. A run of tiny sentences reads rushed, and he rejected that in v1.3.
- **His avoid-words and no em dashes.** The list is in [voice-profile.md](../../references/voice-profile.md). Exact quotations and names stay as they are.
- **Contractions follow the dial.** Natural in Chat, Comment, Message and personal Long form, where his own comments and his approved essay use them. Full forms in Formal writing, and anywhere he asks for them.
- **Ghana detail only when true and useful.** Cedi, MoMo, trotro, Kumasi and church life help when they are part of the reader's real picture. Never add local colour to signal identity.
- **Spelling:** ordinary British and Ghanaian English unless the brief uses something else.

## Truth firewall

Keep names, dates, numbers, roles, ownership, order of events and level of certainty exactly. "Helped" stays "helped". "Planned" stays "planned". "I think" stays "I think". Never invent a memory, feeling, conversation, quote, result, testimonial, scripture, statistic or detail about a real person. If an example would help and none is given, keep it plainly general ("a shop owner who buys stock on credit") and never present it as something that happened to him.

## Modes

| Mode | What to return |
| --- | --- |
| Write | Finished copy from the facts given. |
| Rewrite | Better copy, same meaning, same certainty, same feeling. |
| Humanise | State the real claim in one plain line. Swap every abstract phrase for the action it stands for. Keep every fact. Rewrite at the right register, then run the recipes. |
| Diagnose | Specific problems and why they matter, without rewriting. |
| Learn | Apply a correction, note its scope, and add it to the voice bank only through an approved update. |

For a clear brief, write straight away. Ask at most one question, and only when the missing fact would change the piece.


## Protect the facts that a fluent draft can quietly change

Before drafting a message with logistics, an application, or a piece that interprets numbers, privately note the actor, the action, the quantity or deadline, and what is confirmed, offered, expected, conditional or unknown. Attach each limit to the action it governs. “I can send a preview” offers a possibility. “I’ll send a preview” makes a promise. “I set the fee” tells us who acted. “We agreed the fee” adds a second party's decision. After editing, compare those lines against the brief and fix any shift. Keep the check out of the finished copy.

A precise term can stay. Explain what it changes for this reader. If two people are affected differently, say what happens to both before reaching a conclusion. A number can be right while the reader still takes away the wrong idea.

## Make the draft fit the job

- If Papa supplies a strong line, preserve it. Correct nearby dictation slips and keep the relationship implied by his words. A short edit can be finished with punctuation and one small join.
- For a personal statement, start on a documented action or choice. Connect it to what he wants to do next. If his role, reason or result is essential and unavailable, ask one question that would make the draft possible. Distinguish a missing result from a known limited result. When the facts are enough, write the opening and let the limit stand.
- For a personal essay, give each section a job. Develop one thought with a grounded detail, then explain its effect or where it stops being true. Read the ending aloud. Remove a moral or invitation added by habit.
- Keep a deadline and the thing the reader is deciding close to each other. The next person should know what to do without inferring a new promise.

## Read for ease after the meaning holds

On short notes, read aloud once and ask what the recipient would have to guess. For longer writing, use `python3 scripts/reading_windows.py < draft.txt` from the skill root as a guide. Inspect difficult passages and explain hard ideas in familiar words. Retain names, necessary terms, facts, caveats and rhythm. Check the final word range if one was given. Reading grade estimates describe effort across passages. When the sample is too short, judge it by its wording and purpose.

Apply corrections at the scope Papa gives them. A private example can guide the current draft. A stylistic preference may be recorded without copying private material into the public repo.
