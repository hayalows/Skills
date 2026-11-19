# Live Knowledge Base research gateway (v1.2)

The gateway is a **research method** usable with whatever authorised browser/search tools the assistant actually has. It is NOT a new API, a login, a mirror of the whole KB or permission to use student records. Never claim access to every article, authenticated sections or a student account. The aim is to find and **read** the current official answer, not merely produce a search result.

## Privacy firewall before search

Translate the situation into generic terms. Strip students' names, email addresses, school IDs, phone numbers, screenshots, real private quotes, tuition figures, grades, health details, cases and account status. Example: search `site:help.byupathway.edu "registration hold" PathwayConnect`, not someone's full case. If the task requires protected details or the source is inside a secured employer system, stop public search and use authorised workflow only. A search connector does not grant institutional permission.

## Two gates: finding and verifying

1. **Find:** Search the official Help Center directly: https://help.byupathway.edu/en-US/ . Its official tutorial KA-03273 says to use the search field under "How can we help you?", start with two or three plain keywords, and browse Knowledge Base and Tutorials. If available, use an official-browser search. If the dynamic UI cannot be operated, use web search for `site:help.byupathway.edu/en-US/knowledgebase/article/ "topic" "specific action"`. For tutorials use `site:help.byupathway.edu/en-US/tutorials/ "topic"`. Search `KA-xxxxx` if a source ID is already given.
2. **Read:** Open the article itself. Note its visible title, **exact** KA identifier, canonical URL, text relevant to this question, scope (PathwayConnect vs Certificate & Degree; old catalog vs new), any dates, and whether it is current, cached/offline or inaccessible. A search snippet alone is a **lead**, not a verified procedure.
3. **Cross-check:** For dates, withdrawal, fees, aid or eligibility, compare the applicable academic calendar, block-specific guide and institutional source. For technical steps, check whether the article is a Tutorial or Knowledge Base article and whether it references a different procedure for another catalogue.
4. **Respond:** Give the direct, relevant answer or the single next action, when verified. Put your source note for Papa **after** the student-facing copy; never turn WhatsApp into a citation report.
5. **Log uncertainty:** If the page fails, is outdated, contradicts another official page, or depends on unverified student/account details, mark **not verified** and name the exact remaining check. Do not substitute a generic homepage, third-party answer or model memory and call it official.

### Search escalation when one attempt fails

- **Pass 1:** simple topic + action, e.g. `Canvas missing course`.
- **Pass 2:** synonym or exact error, e.g. `class not visible Canvas`, `student portal enrolled courses`.
- **Pass 3:** site-scoped web query, both Knowledge Base and Tutorials, and an article-number search if one is known.
- **Pass 4:** current official Mentoring Hub/KB staff instructions, authorised support or MSA. Stop if no current trustworthy source can be opened. No invented policy.

Use a narrow search instead of scraping, bulk-copying or downloading the full Help Center. Follow normal site limits and access requirements.

## Evidence tiers and allowed language

| Tier | Evidence | Allowed wording |
| --- | --- | --- |
| E0 | Model memory, old playbook, old template, unopenable link | "A past reference suggests...", or do not state the rule |
| E1 | Search result/snippet/link but article NOT opened | "I found a possible article, but haven't verified its instructions" |
| E2 | Official article opened and relevant text read | "The article says ..." with correct title/ID/link; still check programme/date |
| E3 | E2 plus programme, catalogue, block date, latest guide checked | Source-backed student-specific procedural guidance, without claiming portal status |
| E4 | E3 plus authorised student record verified in an approved system | Can describe an observed account state if institutional privacy permits; never assume E4 from AI or a connected app |

Never claim E4 merely because a file or link exists. For many everyday replies, no KB is needed; do not over-research a "thank you".

## Short source note for the mentor

`Source checked [date]: [title], [KA-#####](official URL). Relevant scope: [programme/catalogue]. It says [one precise point]. Additional check: [none / live deadline / student account / MSA].`

If no usable article is available: `I couldn't confirm [specific fact] from the current official guide. Please check [authorised place/person].`

## Conflicting rules

If two official pages give different dates, preserve **both** dates with their source titles and contexts; do not silently choose. Prefer the current block's verified calendar for deadlines **only when its applicability is clear**. If unresolved, send a cautious non-deadline instruction and ask the authorised support team/MSA. Example: KA-02454 and KA-03385 have described different general add-course timing; the block-specific calendar controls the student-facing decision after verification.

## Tool availability and boundary

The standard skill is prompt-level. It can use the assistant's available web/browser tools for public research, but cannot create an authenticated universal KB API, bypass login, or automatically ingest every new article. An optional companion script `../scripts/kb-gateway.mjs` creates privacy-safe public search URLs and canonical KA leads; **it does not verify content**. See [kb-index.md](kb-index.md) for leads. Reopen every cited article in the actual case.

## Hard completion gate

If source verification is required AND official content is available, **open it in the same turn and finish the answer**; don't simply say "I'll check" after already making that promise. If it cannot be opened, explicitly mark the exact blocker and give one safe step for the mentor or student. No fictional confirmation of reading, referrals, tickets, grades, grants or registration.
