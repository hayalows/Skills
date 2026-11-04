import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");
const skillRoot = path.join(root, "master-craft");
const read = (file) => fs.readFileSync(path.join(root, file), "utf8");
const map = read("master-craft/references/skill-map.md");
const skill = read("master-craft/SKILL.md");
const scenarios = JSON.parse(read("master-craft/tests/routing-scenarios.json"));

function discover() {
  const paths = [];
  for (const item of fs.readdirSync(root, { withFileTypes: true })) {
    if (!item.isDirectory() || item.name === "master-craft" || item.name.startsWith(".")) continue;
    if (fs.existsSync(path.join(root, item.name, "SKILL.md"))) paths.push(item.name + "/SKILL.md");
  }
  const mattRoot = path.join(root, "collections/matt-pocock-skills/skills");
  for (const group of fs.readdirSync(mattRoot, { withFileTypes: true })) {
    if (!group.isDirectory()) continue;
    for (const item of fs.readdirSync(path.join(mattRoot, group.name), { withFileTypes: true })) {
      if (!item.isDirectory()) continue;
      const skillPath = "collections/matt-pocock-skills/skills/" + group.name + "/" + item.name + "/SKILL.md";
      if (fs.existsSync(path.join(root, skillPath))) paths.push(skillPath);
    }
  }
  return paths.sort();
}

const linked = [...map.matchAll(/\]\(\.\.\/([a-z0-9/_-]+\/SKILL\.md)\)/g)].map((m) => m[1]).sort();
assert.equal(new Set(linked).size, linked.length, "Skill map must not contain duplicate entries");
const installedPaths = discover();
const staleHints = linked.filter((p) => !installedPaths.includes(p));
const unmapped = installedPaths.filter((p) => !linked.includes(p));
if (staleHints.length) console.warn("WARN: curated map contains old paths:", staleHints.join(", "));
if (unmapped.length) console.log("INFO: additional skills found dynamically, no manual registration required:", unmapped.join(", "));
assert.match(skill, /^---\r?\nname: master-craft\r?\n/m, "Valid Agent Skills name required");
assert.match(skill, /^description: .{30,1024}$/m, "Use a descriptive skill trigger");
assert.ok(skill.split("\n").length < 500, "Keep root skill concise; use references");
for (const heading of ["Choose the route", "Execute the sequence", "Apply quality gates", "Finish with evidence"]) {
  assert.ok(skill.includes(heading), "Master skill section missing: " + heading);
}
assert.ok(map.includes("personal-craft/SKILL.md"), "Missing execution standard");
assert.ok(map.includes("product-design-os/SKILL.md"), "Missing product design standard");
assert.ok(map.includes("security-audit/SKILL.md"), "Missing security branch");
assert.ok(map.includes("vercel-deployment-steward/SKILL.md"), "Missing Vercel release gate");
assert.ok(map.includes("collections/matt-pocock-skills/skills/engineering/diagnosing-bugs/SKILL.md"), "Missing engineering bug flow");
assert.ok(scenarios.length >= 12, "Provide at least 12 routing examples");
const indexedNames = new Set(installedPaths.map((p) => p.split("/").at(-2)));
for (const scenario of scenarios) {
  assert.ok(scenario.request?.length > 12, "Scenario missing request");
  assert.ok(scenario.expected?.length, "Scenario missing expected skills");
  assert.ok(scenario.rationale?.length > 15, "Scenario missing rationale");
  for (const name of [...scenario.expected, ...(scenario.excluded || [])]) {
    assert.ok(indexedNames.has(name), "Scenario refers to missing skill " + name);
  }
  assert.equal(scenario.expected.filter((s) => (scenario.excluded || []).includes(s)).length, 0,
    "Scenario cannot require and exclude the same skill");
}
assert.ok(fs.existsSync(path.join(skillRoot, "scripts/inventory.mjs")), "Missing discovery tool");
assert.ok(fs.existsSync(path.join(skillRoot, "references/freshness.md")), "Missing freshness reference");
assert.match(skill, /Live skill freshness/, "Master Craft must require live freshness before routing");
console.log("PASS: " + installedPaths.length + " discovered skills; " + linked.length + " curated map hints; valid Master Craft metadata and " + scenarios.length + " routing cases");
