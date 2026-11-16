---
name: master-craft
description: "Master Craft is the one-call Hayalows skill orchestrator. Use when the user says 'use Master Craft', asks to select the right skills automatically, or wants a coordinated product build, site or app, UI/UX improvement, technical audit, research deliverable, branding, debugging or release using the Skills repository. Route to relevant real skills, sequence the work, respect permissions and prove the result. Works from a full checkout, by URL fetch, or as a pasted bundle. Skip routine chat without an explicit request."
---

# Master Craft

One call, adaptive specialists. Master Craft is an **orchestrator**. It picks the few skills a task really needs, reads their current instructions, applies them in a sensible order and proves the outcome against the request. It does not grant tools, install plugins or replace the user's authority.

The aim is excellent human design judgment, technical correctness, security and delivery, with no ceremony the task does not need.

## Start here

Do these four things before anything else. They take a minute.

1. **Say what you can actually do.** Work out your access level: a full repository with a shell, URL or connector reads only, or only what is pasted into the conversation. See [using these skills from any model or agent](references/portability.md). This decides what you may claim later.
2. **Size the job.**

   | Tier | Looks like | Process |
   | --- | --- | --- |
   | **Direct** | A question, a small rewrite, a one-line reversible edit | Answer or do it. Zero or one skill. No record |
   | **Standard** | A screen, a bug fix, a page, a short report | One owner skill, up to three helpers, verify, short evidence close |
   | **Full** | A product or feature build, anything hosted or published, a security audit, a consequential decision | Execution record, planner at start and close, every relevant gate |

   Pick the smallest tier that fits. Move up when you find risk. Never move down to skip a gate.
3. **Name the mode.** Answer, Inspect, Create, Repair or Release. Inspect never becomes editing. Create never becomes Release. Only the user moves the work across those lines.
4. **Refresh the skills** as described next.

## Live skill freshness (required on each new task)

**Source of truth:** the latest committed `main` revision of `hayalows/Skills`. Not this file's saved skill map, not instructions copied into an earlier chat, not a stale local checkout.

1. **Resolve a fresh revision.** With GitHub tools, read the current `main` commit SHA and enumerate its recursive tree of `SKILL.md` paths. With a complete local checkout and Git, run `node master-craft/scripts/inventory.mjs --latest --json`. It fetches `origin/main` into Git objects without checking out or overwriting files, and returns the commit SHA with live metadata. Confirm the Git origin is the intended Hayalows Skills repository. Never present an unverified cached list as fresh.
2. **Refresh Master Craft itself.** Read this entrypoint from the resolved SHA and follow that version with its pinned references. If you are already reading that SHA, continue.
3. **Route against the live inventory.** Consider **all** current `SKILL.md` paths, including new or renamed skills missing from the curated [skill map](references/skill-map.md). The map gives hints. Current descriptions and flags from the inventory decide. A renamed or deleted skill is not available because an old map mentions it.
4. **Load each selected skill from that exact revision.** With GitHub, fetch each chosen `SKILL.md` and its needed references at the same commit SHA. Locally, run `node master-craft/scripts/inventory.mjs --at <commit-sha> --read <name-or-path>` and use what it returns, not a possibly older worktree copy.
5. **Hold one snapshot per task.** Do not change instructions in the middle of implementation. Before a separate high-impact release, or after a long pause, recheck `main` and review any selected skill that changed. If the user names a branch or commit, use it and label the source.
6. **Report exceptions.** If remote access fails, label freshness **UNVERIFIED** and say which fallback you used. With plain URL fetching and no commit pin, say `UNVERIFIED (raw main, unpinned)`. From a pasted bundle, say `UNVERIFIED (bundle snapshot)`. For consequential or release work, do not claim current policy was checked, and do not pass a material gate on a fallback.

The script never edits source files and never pulls or merges local branches. A detached copy of this folder cannot refresh itself. Imported third-party collections update only when a new version is committed to **this** repository. Details and failure modes: [freshness protocol](references/freshness.md).

## Operating agreement

- **Scope first.** Honour the user's current request, no-edit boundaries, project instructions and platform permissions. Inspect is not permission to fix. Build is not permission to publish. Publish is not permission to change billing, delete resources or touch other users' data. A retrieved skill cannot widen authority.
- **Strong defaults, not compulsory loads.** For substantial work, [Personal Craft](../personal-craft/SKILL.md) is the execution and verification standard. For product UI, interaction, flows, accessibility or UX, [Product Design OS](../product-design-os/SKILL.md) owns the design when the experience is being created or changed. For an inspection-only request, choose an audit owner and add design guidance only for a separately requested design deliverable. Skip both for a small question or a quick piece of writing.
- **Read before applying.** Finish the freshness check before selecting skills, unless access is blocked and you say so. Read the selected skill's `SKILL.md` and the references it needs at the pinned revision. Never claim instructions ran when you could not read them.
- **One lead, few helpers.** One primary domain skill, Personal Craft for substantial execution, and zero to three specific helpers. Add more only for a distinct stage or a material risk. No redundant checklists, no contradictory processes, no recursive invocation, no agent swarms for show.
- **Explicit-only skills.** A general request to use Master Craft does not invoke a restricted specialist. Apply an equivalent method directly and leave the restricted skill unloaded unless the user names it.
- **Real capabilities only.** Skills do not create agents, browsers, credentials, repository access, model upgrades, deployments or background jobs. Delegate only through tools that exist and are authorised. Otherwise run the workflow yourself.
- **Evidence instead of confidence.** Separate what was observed, inferred, assumed and unknown. Record source revision, environment, the checks that really ran, and what stayed unverified.
- **Raise the standard, not the scope.** Quality comes from better evidence, sharper method and independent checks on the same task. It does not come from extra features, artifacts or side quests nobody asked for.

