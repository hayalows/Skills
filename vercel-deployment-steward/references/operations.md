# Operations and decision rules

## 1. Start at the team boundary

Before proposing or creating a hosted deployment, identify:
- Vercel team or personal scope and plan. Never guess which account owns the project.
- Target project, repository, default production branch, current live SHA and custom domain.
- Other Vercel projects using the same GitHub repository and their root directories.
- Whether automatic Git deployments are enabled for main, feature branches, or both.
- The user's actual instruction: audit, implement, preview, ship, or change account settings. These are distinct permissions.

Read projects and recent deployments through connected Vercel tools where possible. Inspect GitHub branch and commit metadata through GitHub tools. If the connector provides incomplete account-wide data, mark scope partial.

## 2. Account-wide audit

Collect all deployments in the rolling 24-hour window for the **whole team**. Avoid per-project-only counts. Paginate until the oldest returned record is older than the cutoff or the API provides no further page. Retain records in all states, including ERROR and CANCELED, in the visible-record count. Include queued/initializing records where available.

Create these evidence tables:
- Projects: name, total, production, unlabelled/non-production, ERROR, CANCELED, branch distribution.
- Shared Git repositories: source repo to Vercel projects, noting root directory if known.
- Fan-out: identical Git repo + SHA mapped to two or more Vercel project names.
- Suspected waste: repeated production deployments for the same SHA, feature branches with many commits, manual rebuilds after successful Git auto-deploy.
- Freshness: timestamp, exact 24-hour cutoff, pagination completion and confidence.

A deployment with target=null has an **unlabelled** target in some API results. It is likely a non-production feature-branch build if its branch is not main, but never categorically call every such record a preview. A deployment returned in a list does not prove it was charged to the platform's private limit counter, and the inverse is not guaranteed. A 402 error overrides visible-record estimates.

Separate deployment count from deployment storage (GB-month), transfer, build minutes, functions and other Vercel limits. If storage telemetry is unavailable, mark it unverified; do not estimate storage by multiplying number of records by project size.

## 3. Two separate decisions: deployment risk and platform availability

**Planning risk** is inferred from visible history. It is never a definitive API quota check. **Technical availability** requires a specific attempt and its response, and may change over time or differ by the mechanism used. Record each result with timestamp, environment, team/project and method: Git-triggered, manual Vercel API or CLI. Never infer from a rejected POST that Git-triggered production is universally blocked; never infer from a successful Git deployment that it is quota-exempt.

**Historical expiry is not the earliest technically possible time.** The time when one of the oldest visible records leaves a 24-hour window says when the list-derived count would decline, *if there were no new records*. It does not identify when Vercel's internal quota first accepts a release. Never tell the user they must wait until that date if later evidence shows releases have already succeeded.

## 4. Release guard

Use the planning tiers in SKILL.md, checking percentage against a separately confirmed Hobby cap. When the CLI uses its default cap of 100, label this a configured assumption, not authoritative billing state.

- GREEN: normal local development; still gate changes with lint/build and relevant E2E.
- WATCH: consolidate changes and reduce feature-branch auto-deploy; limit new hosted previews.
- PROTECT: prioritize final release work; consider skipping preview only when local confidence and impact justify it.
- FREEZE: stop unattended and discretionary deployments. This is an internal safety policy, not proof that Vercel will reject a legitimate user-authorized release. With explicit publication authorization, recent accepted outcomes for the intended route, and no fresh 402 for that same route, a single controlled production push can be justified; explain uncertainty, expected blast radius and check its result. Never promise success.
- UNKNOWN: seek missing pages, identity or plan data. Do not issue a "safe to deploy" claim. If the user already authorized production and a genuine time-sensitive need exists, use the observed route-specific evidence to decide whether one attempt is reasonable; do not mistake incomplete account-wide history for certain rejection.

