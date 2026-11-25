# AI Ops Team (Google ADK 2.x + Gemini 4 Neon)

## What It Solves
Turns messy weekly/daily inputs (notes, links, local files) into a verified, **<1-page** deliverable using a 4-agent ADK 2.x graph (`Lead` → parallel `ScoutWeb` + `ScoutFiles` → `JoinNode` → `Scribe` → `Checker` loop capped at 2 rounds → Human-in-the-Loop `Approve`).

## Install in 3 Steps
1. `cd C:\Users\USER\.gemini\antigravity\scratch\ai-ops-team`
2. `pip install -r requirements.txt`
3. Set your environment variable when ready for live runs:
   - PowerShell: `$env:GEMINI_API_KEY="your-key-here"`

## Run in 1 Command
- **Offline graph verification (no API key needed):**
  `python main.py --dry-run "Summarize our Q4 launch priorities"`
- **Live run on `gemini-4-neon`:**
  `python main.py "Summarize our Q4 launch priorities"`
- **Weekly improvement loop:**
  `python main.py --weekly-review`
