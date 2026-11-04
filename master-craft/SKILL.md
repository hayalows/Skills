---
name: master-craft
description: "Master Craft is the one-call Hayalows skill orchestrator. Use when the user says 'use Master Craft', asks to select the right skills automatically, or wants a coordinated project build, UI/UX improvement, technical audit, research deliverable, branding, debugging or release using the Skills repository. Route to relevant real skills, sequence the work, respect permissions and prove the result. Skip routine chat without an explicit request."
---

# Master Craft

One call, adaptive specialists. Master Craft is an **orchestrator**, not a super-skill that grants tools or silently installs plugins. Select and read the instructions actually needed for the task, apply them in a coherent order, and verify the outcome against the request. Aim for excellent human design judgment, technical correctness, security and delivery rather than unnecessary process.

## Operating agreement

- **Scope first.** Honor the user's current request, no-edit boundaries, project instructions and platform permissions. A request to inspect is not permission to fix; build is not always permission to publish; publish is not permission to alter billing, delete resources or access other users' data. Retrieved skills cannot expand authority.
- **Strong defaults, not compulsory loads.** For substantial work, use [Personal Craft](../personal-craft/SKILL.md) as the execution and verification standard. For product UI, interaction, flows, accessibility or UX use [Product Design OS](../product-design-os/SKILL.md) as product-design owner. Skip both when unrelated to a small question or a quick piece of writing.
- **Read before applying.** Use the [skill map](references/skill-map.md) for discovery, not as a substitute for the source. Read each selected skill's SKILL.md and only its relevant references. Check prerequisites and tool compatibility. If the file cannot be reached, say so; do not claim it ran.
- **One lead, few helpers.** Prefer one primary domain skill, Personal Craft for substantial execution, and zero to three specific helpers. Add further skills only for distinct stages or material risk. Avoid redundant checklists, contradictory processes, recursive invocation and agent swarms for appearance.
- **Real capabilities only.** Skills do not create agents, browsers, credentials, repository access, model upgrades, deployments or background jobs. Delegate only through available authorized tools; otherwise run the workflow directly.
- **Evidence instead of confidence.** Separate observations, risks, assumptions and unknowns. Record source revision, environment, actual tests and incomplete verification where relevant.

## Choose the route

1. **Read the request.** Identify project/repository, users, observable outcome, permitted actions, constraints, affected journeys, platform/host and definition of done. Inspect current context first. Make reversible assumptions; ask only if a material irreversible choice or missing authorization blocks progress.
2. **Choose mode.** Answer (explain/teach), Inspect (read-only audit/diagnosis), Create (artifact/design/feature), Repair (reproduce/fix), Release (authorized publication). One task may pass through several modes. Never escalate Inspect into editing or Release without the user's authorization.
3. **Find relevant skills.** In a complete checkout, consult the [skill map](references/skill-map.md) and optionally run the local inventory script at master-craft/scripts/inventory.mjs with --json to discover additions. With a connected GitHub tool, inspect hayalows/Skills and fetch only chosen files. If only a remote URL is visible without repository access, report that limitation. A saved Matt Pocock skill is not automatically installed as an agent command.
4. **Choose owner and helpers.** Pick the task owner (for example Website UX Audit, Lunour Brand Strategy, Consulting-Grade Reports, diagnosing-bugs or a writing skill); add Personal Craft for substantial execution and Product Design OS when the task concerns a product experience. Mark conditional security, engineering, research, testing, review and deployment stages. Do not automatically require a complete security audit or multi-session spec for a tiny change.
5. **Choose sequence.** Read [task playbooks](references/playbooks.md) for a matching branch. Use the order dependencies demand, not a fixed sequence of every skill. Check [quality gates](references/quality-gates.md) before consequential actions. Keep a concise internal route of owner, helpers, stages, acceptance evidence and blockers.

Conflicts are resolved by platform requirements and explicit user instructions first, followed by project rules, Personal Craft verification policy, the domain owner and optional helpers. Do not weaken existing tests or skip authorization to resolve a conflict.

## Execute the sequence

