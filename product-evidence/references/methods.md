# Decision records and examples

| Record | Minimum contents |
| --- | --- |
| Decision | User task, baseline, hypothesis, alternatives, owner, decision date |
| Measures | Primary measure, eligible denominator, improvement threshold, guardrails, segments |
| Method | Evidence type, tasks or assignment unit, observation window, sample and known biases |
| Integrity | Event trace or task rubric, exclusions, missingness, imbalance and comparable conditions |
| Result | Baseline and candidate values, counts, uncertainty, failures and next decision |

## Choosing evidence

- **Expert walkthrough:** Record exact steps and observed behavior. Label it as expert observation.
- **Usability benchmark:** Use neutral, realistic tasks with observable success. Keep prompts stable across versions. Track completion, error, and time where meaningful. Small samples are better suited to identifying friction than estimating small changes.
- **Controlled experiment:** Specify exposure and stable assignment, minimum useful effect, sample and duration before launch. Use an appropriate sequential method if stopping early. Check interference, instrumentation and sample ratio before interpreting results. Review guardrails and show inconclusive results where appropriate.
- **Staged release:** Identify comparable baseline, exposed cohort, health windows, rollback owner and stop conditions. Use it to assess operational risk. Establish causal uplift only if the design supports that inference.

## Examples

- **RouteLab mobile map.** Give users a realistic route and ask them to find traffic conditions without naming the legend. Track successful interpretation and time, alongside accidental map taps. An expert check can establish visible map space and keyboard behavior before participants are available.
- **StigmaClear search.** Compare pinned baseline and candidate using a sealed set. Separate mixed-language and hard-query slices, show top-k relevance and no-result rates, and guard latency and harmful false matches. Report annotation rules and disagreement. Treat benchmark gains separately from production behavior.
- **Pitch Night checkout.** Compare verified registration completion per eligible started checkout. Check that payment callbacks and client events reconcile. If traffic is low, pair task tests with descriptive counts and keep conversion uplift unclaimed.

## Sources

- [GOV.UK usability benchmarking](https://www.gov.uk/service-manual/measuring-success/usability-benchmarking-a-website-or-whole-service) informs realistic tasks and comparable success criteria.
- [Microsoft Research on trustworthy experimentation](https://www.microsoft.com/en-us/research/articles/patterns-of-trustworthy-experimentation-during-experiment-stage/) informs guardrails, telemetry quality, and assignment checks.
- [Google SRE on canarying releases](https://sre.google/workbook/canarying-releases/) informs staged exposure and operational stop conditions.
