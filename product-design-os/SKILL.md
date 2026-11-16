---
name: product-design-os
description: "Design, redesign, audit, specify or build the UI and UX of a digital product: websites, web apps, mobile apps, dashboards, forms, onboarding, checkout, search, pricing pages, design systems and components. Use when a task changes what a user sees or does, when a screen looks generic or confusing, or when a design needs to be turned into working, verified code. Covers flows, hierarchy, visual direction, states, accessibility, performance, ethical engagement, a render-and-look verification loop and a scored quality rubric. Self-contained: works alone or under Master Craft."
---

# Product Design OS

Turn a brief, a screenshot, a codebase or a rough idea into a product experience that is useful, usable, accessible, good-looking for a reason, and proven by looking at the real thing.

This skill is self-contained. Every reference it needs is inside this folder. It works with any model or agent that can read files. With a shell it can also run its own checks.

## Core standard

A design is ready only when a user can understand what is happening, know what to do next, complete the task, recover from errors, use it with a keyboard or assistive technology, and trust what the system tells them.

Three things this skill refuses to confuse:

- **Novelty is not quality.** Use familiar patterns for familiar problems. Depart from convention only when the benefit is specific, testable and worth the learning cost.
- **Engagement is not value.** Repeated use is good only when it serves a recurring need of the user.
- **Described is not verified.** A screen you have not rendered and looked at is a guess. Say which it is.

## Size the job first

Pick the smallest tier that fits. Do not run a full process on a small request.

| Tier | Example | Do | Skip |
| --- | --- | --- | --- |
| **Touch** | Fix a label, a spacing bug, one component state | Inspect, change, look at the result, check neighbours did not break | Briefs, flows, rubric |
| **Screen** | Design or repair one screen or component | Steps 1, 4 to 8 below. Score the rubric | Research plan, full system spec |
| **Flow** | Onboarding, checkout, a feature with several screens | All steps. Every state. Rubric with evidence | Nothing material |
| **Product** | New app, full redesign, design system | All steps, slice by slice, with a written direction and tokens | Nothing. Work in vertical slices, not all screens at once |
| **Audit** | "Review this", "what is wrong with this" | Evidence, findings, priorities. No edits unless asked | Building |

An audit request is not permission to change anything. A build request is not permission to publish.

## The loop

Steps 1 to 5 decide. Steps 6 to 8 prove. Load a reference only when its step needs it.

### 1. Frame the problem

Establish what the task needs from this list. If the user already gave it, proceed. If something is missing and would not change the design, state an assumption and continue. Ask only when the answer would change the direction.

- product or surface, and platform (responsive web, iOS, Android, desktop)
- primary user and the job they are trying to finish
- current state or reference, if one exists
- constraints: brand, tech, content, data, compliance, devices, connectivity, time
- the success signal, and known risks

Write the problem in one sentence:

`[User] needs to [task or outcome] in [context], but [friction or constraint] makes that difficult.`

Then name the primary task, the moment of entry, the desired end state, the cost of failure, and the business goal. If the business goal and the user goal conflict, say so plainly. Do not hide the conflict inside interface mechanics.

Reference: `references/foundations.md` for mental models, cognitive principles, information architecture and journeys.

### 2. Map the experience before styling it

For any flow with more than one meaningful action, map entry points, user decisions, system decisions, data needed, branches, the success path, cancel and undo, and what happens on interruption and return.

Then list the states this flow can reach: empty, loading, validation error, system error, no permission, offline or degraded, success.

Make the shortest safe path obvious. Do not remove necessary context just to reduce the number of screens.

### 3. Reduce effort

Apply in this order:

1. remove unnecessary steps
2. remove unnecessary decisions
3. add smart defaults only where they are safe and reversible
4. make the preferred next action obvious
5. group related information
6. reveal advanced options progressively
7. keep information visible so users recognise instead of recall
8. make frequent targets large and easy to reach
9. keep feedback next to the action that caused it
10. let the system carry complexity the user should not carry

Before adding badges, reminders, streaks or persuasion, first ask whether the action itself can be made easier.

### 4. Set hierarchy and structure

For every screen identify: one primary purpose, one dominant next action if an action is required, supporting information, secondary actions, advanced actions, destructive actions, and system status. The visual hierarchy must match this task hierarchy. If everything is prominent, nothing is.

Design from the smallest realistic width upward. A single desktop frame is not the product. Specify container and gutter behaviour, alignment anchors, vertical rhythm, how components wrap or stack, breakpoints chosen where the content breaks, sticky elements, safe areas, the mobile keyboard, long text and localisation, and zoom and reflow.

Use a small spacing scale instead of arbitrary values. A 4px or 8px base is a useful start, not a law.

Reference: `references/interface-craft.md` for layout, grids, spacing, type, colour, depth, tables and dashboards.

