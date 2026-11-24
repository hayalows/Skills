"""Reproduce the ten-pair development pilot. No model calls."""
import argparse
import hashlib
import json
from pathlib import Path
import statistics
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"scripts"))
from batch_shape_review import review
p=argparse.ArgumentParser(description=__doc__)
p.add_argument("--checker-root",type=Path,default=ROOT.parent/"independent-voice-checker")
a=p.parse_args()
b=(a.checker_root/"pk_checker.py").read_bytes()
if hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()!="3a5dbb0a7f75e295fd7d087cacfeb66ccc55391a":
    raise SystemExit("Use the frozen Independent Voice Checker 1.0.0 from b23c097.")
sys.path.insert(0,str(a.checker_root.resolve()))
import pk_checker as pk
data=json.loads((Path(__file__).parent/"drafts.json").read_text(encoding="utf-8"))
out={}
for col in ("before","after"):
    r=review([(x["id"],x[col]) for x in data])
    ms=[pk.audit(x[col],profile="longform",mode="heuristic") for x in data]
    out[col]={"drafts":len(data),"mean_ease":round(statistics.mean(m["metrics"]["ease_estimate"] for m in ms),2),"mean_grade":round(statistics.mean(m["metrics"]["grade_estimate"] for m in ms),2),"mean_words":round(statistics.mean(m["metrics"]["words"] for m in ms),1),"paragraph_counts":r["paragraph_count_distribution"],"opening_modes":r["opening_mode_distribution"],"example_marker_docs":r["documents_with_example_markers"],"paragraph2_example_docs":r["documents_with_example_marker_in_paragraph_2"],"families":{k:{"documents":v["documents"],"occurrences":v["occurrences"]} for k,v in r["families"].items()},"batch_flags":r["flags"],"strict_target":sum(m["strict_grade5_target"] is True for m in ms),"short_samples":sum(m["audience_status"]=="short_sample" for m in ms),"style_flags":sum(len(m["flags"]) for m in ms),"draft_metrics":[{"id":x["id"],"ease":m["metrics"]["ease_estimate"],"grade":m["metrics"]["grade_estimate"],"words":m["metrics"]["words"],"flags":[f["type"] for f in m["flags"]]} for x,m in zip(data,ms)]}
out["unchanged_drafts"]=sum(x["before"]==x["after"] for x in data)
print(json.dumps(out,ensure_ascii=False,indent=2))
