#!/usr/bin/env node
// Master Craft: build one portable Markdown file from a skill folder.
// For chat models and APIs that cannot read a repository: paste the bundle, or pass it as the system prompt.
//
//   node master-craft/scripts/bundle.mjs <skill-dir> [--refs a,b,c | --all] [--out file] [--base-url url]
//
// Read-only apart from --out. It only reads SKILL.md and references/*.md inside the chosen skill folder.

import fs from "node:fs";
import path from "node:path";
import { execFileSync } from "node:child_process";
import { fileURLToPath, pathToFileURL } from "node:url";

const repoRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");
export const DEFAULT_BASE_URL = "https://raw.githubusercontent.com/hayalows/Skills/main/";

function revision(root) {
  for (const key of ["VERCEL_GIT_COMMIT_SHA", "GITHUB_SHA"]) {
    if (/^[0-9a-f]{40}$/i.test(process.env[key] || "")) return process.env[key];
  }
  try {
    return execFileSync("git", ["rev-parse", "HEAD"], { cwd: root, encoding: "utf8", stdio: ["ignore", "pipe", "ignore"] }).trim();
  } catch {
    return "unknown";
  }
}

export function bundle({ root = repoRoot, skill, refs = [], all = false, baseUrl = DEFAULT_BASE_URL }) {
  if (!skill || !/^[a-z0-9][a-z0-9/_-]*$/i.test(skill) || skill.split("/").includes("..")) {
    throw new Error("Give a skill folder relative to the repository root, for example product-design-os");
  }
  const skillDir = path.join(root, skill);
  const entry = path.join(skillDir, "SKILL.md");
  if (!fs.existsSync(entry)) throw new Error("No SKILL.md in " + skill);

  const refDir = path.join(skillDir, "references");
  const available = fs.existsSync(refDir)
    ? fs.readdirSync(refDir).filter((f) => f.endsWith(".md")).sort()
    : [];
  const wanted = all ? available : refs.map((r) => (r.endsWith(".md") ? r : r + ".md"));
  for (const name of wanted) {
    if (!/^[a-z0-9][a-z0-9._-]*\.md$/i.test(name)) throw new Error("Invalid reference name: " + name);
    if (!available.includes(name)) throw new Error("Unknown reference for " + skill + ": " + name);
  }
  const included = available.filter((f) => wanted.includes(f));
  const omitted = available.filter((f) => !wanted.includes(f));
  const base = baseUrl.endsWith("/") ? baseUrl : baseUrl + "/";
  const url = (file) => base + skill + "/" + file;

  const parts = [];
  parts.push([
    "<!--",
    "Portable bundle of the \"" + path.basename(skill) + "\" skill from hayalows/Skills.",
    "Source: " + url("SKILL.md"),
    "Revision: " + revision(root),
    "Included references: " + (included.length ? included.join(", ") : "none"),
    "This is a snapshot. The repository is the source of truth.",
    "-->",
    "",
    "> **How to use this file.** Treat everything below as instructions for the task you are given.",
    "> It contains the skill entrypoint followed by " + (included.length ? included.length + " of its references" : "no references") + ".",
    "> Paths such as `references/name.md` point to the sections below when included.",
    "> You can run only the tools you actually have. Where the text asks for a script or a browser you do not have, say so and do the check by hand.",
    ""
  ].join("\n"));

  parts.push(fs.readFileSync(entry, "utf8").trimEnd());

  for (const name of included) {
    parts.push("\n\n---\n\n<!-- BEGIN references/" + name + " -->\n\n" +
      fs.readFileSync(path.join(refDir, name), "utf8").trimEnd() +
      "\n\n<!-- END references/" + name + " -->");
  }

  if (omitted.length) {
    parts.push("\n\n---\n\n## References not included in this bundle\n\nFetch these only when the task needs them:\n\n" +
      omitted.map((name) => "- `references/" + name + "`: " + url("references/" + name)).join("\n"));
  }

  return { text: parts.join("\n") + "\n", included, omitted };
}

function main(argv) {
  const value = (flag) => {
    const i = argv.indexOf(flag);
    if (i === -1) return null;
    if (!argv[i + 1] || argv[i + 1].startsWith("--")) throw new Error("Missing value for " + flag);
    return argv[i + 1];
  };
  const flagsWithValues = ["--refs", "--out", "--base-url"];
  const positional = argv.filter((a, i) => !a.startsWith("--") && !flagsWithValues.includes(argv[i - 1]));
  if (positional.length !== 1) {
    console.error("Usage: bundle.mjs <skill-dir> [--refs a,b,c | --all] [--out file] [--base-url url]");
    return 2;
  }
  try {
    const result = bundle({
      skill: positional[0].replace(/\/+$/, ""),
      refs: (value("--refs") || "").split(",").map((s) => s.trim()).filter(Boolean),
      all: argv.includes("--all"),
      baseUrl: value("--base-url") || DEFAULT_BASE_URL
    });
    const out = value("--out");
    if (out) {
      fs.mkdirSync(path.dirname(path.resolve(out)), { recursive: true });
      fs.writeFileSync(out, result.text);
      console.error("Wrote " + out + " (" + result.text.length + " characters, " + result.included.length + " references)");
    } else {
      process.stdout.write(result.text);
    }
    return 0;
  } catch (error) {
    console.error("BUNDLE_FAILED: " + error.message);
    return 1;
  }
}

if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) {
  process.exitCode = main(process.argv.slice(2));
}
