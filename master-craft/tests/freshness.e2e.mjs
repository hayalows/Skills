import assert from "node:assert/strict";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { spawnSync } from "node:child_process";
import { fileURLToPath } from "node:url";

const sourceScript = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../scripts/inventory.mjs");
const scratch = fs.mkdtempSync(path.join(os.tmpdir(), "master-craft-fresh-"));
const bare = path.join(scratch, "remote.git");
const author = path.join(scratch, "author");
const agent = path.join(scratch, "agent");

function command(cwd, program, args, expectSuccess = true) {
  const result = spawnSync(program, args, {
    cwd, encoding: "utf8", timeout: 15000,
    env: { ...process.env, GIT_TERMINAL_PROMPT: "0" }
  });
  if (expectSuccess && result.status !== 0) {
    throw new Error(program + " " + args.join(" ") + "\n" + result.stderr + "\n" + result.stdout);
  }
  return result;
}
const git = (cwd, ...args) => command(cwd, "git", args).stdout.trim();
function skill(name, version) {
  return "---\nname: " + name + "\ndescription: " + name + " updated description " + version + "\n---\n\n# " + name + "\n\nVERSION: " + version + "\n";
}
function write(cwd, file, content) {
  const destination = path.join(cwd, file);
  fs.mkdirSync(path.dirname(destination), { recursive: true });
  fs.writeFileSync(destination, content);
}
function run(...args) {
  return command(agent, process.execPath, [path.join(agent, "master-craft/scripts/inventory.mjs"), ...args]);
}
function runExpectFailure(...args) {
  return command(agent, process.execPath, [path.join(agent, "master-craft/scripts/inventory.mjs"), ...args], false);
}

try {
  command(scratch, "git", ["init", "--bare", "--initial-branch=main", bare]);
  fs.mkdirSync(author, { recursive: true });
  git(author, "init", "-b", "main");
  git(author, "config", "user.email", "skills-test@example.test");
  git(author, "config", "user.name", "Skills Test");
  git(author, "remote", "add", "origin", bare);
  write(author, "master-craft/scripts/inventory.mjs", fs.readFileSync(sourceScript, "utf8"));
  write(author, "master-craft/SKILL.md", skill("master-craft", "initial"));
  write(author, "product-design-os/SKILL.md", skill("product-design-os", "v1"));
  git(author, "add", ".");
  git(author, "commit", "-m", "Initial skills");
  git(author, "push", "-u", "origin", "main");
  command(scratch, "git", ["clone", "--quiet", "--branch", "main", bare, agent]);
  const first = JSON.parse(run("--latest", "--json").stdout);
  assert.equal(first.verified_latest, true);
  assert.ok(first.revision.match(/^[0-9a-f]{40}$/));
  assert.ok(first.skills.some((item) => item.name === "product-design-os" && item.description.includes("v1")));

  // User updates an existing skill and adds an entirely new skill on GitHub.
  write(author, "master-craft/SKILL.md", skill("master-craft", "current"));
  write(author, "product-design-os/SKILL.md", skill("product-design-os", "v2"));
  write(author, "novel-skill/SKILL.md", skill("novel-skill", "initial"));
  git(author, "add", ".");
  git(author, "commit", "-m", "Update old and add new skill");
  git(author, "push", "origin", "main");
  const fresh = JSON.parse(run("--latest", "--json").stdout);
  assert.notEqual(fresh.revision, first.revision, "Snapshot SHA must advance");
  assert.ok(fresh.skills.some((item) => item.name === "novel-skill"), "Previously unmapped skill must be discovered");
  assert.ok(fresh.skills.some((item) => item.name === "product-design-os" && item.description.includes("v2")), "Updated metadata must come from fetched version");
  assert.ok(run("--at", fresh.revision, "--read", "master-craft").stdout.includes("VERSION: current"));
  assert.ok(run("--at", first.revision, "--read", "master-craft").stdout.includes("VERSION: initial"));
  const chosen = run("--at", fresh.revision, "--read", "product-design-os").stdout;
  assert.ok(chosen.includes("VERSION: v2"), "Selected skill must come from the latest remote revision");
  assert.ok(chosen.endsWith("\n"), "Skill content must be returned without trimming");
  assert.ok(run("--at", fresh.revision, "--read", "novel-skill").stdout.includes("VERSION: initial"));
  assert.ok(fs.readFileSync(path.join(agent, "product-design-os/SKILL.md"), "utf8").includes("VERSION: v1"), "Refreshing must not overwrite the local working tree");
  assert.ok(!fs.existsSync(path.join(agent, "novel-skill")), "Refreshing must not create local worktree directories");

  // A later update is visible on the next invocation, while the running task
  // can keep its earlier SHA pinned for reproducible results.
  write(author, "product-design-os/SKILL.md", skill("product-design-os", "v3"));
  git(author, "add", ".");
  git(author, "commit", "-m", "Another instruction revision");
  git(author, "push", "origin", "main");
  const newer = JSON.parse(run("--latest", "--json").stdout);
  assert.ok(run("--at", newer.revision, "--read", "product-design-os").stdout.includes("VERSION: v3"));
  assert.ok(run("--at", fresh.revision, "--read", "product-design-os").stdout.includes("VERSION: v2"), "Pinned version must remain consistent");

  // Offline/failing GitHub refresh is explicit. Never silently call stale
  // instructions 'latest' or delete a user's local changes.
  git(agent, "remote", "set-url", "origin", path.join(scratch, "missing-remote.git"));
  const failed = runExpectFailure("--latest", "--json");
  assert.notEqual(failed.status, 0, "Missing remote must stop strict live refresh");
  assert.match(failed.stderr, /FRESHNESS_BLOCKED/);
  const local = JSON.parse(run("--local", "--json").stdout);
  assert.equal(local.verified_latest, false);
  assert.ok(local.skills.some((item) => item.name === "product-design-os" && item.description.includes("v1")));
  const unsafe = runExpectFailure("--at", newer.revision, "--read", "../../outside/SKILL.md");
  assert.notEqual(unsafe.status, 0, "Skill selector must reject traversal");

  console.log("PASS: latest revision, updated instructions, new-skill discovery, pinned snapshot, clean worktree, blocked refresh, explicit offline mode and safe paths");
} finally {
  fs.rmSync(scratch, { recursive: true, force: true });
}
