# Research, Validation, Analytics, and Performance

Use this reference to reduce uncertainty before, during, and after design.

## 1. Match method to uncertainty

Do not run research because "UX should do research." Choose a method because it can answer a decision.

### Need/problem uncertainty
Use:
- interviews
- observation/contextual inquiry
- support-log review
- search/query analysis
- diary study for repeated behavior

### Mental-model / IA uncertainty
Use:
- card sorting
- tree testing
- first-click testing

### Interaction uncertainty
Use:
- prototype usability testing
- cognitive walkthrough
- accessibility testing

### Live-product behavior uncertainty
Use:
- funnels
- path analysis
- cohort analysis
- search logs
- event data
- session replay with privacy controls

### Causal uncertainty
Use:
- controlled experiments where ethical and technically valid

## 2. Research brief

```text
Decision we need to make:
What we already know:
What we do not know:
Participants:
Tasks/context:
Method:
Evidence to collect:
What would change our mind:
Risks/bias:
Output:
```

## 3. Interviews

Interviews are strongest for:

- goals
- context
- language
- workarounds
- constraints
- motivation
- past behavior

Prefer questions about concrete past behavior:

- "Tell me about the last time..."
- "What happened next?"
- "What did you use?"
- "What made that difficult?"
- "How did you know you were done?"

Avoid:

- "Would you use...?"
- "Do you like...?"
- leading users toward your proposed feature

What people say matters, but observed behavior often reveals different constraints.

## 4. Observation

Watch how the work is actually done.

Record:

- tools
- handoffs
- interruptions
- repeated entry
- unofficial spreadsheets/messages
- environmental constraints
- connectivity
- device
- workarounds

A workaround often reveals a missing product capability.

## 5. Card sorting

Use to test grouping and labeling hypotheses.

### Open sort
Participants create groupings and labels.

Useful early when the taxonomy is unknown.

### Closed sort
Participants place items into predefined categories.

Useful when validating an existing structure.

Do not treat the final grouping as a vote. Look for repeated mental models and problematic items.

## 6. Tree testing

Remove visual design and test whether users can find information/actions in the proposed hierarchy.

Useful metrics:

- task success
- directness
- first choice
- backtracking
- common wrong destination

## 7. Usability testing

Test tasks, not screens.

A task should:

- represent a real goal
- avoid telling the user which control to use
- include enough context
- have a clear success condition

Example:

Weak:
"Click Filters and select Pending."

Better:
"You need to find applications that still need review. Show me how you would do that."

### Observe

- first action
- hesitation
- wrong turns
- backtracking
- questions
- errors
- success
- recovery
- confidence

Do not rescue immediately. Give the user enough space to expose the problem.

## 8. Iterative sample size

There is no magic participant number for every study.

Small repeated rounds can surface many interaction problems quickly, but participant count should depend on:

- diversity of user groups
- task complexity
- risk
- confidence needed
- frequency of issue
- qualitative vs quantitative purpose

For high-stakes decisions, increase rigor.

## 9. Cognitive walkthrough

For each step ask:

1. Will the user try to achieve the correct effect?
2. Will they notice the available action?
3. Will they associate that action with the desired effect?
4. After acting, will feedback show they made progress?

Useful for first-time learnability.

## 10. Heuristic evaluation

Use multiple lenses when possible:

- Nielsen heuristics
- Laws of UX
- product-specific principles
- accessibility
- content
- performance
- error recovery
- ethical behavior

Record evidence, not taste.

## 11. Severity

A practical severity model considers:

- task blockage
- frequency
- user impact
- recoverability
- accessibility exclusion
- financial/data consequence
- breadth of affected users

Example:

### Critical
Prevents or dangerously changes a high-stakes task, causes data loss, security/privacy harm, or blocks an essential flow for an affected population.

### High
Major task failure or repeated severe friction with poor recovery.

### Medium
Causes confusion, extra work, or avoidable errors but users usually recover.

### Low
Minor inconsistency or polish issue with limited task impact.

Severity is not the same as implementation effort.

## 12. Analytics plan

Instrument meaningful product events.

For each event define:

- name
- trigger
- properties
- user state
- success/failure
- privacy classification
- why it is needed

Avoid collecting every click "just in case."

## 13. Funnel analysis

Use funnels for a real sequence:

- entered flow
- completed required step
- reached value
- completed outcome

Investigate exits with qualitative evidence. A drop-off can mean:

- confusion
- performance failure
- ineligibility
- change of mind
- successful information gathering
- external interruption

