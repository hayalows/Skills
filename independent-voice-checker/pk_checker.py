#!/usr/bin/env python3
"""Independent advisory checker. No rewriting and no automatic voice approval."""
import argparse
from collections import Counter
from functools import lru_cache
import json
import math
from pathlib import Path
import re
import statistics
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent / "baseline"))
import adaptive_readability as base
import original_check as original
import conversation_check as old_conversation

VERSION = "1.0.0"
# Common-word calibration from Gemini's supplied checker; accent variants remain estimates.
EXCEPTIONS = dict(base.EXCEPTIONS, **{
    "actually":4,"already":3,"area":3,"beautiful":3,"buyer":2,"buyers":2,
    "cedi":2,"cedis":2,"company":3,"customer":3,"customers":3,"different":3,
    "drawer":1,"earlier":3,"electricity":5,"evening":2,"experience":4,
    "family":3,"ghana":2,"ghanaian":3,"idea":3,"ideas":3,"interest":3,
    "interesting":4,"kumasi":3,"accra":2,"momo":2,"notebook":2,"owner":2,
    "paper":2,"quietly":3,"supplier":3,"suppliers":3,"trotro":2,"usually":4,
    "being":2,"going":2,"doing":2,"created":3,"simple":2,"trouble":2,
    "received":2,"question":2,"questions":2,"wednesday":2,"comfortable":4,
})
PLAIN = re.compile(r"(?m)^[ \t]*(?:#{1,6}[ \t]+.*|(?:[-*_][ \t]*){3,})$")
FENCE = re.compile(r"(?ms)^[ \t]*(" + chr(96)*3 + r"|~~~)[^\n]*\n.*?(?:^[ \t]*\1[^\n]*$|\Z)")
INLINE = re.compile(chr(96)+r"[^"+chr(96)+r"\n]+"+chr(96))
QUOTE = re.compile(r'“[^”]*”|"[^"\n]*"|(?<!\w)‘[^’\n]+’')
WORD = base.WORD
PREFIX = re.compile(r"^(?:(?:still|however|of course|for example|for instance|in fact|over time|at first|meanwhile|in practice|to be fair|so far)|(?:in|on|at|by|during|over|after|before|with|without|from|for|under)\s+[^,]{1,55}),\s*",re.I)
SUB = re.compile(r"^(?:if|when|while|although|because|unless|since|once|before|after|as|even if)\b",re.I)
JOIN = re.compile(r"\b(?:and|or)\b",re.I)
DISCOURSE = re.compile(r"^(?:but|so|yet|because|although|though|however|instead|which|who|where|while|since|unless|rather than)\b",re.I)
NUMBER = re.compile(r"(?<!\w)(?:(?:GH₵|GHS|₵|USD|US\$|[$€£])\s*)?[+\-−]?(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?(?:\s?(?:%|percent\b|per cent\b|cedis?\b|dollars?\b|kg\b|km\b|kWh\b|MWh\b|MW\b|hours?\b|days?\b|years?\b))?(?!\w)",re.I)
WRITTEN = re.compile(r"\b(?:zero|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred|thousand|million|billion|half|quarter|twice|dozen)\b",re.I)
SCOPE = re.compile(r"\b(?:not|never|no|none|nothing|neither|nor|cannot|may|might|could|will|would|possibly|probably|perhaps|maybe|likely|unlikely|must|should|all|every|always|most|many|some|few|rarely|often|usually|only|unless|if|planned|approved|helped|supported|led|built|promised|confirmed)\b",re.I)
CONTRACTIONS = {"can't":"can not","won't":"will not","shan't":"shall not","ain't":"is not"}
PERSON = re.compile(r"\b(?:i|me|my|mine|we|us|our|ours|you|your|yours)\b",re.I)
CONVERSATION = {"detached_take","detached_say","detached_picture","detached_suppose","formal_setup","detached_think","repeated_invitation","question_run"}
COMPOSITION = {"rule_of_three","parallel_overuse","opening_repetition"}
# These exclusions protect common literal tasks, not arbitrary imperatives.
INSTRUCTION = re.compile(r"^(?:say (?:a prayer|a word|thank you|hello|goodbye|the word|your name)|take (?:a seat|a break|a photo|a picture|a look|your\b|the bus)|picture .+\b(?:with|using) (?:your|a|the) (?:phone|camera)|imagine .+\b(?:draw|mark|label|sketch)\b|consider (?:the costs?|the risks?|a request|the evidence)\b|think of (?:a number|a word)\b)",re.I)
SETUPS = [
    ("detached_take",r"^take\s+(?:the case of\b|(?:a|an|the)\s+[^.!?]{1,90}\b(?:that|who|which|with|for example)\b)"),
    ("detached_say",r"^say\s+(?:i|you|we|someone|somebody|a|an)\b"),
    ("detached_picture",r"^(?:picture|imagine)\s+(?:a|an|the|you|yourself|someone|if)\b"),
    ("detached_suppose",r"^suppose\s+(?:i|you|we|a|an|the|someone|that)\b"),
    ("formal_setup",r"^consider\s+(?:a|an|the)\s+(?:scenario|hypothetical|situation|example|case|shop|trader|owner|student|client|person|friend|farmer|family|company)\b"),
    ("detached_think",r"^think of\s+(?:a|an|the)\s+[^.!?]{1,90}\b(?:that|who|which|with)\b"),
]

