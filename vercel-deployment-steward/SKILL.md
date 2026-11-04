---
name: vercel-deployment-steward
description: "Use before building, previewing, pushing, releasing, redeploying, or troubleshooting a Vercel-hosted project. Audit team-wide Hobby deployment headroom, Git-triggered fan-out, failed previews, duplicate projects, and readiness; recommend and verify a low-waste release workflow. Also use on Vercel 402 or requests to avoid upgrades."
---

# Vercel Deployment Steward

A release and development operating procedure for preserving Vercel Hobby allowance. The default action is a **read-only preflight**, not a deployment. Scope all projects in the selected team or account, rather than just the project being edited.

## Enter on these triggers

- The user wants a Vercel site built, pushed, previewed, published, promoted, redeployed, or debugged.
- A deployment quota, 402 error, failed build, excessive previews, storage warning, or duplicated deployment is suspected.
- The user wants to improve Git-to-Vercel workflow, release reliability, or free-tier efficiency.
- An agent or CI runner is about to create a deployment.

Skip ordinary informational conversations that do not involve the user's projects.

## Working agreement

Use [Personal Craft](../personal-craft/SKILL.md) for execution and evidence, especially its [verification](../personal-craft/references/verification.md) policy. Apply Matt Pocock's [writing-for-agents](../collections/matt-pocock-skills/skills/productivity/writing-for-agents/SKILL.md) structure: ordered steps here, conditional details behind references. Use [diagnosing-bugs](../collections/matt-pocock-skills/skills/engineering/diagnosing-bugs/SKILL.md) for actual failures, the [PR](../collections/matt-pocock-skills/skills/engineering/pr/SKILL.md) evidence/merge-risk shape when useful, and [to-spec](../collections/matt-pocock-skills/skills/engineering/to-spec/SKILL.md) for large release plans. Add Product Design OS only for an interface or dashboard, not for every deployment.

## Main procedure

1. **Identify the target.** Confirm the exact Vercel team, project, Git repo, production branch, intended environment, current production commit, and whether the user requested publication or only implementation. Inspect other Vercel projects linked to the same repository.
2. **Audit the whole team.** Use connected Vercel tools when available. List all deployment records from the rolling last 24 hours, paginating to the cutoff. Include successes, errors, cancellations and unfinished records. Classify a null target as unlabeled, **not proven preview**. If records are incomplete, say UNKNOWN. Use [operations](references/operations.md).
3. **Explain the drivers.** Group by project, branch, repo, SHA and state. Detect excessive non-production deployments, duplicated Git-SHA across projects, repeated failed or canceled builds, and needless manual redeployments. Separately check deployment storage and build usage when available. Do not infer storage from deployment count.
4. **Make a gate decision.** Apply the [planning thresholds](references/operations.md). A Vercel 402 deployment-limit error overrides estimated headroom and stops retries. Skipped builds using Ignored Build Step may still count. Never assert that an estimated remaining count is the actual Vercel quota counter.
5. **Do the work without creating deployments.** Build, lint, test and inspect locally first. Batch related fixes into one reviewable change. Do not push each exploratory change to a Vercel-watched branch. Propose explicit Git branch deployment controls only after checking what else they affect. The skill never silently modifies configuration.
6. **Release once and verify.** If the user authorized publication and headroom permits, use one deliberate release path. If Git pushes to main already trigger deployment, inspect the auto-created deployment before considering any manual deploy. Verify production commit, READY state, correct domain and actual user flow. Distinguish Git commit success from live status.
7. **Report evidence.** Show the usage tier, relevant count and timestamp, project contributors, recommended smallest safe fix, actual work done, tests, deployment status and residual uncertainty.

## Conservative planning thresholds

For a 100-deployment Hobby planning cap in the past rolling 24 hours:

| Tier | Estimated records | Behaviour |
| --- | ---: | --- |
| GREEN | 0–54 | Normal work, still batch changes |
| WATCH | 55–69 | Examine preview branches and fan-out |
| PROTECT | 70–84 | Reserve capacity, prefer local testing |
| FREEZE | 85+ | Stop discretionary hosted builds |
| UNKNOWN | Missing or inconsistent evidence | Do not claim a safe deployment |

These are **our safety margins**, not official Vercel limits beyond the 100/day Hobby cap. The Vercel platform may use a counter not fully represented by the visible deployment list. Never invent a precise reset time.

## Tool routing

- **Connected ChatGPT:** use the Vercel project/deployment tools and GitHub history. Prefer connected tools over asking the user for tokens.
- **Local/CI audit:** Node 20+ CLI in [audit-deployments.mjs](scripts/audit-deployments.mjs). With token held only in an environment variable, run the command below from this skill folder:
  
  ```sh
  node scripts/audit-deployments.mjs --team "$VERCEL_TEAM_ID" --gate
  ```

- **Offline investigation:** provide a complete, dated, redacted snapshot and use --snapshot and --now. Incomplete snapshots are UNKNOWN.
- **CLI acceptance:** run the [disposable end-to-end harness](tests/cli-smoke.mjs) with Node 20+: node tests/cli-smoke.mjs.

## Safety boundaries

- Read-only by default. No automatic modification of project settings, billing, deployment retention, production domains, Git rules, project deletion, or access tokens.
- A request to edit code does not authorize a release. A request to release one project does not authorize global branch-control changes.
- Never commit or print credentials. No repeated deploy attempts after quota errors. Do not evade limits by creating new accounts or projects.
- Do not weaken protections or hide failures merely to save deployments. Preserve unrelated projects and branches.
- No claims of live status without checking actual production. No claims of tests passing without running them.

## Load on demand

- [Operations and decision rules](references/operations.md) for release gates, project discovery, duplicate builds, Git branch rules, and failure handling.
- [Platform facts and primary sources](references/platform-facts.md) for quotas and the correct types of skipped deployment.
- [Real account incident](references/pitchnight-incident.md) for an evidence-backed example.
- [CLI usage](references/cli-usage.md) for token-free connected operation, offline snapshots, read-only REST audit and exit codes.

## Standard report

**Budget:** tier; counted records / planning cap; estimated headroom; window; scope; source; confidence.

**Drivers:** top projects, feature branches, errors/cancellations, cross-project duplicate commits.

**Next action:** smallest evidenced remedy, its risk, and required authorization.

**Release proof:** target repo/branch/SHA, checks, production SHA/state/domain, or exact blocker.
