---
name: product-design-os
description: "Use when designing, redesigning, auditing, specifying, prototyping, or improving a digital product, website, mobile app, workflow, interface, component library, design system, onboarding, checkout, dashboard, form, search experience, pricing page, or retention loop. Combines user-centered product thinking, cognitive psychology, interface craft, accessibility, ethical behavior design, research, performance, and implementation-ready handoff."
---

# Product Design OS

## Purpose

Turn a product brief, existing interface, screenshot, codebase, user problem, or rough idea into a coherent product experience that is useful, usable, accessible, resilient, visually disciplined, measurable, and ready to build.

This skill is intentionally broader than a UI styling guide. It covers:

- the problem and user outcome
- information architecture and user flows
- interaction design
- behavioral and cognitive psychology
- responsive layout and visual hierarchy
- component design and design systems
- accessibility and inclusive interaction
- loading, error, empty, offline, permission, and recovery states
- performance as part of experience
- ethical engagement and habit design
- user research, usability testing, analytics, and experiments
- implementation-ready specifications and QA

## Core Standard

A design is ready only when a user can understand what is happening, know what to do next, complete the task, recover from errors, use the experience with keyboard or assistive technology where applicable, and trust the system's feedback.

Do not confuse novelty with quality. Use familiar patterns for familiar problems. Depart from convention only when the user benefit is specific, testable, and worth the learning cost.

Do not confuse engagement with user value. Repeated use is valuable only when repetition serves a recurring user need.

## Evidence Hierarchy

When design inputs conflict, prefer evidence in this order:

1. direct user needs, observed behavior, and task evidence
2. product analytics and support evidence
3. accessibility requirements and platform conventions
4. product constraints, domain rules, and technical reality
5. established interaction patterns and cognitive principles
6. competitive references
7. aesthetic preference

Do not use a UX law as proof that a design will work. Laws and heuristics are hypotheses and guardrails. Validate important decisions with users or behavior data.

## Minimum Brief

Before designing or substantially redesigning, establish as much of the following as the task requires:

- product or surface
- primary user or user group
- job they are trying to complete
- desired outcome
- platform: responsive web, desktop app, iOS, Android, or cross-platform
- current state or reference, if one exists
- constraints: brand, tech, compliance, connectivity, device, time, content, data
- success signal
- known risks or failure modes

If the user already supplied enough context, proceed. Do not turn intake into a questionnaire.

When information is missing but not decision-changing, state the assumption and continue. Ask only when the missing fact would materially change the design.

## Workflow

### 1. Frame the actual problem

Write a one-sentence problem statement in this structure:

`[User] needs to [task/outcome] in [context], but [friction/constraint] makes that difficult.`

Then define:

- the primary task
- the moment of entry
- the desired end state
- the cost of failure
- the business or organizational goal
- where the two goals align or conflict

If business and user goals conflict, surface the conflict instead of hiding it in interface mechanics.

Load `references/foundations.md` for cognitive principles, mental models, IA, journeys, and decision rules.

### 2. Map the experience before styling it

For any flow with more than one meaningful action, map:

- entry points
- user intent
- required decisions
- system decisions
- data inputs
- branch points
- success path
- cancellation
- undo
- empty state
- loading
- validation error
- system error
- permission failure
- offline or degraded network state where relevant
- resumption after interruption

Make the shortest safe path obvious. Do not remove necessary context merely to reduce the number of screens.

### 3. Reduce cognitive and physical effort

Apply this order:

1. remove unnecessary steps
2. remove unnecessary decisions
3. provide smart defaults only when they are safe and reversible
4. make the preferred next action obvious
5. group related information
6. reveal advanced options progressively
7. preserve recognition so users do not have to remember hidden information
8. enlarge and position frequent targets for easy acquisition
9. keep feedback close to the action that caused it
10. let the system carry complexity that users should not have to carry

Before adding motivation, badges, gamification, reminders, or persuasion, first ask whether the action itself can be made easier.

### 4. Establish information hierarchy

For every screen, identify:

- one primary purpose
- one dominant next action, if an action is required
- supporting information
- secondary actions
- tertiary or advanced actions
- destructive actions
- system status

The visual hierarchy must match the task hierarchy.

If everything is prominent, nothing is prominent.

### 5. Design responsive structure

Load `references/interface-craft.md`.

Start from the smallest realistic content width and expand upward. Do not make a single desktop frame the implicit product.

Specify:

- content container behavior
- side padding
- grid or alignment anchors
- vertical rhythm
- component wrapping or stacking
- breakpoints based on content failure, not device labels alone
- sticky elements
- safe areas
- keyboard overlays on mobile
- long-text and localization behavior
- zoom/reflow behavior on web

Use a small spacing vocabulary rather than arbitrary values. A 4pt or 8pt-based scale is usually a useful starting point, not a law.

