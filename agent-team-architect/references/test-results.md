# ChatGPT test report

Date: 2026-11-25. Version 1.1.0. Executed the reference functions in a JavaScript tool runtime. Synthetic merchant reconciliation fixture (integer pesewas), no live financial data, no external writes, no independent LLM workers. All 12 assertions passed. The intentionally faulty baseline missed order B and misstated payments by GHS 5; the independent deterministic checker detected both fields and the targeted repair passed. This demonstrates control-flow behavior, not a statistically valid AI quality improvement. Provider cost, independent-agent performance, parallel execution and live integration remain unmeasured. The reference runner checks approval status only; it does not execute external actions, bind approval payloads, enforce timeouts or implement real delegation. Those are required in a production adapter.

```json
{
  "results": [
    {
      "name": "clean pass",
      "pass": true,
      "status": "completed",
      "repairs": 0,
      "checks": 1
    },
    {
      "name": "targeted repair",
      "pass": true,
      "status": "completed",
      "repairs": 1,
      "checks": 2
    },
    {
      "name": "exhausted repair",
      "pass": true,
      "status": "failed",
      "repairs": 2,
      "checks": 3
    },
    {
      "name": "denied approval",
      "pass": true,
      "status": "cancelled",
      "repairs": 0,
      "checks": 1
    },
    {
      "name": "pending approval",
      "pass": true,
      "status": "awaiting_approval",
      "repairs": 0,
      "checks": 1
    },
    {
      "name": "invalid worker output",
      "pass": true,
      "status": "failed",
      "repairs": 0,
      "checks": 0
    },
    {
      "name": "worker error",
      "pass": true,
      "status": "failed",
      "repairs": 0,
      "checks": 0
    },
    {
      "name": "malformed review",
      "pass": true,
      "status": "failed",
      "repairs": 0,
      "checks": 0
    },
    {
      "name": "blocker overrides score",
      "pass": true,
      "status": "failed",
      "repairs": 2,
      "checks": 3
    },
    {
      "name": "nonactionable review",
      "pass": true,
      "status": "failed",
      "repairs": 0,
      "checks": 1
    },
    {
      "name": "duplicate source row rejected",
      "pass": true
    },
    {
      "name": "exact independent fixture totals and classifications",
      "pass": true
    }
  ],
  "baseline": {
    "score": 67,
    "blockers": [
      "Correct missing",
      "Correct paymentTotal"
    ],
    "fixes": [
      "Correct missing",
      "Correct paymentTotal"
    ]
  },
  "repaired": {
    "status": "completed",
    "repairs": 1,
    "candidate": {
      "matched": [
        "A"
      ],
      "missing": [
        "B"
      ],
      "mismatched": [
        "C"
      ],
      "unallocated": [
        "D"
      ],
      "orderTotal": 25500,
      "paymentTotal": 18500
    },
    "review": {
      "score": 100,
      "blockers": [],
      "fixes": []
    },
    "trace": [
      {
        "role": "lead",
        "repair": 0
      },
      {
        "role": "worker",
        "repair": 0
      },
      {
        "role": "checker",
        "repair": 0,
        "score": 67,
        "blockers": 2
      },
      {
        "role": "lead",
        "repair": 1
      },
      {
        "role": "worker",
        "repair": 1
      },
      {
        "role": "checker",
        "repair": 1,
        "score": 100,
        "blockers": 0
      },
      {
        "role": "approval",
        "status": "not_required"
      }
    ]
  },
  "output": {
    "matched": [
      "A"
    ],
    "missing": [
      "B"
    ],
    "mismatched": [
      "C"
    ],
    "unallocated": [
      "D"
    ],
    "orderTotal": 25500,
    "paymentTotal": 18500
  }
}
```
