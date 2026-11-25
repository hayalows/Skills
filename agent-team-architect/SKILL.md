---
name: agent-team-architect
description: Design, build, test and improve AI agent teams, swarms, graph workflows and recurring agent jobs. Use for multi-agent orchestration, delegation, explicit handoffs, quality loops, approval gates, workflow audits and agent benchmarking. Do not use for a simple task that one agent or deterministic code can complete reliably.
---

# Agent Team Architect

Version: 1.1.0

Build the smallest dependable team for a real job. This skill is instructions, not a grant of tools or permissions. A graph or role-play is not proof of a deployed agent team.

## 1. Inspect capabilities and choose a mode

Check the actual runtime, available tools, file access, execution, supported delegation, persistence and permissions. Read [platform adapters](references/platform-adapters.md) before selecting a provider.

- BUILD: create or edit runnable code in an available runtime. Report separately whether independent LLM workers, mock workers, or deterministic functions ran.
- CHAT: if real model delegation is unavailable, use labeled sequential roles such as Lead, Researcher, Builder and Checker. Never call that independent multi-agent review. You may still execute deterministic tools and checks, and report their actual results.

A chat environment with code tools can combine chat simulation and executable checks. Do not invent agents, tool calls, costs, parallelism or logs.

## 2. Intake and selection

For a new team with material unknowns, ask at most five questions together, each with a recommended default and open alternative: what job consumes time, which part to remove first, which tools/data it uses, what a great result looks like, and what actions require approval. Wait only if a material answer is missing; skip answered questions and proceed when the user delegates decisions.

Select one first job by frequency, effort, feasibility, risk and credible monthly time saving. Explain the assumptions and why other jobs can wait. Compare against a single-agent or deterministic baseline before adding complexity. When useful and possible, consult open-source examples and official runtime documentation; record sources and licenses, not invented research.

## 3. Team and graph

Use three to five roles as a starting point, fewer when sufficient, more only for distinct work with measurable benefit. Include Lead and Checker responsibilities. Give each role one primary job, input and output schema, explicit non-goals, allowed tools, a 3–5-item done-well checklist and a handoff recipient. Workers report to the Lead. The Checker should return exact fixes, not silently rewrite the candidate.

Use [agent contracts and graph](references/agent-contract.md). Draw Mermaid and plain arrow versions showing payloads, fan-out and join, dependencies, exact branch rules, timeouts and terminal states. Run independent work concurrently only if the runtime supports it and the tasks justify it. Use deterministic checks where possible. Separate retrieved untrusted content from instructions. Grant least privilege per role.

## 4. Quality and improvement loops

Per run: Lead dispatches, joins and sends the candidate to Checker. Checker scores against a predeclared rubric, cites evidence, names blockers and assigns precise repairs. Route only necessary work back to the responsible worker. At most two repair rounds after the initial check. If fixes are missing or cap exhausted, return the best safe partial result and escalate. No blocker can be overridden by a high score.

Between runs: review approved memory and compact logs at a user-approved cadence. Propose one measured change, compare with baseline on fixed cases, explain risks and rollback, and wait for approval before changing live behavior. Do not schedule without permission. Store decisions and recurring defects, not secrets or unnecessary personal data; if persistence is unavailable use a portable log.

## 5. Build, run and verify

In BUILD mode, inspect actual runtime APIs and project instructions. Prefer existing dependencies and supported graph/state primitives. Build the minimum end-to-end workflow with validated handoffs, bounded repair, timeouts, error states, a trace, and approval bound to the exact external action and payload. Use real inputs where authorized. Run pass, repair, exhaustion, invalid message, tool error and approval tests. A mock validates wiring only; deterministic checks can verify exact facts or arithmetic but cannot establish independent model judgment.

In CHAT mode, label each simulated role. Produce actual task artifacts, pass them to a labeled Checker, show repairs and scores, then finish with Lead and the usable result. Record which checks used real tools. Provide reusable role prompts and a manual review prompt if useful. Never call a same-model review independent.

For an executable control-flow example, run from the repository root:

    node agent-team-architect/tests/reference-workflow.mjs

This reference is deliberately limited: it uses deterministic workers and checker, does not spawn LLMs, has no provider costs or real side effects, and is not a production runtime. See [test report](references/test-results.md).

## 6. Iterate

Use [evaluation](references/evaluation.md). Run the first version on representative tasks, show three concrete improvements where warranted and let the user choose unless delegated. Compare variants on the same tasks and rubric. Report measured quality, latency, cost, manual intervention and sample size; leave missing values unmeasured. Never infer a general AI quality gain from a synthetic fixture.

## 7. Launch and present

When asked to ship, verify destination and authority. Do not install dependencies, publish, push, delete, spend money, send messages or schedule automations without specific authorization. Bind approvals to actual action and payload; if the payload changes materially, require renewed approval. Never commit secrets. Prepare a README, setup instructions, sample input/output, tests, troubleshooting and rollback. Include a seven-day adoption plan for substantial new teams, with day seven for improvement review.

For substantial work deliver: selected use case, team and prompts, graph and loops, actual execution and tests, launch checklist and first action. For small tasks use only relevant stages. State unresolved failures, untested paths and assumptions. Never claim a step ran unless it did.
