---
name: master-craft
description: "Master Craft is the one-call Hayalows skill orchestrator. Use when the user says 'use Master Craft', asks to select the right skills automatically, or wants a coordinated project build, UI/UX improvement, technical audit, research deliverable, branding, debugging or release using the Skills repository. Route to relevant real skills, sequence the work, respect permissions and prove the result. Skip routine chat without an explicit request."
---

# Master Craft

One call, adaptive specialists. Master Craft is an **orchestrator**, not a super-skill that grants tools or silently installs plugins. Select and read the instructions actually needed for the task, apply them in a coherent order, and verify the outcome against the request. Aim for excellent human design judgment, technical correctness, security and delivery rather than unnecessary process.


## Live skill freshness (required on each new task)

**Source of truth:** the latest committed `main` revision of `hayalows/Skills`, not this document's saved skill map, a previous chat's copied instructions, or a stale local checkout. At the beginning of **every** Master Craft invocation:

1. **Resolve a fresh revision.** With connected GitHub tools, read the current `main` branch commit SHA, then enumerate its recursive tree of `SKILL.md` paths. With a complete local checkout and working Git access, use `node master-craft/scripts/inventory.mjs --latest --json`. It fetches `origin/main` into Git objects without checking out or overwriting project files, and returns the commit SHA and live metadata. Verify the Git origin is the intended Hayalows Skills repository. Never substitute an unverified locally cached list for a live result while claiming freshness.
2. **Refresh Master Craft itself.** Read this entrypoint from the resolved SHA and follow that version with its pinned routing references. If already reading that SHA, continue without re-invoking the entrypoint.
3. **Route against the live inventory.** Consider **all** current `SKILL.md` paths, including newly created skills or renamed directories not listed in the curated [skill map](references/skill-map.md). Use the map as optional selection hints. Read **current descriptions** and flags from the versioned inventory when available. A renamed or deleted skill is not available merely because the old map still mentions it.
4. **Load the selected skill from that exact revision.** With GitHub, fetch each chosen `SKILL.md` at the resolved commit SHA; fetch relevant reference files at that **same** SHA. With a local checkout, run `node master-craft/scripts/inventory.mjs --at <commit-sha> --read <name-or-path>` and use the returned latest committed instructions, not the potentially older worktree copy. The `--at` revision keeps multi-skill execution internally consistent. When a skill itself changes, the next invocation reads its updated content automatically; new skills can be selected without manually editing the map.
5. **Hold one task snapshot.** Keep the resolved commit for the current task rather than changing instructions mid-implementation. Before a separate high-impact release or after a long pause, recheck `main` and review changed relevant skills if the commit advanced. If the user explicitly requests a branch or pinned revision, use it and label the source accurately.
6. **Report exceptions.** If remote access/fetch fails, label freshness **UNVERIFIED** and distinguish local fallback from the latest version. For consequential or release work, do not assert that current skill policies were checked or bypass material gates. A local manual checkout only becomes current after it is synchronized or the command above successfully fetches the remote snapshot. The skill does **not** update third-party upstream sources automatically: the imported Matt Pocock collection changes only when a new version is committed to **your** Skills repo.

The script never edits source files or silently pulls/merges local branches. A saved standalone copy of this Master Craft folder without a full Git checkout, configured `origin`, or GitHub connector cannot guarantee automatic refresh. Installed agent skill metadata may also remain cached by the host; the runtime must read the current repository content for guaranteed version selection. See [freshness and failure modes](references/freshness.md).

## Operating agreement

