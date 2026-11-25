import assert from "node:assert/strict";
import { checkVisualGate } from "../scripts/visual-gate.mjs";
// Synthetic records only. No actual visual inspection is represented by these fixtures.
const complete=()=>({surfaces:[{name:"example",rules:Array.from({length:12},(_,i)=>({id:"VI"+String(i+1).padStart(2,"0"),status:"PASS",reason:"Fixture observation, not real evidence",scope:"Fixture viewport",evidence:[{kind:"seen",ref:"fixture.png"}]}))}]});
const tests=[["complete",r=>{},true],
["missing",r=>r.surfaces[0].rules.pop(),false],
["unknown",r=>r.surfaces[0].rules[0].id="VI99",false],
["duplicate",r=>r.surfaces[0].rules[0].id="VI02",false],
["fail",r=>r.surfaces[0].rules[0].status="FAIL",false],
["nv",r=>r.surfaces[0].rules[0].status="NV",false],
["exception without justification",r=>r.surfaces[0].rules[0].status="EXCEPTION",false],
["justified exception",r=>Object.assign(r.surfaces[0].rules[0],{status:"EXCEPTION",need:"Fixture requirement",alternative:"Fixture tradeoff"}),true],
["missing evidence",r=>r.surfaces[0].rules[0].evidence=[],false],
["read only",r=>r.surfaces[0].rules[0].evidence=[{kind:"read",ref:"source.tsx"}],false],
["measured not seen",r=>r.surfaces[0].rules[0].evidence=[{kind:"measured",ref:"probe.json"}],false],
["NA documented",r=>r.surfaces[0].rules[0]={id:"VI01",status:"NA",reason:"Out of scope for this fixture"},true],
["NA undocumented",r=>r.surfaces[0].rules[0]={id:"VI01",status:"NA"},false],
["all NA",r=>r.surfaces[0].rules.forEach(x=>x.status="NA"),false],
["missing scope",r=>delete r.surfaces[0].rules[0].scope,false],
["fixed no retest",r=>r.surfaces[0].rules[0].fixed=true,false],
["fixed with retest",r=>Object.assign(r.surfaces[0].rules[0],{fixed:true,retest:[{kind:"seen",ref:"after.png"}]}),true],
["duplicate surface",r=>r.surfaces.push(r.surfaces[0]),false],
["no surfaces",r=>r.surfaces=[],false],
["bad evidence",r=>r.surfaces[0].rules[0].evidence=[{kind:"seen",ref:""}],false],
["bad status",r=>r.surfaces[0].rules[0].status="OK",false]];
for(const [name,change,expected] of tests){const report=complete();change(report);assert.equal(checkVisualGate(report).pass,expected,name);}
console.log("PASS: "+tests.length+" visual report gate fixtures");
