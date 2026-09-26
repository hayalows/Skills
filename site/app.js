const directoryView = document.querySelector("#directory-view");
const detailView = document.querySelector("#detail-view");
const grid = document.querySelector("#skill-grid");
const filtersEl = document.querySelector("#filters");
const searchInput = document.querySelector("#search-input");
const resultsCount = document.querySelector("#results-count");
const emptyState = document.querySelector("#empty-state");
const clearFilters = document.querySelector("#clear-filters");
const detail = document.querySelector("#skill-detail");
const template = document.querySelector("#skill-card-template");

let skills = [];
let activeCategory = "All";
let query = "";

const categoryOrder = ["All", "Product & UX", "Design & Frontend", "Writing", "Brand", "Reports & Research", "Workflow"];

function escapeHtml(value = "") {
  return value.replace(/[&<>"']/g, (char) => ({
    "&": "&amp;",
    "<": "&lt;",
    ">": "&gt;",
    '"': "&quot;",
    "'": "&#039;"
  })[char]);
}

function inlineMarkdown(value) {
  let text = escapeHtml(value);
  text = text.replace(/`([^`]+)`/g, "<code>$1</code>");
  text = text.replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>");
  text = text.replace(/\*([^*]+)\*/g, "<em>$1</em>");
  text = text.replace(/\[([^\]]+)\]\((https?:\/\/[^\s)]+)\)/g, '<a href="$2" target="_blank" rel="noreferrer">$1</a>');
  return text;
}

function renderMarkdown(markdown) {
  const body = markdown.replace(/^---\n[\s\S]*?\n---\n?/, "").trim();
  const lines = body.split(/\r?\n/);
  const html = [];
  let paragraph = [];
  let listType = null;
  let inCode = false;
  let code = [];

  const flushParagraph = () => {
    if (!paragraph.length) return;
    html.push(`<p>${inlineMarkdown(paragraph.join(" "))}</p>`);
    paragraph = [];
  };
  const closeList = () => {
    if (!listType) return;
    html.push(`</${listType}>`);
    listType = null;
  };

  for (const line of lines) {
    if (line.trim().startsWith("```")) {
      flushParagraph();
      closeList();
      if (!inCode) {
        inCode = true;
        code = [];
      } else {
        html.push(`<pre><code>${escapeHtml(code.join("\n"))}</code></pre>`);
        inCode = false;
      }
      continue;
    }
    if (inCode) {
      code.push(line);
      continue;
    }
    if (!line.trim()) {
      flushParagraph();
      closeList();
      continue;
    }

    const heading = line.match(/^(#{1,4})\s+(.+)$/);
    if (heading) {
      flushParagraph();
      closeList();
      const level = heading[1].length;
      html.push(`<h${level}>${inlineMarkdown(heading[2])}</h${level}>`);
      continue;
    }

    if (/^---+$/.test(line.trim())) {
      flushParagraph();
      closeList();
      html.push("<hr>");
      continue;
    }

    const unordered = line.match(/^\s*[-*]\s+(.+)$/);
    const ordered = line.match(/^\s*\d+[.)]\s+(.+)$/);
    if (unordered || ordered) {
      flushParagraph();
      const nextType = unordered ? "ul" : "ol";
      if (listType !== nextType) {
        closeList();
        listType = nextType;
        html.push(`<${listType}>`);
      }
      html.push(`<li>${inlineMarkdown((unordered || ordered)[1])}</li>`);
      continue;
    }

    if (line.startsWith("> ")) {
      flushParagraph();
      closeList();
      html.push(`<blockquote>${inlineMarkdown(line.slice(2))}</blockquote>`);
      continue;
    }

    paragraph.push(line.trim());
  }

  flushParagraph();
  closeList();
  if (inCode) html.push(`<pre><code>${escapeHtml(code.join("\n"))}</code></pre>`);
  return html.join("\n");
}

function renderFilters() {
  filtersEl.innerHTML = "";
  const categories = categoryOrder.filter((category) => category === "All" || skills.some((skill) => skill.category === category));
  for (const category of categories) {
    const button = document.createElement("button");
    button.type = "button";
    button.className = "filter";
    button.textContent = category;
    button.setAttribute("aria-pressed", String(activeCategory === category));
    button.addEventListener("click", () => {
      activeCategory = category;
      renderFilters();
      renderCards();
    });
    filtersEl.appendChild(button);
  }
}

function matches(skill) {
  const categoryMatch = activeCategory === "All" || skill.category === activeCategory;
  const needle = query.trim().toLowerCase();
  const text = `${skill.name} ${skill.description} ${skill.category} ${skill.canonicalName}`.toLowerCase();
  return categoryMatch && (!needle || text.includes(needle));
}

