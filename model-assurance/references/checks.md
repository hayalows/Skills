# Checks and worked examples

## Review record

| Item | What to record |
| --- | --- |
| Decision | Owner, as-of date, alternatives, threshold and approved use |
| Inputs | Source link or record, as-of date, value, unit, status, plausible range |
| Calculation | Version, formula location, timing convention, benchmark and reproduction steps |
| Challenge | Check, expected result or tolerance, observed result, pass/fail/blocked |
| Limit | Assumption or missing evidence, effect on the decision, review trigger |

Start with a zero-input or known-answer case where meaningful. Use a second derivation or a small hand-worked fixture to check a material number. Compare forecast quality with a simple baseline on data unavailable during fitting. Distinguish arithmetic verification, suitability for the intended use, and independently reviewed evidence.

## Examples

- **Fund versus Treasury bill.** Align currency and horizon. Map all contributions and payouts to dates. Convert a quoted discount yield only after checking the actual quote convention. Model fees, exit timing, reinvestment, FX and liquidity as applicable. Compare net cash flows and find the fund return or fee where the ranking flips. Label any assumed rollover rates. A scenario is conditional on its assumptions.
- **Event unit economics.** Separate per-ticket costs from fixed costs. Recalculate break-even attendance independently. Test capacity limits, cancellations and combinations of low sales and higher variable costs. If feasible attendance falls below break-even, surface that directly.
- **Demand forecast.** Use chronological training and holdout periods. Check when each feature would actually have been known. Compare error with a seasonal naive forecast and inspect underprediction during peaks. If sample size or historical coverage is poor, give a range and a monitoring plan.

## Sources

- [UK government AQuA Book resources](https://www.gov.uk/government/collections/aqua-book-resources) and [verification and validation guidance](https://www.gov.uk/government/publications/verification-and-validation-for-the-aqua-book) inform proportional assurance, uncertainty and reproducibility.
- [Federal Reserve SR 26-2](https://www.federalreserve.gov/supervisionreg/srletters/SR2602.htm) informs effective challenge, limitations and performance monitoring. Use these as methods. Assess any applicable regulatory requirements separately.
