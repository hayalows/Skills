---
name: website-ux-audit
description: "Audit a live website, prototype, or code-backed web experience for task success, clarity, accessibility, responsive behaviour, performance, trust, and end-to-end user flow. Use when the user asks for a website UX audit, usability review, journey critique, funnel review, or flow improvement plan."
---

# Website UX Audit

## Purpose

Find where a real person becomes uncertain, delayed, blocked, misled, excluded, or forced to do work the system should do for them. Turn those observations into a short, prioritized repair plan.

The unit of analysis is the user’s goal and journey, not the page. A polished screen can still support a poor experience if the wrong users arrive, the next step is unclear, the system loses their work, or success depends on memory.

Reduce avoidable thinking. Keep thinking that protects safety, informed choice, privacy, money, consent, or meaningful decisions.

## When to use

Use this skill for:

- A live website or web app supplied by URL.
- A prototype, design file, screenshot set, or recorded flow.
- A codebase whose routes, components, forms, states, or responsive behaviour need review.
- A specific task such as sign-up, booking, checkout, application, search, onboarding, account recovery, or contact.
- A broad site review where the most important journeys must be selected and audited.

Do not call a visual opinion a UX audit. Do not claim accessibility compliance, user preference, conversion impact, or task success without the evidence needed for that claim. If the user asks for implementation, hand the findings to the relevant build workflow after the audit; do not silently edit during an audit.

## Operating stance

Use supported settings without claiming an unobserved model or reasoning change. Work in two passes for substantial audits:

1. Investigate and write the evidence-backed findings.
2. Critique the draft for missed states, weak assumptions, severity inflation, unsupported claims, and recommendations that merely add decoration or copy.

Keep these separate in notes:

- Observation: what was seen, measured, or provided.
- Interpretation: the likely user or system consequence.
- Recommendation: the change that could improve the outcome.
- Confidence: high, medium, or low, with the reason.

## Intake and scope

Before inspecting, record:

```text
Surface: [site, app, prototype, or codebase]
Primary user: [who]
Goal: [what the user is trying to accomplish]
Trigger: [why they arrive now]
Success: [what completed success looks like]
Scope: [flow, pages, devices, locales, account states]
Evidence available: [screenshots, browser, code, analytics, research]
Constraints: [access, time, privacy, business, technical]
```

If a missing detail would change the audit materially, ask one short question. Otherwise state the assumption and proceed.

Choose the smallest useful scope:

- Quick review: entry page plus one core task, with the top findings only.
- Flow audit: one end-to-end task, including alternate, error, recovery, and completion states.
- Site audit: prioritise the highest-value journeys before inspecting secondary pages.
- Technical UX audit: add DOM semantics, keyboard flow, responsive behaviour, loading, performance, and code evidence.

## Respect the inspection boundary

An audit authorizes inspection, not purchases, messages, live data changes or form submissions with external effects. Use safe previews or disposable test data only within authorization. If the critical step would change real records, inspect the supporting evidence and mark the step untested unless execution is authorized. Redact private data in captured evidence.

Match claims to the evidence surface. Screenshots support visible layout and content findings; they do not prove keyboard behavior, responsive transitions, network performance or successful persistence. Code suggests behavior but does not prove the current deployment. Report blocked states as limitations, not defects in the product.

## Evidence-first workflow

### 1. Reconstruct the real journey

Start outside the interface. Map:

`entry or trigger → expectation → decision → action → system response → next decision → success, failure, or return`

Include steps outside the site when they affect success: a referral, email, payment provider, verification code, physical visit, support handoff, or later return.

For every step, record:

- User intent and expected result.
- What the user must know, decide, remember, enter, or provide.
- The visible next action.
- What the system does and how quickly it communicates that.
- Possible slips, mistakes, dead ends, loops, or lost work.
- The user’s emotional state and the trust question they may be asking.

Count cognitive work. High-cost signals include repeated data entry, hidden prerequisites, unexplained choices, competing primary actions, unclear ownership between steps, and “what do I do now?” moments.

### 2. Capture the current experience

For a live or interactive surface, inspect the actual current state before making recommendations.

- Capture an accepted screenshot for each important state and keep the flow order.
- Observe the page before acting. Use the latest DOM or accessibility tree snapshot before each interaction when available.
- After each action, check the cheapest evidence that proves what changed, then capture the visual state when it matters.
- Test the happy path and the paths people take when they hesitate, make a mistake, lose connection, lack permission, return later, or abandon and resume.
- Inspect loading, empty, validation, error, timeout, permission, confirmation, success, and repeat-use states.
- Check at relevant desktop and mobile widths. Test slow network or low-powered-device behaviour when performance may affect the task.
- For codebases, inspect routes, state transitions, form schemas, validation, content sources, analytics events, and error handling only to the depth needed for the user’s task.

Reject blank, loading, cropped, blocked, or wrong-state screenshots. Name blockers clearly. Indirect web research is background evidence, not proof of how the supplied product behaves.

### 3. Audit from outcome to pixels

Read [references/audit-rubric.md](references/audit-rubric.md) when doing a deep audit. Work through these layers in order:

