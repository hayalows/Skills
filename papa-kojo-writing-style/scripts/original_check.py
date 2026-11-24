#!/usr/bin/env python3
"""Original checker (v3.0): register-aware editing prompts for Papa Kojo drafts.

Usage:
  python3 scripts/original_check.py --register post < draft.txt
  python3 scripts/original_check.py --register chat --json < draft.txt

Registers: chat, comment, message, post, longform, formal.
Every flag means "look again". Nothing here detects AI authorship or proves a
voice match. Meaning and truth come first. No third-party dependencies.
"""
import argparse
import json
import re
import statistics
import sys

VERSION = "3.0.1"
REGISTERS = ("chat", "comment", "message", "post", "longform", "formal")
CASUAL = {"chat", "comment"}
LONGER = {"post", "longform"}

AVOID = ("ensure", "crucial", "nestled", "uncover", "journey", "embark", "unleash", "dive", "delve",
         "discover", "plethora", "indulge", "more than just", "not just", "unlock", "unveil",
         "look no further", "world of", "realm", "whether you're", "whether you’re", "landscape",
         "navigate", "daunting", "both style", "tapestry", "unique blend", "blend", "enhancing",
         "game changer", "stand out", "stark", "contrast", "leverage", "foster", "transformative",
         "i learnt that", "this is not just about")

PATTERNS = [
    ("contrast_flip",
     r"\b(?:it|this|that|they|he|she|we|you|money|income|success)(?:'s|’s| is| are| was)\s+not\s+[^.?!;]{1,60}[.;]\s*(?:it|this|that|they|he|she|we|you)(?:'s|’s| is| are| was)\b"
     r"|\b(?:don['’]t|do not|doesn['’]t|does not|didn['’]t|did not)\s+(?:just\s+)?\w+[^.?!;]{0,60}[.;]\s*(?:they|we|you|it)\s+\w+"
     r"|\bnot only\b[^.?!]*\bbut\b|\bnot because\b[^.?!]*\bbut because\b|\b(?:isn['’]t|is not|wasn['’]t) about\b"
     r"|\b(?:don['’]t|do not) just\b[^.?!;]{1,40}[;,]\s*we\b"
     r"|\bgives? you [^.?!]{1,40}\.\s*it (?:does not|doesn['’]t)\b"
     r"|[.!]\s+(?:it|this|that)(?:['’]s| is) (?:just|only|simply) (?:stuck|about|that|a matter)\b"
     r"|\bonly tells you\b[^.?!]{1,60}[.]\s*it (?:does not|doesn['’]t) tell you\b",
     "Say the true claim directly and give its reason, without the set-up and reversal."),
    ("label_before_point",
     r"\b(?:here['’]s the thing|here is the thing|the key is|the secret is|the truth is|here['’]s why|here is why|"
     r"the reason is (?:often )?simple|what \w+ can do is|let that sink in|bottom line|the lesson\??|the takeaway|"
     r"the real (?:\w+ )?(?:problem|issue|question) is|this matters because|at its core)\b",
     "Delete the label and start with the point."),
    ("sweeping_opener",
     r"(?:^|\n\s*)(?:most people|many people|we all|everyone|in today['’]s|in a world where|have you ever)\b",
     "Open on this reader's real situation or a fact from the brief."),
    ("moral_closer",
     r"(?:and that['’]s okay|and that is okay|(?:that|this) is what (?:\w+ ){1,3}(?:is|means|looks like)|"
     r"small steps (?:lead|add)|one step at a time|the rest will follow|that['’]s the (?:real )?(?:lesson|point)|"
     r"that is the (?:real )?(?:lesson|point))",
     "Stop at the last useful sentence, or end with a plain next step."),
    ("signpost",
     r"\b(?:in summary|in conclusion|to sum up|ultimately,|overall,|at the end of the day|it is worth noting|"
     r"it['’]s worth noting|it is important to note|let['’]s (?:dive|explore|break down|unpack))\b",
     "Cut the signpost; the next sentence can stand alone."),
    ("puffed_importance",
     r"\b(?:plays? a (?:vital|crucial|pivotal|key) role|a testament to|stands as|serves as|boasts|"
     r"cutting-edge|dynamic|robust|seamless(?:ly)?|empower(?:s|ing|ed)?|elevate|vibrant|pivotal|profound)\b",
     "Say the plain fact, with 'is' and 'has' where they fit."),
    ("vague_authority",
     r"\b(?:experts (?:say|agree|believe)|studies (?:show|suggest)|research (?:shows|proves)|it is (?:widely )?(?:known|believed))\b",
     "Name the source from the brief, or drop the claim."),
    ("proof_signpost",
     r"\b(?:that['’]s a number i can point to|this shows the power of|this proves that|which speaks volumes)\b",
     "Let the fact stand on its own."),
    ("ing_tail",
     r",\s+(?:highlighting|underscoring|showcasing|demonstrating|reflecting|emphasizing|emphasising)\b",
     "Cut the tail or make it a new sentence with a real subject."),
    ("sales_template",
     r"(?:^|\n\s*)(?:still \w+ing\b[^?]*\?|tired of\b[^?]*\?|ready to\b[^?]*\?|imagine (?:a world|if)\b)",
     "Describe the reader's real problem plainly instead of a template question."),
]


