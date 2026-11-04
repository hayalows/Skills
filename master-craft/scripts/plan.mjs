import fs from "node:fs";
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
  const verified = snapshot.verified_latest === true || snapshot.source === "pinned-git-commit";

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
  if (intent.measureProduct) select("product-evidence/SKILL.md", true);
  if (intent.validateModel) select("model-assurance/SKILL.md", true);
  for (const file of intent.specialists ?? []) {
    select(file, false, (intent.explicitSkills ?? []).includes(file));
  }
  if (hosting && intent.host === "vercel") select("vercel-deployment-steward/SKILL.md", true);

  if (intent.mode === "repair") stages.push("reproduce");
  if (intent.measureProduct || intent.validateModel) stages.push("define-evidence");
  if (intent.mode === "repair" || intent.mode === "create") stages.push("implement");
  if (intent.mode === "inspect") stages.push("inspect");
  stages.push("verify");
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
    const { intent, snapshot } = JSON.parse(fs.readFileSync(0, "utf8"));
    console.log(JSON.stringify(plan(intent, snapshot), null, 2));
  } catch (error) {
    console.error(error.message);
    process.exitCode = 1;
  }
}
