# Verification policy

## Preserve the user's explicit testing rules

- NEVER write unit tests after implementation code. Do not add retrospective unit tests as a completion ritual.
- Highly prefer E2E as the sole newly authored testing mechanism, through real user or system entry points and observable outcomes.
- If isolation testing is necessary, FIRST write down all identified ways the scoped system could fail, including boundaries and assumptions. THEN author the isolation tests before implementing or fixing that behavior. Do not describe a finite failure list as proof that no other failures exist.
- For already implemented behavior needing a new isolation test, explain the conflict and ask for an explicit exception before authoring it. Continue other authorized work. Do not relabel unit tests as E2E to bypass this rule.
- Run existing tests and required repository gates. Never remove, weaken, or silently skip them to satisfy a preference. If a higher-priority requirement conflicts, surface the conflict and follow the applicable hierarchy.

## Plan scenarios before complex implementation

Define actor, initial state, action, expected observable result, persistence, and cleanup. Include the main journey and material permission, failure, recovery, duplicate-action, and concurrency risks. For bugs, capture the failing behavior before the fix where feasible.

Match the boundary to the product: browser journeys for websites, native UI for apps, command invocations for CLIs, real API-to-persistence flows for services. E2E cannot alone prove every race condition, security property, or numerical invariant. Name remaining uncertainty; propose test-first isolation when necessary under the rule above.

Use controlled disposable data. Never run destructive flows against production without authorization. Disclose mocked dependencies and what remains unverified. Prefer stable user-facing locators, isolated fixtures, observable assertions, and condition-based waits. Do not hide failures with arbitrary sleeps, retries, or weaker assertions.

## Evidence for EVERY E2E run

Leave a repeatable artifact containing:
- Runnable test/script and exact command, prerequisites, fixture setup, cleanup, and rerun instructions.
- Source revision or patch identity; environment and relevant versions; timestamp.
- Actual result for each scenario: pass, fail, skipped, blocked, or not run.
- A saved report and useful trace, screenshots, or logs as supported by the harness.
- Mocked boundaries, environment differences, and residual uncertainty.

Never populate results in advance or mark authored tests as passed. Redact private data, tokens, and credentials. Keep evidence local/private under platform storage rules unless publication is authorized. Do not publish traces merely because application deployment was authorized.

For small content or cosmetic edits, inspect the changed output directly; avoid unnecessary test infrastructure. Existing build/type/static checks support verification but do not prove behavior. If E2E execution is unavailable, deliver the work and explicitly mark behavioral verification incomplete.
