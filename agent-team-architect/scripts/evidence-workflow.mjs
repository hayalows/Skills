function canonical(value){
  if(value===null||typeof value==="boolean"||typeof value==="string")return JSON.stringify(value);
  if(typeof value==="number"&&Number.isFinite(value))return JSON.stringify(value);
  if(Array.isArray(value))return "["+value.map(canonical).join(",")+"]";
  if(value&&typeof value==="object"&&[Object.prototype,null].includes(Object.getPrototypeOf(value))){
    const keys=Object.keys(value).sort();
    return "{"+keys.map(k=>JSON.stringify(k)+":"+canonical(value[k])).join(",")+"}";
  }
  throw Error("non-JSON value");
}

function snapshot(value){
  const s=JSON.parse(canonical(value));
  const freeze=v=>{if(v&&typeof v==="object"){Object.values(v).forEach(freeze);Object.freeze(v);}return v;};
  return freeze(s);
}

function lockRubric(rubric,threshold){
  if(!Number.isFinite(threshold)||threshold<0||threshold>100||!Array.isArray(rubric)||!rubric.length)throw Error("invalid rubric");
  const seen=new Set();
  for(const c of rubric){
    if(!c||typeof c.id!=="string"||!c.id.trim()||seen.has(c.id)||!Number.isInteger(c.weight)||c.weight<=0||typeof c.required!=="boolean"||!Number.isFinite(c.min)||c.min<0||c.min>100||!["deterministic","human","model"].includes(c.method)||typeof c.source!=="string"||!c.source.trim())throw Error("invalid criterion");
    seen.add(c.id);
  }
  if(rubric.reduce((s,c)=>s+c.weight,0)!==100)throw Error("weights must total 100");
  return snapshot(rubric);
}

async function assess({rubric,threshold,verifiers,candidate,input,runId,round}){
  const criteria=[],blockers=[],fixes=[];
  let known=0,coverage=0;
  for(const c of rubric){
    let observation,reason=null;
    const v=verifiers[c.source];
    if(!v||v.method!==c.method||typeof v.check!=="function")reason="trusted adapter unavailable or method mismatch";
    else if(c.required&&c.method==="model"&&!v.independent)reason="same-model judgement cannot satisfy mandatory criterion";
    else{
      try{
        observation=await v.check({criterion:c,candidate,input,runId,round});
        if(!observation||!Number.isFinite(observation.score)||observation.score<0||observation.score>100||!Array.isArray(observation.evidence)||!observation.evidence.length||!observation.evidence.every(e=>e&&typeof e.ref==="string"&&e.ref.trim()&&typeof e.detail==="string"&&e.detail.trim()))reason="missing or invalid evidence or score";
        else if(c.method==="deterministic"&&![0,100].includes(observation.score))reason="deterministic criterion must be binary; split graded checks";
      }catch{reason="verifier unavailable or failed";}
    }
    if(reason){criteria.push({id:c.id,method:c.method,source:c.source,weight:c.weight,required:c.required,score:null,evidence:[],reason});if(c.required)blockers.push(c.id+": "+reason);continue;}
    const score=observation.score;known+=score*c.weight/100;coverage+=c.weight;
    const evidence=snapshot(observation.evidence.map(e=>({ref:e.ref,detail:e.detail})));
    criteria.push({id:c.id,method:c.method,source:c.source,independent:v.independent===true,weight:c.weight,required:c.required,score,evidence});
    if(c.required&&score<c.min)blockers.push(c.id+": mandatory floor failed");
    if(score<c.min||score<100)fixes.push({criterion:c.id,instruction:typeof observation.fix==="string"&&observation.fix.trim()?observation.fix:"Review "+c.id+" against the locked criterion and its evidence."});
  }
  const score=coverage===100?known:null;
  const verdict=criteria.some(x=>x.score===null)?"unverified":blockers.length||score<threshold?"failed":"passed";
  return snapshot({score,coverage,range:[known,known+100-coverage],criteria,blockers,fixes,verdict,threshold});
}

