# Using these skills from any model or agent

A skill here is plain Markdown in the open Agent Skills layout: a folder with a `SKILL.md`, optional `references/`, `scripts/` and `assets/`. Any model that can read text can follow it. What changes between tools is how the files reach the model and which actions the tool can really perform.

Tool behaviour changes often. The paths below were checked in November 2026. Confirm them in the tool's own documentation before changing a global setup.

## Three levels of access

Work out which level you are at, then say so. It decides what you can honestly claim.

| Level | The agent can | Use |
| --- | --- | --- |
| **A. Repository** | Read the whole Skills checkout, run Node and Git | Full Master Craft: live freshness, planner, scripts, every specialist |
| **B. Fetch** | Read files by URL or through a GitHub connector, no shell | Master Craft with pinned reads. Scripts and planner unavailable: do their checks by hand and say so |
| **C. Paste** | Read only what is in the conversation | A bundle. Standalone mode. No freshness claim |

## Level A: coding agents with the repository

Keep one full checkout of `hayalows/Skills`. Link skills into the tool instead of copying them, so relative links between skills keep working and one `git pull` updates everything.

| Tool | Where it looks for skills |
| --- | --- |
| Claude Code | `~/.claude/skills/<name>/` for all projects, `.claude/skills/<name>/` for one project |
| Codex | `~/.agents/skills/<name>/` or `.agents/skills/<name>/` in the project |
| Gemini CLI | `~/.gemini/skills/<name>/` or `.gemini/skills/<name>/`. It also reads `.agents/skills/` |
| Cursor | `.cursor/skills/<name>/` in the project |
| GitHub Copilot | `.github/skills/<name>/` in the repository |
| Other tools | Many read `.agents/skills/`. Check the tool's documentation |

Example for Claude Code and Codex, run from the Skills checkout:

```bash
mkdir -p ~/.claude/skills ~/.agents/skills
for skill in master-craft product-design-os personal-craft; do
  ln -sfn "$PWD/$skill" ~/.claude/skills/$skill
  ln -sfn "$PWD/$skill" ~/.agents/skills/$skill
done
```

Linking `master-craft` alone is enough for routing, because it reads the other skills from the checkout by relative path. Link `product-design-os` as well when you want to call it directly.

**Project instruction files.** When an agent works inside the Skills repository itself, it reads the root `AGENTS.md`. Codex, Cursor, GitHub Copilot and many other tools read that file directly. Claude Code reads `CLAUDE.md`, which imports `AGENTS.md`. Gemini CLI reads `GEMINI.md` by default and can be pointed at `AGENTS.md` with its `context.fileName` setting.

**In another project.** To make an agent use these skills while working on, say, RouteLab, either install them as above or add one line to that project's own `AGENTS.md`:

```text
For product, design and release work, read and follow /absolute/path/to/Skills/master-craft/SKILL.md.
```

## Level B: assistants that can fetch

Give the assistant the entrypoint and tell it where the rest lives.

```text
Read https://raw.githubusercontent.com/hayalows/Skills/main/master-craft/SKILL.md and follow it for this task.
Resolve its relative links against https://raw.githubusercontent.com/hayalows/Skills/main/master-craft/.
The index of every skill is at https://raw.githubusercontent.com/hayalows/Skills/main/llms.txt.
Fetch only the files the task needs. Tell me which files you actually read.

Task: ...
```

With a GitHub connector, ask it to resolve the current `main` commit first and read every file at that one commit, as the freshness protocol describes. With plain URL fetching there is no commit pin: label freshness `UNVERIFIED (raw main, unpinned)`.

To call the design skill directly, swap the first line for `product-design-os/SKILL.md`. It is self-contained.

## Level C: chat models and APIs with no file access

Build a single file and paste it, attach it, or send it as the system prompt.

```bash
# Design skill with its three core references (about 7,500 words)
node master-craft/scripts/bundle.mjs product-design-os --refs visual-direction,build-and-verify,quality-rubric --out product-design-os.bundle.md

# Design skill with everything (about 26,000 words: use only with a large context window)
node master-craft/scripts/bundle.mjs product-design-os --all --out product-design-os.full.md

# Master Craft with its routing and product references
node master-craft/scripts/bundle.mjs master-craft --refs routing,playbooks,product-build,quality-gates,portability --out master-craft.bundle.md
```

The public skills site also serves ready-made bundles under `/bundles/` after each build.

For an API call, put the bundle in the system prompt and the task in the user message:

```text
system: <contents of product-design-os.bundle.md>
user:   Redesign this checkout form. Here is the current HTML: ...
```

A bundle is a snapshot. Rebuild it after the skill changes. Anything the bundle leaves out is listed at its end with a URL.

## Claude apps and uploaded skills

Skills uploaded to an assistant as a packaged folder travel alone. They cannot follow links to sibling folders.

- **Product Design OS** is self-contained and suits this well. Zip the `product-design-os` folder and upload it through the app's skill settings.
- **Master Craft** depends on the rest of the library. Uploaded alone it runs in standalone mode. Prefer Level A or B for it.

## Standalone mode

When Master Craft cannot reach the other skills, it still works, with reduced claims:

1. Say `STANDALONE: sibling skills not reachable` and name what is missing.
2. Use the references that travelled with it: `routing.md`, `playbooks.md`, `product-build.md` and `quality-gates.md` carry the method.
3. Do the specialist's job directly at the level those references describe. Do not claim a specialist skill ran.
4. Keep every authority rule. Missing files never widen what you may do.
5. Label freshness `UNVERIFIED`.

## What no skill can do

A skill is instructions. It does not create tools.

- It cannot give a model a browser, a shell, repository access, credentials or a deployment route.
- It cannot make a model render a page it has no way to render. The honest output then is `NOT VISUALLY VERIFIED`.
- It cannot schedule background work.
- It cannot verify its own freshness without live repository access.

When a step needs a capability the current tool lacks, name the gap, do the part that can be done, and report the rest as not verified.

## Checking a setup

Ask the agent, in a fresh session:

```text
Use Master Craft. Before doing anything, tell me: which access level you are at, which commit of the Skills
repository you are reading, which skills you can reach, and which tools you can actually run.
```

A good answer names a commit or says `UNVERIFIED`, lists real skills, and does not claim tools it lacks.
