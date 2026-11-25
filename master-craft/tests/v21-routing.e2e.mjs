import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";
import { fileURLToPath } from "node:url";
import { plan } from "../scripts/plan.mjs";
import { routingError, parseRoutingBlock } from "../scripts/routing-policy.mjs";
import { checkExecution } from "../scripts/execution.mjs";
const file = x => fileURLToPath(new URL(x, import.meta.url));
const local = JSON.parse(execFileSync(process.execPath, [file("../scripts/inventory.mjs"), "--local", "--json"], {encoding:"utf8"}));
const snapshot = {...local,source:"git-origin-main",verified_latest:true};
const base = {mode:"create",host:"none",substantial:true,productDesign:false,measureProduct:false,validateModel:false,hostedBuild:false,releaseAuthorized:false,freshnessRequired:false,releaseToolAvailable:false};
const p = n => snapshot.skills.find(s=>s.name===n).path;
const run = (names,extra={},s=snapshot) => plan({...base,specialists:names.map(n=>p(n)),...extra},s);
let checks=0;
function test(name,fn){fn();checks++;console.log("PASS "+name);}
test("every active skill has valid metadata and a unique name",()=>{
  assert.equal(snapshot.skills.filter(s=>s.error).length,0);
  assert.equal(new Set(snapshot.skills.map(s=>s.name)).size,snapshot.skills.length);
  assert.ok(snapshot.skills.length>=67);
});
test("every eligible skill routes individually",()=>{
  for(const skill of snapshot.skills){
    if(skill.name==="master-craft") continue;
    const r=plan({...base,mode:skill.routing?.allowed_modes?.[0]??base.mode,specialists:[skill.path],explicitSkills:skill.requires_explicit_invocation?[skill.path]:[]},snapshot);
    assert.ok(r.skills.includes(skill.path),skill.name);
    assert.deepEqual(r.blockers,[],skill.name);
  }
});
test("all actual competing design lead pairs block",()=>{
  const leads=snapshot.skills.filter(s=>s.routing?.exclusive_role==="ui-lead");
  assert.ok(leads.length>=5);
  for(let i=0;i<leads.length;i++)for(let j=i+1;j<leads.length;j++){
    const r=plan({...base,specialists:[leads[i].path,leads[j].path]},snapshot);
    if ([leads[i],leads[j]].some(s=>s.routing?.allowed_modes&&!s.routing.allowed_modes.includes(base.mode))) assert.ok(r.blockers.some(b=>b.startsWith("skill-mode-rejected:")));
    else assert.ok(r.blockers.includes("exclusive-role-conflict:ui-lead"));
    assert.ok(!r.stages.includes("implement"));
    const inspect=plan({...base,mode:"inspect",specialists:[leads[i].path,leads[j].path]},snapshot);
    assert.ok(inspect.blockers.includes("exclusive-role-conflict:ui-lead"));
  }
});
test("actual product design and compatible visual helpers",()=>{
  const r=run(["gemini-frontend-design","frontend-design","ui-ux-craft"],{productDesign:true,specialistRoles:{[p("gemini-frontend-design")]:"supporting"}});
  assert.deepEqual(r.blockers,[]);
  assert.equal(r.specialistRoles[p("product-design-os")],"lead");
  assert.equal(r.specialistRoles[p("frontend-design")],"supporting");
});
test("marketing lead and Gemini helper work together",()=>{
  const r=run(["design-taste-frontend","gemini-frontend-design"],{specialistRoles:{[p("gemini-frontend-design")]:"helper"}});
  assert.deepEqual(r.blockers,[]);
  assert.equal(r.specialistRoles[p("gemini-frontend-design")],"supporting");
});
test("lead-only skills cannot masquerade as supporting or specialist",()=>{
  for(const role of ["helper","supporting","specialist","unknown",false,null]){
    const r=run(["design-taste-frontend"],{productDesign:true,specialistRoles:{[p("design-taste-frontend")]:role}});
    assert.ok(r.blockers.includes("invalid-specialist-role:"+p("design-taste-frontend")));
    assert.ok(r.blockers.includes("exclusive-role-conflict:ui-lead"));
    assert.ok(!r.stages.includes("implement"));
  }
});
test("mandatory product lead cannot be demoted",()=>{
  const r=run(["gemini-frontend-design"],{productDesign:true,specialistRoles:{[p("product-design-os")]:"helper"}});
  assert.ok(r.blockers.includes("invalid-specialist-role:"+p("product-design-os")));
});
test("invalid and stray role assignments blocked",()=>{
  assert.ok(run(["agent-team-architect"],{specialistRoles:{[p("agent-team-architect")]:"unrecognized"}}).blockers.includes("invalid-specialist-role:"+p("agent-team-architect")));
  assert.ok(run([],{specialistRoles:{[p("agent-team-architect")]:"lead"}}).blockers.includes("role-for-unselected-skill:"+p("agent-team-architect")));
});
test("orchestration guard and authorized override remain intact",()=>{
  for(const name of ["agent-team-architect","ai-ops-team"]){
    if(name==="ai-ops-team") assert.throws(()=>run([name],{mode:"answer",substantial:false}),/requires explicit invocation/);
    else assert.ok(run([name],{mode:"answer",substantial:false}).blockers.includes("trivial-task-skill-rejected:"+p(name)));
    const yes=run([name],{mode:"answer",substantial:false,explicitSkills:[p(name)]});
    assert.deepEqual(yes.blockers,[]);
  }
  const team=run(["agent-team-architect","ai-ops-team"],{explicitSkills:[p("ai-ops-team")]});
  assert.deepEqual(team.blockers,[]);
  assert.equal(team.specialistRoles[p("agent-team-architect")],"lead");
  assert.equal(team.specialistRoles[p("ai-ops-team")],"specialist");
});
test("future metadata applies without hardcoded skill names",()=>{
  const a={name:"future-a",path:"future-a/SKILL.md",description:"fixture",routing:{minimum_complexity:"substantial",roles:["lead"],exclusive_role:"future-lead"}};
  const b={name:"future-b",path:"future-b/SKILL.md",description:"fixture",routing:{roles:["lead","supporting"],exclusive_role:"future-lead"}};
  const s={...snapshot,skills:[...snapshot.skills,a,b]};
  assert.ok(plan({...base,substantial:false,specialists:[a.path],explicitSkills:[a.path]},s).blockers.includes("trivial-task-skill-rejected:"+a.path));
  assert.ok(plan({...base,specialists:[a.path,b.path]},s).blockers.includes("exclusive-role-conflict:future-lead"));
  assert.deepEqual(plan({...base,specialists:[a.path,b.path],specialistRoles:{[b.path]:"supporting"}},s).blockers,[]);
});
test("invalid metadata fails closed",()=>{
  for(const routing of [{roles:"lead"},{roles:["lead","lead"]},{roles:["helper"]},{roles:["supporting"],exclusive_role:"ui-lead"},{explicit_override:"true"},{minimum_complexity:"anything"},{default_role:"lead",roles:["supporting"]},{conflicts_with:"x"},{unexpected:true}]){
    assert.ok(routingError(routing));
    const s={...snapshot,skills:[...snapshot.skills,{name:"invalid",path:"invalid/SKILL.md",description:"fixture",routing}]};
    const r=plan({...base,specialists:["invalid/SKILL.md"]},s);
    assert.ok(r.blockers.includes("invalid-routing-metadata:invalid/SKILL.md"));
    assert.ok(!r.stages.includes("implement"));
  }
  assert.throws(()=>parseRoutingBlock(["  roles: [lead]","  roles: [supporting]"]));
  assert.throws(()=>parseRoutingBlock(["  roles:","   - lead"]));
  assert.deepEqual([...parseRoutingBlock(["  roles:","    - lead","    - supporting"]).roles],["lead","supporting"]);
});
test("all conflicts are reported and release is blocked",()=>{
  const a={name:"a",path:"a/SKILL.md",description:"fixture",routing:{conflicts_with:["b","c"]}};
  const b={name:"b",path:"b/SKILL.md",description:"fixture"};
  const c={name:"c",path:"c/SKILL.md",description:"fixture"};
  const r=plan({...base,mode:"release",host:"vercel",releaseAuthorized:true,releaseToolAvailable:true,specialists:[a.path,b.path,c.path]}, {...snapshot,skills:[...snapshot.skills,a,b,c]});
  assert.equal(r.blockers.filter(x=>x.startsWith("skill-conflict:")).length,2);
  assert.ok(!r.stages.includes("publish"));
});
test("legacy skills and explicit-only restrictions remain unchanged",()=>{
  assert.deepEqual(run(["lunour-naming"]).blockers,[]);
  const restricted=snapshot.skills.find(s=>s.requires_explicit_invocation);
  assert.throws(()=>plan({...base,specialists:[restricted.path]},snapshot),/requires explicit invocation/);
  assert.throws(()=>plan({...base,specialists:["master-craft/SKILL.md"]},snapshot),/recursive/);
});
test("sidecar is required in execution contract and helper cannot own lead plan",()=>{
  const s={...snapshot,skills:snapshot.skills.map(v=>v.name==="gemini-frontend-design"?{...v,routing_sha:"a".repeat(40)}:v)};
  const intent={...base,productDesign:true,specialists:[p("gemini-frontend-design")],specialistRoles:{[p("gemini-frontend-design")]:"supporting"}};
  const r=plan(intent,s);
  const input={objective:"Fixture",scope:"Fixture",target:"Fixture",targetRevision:"Fixture",allowedEffects:["inspect","write-target"],primary:p("gemini-frontend-design"),contracts:Object.fromEntries(r.skills.map(path=>[path,{why:"Fixture",procedure:"Fixture",restrictions:"Fixture",references:[],loadEvidence:"Fixture",revision:r.revision,stages:["verify"]}]))};
  const result=checkExecution(r,intent,s,input);
  assert.ok(result.issues.includes("supporting-skill-cannot-own-lead-plan"));
  assert.ok(result.issues.includes("skill-contract-invalid:"+p("gemini-frontend-design")));
});
console.log("PASS: "+checks+" V2.1 targeted checks, including all active specialists and real lead pairs");
