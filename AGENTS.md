# Hayalows Skills: instructions for agents

This repository is a library of agent skills. Each skill is a folder with a `SKILL.md` and optional `references/`, `scripts/`, `assets/` and `tests/`. The format is the open Agent Skills layout, so any agent that reads Markdown can use it.

## If you were asked to use a skill

1. Start at [`master-craft/SKILL.md`](master-craft/SKILL.md) unless the user named another skill. It chooses and sequences the right skills for the task.
2. For interface and product work called directly, use [`product-design-os/SKILL.md`](product-design-os/SKILL.md). It is self-contained.
3. Read a skill's `SKILL.md` first, then only the references the task needs. Do not load every file.
4. The full index with one-line descriptions is in [`llms.txt`](llms.txt).

A skill is instructions. It never grants tools, credentials or permission. The user's request sets what you may do: inspecting is not permission to edit, and building is not permission to publish or deploy.

## If you were asked to change this repository

- Keep each skill self-describing: valid frontmatter with `name` matching the folder and a `description` under 1024 characters that says when to use it.
- Keep `SKILL.md` short and move detail into `references/`. Link every reference from the entrypoint.
- Write plain English. Short sentences. No hype. No em dashes.
- Do not invent sources, test results or measurements in skill text.
- `collections/` and `security-audit/` are third-party copies with their own licences. Do not edit them without being asked, and keep their notices.
- Run the checks before you finish:

  ```bash
  npm test        # integrity, freshness, plan, execution, bundle and design-lint suites
  npm run build   # public directory and portable bundles into dist/
  ```

- `dist/` is build output. Do not commit it.
- A push to `main` can trigger a hosted build of the public directory. Do not push to `main`, open a pull request or deploy unless the user asked. Read [`vercel-deployment-steward/SKILL.md`](vercel-deployment-steward/SKILL.md) before any Vercel action.

## Layout

| Path | What it is |
| --- | --- |
| `master-craft/` | Orchestrator: routing, freshness, product pipeline, quality gates, portability |
| `product-design-os/` | UI and UX design, build-and-look verification, rubric, starter tokens, static checks |
| `personal-craft/` | Working agreement and verification policy for substantial work |
| other top-level folders | Specialist skills: writing, brand, reports, audits, evidence, deployment |
| `collections/matt-pocock-skills/` | Imported engineering and productivity skills (MIT) |
| `site/` | Source of the public skills directory |
| `llms.txt` | Machine-readable index of the skills |
