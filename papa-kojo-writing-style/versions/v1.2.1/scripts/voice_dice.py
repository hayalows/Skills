#!/usr/bin/env python3
"""Optional prompt-aware writing approaches. Ideas, not permission to add facts.

Usage: python3 scripts/voice_dice.py --format linkedin --topic 'small spending'
       python3 scripts/voice_dice.py --format essay --seed 7 --json
No dependencies; defaults preserve the v1.1 plain-text CLI.
"""
import argparse
import json
import random

FORMATS = ("linkedin", "reflective", "caption", "essay", "video", "church", "brand",
           "email", "whatsapp", "comment", "application", "rewrite")
SKIP = {"email", "whatsapp", "comment", "application", "rewrite"}
ENTRY = [
    "Open with a specific fact already provided in the brief",
    "Start with the result, then explain its cause",
    "Start with an ordinary object that is already relevant to the topic",
    "Open with a sincere question and leave room to think",
    "Begin in the middle of a real explanation, without an announced hook",
    "Open with an honest limit or doubt, only if the brief supports it",
]
SHAPE = [
    "Explain a cause, its effect and the next reasonable step",
    "Take one small example and follow its real consequence",
    "Answer first, then give the strongest reason and a useful example",
    "Work through a genuine question and allow a partial answer",
    "Start with a fact, explain a complication, and return to the fact",
]
RHYTHM = [
    "Mostly connected medium sentences, with a natural short one",
    "Start briefly and let later sentences carry the explanation",
    "Mix a longer thought with a short sentence when it feels spoken",
    "Write steadily; vary length only when the meaning calls for it",
]
ENDING = [
    "End when the explanation has done its job",
    "Finish with one next step that follows from the idea",
    "Return to the first fact if it adds meaning",
    "Leave an honest question open if the point is unresolved",
    "End with one relevant image already grounded in the brief",
]
DOMAIN = {
    "money and payments": ("money", "cedi", "momo", "budget", "saving", "spend", "payment", "fare", "price", "finance", "market"),
    "school and learning": ("school", "learn", "exam", "study", "teach", "student", "class", "university"),
    "church and service": ("church", "faith", "serve", "service", "sunday", "scripture", "prayer"),
    "work and teams": ("work", "job", "office", "team", "boss", "career", "role", "interview"),
    "phone and technology": ("phone", "ai", "internet", "software", "app", "website", "code", "tech"),
    "home and family": ("home", "family", "wife", "marriage", "parent", "child", "anniversary"),
    "roads and transport": ("road", "trotro", "traffic", "bus", "car", "travel", "driver"),
    "football and sport": ("football", "sport", "match", "goal", "league", "coach"),
}
ALIASES = {"market": "money and payments", "money": "money and payments", "football": "football and sport",
           "school": "school and learning", "family": "home and family", "tech": "phone and technology",
           "work": "work and teams", "road": "roads and transport", "church": "church and service"}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--format", choices=FORMATS, default="reflective")
    p.add_argument("--topic", default="", help="Topic for selecting relevant images, never a source of facts")
    p.add_argument("--domains", default="", help="Optional comma-separated relevant domains")
    p.add_argument("--seed", type=int, help="Repeatable suggestions for testing")
    p.add_argument("--quote", action="store_true", help="A real quotation exists in the brief; never invent one")
    p.add_argument("--json", action="store_true", help="Machine-readable output")
    a = p.parse_args()
    r = random.Random(a.seed)
    if a.format in SKIP:
        result = {"mode": "skip", "format": a.format,
                  "reason": "Use the reader, facts and purpose to choose this format's structure."}
    else:
        matches = set()
        brief = a.topic.lower()
        for name, keywords in DOMAIN.items():
            if any(k in brief.split() or (len(k) >= 5 and k in brief) for k in keywords):
                matches.add(name)
        if a.domains:
            requested = {ALIASES.get(x.strip().lower(), x.strip().lower()) for x in a.domains.split(",") if x.strip()}
            matches = {x for x in requested if x in DOMAIN}
        # Even a relevant analogy may be unnecessary. Never select an unrelated one.
        picture = r.choice(["none", "none", *sorted(matches)])
        result = {"mode": "suggestions", "format": a.format,
                  "entry": r.choice(ENTRY + (["Open with the exact supplied quotation, only if it helps"] if a.quote else [])),
                  "shape": r.choice(SHAPE), "picture": picture,
                  "rhythm": r.choice(RHYTHM), "ending": r.choice(ENDING),
                  "note": "Suggestions only. Ignore any choice that weakens the brief; never invent a fact, quote, feeling or scene."}
    if a.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print("SKIP: " + result["reason"] if result["mode"] == "skip" else
              "\n".join(f"{key.title()}: {value}" for key, value in result.items() if key not in {"mode", "format"}))


if __name__ == "__main__":
    main()