Do not assume every exit is a UX defect.

## 14. Cohort analysis

Group users by start date, acquisition source, behavior, plan, or other meaningful characteristic.

Useful for:

- retention
- habit testing
- onboarding changes
- feature adoption

Avoid mixing cohorts whose context changed materially.

## 15. Path analysis

Use path analysis to find:

- unexpected loops
- repeated backtracking
- dead ends
- alternate successful routes
- expert shortcuts
- support-seeking behavior

Then validate why the path occurs.

## 16. Search analytics

Search logs can reveal:

- missing content
- vocabulary mismatch
- poor IA
- misspellings
- repeated queries
- no-result terms
- emergent needs

Protect sensitive queries.

## 17. Experiment design

An experiment needs:

- hypothesis
- target population
- primary metric
- guardrail metrics
- exposure rule
- duration/sample rationale
- stopping rule
- ethical review where relevant

Example:

```text
Hypothesis:
If we show the delivery estimate before payment,
then fewer users will abandon checkout,
because uncertainty about arrival is currently a major concern.

Primary metric:
Checkout completion among eligible users.

Guardrails:
Refund rate, support contacts, cancellation, page performance.

Qualitative follow-up:
Interview users who still abandon.
```

Do not run an experiment that makes one group less informed about price, consent, or safety merely to improve conversion.

## 18. Design critique

Critique should answer:

- What goal is this solving?
- What evidence supports it?
- What is the hierarchy?
- What mental model does it rely on?
- What failure state is missing?
- What is the accessibility risk?
- What implementation complexity is created?
- How will we know it worked?

Avoid "I like / I don't like."

## 19. Decision log

Keep consequential choices traceable.

```text
Date:
Decision:
Owner:
Evidence:
Alternatives:
Tradeoff:
Metric/validation:
Revisit trigger:
```

## 20. Performance is UX

A user does not care whether slowness came from design, frontend, backend, or network. It is one experience.

For web, current Core Web Vitals focus on:

- **LCP**: loading performance
- **INP**: interaction responsiveness
- **CLS**: visual stability

Current web.dev guidance uses these "good" thresholds at the 75th percentile:

- LCP ≤ 2.5 s
- INP ≤ 200 ms
- CLS ≤ 0.1

Use both field and lab data. Field data captures real devices, networks, and interactions.

## 21. Performance design rules

### Loading
- prioritize critical content
- avoid large decorative media blocking task content
- reserve dimensions for media
- load below-the-fold content later
- use appropriate image formats/sizes

### Interaction
- acknowledge input immediately
- avoid long main-thread work after frequent controls
- keep menus, accordions, filters, and buttons responsive
- use background processing where appropriate

### Visual stability
- reserve space for images/ads/async content
- avoid inserting banners above current reading position
- use stable skeleton dimensions

## 22. Perceived performance

Good perceived-performance techniques:

- immediate pressed state
- optimistic update when safe
- skeleton that reflects final structure
- progress indicators
- progressive rendering
- useful status copy
- background completion

Bad:

- fake progress
- unnecessary artificial wait
- spinner with no explanation for a long operation
- controls that remain clickable during non-idempotent submission

## 23. Low-connectivity testing

Test:

- slow 3G / throttled network
- intermittent connection
- packet loss where tools allow
- offline after initial load
- retry
- duplicate submission
- large attachment upload
- resume

For critical mobile work, a fast office Wi-Fi test is not enough.

## 24. Accessibility research

Include assistive technology in the research plan when it materially affects the product.

At minimum, design QA should include:

- keyboard
- screen reader
- zoom/text size
- reduced motion
- contrast
- touch target

For public/high-impact services, research with people with disabilities is far stronger than simulation alone.

## 25. Content testing

Test whether users understand:

- labels
- error messages
- instructions
- pricing/fees
- consent
- status
- next steps

Plain language is part of interaction design.

## 26. Post-launch review

After launch compare:

- task success
- funnel/path behavior
- support volume
- error logs
- accessibility reports
- performance
- qualitative feedback
- intended vs unintended repeat behavior

Then decide:

- keep
- iterate
- roll back
- research
- remove

## 27. Validation matrix

```text
Assumption | Risk if wrong | Evidence today | Method | Success signal | Owner
```

Prioritize assumptions that are both uncertain and costly if wrong.

## 28. Research repository note

Store:

- raw evidence with appropriate privacy controls
- synthesis
- decision implications
- date
- participant context
- known limitations

Do not turn old research into timeless truth. Context changes.