function better(candidate,best){
  if(!best)return true;
  const a=candidate.review,b=best.review;
  const rank=r=>r.verdict==="passed"?2:r.verdict==="failed"?1:0;
  if(rank(a)!==rank(b))return rank(a)>rank(b);
  if(a.blockers.length!==b.blockers.length)return a.blockers.length<b.blockers.length;
  if(a.coverage!==b.coverage)return a.coverage>b.coverage;
  return a.range[0]>b.range[0];
}

async function runEvidenceWorkflow({runId,input,worker,rubric,verifiers={},threshold=85,maxRepairs=2,permission=null,critic=null}){
  let best=null,accepted=null,approval=null,trace=[],repairs=0,locked,scope,adapters,task;
  const finish=(status,reason)=>({status,reason,repairs,best,accepted,approval,trace,executedExternalAction:false});
  try{
    if(typeof runId!=="string"||!runId.trim()||typeof worker!=="function"||!Number.isInteger(maxRepairs)||maxRepairs<0||maxRepairs>2)throw Error("invalid run configuration");
    locked=lockRubric(rubric,threshold);task=snapshot(input);
    adapters=Object.freeze(Object.fromEntries(Object.entries(verifiers).map(([id,v])=>[id,Object.freeze({method:v.method,independent:v.independent===true,check:v.check})])));
    if(permission!==null){if(typeof permission.action!=="string"||!permission.action.trim()||!Object.hasOwn(permission,"payload"))throw Error("invalid approval scope");scope={action:permission.action,payload:snapshot(permission.payload),authorize:permission.authorize};}
  }catch(e){return finish("failed",String(e.message||e));}
  let fixes=snapshot([]);
  for(let round=0;round<=maxRepairs;round++){
    let candidate,review;
    try{
      const output=await worker(task,fixes,{runId,round});
      if(!output||typeof output!=="object"||Array.isArray(output))throw Error("invalid candidate");
      candidate=snapshot(output);
    }catch(e){return finish("failed","worker failure: "+String(e.message||e));}
    try{review=await assess({rubric:locked,threshold,verifiers:adapters,candidate,input:task,runId,round});}
    catch(e){return finish("unverified","assessment failed");}
    const record=snapshot({candidate,review,round});
    if(better(record,best))best=record;
    trace.push({phase:"review",round,score:review.score,coverage:review.coverage,blockers:review.blockers.length,verdict:review.verdict,bestRound:best.round});
    // Critic is advisory. It cannot award a pass or forge a verifier observation.
    if(critic){try{await critic({candidate,review,runId,round});trace.push({phase:"advisory",round,status:"returned_not_authoritative"});}catch{trace.push({phase:"advisory",round,status:"unavailable"});}}
    if(review.verdict==="passed"){
      if(scope){
        const request=snapshot({runId,round,action:scope.action,payload:scope.payload,candidate});
        let decision;try{decision=typeof scope.authorize==="function"?await scope.authorize({request}):null;}catch{decision=null;}
        if(decision?.status==="denied"){approval={status:"denied"};return finish("cancelled","approval denied");}
        let bound=false;try{bound=decision?.status==="approved"&&canonical(decision.request)===canonical(request);}catch{}
        if(!bound){approval={status:"pending"};return finish("awaiting_approval","exact run, candidate and action approval required");}
        approval={status:"approved",action:scope.action};
      }
      accepted=record;return finish("completed","verified against declared rubric; external action not executed");
    }
    if(review.verdict==="unverified")return finish("unverified","evidence incomplete; do not invent a score or repair unavailable evidence");
    if(round===maxRepairs)return finish("failed","repair cap reached");
    if(!review.fixes.length)return finish("failed","no actionable fix");
    fixes=review.fixes;repairs++;
  }
  return finish("failed","unexpected termination");
}

export { runEvidenceWorkflow };
