#!/usr/bin/env python3
"""Mechanical audit for the archived Cloudflare A/B results.

No inference is made by this script. It recomputes counts, usage, and
closure no-response decisions. Manual quality grades are separately
identified as non-blind and non-random.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
GROUPS = ("outreach", "continuation", "closure", "followup", "policy", "safetyrecords")
STRONG = ("strong-70b-pilot-transcribed", "strong-70b-batch1", "strong-70b-batch2")
VERSIONS = ("v11", "v12")


def load(stem):
    return json.loads((HERE / f"{stem}.json").read_text(encoding="utf-8"))


def failed(row):
    error = row.get("error")
    return bool(error) if not isinstance(error, list) else bool(error)


def report():
    small = [item for group in GROUPS for item in load(group)["cases"]]
    assert len(small) == 120, f"Expected 120 8B responses, got {len(small)}"
    assert len({(r["id"], r["variant"]) for r in small}) == 120, "Duplicate small-model case"
    assert set(r["variant"] for r in small) == set(VERSIONS)
    assert not [r for r in small if failed(r)], "Failed 8B requests"

    strong = [item for stem in STRONG for item in load(stem)["cases"]]
    assert len(strong) == 22, f"Expected 22 70B responses, got {len(strong)}"
    assert len({(r["case_id"], r["variant"]) for r in strong}) == 22, "Duplicate strong-model case"
    assert not [r for r in strong if failed(r)], "Failed 70B requests"

    closure = [r for r in load("closure")["cases"] if r["gold"] in ("no_reply", "close")]
    no_reply = {}
    for version in VERSIONS:
        rows = [r for r in closure if r["variant"] == version]
        no_reply[version] = {
            "correct": sum(not str((r.get("answer") or {}).get("student_text", "")).strip() for r in rows),
            "total": len(rows),
        }

    audit = load("manual-audit")
    grade_totals = {
        version: sum(float(x[version]) for x in audit["rows"]) for version in VERSIONS
    }
    assert len(audit["rows"]) == 11

    return {
        "small_model": {"cases": 60, "responses": len(small), "neurons": round(sum(r["usage"]["neurons"] for r in small), 2)},
        "strong_model": {"cases": 11, "responses": len(strong), "neurons": round(sum(r["usage"]["neurons"] for r in strong), 2)},
        "recorded_neurons_total": round(sum(r["usage"]["neurons"] for r in small + strong), 2),
        "closure_no_response_only": no_reply,
        "70b_manual_nonblind_stress_scores": grade_totals,
        "cautions": [
            "Non-blind human judgment, not independent adjudication",
            "Hand-picked strong-model stress cases, not representative sampling",
            "External responses only, not live mentoring or policy verification",
            "Cloudflare account billing and unarchived unsuccessful batch attempts are not measured",
        ],
    }


if __name__ == "__main__":
    print(json.dumps(report(), indent=2))
