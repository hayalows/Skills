---
name: ui-ux-craft
description: Evidence-weighted UI and UX craft for designing, reviewing, or rebuilding digital products. Use when a task involves interface design, user flows, information architecture, visual systems, responsive states, usability, accessibility, design critique, AI-assisted product design, or turning a rough idea into a polished working experience.
---

# UI/UX Craft

Build interfaces that help a real person complete a real job. Visual polish matters, but it follows clarity, trust, and task success.

This skill consolidates 20 recent YouTube UI/UX videos published from 2026-03-06 through 2026-09-06. Ten had retrievable caption text; ten had no usable captions, so their public descriptions and visible metadata are kept as secondary evidence. The research trail is in `references/source-matrix.md`, `references/transcript-index.md`, and `references/transcript-notes.md`. Weighted findings are in `references/ui-ux-evidence.md`.

## Route and scale the work

For a quick critique, give the main task, observed friction and a few prioritized repairs. For a full product flow, use the complete working loop. Use Website UX Audit for evidence collection and findings; use frontend-design for visual direction when needed. A design opinion is not a measured conversion result.

Treat the bundled video synthesis as a historical research sample. Its frequency counts indicate coverage, not causal evidence or universal priority. Recheck current platform guidance for implementation decisions. Product evidence and accessibility needs outrank trends and frequency counts.

## Evidence-weighted priorities

Use these as default priorities. The frequency numbers are directional coverage across the 10 retrievable transcripts, not a quality score.

1. **User goal and clarity (9/10, highest):** State the job, audience, constraints, and next action before styling. Every screen should make its purpose and primary action legible.
2. **Human judgment with AI (9/10, highest):** Give AI product context, user evidence, constraints, and a design system. Use it for exploration, variants, scaffolding, and repetitive production. Treat output as a draft. Check behavior, accessibility, edge cases, content, and performance yourself.
3. **Flows, information architecture, and uncertainty reduction (8/10, highest):** Make the path to completion obvious. Use plain labels, explicit totals, honest states, safety nets, and predictable navigation. Answer the question the user is likely to ask next.
4. **Visual hierarchy and composition (7/10, high):** Use size, position, contrast, color, weight, and whitespace to show importance. Establish a grid and spacing relationships before adding decoration.
5. **Responsive behavior and product states (7/10, high):** Design mobile and desktop breakpoints, loading, empty, success, error, disabled, focus, offline, permission, and long-content states. A single happy-path screenshot is not a product.
6. **Typography, color, and spacing (7/10, high):** Start with one strong type family unless the product has a reason for more. Define a small type scale, line-height rules, semantic color tokens, and a spacing scale. Use contrast and hierarchy, not ornament, to guide attention.
7. **Research and testing (6/10, high):** Prefer real product evidence, user interviews, usability tests, analytics, and experiments over gallery imitation. Test the riskiest assumption first and revise from observed behavior.
8. **Consistency and systems (6/10, high):** Design reusable components, tokens, content rules, and interaction patterns. A screen should belong to a coherent product, not look like an isolated poster.
9. **Accessibility and inclusion (baseline, regardless of frequency):** Preserve readable contrast, keyboard and touch access, visible focus, labels, semantic structure, target sizes, reduced motion, and screen-reader meaning. Low mention frequency in the sample does not lower its importance.
10. **Trends and special effects (low default):** Mascots, shaders, 3D, glass, retro treatments, irregular grids, and expressive motion are optional tools. Use them only when they clarify the product, carry brand meaning, or improve feedback and navigation.

## The working loop

### 1. Frame the problem

Write a short brief before opening a design tool:

- User and situation: who is here, what happened just before, and what they need now.
- Job and success: the smallest observable action that counts as success.
- Constraints: platform, device, latency, data, policy, brand, content, technical limits, and business goal.
- Risks: what could make the design confusing, unsafe, inaccessible, or impossible to ship.

If the request is vague, ask targeted questions or state assumptions. Do not invent a decorative solution to an undefined problem.

### 2. Map the experience

Sketch the happy path and at least one recovery path. Name the information architecture, entry points, decisions, permissions, confirmations, and exits. For important actions, show what happens before, during, and after the action.

