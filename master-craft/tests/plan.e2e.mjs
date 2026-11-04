import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";
import fs from "node:fs";
import { fileURLToPath } from "node:url";

const file = (relative) => fileURLToPath(new URL(relative, import.meta.url));
const inventory = JSON.parse(execFileSync(process.execPath, [file("../scripts/inventory.mjs"), "--local", "--json"]));
const current = { ...inventory, source: "git-origin-main", verified_latest: true };
const cases = fs.readFileSync(file("./plan-cases.tsv"), "utf8").trim().split("\n")
  .filter((line) => !line.startsWith("#"));
const flags = ["substantial", "productDesign", "measureProduct", "validateModel", "hostedBuild", "releaseAuthorized", "freshnessRequired"];
const run = (intent, snapshot = current) => JSON.parse(execFileSync(process.execPath, [file("../scripts/plan.mjs")], {
  input: JSON.stringify({ intent, snapshot }), encoding: "utf8"
}));

assert.ok(cases.length >= 50);
assert.equal(new Set(cases.map((line) => line.split("|")[0])).size, cases.length);
for (const line of cases) {
  const [request, mode, host, rawFlags, proposed, expected] = line.split("|").map((value) => value.trim());
  const active = rawFlags.split(",");
  assert.ok(active.every((flag) => [...flags, "-", "offline", "explicit", "no-tool"].includes(flag)), request);
  const specialists = proposed === "-" ? [] : proposed.split(",").map((name) => {
    const matches = inventory.skills.filter((skill) => skill.name === name);
    assert.equal(matches.length, 1, request);
    return matches[0].path;
  });
  const intent = { mode, host, specialists, ...Object.fromEntries(flags.map((flag) => [flag, active.includes(flag)])) };
  intent.releaseToolAvailable = !active.includes("no-tool");
  if (active.includes("explicit")) intent.explicitSkills = specialists;
  const result = run(intent, active.includes("offline") ? inventory : current);
  const names = result.skills.map((skillPath) => inventory.skills.find((skill) => skill.path === skillPath).name);
  const negative = {
    "no-skills": names.length === 0,
    "no-model": !names.includes("model-assurance"),
    "no-evidence": !names.includes("product-evidence"),
    "no-vercel": !names.includes("vercel-deployment-steward"),
    "no-publish": !result.stages.includes("publish"),
    "no-implement": !result.stages.includes("implement"),
    "no-preflight": !result.stages.includes("host-preflight"),
  };
  for (const check of expected.split(",")) {
    const ok = check.startsWith("skill:") ? names.includes(check.slice(6))
      : check.startsWith("blocker:") ? result.blockers.includes(check.slice(8))
      : check in negative ? negative[check] : result.stages.includes(check);
    assert.ok(ok, request + " — " + check);
  }
  const order = ["baseline", "reproduce", "define-evidence", "implement", "inspect", "verify", "host-preflight", "hosted-build", "publish", "verify-production", "report"];
  assert.deepEqual(result.stages, order.filter((stage) => result.stages.includes(stage)), request);
  if (result.blockers.length) assert.ok(!result.stages.includes("publish"), request);
}

const release = { releaseToolAvailable: true, mode: "release", host: "vercel", ...Object.fromEntries(flags.map((flag) => [flag, flag === "releaseAuthorized"])) };
const missing = { ...current, skills: current.skills.filter((skill) => skill.name !== "vercel-deployment-steward") };
assert.ok(run(release, missing).blockers.includes("required-skill-unavailable:vercel-deployment-steward/SKILL.md"));
assert.ok(!run(release, missing).stages.includes("publish"));

const future = { path: "extensions/accessibility-lab/SKILL.md", name: "accessibility-lab", description: "Validate keyboard focus in complex maps." };
const expanded = { ...current, skills: [...current.skills, future] };
assert.ok(run({ ...release, specialists: [future.path] }, expanded).skills.includes(future.path));

console.log("PASS: " + cases.length + " structured scenario plans and release/extension edge cases");
