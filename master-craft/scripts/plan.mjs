import fs from "node:fs";
import { checkExecution, executionPlan } from "./execution.mjs";
import { pathToFileURL } from "node:url";

const modes = ["answer", "inspect", "create", "repair", "release"];
const hosts = ["none", "unknown", "vercel", "other"];
const flags = ["substantial", "productDesign", "measureProduct", "validateModel", "hostedBuild", "releaseAuthorized", "freshnessRequired", "releaseToolAvailable"];

export function plan(intent, snapshot) {
  if (!modes.includes(intent.mode) || !hosts.includes(intent.host) ||
      flags.some((key) => typeof intent[key] !== "boolean")) {
    throw new Error("Supply a valid mode, host and explicit boolean intent flags");
  }
  const inventory = new Map(snapshot.skills.map((skill) => [skill.path, skill]));
  const readOnly = intent.mode === "inspect" || intent.mode === "answer";
  const release = !readOnly && intent.releaseAuthorized;
  const hosting = !readOnly && (release || intent.hostedBuild);
  const blockers = [];
  const stages = ["baseline"];
  const skills = [];
  const verified = /^[0-9a-f]{40}$/i.test(snapshot.revision ?? "") &&
    ((snapshot.verified_latest === true && ["git-origin-main", "github-main"].includes(snapshot.source)) ||
      (snapshot.source === "pinned-git-commit" && intent.pinnedRevision === snapshot.revision));

  function select(file, required = false, explicit = false) {
    const skill = inventory.get(file);
    if (!skill || skill.error || !skill.description) {
      if (required) blockers.push("required-skill-unavailable:" + file);
      else throw new Error("Candidate is missing or invalid at the selected revision: " + file);
      return;
    }
    if (file === "master-craft/SKILL.md" || (skill.requires_explicit_invocation && !explicit)) {
      throw new Error("Candidate is recursive or requires explicit invocation: " + file);
    }
    if (!skills.includes(file)) skills.push(file);
  }

  if (intent.substantial) select("personal-craft/SKILL.md", true);
  if (intent.productDesign && !readOnly) select("product-design-os/SKILL.md", true);
  if (intent.securityReview === true) select("security-audit/SKILL.md", true);
  if (intent.measureProduct) select("product-evidence/SKILL.md", true);
  if (intent.validateModel) select("model-assurance/SKILL.md", true);
  for (const file of intent.specialists ?? []) {
    select(file, false, (intent.explicitSkills ?? []).includes(file));
  }
  if (hosting && intent.host === "vercel") select("vercel-deployment-steward/SKILL.md", true);

  if (intent.mode === "repair") stages.push("reproduce");
  if (intent.measureProduct || intent.validateModel) stages.push("define-evidence");
  if (intent.mode === "repair" || (intent.mode === "create" && !(intent.hostedBuild && intent.existingArtifact === true))) stages.push("implement");
  if (intent.mode === "inspect") stages.push("inspect");
  stages.push("verify");
  if (readOnly && (intent.releaseAuthorized || intent.hostedBuild)) blockers.push("read-only-host-action-conflict");
  if (intent.mode === "release" && !release) blockers.push("release-authorization-missing");
  if (hosting && ["unknown", "none"].includes(intent.host)) blockers.push("host-unresolved");
  if (hosting && !intent.releaseToolAvailable) blockers.push("host-tool-unavailable");
  if ((hosting || intent.freshnessRequired) && !verified) blockers.push("freshness-unverified");
  if (hosting && blockers.length === 0) {
    stages.push("host-preflight");
    if (intent.hostedBuild) stages.push("hosted-build");
    if (release) stages.push("publish", "verify-production");
  }
  stages.push("report");

  return { revision: snapshot.revision, skills, stages, blockers };
}

if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) {
  try {
    const { intent, snapshot, execution } = JSON.parse(fs.readFileSync(0, "utf8"));
    const route = plan(intent, snapshot);
    if (execution != null) {
      route.execution = checkExecution(route, intent, snapshot, execution);
    } else if (intent.substantial || intent.freshnessRequired || intent.releaseAuthorized || intent.hostedBuild ||
               route.skills.includes("security-audit/SKILL.md")) {
      route.execution = { ...executionPlan(route, intent), state: "unrecorded" };
    }
    console.log(JSON.stringify(route, null, 2));
    if (execution?.results != null && route.execution.state !== "complete") process.exitCode = 2;
  } catch (error) {
    console.error(error.message);
    process.exitCode = 1;
  }
}
