# Evaluation and improvement

Declare acceptance criteria before running. Default rubric: correctness 30%, completeness 25%, evidence 20%, practical usefulness 15%, reliability and safety 10%. Score each dimension 0–100; multiply by weight and sum. Default pass is 85/100 and zero blockers. A fabricated source, missing mandatory requirement, leaked secret, unauthorized side effect or false execution claim always blocks.

Checker returns evidence, criterion scores, verdict, blocker list and actionable fixes with responsible roles. If no actionable fix exists, stop and escalate. Do not silently repair reviewed work.

Compare versions and a simple baseline using identical inputs and criteria. Record sample size, pass rate, quality score, duration, actual provider cost, human corrections and blocking failures. Missing measurements remain unknown. A deliberately corrupted fixture is a fault-injection check, not a fair benchmark of an unassisted model.

Run log: run ID, date, version, category, status, checks, repairs, elapsed time, cost if measured, approval outcome and failure summary. Redact private inputs.

Weekly review: inspect logs and approved memory; find a repeated failure; propose one change with measurable success criteria; test against a fixed regression set; show risks and rollback; obtain approval before modifying a live workflow.
