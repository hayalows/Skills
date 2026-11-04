# Master Craft: proportionate quality and safety gates

Apply only the gates relevant to the requested task. This reference is guidance, not additional permission to modify projects, spend money, access personal data, test live sites or publish work.

## Evidence language

- Observed: exact source revision or actual flow was inspected in a named environment.
- Reproduced: stated input/action shows actual failure or success repeatedly.
- Inferred: plausible consequence, not verified behavior.
- Unknown/blocked: missing access, inputs, tools or verification.
- Published and verified: exact source is deployed at the correct destination and a real health/user check was completed. A PR merge or Git push is insufficient.

For substantial changes record repository, branch/commit, actual command and environment, source of truth, result, and residual uncertainty. Scrub tokens, customer details and private traces.

## Product and design

- Can the intended user recognize the primary action and complete the task without avoidable work?
- Preserve approved brand, mental models, primary flows and essential accessibility.
- Check affected small and large screens, touch/keyboard use, visible focus, readable typography and zoom.
- Check state transitions including loading, slow connection, validation, empty, error, retry, permission denied and success where relevant.
- Prefer clear affordances and restrained motion over decorations and clutter.
- Measure performance before optimization, and separate lab results from field measurements.
- Check that user feedback and content claims are truthful. Avoid dark patterns.

## Engineering and verification

- Inspect real source and project guidance before writing.
- Identify representative success and failure cases BEFORE modifying behavior.
- Honor personal-craft/references/verification.md: prefer test-first E2E for new behavior; no retrospective unit tests without explicit exception. Never remove existing safety checks or mislabel isolated mocks as production E2E.
- For bugs, reproduce red before code when feasible, then show green in the same relevant test.
- Keep changed contracts compatible: URLs, persistence, analytics, access and user journeys.
- Run existing relevant lint, type, build, tests and user-entry flows. A static pass does not prove actual browser behavior.
- Avoid unrelated edits, unnecessary dependencies and duplicate logic.
- Use independent review where the expected risk justifies it; never fabricate reviewer findings.

## Security and privacy

- Who can read, create, update, remove and export protected records? Check trusted server-side enforcement and cross-user boundaries.
- Keep secrets out of Git, logs, screenshots, analytics, client bundles and prompt text.
- Examine input validation, injection, command execution, dependencies, permissions, CORS/CSP and data retention where relevant.
- Respect API quota, rate limits, least privilege and recovery behavior.
- Do not run destructive production tests, unauthorized scans or live pen tests. Full security-audit workflow needs the mandatory sandbox controls.
- A security checklist or source inspection does not amount to independent certification or a guarantee.

## Evidence-based research and artifacts

- Source material and market claims must be accurate and dated; distinguish direct facts from hypothetical examples.
- Explain methodology, units, scenarios, assumptions, meaningful tradeoffs and calculation limitations.
- No fabricated findings, client quotes, performance numbers, customer interviews or financial returns.
- Render and inspect PDF, deck, document, spreadsheet or visuals as appropriate; verify layout, charts and citations.
- Preserve third-party licences and attribution when repackaging skills or copied material.

## Hosting and release

- Confirm destination, environment, account permissions, cost exposure and release authorization.
- For Vercel, use vercel-deployment-steward and its quota/402 preflight before hosted work. Avoid wasteful repeat builds and duplicate Git-triggered deployments.
- For other platforms, inspect their native workflow. Do not import Vercel limits into Cloudflare or Netlify.
- Confirm code checks, dependency effects, deployment triggers, actual release version, health status and ability to recover.
- After publishing, verify real domain and key flow. If live inspection is not available, mark it unverified.
- Status vocabulary: NOT REQUESTED, NOT ATTEMPTED, BLOCKED, PUBLISHED AND VERIFIED, PUBLISHED BUT UNVERIFIED.

## Stop rule

Skip an irrelevant gate rather than perform unnecessary ceremony. If a material gate cannot be checked, explicitly say what remains unverified. Do not promise perfect design, complete security or zero regressions.
