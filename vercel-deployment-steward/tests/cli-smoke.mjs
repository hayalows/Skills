#!/usr/bin/env node
// End-to-end checks through the same CLI a person or agent runs.
// No live credentials, deployments, or user projects are changed.
import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import { mkdtempSync, writeFileSync, rmSync } from "node:fs";
import { tmpdir } from "node:os";
import { join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const folder=mkdtempSync(join(tmpdir(),"deployment-steward-e2e-"));
const script=resolve(fileURLToPath(new URL("../scripts/audit-deployments.mjs",import.meta.url)));
const NOW="2026-11-04T22:30:00.000Z";
const timestamp=Date.parse(NOW);
let checks=0;

function deployment(i,{project="routelab",target=null,state="READY",branch="feat/example",repo="routelab",sha=null,daysAgo=0}={}) {
  return {
    id:"dpl_fixture_"+i,
    name:project,
    created:timestamp-daysAgo*86_400_000-i*1000,
    target,state,
    meta:{githubCommitRef:branch,githubCommitSha:sha||"sha_"+i,githubOrg:"hayalows",githubRepo:repo}
  };
}
function execute(records,{complete=true,cap=100,gate=true}={}) {
  const filename=join(folder,"snapshot-"+checks+".json");
  writeFileSync(filename,JSON.stringify({complete,deployments:records}),"utf8");
  const args=[script,"--snapshot",filename,"--now",NOW,"--cap",String(cap),"--json"];
  if(gate)args.push("--gate");
  const p=spawnSync(process.execPath,args,{encoding:"utf8",timeout:10_000});
  if(p.error)throw p.error;
  let result;
  try{result=JSON.parse(p.stdout);}catch(e){throw new Error("CLI returned invalid JSON: "+p.stdout+"\n"+p.stderr);}
  checks+=1;
  return {exit:p.status,result,stderr:p.stderr};
}
try {
  const green=execute(Array.from({length:20},(_,i)=>deployment(i)));
  assert.equal(green.exit,0,"safe usage should allow the gate");
  assert.equal(green.result.status,"GREEN");
  assert.equal(green.result.estimatedRemaining,80);

  const watch=execute(Array.from({length:56},(_,i)=>deployment(i)));
  assert.equal(watch.exit,0);
  assert.equal(watch.result.status,"WATCH");

  const protect=execute(Array.from({length:75},(_,i)=>deployment(i)));
  assert.equal(protect.exit,0);
  assert.equal(protect.result.status,"PROTECT");

  const freeze=execute(Array.from({length:85},(_,i)=>deployment(i)));
  assert.equal(freeze.exit,2,"low deployment headroom should block the gate");
  assert.equal(freeze.result.status,"FREEZE");

  const unknown=execute(Array.from({length:20},(_,i)=>deployment(i)),{complete:false});
  assert.equal(unknown.exit,3,"incomplete evidence must not green-light a release");
  assert.equal(unknown.result.status,"UNKNOWN");

  const stale=execute([
    deployment(1,{daysAgo:2}),
    deployment(2)
  ]);
  assert.equal(stale.result.count,1,"the audit must use a rolling 24-hour window");

  const fanout=execute([
    deployment(1,{project:"papa-kojo-cv",repo:"hayawebsite",sha:"same-commit"}),
    deployment(2,{project:"hayalows-studio",repo:"hayawebsite",sha:"same-commit"})
  ]);
  assert.ok(fanout.result.crossProjectDuplicates.some(x=>x.projects.length===2),"same repo+SHA across projects should be identified");

  const failure=execute([
    deployment(1,{state:"ERROR"}),deployment(2,{state:"CANCELED"})
  ]);
  assert.equal(failure.result.count,2,"failed and cancelled deployments remain visible in the usage estimate");

  // The real November incident: visible records >100, yet Git-created
  // production deployments succeeded. A list count must not assert an exact
  // technical availability or earliest possible retry minute.
  const platformMismatch=execute(Array.from({length:103},(_,i)=>
    deployment(i,{project:i<2?"routelab":"pitchnight",
      state:i<2?"READY":"CANCELED",
      branch:i<2?"main":"feat/example",
      target:i<2?"production":null})));
  assert.equal(platformMismatch.exit,2,"the unattended guard remains conservative");
  assert.equal(platformMismatch.result.status,"FREEZE");
  assert.equal(platformMismatch.result.count,103);
  assert.equal(platformMismatch.result.technicalAvailability,"UNVERIFIED",
    "a visible record count cannot prove technical impossibility");
  assert.equal(platformMismatch.result.earliestGuaranteedMinute,null,
    "no retry minute can be guaranteed from deployment history");
  assert.equal(platformMismatch.result.nextRecordExpiryAt,
    new Date(timestamp-102000+86400000).toISOString(),
    "next record expiration is a historical change, not a guaranteed free slot");
  assert.ok(platformMismatch.result.recommendations.join(" ").includes("explicitly authorized"),
    "permit human-reviewed, single production attempts without claiming a guaranteed slot");

  // Even a low visible count does not prove an API release will succeed.
  const lowVisibility=execute([deployment(1,{state:"READY",target:"production",branch:"main"})]);
  assert.equal(lowVisibility.result.technicalAvailability,"UNVERIFIED");
  assert.equal(lowVisibility.result.earliestGuaranteedMinute,null);

  const noGate=execute(Array.from({length:85},(_,i)=>deployment(i)),{gate:false});
  assert.equal(noGate.exit,0,"report mode should never block");
  assert.equal(noGate.result.status,"FREEZE");

  process.stdout.write("PASS: "+checks+" CLI end-to-end deployment scenarios\n");
} finally {
  rmSync(folder,{recursive:true,force:true});
}
