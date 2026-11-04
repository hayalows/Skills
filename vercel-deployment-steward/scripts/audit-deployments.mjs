#!/usr/bin/env node
/**
 * Vercel Deployment Steward: read-only whole-team audit and release preflight.
 * Node 20+, no third-party packages. No deployment, mutation, token output, or writes.
 *
 * node scripts/audit-deployments.mjs --team team_xxx --json
 * node scripts/audit-deployments.mjs --team team_xxx --gate
 * node scripts/audit-deployments.mjs --snapshot fixture.json --now 2026-11-04T22:30:00Z --gate
 *
 * Gate exits: 0 = passes unattended planning policy (or report-only);
 * 2 = discretionary/unattended releases on hold; 3 = incomplete or unknown.
 * Exit 2 is NOT proof Vercel will reject a user-authorized release.
 */
import { readFile } from "node:fs/promises";

const argumentsList=process.argv.slice(2);
function option(key,fallback=null){
  const i=argumentsList.indexOf("--"+key);
  return i<0?fallback:argumentsList[i+1]??"";
}
const flag=(key)=>argumentsList.includes("--"+key);
const team=option("team",process.env.VERCEL_TEAM_ID);
const snapshot=option("snapshot");
const json=flag("json");
const gate=flag("gate");
const limitNumber=Number(option("cap","100"));
const now=option("now")?Date.parse(option("now")):Date.now();
const HOUR=3_600_000;
const cutoff=now-24*HOUR;
const MAX_PAGES=60;

