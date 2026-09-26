# Website UX audit rubric

Use this as a question bank, not a box-ticking exercise. For each relevant item, record the evidence, the affected task, and the consequence.

## 1. Outcome and user fit

- Who is arriving, from where, and with what expectation?
- Can a first-time visitor say what the site or page does in one sentence?
- Is the primary user goal visible before secondary promotion?
- Can the user tell if they are eligible, in the right place, and ready to act?
- Does the page promise something the flow later fails to deliver?
- Is success defined in the user’s terms, not only the organisation’s metric?

## 2. Entry and orientation

- Does the landing state match the referring link, search result, campaign, or message?
- Is there one clear next action for the likely user?
- Is the current location, account state, progress, and scope visible?
- Can a user who arrives on a deep link understand the surrounding service?
- Are important requirements, cost, timing, and eligibility visible before effort begins?
- After an action, does the user know what changed and what to do next?

## 3. Information architecture and navigation

- Are labels based on user language rather than internal teams or database terms?
- Do grouping, order, and hierarchy match the user’s mental model?
- Can users predict where a link will take them?
- Can they find the same important task in more than one sensible way?
- Is search useful for the words users are likely to type?
- Are filters, sorting, pagination, and result counts understandable?
- Do back, cancel, close, breadcrumbs, tabs, and menus behave consistently?
- Can users leave and return without losing their place?

## 4. Content and comprehension

- Is the first screen scannable at the user’s likely urgency level?
- Do headings answer the question the user has at that moment?
- Are important words first, sentences short, and instructions concrete?
- Are jargon, acronyms, unfamiliar terms, and ambiguous labels explained in context?
- Can users compare options without holding facts in memory?
- Are prices, fees, eligibility, dates, limits, delivery, privacy, and consequences visible before commitment?
- Does help appear at the point of need rather than in a separate manual?
- Are images, icons, colour, animation, and testimonials doing a real job?

## 5. Interaction and control

- Does each interactive element look and behave like the pattern users expect?
- Is the primary action visually and verbally distinct from secondary actions?
- Does every action produce timely, understandable feedback?
- Are disabled states explained, or are users left wondering why something cannot be used?
- Can users undo, cancel, edit, go back, save, pause, and resume?
- Are destructive or expensive actions reversible, previewed, or confirmed at the right moment?
- Does the interface avoid accidental activation, double submission, and hidden state changes?
- Are animations useful for orientation and feedback, and can they be reduced or stopped?

## 6. Forms and decisions

- Is every question necessary for this task? What happens to the answer?
- Is the user asked for information the system already has?
- Are questions ordered by eligibility, dependency, frequency, and user effort?
- Does branching hide irrelevant questions?
- Are labels persistent and associated with their controls?
- Are examples, formats, units, limits, and required status visible before input?
- Are defaults safe, transparent, and easy to change?
- Do controls match the answer: text, select, radio, checkbox, date, file, or search?
- Is validation timed so it helps without interrupting thought?
- Does an error say what went wrong, where, how to fix it, and whether the entered data is preserved?
- Can a user complete the form with keyboard, autofill, paste, zoom, and a screen reader?

## 7. States, reliability, and recovery

Inspect the same task in each relevant state:

| State | Questions |
| --- | --- |
| Loading | Is progress visible? Is the wait explained? Can the user tell the page is alive? |
| Empty | Does the page explain why it is empty and offer a useful next action? |
| Partial | Are incomplete steps saved and clearly marked? |
| Validation | Is the problem attached to the input and written in user language? |
| Error | Can the user recover without starting over or contacting support? |
| Timeout | Is the user told what happened, what was saved, and what to try? |
| Permission | Is the restriction clear and is there a legitimate next route? |
| Duplicate action | Does repeated clicking create duplicate records, charges, or messages? |
| Success | Is completion unmistakable and is the next step useful? |
| Return visit | Can the user resume, review, change, or cancel the earlier action? |

## 8. Accessibility and inclusion

Check the task with:

- Keyboard only: focus order, visible focus, escape, submit, menus, dialogs, and no traps.
- Screen reader or accessibility tree: page title, headings, landmarks, labels, names, roles, values, status messages, error announcements, and meaningful link text.
- Zoom and reflow: text enlargement, 320 CSS pixel width, no clipped content, no forced two-dimensional scrolling for ordinary content.
- Text and control visibility, plus non-colour cues: text, controls, focus, errors, selected state, charts, and status.
- Touch and limited dexterity: target size, spacing, drag alternatives, cancellation, and accidental activation.
- Reduced motion and sensory access: no essential information conveyed only through movement, sound, colour, or position.
- Cognitive and language access: plain words, predictable structure, short steps, visible context, forgiving recovery, and no unnecessary memory burden.

Use WCAG 2.2 success criteria that match the task. Name the criterion when it helps engineering work, but do not imply that a checklist proves the experience works for all people.

## 9. Responsive and performance quality

- Does the task still make sense at mobile width, not merely fit on the screen?
- Does hierarchy survive when navigation collapses or content reorders?
- Are sticky headers, bottom bars, chat widgets, and cookie prompts hiding content or focus?
- Does the page remain usable on a slow connection, small screen, or low-powered device?
- Does content jump while the user is reading or trying to tap?
- Do key interactions respond quickly enough to preserve confidence?
- When field data exists, inspect LCP, INP, and CLS by device and route. Use lab results to diagnose likely causes, not to state how every user experiences the site.

## 10. Trust, consent, and ethical persuasion

- Does the user understand what they are agreeing to, paying for, sharing, or receiving?
- Are choices balanced in wording, visual weight, order, and effort?
- Can the user decline, cancel, unsubscribe, or delete with comparable effort?
- Are fees, renewals, data use, deadlines, stock claims, and consequences presented before commitment?
- Are defaults aligned with the user’s likely interest and clearly disclosed?
- Is urgency based on a real constraint or manufactured pressure?
- Does personalisation help the user, or exploit vulnerability, confusion, or inattention?
- Would a reasonable user feel tricked if the design decision were shown plainly?

## 11. Service and business fit

- What happens after the digital step, and who owns it?
- Do online and offline instructions agree?
- Are support, fulfilment, verification, and escalation paths available when the happy path fails?
- Does the flow create avoidable work for staff or support teams?
- Are analytics events tied to meaningful task milestones rather than clicks alone?
- Can the team tell where users stop, fail, repeat, ask for help, or succeed?

## Cognitive-work ledger

Use this compact table for each major step:

| Step | Decisions | Memory | Input | Wait | Uncertainty | Recovery | Cost |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| [name] | [count] | [low/med/high] | [low/med/high] | [low/med/high] | [low/med/high] | [easy/hard] | [time, money, trust, access] |

The aim is not to minimise every number. Remove work that does not help the user make a good decision or complete the task.

## Flow smells

Raise a finding when you see:

- A page that explains the interface instead of making the interface clear.
- A form that asks for a reason without using the answer.
- A button whose label describes the control instead of the result.
- A success message that leaves the user without a next action.
- A required step that appears only after the user has invested time.
- The same concept named differently across pages.
- A new tab, redirect, or external handoff with no explanation.
- A failed action that silently clears data or returns the user to the start.
- A mobile layout that hides the primary action below unrelated content.
- A visual treatment that creates urgency, shame, or confusion to improve a business metric.
