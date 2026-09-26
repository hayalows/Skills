# Foundations: Human Behavior, Mental Models, Information Architecture

Use this reference when the design problem involves cognition, unfamiliar flows, information density, navigation structure, prioritization, onboarding, or choosing between conventional and novel interaction patterns.

## 1. Start with the user's mental model

People arrive with expectations built from other products, their domain knowledge, and the physical world.

Design implications:

- place common controls where people expect to find them unless there is a measurable reason not to
- use familiar language before internal company terminology
- preserve stable navigation and workflows during redesigns where possible
- if a major pattern must change, teach it in context and consider transition support
- do not make users relearn ordinary tasks so the interface can feel original

Novelty has a cognitive cost. Spend that cost only where the new model provides real user value.

## 2. Jakob's Law

**Use:** familiar task, familiar category, onboarding, redesign.

**Question:** What expectation will users transfer from products they already know?

**Apply:**

- start from category conventions
- preserve common navigation, search, checkout, settings, and form expectations
- change convention deliberately, not accidentally
- test departures from convention with representative users

**Do not misapply:** Jakob's Law does not require products to look identical. Familiar structure can coexist with distinctive brand expression.

## 3. Fitts's Law

The effort to acquire a target depends strongly on its size and distance.

**Use:** buttons, touch controls, menus, toolbars, mobile action placement, repeated actions.

**Apply:**

- enlarge the interactive hit area, not only the visible icon
- keep related action and input physically close
- give destructive actions enough separation from frequent actions
- place frequent controls in reachable areas
- avoid precision-heavy interactions on touch devices

Use current platform/accessibility guidance for actual target dimensions. See `accessibility.md`.

## 4. Hick's Law

Decision time tends to increase with the number and complexity of choices.

**Use:** menus, pricing, onboarding, preference screens, dashboards, forms.

**Apply:**

- remove choices that do not serve the current task
- group choices into meaningful categories
- recommend a choice when the system has enough context and the recommendation is safe
- disclose advanced options after the core path
- break long high-complexity tasks into coherent stages

**Do not misapply:** Fewer choices are not always better. Hiding critical options can create more confusion than showing them.

## 5. Miller's Law and chunking

Do not use "7 ± 2" as a hard navigation limit. The useful design lesson is that working memory is limited and context-dependent.

**Apply:**

- chunk long numbers and codes
- group related fields
- give sections descriptive headings
- keep dependencies visible
- avoid making users remember values from previous screens
- use summaries in long workflows

Chunk around meaning, not arbitrary item counts.

## 6. Postel's Law as resilient UX

Human input varies. Where safe, accept reasonable variation and normalize it for the system.

Examples:

- trim harmless whitespace
- accept phone/card/code spacing variants
- allow punctuation and diacritics in names
- preserve user-entered values when validation fails
- parse dates or numbers carefully rather than rejecting harmless formatting
- explain boundaries before requiring correction

Do not silently reinterpret ambiguous or safety-critical input.

## 7. Peak-End Rule

People often remember the emotionally strongest moments and the ending disproportionately.

Use it to identify:

- approval/rejection moments
- payment
- first success
- error recovery
- cancellation
- support escalation
- completion/confirmation

Design the ending as a real state, not an afterthought. A completion state should confirm what happened, what comes next, and where the user can go if something is wrong.

Negative peaks deserve special attention because failure, loss, embarrassment, uncertainty, and blocked tasks can dominate memory.

## 8. Aesthetic-Usability Effect

Visual polish can increase perceived usability and trust. It can also mask usability problems.

Use aesthetics to support:

- hierarchy
- legibility
- confidence
- emotional tone
- brand recognition

Never use aesthetic ratings as a substitute for task testing. During usability tests, watch behavior even when users say the interface looks good.

## 9. von Restorff Effect

Distinct items attract attention and are remembered.

Use contrast for:

- primary actions
- alerts
- critical status
- important deltas
- selected state

Restraint is mandatory. If five things compete for attention, the distinctiveness disappears.

Do not rely only on hue. Contrast may use position, size, weight, label, border, icon, or shape.

## 10. Tesler's Law

Every meaningful system contains some irreducible complexity.