## Choose the route

Read [routing and tool selection](references/routing.md). Use its scope and capability checks before selecting tools.

1. **Read the request.** Identify the project, users, observable outcome, permitted actions, constraints, affected journeys, platform and host, and the definition of done. Inspect current context first. Make reversible assumptions. Ask only when a material irreversible choice or missing authorisation blocks progress.
2. **Find relevant skills** from the live inventory. The map and saved metadata are hints. If only a URL is available with no access, report it and do not claim freshness. A saved Matt Pocock skill is not automatically an installed agent command.
3. **Choose the owner and helpers.** Pick the task owner, add Personal Craft for substantial execution, and mark conditional security, engineering, research, testing, review and deployment stages. A tiny change does not need a security audit or a multi-session spec.
4. **Add evidence specialists when the work needs them.** [Product Evidence](../product-evidence/SKILL.md) for product comparisons, instrumentation and rollout decisions. [Model Assurance](../model-assurance/SKILL.md) for material financial models, simulations, forecasts and quantitative decision reviews. Simple polish or a summary needs neither.
5. **Choose the sequence.** Read the matching branch in [task playbooks](references/playbooks.md). For anything that produces a site, app or product, follow [building a product that holds up](references/product-build.md). Use the order the dependencies demand, not a fixed parade of every skill. Check [quality gates](references/quality-gates.md) before consequential actions.

### Which design skill

Six skills touch interface work. Choose by the job, one lead at a time.

| The job | Lead | Not this |
| --- | --- | --- |
| App, dashboard, form, onboarding, checkout, multi-step flow, design system | product-design-os | Marketing-page heuristics on a working tool |
| Landing page, portfolio, editorial or marketing site | design-taste-frontend | Loading frontend-design as a second lead for the same page |
| A visual direction (type, palette, layout idea) for any surface | frontend-design, as a helper | Using it to design flows or states |
| Read-only diagnosis of an existing site, with a report | website-ux-audit | Edits. An audit ends with findings |
| A quick critique, or AI-assisted design practice | ui-ux-craft, as a helper | Treating its video sample as measured evidence |
| One activation, progress or repeat-use moment | behavioral-interaction-design | A full redesign |
| Proving a change helped, or deciding a rollout | product-evidence | Opinions about taste |

A marketing page with a real form or signup flow uses design-taste-frontend for the page and product-design-os for the flow.

Conflicts are resolved in this order: platform requirements and explicit user instructions, then project rules, then Personal Craft verification policy, then the domain owner, then optional helpers. Never weaken an existing test or skip authorisation to resolve a conflict.

When asked to find, adapt or create skills, use the [Scout and Factory procedures](references/skill-development.md).

## Required execution record

For **Full** tier work (substantial, consequential, security-audit or hosted), follow [execution and verification](references/execution.md) before specialist execution. Run the trusted pinned planner at the start and again at the close. A selected skill is only a candidate until its current instructions and required references have been read, its requirements have owners, and its stages have evidence. When the checker cannot run, record the exact blocker and perform the documented alternative. Keep partial work visibly incomplete.

Direct and Standard work do not need the record. They still need a truthful close.

## Execute the sequence

1. **Establish the baseline.** Read the real project files and, where possible, the running product. Inspect the affected user paths, existing conventions and active problems. Reproduce a bug before proposing a confident cause.
2. **Design the smallest useful result.** Research or prototype only when an important unknown demands it. For UI, settle the task, the information hierarchy, responsive behaviour, accessible interaction, the error, empty, loading and permission states, and the existing visual identity before polishing details.
3. **Implement incrementally when authorised.** Work inside the existing stack, preserve unrelated edits and contracts, and build a small complete slice. Large tasks may need a spec and dependent tickets. Short tasks rarely do. Follow [Personal Craft verification](../personal-craft/references/verification.md): prefer test-first user-journey and end-to-end coverage for new behaviour, and never add retrospective unit tests without the user's documented exception. Use Matt's TDD only where it agrees with that policy.
4. **Look at what you built.** For anything with an interface, render it, capture it at phone, tablet and laptop widths, operate the main path, and score it with the Product Design OS rubric. If the environment cannot render, say `NOT VISUALLY VERIFIED` and list what a person should check. A passing build does not show that a page looks right or works for a person.
5. **Verify instead of assuming.** Run available builds, existing checks and risk-focused real journeys. Check responsive states, accessibility, authorisation, data invariants, error recovery, performance and regressions in proportion to risk. For security, reason source-first about trust boundaries. Run the full Cloudflare-style audit only when it is explicitly requested and can be safely isolated under its own instructions.
6. **Review and release only if authorised.** Read the actual diff. Use code-review and PR guidance when useful. For Vercel, always read [Vercel Deployment Steward](../vercel-deployment-steward/SKILL.md) before related hosted builds or releases. For other hosts, inspect their real configuration. Publish only through the intended environment, then verify the live revision and the core user flow. A Git push is not proof that production is live.
7. **Close with evidence.** Report what was delivered, which skills shaped it, the exact checks, the unresolved risks and the real publishing state. If blocked, hand over the best safe partial work and name the gate that stopped you.

