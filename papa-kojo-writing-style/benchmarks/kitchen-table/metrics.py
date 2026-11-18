#!/usr/bin/env python3
"""Frozen automatic checks for the Kitchen Table Benchmark (written before v3.0 was built).
Signals only. They do not prove authorship or voice."""
import re, sys, json, glob, os, statistics

RANGES = {"B01":(20,60),"B02":(10,35),"B03":(60,120),"B04":(120,200),"B05":(150,220),"B06":(180,260),
 "B07":(25,60),"B08":(60,120),"B09":(50,100),"B10":(300,450),"B11":(50,110),"B12":(70,130),"B13":(120,180),
 "B14":(40,90),"B15":(25,60),
 "H01":(15,50),"H02":(10,35),"H03":(70,130),"H04":(120,200),"H05":(150,220),"H06":(160,240),"H07":(40,90),"H08":(20,60),"H09":(30,80),"H10":(40,90)}
USER_AVOID = ["ensure","crucial","nestled","uncover","journey","embark","unleash","dive","delve","discover",
 "plethora","indulge","more than just","not just","unlock","unveil","look no further","world of","realm",
 "whether you're","landscape","navigate","daunting","tapestry","blend","enhancing","game changer","stand out",
 "stark","leverage","foster","transformative","i learnt that"]
# Patterns from Wikipedia's "Signs of AI writing" and the earlier tests.
TELLS = {
 "negative_parallelism": r"\b(?:it'?s|it is|this is|that is|they are|they're|isn'?t|is not|are not|aren'?t|wasn'?t|was not)\s+(?:not\s+)?(?:just\s+|only\s+|really\s+)?(?:about\s+)?[^.?!;]{1,50}[.;,]\s*(?:it|they|this|that)(?:'s| is| are| was)\b|\bnot only\b[^.?!]*\bbut\b|\bnot because\b[^.?!]*\bbut because\b|\bdon'?t just\b|\bdo not just\b",
 "label_reveal": r"\b(?:here'?s the thing|here is the thing|the key is|the secret is|the truth is|here'?s why|here is why|the reason is (?:simple|often simple)|let that sink in|bottom line|the real \w+ is|what (?:most )?people miss|the lesson\b|the takeaway\b)",
 "sweeping_opener": r"(?:^|\n)\s*(?:most people|many people|we all|everyone|in today'?s|in a world where|have you ever)",
 "signposting": r"\b(?:in summary|in conclusion|overall,|ultimately,|to sum up|at the end of the day|it is worth noting|it'?s worth noting|it is important to note|let'?s (?:dive|explore|break))",
 "significance_puffery": r"\b(?:testament to|plays a (?:vital|crucial|pivotal) role|stands as|serves as|rich (?:history|tapestry)|vibrant|pivotal|profound|seamless(?:ly)?|cutting-edge|dynamic|robust|empower\w*|elevate|resonate)\b",
 "moral_closer": r"(?:and that'?s okay|and that is okay|that is what \w+ (?:is|means)|that'?s what \w+ (?:is|means)|that is the (?:real )?(?:lesson|point)|remember,|small steps|one step at a time|the rest will follow)",
 "stacked_fragments": r"(?:^|[.!?]\s+)(?:\w+[.!?]\s+){3,}",
}
def split(text):
    parts = re.split(r"^## ([BH]\d\d)\s*$", text, flags=re.M)
    return {parts[i]: parts[i+1].strip() for i in range(1, len(parts), 2)}
def syl(w):
    w=w.lower().strip("'’")
    if len(w)<=3: return 1
    w=re.sub(r"(?:[^laeiouy]es|ed|[^laeiouy]e)$","",w); w=re.sub(r"^y","",w)
    return max(1,len(re.findall(r"[aeiouy]{1,2}",w)))
def sents(t):
    m=re.sub(r"(?<=\d)\.(?=\d)","∯",t)
    return [s for s in re.split(r"(?<=[.!?])\s+|\n+",m) if re.search(r"[A-Za-z]",s)]
