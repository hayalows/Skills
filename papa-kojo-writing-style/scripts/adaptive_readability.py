#!/usr/bin/env python3
"""Advisory readability analysis for Original. No automatic rewriting."""
import argparse
from collections import Counter
import json
import math
from pathlib import Path
import re
import sys

VERSION = "1.0.0"
TARGETS = {"chat": (85, 100), "comment": (85, 100), "message": (80, 95),
           "post": (75, 90), "longform": (80, 95), "formal": (60, 80),
           "educational": (70, 90), "technical": (50, 75)}
WORD = re.compile(r"[^\W\d_]+(?:['’][^\W\d_]+)*", re.UNICODE)
NUMBER = re.compile(r"(?<!\w)[+-]?\d+(?:[,.]\d+)*(?:%|\b)")
ABBR = re.compile(r"\b(?:Mr|Mrs|Ms|Dr|Prof|St|Jr|Sr|vs|etc)\.", re.I)
SHORT = 100
PLAIN = {"utilise": "use", "utilize": "use", "commence": "start",
         "approximately": "about", "subsequently": "later", "prior": "before",
         "assistance": "help", "sufficient": "enough", "demonstrate": "show",
         "purchase": "buy", "individuals": "people", "additional": "extra"}
EXCEPTIONS = {"people": 2, "business": 2, "every": 2, "quiet": 2, "fire": 1,
              "our": 1, "one": 1, "once": 1, "queue": 1, "hour": 1,
              "money": 2, "science": 2, "technology": 4, "really": 2}


def tokens(text):
    return WORD.findall(text)


def sentences(text):
    text = re.sub(r"(?<=\d)\.(?=\d)", "\ue000", text.strip())
    text = ABBR.sub(lambda m: m[0][:-1] + "\ue000", text)
    text = re.sub(r"\b(?:[A-Za-z]\.){2,}", lambda m: m[0].replace(".", "\ue000"), text)
    return [s.replace("\ue000", ".").strip() for s in
            re.split(r"(?<=[.!?])\s+|\n\s*\n", text) if tokens(s)]


def counter_for(dictionary="heuristic"):
    lexicon = None
    if dictionary == "cmu":
        try:
            import cmudict
        except ImportError as exc:
            raise ValueError("CMU mode needs the optional cmudict package") from exc
        lexicon = cmudict.dict()

    def count(word):
        w = word.lower().replace("’", "'")
        if lexicon and w in lexicon:
            return sum(p[-1:].isdigit() for p in lexicon[w][0]) or 1
        if w in EXCEPTIONS:
            return EXCEPTIONS[w]
        w = re.sub(r"'(?:s|d|ll|re|ve|m|t)$", "", w)
        n = len(re.findall(r"[aeiouy]+", w))
        if w.endswith("e") and not re.search(r"[^aeiou]le$", w) and n > 1:
            n -= 1
        if w.endswith("ed") and not re.search(r"[td]ed$", w) and n > 1:
            n -= 1
        return max(1, n)
    return count


def metrics(ss, count, easy=None):
    ws = [w.lower() for s in ss for w in tokens(s)]
    n, k = len(ws), len(ss)
    result = {"words": n, "sentences": k, "ease_estimate": None, "grade_estimate": None,
              "smog_estimate": None, "dale_chall_estimate": None}
    if not n or not k:
        return result
    sy = [count(w) for w in ws]
    avg, ratio = n / k, sum(sy) / n
    poly = sum(x >= 3 for x in sy)
    result.update(ease_estimate=round(206.835 - 1.015 * avg - 84.6 * ratio, 1),
                  grade_estimate=round(.39 * avg + 11.8 * ratio - 15.59, 1),
                  average_sentence_words=round(avg, 1), syllables_per_word=round(ratio, 3),
                  polysyllables=poly)
    if k >= 30:
        result["smog_estimate"] = round(1.043 * math.sqrt(poly * 30 / k) + 3.1291, 1)
    if easy is not None:
        pct = 100 * sum(w not in easy for w in ws) / n
        result["unlisted_word_percent"] = round(pct, 1)
        # Caller must supply an appropriate Dale-Chall list including inflections.
        result["dale_chall_estimate"] = round(.1579 * pct + .0496 * avg + (3.6365 if pct > 5 else 0), 2)
    return result


def protected_pattern(terms):
    return re.compile(r"(?<!\w)(?:" + "|".join(re.escape(t) for t in sorted(set(terms), key=lambda x: (-len(x), x))) + r")(?!\w)") if terms else None