def prose(text):
    return PLAIN.sub("", FENCE.sub("\n", text)).strip()

def style_prose(text):
    text = prose(text)
    text = re.sub(r"(?m)^[ \t]*>[^\n]*", "", text)
    return QUOTE.sub(" ", INLINE.sub(" ", text))

def sentences(text):
    # Preserve decimal points and titles; allow sentence ends after time abbreviations.
    text = prose(text)
    text = re.sub(r"(?<=\d)\.(?=\d)", "\ue000", text)
    text = re.sub(r"\b(?:Mr|Mrs|Ms|Dr|Prof|St|Jr|Sr|vs)\.",lambda m:m[0][:-1]+"\ue000",text,flags=re.I)
    text = re.sub(r"\b(?:[A-Za-z]\.){2,}",lambda m:m[0][:-1].replace(".","\ue000")+".",text)
    text = re.sub(r"\b(?i:a\ue000m|p\ue000m|e\ue000g|i\ue000e)\.(?=\s+[a-z0-9])",lambda m:m[0][:-1]+"\ue000",text)
    return [s.replace("\ue000",".").strip() for s in re.split(r"(?<=[.!?])\s+|(?<=[.!?][\"”’])\s+|\n\s*\n",text) if WORD.search(s)]

@lru_cache(maxsize=2)
def dictionary():
    import cmudict
    return cmudict.dict()

@lru_cache(maxsize=16384)
def heuristic(word):
    w=word.lower().replace("’","'")
    if w in EXCEPTIONS: return EXCEPTIONS[w]
    # Preserve explicit Ghanaian/common-word overrides; otherwise use the frozen fallback.
    return base.counter_for("heuristic")(w)

@lru_cache(maxsize=16384)
def cmu(word):
    entries=dictionary().get(word.lower().replace("’","'"))
    return sum(p[-1:].isdigit() for p in entries[0]) or 1 if entries else heuristic(word)

def metrics(ss, count):
    m=base.metrics(ss,count)
    ws=[w.lower().replace("’","'") for s in ss for w in WORD.findall(s)]
    lens=[len(WORD.findall(s)) for s in ss]
    if not ws: return {**m,"sentence_len_cv":None,"mattr_100":None,"fog_estimate":None,"longest_short_run":0}
    n=len(ws)
    length=min(100,n)
    mattr=sum(len(set(ws[i:i+length]))/length for i in range(n-length+1))/(n-length+1)
    run=longest=0
    for k in lens:
        run=run+1 if k<8 else 0
        longest=max(run,longest)
    # Unadjusted Fog: no claim of proper-noun/inflection recognition.
    return {**m,"sentence_len_cv":round(statistics.pstdev(lens)/(n/len(ss)),3),
            "mattr_100":round(mattr,3),"fog_estimate":round(.4*(n/len(ss)+100*m["polysyllables"]/n),2),
            "longest_short_run":longest}

