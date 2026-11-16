#!/usr/bin/env python3
"""voice_check.py: readability + AI-tell scan for Papa Kojo's voice (v1.1).
No dependencies. Usage: python3 voice_check.py < draft.txt
Numbers are a smoke alarm, not a judge. Read the draft aloud too."""
import sys, re, statistics

t = sys.stdin.read()
low = t.lower()

def syl(w):
    w = w.lower().strip("'")
    if len(w) <= 3:
        return 1
    w = re.sub(r"(?:[^laeiouy]es|ed|[^laeiouy]e)$", "", w)
    w = re.sub(r"^y", "", w)
    return max(1, len(re.findall(r"[aeiouy]{1,2}", w)))

sents = [s.strip() for s in re.split(r"(?<=[.!?])\s+|\n+", t.strip()) if re.search(r"[A-Za-z]", s)]
words = re.findall(r"[A-Za-z']+", t)
lens = [len(re.findall(r"[A-Za-z']+", s)) for s in sents]
W, S = max(len(words), 1), max(len(sents), 1)
Y = sum(syl(w) for w in words)
fk = 0.39 * W / S + 11.8 * Y / W - 15.59
fre = 206.835 - 1.015 * W / S - 84.6 * Y / W
sd = statistics.pstdev(lens) if len(lens) > 1 else 0

print("READABILITY")
print(f"  FK grade {fk:.1f} (aim 2.5-4.5)   Flesch ease {fre:.0f} (aim 80+)")
print(f"  sentences {S}, avg {W/S:.1f} words (aim 8-13), longest {max(lens) if lens else 0}, spread (sd) {sd:.1f} (aim 4+; low = robotic sameness)")
print(f"  one-to-three-word sentences: {sum(1 for l in lens if l <= 3)} (more than 1 per 150 words reads like stacked AI fragments)")
print("  3+ syllable words:", ", ".join(sorted({w for w in words if syl(w) >= 3})) or "none")

BANNED = ["ensure","crucial","nestled","uncover","journey","embark","unleash","dive","delve","discover","plethora",
"indulge","more than just","not just","unlock","unveil","look no further","world of","realm","whether you",
"landscape","navigate","daunting","tapestry","unique blend","blend","enhanc","game changer","game-changer",
"stand out","stark","contrast","leverage","foster","transformative","additionally","align with","boasts",
"bolster","pivotal","robust","showcase","testament","underscore","vibrant","intricate","meticulous",
"seamless","elevate","empower","resonate","profound","nuanced","holistic","in today's","here's the thing",
"let that sink in","at its core","it is important to note","bottom line","the truth is","the reality is",
"in a world where","at the end of the day","quietly","simply put","genuinely","truly","deeply","powerful"]
hits = [b for b in BANNED if re.search(r"\b" + re.escape(b), low)]

PATTERNS = {
 "negative flip (not X, it's Y / isn't about / rather than)": r"\b(?:it'?s|it is|this is|that'?s|that is|isn'?t|wasn'?t|aren'?t|don'?t|doesn'?t)\s+(?:not\s+)?(?:about\s+)?[^.?!]{0,40}[.;,]\s*(?:it'?s|it is|but|they'?re)\b|\brather than\b|\bisn'?t about\b|\bnot because\b",
 "'Most people... / We all...' sweeping opener": r"(?m)^(?:most people|we all|everyone|nobody)\b",
 "label-then-reveal ('The trouble/key/secret/fix is')": r"\bthe (?:real )?(?:trouble|problem|key|secret|fix|point|answer|lesson|truth)\s+is\b",
 "'Here's' signpost": r"\bhere'?s (?:what|why|how|the)\b",
 "colon reveal": r"[a-z]: [A-Z][^.]{0,40}\.",
 "rhetorical Q answered at once": r"\?\s+(?:it'?s|because|the answer|simple|yes|no)\b",
 "tidy triple (X, Y, and Z)": r"\b\w+(?: \w+)?, \w+(?: \w+)?,? and \w+",
 "-ing tail clause (', making/showing...')": r", (?:making|showing|highlighting|reflecting|ensuring|creating|leaving|reminding|proving)\b",
 "'And that's okay/the point' closer": r"\band that'?s (?:okay|ok|fine|the point|the whole point|enough)\b",
 "stock moral closer ('the X will follow/catch up')": r"\bwill (?:follow|catch up|take care of itself)\b",
}
print("\nAI TELLS")
print("  banned/AI vocabulary:", ", ".join(hits) or "none")
for name, rx in PATTERNS.items():
    m = [x.group(0) for x in re.finditer(rx, t, flags=re.I)]
    if m:
        print(f"  {name}: {len(m)}  e.g. {m[0][:60]!r}")
NEG = re.compile(r"\b(?:not|don'?t|doesn'?t|didn'?t|isn'?t|aren'?t|wasn'?t|won'?t|never|no)\b", re.I)
flips = []
for a_, b_ in zip(sents, sents[1:]):
    if NEG.search(a_) and re.match(r"(?i)(?:they|it|you|we|he|she|that|this|but|instead)\b", b_):
        wa = set(re.findall(r"[a-z]{3,}", a_.lower())); wb = set(re.findall(r"[a-z]{3,}", b_.lower()))
        if wa & wb - {"that","this","with","your","have","they","them","what","when","the","and","you","are","for","but","its","not"}:
            flips.append(a_[:40] + " / " + b_[:30])
if flips:
    print(f"  two-sentence flip (negative line, then the same idea turned over): {len(flips)}  e.g. {flips[0]!r}")
openers = [s.split()[0].lower() for s in sents if s.split()]
rep = [w for w in set(openers) if openers.count(w) >= max(3, S // 4)]
if rep:
    print("  repeated sentence openers:", ", ".join(rep))
print("\nPUNCTUATION")
contr = len(re.findall(r"\b\w+'(?:s|t|re|ll|ve|d|m)\b", t))
print(f"  em dashes {t.count(chr(8212))} (must be 0)   exclamation {t.count('!')}   questions {t.count('?')}   "
      f"commas {t.count(',')}   parentheses {t.count('(')}   contractions {contr}")
print("  (only full stops and commas, every sentence the same shape, reads machine-made. Some variety is human.)")
