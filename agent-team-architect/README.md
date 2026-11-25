# Agent Team Architect v1.1.0

A portable skill adapted from a user-supplied agent-team architecture prompt. It designs and verifies small agent workflows, with role contracts, explicit handoffs, bounded repair, human approval and improvement from evidence.

## Start

1. Open [SKILL.md](SKILL.md) in a compatible agent or install the folder using the host's skill mechanism.
2. Ask: "Use Agent Team Architect to build a team for [job]. Compare it against a simpler approach and verify what actually runs."
3. Run the dependency-free reference test with Node: `node agent-team-architect/tests/reference-workflow.mjs` from the repository root.

The test uses synthetic merchant records in integer pesewas. It is a deterministic reference, not a deployed AI team. It has no dependencies beyond a modern JavaScript runtime, no live API calls and no external actions. To stop using the skill, remove its invocation or installed copy; no running service needs disabling. The test report documents the ChatGPT tool-runtime results and limitations.

## Files

- [Skill](SKILL.md)
- [Agent contracts](references/agent-contract.md)
- [Evaluation](references/evaluation.md)
- [Platform adapters](references/platform-adapters.md)
- [Test results](references/test-results.md)
- [Reference workflow](scripts/reference-workflow.mjs)
- [Regression tests](tests/reference-workflow.mjs)

## Changes since 1.0.0

Added executable reference workflow, 12 regression assertions and observed run evidence. Clarified hybrid chat/code mode, simple-task baseline, nonactionable failures and the distinction between deterministic verification and independent model review. Condensed the original instructions for the repository format while retaining their workflow. No live integration or LLM benchmark has been completed.
