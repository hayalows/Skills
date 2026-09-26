import fs from "node:fs";
import path from "node:path";

const root = process.cwd();
const siteDir = path.join(root, "site");
const distDir = path.join(root, "dist");

const catalog = {
  "product-design-os": { category: "Product & UX", featured: true, label: "Product Design OS" },
  "website-ux-audit": { category: "Product & UX", label: "Website UX Audit" },
  "ui-ux-craft": { category: "Product & UX", label: "UI/UX Craft" },
  "design-taste-frontend": { category: "Design & Frontend", featured: true, label: "Design Taste: Frontend" },
  "frontend-design": { category: "Design & Frontend", label: "Frontend Design" },
  "papa-kojo-writing-style": { category: "Writing", featured: true, label: "Papa Kojo Writing Style" },
  "human-copywriting": { category: "Writing", label: "Human Copywriting" },
  "humanize-my-writing": { category: "Writing", label: "Humanize My Writing" },
  "lunour-brand-strategy": { category: "Brand", featured: true, label: "Lunour Brand Strategy" },
  "lunour-naming": { category: "Brand", label: "Lunour Naming" },
  "consulting-grade-reports-decks": { category: "Reports & Research", label: "Consulting-Grade Reports & Decks" },
  "premium-editorial-report-pdf": { category: "Reports & Research", label: "Premium Editorial Reports" },
  "personal-craft": { category: "Workflow", label: "Personal Craft" },
  "luna-astra-behavior": { category: "Workflow", label: "Luna / Astra Behavior" }
};

function parseFrontmatter(markdown) {
  const match = markdown.match(/^---\n([\s\S]*?)\n---/);
  if (!match) return {};
  const data = {};
  for (const line of match[1].split("\n")) {
    const idx = line.indexOf(":");
    if (idx === -1) continue;
    const key = line.slice(0, idx).trim();
    let value = line.slice(idx + 1).trim();
    if ((value.startsWith('"') && value.endsWith('"')) || (value.startsWith("'") && value.endsWith("'"))) {
      value = value.slice(1, -1);
    }
    data[key] = value;
  }
  return data;
}

fs.rmSync(distDir, { recursive: true, force: true });
fs.mkdirSync(path.join(distDir, "skills"), { recursive: true });

const skills = [];
for (const [slug, meta] of Object.entries(catalog)) {
  const sourcePath = path.join(root, slug, "SKILL.md");
  const markdown = fs.readFileSync(sourcePath, "utf8");
  const frontmatter = parseFrontmatter(markdown);
  const skill = {
    slug,
    name: meta.label || frontmatter.name || slug,
    canonicalName: frontmatter.name || slug,
    description: frontmatter.description || "",
    category: meta.category,
    featured: Boolean(meta.featured),
    markdown
  };
  skills.push(skill);
  fs.writeFileSync(
    path.join(distDir, "skills", `${slug}.json`),
    JSON.stringify(skill)
  );
}

const index = skills
  .map(({ markdown, ...skill }) => skill)
  .sort((a, b) => Number(b.featured) - Number(a.featured) || a.name.localeCompare(b.name));

fs.writeFileSync(path.join(distDir, "skill-index.json"), JSON.stringify(index));
for (const asset of ["index.html", "styles.css", "app.js", "favicon.svg"]) {
  fs.copyFileSync(path.join(siteDir, asset), path.join(distDir, asset));
}
