# v1.2 release benchmark

Date: 2026-11-25. Baseline library revision: 2ca7c378f44b562e70112d92fcd12f4c1ce48589. The previous runner and checker functions were reproduced and verified against the pinned source (whitespace-insensitive comparison). The new functions and scenario harnesses were executed in the ChatGPT JavaScript tool runtime, then saved as ECMAScript modules. The Node commands are reproduction instructions; this run did not execute a full Node checkout. No model workers, human evaluations, live credentials, live financial records, or external actions were used.

## Predeclared gate

All targeted scenarios must meet their specified terminal status, mandatory failures must remain blocked, a regression must preserve the best reviewed candidate without accepting it, missing evidence must not receive a numeric overall score, and approvals must match the actual request. Preserve v1.1 source unchanged. Compare same fixture tasks wherever the old interface supports them; report new-only cases separately. Exhaustive six-field fault masks are a finite fixture check, not a real-world holdout.

| Suite | v1.1 | v1.2 |
| --- | ---: | ---: |
| Shared targeted cases (17) | 12/17 | 17/17 |
| Exhaustive fault masks (64) | 64/64 | 64/64 |
| Shared total (81) | 76/81 | 81/81 |
| New-only targeted cases (13) | not applicable | 13/13 |
| Dynamic rubric sizes (7) | not applicable | 7/7 |
| Cross-domain scenarios (12) | not compared | 12/12 |
| All v1.2 expected-outcome cases (113) | not comparable | 113/113 |

The 5 shared v1.1 failures were unsupported checker totals of 100 and 85, a passing total with contradictory correction instructions, unbound approval, and changed approval scope. V1.2 used an independently computed fixed oracle rather than trusting the hostile critic and used exact request comparison for simulated approval. This is an intentional architecture difference, not a blinded model contest. It does not prove an old deployment was unsafe with a correctly implemented verifier, nor prove the new host can authenticate arbitrary claims.

Representative sequences: two staged repairs 67→83→100 vs 60→80→100; unchanged defects 67→67→67 vs 60→60→60; regression 83→0→0 vs 80→0→0 (v1.2 retained 80 for inspection and accepted nothing). New weights produce different totals; score magnitudes are not directly comparable. A 99 with a failed mandatory floor was rejected; 84.999 failed the 85 threshold without rounding; unknown evidence produced a null total and coverage/range. Tested criteria counts 1, 2, 3, 7, 10, 17, 25.

The cross-domain suite checks fixed research provenance, synthetic execution receipts, arithmetic and units, literal writing constraints, simulated supplied editorial ratings and a mandatory reviewer veto. No actual writing preference was evaluated. An additional deliberately compromised trusted adapter falsely accepted a candidate; this is an observed limitation, excluded from the 113 protective expectations. Evidence authenticity requires host controls.

## Raw results and reproduction

- [Shared and new-only results](../benchmarks/evidence-workflow-results.json)
- [Cross-domain results and boundary probe](../benchmarks/domain-results.json)
- [Comparison harness](../tests/evidence-workflow.mjs)
- [Domain harness](../tests/domain-benchmark.mjs)
- [Original v1.1 results](test-results.md) (historical 12/12, not included in the 113 or claimed rerun).

The repository's full npm test/build was not run in this environment: Git clone failed because github.com could not resolve in the local container. The new suite was executed directly in the JS tool runtime. The root npm test command now includes the unchanged old suite and both new suites for normal repository runs. No independent LLM comparison, production timeout, real permission, provider cost, model quality, actual human preference or live catalogue deployment has been established by these tests.
