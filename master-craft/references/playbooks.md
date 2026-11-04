# Master Craft: task playbooks

These are conditional stage plans, not a compulsory pipeline. Read the selected skill's actual SKILL.md first. Personal Craft is the baseline for substantial execution. Product Design OS applies when designing a product experience. Never turn inspection-only work into edits or publication.

## Existing product UI/UX

1. Inspect the project, current routes, real user journeys, existing design system, code and reported pain. If user requested only an audit, use website-ux-audit and end with documented findings.
2. Use product-design-os to map user tasks, navigation and states. Add ui-ux-craft for design/accessibility details. For marketing websites or portfolios, choose design-taste-frontend OR frontend-design rather than invoking both by default.
3. Use product-evidence when a comparative measurement or decision gate matters. Establish before/after user outcomes and relevant mobile, desktop, touch, keyboard, search, error, loading, empty, slow connection and permission behaviors. Avoid clutter and decorative change without benefit.
4. On authorization to edit, use personal-craft for implement/verify and Matt's tdd only if aligned with the user's test-first E2E policy. Use diagnosing-bugs if a defect requires reproduction, not for every feature.
5. Review actual UI, code changes and regressions. For consequential changes add code-review. A complete security audit is not compulsory for a cosmetic improvement.
6. Release only on permission, with the relevant host preflight, and verify the live revision and representative path.

## Bug repair

1. Use diagnosing-bugs to reproduce and isolate the problem in a short red-capable loop. Check the current state before guessing the cause.
2. Document scope and failure cases. Follow Personal Craft verification: new behavioral tests should be chosen and authored before implementing behavior, preferably E2E. Do not append retrospective unit tests without the documented exception.
3. Repair the smallest relevant code, rerun failing case, neighboring cases and existing checks. Preserve the codebase's other edits.
4. Use code-review for material behavior or security changes. State actual red/green evidence and remaining uncertainties.
5. Release only on authorization after host-specific preflight.

## New feature, app or substantial rebuild

1. Establish the end user, job, success measure, product/technical constraints and permission boundaries. Infer routine reversible details. Use grill-with-docs only for important unresolved decisions with a durable workspace; without one use grill-me if questions are needed.
2. Use product-design-os for user flows, information architecture, component and interaction states. Use domain-modeling for complex business terminology; prototype to resolve expensive uncertainties.
3. For a multi-stage build, apply to-spec and optionally to-tickets; use implement or implement-spec only where their tools and working assumptions fit. For bounded changes, implement directly.
4. Plan the test strategy before code. Add tdd for compatible behavior; review architecture, roles and data access early.
5. Build complete vertical slices, validate and review independently for high-consequence decisions. Consider retro only when a meaningful engineering session has completed.
6. Publish through the correct release gate if asked; verify production.

## Brand strategy, naming and content

1. Pick lunour-naming for naming, lunour-brand-strategy for positioning/identity, human-copywriting for audience-directed copy. For writing as the user add papa-kojo-writing-style; never impose the user's personal voice on a client's brand.
2. Research real audiences, competitors, claims, legal/domain availability when relevant; distinguish screening from legal clearance. Avoid fabricated evidence and clichéd generic identity work.
3. For marketing sites add design-taste-frontend or frontend-design. Add Product Design OS only for meaningful customer flows, forms or app-like interactions.
4. Deliver usable original assets, explanations, audience-fit and relevant files; inspect output and rights/attribution.
5. For finding clients, create-opportunities supports target and work-sample decisions; thoughtful-cold-email handles appropriate outreach. Never send without explicit instruction.

## Research, business decisions, finance, reports and decks

1. Define audience, decision, evidence, alternative scenarios, data provenance and uncertainties.
2. Use model-assurance when formulas, forecast validity or scenario assumptions drive the result. Use consulting-grade-reports-decks to make a disciplined argument. Use specialist domain workflows and current primary data where essential.
3. Use premium-editorial-report-pdf only after the content and evidence are stable. Render the requested file and inspect readability and calculations.
4. Label illustrative numbers and hypotheses. No invented returns, medical outcomes, testimonials, quotes or citations. Do not route to Product Design OS for an ordinary report.

## Defensive security or sensitive data

1. Define exact trust boundaries, assets, users, permissions, available evidence and authorized read/write scope.
2. Use security-audit for a specific relevant risk or explicit requested audit. Full audit mode is only for a comprehensive request AND its mandated isolated execution controls. Never probe live systems just because the skill exists.
3. Distinguish confirmed issue, suspected issue, severity and confidence. Check authorization server-side, cross-user records, exposed secrets, untrusted inputs and data lifecycle where applicable.
4. Plan safe synthetic tests and fixes, preserve data, and independently review high-consequence changes. Never claim certification or a full penetration test from static source review.
5. Release only when authorized and checks support it.

## Vercel and other deployment

1. Determine whether the user requested deployment, exact host, account, project, branch, current revision and intended domain.
2. For Vercel use vercel-deployment-steward before a hosted build, preview or release, including team-wide headroom, 402 failures and Git fan-out. Do not bypass its quota gates or alter billing.
3. For Cloudflare, Netlify, or other hosts, inspect actual deployment and build workflows; do not apply Vercel-specific thresholds.
4. Validate locally and avoid repeated exploratory preview deployments. Release through one authorized path, observing auto-deploy triggers.
5. Check production commit, readiness, URL, core flow and errors. Distinguish published-and-verified from published-but-unverified.

## Learning and agent automation

- For teaching use teach or wait-what; avoid engineering release processes.
- For rewriting use humanize-my-writing and relevant voice. Avoid invoking an entire marketing strategy.
- For writing skills or agent instructions use writing-for-agents. Model invocation, actual tool support and progressive disclosure matter.
- For multi-agent design, software-factory and chief-of-staff are experimental; their instructions do not create runtimes or background schedules. Use a real tool or single-worker plan.
- For specialized git hooks, testing tools, or TypeScript module policies, use one matching misc skill, checking current environment and write permission.

## Progression and stopping conditions

Gate 0 authority: right repo and explicit mode. Gate 1 baseline: current state and intended observable outcome. Gate 2 decision: smallest viable design with clear requirements. Gate 3 execution: code/artifact completed within scope. Gate 4 verification: evidence, nearby regressions and meaningful quality gates. Gate 5 release: user authorization, budget/quotas and actual production checks. Gate 6 handoff: truthful report.

Any blocked gate stops that phase. Continue independent safe work if possible, but never report later gates as passed without evidence.