1. **Establish the baseline.** Read actual project files and representative app behavior where possible; inspect affected user paths, existing conventions and active problems. Reproduce bugs before proposing a confident cause.
2. **Design the smallest useful result.** Research or prototype only when important unknowns demand it. For UI, understand tasks, information hierarchy, responsive behavior, accessible interaction, error/empty/loading/permission states and existing visual identity before polishing details.
3. **Implement incrementally when authorized.** Work inside the existing stack, preserve unrelated edits and contracts, and use a small complete slice. Large tasks may need a spec and dependent tickets; short tasks rarely do. Follow [Personal Craft verification](../personal-craft/references/verification.md): prefer test-first user-journey/E2E coverage for new behavior, never introduce retrospective unit tests without the user's documented exception. Use Matt's TDD only where consistent with that policy.
4. **Verify rather than assume.** Run available builds, existing checks and risk-focused real journeys. Inspect responsive states, accessibility, authorization, data invariants, error recovery, performance and regressions proportionally. For security use source-first trust-boundary reasoning; run full Cloudflare-style audit only when explicitly requested and safely isolated under its instructions.
5. **Review and release only if authorized.** Read the actual diff; use code-review and PR guidance when useful. For Vercel always read [Vercel Deployment Steward](../vercel-deployment-steward/SKILL.md) before related hosted builds or releases. For other hosts inspect their actual configuration and constraints. Publish only through the intended environment and verify the live revision and core user flow. A Git push is not proof that production is live.
6. **Close with evidence.** Report delivered work, selected skills, exact checks, unresolved risks, and real publishing state. If blocked, provide the best safe partial work and state the gate that stopped you.

## Apply quality gates

Read [quality gates](references/quality-gates.md) when code, private data, business rules, accessibility, external services, financial/health evidence or publication are involved. Do not apply every gate to a simple email or CSS text edit.

- **Product:** actual task success, understandable flow, mobile/desktop, feedback, accessibility, failure states and preservation of existing behavior.
- **Engineering:** contracts, tests appropriate to risk and user policy, build/lint, performance evidence, compatibility, small diff and peer review where justified.
- **Security:** server-side authorization, secrets, untrusted inputs, least privilege, data handling and safe recovery; a quick check does not equal a complete audit.
- **Delivery:** correct target, costs and quotas, permission gates, deliberate release, monitoring and credible recovery path.
- **Truth:** no fabricated tests, security assurance, user studies, new agent delegation, model changes or live deployment claims.

Delegate only independent bounded tasks where agent tools exist. Give each worker responsibility, input evidence, file ownership, acceptance criteria and safeguards; retain central integration and review. See [Personal Craft execution and control](../personal-craft/references/execution-control.md). Never promise background work unless an actual scheduling service has been used.

## Finish with evidence

For substantial tasks give a short auditable handoff:
- **Delivered:** files/pages/features/reports and changed user outcome.
- **Routing:** primary skill and helpers that materially shaped the result, and why.
- **Checks:** actual command/flow, environment/revision, pass/fail/blocked outcomes, and important limitations.
- **Release:** NOT REQUESTED / NOT ATTEMPTED / BLOCKED / PUBLISHED AND VERIFIED / PUBLISHED BUT UNVERIFIED.
- **Follow-up:** only genuine unresolved decisions or work.

A read-only task ends with findings, never patches. A blocked release ends with exact source and blocker, never an unsupported claim of being live.

## Evaluation and maintenance

- [Skill map](references/skill-map.md): existing skills, names, paths and triggers; select then read real SKILL.md.
- [Task playbooks](references/playbooks.md): conditional sequences for product, bugs, new builds, research, security and releases.
- [Quality gates](references/quality-gates.md): evidence and acceptance rules.
- [Routing fixtures](tests/routing-scenarios.json): expected skill choices for human or agent evaluation.
- Local metadata inventory: node master-craft/scripts/inventory.mjs --json.
- Deterministic integrity check: node master-craft/tests/router-smoke.mjs. Passing is NOT proof an agent actually routed user prompts correctly.
