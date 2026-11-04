# Master Craft: one-call skill orchestrator

Say **Use Master Craft**. It identifies the task, chooses the smallest relevant group from this repository, reads their actual SKILL.md instructions, sequences the work and verifies results. It does not force every skill into every task, replace your authority, or grant inaccessible tools.

## What makes it different

- **Connected library:** a curated map covers all pre-existing top-level Hayalows and Matt Pocock skill definitions, including experimental and tool-specific skills. A local inventory script discovers newly added skills in the checkout.
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

**Option B: Codex or another local coding agent.** Keep a full checkout of the Hayalows/Skills library available to the agent. Install or symlink the master-craft folder into the agent's supported skill-discovery location. In Codex, local skills are typically under ~/.agents/skills/ or the current repo's .agents/skills/. Symlinking to the master folder in the full checkout preserves its relative links to the library. Copying the master folder alone breaks references to the other skills. Check platform documentation before making global setup changes. Refresh the checkout to get new skills.

**Option C: No skill installation.** Give an agent that can read the checkout the path to master-craft/SKILL.md and ask it to apply that file. This is ordinary instruction loading, not an automatically registered plugin.

Not all Matt Pocock experiments work in every runtime. Commands, subagent APIs, Vercel access and safe testing depend on actual available tools and permissions. Master Craft will use a compatible single-agent path if these features are absent.

## Files

- SKILL.md: main entry point and decision framework.
- references/skill-map.md: 57 pre-existing skills, with exact paths and short selection triggers.
- references/playbooks.md: UI, bug, new product, brand, report, security, deployment and agent workflows.
- references/quality-gates.md: observable acceptance and risk conditions.
- scripts/inventory.mjs: dynamic full-checkout metadata listing (Node 20+).
- tests/routing-scenarios.json: 15 realistic manual agent-evaluation cases.
- tests/router-smoke.mjs: static checks that all current skills are mapped and fixtures remain valid.
- references/research-notes.md: research behind routing and platform limitations.

Run from the repository root:

    node master-craft/scripts/inventory.mjs --json
    node master-craft/tests/router-smoke.mjs
    npm run build

The validator checks completeness and structure. **It cannot prove actual LLM routing quality or production behavior.** For a new route, run a real prompt evaluation and inspect decisions before claiming improvement.

## Library updates

When a new top-level skill or Matt Pocock import appears, refresh references/skill-map.md with the correct triggers. The smoke test intentionally fails when a newly discovered skill is not yet represented. Master Craft can still inspect new metadata dynamically even before the index is refreshed, provided the repository is accessible.

## Attribution

The original Matt Pocock collection retains its MIT licence and attribution. Cloudflare's security-audit copy and other sourced skills retain their own notices. Master Craft is an original routing layer, not a claim that the underlying copied skills were authored by Hayalows.