If a release is approved, choose **one** publication route:
1. Git integration: build locally; commit a reviewable set of changes; push once to the production branch; observe the Git-triggered deployment; verify actual live domain. Do NOT manually deploy the same SHA merely because a previous message said "push live."
2. Explicit manual deployment: use only when the repo is not already auto-deploying or the desired path is otherwise demonstrably necessary. Check target/team/project/branch/plan and user permission first.
3. Staged production build + promotion: if the project requires this, stage one production build, test it, then promote the **same production build**, as supported by Vercel. Do not claim a preview can be promoted without a rebuild.

After a 402, stop repeat attempts via that rejected creation method and check whether a deployment record exists. If a normal Git integration subsequently accepts another project's production commit, that is **proof of an accepted Git-triggered build at that timestamp only**, not evidence that Git has a special quota exemption or that the intended project will also succeed. Don't cycle through endpoints or extra projects to circumvent restrictions. Preserve old production until the verified replacement is ready.

## 5. Stop new deployments, not just wasted builds

**Prefer preventing automatic deployment initiation** where no preview is wanted. A project-specific branch configuration can opt out of automatic feature-branch deployments. Example for a repo that intentionally auto-deploys main but NOT feature branches (propose, do not apply without approval):

    {
      "$schema": "https://openapi.vercel.sh/vercel.json",
      "git": {
        "deploymentEnabled": {
          "feat/*": false,
          "fix/*": false,
          "chore/*": false,
          "main": true
        }
      }
    }

Unspecified branches default to enabled, so review other branch prefixes. If several glob rules match, any true match wins. The actual production branch might not be main; verify before changing a rule. For multiple Vercel projects attached to one repo, a shared config can affect them differently. Review each project and root directory first.

**Avoid treating an Ignored Build Step as free:** the deployment is created before the command runs; Vercel says canceled builds created via this method still count toward quotas and concurrent build slots. This is not an effective daily deployment-rate guard.

**Monorepos:** Vercel's automatically skipped **unaffected** deployments may be excluded from rate limits as of 21 October 2026, but only when the built-in feature is actually enabled and detects unchanged source/internal dependencies. This is not equivalent to a custom ignored build command.

## 6. Diagnose the waste instead of guessing

- Many ERROR entries on one feature branch: inspect build logs and the first failing commit; reproduce locally before another push. Use a red-capable feedback loop.
- CANCELED entries: check bursty commits and queued builds. Older builds may be canceled, but their records do not disappear.
- Several Vercel projects on one repo: inspect which domains, env vars and root paths must survive. Recommend targeted repository/project linkage or automatic branch policies only after understanding each legitimate use. Do not delete projects to save deployment counts without authorization.
- Repeated SHA on the same project: inspect manual redeployment, webhook or CI triggers; identify one source of truth for releases.
- Build checks still failing: do not disable them. Fix the cause and run local E2E or existing gates.
- Capacity is healthy but a 402 still appears: trust the platform's error; don't assume the visible count matches the internal counter. Stop retries, collect sanitized error code/time and request metadata, and investigate with Vercel support/docs.

## 7. Low-waste development and verification

Plan project changes with concrete acceptance criteria. Work in a local/unwatched branch when available. Prefer one cohesive commit or a consolidated merge rather than many consecutive pushes to watched branches. Run existing checks and relevant E2E at real user entry points; for UI, inspect mobile, desktop, focus, failure, form and navigation states. For backend, test the real permission and persistence boundaries where feasible.

On release:
- Record Git SHA and expected environment.
- Avoid duplicate manual deployment if Git integration already handled the push.
- Confirm production READY plus correct domain and HEAD SHA. Check runtime errors and key flows.
- Capture observed result with timestamp and tests; never assert a deploy succeeded based solely on Git push.
- Where setup changes impact collaboration, authentication, billing, or production, request explicit approval and leave a reversible plan.

## 8. Output contract

Use a brief report with observed facts, inferences labelled, source coverage, count/time, advisory planning tier **and** technical availability (separate fields), and the recommendation. Use UNVERIFIED when technical availability is not established. Show the latest accepted/rejected attempts with exact timestamp and method. A next record-expiry timestamp is not a guaranteed release minute. For a setting change, specify the affected project and what branches still deploy.
