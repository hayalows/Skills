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
