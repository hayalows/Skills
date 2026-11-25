---
name: ai-ops-team
description: >-
  4-agent AI Ops Team (Lead, Scout, Scribe, Checker) wired as a Google ADK 2.x
  graph with parallel research, a 2-round quality loop, human-in-the-loop
  approval, and weekly improvement.
---

# AI Ops Team Skill

Turns messy inputs (notes, links, local files) into a verified, `<1-page` deliverable using a 4-agent team (`Lead` -> parallel `ScoutWeb` + `ScoutFiles` -> `Join` -> `Scribe` -> `Checker` loop capped at 2 rounds -> `Approve` HITL pause).

## Team Agents (in `agents/`)
- [Lead](agents/lead.md) — Routes tasks, reads `team_memory.md`, logs runs, and pauses for user approval.
- [Scout](agents/scout.md) — Runs web search and local file reads in parallel; returns a cited Fact Brief.
- [Scribe](agents/scribe.md) — Synthesizes the Fact Brief into a `<1-page` Markdown deliverable.
- [Checker](agents/checker.md) — Scores every draft (`0-10`) and sends exact fixes back (max 2 rounds).

## Run Inside Antigravity
1. Read `team_memory.md` first.
2. Execute the graph: `Lead` -> parallel `Scout` (`ScoutWeb` + `ScoutFiles`) -> `Scribe` -> `Checker` (max 2 rounds) -> pause for user `"yes"`.

## Run Outside Antigravity (Python ADK 2.x)
```powershell
python main.py --dry-run "Summarize our AI Ops Team setup"
python main.py "Your live task"   # requires GEMINI_API_KEY
python main.py --weekly-review
```
