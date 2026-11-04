# Platform facts and source provenance

**Revalidate before changing settings.** These facts are current as reviewed on 4 November 2026 and may change.

## Official Vercel sources

- Hobby deployment creation cap: **100 deployments per day** (planning reference, not a live remaining-quota API). Source: https://vercel.com/docs/limits and https://vercel.com/docs/plans/hobby
- Git integration triggers builds on connected-branch commits. Source: https://vercel.com/docs/git and https://vercel.com/docs/project-configuration/project-settings
- Branch-level deployment controls: git.deploymentEnabled in Vercel project configuration. Unspecified branches default to true; with multiple matching rules, any true match deploys. Source: https://vercel.com/docs/project-configuration/git-configuration
- Ignored Build Step produces canceled builds that **still count as full deployments** toward deployment quotas, according to Vercel project settings documentation. Source: https://vercel.com/docs/project-configuration/project-settings
- As of **21 October 2026**, Vercel's automatically skipped **unaffected monorepo** deployments no longer count toward rate limits, provided the feature applies. This is a separate mechanism from custom ignored build steps. Sources: https://vercel.com/changelog/skipped-monorepo-deployments-no-longer-count-against-limits and https://vercel.com/docs/monorepos
- Hobby deployment-storage allowance and retention policy are distinct from daily deployment count. As of 16 September 2026, Vercel changed retention to reduce storage burden. Sources: https://vercel.com/changelog/hobby-projects-now-retain-fewer-deployments-to-free-up-storage and https://vercel.com/docs/limits
- Read-only deployments REST API is GET https://api.vercel.com/v6/deployments, scoped with teamId, using an access token in an environment variable. Source: https://vercel.com/docs/rest-api and https://vercel.com/docs/agent-resources/vercel-mcp/tools
- Staged production builds and promotion are distinct from ordinary preview builds: https://vercel.com/docs/deployments/promoting-a-deployment

## Corrected release interpretation from 4 November 2026

Vercel publishes a Hobby limit of 100 deployments created per day. That is not the same as a complete, exposed, per-team remaining-deployment balance. A manually rejected deployment POST cannot establish that every later Git-triggered deployment will be rejected.

On 4 November 2026, a manual API request for Pitch Night returned HTTP 402 with code `api-deployments-free-per-day` at 22:16:14 GMT. RouteLab's ordinary Git-triggered production deployments then reached READY at 22:27:00 and 23:02:44 GMT, while approximately 101 and 103 visible records, respectively, fell within the preceding 24 hours.

This disproves the earlier interpretation of list-derived 100+ records as a definitive technical lockout. It does **not** establish a Git-specific exemption or the cause of the cross-route difference. See [incident evidence](pitchnight-incident.md).

Keep three facts separate: (1) visible deployment-history records, (2) provider internal quota accounting and method-specific errors, and (3) a team's advisory planning threshold. A record-expiry calculation is not a guaranteed successful-deployment time.
## Important inference limits

A list of deployments can undercount or otherwise differ from Vercel's internal rate-limit counter. Do not promise that an apparent 15 spare records means 15 deployments are guaranteed. An official 402 proves that one attempt through one creation method was rejected at that time, not that every method or project is blocked. Do not repeatedly retry the rejected method. Never claim a precise earliest possible minute from historical record expiry or an unexplained error.

The target field may be null for non-production entries, but that does **not** prove that every such entry was a preview. Use branch, environment and project metadata to qualify conclusions.

Do not treat a Git push as synonymous with a successful deployment, nor a READY deployment as proof the custom domain points to it. Verify the alias/domain and a smoke test.

## Safe ordering of optimisation

1. Local checks and batched commits.
2. Branch Git deploymentEnabled rules, scoped and approved.
3. Check shared Git repos connected to multiple projects.
4. Built-in monorepo skip-unaffected feature, if truly applicable.
5. Deployment retention and separate storage usage review.
6. Consider plan upgrade only after identifying the genuine usage need; never silently change billing.