### 5. Choose a visual direction

Skip this step when a brand or design system already exists: use it.

Otherwise decide on purpose, in this order: how loud the surface should be (a tool used for hours is quiet, a landing page can be loud), what belongs to the subject's own world, three words for the feeling, and one signature element. Then set six dials: type voice, colour, density, shape, imagery and motion. Record them as tokens. Start from `assets/tokens.css` and change the values.

Check the direction against one question: would this exact look have come out for a different product? If yes, it is a default, not a choice.

Reference: `references/visual-direction.md`.

### 6. Design components as behaviour

A component is a set of states and rules, not a picture. For each interactive component define the states that apply:

`default, hover, focus, pressed, selected, disabled, loading, success, warning, error, empty, read-only, permission-limited, pending`

and the rules: label, icon meaning, keyboard behaviour, target size, validation, feedback, destructive behaviour, responsive behaviour, accessible name, role and state, and what happens after activation.

A component is incomplete if its error, loading or focus behaviour is unspecified.

Reference: `references/component-patterns.md` for buttons, forms, navigation, search, dialogs, tables and state patterns. `references/examples-recipes.md` for worked examples by product type.

### 7. Build it and look at it

When the task includes implementation, build one complete slice with real content, then run the look loop:

1. Run the static floor: `node product-design-os/scripts/ui-lint.mjs <path>`. Fix every error.
2. Render the page and capture it at 360, 768 and 1280 wide.
3. Look at each capture as a first-time user. Write down what you see, not what you intended.
4. Operate it: keyboard path, 200% zoom, empty, error, slow network, double submit, back and refresh.
5. Measure contrast for real colour pairs: `ui-lint.mjs contrast <fg> <bg>`.
6. Fix the largest problem first. Render again.

Expect two or three passes. Most quality arrives after the first.

If nothing in the environment can render the page, say `NOT VISUALLY VERIFIED`, review by reading, and list what a person should look at. Never describe the appearance of something you have not seen.

Reference: `references/build-and-verify.md`.

### 8. Score, then hand off

Score the result on the ten dimensions in `references/quality-rubric.md`. Each dimension has a floor. Any score below its floor sends the work back into the loop, whatever the total.

Then hand off what the task needs: tokens, type and colour roles, spacing scale, component anatomy with variants and states, interaction and responsive behaviour, content rules, accessibility requirements, analytics events if needed, performance expectations, and acceptance criteria that design and engineering can both check.

Reference: `references/design-systems-handoff.md`, `references/audit-checklist.md`.

## Gates

Run the gates that apply. They are not optional when they apply.

### Interface restraint and the UX / DX / AX gate

Apply these two principles to every relevant interface decision:

> Cut taglines, helper text and secondary labels. If a screen needs them to make sense, fix the layout.

> Make the best decision that will elevate all three: the user experience (UX), developer experience (DX), and agent experience (AX) always, without breaking anything.

**Read the first rule as a test of information architecture, not a command to erase essential information.** Begin by removing redundant slogans, repeated categories, decorative labels and text that only compensates for a confusing layout. Give the screen a clear purpose, strong hierarchy, familiar patterns and obvious actions. If comprehension still depends on helper copy, repair the grouping, placement, affordance or flow before adding words back. Keep necessary labels, instructions, error recovery, safety information, context, proof, accessible names and anything needed for an informed decision. Do not hide essential meaning behind hover, motion or icons.

**Assess all three experiences together before choosing an implementation:**

- **UX, user experience:** people can recognise what they are looking at, complete the main task, recover from problems, and use the interface across mobile, desktop, keyboard, touch, zoom and assistive technology. Measure task completion or observable comprehension, not visual preference alone.
- **DX, developer experience:** the change fits the existing stack, uses maintainable components and semantic tokens, has clear interfaces, avoids duplicate logic and unnecessary dependencies, and can be tested, debugged and safely extended.
- **AX, agent experience:** agents and automated tools can reliably interpret the product through semantic HTML, meaningful accessible names, stable URLs, machine-readable data or API contracts where appropriate, explicit states and predictable outcomes. Do not add a new agent integration without a task-driven need.

**"Without breaking anything" is a regression requirement, not a claim of zero risk.** Identify the existing user paths, deep links, data formats, analytics, keyboard behaviour, accessibility, search and indexing semantics, and integration contracts that must stay intact. Prefer a small reversible change. Run relevant existing tests and compare important interactions before and after. If a choice helps one experience and harms another, state the trade-off and choose the least disruptive option that protects the core task. Do not claim a UX, DX or AX improvement without showing what changed and how it was checked.

### Accessibility gate

For web work, target WCAG 2.2 AA unless the user names another standard. These are design responsibilities, not late QA:

