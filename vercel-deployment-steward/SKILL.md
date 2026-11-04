---
name: vercel-deployment-steward
description: "Use before releasing, pushing, previewing, or debugging Vercel projects. Audit account-wide deployment history, duplicate builds, and Hobby usage; distinguish advisory planning thresholds from actual platform acceptance, check Git-vs-API results, and verify production without wasteful retries."
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
4. **Separate planning risk from technical availability.** Apply the [planning thresholds](references/operations.md) as an **advisory policy for unattended and discretionary releases**, not a claim that the platform will reject a new deployment. Cross-check recent creation outcomes by method (manual API, Git integration, CLI), exact time, project and team. A 402 stops repeat attempts through the failing method; it does **not** prove a Git-triggered release is blocked or exempt. If technically available status is not confirmed, report **UNVERIFIED**. Skipped builds using Ignored Build Step may still count.
5. **Do the work without creating deployments.** Build, lint, test and inspect locally first. Batch related fixes into one reviewable change. Do not push each exploratory change to a Vercel-watched branch. Propose explicit Git branch deployment controls only after checking what else they affect. The skill never silently modifies configuration.
6. **Release once and verify.** If the user has explicitly requested publication, do not automatically refuse solely because the planning tier is FREEZE. When the release is important, evaluate current method-specific evidence, prepare a single reviewed production push through the project's normal Git integration if appropriate, and clearly disclose the quota risk. Do not repeatedly retry a method that returned 402 or create a second deployment for the same commit. Check the resulting production SHA, READY state, domain alias and live user flow. An unaccepted attempt must be reported as blocked, not successful.
7. **Report evidence.** Show the usage tier, relevant count and timestamp, project contributors, recommended smallest safe fix, actual work done, tests, deployment status and residual uncertainty.

## Conservative planning thresholds

For a 100-deployment Hobby planning cap in the past rolling 24 hours:

| Tier | Estimated records | Behaviour |
| --- | ---: | --- |
| GREEN | 0–54 | Normal work, still batch changes |
| WATCH | 55–69 | Examine preview branches and fan-out |
| PROTECT | 70–84 | Reserve capacity, prefer local testing |
| FREEZE | 85+ | Pause unattended/discretionary builds; a specifically authorized, one-shot production release may still be attempted after risk review |
| UNKNOWN | Missing or inconsistent evidence | Do not claim a safe deployment |

These tiers are **internal planning advice**, not technical availability statuses or hard claims about accepted deployments. A Vercel deployment list can include records that don't correspond one-to-one with internal quota accounting. Never promise an "earliest technically possible minute" from a rolling-window calculation. Show the next **visible record expiry** only as a forecast of the historical count, and use recent observed accepted/rejected deployments as separate evidence. A successful Git release after a manual API 402 disproves a blanket "nothing can deploy" claim but does not establish that Git is exempt from the limit.

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
- Never commit or print credentials. No repeated attempts through a method after its quota error. A normal user-authorized Git release is not a reason to bypass provider restrictions; distinguish its outcome from the prior API error and avoid route-switching solely to evade a quota.
- Do not weaken protections or hide failures merely to save deployments. Preserve unrelated projects and branches.
- No claims of live status without checking actual production. No claims of tests passing without running them.

## Load on demand

- [Operations and decision rules](references/operations.md) for release gates, project discovery, duplicate builds, Git branch rules, and failure handling.
- [Platform facts and primary sources](references/platform-facts.md) for quotas and the correct types of skipped deployment.
- [Real account incident](references/pitchnight-incident.md) for an evidence-backed example.
- [CLI usage](references/cli-usage.md) for token-free connected operation, offline snapshots, read-only REST audit and exit codes.

## Standard report

**Budget:** advisory tier; visible records / planning cap; estimated record headroom (not official quota balance); window; coverage and source.

**Availability:** UNVERIFIED unless supported by a recent accepted deployment, with route/project/time stated. No earliest guaranteed retry minute from deployment history. For API 402 vs Git success, state both and do not extrapolate an exemption.

**Drivers:** top projects, feature branches, errors/cancellations, cross-project duplicate commits.

**Next action:** smallest evidenced remedy, its risk, and required authorization.

**Release proof:** target repo/branch/SHA, checks, production SHA/state/domain, or exact blocker.
