# Evidence case: deployment budget exhausted during Pitch Night work

**Snapshot date:** 4 November 2026. This is an incident example, not an assertion of current usage.

A read-only check of the Vercel team returned the **100 newest recorded deployments**, ranging approximately from 07:41 to 22:10 GMT. Project breakdown of those **100 records**:

| Project | Records | Observed detail |
| --- | ---: | --- |
| routelab | 64 | 59 non-production/unlabelled targets, 5 production |
| pitchnight | 25 | All 25 production, all READY |
| papa-kojo-cv | 6 | 1 production, 5 non-production/unlabelled |
| hayalows-studio | 5 | 5 non-production/unlabelled |

Across those 100 records: 60 READY, 24 ERROR and 16 CANCELED. There were 31 production targets and 69 null/unlabelled targets. This is a **most-recent-100 sample**, not a complete historical quota ledger and not a platform billing count.

Root signals:
- RouteLab was responsible for the largest proportion of recent deployments. Many were created by pushes to temporary feature branches.
- The same five security-branch commits in GitHub repository hayalows/hayawebsite were deployed independently to both papa-kojo-cv and hayalows-studio. This created 10 Vercel deployment records for five source commits.
- Pitch Night's repeated small main-branch commits also created many production builds. The final main SHA was later ahead of the deployed production SHA because the Hobby deployment quota blocked further creation.

## Correction: records are not the platform's authoritative quota counter

A later investigation overturned the initial assumption that the 100 visible records meant no further deployments could be accepted until those records aged out.

**Verified sequence on 4 November 2026 (GMT):**

| Time | Route | Outcome |
| --- | --- | --- |
| 22:16:14 | Manual Vercel API POST /v13/deployments for Pitch Night | HTTP 402, code api-deployments-free-per-day; no new Pitch Night build |
| 22:27:00 | Normal Git-triggered production deployment for RouteLab | READY, Git commit 394266b4143f5171f89753b6c4c077d9d8806aa6 |
| 23:02:44 | Normal Git-triggered production deployment for RouteLab | READY, Git commit 132d073b8a3d08d0d8bcf5f69044a06901eb7ae0 |

The visible team-wide deployment history contained approximately **101 records** in the previous 24 hours at 22:27 and **103** at 23:02. A counter based on those records alone would have predicted rejection, but two subsequent releases were accepted. This is a verified observational contradiction of the old **blanket** assumption, not proof that Git deployments never count against the limit.

**What we know:** A specific manual API request failed; subsequent Git-connected production builds on a separate project succeeded. The earliest *observed* successful post-402 deployment was **22:27 GMT on 4 November**. The genuinely earliest time a deployment could have succeeded is **not knowable from this history**.

**What remains unknown:** The cause of the different outcomes. It may depend on internal counters, deployment creation routes, timing, exclusions, or other provider behaviour. Do not attribute it to a formal Git exemption or claim a precise free-slot time.

**Corrected operational rule:** A FREEZE tier is conservative advice for unattended/discretionary work, not an assertion that deployment is technically impossible. When a user explicitly requests an important production release, check accepted outcomes by method and time, choose the project's normal authorized release route, make no more than one controlled attempt, and verify the resulting commit/domain. Do not repeat 402-rejected API requests or switch routes solely to circumvent platform restrictions. Predict expiry timestamps only for **visible records**, never as guaranteed release slots.

**Decision:** Consolidate changes, stop automatic experimental-branch deploy initiation where safely approved, inspect duplicate project linkage, and avoid manual deployment requests after Git auto-deploy. Do not change the live Vercel configuration purely from this incident example.

**Confidence:** High for observed Vercel deployment states, creation routes, timestamps and the HTTP 402 response. Low for Vercel's internal quota arithmetic or explanation for the cross-method difference, because provider internals were not available.

**Reusable lesson:** Never check only the project the user is working on. A shared Vercel team-wide allowance can be consumed by unrelated projects and feature branches.
