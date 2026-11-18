#!/usr/bin/env python3
"""Advisory voice checks. Checks signals, not authorship or personal authenticity.

Usage: python3 scripts/voice_check.py --format reflective < draft.txt
       python3 scripts/voice_check.py --format comment --json < draft.txt
No third-party dependencies. The author decides which advice applies.
"""
import argparse
import json
import re
import statistics
import sys

USER_AVOID = ("ensure", "crucial", "nestled", "uncover", "journey", "embark", "unleash", "dive",
              "delve", "discover", "plethora", "indulge", "more than just", "not just", "unlock",
              "unveil", "look no further", "world of", "realm", "whether you're", "landscape",
              "navigate", "daunting", "both style", "tapestry", "unique blend", "blend", "enhancing",
              "game changer", "stand out", "stark", "contrast")
WATCH_WORDS = ("additionally", "align with", "boasts", "bolster", "pivotal", "robust", "showcase",
               "testament", "underscore", "vibrant", "intricate", "meticulous", "seamless", "elevate",
               "empower", "resonate", "profound", "nuanced", "holistic", "quietly", "genuinely",
               "truly", "deeply", "powerful", "leverage", "foster", "transformative")
FORMATS = ("reflective", "linkedin", "caption", "essay", "video", "church", "brand", "application",
           "email", "whatsapp", "comment", "technical")
CASUAL = {"whatsapp", "comment"}
LONG = {"reflective", "linkedin", "essay", "video", "church", "brand"}


def syllables(word):
    word = word.lower().strip("'")
    if len(word) <= 3:
        return 1
    word = re.sub(r"(?:[^laeiouy]es|ed|[^laeiouy]e)$", "", word)
    word = re.sub(r"^y", "", word)
    return max(1, len(re.findall(r"[aeiouy]{1,2}", word)))


def sentences(text):
    # Hide decimal points and common honorifics before sentence splitting.
    masked = re.sub(r"(?<=\d)\.(?=\d)", "∯", text.strip())
    masked = re.sub(r"\b(Mr|Mrs|Ms|Dr|Prof|St)\.", r"\1∯", masked, flags=re.I)
    parts = re.split(r"(?<=[.!?])\s+|\n\s*\n", masked)
    return [s.replace("∯", ".").strip() for s in parts if re.search(r"[A-Za-z]", s)]


def scan(text, fmt):
    ws = re.findall(r"[A-Za-z]+(?:['’][A-Za-z]+)?", text)
    ss = sentences(text)
    lens = [len(re.findall(r"[A-Za-z]+(?:['’][A-Za-z]+)?", x)) for x in ss]
    nw = len(ws)
    ns = len(ss)
    sy = sum(syllables(w) for w in ws)
    avg = nw / ns if ns else None
    grade = (0.39 * nw / ns + 11.8 * sy / nw - 15.59) if ns and nw else None
    ease = (206.835 - 1.015 * nw / ns - 84.6 * sy / nw) if ns and nw else None
    metrics = {"words": nw, "sentences": ns, "avg_sentence_words": round(avg, 1) if avg is not None else None,
               "longest_sentence_words": max(lens, default=0),
               "sentence_length_spread": round(statistics.pstdev(lens), 1) if len(lens) > 1 else None,
               "fk_estimate": round(grade, 1) if grade is not None else None,
               "reading_ease_estimate": round(ease, 1) if ease is not None else None}
    flags = []

    def add(key, level, sample, advice):
        flags.append({"id": key, "level": level, "example": sample[:100], "advice": advice})

    def phrases(terms):
        for term in terms:
            rx = r"(?<![A-Za-z])" + r"\s+".join(map(re.escape, term.split())) + r"(?![A-Za-z])"
            m = re.search(rx, text, flags=re.I)
            if m:
                yield m.group(0)

    for phrase in phrases(USER_AVOID):
        add("user_avoid_word", "review", phrase, "User prefers other wording; preserve exact quotations and names.")
    for phrase in phrases(WATCH_WORDS):
        add("generic_word", "consider", phrase, "Check if this is the clearest word; do not replace a useful technical term.")
    if "—" in text:
        add("punctuation_em_dash", "review", "—", "User prefers no em dashes in newly written prose.")
    if "!" in text and fmt not in CASUAL:
        add("punctuation_exclamation", "consider", "!", "Check the reader and occasion before cutting emphasis.")
    # Specific clichés are more useful to flag than common neutral constructions.
    for key, rx, advice in [
        ("sweeping_opener", r"(?:^|\n\s*)(most people|we all|everyone knows|in a world where)\b",
         "Start with a supported observation about the actual subject."),
        ("label_reveal", r"\b(the secret is|the truth is|here's the thing|let that sink in|at its core)\b",
         "Remove the label if it contributes nothing."),
        ("negative_flip", r"\b(?:isn['’]t about|not because|rather than)\b|\bmost people\s+don['’]t\b[^.!?]*[.!?]\s*they\b",
         "Consider explaining the real cause directly, without a manufactured reversal."),
        ("stock_closer", r"\b(and that['’]s okay|the rest will follow|the feeling will catch up)\b",
         "Stop when the meaning is complete."),
        ("ing_tail", r",\s+(?:showing|highlighting|demonstrating|underscoring)\b",
         "Check whether the tail adds new information."),
    ]:
        m = re.search(rx, text, flags=re.I)
        if m:
            add(key, "consider", m.group(0), advice)
    if fmt in LONG and nw >= 80 and avg is not None and avg > 22:
        add("long_sentences", "consider", str(round(avg, 1)), "Consider splitting a dense thought where a person would pause.")
    if fmt in LONG and nw >= 80 and len(lens) >= 5 and statistics.pstdev(lens) < 2.0:
        add("even_rhythm", "consider", str(lens[:8]), "Read aloud; repetitive lengths may be intentional, so don't edit by number alone.")
    return {"format": fmt, "metrics": metrics, "flags": flags,
            "notice": "Readability is approximate. Flags are editing prompts, not proof of AI authorship or of Papa Kojo's voice."}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--format", choices=FORMATS, default="reflective")
    p.add_argument("--json", action="store_true")
    a = p.parse_args()
    data = scan(sys.stdin.read(), a.format)
    if a.json:
        print(json.dumps(data, indent=2, ensure_ascii=False))
        return
    m = data["metrics"]
    print(f"VOICE CHECK v1.2 | {a.format}")
    print(f"Words: {m['words']}  Sentences: {m['sentences']}  Mean length: {m['avg_sentence_words']}")
    print(f"Approx. grade: {m['fk_estimate']}  Reading ease: {m['reading_ease_estimate']}")
    if not data["flags"]:
        print("No selected style signals flagged. Read aloud and check the meaning.")
    else:
        for f in data["flags"]:
            print(f"[{f['level']}] {f['id']}: {f['example']} | {f['advice']}")
    print(data["notice"])


if __name__ == "__main__":
    main()
