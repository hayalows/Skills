import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";
import { fileURLToPath } from "node:url";
import { plan } from "../scripts/plan.mjs";
import { checkExecution } from "../scripts/execution.mjs";

const file = (relative) => fileURLToPath(new URL(relative, import.meta.url));
const inventory = JSON.parse(execFileSync(process.execPath, [file("../scripts/inventory.mjs"), "--local", "--json"], { encoding: "utf8" }));
const current = { ...inventory, source: "git-origin-main", verified_latest: true };

const base = {
  host: "none",
  substantial: false,
  productDesign: false,
  measureProduct: false,
  validateModel: false,
  hostedBuild: false,
  releaseAuthorized: false,
  freshnessRequired: true,
  releaseToolAvailable: false,
};

// 1. Verify all discovered skills parse cleanly and routing metadata is attached where declared.
assert.ok(inventory.skills.length >= 66);
const architect = inventory.skills.find((s) => s.path === "agent-team-architect/SKILL.md");
const aiOps = inventory.skills.find((s) => s.path === "ai-ops-team/SKILL.md");
assert.equal(architect?.routing?.minimum_complexity, "substantial");
assert.equal(architect?.routing?.explicit_override, true);
assert.deepEqual(architect?.routing?.roles, ["lead", "specialist"]);
assert.equal(architect?.routing?.category, "orchestration");
assert.equal(aiOps?.routing?.minimum_complexity, "substantial");

// 2. Trivial-task guard blocks heavy orchestration skills when substantial=false and not explicit.
const trivial = plan({ ...base, mode: "answer", specialists: ["agent-team-architect/SKILL.md"] }, current);
assert.ok(trivial.blockers.includes("trivial-task-skill-rejected:agent-team-architect/SKILL.md"));
assert.ok(!trivial.skills.includes("agent-team-architect/SKILL.md"));

// 3. Explicit override allows it when the user explicitly requests an agent team.
const overridden = plan({
  ...base,
  mode: "answer",
  specialists: ["agent-team-architect/SKILL.md"],
  explicitSkills: ["agent-team-architect/SKILL.md"],
}, current);
assert.deepEqual(overridden.blockers, []);
assert.ok(overridden.skills.includes("agent-team-architect/SKILL.md"));

// 4. Substantial task allows both agent-team-architect and ai-ops-team without blockers.
const substantial = plan({
  ...base,
  mode: "create",
  substantial: true,
  specialists: ["agent-team-architect/SKILL.md", "ai-ops-team/SKILL.md"],
}, current);
assert.deepEqual(substantial.blockers, []);
assert.ok(substantial.skills.includes("agent-team-architect/SKILL.md"));
assert.ok(substantial.skills.includes("ai-ops-team/SKILL.md"));

// 5. Role-aware conflict detection using synthetic skills in memory.
const syntheticSnapshot = {
  ...current,
  skills: [
    ...current.skills,
    {
      path: "synthetic-lead-a/SKILL.md",
      name: "synthetic-lead-a",
      description: "Primary UI lead A.",
      routing: { exclusive_role: "ui-lead", roles: ["lead"] },
    },
    {
      path: "synthetic-lead-b/SKILL.md",
      name: "synthetic-lead-b",
      description: "Design helper or lead B.",
      routing: { exclusive_role: "ui-lead", roles: ["lead", "supporting"] },
    },
    {
      path: "synthetic-conflict-c/SKILL.md",
      name: "synthetic-conflict-c",
      description: "Incompatible with lead A.",
      routing: { conflicts_with: ["synthetic-lead-a"] },
    },
  ],
};

const exclusiveConflict = plan({
  ...base,
  mode: "create",
  specialists: ["synthetic-lead-a/SKILL.md", "synthetic-lead-b/SKILL.md"],
}, syntheticSnapshot);
assert.ok(exclusiveConflict.blockers.includes("exclusive-role-conflict:ui-lead"));

const complementary = plan({
  ...base,
  mode: "create",
  specialists: ["synthetic-lead-a/SKILL.md", "synthetic-lead-b/SKILL.md"],
  specialistRoles: { "synthetic-lead-b/SKILL.md": "supporting" },
}, syntheticSnapshot);
assert.deepEqual(complementary.blockers, []);

const explicitConflict = plan({
  ...base,
  mode: "create",
  specialists: ["synthetic-lead-a/SKILL.md", "synthetic-conflict-c/SKILL.md"],
}, syntheticSnapshot);
assert.ok(explicitConflict.blockers.includes("skill-conflict:synthetic-conflict-c/SKILL.md:synthetic-lead-a/SKILL.md"));

// 6. Execution record enforces selection rationale (contract.why).
const route = plan({ ...base, mode: "create", specialists: ["lunour-naming/SKILL.md"] }, current);
const namingSkill = current.skills.find((s) => s.path === "lunour-naming/SKILL.md");
const missingWhy = checkExecution(route, { ...base, mode: "create" }, current, {
  objective: "Name brand",
  scope: "Naming only",
  target: "brand",
  targetRevision: "HEAD",
  allowedEffects: ["inspect", "write-target"],
  primary: "lunour-naming/SKILL.md",
  contracts: {
    "lunour-naming/SKILL.md": {
      why: "   ",
      procedure: "Generate 5 names",
      restrictions: "No trademark claims",
      references: ["lunour-naming/SKILL.md"],
      loadEvidence: "Loaded from inventory",
      revision: route.revision,
      blob: namingSkill?.sha,
      stages: ["implement"],
    },
  },
  toolPlan: {
    baseline: { status: "ready", capability: "fs", basis: "local" },
    implement: { status: "ready", capability: "fs", basis: "local" },
    verify: { status: "ready", capability: "fs", basis: "local" },
    report: { status: "ready", capability: "fs", basis: "local" },
  },
});
assert.ok(missingWhy.issues.includes("skill-contract-invalid:lunour-naming/SKILL.md"));

console.log("PASS: V2 routing metadata, trivial-task guard + override, role-aware conflict detection, synthetic skills, and rationale checks");
