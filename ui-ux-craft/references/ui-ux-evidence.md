# Weighted UI/UX evidence synthesis

## How the weighting works

The source set contains 20 current videos, with 10 usable transcripts. For each of the 10 transcripted videos, a theme was counted once when the idea was materially present, even if the speaker repeated it. The result is a directional coverage measure, not a scientific estimate of design truth. A second filter keeps high-impact practices, such as accessibility and recovery states, as mandatory even when the sample mentions them less often.

For prioritization, use this simple model:

`priority = 0.50 × transcript coverage + 0.30 × user impact + 0.20 × transferability`

Coverage is normalized from 0 to 1 across the 10 transcripts. User impact and transferability are expert judgments from the cross-video synthesis. A safety/accessibility floor overrides the score: never remove those checks because a trend video omitted them.

## Direct transcript coverage

| Theme | Videos with material evidence | Coverage | Default weight |
|---|---:|---:|---|
| User problem, audience, and goal clarity | 9/10 | 0.90 | Highest |
| AI with context and human judgment | 9/10 | 0.90 | Highest |
| Flows, information architecture, and signifiers | 8/10 | 0.80 | Highest |
| Conversion, trust, and uncertainty reduction | 8/10 | 0.80 | Highest |
| Visual hierarchy and composition | 7/10 | 0.70 | High |
| Typography, color, spacing, and grids | 7/10 | 0.70 | High |
| Responsive behavior and product states | 7/10 | 0.70 | High |
| Research, testing, real products, and experiments | 6/10 | 0.60 | High |
| Consistency, components, and design systems | 6/10 | 0.60 | High |
| Accessibility and inclusion | 3/10 | 0.30 | Mandatory floor |
| Trend styling, 3D, shaders, and decorative effects | 3/10 | 0.30 | Low / conditional |

## What repeated evidence means in practice

### 1. Start with the job, not the canvas

Repeated across explainers, redesigns, learning advice, trend videos, and AI videos: define the user, context, desired outcome, constraints, and primary action before selecting colors or components. This prevents attractive but purposeless screens.

### 2. Make the next action and system status obvious

Signifiers, labels, hierarchy, states, and feedback recur across the strongest practical examples. A user should not have to infer whether something is clickable, selected, loading, complete, disabled, or safe to undo.

### 3. Reduce uncertainty at decisions

The redesign examples add a behavioral layer to visual craft: show totals, timing, eligibility, trial terms, safety signals, and consequences near the decision. Honest copy and clear CTA labels often matter more than a new visual style.

### 4. Treat the screen as a product system

Grid, spacing, type, imagery, components, content rules, and states should remain coherent across repeated views and changing data. This is both a visual-quality rule and a maintainability rule.

### 5. Design the paths that screenshots hide

Loading, empty, error, permission, offline, focus, disabled, long-content, and recovery states separate a usable product from a polished mock. Model them while the structure is still cheap to change.

### 6. Use taste deliberately

The sample does not reject expressive work. It consistently places it after fundamentals: hierarchy, type, spacing, grid, and purpose. Personality, texture, irregularity, 3D, and motion earn their place when they clarify, orient, communicate brand meaning, or make feedback easier.

### 7. Give AI context and keep accountability

The repeated AI lesson is not “use more tools.” It is “supply better context.” Give the model the brief, evidence, constraints, content, components, and acceptance criteria. Ask for bounded options or scaffolding, then review the result as a human designer, product thinker, and accessibility reviewer.

### 8. Design AI behavior, not only AI chrome

For AI features, the interface must explain context, memory, uncertainty, progress, refusal, correction, undo, permissions, and handoff. A chat box pasted into a conventional shell does not solve the interaction problem.

## A compact decision model

When choosing between two interface directions, score each from 1–5 on:

| Criterion | Question |
|---|---|
| Goal clarity | Can the intended user identify the job and next action quickly? |
| Uncertainty | Does the option answer likely questions about cost, risk, timing, and consequences? |
| Evidence | Is the choice supported by observation, testing, analytics, or an explicit assumption? |
| System fit | Does it use or extend the existing component, content, and token system cleanly? |
| State coverage | Does it handle success, loading, empty, error, focus, disabled, and recovery? |
| Access | Can people with keyboard, touch, vision, motion, language, or device constraints use it? |
| Implementation | Can the team ship and maintain it at the required performance? |
| Personality | Does the visual character serve the product rather than compete with it? |

Use the total as a conversation aid, not a substitute for user evidence. A direction that fails access, safety, or recovery should not pass because it scores well on personality.

## Research limits

- Search results and view counts change, so the ranking is a dated sample.
- Ten videos had no usable transcript in the capture environment. Metadata-only rows were not counted as transcript evidence.
- Coverage is based on idea-level coding of captions and may miss implicit teaching.
- Video popularity is not proof of correctness. The skill therefore uses repetition to set attention, then checks impact, accessibility, and implementation risk.
