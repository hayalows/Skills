import fs from "node:fs";
import path from "node:path";
import { execFileSync } from "node:child_process";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");
const args = process.argv.slice(2);
const latest = args.includes("--latest");
const offline = args.includes("--local");
const json = args.includes("--json");

function argValue(flag) {
  const i = args.indexOf(flag);
  if (i === -1) return null;
  if (!args[i + 1] || args[i + 1].startsWith("--")) throw new Error("Missing value for " + flag);
  return args[i + 1];
}

function gitRaw(...argv) {
  return execFileSync("git", argv, {
    cwd: root, encoding: "utf8", timeout: 30000, maxBuffer: 20 * 1024 * 1024,
    stdio: ["ignore", "pipe", "pipe"]
  });
}
function git(...argv) { return gitRaw(...argv).trimEnd(); }
function parseMetadata(content, file) {
  const match = content.match(/^---\r?\n([\s\S]*?)\r?\n---(?:\r?\n|$)/);
  if (!match) return { name: path.basename(path.dirname(file)), description: "", error: "missing frontmatter" };
  const fields = {};
  const lines = match[1].split(/\r?\n/);
  for (let i = 0; i < lines.length; i++) {
    const pair = lines[i].match(/^([a-zA-Z][\w-]*):\s*(.*)$/);
    if (!pair) continue;
    let value = pair[2].trim();
    if (value === "|" || value === ">") {
      const chunks = [];
      while (i + 1 < lines.length && /^\s{2,}\S/.test(lines[i + 1])) chunks.push(lines[++i].trim());
      value = chunks.join(value === ">" ? " " : "\n");
    } else if (value.startsWith('"') && value.endsWith('"')) {
      try { value = JSON.parse(value); } catch { value = value.slice(1, -1); }
    } else if (value.startsWith("'") && value.endsWith("'")) {
      value = value.slice(1, -1).replaceAll("''", "'");
    }
    fields[pair[1]] = value;
  }
  return {
    name: fields.name || path.basename(path.dirname(file)),
    description: fields.description || "",
    requires_explicit_invocation: fields["disable-model-invocation"] === "true"
  };
}
function isSkill(p) {
  if (!p.endsWith("/SKILL.md") || p.startsWith("/") || p.includes("\\") || p.split("/").includes("..")) return false;
  return !p.split("/").some((part) => [".git", "node_modules", "dist", "coverage", ".next"].includes(part));
}
function origin(p) {
  return p.startsWith("collections/matt-pocock-skills/") ? "matt-pocock" : "hayalows";
}
function localPaths() {
  const result = [];
  const walk = (dir) => {
    for (const item of fs.readdirSync(path.join(root, dir), { withFileTypes: true })) {
      if (item.name.startsWith(".") || ["node_modules", "dist", "coverage", ".next"].includes(item.name) || item.isSymbolicLink()) continue;
      const relative = path.posix.join(dir, item.name);
      if (item.isDirectory()) walk(relative);
      else if (item.isFile() && isSkill(relative)) result.push(relative);
    }
  };
  walk("");
  return result.sort();
}
function remotePaths(commit) {
  const entries = gitRaw("ls-tree", "-r", "-z", "--full-tree", commit).split("\0").filter(Boolean);
  return entries.map((row) => {
    const separator = row.indexOf("\t");
    return { info: row.slice(0, separator), path: row.slice(separator + 1) };
  }).filter((entry) => isSkill(entry.path) && entry.info.includes(" blob ")).map((entry) => ({
    path: entry.path, sha: entry.info.split(" ")[2]
  })).sort((a,b)=>a.path.localeCompare(b.path));
}
function resolvePath(specifier, paths) {
  if (!specifier) return null;
  const exact = paths.find((p) => p.path === specifier);
  if (exact) return exact;
  if (specifier.includes("/") || specifier.includes("\\") || specifier.includes("..")) throw new Error("Unknown or unsafe skill path: " + specifier);
  const found = paths.filter((p) => path.posix.basename(path.posix.dirname(p.path)) === specifier);
  if (found.length === 0) throw new Error("No skill named " + specifier + " at this revision");
  if (found.length !== 1) throw new Error("Ambiguous skill name " + specifier + "; use its full relative path");
  return found[0];
}

try {
  if (latest && offline) throw new Error("Choose --latest or --local, not both");
  if (argValue("--at") && (latest || offline)) throw new Error("--at is a pinned source revision; do not combine with --latest or --local");
  const specifier = argValue("--read");
  const pinned = argValue("--at");
  if (pinned && !/^[0-9a-f]{40}$/i.test(pinned)) throw new Error("--at requires a complete 40-character commit SHA");
  let revision = null;
  let source = "local-checkout";
  let verifiedLatest = false;
  let items;
  if (latest || pinned) {
    // Fetching changes Git objects and FETCH_HEAD only. It never checks out, merges,
    // resets or replaces the project's working files.
    if (latest) {
      const remote = git("remote", "get-url", "origin");
      if (!remote) throw new Error("Git origin remote is not configured");
      git("fetch", "--quiet", "--no-tags", "origin", "refs/heads/main");
      revision = git("rev-parse", "FETCH_HEAD");
      verifiedLatest = true;
    } else {
      revision = pinned;
      if (git("cat-file", "-t", revision) !== "commit") throw new Error("Pinned SHA is not a locally available commit");
    }
    source = verifiedLatest ? "git-origin-main" : "pinned-git-commit";
    items = remotePaths(revision);
    for (const item of items) {
      const content = gitRaw("show", revision + ":" + item.path);
      Object.assign(item, parseMetadata(content, item.path), { origin: origin(item.path) });
    }
  } else {
    items = localPaths().map((p) => ({
      path: p, origin: origin(p),
      ...parseMetadata(fs.readFileSync(path.join(root, p), "utf8"), p)
    }));
    try { revision = git("rev-parse", "HEAD"); } catch { /* unversioned checkout */ }
  }
  const selected = resolvePath(specifier, items);
  if (selected) {
    const content = latest || pinned ? gitRaw("show", revision + ":" + selected.path) : fs.readFileSync(path.join(root, selected.path), "utf8");
    if (json) console.log(JSON.stringify({ source, revision, verified_latest: verifiedLatest, skill: selected, content }, null, 2));
    else process.stdout.write(content);
  } else if (json) {
    console.log(JSON.stringify({
      source, revision, verified_latest: verifiedLatest,
      warning: verifiedLatest ? null : "Not verified against current origin/main",
      skills: items
    }, null, 2));
  } else {
    console.log("Source: " + source + " | revision: " + (revision || "unknown") + " | latest verified: " + verifiedLatest);
    for (const item of items) console.log(item.name.padEnd(30) + item.origin.padEnd(15) + item.path);
  }
} catch (error) {
  const message = error.stderr ? error.stderr.toString().slice(0, 1000) : error.message;
  console.error("FRESHNESS_BLOCKED: " + message);
  console.error("No silent fallback was used. Choose --local explicitly to inspect a potentially stale checkout.");
  process.exitCode = 1;
}
