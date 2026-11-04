import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");

function parseMetadata(file) {
  const content = fs.readFileSync(file, "utf8");
  const match = content.match(/^---\r?\n([\s\S]*?)\r?\n---/);
  if (!match) return { name: path.basename(path.dirname(file)), description: "", error: "missing frontmatter" };
  const fields = {};
  for (const line of match[1].split(/\r?\n/)) {
    const colon = line.indexOf(":");
    if (colon < 0) continue;
    const key = line.slice(0, colon).trim();
    let value = line.slice(colon + 1).trim();
    if (value.startsWith('"') && value.endsWith('"')) {
      try { value = JSON.parse(value); } catch { value = value.slice(1, -1); }
    } else if (value.startsWith("'") && value.endsWith("'")) value = value.slice(1, -1);
    fields[key] = value;
  }
  return { name: fields.name || path.basename(path.dirname(file)), description: fields.description || "", experimental: fields["disable-model-invocation"] === "true" };
}

const found = [];
function add(absolutePath, origin) {
  if (!fs.existsSync(absolutePath)) return;
  found.push({ ...parseMetadata(absolutePath), path: path.relative(root, absolutePath).replaceAll(path.sep, "/"), origin });
}
for (const item of fs.readdirSync(root, { withFileTypes: true })) {
  if (!item.isDirectory() || item.name.startsWith(".")) continue;
  add(path.join(root, item.name, "SKILL.md"), "hayalows");
}
const base = path.join(root, "collections/matt-pocock-skills/skills");
if (fs.existsSync(base)) {
  for (const group of fs.readdirSync(base, { withFileTypes: true })) {
    if (!group.isDirectory()) continue;
    for (const skill of fs.readdirSync(path.join(base, group.name), { withFileTypes: true })) {
      if (skill.isDirectory()) add(path.join(base, group.name, skill.name, "SKILL.md"), "matt-pocock/" + group.name);
    }
  }
}
found.sort((a, b) => a.path.localeCompare(b.path));
if (process.argv.includes("--json")) console.log(JSON.stringify(found, null, 2));
else for (const item of found) console.log(item.name.padEnd(29) + item.origin.padEnd(25) + item.path);
