"""Score two external model-run outputs, with conservative automated checks.

Reads outputs produced by independent model sessions; no model calls in this script.
Scores only routing and output hygiene, not true empathy, KB currency or voice fidelity.
"""
from pathlib import Path
import json, csv, re, collections, sys
ROOT=Path(__file__).resolve().parents[3].parent
CASES=json.loads((ROOT/"Skills-main/springboard-mentor/benchmarks/holdout-v12/cases.json").read_text(encoding="utf-8"))["cases"] if (ROOT/"Skills-main").exists() else json.loads((Path(__file__).parent/"cases.json").read_text(encoding="utf-8"))["cases"]
EVAL=ROOT/"independent-eval"
def load(variant):
    out={}
    for batch in (1,2,3):
        file=EVAL/variant/str(batch)/"output.json"
        if not file.exists():
            print("MISSING",str(file),file=sys.stderr)
            continue
        text=file.read_text(encoding="utf-8-sig").strip()
        if text.startswith("```"): text=re.sub(r"^\x60{3}json\s*|\x60{3}$","",text,flags=re.I).strip()
        try:
            data=json.loads(text)
            rows=data.get("responses",[]) if isinstance(data,dict) else data
            for row in rows:
                if row.get("id") in out: print("DUPLICATE",variant,row["id"],file=sys.stderr)
                out[row["id"]]=row
        except Exception as exc: print("INVALID JSON",file,exc,file=sys.stderr)
    return out
def normalise(s): return re.sub(r"[^a-z0-9]+","_",str(s or "").lower()).strip("_")
equivalents={
"outreach":{"outreach","first_contact","send_draft"},
"reply":{"reply","continue","send_draft","answer"},
"close":{"close","no_reply","acknowledge"},
"no_reply":{"no_reply","close","wait"},
"verify_then_reply":{"verify_then_reply","research","source_check","verify_first"},
"verify_then_outreach":{"verify_then_outreach","verify_first","source_check"},
"followup":{"followup","follow_up","send_draft","reply"},
"block":{"block","refuse","do_not_send","do_not_send_bulk"},
"defer":{"defer","defer_contact","no_reply"},
"repair":{"repair","apologise_and_repair","service_recovery"},
"clarify":{"clarify","ask_one_question"},
"research":{"research","verify_first","source_check"},
"do_not_update":{"do_not_update","block","verify_first"},
"do_not_complete":{"do_not_complete","do_not_update"},
"correct_record":{"correct_record","do_not_update","record_only"},
"record_minimal":{"record_minimal","record_only","document"},
"refuse_and_guide":{"refuse_and_guide","refuse","verify_then_reply"},
"conflict_escalate":{"conflict_escalate","verify_then_reply","source_check"},
"urgent_escalation":{"urgent_escalation","escalate","crisis"}
}
def evaluate(case,row):
    if not row:return {"present":0,"route_ok":0,"format_ok":0,"brief_ok":0,"unsupported_verified":0}
    route=normalise(row.get("route"))
    gold=normalise(case["gold"])
    route_ok=int(route in equivalents.get(gold,{gold}))
    reply=str(row.get("student_text","") or "")
    note=str(row.get("mentor_note","") or "")
    format_ok=int(all(k in row and isinstance(row[k],str) for k in ["id","route","student_text","mentor_note","source_status"]))
    brief_ok=int(len(reply.split())<=90 and not re.search(r"^(oh okay|good to hear|i understand)(\b|[,.!])",reply.lower().strip()))
    verified=(row.get("source_status")=="verified")
    # A claim of verified without article identifier or official URL is suspicious, not proof of a hallucination.
    unsupported_verified=int(verified and not re.search(r"KA-\d{5}|https://help\.byupathway\.edu|official .+ guide",note,re.I))
    return {"present":1,"route_ok":route_ok,"format_ok":format_ok,"brief_ok":brief_ok,"unsupported_verified":unsupported_verified}
def main():
    outputs={v:load(v) for v in ("v11","v12")}
    lines=[]
    for case in CASES:
        record={"id":case["id"],"group":case["group"],"expected_route":case["gold"]}
        for v in ("v11","v12"):
            stats=evaluate(case,outputs[v].get(case["id"]))
            for k,val in stats.items():record[f"{v}_{k}"]=val
            record[f"{v}_route"]=(outputs[v].get(case["id"]) or {}).get("route","")
        lines.append(record)
    out=Path(__file__).parent/"comparison_scores.csv"
    with out.open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=list(lines[0]));w.writeheader();w.writerows(lines)
    summary={}
    for v in ("v11","v12"):
        summary[v]={k:sum(r[f"{v}_{k}"] for r in lines) for k in ("present","route_ok","format_ok","brief_ok","unsupported_verified")}
    print(json.dumps({"case_count":len(CASES),"summary":summary,"comparison_file":str(out),"IMPORTANT":"Mechanical checks only; routes require manual and blind quality evaluation; policy claims not verified here."},indent=2))
if __name__=="__main__":main()
