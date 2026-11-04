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

**Decision:** Consolidate changes, stop automatic experimental-branch deploy initiation where safely approved, inspect duplicate project linkage, and avoid manual deployment requests after Git auto-deploy. Do not change the live Vercel configuration purely from this incident example.

**Confidence:** High for the deployment records, project/group counts and Git metadata observed in the connected tools. Lower for claims about exact quota-accounting or the reset time; provider internals were not visible.

**Reusable lesson:** Never check only the project the user is working on. A shared Vercel team-wide allowance can be consumed by unrelated projects and feature branches.