def status(m, profile):
    if m["words"]<100 or m["sentences"]<5: return "short_sample"
    lo,hi=base.TARGETS[profile]; e=m["ease_estimate"]
    if e<lo-2: return "review_difficulty"
    if e<lo: return "near_target"
    if profile=="longform" and m["grade_estimate"]>6.5: return "review_grade"
    return "above_range_no_penalty" if e>hi else "in_range"

def triplet(s):
    s=re.sub(r"(?<=\d),(?=\d)","",s)
    for segment in re.split(r"[;:]",s):
        body=segment.strip()
        for _ in range(3):
            new=PREFIX.sub("",body)
            if new==body: break
            body=new
        parts=[x.strip(" .!?") for x in body.split(",")]
        if len(parts)<2 or not all(parts): continue
        if SUB.match(parts[0]):
            # Keep parallel dependent clauses; strip ordinary conditional preface.
            if not re.match(r"^(?:what|when|how|where|who|if)\b",parts[1],re.I):
                parts=parts[1:]
            elif len(parts)>=4 and re.match(r"^(?:and|or)\s+(?:what|when|how|where|who|if)\b",parts[2],re.I):
                # A coordinated dependent list followed by the main clause.
                parts=parts[:3]
        if len(parts)<2: continue
        if any(DISCOURSE.match(p) for p in parts[1:]): continue
        tail=parts[-1]
        if JOIN.match(tail):
            items=parts[:-1]+[JOIN.sub("",tail,count=1).strip()]
        else:
            joins=list(JOIN.finditer(tail))
            if len(joins)!=1: continue
            j=joins[0]; items=parts[:-1]+[tail[:j.start()].strip(),tail[j.end():].strip()]
        if len(items)>=3 and all(WORD.search(x) for x in items): return True
    return False

def conversation(ss,profile):
    if profile not in {"longform","post"}: return []
    out=[]; last=-100
    for i,s in enumerate(ss,1):
        opening=re.sub(r"^(?:so|now|then)[, ]+","",s,flags=re.I)
        if not INSTRUCTION.match(opening):
            matched=False
            for kind,rx in SETUPS:
                if re.match(rx,opening,re.I):
                    out.append((kind,s,i)); matched=True; break
            if matched or re.match(r"^(?:let us|let['’]s)\b",opening,re.I):
                if i-last<=4: out.append(("repeated_invitation",s,i))
                last=i
        if i>=3 and all(x.endswith("?") for x in ss[i-3:i]): out.append(("question_run",s,i))
    return out

