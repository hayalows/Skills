import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";
import { fileURLToPath } from "node:url";
import { plan } from "../scripts/plan.mjs";
import { routingError } from "../scripts/routing-policy.mjs";
import { catalogue } from "../scripts/catalogue.mjs";

const inv=JSON.parse(execFileSync(process.execPath,[fileURLToPath(new URL("../scripts/inventory.mjs",import.meta.url)),"--local","--json"],{encoding:"utf8"}));
const base={mode:"inspect",host:"none",substantial:true,productDesign:false,measureProduct:false,validateModel:false,hostedBuild:false,releaseAuthorized:false,freshnessRequired:false,releaseToolAvailable:false};
const architect="agent-team-architect/SKILL.md", ops="ai-ops-team/SKILL.md", luna="luna-astra-behavior/SKILL.md", audit="website-ux-audit/SKILL.md";
let count=0;
const test=(name,fn)=>{fn();count++;console.log("PASS "+name);};
test("AI Ops and Luna Astra require explicit invocation at every complexity",()=>{
  for(const path of [ops,luna]) for(const substantial of [true,false]) {
    assert.throws(()=>plan({...base,substantial,specialists:[path]},inv),/requires explicit invocation/);
    const r=plan({...base,substantial,specialists:[path],explicitSkills:[path]},inv);
    assert.ok(r.skills.includes(path));assert.deepEqual(r.blockers,[]);
  }
});
test("Architect stays automatically eligible, without AI Ops",()=>{
  const r=plan({...base,specialists:[architect]},inv);
  assert.deepEqual(r.blockers,[]);assert.ok(r.skills.includes(architect));assert.ok(!r.skills.includes(ops));
});
test("explicit AI Ops can lead its own plan or work under Architect",()=>{
  const single=plan({...base,specialists:[ops],explicitSkills:[ops],specialistRoles:{[ops]:"lead"}},inv);
  assert.deepEqual(single.blockers,[]);
  const duo=plan({...base,specialists:[architect,ops],explicitSkills:[ops]},inv);
  assert.deepEqual(duo.blockers,[]);assert.equal(duo.specialistRoles[architect],"lead");assert.equal(duo.specialistRoles[ops],"specialist");
});
test("two orchestration leads block, even on explicit invocation",()=>{
  const r=plan({...base,mode:"create",specialists:[architect,ops],explicitSkills:[ops],specialistRoles:{[ops]:"lead"}},inv);
  assert.ok(r.blockers.includes("exclusive-role-conflict:workflow-lead"));assert.ok(!r.stages.includes("implement"));
});
test("read-only audit cannot be assigned mutable task modes",()=>{
  for(const mode of ["answer","create","repair","release"]) {
    const r=plan({...base,mode,specialists:[audit],explicitSkills:[audit]},inv);
    assert.ok(r.blockers.includes("skill-mode-rejected:"+audit+":"+mode));assert.ok(!r.skills.includes(audit));assert.ok(!r.stages.includes("implement"));assert.ok(!r.stages.includes("publish"));
  }
  assert.deepEqual(plan({...base,specialists:[audit]},inv).blockers,[]);
});
test("new allowed_modes policy fails closed for invalid values",()=>{
  for(const allowed_modes of ["inspect",[],["inspect","inspect"],["deploy"],[false]]) assert.ok(routingError({allowed_modes}));
  assert.equal(routingError({allowed_modes:["inspect","answer"]}),null);
});
test("unmapped new skills remain eligible with optional metadata",()=>{
  const fresh={path:"extension/fresh-skill/SKILL.md",name:"fresh-skill",description:"A new example skill without routing metadata."};
  const s={...inv,skills:[...inv.skills,fresh]};
  assert.deepEqual(plan({...base,specialists:[fresh.path]},s).blockers,[]);
  assert.ok(catalogue(s).includes("/"+fresh.path+")"));
});
test("all explicit-only skills remain protected",()=>{
  for(const skill of inv.skills.filter(s=>s.requires_explicit_invocation)) assert.throws(()=>plan({...base,specialists:[skill.path]},inv),/requires explicit invocation/);
});
console.log("PASS: "+count+" V2.3 regression groups");