def analyze(text, profile="longform", protected=(), dictionary="heuristic", easy=None):
    ss = sentences(text)
    count = counter_for(dictionary)
    total = metrics(ss, count, easy)
    low, high = TARGETS[profile]
    short = total["words"] < SHORT or total["sentences"] < 5
    pat = protected_pattern(protected)
    hotspots = []
    for i, s in enumerate(ss, 1):
        free = pat.sub(" ", s) if pat else s
        terms = sorted(set(w.lower() for w in tokens(free) if count(w) >= 3 or w.lower() in PLAIN))
        if len(tokens(s)) > 23 or terms:
            hotspots.append({"sentence": i, "text": s, "words": len(tokens(s)),
                             "review_words": terms, "plain_options": {w: PLAIN[w] for w in terms if w in PLAIN}})
    windows = []
    for start in range(0, len(ss), 5):
        chunk = ss[start:start + 10]
        m = metrics(chunk, count, easy)
        if m["words"] >= SHORT and len(chunk) >= 5:
            windows.append({"start_sentence": start + 1, "end_sentence": start + len(chunk), **m})
        if start + 10 >= len(ss):
            break
    paragraphs = []
    for i, p in enumerate(re.split(r"\n\s*\n", text.strip()), 1):
        m = metrics(sentences(p), count, easy)
        if m["words"]:
            paragraphs.append({"paragraph": i, **m, "short_sample": m["words"] < SHORT or m["sentences"] < 5})
    # A separate lexical diagnostic; never exclude names from the published raw score.
    free_words = tokens(pat.sub(" ", text) if pat else text)
    free_ratio = round(sum(count(w) for w in free_words) / len(free_words), 3) if free_words else None
    return {"version": VERSION, "profile": profile, "dictionary": dictionary,
            "target_ease": [low, high], "short_sample": short, "metrics": total,
            "target_status": "review_manually" if short else ("below_target" if total["ease_estimate"] < low else "at_or_above_minimum"),
            "unprotected_syllables_per_word": free_ratio, "protected_terms": list(protected),
            "hotspots": hotspots, "paragraphs": paragraphs, "windows": windows,
            "notice": "Estimated scores, not comprehension or voice tests. Review suggestions in context. Dale-Chall requires a suitable supplied list. SMOG needs 30 sentences. Keep names, facts and meaning."}


def compare(before, after, profile="longform", protected=(), dictionary="heuristic", easy=None):
    a = analyze(before, profile, protected, dictionary, easy)
    b = analyze(after, profile, protected, dictionary, easy)
    old, new = a["metrics"]["ease_estimate"], b["metrics"]["ease_estimate"]
    old_num, new_num = Counter(NUMBER.findall(before)), Counter(NUMBER.findall(after))
    pat = protected_pattern(protected)
    old_terms = Counter(pat.findall(before)) if pat else Counter()
    new_terms = Counter(pat.findall(after)) if pat else Counter()
    missing = dict(old_terms - new_terms)
    added = dict(new_terms - old_terms)
    num_missing, num_added = dict(old_num - new_num), dict(new_num - old_num)
    return {"before": a, "after": b, "ease_change": round(new - old, 1) if old is not None and new is not None else None,
            "review_required": bool(missing or added or num_missing or num_added),
            "protected_removed": missing, "protected_added": added,
            "numbers_removed": num_missing, "numbers_added": num_added,
            "notice": "Literal changes require review; unchanged literals do not prove factual or semantic equivalence. The editor decides."}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--profile", choices=TARGETS, default="longform")
    p.add_argument("--dictionary", choices=("heuristic", "cmu"), default="heuristic")
    p.add_argument("--protect", action="append", default=[])
    p.add_argument("--easy-words", type=Path, help="Optional suitable Dale-Chall list, one word per line")
    p.add_argument("--before", type=Path, help="Compare original file with revised stdin")
    a = p.parse_args()
    if any(not term.strip() for term in a.protect):
        p.error("protected terms must not be empty")
    try:
        easy = set(a.easy_words.read_text(encoding="utf-8").lower().split()) if a.easy_words else None
        if easy is not None and not easy:
            raise ValueError("easy-word list is empty")
        text = sys.stdin.read()
        opts = (a.profile, a.protect, a.dictionary, easy)
        report = compare(a.before.read_text(encoding="utf-8"), text, *opts) if a.before else analyze(text, *opts)
        print(json.dumps(report, ensure_ascii=False, indent=2))
    except (OSError, ValueError) as exc:
        p.error(str(exc))


if __name__ == "__main__":
    main()