function fail(message){
  const output={status:"UNKNOWN",complete:false,error:message,gateAllowed:false};
  if(json)process.stdout.write(JSON.stringify(output,null,2)+"\n");
  else process.stderr.write("Deployment Steward: "+message+"\n");
  process.exitCode=3;
}
function summarize(records,{complete,source,pageCount}){
  const filtered=[];
  let invalid=0;
  const seen=new Set();
  for(const item of records) {
    const at=Number(item.created??item.createdAt);
    if(!Number.isFinite(at)||at<=0){invalid++;continue;}
    if(at<cutoff||at>now+60_000)continue;
    const id=String(item.id??item.uid??item.url??"")
      || [item.name,item.meta?.githubCommitSha,at,item.target].join(":");
    if(seen.has(id))continue;
    seen.add(id);filtered.push(item);
  }
  const count=filtered.length;
  // A history count is not Vercel's authoritative internal quota counter.
  const estimatedRemaining=Math.max(0,limitNumber-count);
  const oldestVisible=filtered.length
    ? Math.min(...filtered.map(d=>Number(d.created??d.createdAt))) : null;
  const nextRecordExpiryAt=oldestVisible===null ? null
    : new Date(oldestVisible+24*HOUR).toISOString();
  const usageRatio=count/limitNumber;
  const known=Boolean(complete)&&invalid===0;
  const status=!known?"UNKNOWN":usageRatio>=.85?"FREEZE":
    usageRatio>=.70?"PROTECT":usageRatio>=.55?"WATCH":"GREEN";
  const perProject=new Map(),states={},targets={},repoProject=new Map(),repoSha=new Map();
  for(const d of filtered){
    const project=String(d.name??d.projectId??"unknown");
    const row=perProject.get(project)??{project,count:0,production:0,nonProductionOrUnknown:0,errors:0,canceled:0,branches:{}};
    row.count++;
    if(d.target==="production")row.production++;
    else row.nonProductionOrUnknown++;
    if(d.state==="ERROR")row.errors++;
    if(d.state==="CANCELED")row.canceled++;
    const branch=String(d.meta?.githubCommitRef??"unlabelled");
    row.branches[branch]=(row.branches[branch]??0)+1;
    perProject.set(project,row);
    const state=String(d.state??"unlabelled");
    states[state]=(states[state]??0)+1;
    const target=String(d.target??"unlabelled (often preview)");
    targets[target]=(targets[target]??0)+1;

    const repo=d.meta?.githubRepo;
    const org=d.meta?.githubOrg;
    const sha=d.meta?.githubCommitSha;
    if(repo&&org){
      const slug=String(org)+"/"+String(repo);
      const projects=repoProject.get(slug)??new Set();
      projects.add(project);repoProject.set(slug,projects);
      if(sha){
        const key=slug+"@"+sha;
        const duplicate=repoSha.get(key)??new Set();
        duplicate.add(project);
        repoSha.set(key,duplicate);
      }
    }
  }
  const crossProjectDuplicates=[...repoSha.entries()]
    .filter(([_,projects])=>projects.size>=2)
    .map(([key,projects])=>({commit:key,projects:[...projects].sort()}))
    .sort((a,b)=>a.commit.localeCompare(b.commit));
  const sharedRepositories=[...repoProject.entries()]
    .filter(([_,projects])=>projects.size>=2)
    .map(([repository,projects])=>({repository,projects:[...projects].sort()}));
  const projects=[...perProject.values()].sort((a,b)=>b.count-a.count||a.project.localeCompare(b.project));

  const recommendations=[];
  if(!known)recommendations.push("The deployment record is incomplete or contains invalid timestamps. Do not treat the headroom estimate as authoritative.");
  if(status==="FREEZE")recommendations.push("Pause discretionary and unattended releases. A single explicitly authorized production attempt may be considered with recent route-specific evidence; a FREEZE history count is NOT proof of technical unavailability. Never repeatedly retry a 402 from the same method.");
  else if(status==="PROTECT")recommendations.push("Protect the remaining capacity. Group approved changes and plan one release only when needed.");
  else if(status==="WATCH")recommendations.push("Reduce deployment frequency and review branch preview settings before more pushes.");
  if(sharedRepositories.length)recommendations.push("Review multiple Vercel projects connected to the same repository; a single commit can deploy several sites.");
  if(projects.some(p=>p.nonProductionOrUnknown>=5))recommendations.push("Review automatic feature-branch deployments; target=null means unlabeled, not proven preview.");
  if((states.ERROR??0)+(states.CANCELED??0)>=5)recommendations.push("Investigate repeated failures and cancellations locally before publishing another attempt.");
  if(!recommendations.length)recommendations.push("Headroom looks healthy. Still verify the project, branch, latest SHA, and whether Git already auto-deployed.");

  return {
    status,complete:known,source,generatedAt:new Date(now).toISOString(),
    windowStart:new Date(cutoff).toISOString(),cap:limitNumber,capNote:"Configured Hobby planning cap, not Vercel's authoritative remaining quota.",
    count,estimatedRemaining,invalid,pageCount,states,targets,projects,
    sharedRepositories,crossProjectDuplicates,recommendations,
    countMeaning:"Visible deployment records; not Vercel's official quota counter.",
    technicalAvailability:"UNVERIFIED",
    earliestGuaranteedMinute:null,
    nextRecordExpiryAt,
    releaseGateMeaning:"Policy for unattended/discretionary releases, not proof of platform acceptance.",
    gateAllowed:known&&status!=="FREEZE"
  };
}
async function fetchDeployments(){
  if(!team)throw Error("Set --team team_xxx or VERCEL_TEAM_ID for a team-wide audit.");
  const token=process.env.VERCEL_ACCESS_TOKEN??process.env.VERCEL_TOKEN;
  if(!token)throw Error("Missing VERCEL_ACCESS_TOKEN or VERCEL_TOKEN environment variable.");
  let until=null,pages=0,complete=false;
  const collected=[];
  const cursors=new Set();
  while(pages<MAX_PAGES){
    const url=new URL("https://api.vercel.com/v6/deployments");
    url.searchParams.set("teamId",team);
    url.searchParams.set("limit","100");
    if(until!==null)url.searchParams.set("until",String(until));
    const response=await fetch(url,{headers:{Authorization:"Bearer "+token,Accept:"application/json"},signal:AbortSignal.timeout(20000)});
    if(!response.ok){
      // Avoid printing returned content, which may contain sensitive metadata.
      throw Error("Vercel deployments read failed with HTTP "+response.status+". No deployment was attempted.");
    }
    const body=await response.json();
    if(!Array.isArray(body.deployments))throw Error("Vercel returned an unexpected deployments payload.");
    pages++;
    collected.push(...body.deployments);
    const oldest=Math.min(...body.deployments.map(x=>Number(x.created??x.createdAt)));
    if(body.deployments.length===0 || (Number.isFinite(oldest)&&oldest<cutoff)){
      complete=true;break;
    }
    const next=body.pagination?.next;
    if(next===null||next===undefined){
      // Trust a real pagination object. If absent and exactly 100 rows,
      // fail closed rather than assuming the window was fully collected.
      complete=Boolean(body.pagination)||body.deployments.length<100;
      break;
    }
    if(!Number.isFinite(Number(next))||cursors.has(String(next))){
      throw Error("Vercel pagination cursor repeated or was invalid. Audit incomplete.");
    }
    cursors.add(String(next));
    until=Number(next);
  }
  if(pages===MAX_PAGES)complete=false;
  return {records:collected,complete,pageCount:pages};
}
function writeText(result){
  process.stdout.write(
    "Deployment Steward | "+result.status+" | "+result.generatedAt+"\n"+
    "Team-wide rolling 24h: "+result.count+"/"+result.cap+
    " (planning headroom "+result.estimatedRemaining+"; NOT a verified quota balance)"+
    (result.complete?"":" [INCOMPLETE]")+"\n"+
    "Technical availability: UNVERIFIED; earliest guaranteed retry: unknown.\n"+
    "Next visible record expiry: "+(result.nextRecordExpiryAt??"none in window")+
    " (not a guaranteed free slot).\n"+
    "Recorded states: "+JSON.stringify(result.states)+"\n"+
    "Projects:\n"+result.projects.map(p=>
      "  "+p.project+": "+p.count+" records, "+p.production+" production, "+
      p.nonProductionOrUnknown+" non-production/unlabelled, "+
      p.errors+" errors, "+p.canceled+" canceled"
    ).join("\n")+"\n"+
    "Shared repositories: "+JSON.stringify(result.sharedRepositories)+"\n"+
    "Repeated commit across projects: "+JSON.stringify(result.crossProjectDuplicates)+"\n"+
    "Next: "+result.recommendations.join(" ")+"\n"+
    "Note: an API 402 does not prove the Git-triggered path is blocked. Do not infer an exemption either.\n"
  );
}
async function main(){
  if(!Number.isInteger(limitNumber)||limitNumber<1||!Number.isFinite(now)){
    throw Error("Invalid --cap or --now value.");
  }
  if(snapshot&&(!snapshot.trim()||snapshot.startsWith("--")))throw Error("--snapshot requires a file path.");
  let source,data;
  if(snapshot){
    const parsed=JSON.parse(await readFile(snapshot,"utf8"));
    if(Array.isArray(parsed))throw Error("Snapshot requires {complete:boolean,deployments:[...]}.");
    data={
      records:parsed.deployments,
      complete:parsed.complete===true,
      pageCount:parsed.pageCount??1
    };
    if(!Array.isArray(data.records))throw Error("Snapshot is missing its deployments array.");
    source="snapshot (offline)";
  } else {
    data=await fetchDeployments();source="Vercel REST API (read-only)";
  }
  const result=summarize(data.records,{complete:data.complete,source,pageCount:data.pageCount});
  if(json)process.stdout.write(JSON.stringify(result,null,2)+"\n");
  else writeText(result);
  if(gate&&result.status==="UNKNOWN")process.exitCode=3;
  else if(gate&&result.status==="FREEZE")process.exitCode=2;
}
main().catch(error=>fail(error?.message??"Unknown audit failure."));
