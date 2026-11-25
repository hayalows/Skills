function reconcile(input) {
  if (!input || !Array.isArray(input.orders) || !Array.isArray(input.payments)) throw Error("invalid input");
  const checkRows=(rows)=>{const seen=new Set(); for(const r of rows){if(!r || typeof r.id!=="string" || !r.id || !Number.isSafeInteger(r.amount) || r.amount<0 || seen.has(r.id))throw Error("invalid or duplicate row");seen.add(r.id);}};
  checkRows(input.orders);checkRows(input.payments);
  const p=new Map(input.payments.map(r=>[r.id,r.amount]));
  const o=new Map(input.orders.map(r=>[r.id,r.amount]));
  return {matched:input.orders.filter(r=>p.get(r.id)===r.amount).map(r=>r.id),missing:input.orders.filter(r=>!p.has(r.id)).map(r=>r.id),mismatched:input.orders.filter(r=>p.has(r.id)&&p.get(r.id)!==r.amount).map(r=>r.id),unallocated:input.payments.filter(r=>!o.has(r.id)).map(r=>r.id),orderTotal:input.orders.reduce((a,r)=>a+r.amount,0),paymentTotal:input.payments.reduce((a,r)=>a+r.amount,0)};
}

async function runWorkflow({input,worker,checker,approval="not_required",maxRepairs=2}) {
  if(!Number.isInteger(maxRepairs)||maxRepairs<0||maxRepairs>2)throw Error("invalid repair cap");
  let repairs=0, candidate, review, fixes=[], trace=[];
  const finish=(status,error)=>({status,repairs,candidate,review,trace,...(error?{error}:{} )});
  try {
    if(!["not_required","approved","pending","denied"].includes(approval))throw Error("invalid approval");
    for(;;){
      trace.push({role:"lead",repair:repairs});
      candidate=await worker(input,fixes);
      if(!candidate||typeof candidate!=="object"||Array.isArray(candidate))throw Error("invalid candidate");
      trace.push({role:"worker",repair:repairs});
      review=await checker(input,candidate);
      if(!review||!Number.isFinite(review.score)||review.score<0||review.score>100||!Array.isArray(review.blockers)||!Array.isArray(review.fixes)||!review.fixes.every(x=>typeof x==="string"&&x.length>0))throw Error("invalid review");
      trace.push({role:"checker",repair:repairs,score:review.score,blockers:review.blockers.length});
      if(review.score>=85&&review.blockers.length===0){
        trace.push({role:"approval",status:approval});
        return finish(approval==="denied"?"cancelled":approval==="pending"?"awaiting_approval":"completed");
      }
      if(repairs===maxRepairs)return finish("failed","repair cap reached");
      if(!review.fixes.length)return finish("failed","no actionable fix");
      fixes=review.fixes;repairs++;
    }
  } catch(e){return finish("failed",String(e.message||e));}
}

function verify(input,candidate){
  // Independently calculate each acceptance field using direct scans, not the worker function.
  const orders=input.orders,payments=input.payments;
  const expected={matched:[],missing:[],mismatched:[],unallocated:[],orderTotal:0,paymentTotal:0};
  for(const o of orders){expected.orderTotal+=o.amount;const p=payments.find(x=>x.id===o.id);expected[!p?"missing":p.amount===o.amount?"matched":"mismatched"].push(o.id);}
  for(const p of payments){expected.paymentTotal+=p.amount;if(!orders.some(o=>o.id===p.id))expected.unallocated.push(p.id);}
  const fixes=Object.keys(expected).filter(k=>JSON.stringify(expected[k])!==JSON.stringify(candidate[k])).map(k=>"Correct "+k);
  return {score:Math.round(100*(6-fixes.length)/6),blockers:fixes,fixes};
}

async function runTests(){
  const input={orders:[{id:"A",amount:12000},{id:"B",amount:8500},{id:"C",amount:5000}],payments:[{id:"A",amount:12000},{id:"C",amount:4500},{id:"D",amount:2000}]};
  const wrong={...reconcile(input),missing:[],paymentTotal:18000};
  const cases=[
    ["clean pass",reconcile,verify,"not_required","completed",0],
    ["targeted repair",(_,f)=>f.length?reconcile(input):wrong,verify,"not_required","completed",1],
    ["exhausted repair",()=>wrong,verify,"not_required","failed",2],
    ["denied approval",reconcile,verify,"denied","cancelled",0],
    ["pending approval",reconcile,verify,"pending","awaiting_approval",0],
    ["invalid worker output",()=>null,verify,"not_required","failed",0],
    ["worker error",()=>{throw Error("tool failure")},verify,"not_required","failed",0],
    ["malformed review",reconcile,()=>({score:100}),"not_required","failed",0],
    ["blocker overrides score",reconcile,()=>({score:100,blockers:["missing evidence"],fixes:["verify source"]}),"not_required","failed",2],
    ["nonactionable review",reconcile,()=>({score:50,blockers:["error"],fixes:[]}),"not_required","failed",0]
  ];
  const results=[];
  for(const [name,worker,checker,approval,status,repairs] of cases){const out=await runWorkflow({input,worker,checker,approval});results.push({name,pass:out.status===status&&out.repairs===repairs,status:out.status,repairs:out.repairs,checks:out.trace.filter(x=>x.role==="checker").length});}
  let rejected=false;try{reconcile({orders:[{id:"X",amount:1},{id:"X",amount:2}],payments:[]})}catch{rejected=true}
  results.push({name:"duplicate source row rejected",pass:rejected});
  const output=reconcile(input);
  results.push({name:"exact independent fixture totals and classifications",pass:JSON.stringify(output)===JSON.stringify({matched:["A"],missing:["B"],mismatched:["C"],unallocated:["D"],orderTotal:25500,paymentTotal:18500})});
  return {results,baseline:verify(input,wrong),repaired:await runWorkflow({input,worker:(_,f)=>f.length?reconcile(input):wrong,checker:verify}),output};
}

export { reconcile, runWorkflow, verify, runTests };
