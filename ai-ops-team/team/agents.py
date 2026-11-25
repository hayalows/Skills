"""Agent definitions and local tools for the AI Ops Team."""

from __future__ import annotations

from pathlib import Path
from google.adk import Agent

MODEL_ID = "gemini-4-neon"
PROJECT_ROOT = Path(__file__).resolve().parent.parent
MEMORY_PATH = PROJECT_ROOT / "team_memory.md"


def read_team_memory() -> str:
    """Read team_memory.md before every run."""
    if MEMORY_PATH.exists():
        return MEMORY_PATH.read_text(encoding="utf-8")
    return "No team memory found."


def read_local_files(paths_csv: str) -> str:
    """Read local workspace files for ScoutFiles."""
    results: list[str] = []
    for raw in [p.strip() for p in paths_csv.split(",") if p.strip()]:
        p = Path(raw)
        if not p.is_absolute():
            p = PROJECT_ROOT / p
        if p.exists() and p.is_file():
            content = p.read_text(encoding="utf-8", errors="replace")[:4000]
            results.append(f"FILE: {p}\n{content}")
        else:
            results.append(f"MISSING: {p}")
    return "\n\n".join(results) if results else "No local file paths provided."


def build_agents() -> dict[str, Agent]:
    """Create the 4 specialized Gemini 4 Neon agents."""
    lead = Agent(
        name="lead",
        model=MODEL_ID,
        description="Orchestrates the team, reads team_memory.md, and manages user approval.",
        instruction=(
            "JOB: Route the user's request, enforce if/then rules, manage team memory, "
            "and pause for final user approval.\n"
            "INPUT: User raw request + team_memory.md.\n"
            "OUTPUT: Clear task brief and acceptance criteria for Scout and Scribe.\n"
            "DONE WELL: Reads team_memory.md first; sets clear criteria; logs every run.\n"
            "NEVER: Never research facts, draft final prose, or publish without user approval."
        ),
        tools=[read_team_memory],
        output_key="lead_brief",
    )

    scout_web = Agent(
        name="scout_web",
        model=MODEL_ID,
        description="Gathers external facts and references for the Fact Brief.",
        instruction=(
            "JOB: Gather and verify external facts for the Lead's brief.\n"
            "INPUT: Lead's task brief.\n"
            "OUTPUT: Cited bulleted web facts with explicit gaps.\n"
            "DONE WELL: Every claim has a source; zero filler or speculation.\n"
            "NEVER: Never write final prose or invent URLs/numbers."
        ),
        output_key="web_facts",
    )

    scout_files = Agent(
        name="scout_files",
        model=MODEL_ID,
        description="Reads local workspace files and extracts cited facts.",
        instruction=(
            "JOB: Read local files referenced in the brief using read_local_files.\n"
            "INPUT: Lead's task brief + local file paths.\n"
            "OUTPUT: Cited local file facts with exact paths and gaps.\n"
            "DONE WELL: Every claim cites a verified file path; zero filler.\n"
            "NEVER: Never invent file contents or write final prose."
        ),
        tools=[read_local_files],
        output_key="file_facts",
    )

    scribe = Agent(
        name="scribe",
        model=MODEL_ID,
        description="Synthesizes the Fact Brief into a crisp <1-page Markdown deliverable.",
        instruction=(
            "JOB: Turn Lead's brief + Scout's Fact Brief (+ Checker fixes if any) "
            "into a crisp, actionable <1-page Markdown deliverable (~300-500 words).\n"
            "DONE WELL: Leads with the key takeaway; zero fluff; preserves all citations.\n"
            "NEVER: Never invent facts not in the Fact Brief; never drop citations."
        ),
        output_key="draft",
    )

    checker = Agent(
        name="checker",
        model=MODEL_ID,
        description="Scores the draft against Done Well criteria and outputs exact fixes.",
        instruction=(
            "JOB: Score Scribe's draft (0-10) against the Done Well checklist.\n"
            "OUTPUT: Return JSON with keys: pass (bool), score (int), "
            "target_agent ('scout'|'scribe'|'none'), fixes (list[str]).\n"
            "DONE WELL: Verifies every claim against Fact Brief; confirms <1 page & zero fluff.\n"
            "NEVER: Never rewrite the draft yourself; never pass unverified claims."
        ),
        output_key="scorecard",
    )

    return {
        "lead": lead,
        "scout_web": scout_web,
        "scout_files": scout_files,
        "scribe": scribe,
        "checker": checker,
    }
