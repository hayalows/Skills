#!/usr/bin/env node
// Product Design OS: dependency-free static checks for HTML, CSS, JSX and TSX.
// It reads files as text. It never runs them, fetches anything or edits anything.
//
//   node ui-lint.mjs <file-or-dir> [more paths] [--json]
//   node ui-lint.mjs contrast <foreground> <background>
//
// Exit codes: 0 = no errors, 1 = at least one error, 2 = bad usage.
// A clean result is a floor, not proof of a usable interface. Look at the rendered page.

import fs from "node:fs";
import path from "node:path";
import { pathToFileURL } from "node:url";

const SKIP_DIRS = new Set(["node_modules", ".git", "dist", "build", ".next", "coverage", "vendor"]);
const EXTENSIONS = new Set([".html", ".htm", ".css", ".jsx", ".tsx", ".vue", ".svelte", ".astro"]);

// ---------- colour and contrast ----------

export function parseColor(input) {
  const value = String(input).trim().toLowerCase();
  let m = value.match(/^#([0-9a-f]{3,8})$/);
  if (m) {
    let hex = m[1];
    if (hex.length === 3 || hex.length === 4) hex = [...hex].map((c) => c + c).join("");
    if (hex.length !== 6 && hex.length !== 8) return null;
    return [0, 2, 4].map((i) => parseInt(hex.slice(i, i + 2), 16));
  }
  m = value.match(/^rgba?\(\s*(\d{1,3})[\s,]+(\d{1,3})[\s,]+(\d{1,3})/);
  if (m) return m.slice(1, 4).map(Number);
  return null;
}

function luminance([r, g, b]) {
  const channel = (v) => {
    const s = v / 255;
    return s <= 0.04045 ? s / 12.92 : ((s + 0.055) / 1.055) ** 2.4;
  };
  return 0.2126 * channel(r) + 0.7152 * channel(g) + 0.0722 * channel(b);
}

export function contrastRatio(foreground, background) {
  const a = parseColor(foreground);
  const b = parseColor(background);
  if (!a || !b) return null;
  const [light, dark] = [luminance(a), luminance(b)].sort((x, y) => y - x);
  return (light + 0.05) / (dark + 0.05);
}

export function contrastReport(foreground, background) {
  const ratio = contrastRatio(foreground, background);
  if (ratio === null) return null;
  return {
    foreground, background,
    ratio: Math.round(ratio * 100) / 100,
    normalText: ratio >= 4.5,      // WCAG 2.2 SC 1.4.3 (AA), text below 24px or 18.66px bold
    largeText: ratio >= 3,         // WCAG 2.2 SC 1.4.3 (AA), large text
    nonText: ratio >= 3            // WCAG 2.2 SC 1.4.11 (AA), control boundaries, focus, icons
  };
}

// ---------- helpers ----------

function lineOf(text, index) {
  return text.slice(0, index).split("\n").length;
}

function attr(tag, name) {
  const m = tag.match(new RegExp("\\s" + name + "\\s*=\\s*(?:\"([^\"]*)\"|'([^']*)'|\\{([^}]*)\\}|([^\\s>]+))", "i"));
  return m ? (m[1] ?? m[2] ?? m[3] ?? m[4] ?? "") : null;
}

function hasAttr(tag, name) {
  return new RegExp("\\s" + name + "(\\s|=|>|/)", "i").test(tag);
}

function stripComments(text) {
  return text
    .replace(/<!--[\s\S]*?-->/g, (c) => c.replace(/[^\n]/g, " "))
    .replace(/\/\*[\s\S]*?\*\//g, (c) => c.replace(/[^\n]/g, " "));
}

// ---------- checks ----------

function checkMarkup(text, isDocument, add) {
  if (isDocument) {
    const viewport = text.match(/<meta[^>]+name\s*=\s*["']viewport["'][^>]*>/i);
    if (!viewport) add("error", "viewport-missing", 1, "No viewport meta tag. The page will not fit small screens.");
    else if (/user-scalable\s*=\s*(no|0)|maximum-scale\s*=\s*1(\.0)?\b/i.test(viewport[0])) {
      add("error", "zoom-blocked", lineOf(text, viewport.index), "The viewport blocks pinch zoom. Remove user-scalable=no and maximum-scale=1.");
    }
    const html = text.match(/<html[^>]*>/i);
    if (html && !hasAttr(html[0], "lang")) add("error", "lang-missing", lineOf(text, html.index), "<html> has no lang attribute.");
    if (!/<title>\s*\S[\s\S]*?<\/title>/i.test(text)) add("error", "title-missing", 1, "No non-empty <title>.");
    if (!/<main[\s>]|role\s*=\s*["']main["']/i.test(text)) add("warn", "main-missing", 1, "No <main> landmark.");

    const headings = [...text.matchAll(/<h([1-6])[\s>]/gi)].map((m) => ({ level: Number(m[1]), index: m.index }));
    const h1 = headings.filter((h) => h.level === 1);
    if (headings.length && h1.length === 0) add("warn", "h1-missing", 1, "Headings exist but there is no <h1>.");
    if (h1.length > 1) add("warn", "h1-multiple", lineOf(text, h1[1].index), "More than one <h1>. Use one page title.");
    for (let i = 1; i < headings.length; i++) {
      if (headings[i].level > headings[i - 1].level + 1) {
        add("warn", "heading-skip", lineOf(text, headings[i].index),
          "Heading level jumps from h" + headings[i - 1].level + " to h" + headings[i].level + ".");
      }
    }
  }

  for (const m of text.matchAll(/<img\b[^>]*>/gi)) {
    if (!hasAttr(m[0], "alt") && !/\{\s*\.\.\./.test(m[0])) {
      add("error", "img-alt", lineOf(text, m.index), "<img> has no alt attribute. Use alt=\"\" for decoration.");
    }
    if (!hasAttr(m[0], "width") && !hasAttr(m[0], "height") && !/aspect-ratio/i.test(m[0])) {
      add("info", "img-size", lineOf(text, m.index), "<img> has no width and height. Reserve space to avoid layout shift.");
    }
  }

  for (const m of text.matchAll(/<(div|span|li|p|td|section|img)\b[^>]*\son[Cc]lick\b[^>]*>/g)) {
    const tag = m[0];
    const role = attr(tag, "role");
    if (!(role && /button|link|menuitem|tab|checkbox|switch/.test(role) && hasAttr(tag, "tabindex"))) {
      add("error", "click-non-control", lineOf(text, m.index),
        "Click handler on <" + m[1] + ">. Use <button> or <a> so keyboard and assistive technology can operate it.");
    }
  }

  for (const m of text.matchAll(/\stab[Ii]ndex\s*=\s*["'{]?\s*([0-9]+)/g)) {
    if (Number(m[1]) > 0) add("warn", "tabindex-positive", lineOf(text, m.index), "Positive tabindex changes the natural focus order.");
  }

  for (const m of text.matchAll(/<a\b[^>]*>/gi)) {
    const href = attr(m[0], "href");
    if (href !== null && /^(#|javascript:)/i.test(href.trim()) && href.trim().length <= 1 + 11) {
      if (href.trim() === "#" || /^javascript:/i.test(href.trim())) {
        add("warn", "link-placeholder", lineOf(text, m.index), "Link goes nowhere (href=\"" + href + "\"). Use a real URL or a <button>.");
      }
    }
  }

  // Icon-only buttons and links need an accessible name.
  for (const m of text.matchAll(/<(button|a)\b([^>]*)>([\s\S]*?)<\/\1>/gi)) {
    const open = "<" + m[1] + m[2] + ">";
    if (hasAttr(open, "aria-label") || hasAttr(open, "aria-labelledby") || hasAttr(open, "title")) continue;
    const inner = m[3];
    if (/\{[^}]*\}/.test(inner)) continue; // dynamic content, cannot judge
    const visible = inner.replace(/<svg[\s\S]*?<\/svg>/gi, "").replace(/<[^>]+>/g, "").replace(/&nbsp;/g, " ").trim();
    const imageAlt = [...inner.matchAll(/<img\b[^>]*>/gi)].some((i) => (attr(i[0], "alt") || "").trim());
    const svgTitle = /<title>\s*\S/i.test(inner) || /aria-label\s*=/.test(inner);
    if (!visible && !imageAlt && !svgTitle) {
      add("error", "control-name", lineOf(text, m.index), "<" + m[1] + "> has no text or accessible name.");
    }
  }

  // Form fields need a programmatic label.
  const labelFor = new Set([...text.matchAll(/<label\b[^>]*\s(?:for|htmlFor)\s*=\s*["'{]?([^"'}\s>]+)/gi)].map((m) => m[1]));
  const wrapped = [];
  for (const m of text.matchAll(/<label\b[^>]*>[\s\S]*?<\/label>/gi)) wrapped.push([m.index, m.index + m[0].length]);
  for (const m of text.matchAll(/<(input|select|textarea)\b[^>]*>/gi)) {
    const tag = m[0];
    const type = (attr(tag, "type") || "text").toLowerCase();
    if (m[1].toLowerCase() === "input" && ["hidden", "submit", "button", "reset", "image"].includes(type)) continue;
    if (hasAttr(tag, "aria-label") || hasAttr(tag, "aria-labelledby") || /\{\s*\.\.\./.test(tag)) continue;
    const id = attr(tag, "id");
    if (id && labelFor.has(id)) continue;
    if (wrapped.some(([start, end]) => m.index > start && m.index < end)) continue;
    add("error", "field-label", lineOf(text, m.index),
      "<" + m[1] + "> has no label. A placeholder is not a label.");
  }

  for (const m of text.matchAll(/<(video|audio)\b[^>]*\sautoplay\b[^>]*>/gi)) {
    if (!hasAttr(m[0], "muted")) add("warn", "autoplay-sound", lineOf(text, m.index), "Media autoplays with sound.");
  }
}

function checkStyles(css, add, offsetLine = 0, project = "") {
  const at = (index) => offsetLine + lineOf(css, index);

  const removesOutline = [...css.matchAll(/outline\s*:\s*(none|0)\b/gi)];
  // Focus and reduced-motion rules often live in a shared stylesheet, so look across every scanned file.
  const focusRules = [...(css + "\n" + project).matchAll(/:focus(?:-visible|-within)?\b[^{}]*\{([^}]*)\}/gi)].map((m) => m[1]);
  const hasReplacement = focusRules.some((body) =>
    /outline(?:-width|-style|-color)?\s*:\s*(?!\s*(?:none|0)\b)\S/i.test(body) || /box-shadow\s*:\s*(?!\s*none)\S|border(?:-color)?\s*:/i.test(body));
  if (removesOutline.length && !hasReplacement) {
    add("error", "focus-removed", at(removesOutline[0].index), "Focus outline is removed and no visible replacement is defined.");
  }

  for (const m of css.matchAll(/font-size\s*:\s*([0-9.]+)px/gi)) {
    if (Number(m[1]) < 12) add("warn", "text-tiny", at(m.index), "Text at " + m[1] + "px is hard to read. Keep body text at 16px or larger.");
  }

  if (/(^|[\s;{])(animation|transition)\s*:/i.test(css) && !/prefers-reduced-motion/i.test(css + project)) {
    add("warn", "reduced-motion", at(css.search(/(animation|transition)\s*:/i)), "Motion is defined with no prefers-reduced-motion rule.");
  }

  const vh = css.search(/:\s*100vh\b/);
  if (vh !== -1) add("info", "viewport-height", at(vh), "100vh is taller than the visible area on mobile browsers. Consider 100dvh with a fallback.");

  const justify = css.search(/text-align\s*:\s*justify/i);
  if (justify !== -1) add("info", "justified-text", at(justify), "Justified text creates uneven gaps and is harder to read.");

  const declarations = css.replace(/--[\w-]+\s*:[^;}]+/g, ""); // ignore token definitions
  const colors = new Set([...declarations.matchAll(/#[0-9a-f]{3,8}\b/gi)].map((m) => m[0].toLowerCase()));
  if (colors.size > 12) add("info", "color-sprawl", 1, colors.size + " literal colours outside tokens. Move them to semantic variables.");

  const spacing = new Set();
  for (const m of declarations.matchAll(/(?:margin|padding|gap)[\w-]*\s*:\s*([^;}]+)/gi)) {
    for (const px of m[1].matchAll(/(\d+(?:\.\d+)?)px/g)) spacing.add(Number(px[1]));
  }
  const offGrid = [...spacing].filter((v) => v > 2 && v % 4 !== 0);
  if (offGrid.length > 4) add("info", "spacing-sprawl", 1, "Spacing values off a 4px scale: " + offGrid.sort((a, b) => a - b).join(", ") + ".");

  const important = (css.match(/!important/g) || []).length;
  if (important > 10) add("info", "important-overuse", 1, important + " uses of !important suggest a specificity problem.");
}

export function lintText(source, file = "input.html", project = "") {
  const findings = [];
  const add = (severity, rule, line, message) => findings.push({ file, line, severity, rule, message });
  const ext = path.extname(file).toLowerCase();
  const text = stripComments(source);

  if (ext === ".css") {
    checkStyles(text, add, 0, project);
  } else {
    const isDocument = /<html[\s>]/i.test(text);
    checkMarkup(text, isDocument, add);
    let css = "";
    let firstLine = 0;
    for (const m of text.matchAll(/<style\b[^>]*>([\s\S]*?)<\/style>/gi)) {
      if (!css) firstLine = lineOf(text, m.index) - 1;
      css += m[1] + "\n";
    }
    if (css) checkStyles(css, add, firstLine, project);
  }
  return findings.sort((a, b) => a.line - b.line);
}

function collect(target, out) {
  const stat = fs.statSync(target);
  if (stat.isDirectory()) {
    for (const entry of fs.readdirSync(target, { withFileTypes: true })) {
      if (entry.isSymbolicLink() || entry.name.startsWith(".") || SKIP_DIRS.has(entry.name)) continue;
      collect(path.join(target, entry.name), out);
    }
  } else if (EXTENSIONS.has(path.extname(target).toLowerCase())) {
    out.push(target);
  }
}

function main(argv) {
  if (argv[0] === "contrast") {
    const report = argv.length === 3 ? contrastReport(argv[1], argv[2]) : null;
    if (!report) {
      console.error("Usage: ui-lint.mjs contrast <foreground> <background>   (hex or rgb() values)");
      return 2;
    }
    console.log(report.ratio + ":1  " + report.foreground + " on " + report.background);
    console.log("  normal text (4.5:1): " + (report.normalText ? "pass" : "FAIL"));
    console.log("  large text (3:1):    " + (report.largeText ? "pass" : "FAIL"));
    console.log("  controls, focus, icons (3:1): " + (report.nonText ? "pass" : "FAIL"));
    return report.normalText ? 0 : 1;
  }

  const json = argv.includes("--json");
  const targets = argv.filter((a) => !a.startsWith("--"));
  if (!targets.length) {
    console.error("Usage: ui-lint.mjs <file-or-dir> [more paths] [--json]\n       ui-lint.mjs contrast <foreground> <background>");
    return 2;
  }
  const files = [];
  for (const target of targets) {
    if (!fs.existsSync(target)) { console.error("Not found: " + target); return 2; }
    collect(target, files);
  }
  const sources = files.map((file) => [file, fs.readFileSync(file, "utf8")]);
  const project = sources.map(([file, text]) => path.extname(file).toLowerCase() === ".css"
    ? text
    : [...text.matchAll(/<style\b[^>]*>([\s\S]*?)<\/style>/gi)].map((m) => m[1]).join("\n")).join("\n");
  const findings = sources.flatMap(([file, text]) => lintText(text, file, stripComments(project)));
  const count = (severity) => findings.filter((f) => f.severity === severity).length;
  const summary = { files: files.length, errors: count("error"), warnings: count("warn"), info: count("info") };

  if (json) {
    console.log(JSON.stringify({ summary, findings }, null, 2));
  } else {
    for (const f of findings) console.log(f.severity.toUpperCase().padEnd(5) + " " + f.file + ":" + f.line + "  [" + f.rule + "] " + f.message);
    console.log("\n" + summary.files + " file(s): " + summary.errors + " error(s), " + summary.warnings + " warning(s), " + summary.info + " note(s).");
    console.log("Static text checks only. A clean result does not prove the interface is usable. Render it and look.");
  }
  return summary.errors ? 1 : 0;
}

if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) {
  process.exitCode = main(process.argv.slice(2));
}