The design question is where that complexity should live.

Move complexity into the system when the system can safely:

- calculate
- remember
- format
- validate
- infer
- prefill
- synchronize
- reconcile
- transform

Keep complexity visible when users need it for:

- informed consent
- professional judgment
- financial decisions
- safety
- irreversible actions
- legal or domain-critical review

Oversimplification can be as harmful as complexity.

## 11. Doherty Threshold and feedback

Fast feedback preserves flow and confidence.

Design implication:

- react immediately to clicks/taps, even if the underlying work continues
- show pressed/selected state
- use optimistic UI only when rollback is safe
- use progress indicators for meaningful waits
- explain long waits or background jobs
- prevent duplicate submissions
- keep controls from appearing dead

The historical 400 ms concept is a useful psychological reference, not a modern web-performance metric. For current web metrics, use Core Web Vitals in `research-validation.md`.

## 12. Nielsen usability heuristics

Use these as a broad review layer:

1. visibility of system status
2. match between system and the real world
3. user control and freedom
4. consistency and standards
5. error prevention
6. recognition rather than recall
7. flexibility and efficiency of use
8. aesthetic and minimalist design
9. recognition, diagnosis, and recovery from errors
10. help and documentation

Do not mechanically produce ten findings. Use the heuristic that explains the observed problem.

## 13. Progressive disclosure

Show what most people need first and make advanced or infrequent controls available when requested.

Good candidates:

- advanced filters
- expert settings
- optional profile fields
- destructive account controls
- uncommon table columns
- complex configuration

Bad candidates:

- hiding required information
- burying privacy consequences
- hiding fees
- concealing the current system state
- moving primary tasks into mystery menus

## 14. Information architecture

Before drawing screens:

### Inventory
List content, actions, objects, roles, and system statuses.

### Group
Cluster by user task and mental model, not by the company's org chart.

### Label
Use the words users use.

### Structure
Choose hierarchy, hub-and-spoke, linear flow, network, search-first, or task-first structure based on behavior.

### Validate
Use card sorting for grouping hypotheses and tree testing for findability.

## 15. User flows

A useful flow includes:

- trigger / entry
- context
- decision
- action
- system response
- branch
- recovery
- completion

Annotate system responsibilities separately from user responsibilities. This exposes places where the product is asking the user to do work the system could do instead.

## 16. Journeys and emotional peaks

Use a journey map when the experience spans time, channels, or multiple teams.

Capture:

- stages
- user goal per stage
- actions
- touchpoints
- questions
- emotional state
- friction
- opportunity
- ownership
- evidence

Pay particular attention to high-stakes peaks and endings.

## 17. Personas

Use personas only when they are grounded in research and help the team make different decisions.

A useful persona includes:

- context
- goals
- recurring tasks
- constraints
- domain knowledge
- behaviors
- pain points
- accessibility/device realities where relevant
- direct evidence

Avoid invented demographics that do not change the design.

## 18. Cognitive load audit

For each screen ask:

- What must the user understand?
- What must they remember?
- What must they decide?
- What must they physically do?
- What uncertainty remains after they act?
- What can the system remove, infer, or explain?

Common load sources:

- unlabeled icons
- hidden dependencies
- inconsistent terminology
- dense undifferentiated text
- too many equal-priority actions
- repeated data entry
- unclear progress
- invisible state
- switching between screens to compare values
- forcing memory of codes/instructions

## 19. Friction: remove the wrong kind, keep the right kind

Remove friction that is:

- repetitive
- accidental
- caused by poor system design
- unrelated to user safety or understanding

Keep or add deliberate friction for:

- irreversible deletion
- large financial transfer
- public publishing
- permission escalation
- high-impact configuration
- data export or account closure confirmations where necessary

Good friction gives the user a chance to understand consequences. Bad friction protects a metric at the user's expense.

## 20. Decision template

For a consequential design choice, record:

```text
Decision:
User goal:
Observed problem:
Evidence:
Relevant principle:
Options considered:
Chosen direction:
Tradeoff:
What would falsify this decision:
How we will validate:
```

This keeps psychology and design principles connected to evidence rather than preference.