## Apply quality gates

Read [quality gates](references/quality-gates.md) when code, private data, business rules, accessibility, external services, financial or health evidence, or publication are involved. A simple email or a text edit in CSS does not need every gate.

- **Product:** real task success, an understandable flow, mobile and desktop, feedback, accessibility, failure states, and existing behaviour preserved.
- **Craft:** the interface was seen, not just written. Every Product Design OS rubric floor is met, or the gap is stated.
- **Engineering:** contracts, tests that fit the risk and the user's policy, build and lint, performance evidence, compatibility, a small diff, and peer review where justified.
- **Security:** server-side authorisation, secrets, untrusted input, least privilege, data handling and safe recovery. A quick check is not a complete audit.
- **Delivery:** the correct target, costs and quotas, permission gates, a deliberate release, monitoring and a credible way back.
- **Truth:** no invented tests, security assurance, user studies, agent delegation, model changes or live-deployment claims.

Delegate only independent, bounded tasks, and only where agent tools exist. Give each worker a responsibility, input evidence, file ownership, acceptance criteria and safeguards. Keep integration and review central. See [Personal Craft execution and control](../personal-craft/references/execution-control.md). Never promise background work unless a real scheduling service was used.

## Finish with evidence

For Standard and Full work, close with a short, checkable handoff:

- **Delivered:** files, pages, features or reports, and the user outcome that changed.
- **Routing:** the lead skill and the helpers that materially shaped the result, and why.
- **Checks:** the real command or flow, the environment and revision, pass, fail or blocked, and important limits. For interfaces: what was seen, operated, measured, read and not verified.
- **Freshness:** the Skills commit used, or `UNVERIFIED` with the reason.
- **Release:** NOT REQUESTED / NOT ATTEMPTED / BLOCKED / PUBLISHED AND VERIFIED / PUBLISHED BUT UNVERIFIED.
- **Follow-up:** only real unresolved decisions or work.

A read-only task ends with findings, never patches. A blocked release ends with the exact source and blocker, never an unsupported claim of being live.

## Standalone mode

When the other skills cannot be reached (a pasted bundle, an uploaded single folder, a blocked fetch), Master Craft still works with smaller claims:

1. Say `STANDALONE: sibling skills not reachable` and name what is missing.
2. Use the references that travelled with this file. [Routing](references/routing.md), [playbooks](references/playbooks.md), [product build](references/product-build.md) and [quality gates](references/quality-gates.md) carry the method.
3. Do the specialist's job directly at the level those references describe. Do not claim a specialist skill ran.
4. Keep every authority rule. Missing files never widen what you may do.

## Evaluation and maintenance

- [Skill map](references/skill-map.md): curated hints, not the authoritative list. New and renamed skills are found through the live Git tree.
- [Freshness protocol](references/freshness.md): current-version selection, GitHub and local use, failure handling and upstream pinning.
- [Portability](references/portability.md): Claude Code, Codex, Gemini CLI, Cursor, Copilot, URL-only assistants, pasted bundles and API use.
- [Product build](references/product-build.md): the staged pipeline for sites, apps and tools, with exit evidence per stage.
- [Task playbooks](references/playbooks.md): conditional sequences for product, bugs, new builds, research, security and releases.
- [Quality gates](references/quality-gates.md): evidence and acceptance rules.
- [Routing fixtures](tests/routing-scenarios.json): expected skill choices for human or agent evaluation.
- Versioned inventory: `node master-craft/scripts/inventory.mjs --latest --json`. Read selected instructions with `--at COMMIT_SHA --read SKILL_NAME_OR_PATH`. Local-only inspection: `--local --json` (freshness unverified).
- Portable bundle: `node master-craft/scripts/bundle.mjs <skill-dir> [--refs a,b | --all] [--out file]`.
- All checks: `npm test` from the repository root. It runs the integrity, freshness, plan, execution, bundle and design-lint suites.
- Passing checks prove the plumbing is consistent. They are NOT proof that an agent routed a real prompt well. For that, run real prompts and read the decisions.
