# Routing metadata (V2.1)

Master Craft keeps semantic interpretation in the host model. The planner enforces declared rules; it cannot prove a request was correctly classified or that an override was actually authorized. Do not mark a task substantial just to evade a complexity guard. Do not label a skill explicit unless the user actually requested it.

Optional skill frontmatter, using a restricted flat mapping and lists:

    routing:
      minimum_complexity: substantial
      explicit_override: true
      roles: [lead, supporting]
      default_role: lead
      category: orchestration
      exclusive_role: workflow-lead
      conflicts_with: [other-skill]

- minimum_complexity: optional; currently only substantial is supported.
- explicit_override: optional boolean; defaults to false. Only the exact user-requested skill can override minimum complexity. No override bypasses permissions, conflicts or allowed roles.
- roles: nonempty unique list of lead, specialist, supporting. Defaults to all three for older skills without role metadata. default_role must be declared; otherwise lead is preferred when declared, or the first declared role, or specialist for a legacy skill.
- category: optional descriptive token; not an automatic routing rule.
- exclusive_role: optional shared ownership token; requires the lead role to be declared. A non-supporting selection claims the exclusive role. Two owners block the plan. Supporting is permitted only when declared.
- conflicts_with: optional list of exact relative skill paths or skill names. Any matching selected pair blocks, regardless of role.

The parser supports the documented block, scalar strings/booleans and simple inline or indented lists; it is not a general YAML parser. Unknown or malformed policy fails closed. For a verbatim third-party import, an adjacent regular-file routing.json with the same flat schema is supported instead of editing upstream frontmatter (not both). Remote snapshots carry the sidecar blob SHA; Full execution contracts record it as routingBlob alongside the skill blob. Read policy and skill instructions at the same pinned commit.

## Examples

Product Design OS owns product interfaces, Design Taste owns marketing pages, Gemini Frontend Design and Interface Workshop can be a lead or an explicitly assigned visual helper. Frontend Design and UI/UX Craft are supporting skills. Website UX Audit is a read-only lead; Behavioral Interaction Design can support a particular interaction. If two distinct deliverables need separate leads (marketing page and signup flow), split the work into two plans rather than weakening exclusivity. No restriction on separate tasks using different skills.

    {"specialists":["gemini-frontend-design/SKILL.md"],"productDesign":true,
     "specialistRoles":{"gemini-frontend-design/SKILL.md":"supporting"}}

This combines the mandatory product-design owner with a visual helper. With the role omitted, both default to lead and the plan blocks. A lead-only skill cannot become a helper by changing a string. The planner returns specialistRoles with resolved roles for inspection. Do not execute affected work while routing blockers remain; revise the plan. A routing-blocked plan omits implementation and hosted release stages. On Full tasks, record why each selected skill is necessary in the existing execution contract why, along with procedure, restrictions, references and revision. A nonempty rationale is not evidence of correct semantic routing.

Archived versions stay out of automatic discovery; use a deliberately pinned historical source when needed. Run the full repository test command before changing active policy.
