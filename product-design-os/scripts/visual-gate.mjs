#!/usr/bin/env node
// Report completeness checker. Does not inspect screenshots or establish truth of evidence.
import fs from "node:fs";
import { pathToFileURL } from "node:url";
export function checkVisualGate(report){
  const required=Array.from({length:12},(_,i)=>"VI"+String(i+1).padStart(2,"0"));
  const issues=[];
  const hasText=x=>typeof x==="string"&&x.trim().length>0;
  const validEvidence=e=>e&&["seen","operated","measured","read"].includes(e.kind)&&hasText(e.ref);
  if(!report||!Array.isArray(report.surfaces)||!report.surfaces.length)return {pass:false,issues:["Provide at least one named surface with rule records."]};
  const names=new Set();
  for(const surface of report.surfaces){
    if(!surface||!hasText(surface.name)||!Array.isArray(surface.rules)){issues.push("Invalid surface name or rules.");continue;}
    const name=surface.name;
    if(names.has(name))issues.push(name+": duplicate surface.");
    names.add(name);
    const seen=new Set();
    for(const row of surface.rules){
      if(!row||!required.includes(row.id)){issues.push(name+": unknown rule ID.");continue;}
      const label=name+" / "+row.id;
      if(seen.has(row.id))issues.push(label+": duplicate rule.");
      seen.add(row.id);
      if(!["PASS","FAIL","EXCEPTION","NV","NA"].includes(row.status)){issues.push(label+": invalid status.");continue;}
      if(["FAIL","NV"].includes(row.status)){issues.push(label+": "+row.status+" blocks visual approval.");continue;}
      if(!hasText(row.reason))issues.push(label+": provide a specific reason or observation.");
      if(row.status==="NA")continue;
      if(!hasText(row.scope))issues.push(label+": identify viewport/state/element scope.");
      const ev=Array.isArray(row.evidence)?row.evidence:[];
      if(!ev.length||!ev.every(validEvidence))issues.push(label+": evidence records require kind and reference.");
      if(!ev.some(e=>validEvidence(e)&&e.kind!=="read"))issues.push(label+": source reading alone cannot pass rendered visual checks.");
      if(["VI01","VI02","VI04","VI05","VI08","VI09","VI11","VI12"].includes(row.id)&&!ev.some(e=>validEvidence(e)&&e.kind==="seen"))issues.push(label+": inspected screenshot or rendering evidence required.");
      if(row.status==="EXCEPTION"&&(!hasText(row.need)||!hasText(row.alternative)))issues.push(label+": exception requires user/brand need and why a compliant alternative harms it.");
      if(row.fixed===true&&(!Array.isArray(row.retest)||!row.retest.some(e=>validEvidence(e)&&e.kind!=="read")))issues.push(label+": fixed finding requires retest evidence.");
    }
    for(const id of required)if(!seen.has(id))issues.push(name+" / "+id+": missing rule record; mark NA with reason if not applicable.");
    if(surface.rules.every(r=>r?.status==="NA"))issues.push(name+": all-NA surface cannot receive visual approval.");
  }
  return {pass:issues.length===0,issues};
}
if(process.argv[1]&&import.meta.url===pathToFileURL(process.argv[1]).href){
  try{
    if(process.argv.length!==3)throw Error("Usage: node visual-gate.mjs report.json");
    const result=checkVisualGate(JSON.parse(fs.readFileSync(process.argv[2],"utf8")));
    console.log(JSON.stringify(result,null,2));
    process.exitCode=result.pass?0:1;
  }catch(error){console.error(error.message);process.exitCode=2;}
}
