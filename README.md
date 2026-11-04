# Skills

A practical library of reusable agent skills.

## Master Craft: one-call orchestration

[Master Craft](master-craft/SKILL.md) is the single entry point for selecting and sequencing relevant skills across this repository. It uses Personal Craft for substantial execution, Product Design OS for real UI/UX, engineering/research/brand specialists as needed, and Vercel Deployment Steward for eligible releases. The [routing map](master-craft/references/skill-map.md) currently covers every other saved skill, including Matt Pocock's collection. See [usage and installation](master-craft/README.md). It does not automatically grant tools, launch agents or publish anything.

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
- `master-craft/`
- `personal-craft/`
- `premium-editorial-report-pdf/`
- `product-design-os/`
- `security-audit/` (Cloudflare, MIT licensed)
- `ui-ux-craft/`
- `website-ux-audit/`
- `vercel-deployment-steward/`

Each skill keeps its own `SKILL.md` plus any supporting `references/`, `agents/`, and `assets/` files.

## Vercel Deployment Steward

The [Vercel Deployment Steward skill](vercel-deployment-steward/SKILL.md) helps keep Hobby deployments under control across all projects. It audits account-wide deployment history, flags shared-repository fan-out, reviews release readiness, and explains ways to reduce unnecessary preview and production builds.

It includes a read-only Node CLI, an offline test harness, release guidance, current platform references, and an evidence-based Pitch Night case study. Its FREEZE threshold is an advisory safeguard for unattended releases, **not proof that Vercel cannot publish**. Following a verified manual API 402 and subsequent successful Git deployments, the skill now distinguishes the two creation paths and avoids claiming a guaranteed retry minute. It does not deploy projects, change billing, disable Git deployments, or run recurring checks without separate authorization.

See [operations](vercel-deployment-steward/references/operations.md), [CLI usage](vercel-deployment-steward/references/cli-usage.md), and [platform facts](vercel-deployment-steward/references/platform-facts.md).

## Security Audit

`security-audit/` is a locally saved copy of Cloudflare's multi-phase defensive security audit skill, including all domain companions, JSON schema, validators, tests, and its MIT licence. Use [the skill](security-audit/SKILL.md) to review code and [PKM usage notes](security-audit/PKM-USAGE.md) for scoped checks and complete-audit setup. Full audits need an isolated OS-enforced sandbox; do not test live services or confuse unverified concerns with confirmed vulnerabilities.

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

## Matt Pocock Skills Collection

A complete MIT-licensed snapshot of Matt Pocock's engineering and productivity skills is saved under [`collections/matt-pocock-skills/`](collections/matt-pocock-skills/README.md). It includes 27 main skills, experimental and miscellaneous skills, and their supporting files. See [PKM usage notes](collections/matt-pocock-skills/PKM-USAGE.md) for setup and project examples. This copy is not automatically installed as an agent plugin.
