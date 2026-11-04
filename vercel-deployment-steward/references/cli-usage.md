# Read-only CLI usage, E2E and operational notes

## Requirements

Node.js 20 or newer and a Vercel token with **read access** to the selected team. Save the token in a local environment variable or CI secret; never commit, paste into chat, or print it. In connected ChatGPT conversations, prefer the authenticated Vercel tools and do **not** request a token just to inspect deployment history.

The executable script performs HTTP GET requests only. It does not create, promote, delete, cancel or redeploy anything.

From this skill directory:

    node scripts/audit-deployments.mjs --team "$VERCEL_TEAM_ID"
    node scripts/audit-deployments.mjs --team "$VERCEL_TEAM_ID" --json
    node scripts/audit-deployments.mjs --team "$VERCEL_TEAM_ID" --gate

Set VERCEL_ACCESS_TOKEN or VERCEL_TOKEN and VERCEL_TEAM_ID in the environment. On Windows PowerShell, use:

    node .\scripts\audit-deployments.mjs --team $env:VERCEL_TEAM_ID --gate

## Modes

- Normal: prints a compact whole-team audit and always exits zero when a complete report was produced (even if risk is FREEZE).
- --json: emits machine-readable JSON. Use this for review reports or CI.
- --gate: exits 0 for GREEN, WATCH and PROTECT; exits 2 for FREEZE; exits 3 for UNKNOWN or technical failure. This is an **unattended/discretionary-release policy gate**, not a Vercel API acceptance test. Exit 2 means stop automatic publishing, not "deployment is impossible." A user-authorized, time-sensitive production release may be assessed independently for a single deliberate attempt using the project's normal integration. Exit 0 is not a guaranteed deploy slot.
- --cap N: planning cap (default 100, Hobby) to accommodate another verified plan.
- --now UTC_ISO: freezes audit time for reproducible offline checks.
- --snapshot PATH: read a local JSON payload instead of contacting Vercel. Format: {"complete":true,"deployments":[...]}. Set complete=true only after exhaustively checking the entire 24h window. An incomplete snapshot must report UNKNOWN.

The script paginates at 100 records per request, stops at the 24-hour cutoff, handles duplicate deployment IDs, and fails closed on malformed/unfinished evidence. If pagination stops unexpectedly, the report must not claim green status.

The JSON includes `technicalAvailability: "UNVERIFIED"`, `earliestGuaranteedMinute: null`, and `nextRecordExpiryAt`. The last is the expiry of the *oldest visible record*, **not** the first minute a deployment can succeed. The `estimatedRemaining` number is only planning headroom derived from the visible list and may disagree with the provider's actual quota counter.

## Integration with GitHub/CI

Use the gate **before a Git push or merge that will trigger an automatic Vercel deployment**. Running the gate in GitHub Actions after a push to main is valuable evidence, but it **cannot stop** the Vercel Git integration deployment already triggered by that same push. To make it a real protection, use approved branch rules and merge checks, or a deliberate manual release workflow that consults the gate before calling Vercel.

Do not use the 24h CLI audit as an excuse to bypass failed build, security or accessibility checks. Read-only REST audits may encounter provider rate limits; fail closed, and do not retry aggressively.

## CLI E2E harness

Run:

    node tests/cli-smoke.mjs

No token, no user data, no live Vercel deployments, and no network access are required. The harness invokes the CLI as a child process with disposable snapshots and checks:
- healthy, watch, protect and freeze thresholds,
- incomplete-data fail-closed response,
- rolling 24-hour filter,
- one SHA deployed to two projects,
- failed/canceled count inclusion,
- report mode (no gate) behaviour,
- more than 100 visible records coexisting with successful Git-triggered deployments,
- no fabricated earliest guaranteed deployment minute even for a small visible count.

A checked-in test is not a passed test. Report its actual execution result, environment and commit SHA when run. The GitHub workflow also executes this E2E harness on changes to this skill.

## Operational recommendations

- A scheduled ChatGPT task can request the skill to check connected Vercel usage on a cadence, but scheduling is separate from installing the skill. Do not claim background monitoring unless a schedule really exists.
- Do not authorize the script to write or edit Vercel settings. It only recommends branch configuration changes.
- For per-project recommendations, combine the CLI JSON with connected project settings, GitHub branch history and verification evidence.
- After a manual API 402, do not assume all release methods are technically unavailable. In the verified 4 November incident, Git-connected RouteLab production succeeded about 11 minutes after a manual API request failed. This does not mean Git is quota-exempt. Record method, timestamp and exact result; avoid repeated API attempts and routing around provider restrictions.
- If asked for the "first possible minute," distinguish the earliest **observed** accepted deployment from the unknown earliest *technically possible* minute. Expiry forecasts are only calculations about the visible history.