def words(text):
    return re.findall(r"[A-Za-z]+(?:['’][A-Za-z]+)?", text)


def sentences(text):
    masked = re.sub(r"(?<=\d)\.(?=\d)", "∯", text.strip())
    masked = re.sub(r"\b(Mr|Mrs|Ms|Dr|Prof|St)\.", r"\1∯", masked, flags=re.I)
    parts = re.split(r"(?<=[.!?])\s+|\n+", masked)
    return [s.replace("∯", ".").strip() for s in parts if re.search(r"[A-Za-z]", s)]


def syllables(word):
    word = word.lower().strip("'’")
    if len(word) <= 3:
        return 1
    word = re.sub(r"(?:[^laeiouy]es|ed|[^laeiouy]e)$", "", word)
    word = re.sub(r"^y", "", word)
    return max(1, len(re.findall(r"[aeiouy]{1,2}", word)))


COMPOSITION_FLAGS = {'rule_of_three', 'parallel_overuse', 'opening_repetition'}

# These are review candidates, not judgments about meaning.
INTRO = re.compile(r"^(?:(?:and|but|so)\s+)?(?:if|when|while|although|though|because|since|before|after|unless|once|as|even if|for example|for instance|of course|however|instead|in fact|by the time)\b", re.I)
LINK = re.compile(r"^(?:but|because|so|yet|although|though|if|when|while|since|unless|as|before|after|which|who|where|with|rather than)\b", re.I)
JOIN = re.compile(r"\b(?:and|or)\b", re.I)


def composition_candidates(ss):
    """Find surface patterns; leave the necessity of each item to the editor."""
    candidates = []
    for i, sentence in enumerate(ss, 1):
        # Ignore thousands separators and explicit quoted/code material.
        masked = re.sub(r"(?<=\d),(?=\d)", "", sentence)
        if re.search(r'[`"“”]', masked):
            continue
        parts = [p.strip() for p in masked.strip(".!?; ").split(",")]
        if len(parts) < 2 or not all(parts) or INTRO.match(parts[0]):
            continue
        if any(LINK.match(p) for p in parts[1:]):
            continue
        # Oxford comma or a list with no comma before the last conjunction.
        last = parts[-1]
        if JOIN.match(last):
            items = parts[:-1] + [JOIN.sub("", last, count=1).strip()]
        else:
            joins = list(JOIN.finditer(last))
            if len(joins) != 1:
                continue
            j = joins[0]
            items = parts[:-1] + [last[:j.start()].strip(), last[j.end():].strip()]
        if len(items) < 3 or any(not p or not re.search(r"[A-Za-z]", p) for p in items):
            continue
        if any(JOIN.match(p) or LINK.match(p) or INTRO.match(p) for p in items[1:]):
            continue
        candidates.append((i, sentence))
    return candidates


def composition_review(ss):
    flags = []
    candidates = composition_candidates(ss)
    for i, sentence in candidates:
        flags.append(("rule_of_three", sentence, f"Sentence {i}: review each coordinated item. Keep necessary lists; develop one detail or remove padding if the rhythm drove the choice."))
    if len(candidates) >= 2:
        flags.append(("parallel_overuse", "; ".join(str(i) for i, _ in candidates), "Several sentences use lists of three or more. Check the overall rhythm; keep only independently useful items."))
    # Adjacent repeated two-word openings: one common word alone is not evidence.
    openings = [tuple(re.findall(r"[A-Za-z]+(?:['’][A-Za-z]+)?", s.lower())[:2]) for s in ss]
    for i in range(2, len(openings)):
        if len(openings[i]) == 2 and openings[i] == openings[i-1] == openings[i-2]:
            flags.append(("opening_repetition", " / ".join(ss[i-2:i+1]), "Three adjacent sentences share an opening. Check for a rhetorical template; retain intentional repetition if it serves the meaning."))
            break
    return flags



