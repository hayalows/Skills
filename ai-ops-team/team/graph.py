"""ADK 2.x Graph Workflow for the AI Ops Team (no deprecated Sequential/Parallel/LoopAgent)."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from google.adk import Workflow
from google.adk.workflow import JoinNode, START

from team.agents import PROJECT_ROOT, build_agents

RUNS_LOG_PATH = PROJECT_ROOT / "logs" / "runs.jsonl"
MAX_QUALITY_ROUNDS = 2


def log_run(record: dict[str, Any]) -> None:
    """Append a structured run record to logs/runs.jsonl."""
    RUNS_LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        **record,
    }
    with RUNS_LOG_PATH.open("a", encoding="utf-8") as f:
        f.write(json.dumps(payload) + "\n")


def join_facts(node_input: dict[str, Any]) -> str:
    """JoinNode downstream combiner for parallel ScoutWeb + ScoutFiles outputs."""
    web = node_input.get("scout_web", "")
    files = node_input.get("scout_files", "")
    return f"## Cited Fact Brief\n\n### Web Facts\n{web}\n\n### Local File Facts\n{files}"


def quality_router(node_input: Any) -> str:
    """Route Checker output: pass -> approve, fail (<2 rounds) -> retry, else escalate."""
    # Expecting JSON or dict with pass, round, target_agent
    data: dict[str, Any] = {}
    if isinstance(node_input, dict):
        data = node_input
    elif isinstance(node_input, str):
        try:
            data = json.loads(node_input)
        except json.JSONDecodeError:
            data = {"pass": False, "score": 0, "target_agent": "scribe", "fixes": [node_input]}

    passed = bool(data.get("pass", False))
    rounds = int(data.get("round", 1))
    target = str(data.get("target_agent", "scribe")).lower()

    if passed:
        return "approve"
    if rounds < MAX_QUALITY_ROUNDS:
        return "retry_scout" if target == "scout" else "retry_scribe"
    return "escalate"


def hitl_approve(node_input: Any) -> dict[str, Any]:
    """Human-in-the-loop pause point before any deliverable leaves."""
    return {
        "status": "AWAITING_USER_APPROVAL",
        "deliverable": node_input,
        "message": "Paused at Approve node. Reply 'yes' to approve and save/send.",
    }


def escalate_to_lead(node_input: Any) -> dict[str, Any]:
    """Escalate to Lead & User after 2 failed quality rounds."""
    return {
        "status": "ESCALATED_AFTER_2_ROUNDS",
        "details": node_input,
        "message": "Checker failed after 2 rounds. Returning to Lead/User with remaining issues.",
    }


def build_workflow() -> Workflow:
    """Compile the ADK 2.x graph workflow with parallel fan-out, JoinNode, loop, and HITL."""
    agents = build_agents()
    scout_join = JoinNode(name="scout_join")

    return Workflow(
        name="ai_ops_team_workflow",
        description="Lead -> parallel ScoutWeb/ScoutFiles -> Join -> Scribe -> Checker (max 2) -> HITL Approve",
        edges=[
            (START, agents["lead"]),
            # Parallel fan-out from Lead to ScoutWeb and ScoutFiles
            (agents["lead"], (agents["scout_web"], agents["scout_files"])),
            # Fan-in to JoinNode
            (agents["scout_web"], scout_join),
            (agents["scout_files"], scout_join),
            # Combined Fact Brief -> Scribe -> Checker
            (scout_join, join_facts),
            (join_facts, agents["scribe"]),
            (agents["scribe"], agents["checker"]),
            # Quality loop & HITL routing
            (agents["checker"], quality_router),
            (
                quality_router,
                {
                    "approve": hitl_approve,
                    "retry_scribe": agents["scribe"],
                    "retry_scout": agents["scout_web"],
                    "escalate": escalate_to_lead,
                },
            ),
        ],
    )