function renderCards() {
  const filtered = skills.filter(matches);
  grid.innerHTML = "";

  for (const skill of filtered) {
    const card = template.content.firstElementChild.cloneNode(true);
    card.href = `#/skill/${skill.slug}`;
    if (skill.featured) card.classList.add("is-featured");
    card.querySelector(".card-category").textContent = skill.category;
    card.querySelector(".card-title").textContent = skill.name;
    card.querySelector(".card-description").textContent = skill.description;
    card.setAttribute("aria-label", `Open ${skill.name}`);
    grid.appendChild(card);
  }

  resultsCount.textContent = `${filtered.length} skill${filtered.length === 1 ? "" : "s"} shown`;
  emptyState.hidden = filtered.length !== 0;
  grid.hidden = filtered.length === 0;
  clearFilters.hidden = activeCategory === "All" && !query.trim();
}

function clearAll() {
  activeCategory = "All";
  query = "";
  searchInput.value = "";
  renderFilters();
  renderCards();
  searchInput.focus();
}

async function openSkill(slug) {
  directoryView.hidden = true;
  detailView.hidden = false;
  detail.innerHTML = '<div class="loading-panel">Loading skill…</div>';
  window.scrollTo(0, 0);

  const skill = skills.find((item) => item.slug === slug);
  if (!skill) {
    detail.innerHTML = '<div class="loading-panel">That skill could not be found.</div>';
    return;
  }

  try {
    const response = await fetch(`/skills/${encodeURIComponent(slug)}.json`);
    if (!response.ok) throw new Error("Failed to load skill");
    const full = await response.json();

    detail.innerHTML = `
      <header class="detail-header">
        <div class="detail-meta">
          <span class="detail-chip primary">${escapeHtml(full.category)}</span>
          <span class="detail-chip">Source-backed</span>
          <span class="detail-chip">SKILL.md</span>
        </div>
        <h1>${escapeHtml(full.name)}</h1>
        <p class="detail-description">${escapeHtml(full.description)}</p>
        <div class="detail-actions">
          <button class="button" type="button" data-copy-prompt>Copy use prompt</button>
          <button class="button secondary" type="button" data-download>Download SKILL.md</button>
        </div>
      </header>
      <article class="skill-document">${renderMarkdown(full.markdown)}</article>
    `;

    detail.querySelector("[data-copy-prompt]").addEventListener("click", async (event) => {
      const prompt = `Use the ${full.canonicalName} skill for this task. Read its SKILL.md instructions carefully and follow them.`;
      try {
        await navigator.clipboard.writeText(prompt);
        const button = event.currentTarget;
        const original = button.textContent;
        button.textContent = "Copied";
        setTimeout(() => button.textContent = original, 1400);
      } catch {
        window.prompt("Copy this prompt:", prompt);
      }
    });

    detail.querySelector("[data-download]").addEventListener("click", () => {
      const blob = new Blob([full.markdown], { type: "text/markdown;charset=utf-8" });
      const url = URL.createObjectURL(blob);
      const anchor = document.createElement("a");
      anchor.href = url;
      anchor.download = `${full.slug}-SKILL.md`;
      anchor.click();
      URL.revokeObjectURL(url);
    });

    document.querySelector("#main").focus({ preventScroll: true });
  } catch {
    detail.innerHTML = '<div class="loading-panel">The skill could not be loaded. Please try again.</div>';
  }
}

function showDirectory() {
  detailView.hidden = true;
  directoryView.hidden = false;
  window.scrollTo(0, 0);
  document.querySelector("#main").focus({ preventScroll: true });
}

function route() {
  const match = location.hash.match(/^#\/skill\/([^/?#]+)/);
  if (match) openSkill(decodeURIComponent(match[1]));
  else showDirectory();
}

async function init() {
  try {
    const response = await fetch("/skill-index.json");
    skills = await response.json();
    document.querySelector("#skill-count").textContent = skills.length;
    document.querySelector("#category-count").textContent = new Set(skills.map((skill) => skill.category)).size;
    renderFilters();
    renderCards();
    route();
  } catch {
    resultsCount.textContent = "The library could not be loaded.";
  }
}

searchInput.addEventListener("input", () => {
  query = searchInput.value;
  renderCards();
});
clearFilters.addEventListener("click", clearAll);
document.querySelectorAll("[data-clear]").forEach((button) => button.addEventListener("click", clearAll));
window.addEventListener("hashchange", route);

init();