semantic structure, keyboard operability, visible focus, accessible names and instructions, text and non-text contrast, target size and spacing, no colour-only meaning, error identification and recovery, zoom and reflow, reduced motion, correct control relationships for screen readers, and sensible focus management in dialogs and dynamic content.

Reference: `references/accessibility.md`.

### Ethical behaviour gate

Run this whenever the product includes retention loops, notifications, streaks, variable rewards, social proof, defaults, autoplay, infinite feeds, urgency, scarcity, subscriptions, cancellation flows, persuasive onboarding, gamification or repeated prompts.

Before applying any engagement mechanic, answer:

1. What recurring user problem does this behaviour solve?
2. Would the user still choose this if the mechanism were explained plainly?
3. Is it easy to stop, mute, undo or leave?
4. Does it preserve meaningful choice?
5. Is the reward tied to user value, not time spent?
6. What happens to vulnerable, compulsive, distressed or unintended heavy users?
7. Are we measuring a user outcome alongside the business metric?

Do not build around compulsion, false scarcity, obstructed cancellation, disguised ads, forced continuity, confirm-shaming or hidden consequences.

Reference: `references/behavior-ethics.md`. For one focused moment of activation, progress or voluntary repeat use, load [Behavioral Interaction Design](../behavioral-interaction-design/SKILL.md) when it is available.

### Resilience gate

Test outside the happy path. At minimum consider: slow network, timeout, partial data, duplicate action, accidental repeat tap, refresh, back navigation, interrupted session, expired sign-in, denied permission, unavailable dependency, empty history, very long names and content, small screen, zoomed text, first-time user and returning expert.

The product should fail in ways a person can understand and recover from.

When many users are on low-cost phones, metered data or unreliable networks, load `references/constrained-contexts.md`. It also covers mobile payment flows.

### Evidence gate

When design inputs conflict, prefer evidence in this order:

1. direct user needs, observed behaviour and task evidence
2. product analytics and support evidence
3. accessibility requirements and platform conventions
4. product constraints, domain rules and technical reality
5. established interaction patterns and cognitive principles
6. competitive references
7. aesthetic preference

A UX law is a hypothesis and a guardrail, not proof that a design will work. Validate important decisions with users or behaviour data. Choose the lightest method that answers the biggest uncertainty: interview, card sort, tree test, prototype usability test, cognitive walkthrough, heuristic review, accessibility test, analytics, experiment or field performance data. Do not ask users which design they like when the real question is whether they can complete the task.

Never invent participants, test results, metrics or quotes. An expert walkthrough is labelled as an expert walkthrough.

Reference: `references/research-validation.md`.

### Psychology, used carefully

Use cognitive principles to explain behaviour, not to decorate a rationale.

- Jakob's Law: keep familiar mental models for familiar tasks.
- Fitts's Law: make important targets easy to reach.
- Hick's Law: reduce unnecessary choice.
- Miller's Law: chunk information. There is no magic limit of seven.
- Postel's Law: accept reasonable variation in input, produce structured output.
- Peak-End Rule: design the high-stakes moments and the ending on purpose.
- Aesthetic-Usability Effect: polish raises perceived usability and can hide real defects.
- von Restorff Effect: make the most important item distinct, and use contrast sparingly.
- Tesler's Law: unavoidable complexity lives somewhere. Prefer the system carrying it.
- Doherty Threshold: respond fast, and show feedback at once when work continues in the background.

## Operating modes and what to deliver

| Mode | Deliver |
| --- | --- |
| **New product or feature** | Brief and assumptions, primary user and job, flow or IA, screen and component architecture, visual direction and tokens, states, responsive rules, accessibility requirements, measurement plan, risks and open questions, implementation-ready spec or the built slice with its rubric |
| **Redesign** | First separate what is broken, what is only unfamiliar, what is constrained, what already works, and what must stay stable for users. Then change the smallest set of things that meaningfully improves the outcome |
| **Audit** | For each issue: location, observed behaviour, user consequence, principle or evidence, recommended change, severity by task impact, confidence, and how to validate the fix. Add the rubric scores. No generic aesthetic opinions |
| **Design system** | Foundations and semantic tokens, then primitives, then components, then compositions. Document when to use and when not to use, not only variants |
| **Component spec** | Purpose, anatomy, variants, states, content rules, behaviour, responsive behaviour, accessibility, errors, examples, anti-patterns, acceptance criteria |
| **Behaviour or retention** | Run the ethical behaviour gate. Design a habit loop only when repeated behaviour serves the user's own recurring goal |
| **Landing or marketing surface** | A page that quickly answers: what is this, who is it for, what useful change does it provide, why should I believe it, what can I do next. Conversion tactics must not damage clarity, consent or credibility |
| **Build** | Working code in the project's own stack, the look-loop evidence, rubric scores, and a plain list of what was not verified |

