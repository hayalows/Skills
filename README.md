# Skills

A practical library of reusable agent skills.

## Skill Library

- `consulting-grade-reports-decks/`
- `design-taste-frontend/`
- `frontend-design/`
- `human-copywriting/`
- `humanize-my-writing/`
- `luna-astra-behavior/`
- `lunour-brand-strategy/`
- `lunour-naming/`
- `papa-kojo-writing-style/`
- `personal-craft/`
- `premium-editorial-report-pdf/`
- `product-design-os/`
- `ui-ux-craft/`
- `website-ux-audit/`

Each skill keeps its own `SKILL.md` plus any supporting `references/`, `agents/`, and `assets/` files.

## Product Design OS

`product-design-os/` is a source-backed product design operating system for designing, reviewing, improving, and specifying digital products at a high standard.

It synthesizes:

- interface craft and component design from Adrian Kuleszo's *How to Design Better UI 3.0*
- cognitive and behavioral design principles from Jon Yablonski's *Laws of UX*
- habit and engagement mechanics from Nir Eyal and Ryan Hoover's *Hooked*, with stricter user-benefit and anti-dark-pattern guardrails
- current accessibility guidance from WCAG 2.2 and WAI-ARIA APG
- current Android accessibility guidance
- Nielsen Norman Group usability heuristics and progressive disclosure guidance
- GOV.UK form-validation patterns
- current Core Web Vitals guidance from web.dev

### Use it

Start with:

```text
Read product-design-os/SKILL.md and apply it to this product/design task.
```

The root skill routes into focused reference files, so an agent can load only the material needed for the task.

### Typical prompts

```text
Use Product Design OS to redesign this onboarding flow. Keep the existing brand, reduce friction, include every interaction state, and explain the decisions that materially affect the user.
```

```text
Use Product Design OS to audit this mobile app flow. Separate evidence from inference, identify the highest-impact issues, check accessibility and performance, then produce a prioritized fix plan.
```

```text
Use Product Design OS to design a new dashboard from this brief. Start with the user task and information architecture, then define layout, components, states, responsive behavior, accessibility, and handoff specs.
```

```text
Use Product Design OS to review this retention idea. Apply the ethical behavior-design gate before using habit-forming mechanics.
```

## Structure

- `product-design-os/SKILL.md` — router, workflow, decision rules, deliverables, and quality gates
- `references/foundations.md` — user goals, mental models, cognitive laws, hierarchy, information architecture
- `references/interface-craft.md` — responsive layout, grids, spacing, type, color, elevation, cards, hero sections
- `references/component-patterns.md` — buttons, forms, navigation, search, selects, dialogs, tables, states
- `references/accessibility.md` — WCAG 2.2, keyboard/focus, semantics, contrast, motion, input, validation
- `references/behavior-ethics.md` — Hook Model, habit testing, autonomy, user-benefit gates, deceptive-pattern prevention
- `references/research-validation.md` — research, usability testing, analytics, experiments, performance metrics
- `references/design-systems-handoff.md` — tokens, component APIs, documentation, Figma/code parity, handoff
- `references/examples-recipes.md` — worked examples across common product categories
- `references/audit-checklist.md` — reusable audit and pre-launch quality checklist
- `references/source-map.md` — source provenance and current external references

## Philosophy

A polished screen is not the goal by itself. The goal is a product that helps a real person complete a meaningful task with clarity, confidence, accessibility, resilience, and as little unnecessary effort as possible. Visual quality matters, but it cannot compensate for a broken flow.

The skill treats psychology as an explanatory tool, not a permission slip to manipulate people.

## Public Skills Directory

This repository includes a lightweight public catalogue for browsing the skills.

- Source: `site/`
- Build command: `npm run build`
- Generated output: `dist/`
- Deployment target: any static host; `vercel.json` is included for Vercel
- Skill content is generated directly from each top-level `SKILL.md`, so the website stays aligned with the source files.

The catalogue includes search, discipline filters, shareable hash routes, readable skill documentation, copyable invocation prompts, and downloadable `SKILL.md` files.