def analyse(bid, t, brief):
    ws=re.findall(r"[A-Za-z0-9₵¢’'-]+",t); ss=sents(t)
    lens=[len(re.findall(r"[A-Za-z0-9’'-]+",s)) for s in ss]
    words=[w for w in re.findall(r"[A-Za-z’']+",t)]
    fre=206.835-1.015*len(words)/max(1,len(ss))-84.6*sum(map(syl,words))/max(1,len(words)) if words else None
    low=t.lower()
    tells={k:len(re.findall(v,t if k=="stacked_fragments" else low,flags=re.I)) for k,v in TELLS.items()}
    avoid=sorted({a for a in USER_AVOID if re.search(r"(?<![a-z])"+re.escape(a)+r"(?![a-z])",low)})
    nums_out=set(re.findall(r"\d+(?:[.,]\d+)?",t)); nums_in=set(re.findall(r"\d+(?:[.,]\d+)?",brief))
    new_nums=sorted(n for n in nums_out-nums_in if n not in {"1","2"})
    contr=len(re.findall(r"\b\w+['’](?:re|ve|ll|d|t|m)\b|\b(?:it|that|there|what|here|let|he|she|who)['’]s\b",t,re.I))
    lo,hi=RANGES[bid]
    paras=[p for p in re.split(r"\n\s*\n",t) if p.strip()]
    return {"words":len(ws),"in_range":lo<=len(ws)<=hi,"fre":round(fre,1) if fre is not None else None,
      "avg_sent":round(statistics.mean(lens),1) if lens else 0,"sent_cv":round(statistics.pstdev(lens)/statistics.mean(lens),2) if len(lens)>2 else None,
      "paras":len(paras),"em_dash":t.count("—")+t.count("–"),"contractions":contr,"avoid_words":avoid,
      "tells":tells,"new_numbers":new_nums,"exclaim":t.count("!"),"questions":t.count("?")}
if __name__=="__main__":
    outdir=sys.argv[1]; briefs=split(open(sys.argv[2] if len(sys.argv)>2 else os.path.join(os.path.dirname(__file__),"round-1","briefs.md")).read().replace("## B","## B"))
    braw=open(sys.argv[2] if len(sys.argv)>2 else os.path.join(os.path.dirname(__file__),"round-1","briefs.md")).read()
    btxt={m.group(1):m.group(2) for m in re.finditer(r"^## ([BH]\d\d)[^\n]*\n(.*?)(?=^## [BH]|\Z)",braw,re.S|re.M)}
    res={}
    for f in sorted(glob.glob(os.path.join(outdir,"*.md"))):
        n=os.path.basename(f)[:-3]; p=split(open(f).read())
        res[n]={b:analyse(b,p[b],btxt[b]) for b in btxt if b in p}; res[n]["_missing"]=[b for b in btxt if b not in p]
    json.dump(res,open(os.path.join(outdir,"..","metrics.json"),"w"),indent=1,ensure_ascii=False)
    hdr=f"{'version':16}{'n':>3}{'inRng':>6}{'FRE':>6}{'FRElong':>8}{'sentCV':>7}{'emd':>4}{'contr':>6}{'avoid':>6}{'flip':>5}{'label':>6}{'sweep':>6}{'sign':>5}{'puff':>5}{'moral':>6}{'frag':>5}{'newNum':>7}"
    print(hdr)
    for n,d in res.items():
        it=[v for k,v in d.items() if not k.startswith("_")]
        if not it: print(n,"no pieces"); continue
        fr=[v["fre"] for v in it if v["fre"] is not None]; lg=[d[b]["fre"] for b in ("B04","B05","B06","B10","B13","H04","H05","H06") if b in d] or fr
        cv=[v["sent_cv"] for v in it if v["sent_cv"] is not None]
        S=lambda k: sum(v["tells"][k] for v in it)
        print(f"{n:16}{len(it):>3}{sum(v['in_range'] for v in it):>6}{statistics.mean(fr):>6.1f}{statistics.mean(lg):>8.1f}{statistics.mean(cv):>7.2f}{sum(v['em_dash'] for v in it):>4}{sum(v['contractions'] for v in it):>6}{sum(len(v['avoid_words']) for v in it):>6}{S('negative_parallelism'):>5}{S('label_reveal'):>6}{S('sweeping_opener'):>6}{S('signposting'):>5}{S('significance_puffery'):>5}{S('moral_closer'):>6}{S('stacked_fragments'):>5}{sum(len(v['new_numbers']) for v in it):>7}")
