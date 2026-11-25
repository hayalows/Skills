# Agent Team Architect v1.2.0: Evidence-First Evaluation

A portable skill adapted from a user-supplied agent architecture prompt. It builds the smallest dependable team and evaluates outputs against a frozen rubric with explicit evidence, weighted scores, unknowns, mandatory floors, bounded repairs and approval scope.

## Start

1. Open [SKILL.md](SKILL.md) in a compatible agent, or install the folder using the host's skill mechanism.
2. Ask: "Use Agent Team Architect to design or audit this workflow. Freeze the evaluation before seeing outputs, verify each claim, report missing evidence, and compare with the simplest baseline."
3. To reproduce the reference checks from repository root, run the three commands in [runtime documentation](references/evidence-runtime.md). Node 20+ is intended. No external calls, credentials or packages are needed.

## What changed

- The new engine computes scores from criterion-level observations and declared weights; checker totals are never authoritative.
- Unknown evidence withholds the score; mandatory floors and verdicts cannot be overridden by averages.
- The task, candidate and rubric are copied and frozen; best reviewed candidate is retained if repair regresses.
- Approval is tied to the exact in-memory request. No action is executed.
- The old v1.1 source remains unchanged for reproducibility.
- 113 deterministic/simulated expected-outcome scenarios passed in the JavaScript tool runtime. Shared cases: v1.1 76/81, v1.2 81/81. A compromised trusted host verifier can still lie. No independent LLM performance or human preference improvement was measured.

## Read more

- [Agent contracts](references/agent-contract.md)
- [Evaluation policy](references/evaluation.md)
- [Runtime API and trust boundaries](references/evidence-runtime.md)
- [Platform adapters](references/platform-adapters.md)
- [v1.2 benchmark and raw results](references/benchmark-v1.2.md)
- [Historical v1.1 test results](references/test-results.md)

This is a reference engine, not a production orchestration service. Provider calls, real authentication, timeouts, parallelism, persistence and external actions need a host adapter. Rollback: invoke the previous pinned skill at commit 2ca7c378f44b562e70112d92fcd12f4c1ce48589 or use the unchanged historical reference module for comparison, rather than changing live state without review.