Use progressive disclosure to keep the first view focused. Do not hide essential cost, risk, eligibility, or consequences behind a surprise interaction.

### 3. Prototype the structure

Start low fidelity: content, hierarchy, navigation, form logic, and state changes. Use real or representative copy, not lorem ipsum. If a decision is risky, prototype it before polishing the surface.

### 4. Build the visual system

Define tokens for type, color, spacing, radius, elevation, motion, and focus. Establish a grid, alignment rules, component variants, and content limits. Use one focal point per view. Make signifiers visible: active, hover, pressed, focus, disabled, selected, expandable, draggable, and destructive states should look and behave differently.

Keep shadows and dividers quiet. Let whitespace express relationships. Remove elements that do not support the job before adding more decoration. Break a convention only when the reason is clear and the result remains understandable.

### 5. Design every state and viewport

For each important component, specify:

`default → hover/pressed → focus → disabled → loading → success → empty → error → offline/permission (if relevant)`

Check narrow mobile, wide desktop, touch, keyboard, long labels, large text, slow network, missing images, and unusual data. Preserve hierarchy when the layout collapses; do not merely shrink the desktop view.

### 6. Test, critique, and iterate

Test the riskiest flow with representative users when available. Otherwise perform and label an expert walkthrough; do not invent participants or report simulated reactions as user research. Observe completion, hesitation, errors, backtracking and comprehension only where the method supports those observations. Use analytics or experiments for behavior claims, not taste arguments.

Run critiques as structured evaluations. State the user journey, goal/KPI, constraints, and question. Separate usability, content, visual, accessibility, and implementation issues. For every comment, record: **issue → evidence → user/business impact → recommendation → priority**.

### 7. Ship with implementation in mind

Inspect the existing code, design system, content model, and breakpoints before changing UI. Reuse components and tokens where they fit; add a new pattern only when the old one cannot express the job. Verify keyboard behavior, responsive layout, loading performance, motion preferences, and real content in the browser. A beautiful static mock that cannot survive implementation is unfinished UX.

## AI-assisted product design

Use a context-first loop:

1. Provide the product brief, users, evidence, constraints, content, platform, existing components, and acceptance criteria.
2. Ask for flows, edge cases, variants, copy alternatives, or code scaffolding, not an unbounded “make it beautiful” screen.
3. Keep the design system and decisions in a durable source of truth. Feed the relevant slice back to the model.
4. Review generated output for hierarchy, signifiers, semantic HTML, contrast, focus, responsive behavior, data states, privacy, and performance.
5. Test the result with people and real content. Record what changed and why.

For AI products, design the behavior as carefully as the shell. Make conversational, agentic, memory/context, personalization, progress, uncertainty, refusal, correction, undo, and human handoff states visible. Tell users what the system knows, what it is doing, what it may be wrong about, and how to regain control.

## Fast quality gate

Before handoff, mark the applicable checks as verified, unverified or not applicable, with a reason. Do not turn a proposed state or inaccessible test into a yes:

- Can a first-time user name the purpose and primary action quickly?
- Does the interface reduce uncertainty about cost, risk, timing, and next steps?
- Are hierarchy, signifiers, copy, and states understandable without a tutorial?
- Is the main flow usable on mobile, desktop, keyboard, and slow network?
- Are empty, loading, success, error, focus, disabled, and recovery states designed?
- Do color, type, spacing, imagery, and motion form a coherent system?
- Is the contrast and semantic structure accessible, with reduced-motion behavior?
- Is the pattern supported by user evidence or a clearly stated assumption?
- Can the design be implemented and maintained with the existing product system?
- If AI helped, can a human explain and defend every important decision?

When a choice is uncertain, prefer the option that makes the user's goal, system status, and recovery path more obvious.

## Research references

- `references/ui-ux-evidence.md` — weighted synthesis and coverage counts.
- `references/source-matrix.md` — the 20-video scope, ranking method, dates, links, and evidence status.
- `references/transcript-index.md` — transcript export status and copyright-safe handling.
- `references/transcript-notes.md` — paraphrased notes from every retrievable transcript plus metadata notes for the rest.