def audit(text,profile="longform",mode="auto",protected=()):
    clean=prose(text); ss=sentences(clean); style=style_prose(text); st=sentences(style)
    h=metrics(ss,heuristic); c=None
    if mode!="heuristic":
        try: dictionary(); c=metrics(ss,cmu)
        except ImportError:
            if mode=="cmu": raise ValueError("CMU mode requires optional cmudict")
    primary=c if c is not None else h; counter=cmu if c is not None else heuristic
    flags=[]
    def add(kind,match,advice="Review in context; preserve meaning.",sentence=None):
        flags.append({"type":kind,"match":match,"advice":advice,"sentence":sentence})
    # Use frozen pattern vocabulary, but report all occurrences from visible prose.
    for term in original.AVOID:
        for m in re.finditer(r"(?<!\w)"+r"\s+".join(map(re.escape,term.split()))+r"(?!\w)",style,re.I):
            add("avoid_word",m[0],"Prefer familiar wording; keep required terms.")
    for m in re.finditer(r"—|(?<!\d)–|–(?!\d)|(?<!-)--(?!-)",style):
        add("dash_review",m[0],"Review punctuation; retain exact notation and ranges.")
    for kind,rx,advice in original.PATTERNS:
        for m in re.finditer(rx,style,re.I|re.M): add(kind,m[0],advice)
    hits=[i for i,s in enumerate(st,1) if triplet(s)]
    for i in hits: add("rule_of_three",st[i-1],"Review coordinated items; retain needed lists.",i)
    if len(hits)>=2: add("parallel_overuse",str(hits))
    openings=[tuple(WORD.findall(s.lower())[:2]) for s in st]
    for i in range(2,len(st)):
        if len(openings[i])==2 and openings[i]==openings[i-1]==openings[i-2]: add("opening_repetition"," / ".join(st[i-2:i+1]),sentence=i+1)
    for kind,s,i in conversation(st,profile): add(kind,s,"Review framing; preserve real instructions and useful questions.",i)
    # Retain register behavior from Original. Educational/technical are measurement profiles, not mandatory personal registers.
    reg=profile if profile in original.REGISTERS else "formal"
    legacy=original.scan(style,reg)
    for f in legacy["flags"]:
        if f["id"] in {"register_contractions","register_emoji","register_exclamation","register_fragments","too_even_paragraphs","question_ending"}:
            add(f["id"],f["example"],f["advice"])
    if profile in {"longform","post","message"} and primary["longest_short_run"]>=5: add("too_fast",str(primary["longest_short_run"]))
    if primary["words"]>=120 and profile in {"longform","post"} and primary["sentence_len_cv"]<.30: add("flat_rhythm",str(primary["sentence_len_cv"]))
    if primary["words"]>=80 and profile in {"longform","post"} and not PERSON.search(style): add("no_person","entire draft","Check stance, detail or care; pronouns are optional.")
    starts=sorted(set(range(0,max(1,len(ss)-9),5))|{max(0,len(ss)-10)}) if ss else []
    windows=[{"start_sentence":i+1,"end_sentence":min(i+10,len(ss)),**metrics(ss[i:i+10],counter)} for i in starts]
    paragraphs=[{"paragraph":i+1,**metrics(sentences(p),counter)} for i,p in enumerate(re.split(r"\n\s*\n",clean)) if WORD.search(p)]
    pat=base.protected_pattern(protected)
    hotspots=[]
    for i,s in enumerate(ss,1):
        free=pat.sub(" ",s) if pat else s
        hard=sorted(set(w for w in WORD.findall(free) if counter(w)>=3))
        if hard or len(WORD.findall(s))>23: hotspots.append({"sentence":i,"text":s,"review_words":hard})
    es,gs=primary["ease_estimate"],primary["grade_estimate"]
    strict=None if status(primary,profile)=="short_sample" or profile not in {"longform","post","message","chat","comment"} else 80<=es<=95 and 4<=gs<=6
    gap=round(c["ease_estimate"]-h["ease_estimate"],2) if c and es is not None else None
    return {"version":VERSION,"profile":profile,"primary_estimator":"cmu" if c is not None else "heuristic","metrics":primary,
            "heuristic":h,"cmu":c,"cmu_minus_heuristic":gap,"estimator_review":gap is not None and (abs(gap)>=5 or status(c,profile)!=status(h,profile)),
            "audience_status":status(primary,profile),"strict_grade5_target":strict,"flags":flags,
            "paragraphs":paragraphs,"hardest_windows":sorted(windows,key=lambda w:w["ease_estimate"])[:5],"hotspots":hotspots,
            "notice":"Advisory surface candidates, not AI detection, semantic proof or voice rating. Fog is unadjusted. Scores are estimates."}

def literal_pattern(term):
    return re.compile(r"(?<!\w)"+re.escape(term)+r"(?!\w)")

