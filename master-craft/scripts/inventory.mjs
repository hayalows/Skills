import fs from "node:fs";
import { parseRoutingBlock, routingError } from "./routing-policy.mjs";
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
  const fields = Object.create(null);
  let routing = null, routingProblem = null;
  const lines = match[1].split(/\r?\n/);
  for (let i = 0; i < lines.length; i++) {
    const pair = lines[i].match(/^([a-zA-Z][\w-]*):\s*(.*)$/);
    if (!pair) continue;
    if (pair[1] === "routing") {
      const block = [];
      while (i + 1 < lines.length && (/^\s{2,}/.test(lines[i + 1]) || lines[i + 1].trim() === "")) block.push(lines[++i]);
      try {
        if (routing || routingProblem) throw Error("duplicate routing block");
        if (pair[2].trim()) throw Error("routing requires a flat indented block");
        routing = parseRoutingBlock(block);
      } catch (error) { routingProblem = error.message; }
      continue;
    }
    let value = pair[2].trim();
    if (/^[|>][+-]?$/.test(value)) {
      const chunks = [];
      while (i + 1 < lines.length && /^\s{2,}\S/.test(lines[i + 1])) chunks.push(lines[++i].trim());
      value = chunks.join(value.startsWith(">") ? " " : "\n");
    } else if (value.startsWith('"') && value.endsWith('"')) {
      try { value = JSON.parse(value); } catch { value = value.slice(1, -1); }
    } else if (value.startsWith("'") && value.endsWith("'")) {
      value = value.slice(1, -1).replaceAll("''", "'");
    }
    fields[pair[1]] = value;
  }
  const meta = {
    name: fields.name || path.basename(path.dirname(file)),
    description: fields.description || "",
    requires_explicit_invocation: fields["disable-model-invocation"] === "true"
  };
  if (routing) meta.routing = routing;
  if (routingProblem) meta.error = "invalid routing metadata: " + routingProblem;
  return meta;
}
// Sidecar keeps imported upstream skill instructions byte-for-byte intact.
function sidecarPath(p) { return p.replace(/SKILL\.md$/, "routing.json"); }
function withSidecar(item, raw) {
  if (raw == null) return item;
  try {
    if (item.routing || item.error) throw Error("ambiguous or invalid frontmatter routing");
    const routing = JSON.parse(raw);
    const error = routingError(routing);
    if (error) throw Error(error);
    item.routing = routing;
    item.routing_source = "sidecar";
  } catch (error) { item.error = "invalid routing sidecar: " + error.message; }
  return item;
}
function isSkill(p) {
  if (!p.endsWith("/SKILL.md") || p.startsWith("/") || p.includes("\\") || p.split("/").includes("..")) return false;
  return !p.split("/").some((part) => [".git", "node_modules", "dist", "coverage", ".next", "versions"].includes(part));
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
  const all = entries.map(row => {
    const separator = row.indexOf("\t");
    return { info: row.slice(0, separator), path: row.slice(separator + 1) };
  });
  const blobs = all.filter(entry => /^100(?:644|755) blob /.test(entry.info));
  const byPath = new Map(blobs.map(entry => [entry.path, entry.info.split(" ")[2]]));
  const allPaths = new Set(all.map(entry => entry.path));
  return blobs.filter(entry => isSkill(entry.path)).map(entry => ({
    path: entry.path, sha: byPath.get(entry.path),
    ...(byPath.has(sidecarPath(entry.path)) ? { routing_sha: byPath.get(sidecarPath(entry.path)) } : allPaths.has(sidecarPath(entry.path)) ? { invalid_sidecar: true } : {})
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
    // Resolve the advertised SHA first so concurrent fetches cannot replace it.
    if (latest) {
      const remote = git("remote", "get-url", "origin");
      if (!remote) throw new Error("Git origin remote is not configured");
      const advertised = git("ls-remote", "--exit-code", "origin", "refs/heads/main");
      const match = advertised.match(/^([0-9a-f]{40})\trefs\/heads\/main$/);
      if (!match) throw new Error("Could not resolve exactly one main revision");
      revision = match[1];
      git("fetch", "--quiet", "--no-tags", "--no-write-fetch-head", "origin", revision);
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
      if (item.invalid_sidecar) item.error = "routing sidecar must be a regular file";
      if (item.routing_sha) withSidecar(item, gitRaw("show", revision + ":" + sidecarPath(item.path)));
    }
  } else {
    items = localPaths().map(p => {
      const item = { path: p, origin: origin(p), ...parseMetadata(fs.readFileSync(path.join(root, p), "utf8"), p) };
      const sidecar = path.join(root, sidecarPath(p));
      let stat;
      try { stat = fs.lstatSync(sidecar); } catch (error) { if (error.code !== "ENOENT") throw error; }
      if (stat) {
        if (!stat.isFile()) item.error = "routing sidecar must be a regular file";
        else withSidecar(item, fs.readFileSync(sidecar, "utf8"));
      }
      return item;
    });
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
