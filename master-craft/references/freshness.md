# Live skill freshness and version selection

## What "latest" means

Master Craft uses the newest **committed** revision on the default `main` branch of `hayalows/Skills` when a new task begins. If you change Personal Craft, Product Design OS, Vercel Deployment Steward, or any other skill in this GitHub repository and commit it to `main`, the next invocation must read that version.

- **Updates:** the latest instruction file replaces any cached instructions from an earlier session.
- **New skills:** the current recursive tree is scanned for every `SKILL.md`, even if the new skill isn't listed in the curated `references/skill-map.md`.
- **Renamed/removed skills:** the current tree decides what exists; old map links are merely hints.
- **Additional reference files:** fetch the chosen skill's needed files from **the same commit** to prevent mixing old instructions with new references.
- **Third-party collections:** an imported Matt Pocock/Cloudflare skill is latest only relative to **your** copy. Its upstream original is *not* auto-synced into your repository.
- **Work in progress:** files edited locally or on an unmerged branch aren't the default latest. Use a specified branch or commit only when explicitly requested.

A task's chosen skill versions are held at a single commit SHA for consistent execution. On the next task Master Craft checks again. Before a separate high-impact production release, recheck current `main` and examine changed relevant skill instructions if the revision advanced.

## Connected ChatGPT/GitHub workflow

1. Read the active GitHub repository `hayalows/Skills`; resolve its default `main` branch HEAD commit SHA using the GitHub connector.
2. Read the recursive Git tree **at that commit**. If the connector has no recursive tree operation, use an available Git checkout and verify its snapshot revision, or use another authorized GitHub interface that exposes the complete tree. If enumeration is unavailable, direct pinned file reads can verify known specialists but cannot establish complete discovery. Label that partial result. Include paths ending in `SKILL.md`, regardless of their directories or inclusion in the cached skill map.
3. First read Master Craft itself and its relevant references at the pinned SHA. Consider current skill names/descriptions and file paths when selecting candidates. Read the current full SKILL.md for the chosen specialists using `ref=<HEAD_SHA>`; load relevant references at the **same SHA**.
4. Execute only the relevant skill paths, following scope and permissions. Log the library SHA in consequential work reports. If the user asks for a different branch, label the source and use that branch's exact SHA.
5. If GitHub is inaccessible, say `FRESHNESS UNVERIFIED`, identify the fallback instructions used, and do not claim that current skill policy or live release readiness was verified.

Connected GitHub access is required to follow this procedure in ChatGPT. Merely mentioning the skill does not create GitHub permissions.

## Local Codex/CLI workflow

Requires Node 20+, Git, an agent-accessible checkout of `hayalows/Skills`, a configured `origin` remote pointing to the intended library, and network/authentication that permits `git fetch`.

From the repository root:

    node master-craft/scripts/inventory.mjs --latest --json

This reads `origin/main` into the **Git object database** and returns:
- `verified_latest: true` when the remote fetch succeeded.
- `revision`: the exact commit SHA.
- `skills`: all current SKILL.md paths, names, descriptions, origin and blob SHA.

After choosing a skill, load the pinned version using the revision returned by the first command:

    node master-craft/scripts/inventory.mjs --at COMMIT_SHA --read product-design-os

To load a supporting skill with a potentially duplicated name, supply the exact relative path ending in `SKILL.md`:

    node master-craft/scripts/inventory.mjs --at COMMIT_SHA --read collections/matt-pocock-skills/skills/engineering/code-review/SKILL.md

For a raw current read without a separately recorded SHA (suitable for a quick one-skill task):

    node master-craft/scripts/inventory.mjs --latest --read personal-craft

For diagnostic local-only inspection:

    node master-craft/scripts/inventory.mjs --local --json

The local mode is explicitly `verified_latest: false`. It is NOT a way to claim remote freshness. The default invocation without `--latest` also inspects the local checkout for compatibility and makes no freshness claim.

The latest and pinned modes read Git object contents directly, **without running git pull, git checkout, git reset or merges**. They do not overwrite your working copy, including uncommitted edits. The current branch SHA is resolved first and fetched by SHA without sharing `FETCH_HEAD`. The latest mode only reads `origin`/`main` and doesn't create local source files. You can use the most recent instructions during a task even while keeping your worktree on a separate older commit.

## Failure handling

- Remote unreachable, no `origin`, authentication required or fetch error: `--latest` fails with `FRESHNESS_BLOCKED` and exit status 1. **It never silently falls back** to local or previously fetched instructions. An agent may explain the limitation, use a clearly labeled local copy for low-risk work, or stop a consequential action at its material gate.
- Requested commit SHA not fetched: `--at` fails; invoke `--latest` first if you want the current version.
- Deleted or unknown skill: fails with a clear error; do not treat the curated map as permission to run an absent skill.
- Ambiguous name: pass a full repository-relative skill path.
- New skill not mapped: it appears in the live inventory and can be selected; it does not need to be manually registered in the map first.
- Running inside an unrelated project or from a standalone copy of the master-craft folder: a real Skills checkout and appropriate Git origin are still needed. Instead use the connected GitHub workflow.
- Agent runtime caches metadata or an installed static skill copy: an agent may need to reload the skill or update its installed entrypoint. Master Craft's freshness procedure governs the **selected source instructions**, not cache invalidation inside every host product.

## Verification

Run the local end-to-end test with isolated temporary Git repositories:

    node master-craft/tests/freshness.e2e.mjs

The test creates a local bare Git remote and a stale agent checkout, updates an existing skill, adds a new one, and proves that a fresh inventory and pinned read use the changed remote files **without changing the checkout**. It also covers another subsequent update, deterministic pinning, unavailable remote, explicit offline mode and unsafe path rejection.

The repository CI also verifies that the curated skill map's current referenced paths exist when relevant, that the routing scenarios reference real skills and that the public directory builds. Passing those checks proves the plumbing is consistent, not that a real AI agent always selects the best specialist.

## Updating this protocol

Re-read this file and the actual Master Craft entrypoint from current main when a new session starts. If these files themselves are updated, the new version becomes the policy after the agent can access them. Prefer installation by symlink to the full Skills checkout instead of copying a detached folder. An installed static snapshot with no live repository connectivity cannot refresh itself.
