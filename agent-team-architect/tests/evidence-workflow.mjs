import { runEvidenceWorkflow } from "../scripts/evidence-workflow.mjs";
import { runWorkflow, verify } from "../scripts/reference-workflow.mjs";

function fixtures(){
  const definitions=[
["clean","completed",true],["repair_one","completed",true],["repair_two","completed",true],["stagnation","failed",true],["regression","failed",true],["worker_error","failed",true],["invalid_candidate","failed",true],["denied","cancelled",true],["pending","awaiting_approval",true],["approved","completed",true],["dishonest_100","failed",true],["dishonest_85","failed",true],["contradictory","failed",true],["malformed","failed",true],["missing_evidence","unverified",false],["verifier_error","unverified",false],["wrong_method","unverified",false],["unbound_approval","awaiting_approval",true],["changed_approval","awaiting_approval",true],["duplicate_criteria","failed",false],["bad_weights","failed",false],["mandatory_floor","failed",false],["threshold_precision","failed",false],["optional_unknown","unverified",false],["same_model_critical","unverified",false],["empty_rubric","failed",false],["invalid_score","unverified",false],["unknown_criterion","failed",false],["candidate_mutation","unverified",false],["repair_error_retains_best","failed",true]];
  return definitions;
}

async function benchmark(run,legacy,legacyVerify,legacyReconcile){
  const rows=[];
  const input={orders:[{id:"A",amount:12000},{id:"B",amount:8500},{id:"C",amount:5000}],payments:[{id:"A",amount:12000},{id:"C",amount:4500},{id:"D",amount:2000}]};
  const expected={matched:["A"],missing:["B"],mismatched:["C"],unallocated:["D"],orderTotal:25500,paymentTotal:18500};
  const fields=Object.keys(expected);
  const bad={...expected,missing:[],paymentTotal:18000}, partial={...expected,missing:[]}, worse={};
  const same=(x,y)=>JSON.stringify(x)===JSON.stringify(y);
  const rubric=()=>fields.map((id,i)=>({id,weight:[15,20,15,10,20,20][i],method:"deterministic",min:100,required:true,source:"fixture-oracle"}));
  const verifiers=()=>({"fixture-oracle":{method:"deterministic",independent:true,check:({criterion,candidate})=>({score:same(candidate[criterion.id],expected[criterion.id])?100:0,evidence:[{ref:"fixture:"+criterion.id,detail:"Compared the supplied candidate field with the fixed expected field."}]})}});
  for(const [name,want,shared] of fixtures()){
    let calls=0;
    let seq=[expected],oldApproval="not_required",permission=null,legacyChecker=legacyVerify,rs=rubric(),vs=verifiers(),critic,threshold=85,extra={};
    const grant=({request})=>({status:"approved",request});
    const requiredApproval={action:"publish",payload:{destination:"disposable-fixture"},authorize:grant};
    switch(name){
      case "repair_one":seq=[bad,expected];break;
      case "repair_two":seq=[bad,partial,expected];break;
      case "stagnation":seq=[bad];break;
      case "regression":seq=[partial,worse,worse];break;
      case "worker_error":seq=[new Error("worker failed")];break;
      case "invalid_candidate":seq=[null];break;
      case "denied":oldApproval="denied";permission={...requiredApproval,authorize:()=>({status:"denied"})};break;
      case "pending":oldApproval="pending";permission={...requiredApproval,authorize:()=>({status:"pending"})};break;
      case "approved":oldApproval="approved";permission=requiredApproval;break;
      case "dishonest_100":seq=[bad];legacyChecker=()=>({score:100,blockers:[],fixes:[]});critic=()=>({score:100,blockers:[],fixes:[]});break;
      case "dishonest_85":seq=[bad];legacyChecker=()=>({score:85,blockers:[],fixes:[]});critic=legacyChecker;break;
      case "contradictory":seq=[bad];legacyChecker=()=>({score:96,blockers:[],fixes:["Correct missing"]});critic=legacyChecker;break;
      case "malformed":seq=[bad];legacyChecker=()=>({score:100});critic=legacyChecker;break;
      case "missing_evidence":vs["fixture-oracle"].check=()=>({score:100,evidence:[]});break;
      case "verifier_error":vs["fixture-oracle"].check=()=>{throw Error("source offline")};break;
      case "wrong_method":vs["fixture-oracle"].method="model";break;
      case "unbound_approval":oldApproval="approved";permission={...requiredApproval,authorize:()=>({status:"approved"})};break;
      case "changed_approval":oldApproval="approved";permission={...requiredApproval,authorize:({request})=>({status:"approved",request:{...request,payload:{destination:"other"}}})};break;
      case "duplicate_criteria":rs.push(rs[0]);break;
      case "bad_weights":rs[0].weight=14;break;
      case "mandatory_floor":seq=[partial];rs=rs.map(x=>({...x,weight:x.id==="missing"?1:x.id==="matched"?34:x.weight}));break;
      case "threshold_precision":rs=[{id:"rating",weight:100,method:"human",min:0,required:false,source:"editor"}];vs={editor:{method:"human",independent:true,check:()=>({score:84.999,evidence:[{ref:"human-fixture",detail:"Synthetic rating for threshold boundary."}]})}};break;
      case "optional_unknown":rs[0].required=false;vs["fixture-oracle"].check=({criterion,candidate})=>criterion.id==="matched"?{score:null,evidence:[]}:{score:same(candidate[criterion.id],expected[criterion.id])?100:0,evidence:[{ref:"fixture:"+criterion.id,detail:"Fixed field comparison"}]};break;
      case "same_model_critical":rs=[{id:"claim",weight:100,method:"model",min:100,required:true,source:"editor"}];vs={editor:{method:"model",independent:false,check:()=>({score:100,evidence:[{ref:"self",detail:"Self claim"}]})}};break;
      case "empty_rubric":rs=[];break;
      case "invalid_score":vs["fixture-oracle"].check=()=>({score:101,evidence:[{ref:"bad",detail:"Out of range"}]});break;
      case "unknown_criterion":rs[0].method="invented";break;
      case "candidate_mutation":vs["fixture-oracle"].check=({candidate})=>{candidate.missing.push("forged");return {score:100,evidence:[{ref:"forged",detail:"Changed candidate"}]}};break;
      case "repair_error_retains_best":seq=[partial,new Error("repair failed")];break;
    }
    const worker=()=>{const v=seq[Math.min(calls++,seq.length-1)];if(v instanceof Error)throw v;return JSON.parse(JSON.stringify(v));};
    const out=await run({runId:"test:"+name,input,worker,rubric:rs,verifiers:vs,permission,critic,threshold,...extra});
    let pass=out.status===want;
    if(name==="regression"||name==="repair_error_retains_best")pass=pass&&out.best?.candidate?.paymentTotal===18500&&out.best?.review?.score===80&&out.accepted===null;
    if(name==="mandatory_floor")pass=pass&&out.best?.review?.score===99&&out.best?.review?.blockers.length>0;
    if(name==="threshold_precision")pass=pass&&out.best?.review?.score===84.999;
    if(name==="optional_unknown")pass=pass&&out.best?.review?.score===null&&out.best?.review?.coverage===85;
    if(name==="approved")pass=pass&&out.approval?.status==="approved"&&out.executedExternalAction===false;
    let old=null;
    if(shared){calls=0;const o=await legacy({input,worker,checker:legacyChecker,approval:oldApproval});old={status:o.status,pass:o.status===want,scores:o.trace.filter(t=>t.role==="checker").map(t=>t.score)};}
    rows.push({name,want,pass,status:out.status,legacy:old,scores:out.trace.filter(t=>t.phase==="review").map(t=>t.score),best:out.best?.review?.score??null});
  }
  // Every bit mask of six fixture fields, including the clean case. Shared oracle outcomes.
  let masksNew=0,masksOld=0,maskCount=0;
  const distributions={old:{},next:{}};
  for(let mask=0;mask<64;mask++){
    const candidate={...expected};fields.forEach((k,i)=>{if(mask&(1<<i))candidate[k]=null;});
    const want=mask===0?"completed":"failed";
    const a=await run({runId:"mask:"+mask,input,worker:()=>candidate,rubric:rubric(),verifiers:verifiers(),maxRepairs:0});
    const b=await legacy({input,worker:()=>candidate,checker:legacyVerify,maxRepairs:0});
    if(a.status===want)masksNew++;if(b.status===want)masksOld++;maskCount++;
    const n=a.best?.review?.score??"unknown",o=b.review?.score??"unknown";
    distributions.next[n]=(distributions.next[n]||0)+1;distributions.old[o]=(distributions.old[o]||0)+1;
  }
  const dynamic=[];
  for(const count of [1,2,3,7,10,17,25]){
    const rr=Array.from({length:count},(_,i)=>({id:"r"+i,weight:(i===count-1?100-(count-1)*Math.floor(100/count):Math.floor(100/count)),method:"deterministic",required:true,min:100,source:"oracle"}));
    const out=await run({runId:"dynamic:"+count,input:{},worker:()=>({ok:true}),rubric:rr,verifiers:{oracle:{method:"deterministic",independent:true,check:({criterion})=>({score:criterion.id==="r0"?0:100,evidence:[{ref:criterion.id,detail:"synthetic criterion"}]})}},maxRepairs:0});
    dynamic.push({count,score:out.best?.review?.score,expected:100-rr[0].weight,pass:out.status==="failed"&&out.best?.review?.score===100-rr[0].weight});
  }
  const shared=rows.filter(r=>r.legacy);
  return {rows,shared:{count:shared.length,legacyPassed:shared.filter(r=>r.legacy.pass).length,nextPassed:shared.filter(r=>r.pass).length},all:{count:rows.length,passed:rows.filter(r=>r.pass).length},masks:{count:maskCount,legacyPassed:masksOld,nextPassed:masksNew,distributions},dynamic};
}

const report=await benchmark(runEvidenceWorkflow,runWorkflow,verify);
console.log(JSON.stringify(report,null,2));
if(report.all.passed!==report.all.count||report.masks.nextPassed!==64||report.dynamic.some(x=>!x.pass))process.exitCode=1;
