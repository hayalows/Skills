# Design references and decisions (reviewed 2026-11-04)

Primary specifications and documentation consulted while building this skill:

- Agent Skills specification: https://github.com/agentskills/agentskills/blob/main/docs/specification.mdx . A skill has a named SKILL.md, optional references/scripts and progressive disclosure. This router follows that structure and keeps its frontmatter concise.
- OpenAI Skill Creator guidance: https://github.com/openai/codex/blob/main/codex-rs/skills/src/assets/samples/skill-creator/SKILL.md . Use only details that change decisions; avoid excessive routing layers, scope expansion, silent permissions and generic ceremony.
- OpenAI Codex skill discovery: https://learn.chatgpt.com/docs/customization/overview . Metadata selects a skill, the body loads on activation, and references load on demand. A GitHub copy is not the same as an installed local skill.
- OpenAI plugin skills: https://developers.openai.com/plugins/concepts/skills . Skill instructions coordinate real connected tools; they do not provide tool connectivity themselves.
- Matt Pocock upstream router: https://github.com/mattpocock/skills (local pinned copy: collections/matt-pocock-skills/skills/engineering/ask-matt/SKILL.md). Source for staged engineering flows and choosing testing, triage, spec and review when appropriate.
- Matt Pocock writing-for-agents: https://github.com/mattpocock/skills (local pinned copy: collections/matt-pocock-skills/skills/productivity/writing-for-agents/SKILL.md and SKILL-MECHANICS.md). Context pointers and routing branches help avoid loading every skill.
- Firecrawl secondary account developer-skill search was used for additional examples of progressive disclosure and router anti-patterns. These secondary examples informed the comparison, not the source of platform guarantees.

Architectural decisions:
1. **One user-facing name, conditional routes.** Master Craft is a router, not a large combined instruction document. It exposes just enough routing behavior for task-specific loading.
2. **Skill path map + live inventory.** The map is human-reviewed; the Node metadata scanner and integrity test prevent silent omission when the checkout changes.
3. **Task sequences instead of fixed choreography.** Branding and UI require different procedures; deployment is conditional and permission-gated.
4. **Quality from evidence.** Define actual task outcomes and tests, not self-assigned quality scores or universal claims about security.
5. **Safety boundaries are preserved.** Read-only audits stay read-only, full security audits keep isolation limits, and production publication remains a separate action.
6. **No hidden agent claim.** Delegation uses available services only; a skill file cannot spawn agents or run asynchronously by itself.

These sources and decisions describe the design; they are not proof that every target runtime supports all stages. Verify installed runtimes and connectors per task.


## Routing and specialist design review

The review covered the names, descriptions and routing hints of all 58 existing definitions, with deeper review of nearby workflows. The imported engineering skills cover diagnosis, design, specs and implementation. The productivity and experimental groups already cover interviewing, teaching, handoff and agent coordination. The native product skills cover design, audit and verification, while the report skills cover evidence and presentation. The two additions handle narrower outputs missing from that set:

| Gap | Nearby coverage | New output |
| --- | --- | --- |
| Evidence for a product decision | Product Design OS, UI/UX Craft, Website UX Audit | Comparable tasks or measurements, instrumentation integrity, thresholds, guardrails and a bounded ship decision |
| Decision model challenge | Consulting-Grade Reports, Personal Craft | Reproducible cash-flow or forecast logic, independent recalculation, a flip point or benchmark, and validity limits |

- [Agent Skills specification](https://agentskills.io/specification) and [Anthropic's composable skill design](https://www.anthropic.com/research/equipping-agents-for-the-real-world-with-agent-skills) support progressive loading from a current inventory.
- [Anthropic's effective agents guide](https://www.anthropic.com/engineering/building-effective-agents) separates routing from execution and recommends the simplest sufficient workflow. Master Craft keeps semantic judgment with the agent and uses deterministic gates for scope and release ordering.
- [OpenAI's skill eval guide](https://developers.openai.com/blog/eval-skills) distinguishes captured agent behavior from static checks. The planner suite exercises 55 independently specified request plans and extension/release edge cases. A separate five-request agent dry run covered product repair, search evidence, a read-only model, unavailable Vercel access and a short voice rewrite. That run identified a missing release-tool gate, now covered by the planner suite. Two additional independent passes interpreted 50 raw requests without the fixture labels. They distinguished the evidence and model workflows, preserved read-only boundaries, and withheld production on missing target or approval. They also exposed one accidental explicit-only skill selection in a simple explanation and an extra design owner in a read-only UX audit. The entrypoint, playbook and metadata check now clarify both cases. A preview route was appropriately limited to preview even though the reviewer used “publish” for the preview operation. The planner uses separate hosted-build and production-publish stages to disambiguate this. Some routes reasonably used different modes or optional skills while keeping the same authority and outcome. These dry runs tested routing decisions. They did not execute the target projects or estimate a general routing accuracy.

The specialist references document the analytical assurance, usability, experimentation and release sources behind their procedures.
