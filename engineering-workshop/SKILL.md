---
name: engineering-workshop
description: "Plan, build, debug, refactor and verify working software, or teach engineering judgment using a real change. Use for backend features, APIs, data consistency, architecture tradeoffs, integrations, performance regressions and end-to-end delivery."
---

# Engineering Workshop

Turn the request into a behavior someone can observe through a supported entry point. For a small change, inspect the caller, implement the change and exercise it. Scale the process below to the cost of getting it wrong.

## Choose a starting point

- **New build.** Identify the smallest usable outcome. Walk from input through validation and storage to the result the caller receives. Build that path first. Replace stand-ins at the boundary the user expects to work.
- **Bug.** Capture the observed and expected outcomes with the same input. Pick competing explanations and a cheap observation that distinguishes them. Trace where the state first diverges. Use a local fixture for diagnosis when a live write has consequences.
- **Refactor.** Sample current callers, stored records and error behavior. Identify what must survive the change, including supported older inputs. Preserve that behavior through the public interface.
- **Teach or review.** Give one design decision, two credible implementations and a failure that would distinguish them. In a lesson let the learner predict the result before showing the trace. In review, order findings by consequence and ground each in code or observed behavior. Honour read-only requests.

## Find the boundary that owns the rule

Read repository instructions, entry points, callers, existing tests and the last relevant change. Write a short contract in the vocabulary of the product. What must remain true, who owns it, and how would a caller know? Locate the authoritative record and the moment a change becomes durable. Validate untrusted input and enforce access at the boundary that owns the data. Keep private values out of logs and examples.

For a consequential choice compare the least complex viable design with one alternative. Name the assumption that could reverse the choice. Keep logic close to its owner. Add an abstraction when current callers share the same rule and failure behavior. For performance work, measure a representative input first, identify the expensive step, and compare the same workload afterwards.

## Deliver a working slice

Follow the project's existing conventions. Carry one real case through the public interface before widening coverage. Consider only relevant failure modes: stale input, concurrent writers, retried requests, a crash between durable writes, or version skew during rollout. Put each guarantee at a layer able to uphold it. A disabled button cannot guarantee exactly one stored record. Use bounded retries only when repeating the operation is safe.

When changing a schema used by running clients, expand support first, check mixed-version reads and writes, migrate records in restartable batches when needed, then remove obsolete paths after compatibility is proven. For an external side effect, trace what happens if the provider succeeds and the local acknowledgement is lost. Describe reconciliation if the two systems cannot commit atomically.

## Prove the claim

Exercise the supported entry point. For a regression, show that the same check detects the original defect and passes after the change when feasible. Include one nearby behavior that must still work and the failure case most likely to contradict your claim. Reuse existing checks. Add a targeted durable test when the old suite could miss the defect. Record the actual command, expected result and observation. A mocked dependency leaves the real integration unverified.

Review the diff for accidental changes, debug data and unused machinery. For a release request, distinguish a passing local build, a published revision and a successful live operation. Verify the authorized environment and use a safe readback or smoke check. For material data changes, explain what rolling back code can recover and what needs reconciliation. For multi-session work leave a short checkpoint of last verified behavior, open risk and next runnable check.

Read [Failure drills and source notes](references/field-notes.md) for worked examples and practice. Return the outcome, evidence and material unknowns in the user's terms.
