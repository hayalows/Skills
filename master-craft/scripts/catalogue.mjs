import { execFileSync } from "node:child_process";
import { fileURLToPath, pathToFileURL } from "node:url";

export function catalogue(snapshot) {
  const base = snapshot.source === "local-checkout" ? "./" : "https://raw.githubusercontent.com/hayalows/Skills/" + (snapshot.revision ?? "main") + "/";
  const lines = ["# Hayalows Skills - current inventory", "", "Source: " + snapshot.source + " | revision: " + (snapshot.revision ?? "unknown") + " | verified latest: " + snapshot.verified_latest, "", "Start with Master Craft. Load selected instructions and policy at the same revision. Explicit-only skills require a direct user request. Local output may include uncommitted files.", ""];
  for (const skill of snapshot.skills) {
    if (skill.error || !skill.description) throw Error("Invalid skill metadata: " + skill.path);
    const tags = [skill.requires_explicit_invocation ? "explicit only" : null, skill.routing?.category, skill.routing?.allowed_modes?.join("/")].filter(Boolean);
    lines.push("- [" + skill.name + "](" + base + skill.path + ")" + (tags.length ? " [" + tags.join("; ") + "]" : "") + ": " + skill.description.replace(/\s+/g," "));
    if (skill.routing_sha || (snapshot.source === "local-checkout" && skill.routing && skill.routing_source === "sidecar")) lines.push("  - Routing policy: " + base + skill.path.replace(/SKILL\.md$/, "routing.json"));
  }
  return lines.join("\n") + "\n";
}
if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) {
  try {
    const args = process.argv.slice(2);
    if (!args.length) args.push("--latest");
    const snapshot = JSON.parse(execFileSync(process.execPath, [fileURLToPath(new URL("./inventory.mjs", import.meta.url)), ...args, "--json"], {encoding:"utf8",maxBuffer:20*1024*1024}));
    process.stdout.write(catalogue(snapshot));
  } catch (error) { console.error("CATALOGUE_FAILED: " + error.message); process.exitCode = 1; }
}
