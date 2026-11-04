# Matt Pocock Skills: Usage Notes for PKM

**Source:** https://github.com/mattpocock/skills  
**Original author:** Matt Pocock  
**Source commit:** `4ae2317ddb22b046e26455e4f9c9b3aaaf62212d` (2026-11-04 snapshot)  
**License:** MIT; see [LICENSE](./LICENSE).

This folder is a complete, pinned copy of the upstream repository (184 original files). It keeps the upstream directories, documentation, templates, scripts, and plugin metadata intact. The imported copy has not been run or activated. It does not automatically update when the upstream changes.

## Which skills are ready to use?

- `skills/engineering/`: 20 main engineering skills, for defining work, bugs, tests, architecture, code review, research, and implementation.
- `skills/productivity/`: 7 main skills, for interviewing, teaching, plain-language explanation, and handoffs.
- `skills/in-progress/`: experimental work. Read and review before relying on it.
- `skills/misc/`: miscellaneous utilities. Check scripts and prerequisites before use.
- `docs/`: deeper explanations of how the main workflows operate.

The public README is the most useful overview: [README.md](./README.md).

## How to use this saved copy

These are instruction files, not executable agents or trained models. Your coding agent must be able to read the skill files in its working environment. Keeping a copy in the GitHub library does not automatically add slash commands in ChatGPT, Codex or Claude.

**Reference the saved file directly** when your agent can read this repository:

```text
Use hayalows/Skills/collections/matt-pocock-skills/skills/engineering/diagnosing-bugs/SKILL.md.
Read its linked supporting files. Reproduce the bug, write a regression test,
fix the cause, run tests, and report exactly what passed and what remains unverified.
```

**Install the maintained upstream plugin** for built-in skill discovery and slash commands, if supported by your tool:

Codex:

```bash
codex plugin marketplace add mattpocock/skills
codex plugin add mattpocock-skills@mattpocock
```

Claude Code:

```bash
claude plugin install mattpocock-skills@claude-plugins-official
```

Or use the author's editable-install option in the upstream README. Install once per agent, not simultaneously through several methods. The upstream plugin updates separately from this archived copy.

For a project, the original author recommends running `/setup-matt-pocock-skills` once. Pick the issue tracker, triage labels and document directory. This requires the skill to be installed in that coding environment.

## Practical workflows

### Portfolio (hayalows/hayawebsite)

1. `improve-codebase-architecture`: study component structure and identify expensive coupling.
2. `diagnosing-bugs`: reproduce a mobile layout, animation or interaction bug.
3. `tdd`: write a failing test and implement a narrow fix.
4. `code-review`: independently check coding standards and the requested behavior.
5. `pr`: document the change, proof and merge risk.

### Learning Room

Use `grill-with-docs` to agree on discovery and recommendation behavior, `to-spec` and `to-tickets` to break it into small changes, `implement` to build with checks, and `retro` to identify recurring reliability problems.

### RouteLab or Muse

Use `domain-modeling` for terms such as route, waypoint, ETA and stop. Use `prototype` for alternate itinerary interactions and `diagnosing-bugs` for microphone or map issues. Compare route calculation outputs against known cases before accepting any improvement.

### StigmaClear

Use `research` for source-led technical investigation, `tdd` for search regression cases and `code-review` before publishing. These skills do not replace domain expert review or product-specific safety evaluation.

## Rules for careful use

- Start with a single relevant skill, rather than telling the agent to run all of them.
- Read a skill's dependencies and linked templates. Some workflows expect multiple agents, a browser or a configured issue tracker.
- Never treat a proposed change as a tested fix without a red-to-green test or equivalent evidence.
- Do not execute downloaded scripts without first inspecting them and confirming the project scope.
- Keep credentials out of logs and commits. Use a secure secret manager or environment variables.
- Keep changes in a branch until tests and reviews have passed.
- Revisit the upstream repository for changes; this snapshot remains fixed until deliberately updated.

## Useful first prompt

```text
For my portfolio repository, read Matt Pocock's diagnosing-bugs and tdd skills
from my Skills collection. Inspect the project without making changes first.
List reproducible issues and rank them. Then fix one issue at a time with a
regression test. Report files changed, commands run, results and open risks.
```
