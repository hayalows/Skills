# Master Craft: one-call skill orchestrator

Say **Use Master Craft**. It identifies the task, chooses the smallest relevant group from this repository, reads their actual SKILL.md instructions, sequences the work and verifies results. It does not force every skill into every task, replace your authority, or grant inaccessible tools.

## Automatic updates from your Skills repository

**Master Craft now checks the latest committed `main` version of every selected skill at the start of each new task.** It also scans the current Git tree for newly added skills. The static skill map is a guide, not the source of truth. This applies to Personal Craft, Product Design OS, Vercel Deployment Steward and the imported Matt Pocock skills **as committed in your own repo**. It does not independently update Matt's upstream repository.

In connected ChatGPT sessions, it fetches current branch/tree/file contents from GitHub with a consistent commit SHA. In a local Skills checkout, it uses a safe Git fetch and reads selected files directly from the fetched snapshot without overwriting your working files.

Run from the Skills checkout:

    node master-craft/scripts/inventory.mjs --latest --json
    node master-craft/scripts/inventory.mjs --at COMMIT_SHA --read product-design-os

`--latest` fails explicitly if remote access is blocked. Use `--local --json` only as a labeled potentially stale fallback. Read the full [freshness protocol](references/freshness.md) for setup, limitations, and examples. Installed static copies with no live repository access do not magically refresh.

## Execution records

Substantial tasks run the planner before work and at close. The [execution contract](references/execution.md) covers skill versions, authorized effects, dependencies, tool readiness, and evidence. Exit code 2 marks an incomplete checked record. The [Scout and Factory procedures](references/skill-development.md) cover evaluating and developing skills.

## Two specialists

- [Product Evidence](../product-evidence/SKILL.md) helps decide whether a product change improved a task or is ready to ship, using measurements that match the claim.
- [Model Assurance](../model-assurance/SKILL.md) helps verify the numbers behind forecasts, financial models, stress tests and decisions.

## What makes it different

- **Connected library:** a curated map covers all pre-existing top-level Hayalows and Matt Pocock skill definitions, including experimental and tool-specific skills. A live inventory discovers newly added or updated skills in the current GitHub main branch.
- **Context-aware routing:** Product Design OS is chosen for real product UX; Personal Craft is the substantial-work agreement; debugging, brand strategy, content, research and releases have separate conditional routes.
- **Stage-dependent selection:** research or discovery before design where needed, implementation after agreement, appropriate checks, release only with user authorization and host-specific gates.
- **Risk control:** read-only stays read-only; user test-first E2E policy is preserved; sensitive-data security reviews require supported safe conditions; Vercel preflights respect quotas.
- **Evidence:** reports exact changed files/flows, commands, observed results, blockers and whether production was actually verified.

## Try these prompts

Use Master Craft to refine RouteLab's mobile search and maps UX. Preserve the current brand, data contracts and existing behavior. Select the right skills from my Skills repo and verify changes before publishing; do not deploy unless I ask.

Use Master Craft to investigate this portfolio UI bug and fix it. Reproduce the problem first, choose compatible test-first behavioral checks, preserve unrelated code and report precisely what passed.

Use Master Craft to audit my client's website in read-only mode. Find the most consequential problems and prepare a credible report. Do not change files or publish anything.

Use Master Craft to finish this approved feature and deploy to Vercel. Apply the quota preflight, review the code, publish once and verify the production commit and critical user flow.

Use Master Craft to develop a naming and brand identity proposal for this company. Use real research, and don't invent evidence or imply a trademark check happened if it didn't.

## Runtime availability

**Option A: ChatGPT with GitHub access.** Ask the assistant to read the Master Craft skill from hayalows/Skills, and give it your task. It may fetch selected files using the connected GitHub tools. A public repo URL alone does not guarantee a specific conversation can use GitHub or edit other repositories.

**Option B: Codex or another local coding agent.** Keep a full checkout of the Hayalows/Skills library available to the agent. Install or symlink the master-craft folder into the agent's supported skill-discovery location. In Codex, local skills are typically under ~/.agents/skills/ or the current repo's .agents/skills/. Symlinking to the master folder in the full checkout preserves its relative links to the library. Copying the master folder alone breaks references to the other skills. Check platform documentation before making global setup changes. For current instructions, run the live inventory command above and read selected skills at its pinned SHA. A local checkout is not updated automatically.

**Option C: No skill installation.** Give an agent that can read the checkout the path to master-craft/SKILL.md and ask it to apply that file. This is ordinary instruction loading, not an automatically registered plugin.

Not all Matt Pocock experiments work in every runtime. Commands, subagent APIs, Vercel access and safe testing depend on actual available tools and permissions. Master Craft will use a compatible single-agent path if these features are absent.

## Files

- SKILL.md: main entry point and decision framework.
- references/skill-map.md: curated skill paths and selection triggers.
- references/routing.md: scope, tool selection and planner input contract.
- tests/plan-cases.tsv and tests/plan.e2e.mjs: 55 realistic requests tested at the normalized-plan layer.
- references/playbooks.md: UI, bug, new product, brand, report, security, deployment and agent workflows.
- references/quality-gates.md: observable acceptance and risk conditions.
- scripts/inventory.mjs: local and remote-fresh Git skill discovery, pinned SHA reads (Node 20+ and Git).
- tests/routing-scenarios.json: 15 realistic manual agent-evaluation cases.
- tests/freshness.e2e.mjs: local Git end-to-end regression tests of automatic revision selection, new skills, offline safety and pinned reads.
- references/freshness.md: exact freshness contract and runtime compatibility.
- tests/router-smoke.mjs: static checks that all current skills are mapped and fixtures remain valid.
- references/research-notes.md: research behind routing and platform limitations.

Run from the repository root:

    node master-craft/scripts/inventory.mjs --latest --json
    node master-craft/tests/freshness.e2e.mjs
    node master-craft/tests/router-smoke.mjs
    node master-craft/tests/plan.e2e.mjs
    node master-craft/tests/execution.e2e.mjs
    npm run build

The validator checks completeness and structure. **It cannot prove actual LLM routing quality or production behavior.** For a new route, run a real prompt evaluation and inspect decisions before claiming improvement.

## Library updates

A new or updated skill committed to the Skills repository's main branch is detected by the next live inventory. It can be selected without manually updating references/skill-map.md. Update the curated map later when its human-readable hints need improvement; the live tree and source files govern actual routing.

## Attribution

The original Matt Pocock collection retains its MIT licence and attribution. Cloudflare's security-audit copy and other sourced skills retain their own notices. Master Craft is an original routing layer, not a claim that the underlying copied skills were authored by Hayalows.
