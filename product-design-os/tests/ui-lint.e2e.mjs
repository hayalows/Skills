// End-to-end checks for scripts/ui-lint.mjs. Runs the real CLI against files on disk.
import assert from "node:assert/strict";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { spawnSync } from "node:child_process";
import { fileURLToPath } from "node:url";
import { contrastRatio } from "../scripts/ui-lint.mjs";
import "./visual-lint.test.mjs";

const here = path.dirname(fileURLToPath(import.meta.url));
const cli = path.join(here, "../scripts/ui-lint.mjs");
const tmp = fs.mkdtempSync(path.join(os.tmpdir(), "pdos-lint-"));
const run = (...args) => spawnSync(process.execPath, [cli, ...args], { encoding: "utf8" });
const write = (name, text) => { const p = path.join(tmp, name); fs.writeFileSync(p, text); return p; };
const rules = (result) => JSON.parse(result.stdout).findings.map((f) => f.rule);

try {
  const bad = write("bad.html", `<!doctype html>
<html>
<head>
<meta name="viewport" content="width=device-width, user-scalable=no">
<style>
  a:focus { outline: none; }
  .fine { font-size: 10px; transition: all 1s; height: 100vh; }
</style>
</head>
<body>
<h1>One</h1><h1>Two</h1><h4>Skipped</h4>
<img src="a.png">
<div onclick="go()">Open</div>
<a href="#">More</a>
<button><svg viewBox="0 0 1 1"></svg></button>
<input type="email" placeholder="Email">
<video autoplay></video>
<span tabindex="3">x</span>
</body>
</html>`);
  const badResult = run(bad, "--json");
  assert.equal(badResult.status, 1, "errors must exit 1");
  const found = rules(badResult);
  for (const rule of ["zoom-blocked", "lang-missing", "title-missing", "main-missing", "h1-multiple", "heading-skip",
    "img-alt", "click-non-control", "link-placeholder", "control-name", "field-label", "autoplay-sound",
    "tabindex-positive", "focus-removed", "text-tiny", "reduced-motion", "viewport-height", "visual-transition-all", "visual-small-text"]) {
    assert.ok(found.includes(rule), "expected rule " + rule + " in " + found.join(","));
  }

  const good = write("good.html", `<!doctype html>
<html lang="en">
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Pay a bill</title>
<style>
  :focus-visible { outline: 2px solid #1d5bd6; }
  .card { padding: 16px; transition: opacity 120ms; }
  @media (prefers-reduced-motion: reduce) { .card { transition: none; } }
</style>
</head>
<body>
<main>
<h1>Pay a bill</h1>
<h2>Amount</h2>
<img src="meter.png" alt="Your meter" width="320" height="200">
<img src="wave.svg" alt="" width="10" height="10">
<form>
  <label for="amount">Amount in cedis</label>
  <input id="amount" inputmode="decimal">
  <label>Phone <input type="tel" name="phone"></label>
  <input type="hidden" name="token" value="x">
  <button type="submit">Pay now</button>
  <button type="button" aria-label="Close"><svg viewBox="0 0 1 1"></svg></button>
  <a href="/help">Get help</a>
</form>
</main>
</body>
</html>`);
  const goodResult = run(good, "--json");
  assert.equal(goodResult.status, 0, "clean page must exit 0: " + goodResult.stdout);
  assert.deepEqual(rules(goodResult), [], "clean page must have no findings");

  const jsx = write("Card.tsx", `export function Card({ item, ...rest }) {
  return (
    <div onClick={() => open(item)}>
      <img src={item.src} />
      <button aria-label="Remove"><Icon /></button>
      <input {...rest} />
    </div>
  );
}`);
  const jsxRules = rules(run(jsx, "--json"));
  assert.ok(jsxRules.includes("click-non-control") && jsxRules.includes("img-alt"), "JSX checks: " + jsxRules.join(","));
  assert.ok(!jsxRules.includes("title-missing"), "fragments are not judged as full documents");
  assert.ok(!jsxRules.includes("field-label"), "spread props cannot be judged, so they are not reported");

  const css = write("site.css", ".x { outline: 0; } .y { margin: 13px 7px 9px 11px 15px; }");
  const cssRules = rules(run(css, "--json"));
  assert.ok(cssRules.includes("focus-removed") && cssRules.includes("spacing-sprawl"), "CSS checks: " + cssRules.join(","));

  // Shared rules count across files: a page may rely on a stylesheet for focus and reduced motion.
  const shared = fs.mkdtempSync(path.join(os.tmpdir(), "pdos-shared-"));
  fs.writeFileSync(path.join(shared, "base.css"), ":focus-visible { outline: 2px solid #1d5bd6; } @media (prefers-reduced-motion: reduce) { * { transition: none; } }");
  fs.writeFileSync(path.join(shared, "page.css"), "a { outline: none; transition: color 120ms; }");
  assert.deepEqual(rules(run(shared, "--json")), [], "rules defined in a shared stylesheet satisfy other files");
  assert.ok(rules(run(path.join(shared, "page.css"), "--json")).includes("focus-removed"), "scanned alone, the gap is reported");
  fs.rmSync(shared, { recursive: true, force: true });

  // Directory scan skips dependencies and reports the right file count.
  fs.mkdirSync(path.join(tmp, "node_modules"));
  write("node_modules/ignored.html", "<img src=x>");
  const dir = JSON.parse(run(tmp, "--json").stdout);
  assert.equal(dir.summary.files, 4, "directory scan must skip node_modules");

  // Contrast: known reference values.
  assert.equal(Math.round(contrastRatio("#000", "#fff")), 21);
  assert.ok(Math.abs(contrastRatio("#777777", "#ffffff") - 4.48) < 0.01, "#777 on white is the classic near miss");
  assert.equal(run("contrast", "#777777", "#ffffff").status, 1);
  assert.equal(run("contrast", "#14181f", "#ffffff").status, 0);
  assert.equal(run("contrast", "blue", "#fff").status, 2, "unsupported colour formats are a usage error");
  assert.equal(run().status, 2);
  assert.equal(run(path.join(tmp, "missing.html")).status, 2);

  // The shipped starter tokens must keep their contrast promise in both themes.
  const tokens = fs.readFileSync(path.join(here, "../assets/tokens.css"), "utf8");
  const [light, dark] = tokens.split("@media (prefers-color-scheme: dark)");
  for (const [theme, block] of [["light", light], ["dark", dark]]) {
    const value = (name) => block.match(new RegExp("--color-" + name + ":\\s*(#[0-9a-f]{6})"))[1];
    const pairs = [
      ["text", "bg", 4.5], ["text", "surface", 4.5], ["text-muted", "bg", 4.5], ["text-muted", "surface", 4.5],
      ["text-muted", "surface-sunken", 4.5], ["accent", "bg", 4.5], ["accent", "surface", 4.5],
      ["on-accent", "accent", 4.5], ["on-accent", "accent-hover", 4.5], ["accent", "accent-soft", 4.5],
      ["danger", "bg", 4.5], ["danger", "danger-soft", 4.5], ["success", "bg", 4.5], ["success", "success-soft", 4.5],
      ["warning", "bg", 4.5], ["warning", "warning-soft", 4.5],
      ["border-strong", "bg", 3], ["border-strong", "surface", 3], ["focus", "bg", 3]
    ];
    for (const [fg, bg, min] of pairs) {
      const ratio = contrastRatio(value(fg), value(bg));
      assert.ok(ratio >= min, theme + " " + fg + " on " + bg + " is " + ratio.toFixed(2) + ", needs " + min);
    }
  }
  assert.equal(run(path.join(here, "../assets/tokens.css")).status, 0, "tokens.css must lint clean");

  console.log("PASS: ui-lint markup, JSX, CSS, directory, contrast and starter-token checks");
} finally {
  fs.rmSync(tmp, { recursive: true, force: true });
}
