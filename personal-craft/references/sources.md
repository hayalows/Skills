# Primary sources and limits

Research checked 2026-09-21. Recheck relevant pages when standards, APIs, or service behavior affect current work. Sources support the bounded principles below; the overall workflow is a tailored synthesis, not a validated guarantee of superior design.

| Source | Applied principle |
| --- | --- |
| [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/) | Accessibility target and normative criteria; consult exact exceptions rather than inferring compliance from a checklist |
| [W3C target size minimum](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html) | Pointer-target evaluation, including size/spacing exceptions |
| [GOV.UK error summary](https://design-system.service.gov.uk/components/error-summary/) | Pair navigable summaries with field-specific error messages where appropriate |
| [GOV.UK task list](https://design-system.service.gov.uk/components/task-list/) | Choose task organization appropriate to the service; a task list is not universally suitable |
| [GOV.UK type scale](https://design-system.service.gov.uk/styles/type-scale/) | Consistent typography roles and reusable size/line-height relationships |
| [NN/g visual design principles](https://www.nngroup.com/articles/principles-visual-design/) | Evaluate scale, hierarchy, balance, and perceptual grouping |
| [Playwright best practices](https://playwright.dev/docs/best-practices) | Test visible outcomes, isolate tests, use resilient locators and observable assertions |
| [Web Vitals](https://web.dev/articles/vitals) | LCP/INP/CLS thresholds and field percentile evaluation |
| [OWASP authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) | Default-deny permissions and authorization checks on each request |

Distinguish three categories:
- Standards: apply normative criteria and exceptions accurately; do not claim formal compliance without sufficient evidence.
- Domain guidance: adapt to the product and platform; do not copy GOV.UK branding or treat one design system as universal.
- User preferences and craft heuristics: Luna-first routing, test ordering, E2E preference, limited delegation, typography starting ranges, reference counts, and review sequence. These are deliberate working choices, not requirements established by the cited sources.

Model IDs in execution-control preserve the supplied preference and must be checked against the runtime. No web source here establishes their availability or relative cost.
