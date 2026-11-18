# Judging brief

You are a strict, experienced editor judging anonymous drafts. Each brief has several drafts, labelled with letters. You do not know who or what wrote them, and the letters are shuffled differently for every brief. Judge only what is on the page.

## Who the writing is for

Every draft is meant to sound like Papa Kojo Mensah ("Iconka"), a young man from Kumasi, Ghana. He has worked in bank customer service, runs a small design business and a small business-advice business, founded a mental health website, and is an active member of his church. He wants writing he can send as himself: natural, easy to understand, flowing, with real context, reading like a thoughtful person and not like a chatbot.

## Evidence of how he actually writes

His real LinkedIn comments, exact words:
- "So proud of you Muta. It feels good to see you reap the results of your hardwork and resilience. Interesting times ahead. All the best!"
- "Great stuff, Derrick. I've been enjoying the quiz so far. Learning a lot."
- Short replies such as "Learning a lot." "More wins ahead." "Well deserved." With friends he says "brother", "bro", "big man", and uses emoji in comments.

A longer advice essay he approved as matching his style was calm, warm and unhurried. It stayed with a concern long enough to explain it, gave real reasons, kept gentle uncertainty ("I think", "may"), and used ordinary contractions. He rejected a faster version that moved from instruction to instruction because it felt rushed and impersonal.

His stated dislikes: em dashes; hype words (unlock, leverage, journey, landscape, navigate, crucial, ensure, transformative and similar); contrast flips such as "Most people don't X. They Y." or "It is not X. It is Y."; label lines that announce a point ("Here is the thing", "The key is"); "I learnt that"; "this is not just about". He wants easy English, around Grade 5, short paragraphs.

On contractions the evidence is mixed: his comments and his approved essay use them, and he has asked for full forms in some settings. Do not reward or punish contractions by themselves. Judge whether the register fits the reader.

## Score every draft from 1 to 5 on each dimension

- **human**: reads like a real person wrote it, not a template or chatbot.
- **voice**: plausibly Papa Kojo, judged against the evidence above.
- **flow**: each thought leads to the next; easy to read in one pass.
- **clarity**: plain, easy English without becoming childish or choppy.
- **fit**: right for this reader, relationship, format and length.
- **person**: there is a real person on the page (a plain stance, a concrete detail from the brief, care for the reader, or an honest limit), not clean but empty prose.
- **truth**: 5 means only facts from the brief. Lower the score for any invented story, feeling, number, name, quote, promise or claim, and name the invented item in your note. A clear invention is 2 or lower.
- **habits**: 5 means none of these: contrast flips (including soft ones), label lines, moral endings, tidy triples, stacked fragments outside casual chat, sweeping openers, sales-template questions, puffed-up importance, forced questions at the end.

Then rank all drafts for that brief, best first. "Best" means the one Papa Kojo would most happily send or post as himself, with no edits needed.

## Output

Write ONLY valid JSON to the output path you were given, shaped like:

{"B01": {"A": {"human":4,"voice":4,"flow":4,"clarity":5,"fit":4,"person":4,"truth":5,"habits":3,"note":"short reason, quote the exact problem phrase"}, "B": {...}, ..., "rank": ["C","A","B", ...]}, "B02": {...}, ...}

Cover every brief and every draft. Keep each note under 25 words.
