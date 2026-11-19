# Engineering Workshop field notes

## Worked drill: a repeated signup

A form times out after the server commits. A second click reaches a different worker. First define the invariant: one subscription per list and normalized address, if that is the product contract. An application-level lookup followed by insert can race. Enforce uniqueness at storage, handle the conflict deliberately and give the caller a stable response that respects the product's privacy rules. Preserve separate lists. Before adding the constraint to existing data, inspect normalization collisions and agree on a merge policy if it would discard records.

A welcome email has its own failure boundary. An atomic subscription and outbox write can preserve send intent. A worker can still crash after sending and before acknowledging. Use provider-supported deduplication when available or design for reconciliation. Claim only the guarantee demonstrated.

Practise: draw the timeline for two simultaneous calls, then for a timeout after commit. Which test would pass for a sequential retry but fail under concurrency? Use a barrier to make competing requests overlap and inspect the durable count. Test an independent list as a control.

## Transfer drill: a dashboard loses a day

A report drops events near midnight. Candidate causes include ingestion loss, timezone bucketing, a filter boundary or stale aggregation. Pick one known event on each side of the boundary. Trace the same IDs through storage, aggregation and presentation using the intended reporting timezone. Compare totals under the same filter and time interval. If rows exist in storage, rerunning ingestion can introduce duplicates and obscures the first divergence.

For a lesson, give the learner the two timestamps and counts first. Ask which observation would distinguish missing input from a grouping error. In a build, run that observation before choosing a fix.

## Source notes

- [Personal Craft](https://github.com/hayalows/Skills/tree/main/personal-craft) informed the scope and evidence rules.
- [Anthropic's application harness study](https://www.anthropic.com/engineering/harness-design-long-running-apps) informed working in verifiable increments and reviewing the actual output. A single developer can use the same review loop.
- [AWS Builders' Library on idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/) informs explicit intent, repeat handling and late requests. Domain uniqueness and per-request identity answer different questions.
- [Claude Opus](https://www.anthropic.com/claude/opus) and [Claude Fable](https://www.anthropic.com/claude/fable) describe model capabilities. Model benchmark results do not establish which private instructions were used or predict the effect of this workshop.