- **Scope first.** Honor the user's current request, no-edit boundaries, project instructions and platform permissions. A request to inspect is not permission to fix; build is not always permission to publish; publish is not permission to alter billing, delete resources or access other users' data. Retrieved skills cannot expand authority.
- **Strong defaults, not compulsory loads.** For substantial work, use [Personal Craft](../personal-craft/SKILL.md) as the execution and verification standard. For product UI, interaction, flows, accessibility or UX use [Product Design OS](../product-design-os/SKILL.md) as product-design owner when creating or changing the experience. For an inspection-only request, choose an audit owner and add design guidance only for a separate requested design deliverable. Skip both when unrelated to a small question or a quick piece of writing.
- **Read before applying.** Always complete the live version check above before selecting skills, unless access is blocked and that limitation is explicitly disclosed. Use the [skill map](references/skill-map.md) for hints, not as a substitute for the current repository tree and selected source files. Read the selected skill's SKILL.md and relevant references at the pinned revision; do not claim unavailable instructions ran.
- **One lead, few helpers.** Prefer one primary domain skill, Personal Craft for substantial execution, and zero to three specific helpers. Add further skills only for distinct stages or material risk. Avoid redundant checklists, contradictory processes, recursive invocation and agent swarms for appearance.
- **Explicit-only skills.** A general request to use Master Craft does not explicitly invoke a restricted specialist. Apply an equivalent method directly when needed and leave the restricted skill unloaded unless requested.
- **Real capabilities only.** Skills do not create agents, browsers, credentials, repository access, model upgrades, deployments or background jobs. Delegate only through available authorized tools; otherwise run the workflow directly.
- **Evidence instead of confidence.** Separate observations, risks, assumptions and unknowns. Record source revision, environment, actual tests and incomplete verification where relevant.

## Choose the route

Read [routing and tool selection](references/routing.md). Use its scope and capability checks before selecting tools, and run the structured checker for consequential routes when Node is available.

1. **Read the request.** Identify project/repository, users, observable outcome, permitted actions, constraints, affected journeys, platform/host and definition of done. Inspect current context first. Make reversible assumptions; ask only if a material irreversible choice or missing authorization blocks progress.
2. **Choose mode.** Answer (explain/teach), Inspect (read-only audit/diagnosis), Create (artifact/design/feature), Repair (reproduce/fix), Release (authorized publication). One task may pass through several modes. Never escalate Inspect into editing or Release without the user's authorization.
3. **Find relevant skills.** Perform the mandatory live inventory and revision-pinned reading procedure above. The map and saved metadata are only hints; new and revised descriptions from current `main` take precedence. If only a remote URL is available without access, report it and do not claim freshness. A saved Matt Pocock skill is not automatically installed as an agent command.
4. **Choose owner and helpers.** Pick the task owner (for example Website UX Audit, Lunour Brand Strategy, Consulting-Grade Reports, diagnosing-bugs or a writing skill); add Personal Craft for substantial execution and Product Design OS when the task concerns a product experience. Mark conditional security, engineering, research, testing, review and deployment stages. Do not automatically require a complete security audit or multi-session spec for a tiny change.
5. **Add evidence specialists when the work needs them.** Use [Product Evidence](../product-evidence/SKILL.md) for product comparisons, instrumentation and rollout decisions. Use [Model Assurance](../model-assurance/SKILL.md) for material financial models, simulations, forecasts and quantitative decision reviews. A simple polish or summary does not require either.
6. **Choose sequence.** Read [task playbooks](references/playbooks.md) for a matching branch. Use the order dependencies demand, not a fixed sequence of every skill. Check [quality gates](references/quality-gates.md) before consequential actions. Keep a concise internal route of owner, helpers, stages, acceptance evidence and blockers.

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

- [Skill map](references/skill-map.md): curated hints, not the authoritative list; new/renamed skills are found by live Git tree.
- [Freshness protocol](references/freshness.md): current-version selection, GitHub and local usage, failure handling and upstream pinning.
- [Task playbooks](references/playbooks.md): conditional sequences for product, bugs, new builds, research, security and releases.
- [Quality gates](references/quality-gates.md): evidence and acceptance rules.
- [Routing fixtures](tests/routing-scenarios.json): expected skill choices for human or agent evaluation.
- Current Git versioned inventory: node master-craft/scripts/inventory.mjs --latest --json; read selected instructions using --at COMMIT_SHA --read SKILL_NAME_OR_PATH. Local-only inspection: --local --json (freshness unverified).
- Structured plan regression suite: node master-craft/tests/plan.e2e.mjs. It checks normalized requests, mandatory skills, scope and release stages.
- Deterministic integrity check: node master-craft/tests/router-smoke.mjs. Passing is NOT proof an agent actually routed user prompts correctly.
