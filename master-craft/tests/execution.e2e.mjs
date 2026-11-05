import assert from "node:assert/strict";
import fs from "node:fs";
import { execFileSync, spawnSync } from "node:child_process";
import { fileURLToPath } from "node:url";

const file = (relative) => fileURLToPath(new URL(relative, import.meta.url));
const snapshot = JSON.parse(execFileSync(process.execPath, [file("../scripts/inventory.mjs"), "--local", "--json"]));
const flags = ["substantial", "productDesign", "measureProduct", "validateModel", "hostedBuild", "releaseAuthorized", "freshnessRequired", "releaseToolAvailable"];
const defaults = Object.fromEntries(flags.map((flag) => [flag, false]));
const current = { ...snapshot, source: "git-origin-main", verified_latest: true };
const security = "security-audit/SKILL.md";
function run(intent, execution, source = current, expected = 0) {
  const result = spawnSync(process.execPath, [file("../scripts/plan.mjs")], {
    input: JSON.stringify({ intent, snapshot: source, execution }), encoding: "utf8"
  });
  assert.equal(result.status, expected, result.stderr || result.stdout);
  return JSON.parse(result.stdout);
}

function record(route, intent, mode = "focused") {
  const allowedEffects = ["inspect"];
  if (route.stages.includes("implement")) allowedEffects.push("write-target");
  if (route.stages.includes("hosted-build")) allowedEffects.push("preview");
  if (route.stages.includes("publish")) allowedEffects.push("publish");
  if (mode === "full") allowedEffects.push("write-artifact");
  const primary = route.skills.find((path) => path !== "personal-craft/SKILL.md") ?? route.skills[0] ?? null;
  return {
    objective: "Synthetic fixture", target: "disposable test scope", targetRevision: "fixture v1", scope: intent.mode,
    allowedEffects, primary, auditMode: mode,
    contracts: Object.fromEntries(route.skills.map((path) => [path, {
      why: "fixture rationale", procedure: "fixture procedure", restrictions: "fixture limits",
      revision: route.revision, references: [], loadEvidence: "synthetic load receipt", stages: ["verify"],
    }])),
  };
}

function prepare(intent, execution, source) {
  const draft = run(intent, execution, source).execution;
  execution.toolPlan = Object.fromEntries(draft.stages.map(({ id }) =>
    [id, { status: "ready", capability: "fixture reader", basis: "synthetic access" }]));
  return run(intent, execution, source).execution;
}

function finish(execution, graph) {
  execution.checker = { status: "ran", evidence: "fixture planner invocation above" };
  execution.tools = { fixture: "synthetic result, not a live target operation" };
  execution.results = Object.fromEntries(graph.stages.map(({ id, effect }) =>
    [id, { status: "passed", effects: [effect], tools: ["fixture"], evidence: "fixture output", proves: "fixture assertion" }]));
  if (graph.auditMode) execution.coverage = [{ boundary: "public to admin", scope: "fixture endpoint", evidence: "fixture lines", status: "checked" }];
}

const cases = fs.readFileSync(file("./plan-cases.tsv"), "utf8").trim().split("\n").slice(1);
for (const line of cases) {
  const [request, mode, host, rawFlags, proposed] = line.split("|").map((field) => field.trim());
  const active = rawFlags.split(",");
  const specialists = proposed === "-" ? [] : proposed.split(",").map((name) => snapshot.skills.find((s) => s.name === name).path);
  const intent = { mode, host, specialists, ...Object.fromEntries(flags.map((flag) => [flag, active.includes(flag)])) };
  intent.releaseToolAvailable = !active.includes("no-tool");
  if (active.includes("explicit")) intent.explicitSkills = specialists;
  const source = active.includes("offline") ? snapshot : current;
  const route = run(intent, undefined, source);
  const execution = record(route, intent);
  const graph = prepare(intent, execution, source);
  assert.deepEqual(graph.issues, route.blockers, request);
  finish(execution, graph);
  const result = run(intent, execution, source, route.blockers.length ? 2 : 0);
  assert.equal(result.execution.state, route.blockers.length ? "incomplete" : "complete", request);
}