def number_matches(text):
    return sorted([*NUMBER.finditer(text),*WRITTEN.finditer(text)],key=lambda m:m.start())

def normalize_number(s):
    return re.sub(r"\s+"," ",s.lower().replace("−","-").replace(",","")).strip()

def cues(text):
    text=text.lower().replace("’","'")
    for old,new in CONTRACTIONS.items(): text=re.sub(r"(?<!\w)"+re.escape(old)+r"(?!\w)",new,text)
    text=re.sub(r"\b(\w+)n't\b",r"\1 not",text)
    text=text.replace("cannot","can not")
    return Counter(SCOPE.findall(text))

def contexts(text):
    # Nearby lexical anchors are advisory: rephrasing may create a warning.
    result=[]
    for s in sentences(text):
        for m in number_matches(s):
            left=WORD.findall(s[:m.start()].lower())[-3:]
            right=WORD.findall(s[m.end():].lower())[:2]
            result.append((normalize_number(m[0])," ".join(left)," ".join(right)))
    return result

def diff_revisions(before,after,profile="longform",mode="auto",protected=(),required=()):
    a=audit(before,profile,mode,protected); b=audit(after,profile,mode,protected)
    old=Counter(normalize_number(m[0]) for m in number_matches(before)); new=Counter(normalize_number(m[0]) for m in number_matches(after))
    oldp=Counter({t:len(literal_pattern(t).findall(before)) for t in set(protected)})
    newp=Counter({t:len(literal_pattern(t).findall(after)) for t in set(protected)})
    oc,nc=cues(before),cues(after)
    missing=[t for t in required if not literal_pattern(t).search(after)]
    delta={"missing_required":missing,"protected_removed":dict(oldp-newp),"protected_added":dict(newp-oldp),
           "numbers_removed":dict(old-new),"numbers_added":dict(new-old),"scope_cues_removed":dict(oc-nc),"scope_cues_added":dict(nc-oc)}
    changed=contexts(before)!=contexts(after)
    e1,e2=a["metrics"]["ease_estimate"],b["metrics"]["ease_estimate"]
    return {"version":VERSION,"before":a,"after":b,**delta,"numeric_context_changed":changed,
            "numeric_context_before":contexts(before) if changed else [],"numeric_context_after":contexts(after) if changed else [],
            "ease_change":round(e2-e1,1) if e1 is not None and e2 is not None else None,
            "literal_review_required":any(delta.values()) or changed,"editor_review_required":True,
            "notice":"Check actors, facts, causality, certainty and tone manually, even if no literal warning. Context flags can reflect harmless rephrasing."}

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--profile",choices=base.TARGETS,default="longform")
    p.add_argument("--dictionary",choices=("auto","heuristic","cmu"),default="auto")
    p.add_argument("--before",type=Path); p.add_argument("--protect",action="append",default=[]); p.add_argument("--require",action="append",default=[])
    p.add_argument("--json",action="store_true",help="JSON is the default")
    p.add_argument("--composition-gate",action="store_true"); p.add_argument("--review-gate",action="store_true")
    a=p.parse_args()
    if any(not t.strip() for t in a.protect+a.require): p.error("terms must not be empty")
    if a.require and not a.before: p.error("--require needs --before")
    try:
        s=sys.stdin.read()
        r=diff_revisions(a.before.read_text(encoding="utf-8"),s,a.profile,a.dictionary,a.protect,a.require) if a.before else audit(s,a.profile,a.dictionary,a.protect)
        print(json.dumps(r,ensure_ascii=False,indent=2))
        flags=(r["after"] if a.before else r)["flags"]
        ids={f["type"] for f in flags}
        return 2 if (a.review_gate and (ids or r.get("literal_review_required"))) or (a.composition_gate and ids&COMPOSITION) else 0
    except (OSError,ValueError) as e: p.error(str(e))

if __name__=="__main__":
    sys.exit(main())
