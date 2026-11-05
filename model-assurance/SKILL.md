---
name: model-assurance
description: "Build, challenge, or validate decision models, financial spreadsheets, forecasts, simulations, and quantitative comparisons when formulas, assumptions, uncertainty, or backtests could change a decision. Use for scenario design, independent recalculation, break-even thresholds, and model review. Skip simple arithmetic and reports that only summarize existing findings."
---
# Model Assurance

Make the decision, inputs, calculation, and uncertainty traceable. Start with the simplest model that can answer the question. Apply more scrutiny when error would change a costly or hard-to-reverse decision.

1. **Define the decision.** Record the owner, intended use, alternatives including the current baseline, decision date, horizon, and the outcome that would change the choice. Set materiality or tolerance before inspecting results. Honor an audit-only scope.
2. **Lock the inputs.** For material inputs record value, unit, currency, effective date, source, availability at the decision date, and whether observed, estimated, or assumed. Separate cash-flow timing from quote timing. Flag missing or incomparable inputs and choose defensible ranges instead of filling gaps with invented precision.
3. **Build a reproducible baseline.** Separate inputs, calculations, and results. Write the governing equations or cash-flow rules in plain language. Check sign, timing, fees, taxes where supported, compounding, nominal versus real terms, and currencies where relevant. Compare like for like. Save the calculation or formula path with enough detail for another person to reproduce it.
4. **Challenge the result.** Independently recompute at least one material result by a different method. Test identities, boundary cases, plausible joint scenarios and the input that flips the decision. For predictive work, choose a time-appropriate holdout and naive benchmark, then inspect error by relevant segment. Guard against leakage, survivorship, revised data and look-ahead. If observations are insufficient, label the result as a scenario or hypothesis.
5. **Report the decision conditions.** State the baseline, plausible range, key sensitivities, flip point, and where the model should not be used. Show what evidence would change the result. Ask for independent challenge where warranted and permitted. Label self-review as such. Assign an input refresh or monitoring trigger if the model will be reused.

Read [Checks and worked examples](references/checks.md) for material decisions, forecasts, or investment comparisons. Use domain guidance and current primary sources where applicable. Use spreadsheet tooling to deliver editable formulas when requested, and report tooling to present the finished analysis.
