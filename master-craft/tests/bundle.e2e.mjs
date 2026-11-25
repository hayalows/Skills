// End-to-end checks for the portable bundle, the skill index and cross-agent entry files.
import assert from "node:assert/strict";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { spawnSync } from "node:child_process";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");
const cli = path.join(root, "master-craft/scripts/bundle.mjs");
const run = (...args) => spawnSync(process.execPath, [cli, ...args], { cwd: root, encoding: "utf8", maxBuffer: 32 * 1024 * 1024 });
const read = (file) => fs.readFileSync(path.join(root, file), "utf8");

// Core bundle: entrypoint plus chosen references, the rest listed with URLs.
const core = run("product-design-os", "--refs", "visual-direction,build-and-verify,quality-rubric");
assert.equal(core.status, 0, core.stderr);
assert.ok(core.stdout.includes("name: product-design-os"), "bundle keeps the entrypoint frontmatter");
for (const name of ["visual-direction", "build-and-verify", "quality-rubric"]) {
  assert.ok(core.stdout.includes("<!-- BEGIN references/" + name + ".md -->"), "missing " + name);
}
assert.ok(!core.stdout.includes("<!-- BEGIN references/accessibility.md -->"), "unrequested reference was inlined");
assert.ok(core.stdout.includes("https://raw.githubusercontent.com/hayalows/Skills/main/product-design-os/references/accessibility.md"),
  "omitted references must be listed with a URL");

// Full bundle is complete and is not cut off when piped.
const full = run("product-design-os", "--all");
assert.equal(full.status, 0);
const refs = fs.readdirSync(path.join(root, "product-design-os/references")).filter((f) => f.endsWith(".md"));
for (const name of refs) assert.ok(full.stdout.includes("<!-- END references/" + name + " -->"), "full bundle missing " + name);
assert.ok(full.stdout.length > 100000, "full bundle looks truncated");
assert.ok(!full.stdout.includes("References not included"), "full bundle omits nothing");

// Master Craft bundles its own method.
const master = run("master-craft", "--refs", "routing,playbooks,product-build,quality-gates,portability");
assert.equal(master.status, 0);
assert.ok(master.stdout.includes("Standalone mode") && master.stdout.includes("<!-- BEGIN references/product-build.md -->"));

// --out writes a file. Bad input fails without output.
const tmp = fs.mkdtempSync(path.join(os.tmpdir(), "mc-bundle-"));
try {
  const out = path.join(tmp, "nested/pdos.md");
  assert.equal(run("product-design-os", "--out", out).status, 0);
  assert.ok(fs.readFileSync(out, "utf8").startsWith("<!--"));
} finally {
  fs.rmSync(tmp, { recursive: true, force: true });
}
for (const bad of [["../outside"], ["product-design-os", "--refs", "../../README"], ["product-design-os", "--refs", "missing"], ["no-such-skill"]]) {
  const result = run(...bad);
  assert.equal(result.status, 1, "must fail: " + bad.join(" "));
  assert.equal(result.stdout, "", "no partial output on failure");
}
assert.equal(run().status, 2);

// Every reference linked from the two entrypoints exists, and every reference file is linked.
for (const skill of ["master-craft", "product-design-os"]) {
  const entry = read(skill + "/SKILL.md");
  const linked = new Set([...entry.matchAll(/(?:\(|`)(references\/[a-z0-9-]+\.md)/g)].map((m) => m[1]));
  for (const file of linked) assert.ok(fs.existsSync(path.join(root, skill, file)), skill + " links a missing file: " + file);
  for (const file of fs.readdirSync(path.join(root, skill, "references"))) {
    if (file === "research-notes.md") continue; // design history, intentionally not loaded during tasks
    assert.ok(linked.has("references/" + file), skill + "/references/" + file + " is not linked from SKILL.md");
  }
  for (const m of entry.matchAll(/`((?:scripts|assets)\/[\w.-]+)`/g)) {
    assert.ok(fs.existsSync(path.join(root, skill, m[1])), skill + " names a missing file: " + m[1]);
  }
  const description = entry.match(/^description: "(.*)"$/m)?.[1] ?? "";
  assert.ok(description.length >= 30 && description.length <= 1024, skill + " description length " + description.length);
  assert.ok(entry.split("\n").length < 500, skill + " entrypoint should stay under 500 lines");
}

// Cross-agent entry files and the index stay in step with the library.
assert.ok(read("AGENTS.md").includes("master-craft/SKILL.md"), "AGENTS.md must point at Master Craft");
assert.ok(read("CLAUDE.md").includes("@AGENTS.md"), "CLAUDE.md must import AGENTS.md");
const index = read("llms.txt");
// llms.txt is a curated entrypoint; the generated catalogue is exhaustive and grows automatically.
const inventory = JSON.parse(spawnSync(process.execPath, [path.join(root,"master-craft/scripts/inventory.mjs"),"--local","--json"], {encoding:"utf8"}).stdout);
const generated = spawnSync(process.execPath,[path.join(root,"master-craft/scripts/catalogue.mjs"),"--local"],{encoding:"utf8"});
assert.equal(generated.status,0,generated.stderr);
for (const skill of inventory.skills) assert.ok(generated.stdout.includes("/"+skill.path+")"), "Dynamic catalogue missing "+skill.path);
for (const m of index.matchAll(/https:\/\/raw\.githubusercontent\.com\/hayalows\/Skills\/main\/([^)\s]+)/g)) {
  assert.ok(fs.existsSync(path.join(root, m[1])), "llms.txt links a missing path: " + m[1]);
}

console.log("PASS: portable bundles, entrypoint links, agent entry files and llms.txt index");
