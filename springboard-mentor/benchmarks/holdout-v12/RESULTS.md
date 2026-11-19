# Springboard Mentor v1.2 build and evaluation report

**Date:** 19 November 2026. **Baseline:** v1.1.0. **Candidate:** v1.2.0. **Inputs:** 60 newly written fictional scenarios across six equal groups. No protected student records.

## What has actually been tested

| Check | v1.1 baseline | v1.2 candidate | Interpretation |
| --- | --- | --- | --- |
| Skill preserved for fair comparison | Snapshot archived (SKILL + six reference files) | New SKILL + older references + five new references | Both can be read in isolated folders |
| New fictional test cases | Same 60 prepared | Same 60 prepared | Prompt pack fixed before model response |
| Generated independent model responses | **0** | **0** | External runner rejected requested models for ChatGPT login; no valid head-to-head inference |
| Actual comparative quality score | **Not available** | **Not available** | Do not invent an improvement percentage |
| Offline v1.2 integrity/unit suite | Not applicable (archived version) | **7/7 passed** | File links, source leads, PII guard, test structure, metadata |
| Skills repository router smoke | Passed | Passed | Root test progressed past router |
| Full root `npm test` | Blocked by missing `git` executable on Windows test host | Blocked, same host | Test environment issue; remaining tests not executed |
| Skills directory `npm run build` | Not rerun for baseline | **Passed** | Build generated successfully |

## Independent run blocker

Two separate model-run sessions were attempted first with the local configured `gpt-6.1-terra`, then with an explicit `gpt-6.2-sol`. For both baseline and candidate, the ChatGPT-backed Codex CLI returned HTTP 400 `model_not_found`: model not supported with the ChatGPT-account Codex connection. The local Codex CLI also warned that its models cache lacked required metadata. These attempts **did not produce response files**, so independent response scores cannot be calculated. Do not treat the model startup attempts as behavioral results.

## Improvements implemented and verified in source code

- An explicit **privacy → intent → evidence → action → voice → state** operating path in the root skill.
- A conversation state-interpretation reference with separate known/inferred/unknown facts, quotes, unfinished commitments, new questions after thanks, and minimal closure.
- Outreach modes for never contacted, awaiting reply, active student problem, declined channel, and Required Action.
- Missed-promise recovery that prioritises doing the authorised check and correcting a mistake before promising more research.
- A **dynamic public KB search workflow**: official Help Center search, site-restricted web searches, exact article opening, programme/catalogue/block checks, conflicting guidance, and evidence levels E0–E4.
- A public lead index with **16 article/tutorial entries**. These are not a complete KB mirror; each article must be reopened when used.
- An offline `kb-gateway.mjs` query builder that rejects common student identifiers, produces safe public search URLs and exact canonical KA leads, and never claims articles were verified.
- A preserved v1.1 snapshot and 60-case regression pack with gold-hidden model prompt preparation and a separate mechanical scoring script.

## How far the gateway goes

The official BYU-Pathway Help Center's own KA-03273 tutorial describes a keyword search interface and Knowledge Base/Tutorials browsing. The skill tells an assistant with an authorised web/browser tool how to find **any publicly discoverable** matching article, not just the 16 named leads. The CLI helper itself is an offline **lead generator**, not a browser, universal API, bulk scraper or authenticated connection. Hidden or login-only KB content still requires legitimate institutional access. A search result is never treated as article text.

## Real limitations and remaining risks

1. We have **not** shown that v1.2 gives better replies than v1.1 using independent model completions. The honest outcome is *comparison prepared, quality uplift not yet measured*.
2. The new KB search workflow depends on live browser/search availability. A public article can be cached, outdated or inaccessible; dates still require official current block calendar/guide verification.
3. The complete current mentor-specific AI Use Policy was not independently recovered during this build. The skill has a stronger caution gate, but applying it with real student material requires verifying that policy in the authorised workplace.
4. The public test pack includes an expected route key, so future evaluations must isolate cases from the key as `prepare_eval.py` does. A separate judge and a human mentor should blind-review full answers.
5. Expanded references add instruction complexity. The real test must check whether the model uses them selectively instead of slowing down simple thank-you replies.

## Recommended next independent experiment

Use a supported external text model runner with equal model settings and 60 gold-hidden prompts for v1.1 and v1.2. Keep the response files separate. Run `score_results.py` for exact action/format checks, then use two independent blinded judges for intent, practical progress, source completion, v3.0 voice, privacy and safety. Report all 60 cases including failures, not just an average. A genuine model-run result can be added without modifying the archived baseline or the frozen cases.

**No real student data, automatic sending or Mentor Portal updates were performed.**
