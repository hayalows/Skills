# Using Cloudflare Security Audit in Papa Kojo's projects

Source: [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill), copied from upstream `main` at commit `c1c8a8c1471069fb0e188eeaff69b8e8db6564a8` on 2026-11-04. The original MIT license is at [LICENSE](LICENSE). All upstream files are preserved in this folder.

## 1. How to start

Point your coding agent at a local checkout of the project and tell it to read `security-audit/SKILL.md`. That is the router. It selects relevant companion references. This folder being in GitHub does **not** automatically install it on every device or agent.

Install with the official CLI if desired:

```sh
npx skills add https://github.com/cloudflare/security-audit-skill --skill security-audit
```

Or clone `hayalows/Skills` and make the `security-audit/` folder visible to your agent according to its skill-loading conventions.

## 2. Ask the right question

**Focused security review (guidance mode)**

> Read security-audit/SKILL.md. Review the authentication, input validation, and data access in this route. Identify verified trust-boundary failures, source-grounded matters needing validation, and hardening opportunities separately. Use no live probes.

**Complete audit (full audit mode)**

> Read security-audit/SKILL.md and run its full six-phase audit on this repository in an OS-enforced offline sandbox. Use the standard profile. Track every coverage unit, independently verify every candidate, validate findings and coverage schemas, and place all reports outside the target repository. Do not touch deployed infrastructure. Report any blocked phases explicitly.

**Portfolio case**

> Use security-audit/SKILL.md to audit `hayalows/hayawebsite`, focusing on `cv/`: private analytics, Spotify OAuth, public listening route, and browser scripts. Include `hayalows/fplengine/api/analytics.py` as an external companion trust boundary. Produce a coverage ledger, verified findings, and a separate remediation plan. Do not change code during the audit; apply fixes later on a review branch with tests.

## 3. Read the verdict carefully

- `confirmed`: concrete affected principal/resource, a real security boundary violation, supported source trace, and safely reproduced local result. Severity is permitted.
- `needs_validation`: specific missing deployment fact, unavailable sandbox, or unverified behavior. Do not assign a severity.
- `rejected`: candidate was independently disproved.
- Hardening advice: useful risk reduction, but **not** a vulnerability until evidence establishes a boundary violation.

Never describe one static source review as a complete penetration test.

## 4. Safe execution

The upstream skill prohibits live probing, attacks on production endpoints, and target-controlled test execution unless an OS-enforced sandbox has no external network, an allowlisted environment, read-only target/toolchain, scratch-only writes, and bounded resources. If those controls are missing, do source-only analysis and keep reproduction as `needs_validation`.

The full six-phase workflow is **audit-only**. Apply approved fixes in a separate remediation task or pull request. Verify regression tests and deploy only after review.

## 5. Repeat it

Run the focused review after changes to authentication, data storage, new API routes, third-party integrations, or deployment configuration. Repeat fuller audits before significant releases and revisit prior coverage ledgers; repeated runs can target gaps without guessing that everything was checked.

## Portfolio example (2026-11-04)

A focused source-only review led to [portfolio PR #20](https://github.com/hayalows/hayawebsite/pull/20) proposing analytics dashboard CSP, anti-framing and no-store headers. Configuration was statically inspected. It is **not** a completed six-phase audit and live deployment security was not tested.
