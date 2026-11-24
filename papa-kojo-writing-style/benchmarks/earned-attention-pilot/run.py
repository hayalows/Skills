"""Replay authored development pairs; not an independent generation study."""
import argparse, hashlib, json, sys, statistics
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"scripts"))
from arc_review import review
p=argparse.ArgumentParser(description=__doc__)
p.add_argument("--checker-root",type=Path,default=ROOT.parent/"independent-voice-checker")
a=p.parse_args()
b=(a.checker_root/"pk_checker.py").read_bytes()
if hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()!="3a5dbb0a7f75e295fd7d087cacfeb66ccc55391a":
    raise SystemExit("Use the frozen checker 1.0.0 from b23c097.")
sys.path.insert(0,str(a.checker_root.resolve()))
import pk_checker as pk
data=json.loads((Path(__file__).parent/"drafts.json").read_text(encoding="utf-8"))
out={}
for col in ("before","after"):
    rows=[]
    for d in data:
        profile="message" if d["id"]=="message" else "post" if d["id"]=="sales" else "longform"
        r=pk.audit(d[col],profile,mode="heuristic")
        m=r["metrics"]
        rows.append({"id":d["id"],"words":m["words"],"ease":m["ease_estimate"],"grade":m["grade_estimate"],"flags":[f["type"] for f in r["flags"]],"status":r["audience_status"],"strict":r["strict_grade5_target"]})
    substantial=[r for r in rows if r["status"]!="short_sample"]
    out[col]={"rows":rows,"substantial":len(substantial),"mean_ease":round(statistics.mean(r["ease"] for r in substantial),2),"mean_grade":round(statistics.mean(r["grade"] for r in substantial),2),"strict_passes":sum(r["strict"] is True for r in substantial),"style_flags":sum(len(r["flags"]) for r in rows),"edge_candidates":review([(d["id"],d[col]) for d in data])["candidates"]}
out["unchanged"]=sum(d["before"]==d["after"] for d in data)
print(json.dumps(out,ensure_ascii=False,indent=2))
