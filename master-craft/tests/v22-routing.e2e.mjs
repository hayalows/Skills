import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";
import { fileURLToPath } from "node:url";
import { plan } from "../scripts/plan.mjs";
import { routingError } from "../scripts/routing-policy.mjs";

const file = (relative) => fileURLToPath(new URL(relative, import.meta.url));
const inventory = JSON.parse(execFileSync(process.execPath, [file("../scripts/inventory.mjs"), "--local", "--json"], { encoding: "utf8" }));
const current = { ...inventory, source: "git-origin-main", verified_latest: true };

const selectable = inventory.skills.filter((s) => s.path !== "master-craft/SKILL.md");
assert.ok(selectable.length > 0, "Inventory must contain selectable skills");

// 1. Validate every declared policy, while keeping future metadata optional.
for (const skill of selectable) {
  assert.ok(!skill.error && skill.description, "Invalid metadata: " + skill.path);
  if (skill.routing !== undefined) assert.equal(routingError(skill.routing), null, "Invalid routing metadata: " + skill.path);
}

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

// 2. Test every discovered selectable skill individually against its declared policy.
for (const skill of selectable) {
  const needsSubstantial = skill.routing?.minimum_complexity === "substantial";
  const explicitSkills = skill.requires_explicit_invocation ? [skill.path] : [];
  const res = plan({
    ...base,
    mode: skill.routing?.allowed_modes?.[0] ?? "create",
    substantial: needsSubstantial,
    specialists: [skill.path],
    explicitSkills,
  }, current);
  assert.deepEqual(res.blockers, [], `Unexpected blocker for ${skill.path}: ${res.blockers.join(", ")}`);
  assert.ok(res.skills.includes(skill.path), `Skill missing from plan: ${skill.path}`);
}

// 3. Test realistic cross-domain combinations (no false rejections).
const combos = [
  {
    name: "Product UI + UX helper + Product Evidence",
    intent: {
      ...base,
      mode: "create",
      substantial: true,
      productDesign: true,
      measureProduct: true,
      specialists: ["ui-ux-craft/SKILL.md"],
      specialistRoles: { "ui-ux-craft/SKILL.md": "supporting" },
    },
  },
  {
    name: "Marketing page + Gemini visual helper + Brand + Naming",
    intent: {
      ...base,
      mode: "create",
      substantial: true,
      specialists: [
        "design-taste-frontend/SKILL.md",
        "gemini-frontend-design/SKILL.md",
        "lunour-brand-strategy/SKILL.md",
        "lunour-naming/SKILL.md",
      ],
      specialistRoles: {
        "design-taste-frontend/SKILL.md": "lead",
        "gemini-frontend-design/SKILL.md": "supporting",
      },
    },
  },
  {
    name: "Engineering + TDD + Code Review",
    intent: {
      ...base,
      mode: "create",
      substantial: true,
      specialists: [
        "engineering-workshop/SKILL.md",
        "collections/matt-pocock-skills/skills/engineering/tdd/SKILL.md",
        "collections/matt-pocock-skills/skills/engineering/code-review/SKILL.md",
      ],
      specialistRoles: {
        "engineering-workshop/SKILL.md": "lead",
        "collections/matt-pocock-skills/skills/engineering/tdd/SKILL.md": "supporting",
        "collections/matt-pocock-skills/skills/engineering/code-review/SKILL.md": "supporting",
      },
    },
  },
  {
    name: "Multi-agent Orchestration + AI Ops Team",
    intent: {
      ...base,
      mode: "create",
      substantial: true,
      specialists: ["agent-team-architect/SKILL.md", "ai-ops-team/SKILL.md"],
      explicitSkills: ["ai-ops-team/SKILL.md"],
    },
  },
  {
    name: "Consulting Report + Editorial PDF + Model Assurance",
    intent: {
      ...base,
      mode: "create",
      substantial: true,
      validateModel: true,
      specialists: ["consulting-grade-reports-decks/SKILL.md", "premium-editorial-report-pdf/SKILL.md"],
      specialistRoles: { "premium-editorial-report-pdf/SKILL.md": "supporting" },
    },
  },
  {
    name: "Personal Voice + Copywriting helper",
    intent: {
      ...base,
      mode: "create",
      specialists: ["papa-kojo-writing-style/SKILL.md", "human-copywriting/SKILL.md"],
      specialistRoles: {
        "papa-kojo-writing-style/SKILL.md": "lead",
        "human-copywriting/SKILL.md": "supporting",
      },
    },
  },
];

for (const combo of combos) {
  const res = plan(combo.intent, current);
  assert.deepEqual(res.blockers, [], `Combo failed (${combo.name}): ${res.blockers.join(", ")}`);
}

// 4. Verify substantial guard on newly annotated heavy skills & explicit override.
assert.throws(() => plan({ ...base, mode: "answer", specialists: ["luna-astra-behavior/SKILL.md"] }, current), /requires explicit invocation/);

const heavyOverride = plan({
  ...base,
  mode: "answer",
  specialists: ["luna-astra-behavior/SKILL.md"],
  explicitSkills: ["luna-astra-behavior/SKILL.md"],
}, current);
assert.deepEqual(heavyOverride.blockers, []);

// 5. Verify complements validation fails closed on invalid paths.
assert.equal(routingError({ roles: ["lead"], complements: ["../secret"] }), "invalid complements list");
assert.equal(routingError({ roles: ["lead"], complements: ["tdd", "tdd"] }), "invalid complements list");

console.log(`PASS: All ${selectable.length} skills individually verified, 6 cross-domain combos passed with zero false rejections, and V2.2 metadata validated`);
