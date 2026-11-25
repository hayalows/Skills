# Executable reference: v1.2

The dependency-free ECMAScript module is [evidence-workflow.mjs](../scripts/evidence-workflow.mjs). It is a small testable evaluation engine, not an LLM service. Node 20+ is the intended local host. The original v1.1 module remains unchanged and is only a historical baseline.

## API

```js
import { runEvidenceWorkflow } from "./scripts/evidence-workflow.mjs";

const result = await runEvidenceWorkflow({
  runId: "example-unique-run",
  input: { values: [12, 8] },
  worker: async (input, fixes) => ({ total: 20 }),
  rubric: [
    { id: "sum", weight: 100, method: "deterministic",
      min: 100, required: true, source: "arithmetic" }
  ],
  verifiers: {
    arithmetic: {
      method: "deterministic",
      independent: true,
      check: ({ candidate, input }) => ({
        score: candidate.total === input.values.reduce((a,b) => a+b,0) ? 100 : 0,
        evidence: [{ ref: "local-sum", detail: "Recalculated from the supplied input." }]
      })
    }
  },
  threshold: 85,
  maxRepairs: 2
});
```

Inputs and candidates are JSON-like data, copied and deeply frozen; criterion definitions and adapter configuration are copied at start. Criterion IDs must be unique, weights positive integers summing to 100, methods deterministic/human/model, and floors numeric. The trusted adapter returns a score and nonempty evidence references with details; deterministic scores are binary. Optional fix text names the needed repair. The runner computes the weighted total and bounds, never trusts the worker or an arbitrary critic total. If a declared criterion cannot be assessed, the total is null, the coverage shows evaluated weight, and the outcome is unverified. A required model criterion cannot rely on an adapter declared same-model. Do not misdeclare independence.

Result: status (completed, failed, unverified, awaiting_approval, cancelled), reason, repairs, best, accepted, approval and trace. Each best or accepted record carries candidate, full review and round. Best is ranked by verified verdict, fewer blockers, coverage, then lower-bound score; it is for inspection, not automatic use. Even a high aggregate fails a mandatory floor. The trace logs each review and best round; it is not a durable audit store. A failed or unverified run has no accepted candidate. Non-perfect observations can have improvement suggestions even on an otherwise passing review; those are not hard blockers unless the locked floor fails.

## Permission boundary

If no action is requested, omit permission. For an action, the host provides permission = {action, payload, authorize}. authorize receives {request}, which includes run ID, round, action, exact payload and current candidate. A trusted host that actually obtained approval can return {status: "approved", request}; mismatch, absent approval or a thrown provider call yields awaiting_approval. Denial cancels. The runner never executes the external action. An echo in the test is a simulated approval, not human consent. A live adapter must authenticate who approved, verify freshness and unique run IDs, bind actual bytes, handle replay and concurrency, enforce permission at execution and use idempotency. This module does none of those side effects.

## Trust and assurance limits

Host adapter code is trusted. The engine checks schema and policy, not the truth of an arbitrary evidence string. A compromised adapter can lie and pass: this was reproduced in the domain benchmark. Keep adapters in reviewed host code, not dynamically supplied by workers. Bind genuine tool receipts, validate sources and candidate versions, and independently recheck consequential observations. Do not expose privileged callbacks to arbitrary model-supplied code. In-process functions are not a security sandbox. The optional critic is advisory and its return is not used for scoring; make a trusted adjudication a mandatory rubric criterion for a real veto. The reference does not execute or authenticate LLM calls, prove independence, enforce provider timeouts, persist state, implement parallelism, verify source URLs or execute side effects. Implement these in the production host and test them before claiming live reliability.

## Reproduce

From repository root:

    node agent-team-architect/tests/reference-workflow.mjs
    node agent-team-architect/tests/evidence-workflow.mjs
    node agent-team-architect/tests/domain-benchmark.mjs

The first is the frozen v1.1 historical test suite. The last two print results and fail nonzero on unmet expectations. The cases use synthetic deterministic fixtures and simulated human/model scores, not live people or provider calls.