1. **Outcome and fit**: Can the right person tell what this is, why it matters, whether it is for them, and what happens after the primary action?
2. **Entry and orientation**: Does the landing state match the user’s expectation from the referral, search result, ad, or internal link? Is location, scope, and next action obvious?
3. **Information architecture**: Do labels, grouping, hierarchy, search, filters, and navigation match the user’s language and mental model? Can users recover when they enter at a deep link?
4. **Comprehension and content**: Is the important information easy to scan? Are costs, requirements, timing, eligibility, limits, privacy, and consequences visible before commitment? Do headings and controls say what they do?
5. **Interaction and control**: Are controls recognisable? Do actions give timely feedback? Can users undo, cancel, go back, edit, save, and resume without losing work?
6. **Forms and decisions**: Is every question needed? Are defaults safe? Are fields grouped by the user’s task? Are eligibility and branching questions early enough? Are errors local, plain, specific, constructive, and recoverable?
7. **States and reliability**: Does the product handle latency, duplicate clicks, stale data, partial completion, failures, permission changes, and interrupted sessions without making the user guess?
8. **Accessibility and inclusion**: Can the task be completed with keyboard, zoom, screen reader, touch, voice input, reduced motion, clear text and control visibility, limited dexterity, and limited reading confidence? Use WCAG 2.2 as a technical reference, not as the whole UX verdict.
9. **Responsive and performance quality**: Does hierarchy survive smaller screens? Are touch targets, focus, text reflow, scrolling, input, and sticky controls usable? Check field data when available. Use lab tools as diagnostics, not as a substitute for real-user evidence.
10. **Trust and ethics**: Are choices balanced, reversible, and understandable? Look for hidden fees, forced account creation, confusing consent, preselected disclosures, obstructed cancellation, urgency without proof, and choices that benefit the organisation at the user’s expense.
11. **Business and service fit**: Does the flow support the actual operating model, handoffs, support capacity, fulfilment, and measurement? A short interface that creates work or confusion later is not a successful flow.

Do not apply every checklist item mechanically. Spend time where the user risk, task frequency, uncertainty, or business consequence is highest.

### 4. Challenge the first explanation

For each serious issue, ask:

- Is the problem caused by the interface, the content, the policy, the backend, the channel handoff, or a mismatch between them?
- Is the user failing, or is the system asking the user to compensate for its design?
- Is the proposed fix removing a step, or merely explaining a bad step more loudly?
- Could the change harm another user group, slow an expert, reduce privacy, or create a new error?
- What evidence would prove this finding wrong?

### 5. Write findings that can be fixed

Use one finding per issue. Each finding must include:

```text
ID and priority: P0, P1, P2, or P3
Location: page, step, control, state, viewport, or code path
Observation: what happened or what is visible
User consequence: what the user must do, risk, feel, or lose
Root cause: verified cause, or clearly labeled hypothesis with next evidence needed
Recommendation: the smallest high-leverage change
Why: why the change improves the task
Evidence: screenshot, URL, DOM/code, metric, research, or test note
Confidence: high, medium, or low
Verification: the test or metric that should improve after the change
```

Use plain language. Say “The form asks for the same phone number twice” instead of “The form has unnecessary friction.”

### 6. Prioritise by user damage

- **P0**: verified critical harm such as sensitive-data exposure, irreversible loss, dangerous behavior, or a widespread core-task blocker with no workable recovery. Flag plausible critical risks urgently while labeling uncertainty.
- **P1**: a major task blocker or serious barrier for an affected group, repeated errors, or a substantial trust problem. State reach and evidence; do not claim measured abandonment without data.
- **P2**: slows or confuses users but has a workable path around it.
- **P3**: polish, consistency, or low-risk improvement with limited task impact.

Within a priority level, sort by user harm × frequency or reach × business importance × confidence, then show effort separately. Do not use a numerical score to disguise weak evidence. Group repeated symptoms under the root problem so the backlog does not become a pile of duplicate fixes.

### 7. Design the improved flow

For the highest-impact problems, show the future path in user terms:

- What the user sees first.
- What the system decides or fills in for them.
- What the user must decide and why.
- What happens when the input is wrong or incomplete.
- How progress, cost, privacy, and timing are communicated.
- How the user exits, saves, resumes, or gets help.
- What success looks like and what happens next.

Prefer removing a decision, asking one useful question at the right time, using safe defaults, preserving work, and making the next action visible. Use progressive disclosure for secondary detail, but do not hide information needed for an informed decision.

### 8. Verify the audit

Before delivery, check:

- Every finding points to current evidence.
- Observations, interpretations, recommendations, and confidence are separate.
- The whole task is covered, including alternate and failure states.
- The strongest finding is about user consequence, not visual taste.
- Accessibility claims match the tests actually performed.
- Performance claims identify lab versus field evidence.
- Recommendations address root causes and include a verification method.
- Good existing decisions are named so a redesign does not remove them.
- Limits, blocked states, missing data, and unresolved uncertainty are explicit.

## Deliverable

Read [references/report-template.md](references/report-template.md) when preparing the final report. The default output is:

1. Executive verdict in a few sentences.
2. Scope, user goal, assumptions, and evidence limits.
3. A numbered journey with the health of each step.
4. Strengths worth preserving.
5. Prioritized findings, each tied to a step or screenshot.
6. The recommended future flow for the highest-impact journey.
7. A practical repair backlog grouped by now, next, and later.
8. Verification plan and success measures.

For a short review, return only the verdict, strongest findings, and next actions. For a deep audit, include the accepted screenshots or direct links to the evidence when the product and tools allow it.

## Research calibration

Read [references/foundations.md](references/foundations.md) when you need to calibrate the audit, explain the method, or handle a specialised flow. It summarises the most useful books, expert methods, standards, and first-party guidance from NN/g, GOV.UK, W3C, Google, Apple, Microsoft, Baymard, and IDEO.org.

These sources are lenses, not authorities over the observed user. A heuristic can flag a likely problem; only appropriate user, product, and operational evidence can establish its importance.
