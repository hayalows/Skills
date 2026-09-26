# Website UX audit report template

Use the smallest format that lets the reader decide what to fix and why. Keep evidence close to the finding. Use screenshots or links only when they show the state being discussed.

## Executive verdict

```text
[One sentence on whether the main task is clear and completable.]

[One sentence on the biggest user or business risk.]

[One sentence on the first repair that will improve the journey.]
```

## Scope and evidence

| Item | Notes |
| --- | --- |
| Surface | [URL, prototype, route, or codebase] |
| Task | [user goal and scenario] |
| User | [primary user, skill, urgency, context] |
| States checked | [entry, loading, empty, form, error, success, return, etc.] |
| Viewports and input | [desktop, mobile, keyboard, touch, screen reader, etc.] |
| Evidence | [screenshots, observation, DOM/code, analytics, research, tests] |
| Limits | [what could not be accessed or proven] |

## Journey health

| Step | User goal | What happens | Health | Main risk |
| --- | --- | --- | --- | --- |
| 1 | [goal] | [brief description] | Good / mixed / weak / blocked | [one sentence] |

Use “blocked” only when the task cannot proceed. Explain the exact point of failure.

## Strengths to preserve

1. **[Strength]** at [step or screen]. [Why it helps the user].
2. **[Strength]** at [step or screen]. [Why it should survive a redesign].

## Finding format

### [ID] [Short problem statement]

**Priority:** P0 / P1 / P2 / P3

**Location:** [URL, step, control, state, viewport, or code path]

**Confidence:** High / medium / low. [Reason].

**Observation**

[Describe what was seen or measured. Avoid intent claims unless the source supports them.]

**User consequence**

[Explain the work, uncertainty, risk, delay, exclusion, or loss created for the user.]

**Likely cause**

[Name the interface, content, policy, backend, or handoff condition that creates the problem.]

**Recommendation**

[Describe the change in user terms. Prefer a system or flow change over extra explanation.]

**Why this matters**

[Connect the recommendation to task success, trust, access, support cost, or a defined business outcome.]

**Evidence**

[Screenshot number, URL, DOM/code path, event, metric, research note, or test observation.]

**Verification**

[Scenario test, accessibility check, performance measure, funnel metric, support signal, or repeat-use observation.]

## Future flow

Describe only the highest-impact journey first.

```text
Entry: [what the user sees and expects]
1. [User action or decision]
   System: [what the product does automatically]
   Feedback: [what the user sees]
2. [User action or decision]
   Error path: [what happens when input fails]
3. [User action or decision]
Success: [clear result and useful next step]
Recovery: [save, edit, cancel, resume, help, or escalation]
```

## Repair backlog

| Order | Change | Owner | Effort | User outcome | Verification |
| ---: | --- | --- | --- | --- | --- |
| Now | [P0/P1 root fix] | [team] | S / M / L | [expected improvement] | [test or metric] |
| Next | [P1/P2 fix] | [team] | S / M / L | [expected improvement] | [test or metric] |
| Later | [P2/P3 improvement] | [team] | S / M / L | [expected improvement] | [test or metric] |

“Now” means high user damage or high leverage, not simply easy. Put cheap content fixes first only when they address a real user problem.

## Verification plan

Use measures that match the problem:

- Task completion and abandonment for a defined journey.
- Time, errors, retries, backtracking, and support requests.
- Qualitative observation of the target user group.
- Single Ease Question or perceived ease after a task when a subjective measure is useful.
- Accessibility checks for the affected interaction.
- LCP, INP, and CLS by device or route when performance is involved.
- HEART or a similar goal-to-signal-to-metric map for product-level monitoring.

Do not treat clicks, time on page, engagement, or retention as automatically positive. Interpret each measure in relation to the user’s goal.

## Evidence language

Prefer:

- “Observed: the confirmation page shows a reference number but no next action.”
- “This likely creates uncertainty for users who need to know whether they must do anything else.”
- “Confidence is medium because no user test or support data was available.”
- “Verify by testing the task with people who match the primary audience.”

Avoid:

- “Users will hate this.”
- “This violates UX best practices” without naming the principle and evidence.
- “This will increase conversion” without a test or reliable prior evidence.
- “The site is inaccessible” after a visual inspection alone.
- “Make it cleaner” without naming what should be removed, grouped, or clarified.