const intent = { ...defaults, mode: "inspect", host: "none", substantial: true, specialists: [security] };
const route = run(intent);
assert.ok(run({ ...intent, specialists: [], securityReview: true }).skills.includes(security));
assert.ok(run({ ...intent, releaseAuthorized: true }).blockers.includes("read-only-host-action-conflict"));
assert.equal(route.execution.state, "unrecorded");
assert.ok(route.execution.blockers.includes("audit-mode-unresolved"));
const focused = record(route, intent);
const graph = prepare(intent, focused);
assert.deepEqual(graph.issues, []);
assert.ok(!graph.stages.some(({ id }) => id === "security-hunting"));
finish(focused, graph);
function rejected(change, expected) {
  const input = structuredClone(focused);
  change(input);
  assert.ok(run(intent, input, current, 2).execution.issues.includes(expected), expected);
}
rejected((x) => delete x.checker, "checker-execution-unverified");
rejected((x) => x.checker = { status: "fallback", reason: "Node unavailable", evidence: "manual check" }, "checker-execution-unverified");
rejected((x) => delete x.coverage, "security-coverage-invalid");
rejected((x) => x.coverage[0].status = "blocked", "security-coverage-blocked");
rejected((x) => x.results["security-source-review"] = { status: "failed", reason: "repository unavailable" }, "stage-dependency-incomplete:security-verification-disposition");
rejected((x) => delete x.tools.fixture, "stage-evidence-invalid:verify");
rejected((x) => x.toolPlan.verify.status = "blocked", "stage-tool-not-ready:verify");
rejected((x) => x.allowedEffects.push("run-target"), "security-sandbox-unverified");
rejected((x) => x.results.inspect.effects.push("run-target"), "unauthorized-stage-effect:inspect");
rejected((x) => x.allowedEffects.push("write-target"), "read-only-target-write-forbidden");
rejected((x) => x.contracts[security].revision = "previous", "skill-contract-invalid:" + security);
const pinned = { ...current, skills: current.skills.map((skill) => skill.path === security ? { ...skill, sha: "current-blob" } : skill) };
assert.ok(run(intent, focused, pinned, 2).execution.issues.includes("skill-contract-invalid:" + security));

const full = record(route, intent, "full");
const fullGraph = prepare(intent, full);
finish(full, fullGraph);
assert.equal(fullGraph.stages.filter(({ id }) => /^security-/.test(id)).length, 8);
assert.ok(run(intent, full, current, 2).execution.issues.includes("security-validators-unverified"));
full.auditValidators = { findings: "fixture findings validator output", coverage: "fixture coverage validator output" };
assert.ok(run(intent, full, current, 2).execution.issues.includes("security-independence-unverified"));
full.auditIndependence = { candidates: 0, evidence: "fixture no candidate result" };
full.auditArtifacts = Object.fromEntries(["run-metadata.json", "architecture.md", "coverage-ledger.json", "findings.json",
  "REPORT.md", "FINDINGS-DETAIL.md", "NEEDS-VALIDATION.md"].map((name) => [name, "fixture artifact"]));
assert.equal(run(intent, full).execution.state, "complete");
const fullRuntime = record(route, intent, "full");
fullRuntime.auditChecks = { "security-candidate-validation": [{ id: "sandboxed-reproduction", effect: "run-target" }] };
fullRuntime.allowedEffects.push("run-target");
fullRuntime.sandboxEvidence = "synthetic OS-isolation receipt";
const runtimeGraph = prepare(intent, fullRuntime);
assert.deepEqual(runtimeGraph.issues, []);
assert.deepEqual(runtimeGraph.stages.find(({ id }) => id === "security-structured-output").dependsOn, ["sandboxed-reproduction"]);
full.allowedEffects = ["inspect"];
assert.ok(run(intent, full, current, 2).execution.issues.includes("audit-artifacts-not-authorized"));
const release = { ...defaults, mode: "release", host: "vercel", releaseAuthorized: true, releaseToolAvailable: true };
assert.ok(run(release, undefined, { ...current, source: "pinned-git-commit", revision: "fake" }).blockers.includes("freshness-unverified"));

assert.ok(!run({ ...release, mode: "create", releaseAuthorized: false, hostedBuild: true, existingArtifact: true }).stages.includes("implement"));
const releaseRecord = record(run(release), release);
const releaseGraph = prepare(release, releaseRecord);
finish(releaseRecord, releaseGraph);
releaseRecord.results.baseline.effects = ["publish"];
assert.ok(run(release, releaseRecord, current, 2).execution.issues.includes("unauthorized-stage-effect:baseline"));

const modelIntent = { ...defaults, mode: "create", host: "none", validateModel: true };
const modelRoute = run(modelIntent);
const method = record(modelRoute, modelIntent);
method.methodOnly = ["model-assurance/SKILL.md"];
method.allowedEffects = ["inspect", "write-artifact"];
const methodGraph = prepare(modelIntent, method);
assert.ok(methodGraph.stages.some(({ id }) => id === "model-assurance-method-review"));
assert.ok(!methodGraph.stages.some(({ id }) => id === "model-independent-recalculation"));
finish(method, methodGraph);
assert.equal(run(modelIntent, method).execution.state, "complete");

const future = { path: "nested/future/SKILL.md", description: "New specialist", sha: "future-blob" };
const expanded = { ...current, skills: [...current.skills, future] };
const extensionIntent = { ...defaults, mode: "inspect", host: "none", specialists: [future.path] };
const extension = record(run(extensionIntent, undefined, expanded), extensionIntent);
extension.contracts[future.path].blob = future.sha;
extension.beforeVerify = [{ id: "future-procedure", owner: future.path, effect: "inspect" }];
const extensionGraph = prepare(extensionIntent, extension, expanded);
finish(extension, extensionGraph);
assert.equal(run(extensionIntent, extension, expanded).execution.state, "complete");
delete extension.results["future-procedure"];
assert.ok(run(extensionIntent, extension, expanded, 2).execution.issues.includes("stage-incomplete:future-procedure"));
console.log("PASS: " + cases.length + " scenario executions through planner CLI with synthetic evidence, plus security, scope, freshness and future-skill regressions");