def scan(text, register):
    ws = words(text)
    ss = sentences(text)
    lens = [len(words(s)) for s in ss]
    paras = [p for p in re.split(r"\n\s*\n", text.strip()) if p.strip()]
    nw, ns = len(ws), len(ss)
    sy = sum(syllables(w) for w in ws)
    ease = round(206.835 - 1.015 * nw / ns - 84.6 * sy / nw, 1) if nw and ns else None
    grade = round(0.39 * nw / ns + 11.8 * sy / nw - 15.59, 1) if nw and ns else None
    cv = round(statistics.pstdev(lens) / statistics.mean(lens), 2) if len(lens) > 2 and statistics.mean(lens) else None
    metrics = {"words": nw, "sentences": ns, "paragraphs": len(paras),
               "avg_sentence_words": round(nw / ns, 1) if ns else None,
               "longest_sentence_words": max(lens, default=0),
               "sentence_variation": cv, "grade_estimate": grade, "reading_ease_estimate": ease}
    flags = []

    def add(fid, example, advice):
        flags.append({"id": fid, "example": example.strip()[:100], "advice": advice})

    low = text.lower()
    for term in AVOID:
        rx = r"(?<![A-Za-z])" + r"\s+".join(map(re.escape, term.split())) + r"(?![A-Za-z])"
        m = re.search(rx, low)
        if m:
            add("avoid_word", m.group(0), "He prefers other wording. Keep exact quotations and names.")
    if "—" in text or " – " in text:
        add("em_dash", "—", "Use a full stop, comma or colon instead.")
    for fid, rx, advice in PATTERNS:
        m = re.search(rx, text, flags=re.I | re.M)
        if m:
            add(fid, m.group(0), advice)

    contractions = re.findall(r"\b\w+['’](?:re|ve|ll|d|t|m)\b|\b(?:it|that|there|what|here|let|he|she|who)['’]s\b", text, re.I)
    if register == "formal" and contractions:
        add("register_contractions", ", ".join(contractions[:5]), "Formal register uses full forms.")
    emoji = re.findall(r"[\U0001F300-\U0001FAFF☀-➿]", text)
    if emoji and register not in CASUAL:
        add("register_emoji", "".join(emoji[:3]), "Emoji usually belong in Chat and Comment only.")
    if text.count("!") > (2 if register in CASUAL else 0):
        add("register_exclamation", "!", "Keep exclamation marks for real excitement in casual writing.")
    if register in {"message", "formal", "longform"}:
        frag = [s for s in ss if len(words(s)) <= 2 and not re.match(r"^(thanks|thank you|best|regards|cheers|hi|hello|dear)\b", s, re.I)]
        if len(frag) >= 2:
            add("register_fragments", " | ".join(frag[:3]), "Join short fragments into full sentences in this register.")
    run = longest = 0
    for n in lens:
        run = run + 1 if n < 8 else 0
        longest = max(longest, run)
    if register in LONGER | {"message"} and longest >= 5:
        add("too_fast", f"{longest} short sentences in a row", "Join related ideas with 'and', 'so' or 'because'; give reasons next to instructions.")
    if register in LONGER and nw >= 120 and cv is not None and cv < 0.3:
        add("too_even", f"sentence variation {cv}", "Let length follow the thought; read aloud before changing anything.")
    if register in LONGER and len(paras) >= 4:
        plen = [len(words(p)) for p in paras]
        if statistics.mean(plen) and statistics.pstdev(plen) / statistics.mean(plen) < 0.15:
            add("too_even_paragraphs", str(plen), "Paragraphs need not match; let a short point have a short paragraph.")
    for fid, example, advice in composition_review(ss):
        add(fid, example, advice)
    if register in LONGER and paras and paras[-1].rstrip().endswith("?"):
        add("question_ending", paras[-1][-80:], "End on the useful line or a next step unless he wants answers.")
    if register in LONGER and nw >= 80 and grade is not None and grade > 8:
        add("hard_words", f"grade about {grade}", "Swap long words for common ones where no meaning is lost.")
    presence = bool(re.search(r"\b(?:i|i['’]m|i['’]ve|my|we|our)\b", low)) or bool(re.search(r"\byou\b", low))
    if register in LONGER and nw >= 80 and not presence:
        add("no_person", "no 'I', 'we' or 'you'", "Check there is a person on the page: a stance, a detail, care or a limit.")
    return {"checker": "original", "version": VERSION, "register": register, "metrics": metrics, "flags": flags,
            "notice": "Flags are prompts to look again, not proof of AI writing or of his voice."}


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--register", choices=REGISTERS, default="post")
    p.add_argument("--json", action="store_true")
    p.add_argument("--composition-gate", action="store_true", help="Exit 2 if composition review candidates are present; necessary lists may remain after editorial review.")
    a = p.parse_args()
    data = scan(sys.stdin.read(), a.register)
    exit_status = 2 if a.composition_gate and any(f["id"] in COMPOSITION_FLAGS for f in data["flags"]) else 0
    if a.json:
        print(json.dumps(data, indent=2, ensure_ascii=False))
        return exit_status
    m = data["metrics"]
    print(f"ORIGINAL CHECK {VERSION} | register: {a.register}")
    print(f"Words {m['words']} | sentences {m['sentences']} | paragraphs {m['paragraphs']} | "
          f"average {m['avg_sentence_words']} | grade about {m['grade_estimate']} | ease {m['reading_ease_estimate']}")
    if not data["flags"]:
        print("Nothing flagged. Now read it aloud as him, to this reader.")
    for f in data["flags"]:
        print(f"- {f['id']}: {f['example']}  ->  {f['advice']}")
    print(data["notice"])
    return exit_status


if __name__ == "__main__":
    sys.exit(main())