### 6. Design components as behavior, not pictures

Load `references/component-patterns.md`.

For every interactive component define, when relevant:

- default
- hover
- focus
- pressed/active
- selected
- disabled
- loading
- success
- warning
- error
- empty
- read-only
- permission-limited
- skeleton/pending

Also define:

- label rules
- icon meaning
- keyboard behavior
- touch/click target
- validation
- feedback
- destructive behavior
- responsive behavior
- accessibility name/role/state
- what happens after activation

A component is incomplete if its error, loading, or focus behavior is unspecified.

### 7. Apply psychology carefully

Use cognitive principles to explain user behavior, not to decorate rationale.

Core lenses:

- Jakob's Law: preserve familiar mental models for familiar tasks.
- Fitts's Law: make important targets easy to acquire.
- Hick's Law: reduce unnecessary choice complexity.
- Miller's Law: use chunking; do not impose a mythical seven-item limit.
- Postel's Law: accept reasonable variation in human input while producing structured output.
- Peak-End Rule: design high-stakes peaks and the ending deliberately.
- Aesthetic-Usability Effect: polish can improve perceived usability but may also hide real usability defects.
- von Restorff Effect: make the most important item distinct, using contrast sparingly.
- Tesler's Law: unavoidable complexity has to live somewhere; prefer the system carrying it when practical.
- Doherty Threshold: respond fast and provide immediate feedback when work continues in the background.

See `references/foundations.md`.

### 8. Run the accessibility gate

Load `references/accessibility.md`.

For web work, target WCAG 2.2 AA unless the user specifies another standard. Treat the following as baseline design responsibilities:

- semantic structure
- keyboard operability
- visible focus
- accessible names and instructions
- sufficient text and non-text contrast
- target size and spacing
- no color-only meaning
- error identification and recovery
- zoom and reflow
- reduced-motion behavior
- screen-reader-friendly control relationships
- sensible focus management in dialogs and dynamic content

Accessibility cannot be postponed to visual QA.

### 9. Run the ethical behavior gate

Load `references/behavior-ethics.md` whenever the product includes:

- retention loops
- notifications
- streaks
- variable rewards
- social proof
- default choices
- autoplay
- infinite feeds
- urgency
- scarcity
- subscriptions
- cancellation flows
- persuasive onboarding
- gamification
- repeated prompts

Before applying any engagement mechanic, answer:

1. What recurring user problem does this behavior solve?
2. Would the user still choose this if the mechanism were explained plainly?
3. Is the behavior easy to stop, mute, undo, or leave?
4. Does the mechanic preserve meaningful choice?
5. Is the reward tied to user value rather than time spent alone?
6. What happens to vulnerable, compulsive, distressed, or unintended heavy users?
7. Are we measuring a user outcome alongside a business metric?

Do not optimize a product around compulsion, deceptive scarcity, obstructed cancellation, disguised ads, forced continuity, confirm-shaming, or hidden consequences.

### 10. Design for resilience

Test the experience outside the happy path.

At minimum consider:

- slow network
- request timeout
- partial data
- duplicate action
- accidental repeat tap/click
- browser refresh
- back navigation
- interrupted session
- expired auth
- denied permission
- unavailable dependency
- empty history
- very long names/content
- small screen
- zoomed text
- offline mode if relevant
- first-time user
- returning expert user

The product should fail in understandable, recoverable ways.

### 11. Validate

Load `references/research-validation.md`.

Choose the lightest method that can answer the biggest uncertainty:

- user interview for needs and mental models
- card sorting for grouping
- tree testing for findability
- prototype usability test for task completion
- cognitive walkthrough for learnability
- heuristic review for broad interaction risk
- accessibility testing for keyboard, screen reader, zoom, contrast, motion
- analytics for real behavior
- experiment for causal comparison when appropriate
- field performance data for responsiveness

Do not ask users which design they "like" when the real question is whether they can complete the task.

### 12. Specify the system and handoff

Load `references/design-systems-handoff.md`.

Define:

- design tokens
- typography roles
- color roles
- spacing scale
- radius/elevation rules
- grid/container rules
- icon rules
- component anatomy
- variants and states
- interaction behavior
- responsive behavior
- content rules
- accessibility requirements
- analytics events if needed
- performance expectations
- acceptance criteria

Design systems are not libraries of screenshots. They are shared decisions encoded as reusable rules and components.

### 13. QA before handoff

Load `references/audit-checklist.md`.

A strong handoff includes a final pass for:

- task clarity
- cognitive load
- state completeness
- consistency
- accessibility
- responsive behavior
- content quality
- error recovery
- performance
- ethical behavior
- instrumentation
- implementation detail

Do not call the work finished because the happy-path screens look polished.

## Operating Modes

### New product or feature

Deliver:

1. brief and assumptions
2. primary user/job
3. flow or IA
4. screen/component architecture
5. interaction states
6. responsive rules
7. accessibility requirements
8. measurement plan
9. risks and open questions
10. implementation-ready specification

### Redesign

First separate:

- what is broken
- what is merely unfamiliar
- what is constrained
- what already works
- what should stay stable to preserve mental models

Then redesign the smallest set of things that meaningfully improves the outcome.

### Audit

Use evidence from the actual product where possible.

For each issue include:

- location
- observed behavior
- user consequence
- principle or evidence
- recommended change
- severity based on task impact
- confidence
- how to validate the fix

Do not fill an audit with generic aesthetic opinions.

### Design system

Start with foundations and semantic tokens, then primitives, then reusable components, then compositions. Document usage and non-usage, not only visual variants.

### Component specification

Include:

- purpose
- anatomy
- variants
- states
- content rules
- behavior
- responsive behavior
- accessibility
- errors
- examples
- anti-patterns
- acceptance criteria

### Behavior / retention design

Use `references/behavior-ethics.md`. Only design a habit loop when repeated behavior is necessary to the user's own recurring goal.

### Landing / marketing surface

Use the same user-centered principles. A hero should quickly answer:

- what is this?
- who is it for?
- what useful change does it provide?
- why should I believe it?
- what can I do next?

Do not let conversion tactics damage clarity, consent, or credibility.

## Source Loading Map

Load only the references needed for the task:

- cognition, journeys, mental models, IA → `references/foundations.md`
- layout, typography, spacing, color, cards, heroes → `references/interface-craft.md`
- buttons, forms, nav, search, dialogs, tables, states → `references/component-patterns.md`
- accessibility → `references/accessibility.md`
- retention, habits, notifications, engagement ethics → `references/behavior-ethics.md`
- research, testing, metrics, performance → `references/research-validation.md`
- tokens, libraries, documentation, handoff → `references/design-systems-handoff.md`
- practical worked examples → `references/examples-recipes.md`
- audit / pre-launch review → `references/audit-checklist.md`
- provenance and external references → `references/source-map.md`

## Universal Decision Rules

- Prefer clarity over cleverness.
- Prefer recognition over recall for ordinary tasks.
- Prefer direct manipulation over hidden commands.
- Prefer fewer meaningful choices over many undifferentiated choices.
- Prefer reversible actions over confirmation dialogs when safe undo is possible.
- Prefer prevention over error messaging.
- Prefer tolerant input parsing over forcing users into machine formatting.
- Prefer explicit labels over placeholder-only forms.
- Prefer visible focus over decorative focus removal.
- Prefer system feedback immediately after input.
- Prefer real progress over fake progress.
- Prefer user-controlled notifications over aggressive re-engagement.
- Prefer content-first responsive behavior over device-name breakpoints.
- Prefer semantic tokens over literal color/size values.
- Prefer native/standard controls unless custom interaction has a demonstrated benefit.
- Prefer real content and realistic edge cases in design reviews.
- Prefer evidence-backed design rationale over taste debates.

## Anti-Patterns

Reject or challenge:

- hidden or changing navigation without a strong user reason
- tiny targets
- low-contrast text used for fashion
- destructive primary buttons beside harmless secondary actions with weak differentiation
- disabled controls with no explanation
- placeholder-only labels
- validation that erases user input
- error messages that only say "invalid"
- nested modals
- auto-advancing carousels without controls
- infinite feeds when the user's task has a natural stopping point
- autoplay that steals attention
- fake scarcity, fake activity, fake social proof
- preselected paid add-ons
- cancellation harder than signup
- notification permission before value is demonstrated
- loading indicators with no feedback after an action
- skeleton screens that shift layout when content loads
- arbitrary one-off spacing values everywhere
- one-off components that duplicate an existing pattern
- visually dramatic dashboards that obscure the decision users need to make
- mobile designs derived only by shrinking desktop
- animations that are required to understand state
- important meaning conveyed by color alone
- habit mechanics without a user-benefit case

## Output Quality

When presenting design work, explain the decisions that materially affect:

- user task success
- cognitive effort
- error risk
- accessibility
- trust
- performance
- repeated behavior
- implementation complexity

Do not narrate every visual choice.

Use concrete language. Instead of "make the UX cleaner," say what changes, where, and why.

## Definition of Done

The work can be considered ready for implementation when:

- the primary task and outcome are explicit
- the flow covers success, recovery, and interruption
- each screen has a clear purpose and hierarchy
- interactive components have defined states
- responsive behavior is specified
- accessibility requirements are included
- behavior-design choices pass the user-benefit gate
- performance-sensitive interactions have feedback expectations
- design tokens/components are reusable where appropriate
- major assumptions are labeled
- the validation plan addresses the riskiest assumptions
- acceptance criteria can be checked by design and engineering
