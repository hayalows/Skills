import { runEvidenceWorkflow } from "../scripts/evidence-workflow.mjs";

async function domainBenchmark(run){
  const cases=[];
  const source=(check)=>({method:"deterministic",independent:true,check});
  const criterion=(id,weight=100,method="deterministic",required=true,min=100,source="oracle")=>({id,weight,method,required,min,source});
  const obs=(ok,ref,detail)=>({score:ok?100:0,evidence:[{ref,detail}]});
  const pair=(id,domain,want,input,candidate,rubric,verifiers,rest={})=>cases.push({id,domain,want,config:{runId:"domain:"+id,input,worker:()=>candidate,rubric,verifiers,maxRepairs:0,...rest}});
  const records={benchmarkVersion:"3.0",pilotPairs:6,independent:false};
  const auditChecks=source(({candidate,input,criterion:c})=>obs(candidate[c.id]===input[c.id],"synthetic-source:"+c.id,"Compared exact fixture field."));
  const auditRubric=[criterion("benchmarkVersion",50),criterion("pilotPairs",20),criterion("independent",30)];
  pair("audit-correct","research","completed",records,records,auditRubric,{oracle:auditChecks});
  pair("audit-version-misattribution","research","failed",records,{...records,benchmarkVersion:"3.0.6"},auditRubric,{oracle:auditChecks});
  pair("audit-fake-independent-review","research","failed",records,{...records,independent:true},auditRubric,{oracle:auditChecks});
  const receipt={completedTests:["t1","t2","t3"]};
  const runProof=source(({candidate,input})=>obs(candidate.testsPassed===input.completedTests.length,"synthetic-tool-receipts","Counted actual fixture receipt entries, not the worker's asserted total."));
  pair("execution-claim-correct","engineering","completed",receipt,{testsPassed:3},[criterion("count")],{oracle:runProof});
  pair("execution-claim-invented","engineering","failed",receipt,{testsPassed:11},[criterion("count")],{oracle:runProof});
  const money={rows:[12000,8500,5000],unit:"pesewas"};
  const finance=source(({criterion:c,candidate,input})=>obs(c.id==="total"?candidate.total===input.rows.reduce((a,b)=>a+b,0):candidate.unit===input.unit,"synthetic-ledger:"+c.id,"Verified arithmetic or unit."));
  const financeRubric=[criterion("total",70),criterion("unit",30)];
  pair("finance-correct","finance","completed",money,{total:25500,unit:"pesewas"},financeRubric,{oracle:finance});
  pair("finance-unit-error","finance","failed",money,{total:25500,unit:"cedis"},financeRubric,{oracle:finance});
  const writing={required:"I think",forbidden:"When I lost my first business"};
  const textCheck=source(({candidate,input,criterion:c})=>obs(c.id==="certainty"?candidate.text.includes(input.required):!candidate.text.includes(input.forbidden),"synthetic-brief:"+c.id,"Checked the fixture's literal constraint; not general semantic analysis."));
  const textRubric=[criterion("certainty",25),criterion("inventedExperience",25),criterion("voice",50,"human",true,70,"editor")];
  const rating={method:"human",independent:true,check:()=>({score:82,evidence:[{ref:"synthetic-editor-rating",detail:"Simulated supplied editorial rating; no real human evaluated this text."}]})};
  pair("writing-with-supplied-rating","writing","completed",writing,{text:"I think the cost matters."},textRubric,{oracle:textCheck,editor:rating});
  pair("writing-missing-user-judgment","writing","unverified",writing,{text:"I think the cost matters."},textRubric,{oracle:textCheck});
  pair("writing-invented-experience","writing","failed",writing,{text:"I think so. When I lost my first business, I learned."},textRubric,{oracle:textCheck,editor:rating});
  pair("writing-altered-certainty","writing","failed",writing,{text:"The cost is the only thing that matters."},textRubric,{oracle:textCheck,editor:rating});
  pair("trusted-adversarial-veto","research","failed",records,records,[criterion("benchmarkVersion",99),criterion("adversarial",1,"model",true,100,"reviewer")],{oracle:auditChecks,reviewer:{method:"model",independent:true,check:()=>({score:0,evidence:[{ref:"synthetic-review-veto",detail:"Simulated independent reviewer found a material unresolved issue."}]})}});
  const result=[];
  for(const c of cases){
    const r=await run(c.config);
    result.push({id:c.id,domain:c.domain,expected:c.want,status:r.status,pass:r.status===c.want,score:r.best?.review?.score??null,coverage:r.best?.review?.coverage??null,blockers:r.best?.review?.blockers??[],range:r.best?.review?.range??null});
  }
  // An intentionally compromised host verifier is outside the protection boundary.
  const boundary=await run({runId:"boundary:compromised-host",input:records,worker:()=>({benchmarkVersion:"wrong"}),rubric:[criterion("benchmarkVersion")],verifiers:{oracle:source(()=>obs(true,"fabricated","Intentionally dishonest trusted adapter"))},maxRepairs:0});
  return {count:result.length,passed:result.filter(x=>x.pass).length,result,trustBoundary:{status:boundary.status,expectedLimitation:"A compromised trusted host adapter can fabricate evidence and award a pass. The runtime cannot authenticate a source from its text alone.",countedAsProtection:false}};
}

const report=await domainBenchmark(runEvidenceWorkflow);
console.log(JSON.stringify(report,null,2));
if(report.count!==report.passed)process.exitCode=1;