When presenting work, explain the decisions that materially affect task success, cognitive effort, error risk, accessibility, trust, performance, repeated behaviour and implementation cost. Do not narrate every visual choice. Use concrete language: say what changes, where and why, not "make the UX cleaner".

## Reference map

Load only what the task needs.

| Need | File |
| --- | --- |
| Cognition, journeys, mental models, IA | `references/foundations.md` |
| Layout, type, spacing, colour, cards, heroes, dashboards | `references/interface-craft.md` |
| Choosing a look on purpose | `references/visual-direction.md` |
| Buttons, forms, navigation, search, dialogs, tables, states | `references/component-patterns.md` |
| Accessibility | `references/accessibility.md` |
| Retention, habits, notifications, engagement ethics | `references/behavior-ethics.md` |
| Research, testing, metrics, performance | `references/research-validation.md` |
| Tokens, libraries, documentation, handoff | `references/design-systems-handoff.md` |
| Implementing and checking a real page | `references/build-and-verify.md` |
| Scoring quality | `references/quality-rubric.md` |
| Budget phones, metered data, weak networks, mobile payments | `references/constrained-contexts.md` |
| Worked examples by product type | `references/examples-recipes.md` |
| Audit and pre-launch checklist | `references/audit-checklist.md` |
| Provenance and external sources | `references/source-map.md` |
| Starter tokens (CSS) | `assets/tokens.css` |
| Static checks and contrast (Node, no dependencies) | `scripts/ui-lint.mjs` |

## Working with other skills

This skill owns the product experience. Others own narrower jobs. When they are not available, this skill is enough on its own.

| Job | Skill |
| --- | --- |
| Choosing and sequencing skills across a whole project | Master Craft |
| Read-only diagnosis of an existing website with a formal report | Website UX Audit |
| Composition and taste for landing pages, portfolios and editorial sites | Design Taste: Frontend, or Frontend Design |
| One activation, progress or repeat-use moment | Behavioral Interaction Design |
| Proving a change improved an outcome, or deciding a rollout | Product Evidence |
| Execution discipline and test policy for substantial work | Personal Craft |

## Universal decision rules

Prefer:

- clarity over cleverness
- recognition over recall
- direct manipulation over hidden commands
- fewer meaningful choices over many similar ones
- reversible actions over confirmation dialogs, when safe undo is possible
- prevention over error messages
- tolerant input parsing over forcing machine formats
- explicit labels over placeholder-only fields
- visible focus over decorative focus removal
- immediate feedback after input
- real progress over fake progress
- user-controlled notifications over aggressive re-engagement
- content-first breakpoints over device-name breakpoints
- semantic tokens over literal colour and size values
- native and standard controls, unless a custom one has a demonstrated benefit
- real content and realistic edge cases in every review
- evidence-backed rationale over taste debates

## Anti-patterns

Reject or challenge:

- hidden or shifting navigation without a strong user reason
- tiny targets, and low-contrast text used for fashion
- a destructive primary button beside a harmless secondary one with weak distinction
- disabled controls with no explanation
- placeholder-only labels
- validation that erases input, and errors that only say "invalid"
- nested modals
- auto-advancing carousels without controls
- infinite feeds where the task has a natural stopping point
- autoplay that steals attention
- fake scarcity, fake activity, fake social proof
- preselected paid add-ons, and cancellation harder than signup
- asking for notification permission before showing value
- no feedback after an action, and skeletons that shift layout when content arrives
- arbitrary one-off spacing values, and one-off components that duplicate an existing pattern
- dramatic dashboards that hide the decision the user needs to make
- mobile layouts made by shrinking desktop
- animation that is required to understand state
- meaning carried by colour alone
- habit mechanics without a user-benefit case
- a look chosen by default instead of for the subject
- describing a result as verified when it was only read

## Definition of done

Ready for implementation when:

- the primary task and outcome are explicit
- the flow covers success, recovery and interruption
- each screen has a clear purpose and hierarchy
- interactive components have defined states
- responsive behaviour is specified
- accessibility requirements are included
- behaviour-design choices pass the user-benefit gate
- performance-sensitive interactions have feedback expectations
- tokens and components are reusable where appropriate
- major assumptions are labelled
- the validation plan addresses the riskiest assumptions
- acceptance criteria can be checked by design and engineering

Ready to ship when, in addition:

- the page was rendered and looked at across the supported widths, or the gap is stated
- `ui-lint` reports no errors, and remaining warnings are deliberate
- the keyboard path, zoom and the reachable states were operated
- contrast was measured for the real colour pairs
- every rubric dimension meets its floor, with evidence
- the report says plainly what was seen, operated, measured, read and not verified
