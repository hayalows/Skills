#!/usr/bin/env python3
"""Advisory cross-document review of repeated openings and discourse scaffolds.
No authorship inference, uniqueness score, persistence or automatic rewriting.
"""
import argparse
from collections import Counter, defaultdict
import json
from pathlib import Path
import re

VERSION = "1.0.0"
WORD = re.compile(r"[^\W\d_]+(?:['’][^\W\d_]+)?", re.UNICODE)
FAMILIES = {
    "shared_invitation": re.compile(r"^(?:(?:so|now|then)[, ]+)?(?:let us|let's)\s+(?:say|take|look|consider|think|suppose|imagine|use|work)", re.I),
    "detached_setup": re.compile(r"^(?:(?:so|now|then)[, ]+)?(?:take|say|suppose|picture|imagine|consider|think of)\b", re.I),
    "explicit_example": re.compile(r"\b(?:for example|for instance|as an example)\b", re.I),
    "concession": re.compile(r"^(?:of course|to be fair|admittedly|there are times when)\b", re.I),
    "personal_hedge": re.compile(r"^(?:i think|i believe|i feel|in my view)\b", re.I),
    "explanation_signpost": re.compile(r"^(?:this is why|that is why|this is what|the reason is)\b", re.I),
}
def prose(text):
    text = re.sub(r"(?ms)^[ \t]*(" + chr(96)*3 + r"|~~~)[^\n]*\n.*?(?:^[ \t]*\1[^\n]*$|\Z)", "\n", text)
    text = re.sub(r"(?m)^[ \t]*(?:#{1,6}[ \t]+.*|>.*|(?:[-*_][ \t]*){3,})$", "", text)
    text = re.sub(chr(96)+r"[^"+chr(96)+r"\n]+"+chr(96), " ", text)
    return re.sub(r'“[^”]*”|"[^"\n]*"|(?<!\w)‘[^’\n]+’', " ", text).strip()

def sentences(text):
    text = re.sub(r"(?<=\d)\.(?=\d)", "\ue000", text)
    text = re.sub(r"\b(?:Mr|Mrs|Ms|Dr|Prof|St)\.",lambda m:m[0][:-1]+"\ue000",text,flags=re.I)
    return [s.replace("\ue000",".").strip() for s in re.split(r"(?<=[.!?])\s+",text) if WORD.search(s)]

def tokens(s):
    return [w.lower().replace("’","'") for w in WORD.findall(s)]

def opening_mode(s):
    t=s.lower().lstrip()
    if FAMILIES["shared_invitation"].match(t): return "invitation"
    if re.match(r"^(?:if|when|while|once|before|after|as)\b",t): return "dependent_clause"
    if re.match(r"^(?:i|my|we|our|for me)\b",t): return "personal"
    if re.match(r"^(?:you|your)\b",t): return "reader"
    if re.match(r"^(?:what|why|how|where|who|can|do|does|is|are|would|could)\b",t) and t.endswith("?"): return "question"
    return "other_or_direct"

def inspect(doc_id,text):
    ps=[sentences(p.replace("\n"," ")) for p in re.split(r"\n\s*\n",prose(text)) if WORD.search(p)]
    ps=[p for p in ps if p]
    hits=defaultdict(list)
    prefixes=[]
    sentence_no=0
    for i,para in enumerate(ps,1):
        for j,s in enumerate(para,1):
            sentence_no+=1
            s=s.replace("’","'")
            loc={"paragraph":i,"sentence":sentence_no,"text":s[:180],"at_paragraph_start":j==1,"last_paragraph":i==len(ps)}
            for name,rx in FAMILIES.items():
                if rx.search(s): hits[name].append(loc)
            if j==1 and len(tokens(s))>=4:
                prefixes.append((" ".join(tokens(s)[:4]),loc))
    return {"id":doc_id,"paragraphs":len(ps),"sentence_counts":[len(p) for p in ps],"words":sum(len(tokens(s)) for p in ps for s in p),
            "opening_mode":opening_mode(ps[0][0]) if ps else None,"hits":dict(hits),"prefixes":prefixes}

def review(documents,min_docs=3,coverage=.4):
    """documents: iterable of (unique document id, body text), same register."""
    if min_docs<2 or not 0<coverage<=1: raise ValueError("invalid review thresholds")
    docs=[inspect(k,v) for k,v in documents]
    if len({d["id"] for d in docs})!=len(docs): raise ValueError("duplicate document id")
    n=len(docs)
    families={}
    flags=[]
    for f in FAMILIES:
        found={d["id"]:d["hits"][f] for d in docs if f in d["hits"]}
        k=len(found)
        families[f]={"documents":k,"occurrences":sum(map(len,found.values())),"locations":found}
        if k>=min_docs and k/n>=coverage:
            flags.append({"type":"repeated_scaffold","family":f,"documents":list(found),"coverage":round(k/n,3)})
    # Count an example marker only once per sentence even when several expressions overlap.
    ex={}
    for d in docs:
        loc={x["sentence"]:x for f in ("shared_invitation","detached_setup","explicit_example") for x in d["hits"].get(f,[])}
        if loc: ex[d["id"]]=list(loc.values())
    second=[k for k,ls in ex.items() if any(x["paragraph"]==2 for x in ls)]
    if len(second)>=min_docs and len(second)/n>=coverage:
        flags.append({"type":"repeated_position","family":"example_marker_in_paragraph_2","documents":second,"coverage":round(len(second)/n,3)})
    prefixes=defaultdict(dict)
    for d in docs:
        for p,loc in d["prefixes"]:
            prefixes[p].setdefault(d["id"],[]).append(loc)
    for p,found in sorted(prefixes.items()):
        if len(found)>=min_docs and len(found)/n>=coverage:
            flags.append({"type":"repeated_paragraph_opening","prefix":p,"documents":list(found),"coverage":round(len(found)/n,3)})
    return {"version":VERSION,"documents":n,"families":families,"documents_with_example_markers":len(ex),
            "documents_with_example_marker_in_paragraph_2":len(second),
            "paragraph_count_distribution":dict(Counter(d["paragraphs"] for d in docs)),
            "opening_mode_distribution":dict(Counter(d["opening_mode"] or "empty" for d in docs)),
            "flags":flags,"drafts":docs,
            "notice":"Surface cues only. A flag invites editorial review; necessary shared language, format and examples may stay. No claim of authorship, naturalness or statistical uniqueness."}

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("drafts",nargs="+",type=Path,help="Comparable prose drafts, with Markdown headings if needed")
    p.add_argument("--min-docs",type=int,default=3)
    p.add_argument("--coverage",type=float,default=.4)
    a=p.parse_args()
    try:
        r=review([(str(f),f.read_text(encoding="utf-8")) for f in a.drafts],a.min_docs,a.coverage)
        print(json.dumps(r,ensure_ascii=False,indent=2))
    except (OSError,ValueError) as e: p.error(str(e))
if __name__=="__main__": main()
