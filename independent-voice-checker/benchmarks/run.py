"""Compare the pinned baseline with this candidate on labelled development cases."""
import json
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
import pk_checker as p
data=json.loads((ROOT/"datasets/development_cases.json").read_text(encoding="utf-8"))
def summarize(rows):
    tp=sum(w and a for _,w,a in rows); fp=sum(not w and a for _,w,a in rows)
    fn=sum(w and not a for _,w,a in rows); tn=sum(not w and not a for _,w,a in rows)
    return dict(tp=tp,fp=fp,fn=fn,tn=tn,precision=tp/(tp+fp) if tp+fp else None,recall=tp/(tp+fn) if tp+fn else None)
out={}
for family,cases in ((k,data[k]) for k in ("conversation","composition")):
    old=[];new=[]
    for s,want in cases:
        a=bool(p.old_conversation.review(s)["flags"]) if family=="conversation" else bool(p.original.composition_candidates([s]))
        b=bool(p.conversation(p.sentences(p.style_prose(s)),"longform")) if family=="conversation" else p.triplet(s)
        old.append((s,want,a)); new.append((s,want,b))
    out[family]={"baseline":summarize(old),"candidate":summarize(new),"cases":[{"text":s,"expected":w,"baseline":a,"candidate":b} for (s,w,a),(_,_,b) in zip(old,new)]}
print(json.dumps(out,ensure_ascii=False,indent=2))
