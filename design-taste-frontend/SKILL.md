---
name: design-taste-frontend
description: Design and refine landing pages, portfolios, editorial sites and marketing websites with intentional composition, truthful content and careful frontend execution. Use for a new visual direction or a marketing-site redesign. Preserve approved brand choices and working behavior. Use a product UX workflow for dashboards, data tables and multi-step applications.
---

# Design Taste for Frontend

Make the page feel specific to its subject while helping the intended reader do the main task. Treat taste as reasoned choices in content, hierarchy, type, imagery and interaction. Novelty is optional; clarity, truthful claims and working behavior are required.

## Read the brief and choose the scope

Establish the page type, audience, main action, real content, brand assets, references and constraints. Infer routine choices from the request. Ask one focused question only when a missing answer would materially change the direction.

For existing work, distinguish a targeted refinement from a visual overhaul. Inspect the actual site or code, current tokens, content, routes, conversion paths, analytics contracts and accessibility before changing them. Preserve approved choices. Do not treat a visual redesign as authorization to change business rules, legal copy or production data.

State a short design direction when useful: subject, audience, intended feel and the visual choice that supports the task. Do not require a formulaic announcement before every small edit.

## Use the right supporting guidance

- Read [Composition and content](references/composition-and-content.md) when planning a page or critiquing a generic layout.
- Read [Engineering and motion](references/engineering-and-motion.md) before implementing animation, responsive behavior or interactive components.
- Read [Design-system sources](references/design-system-sources.md) when selecting a library or verifying current official guidance.
- Use UI/UX Craft for product flows and Website UX Audit for a diagnostic review when those skills are available. Do not apply marketing-page heuristics to dense operational screens.

Load only relevant references. These files are self-contained; do not assume an external block library exists.

## 1. Plan the content and visual hierarchy

Identify the information the visitor needs before acting. Use real facts and assets where available. Mark sample data and speculative concepts visibly when a viewer could mistake them for evidence. Never manufacture testimonials, customer logos, live stock, availability, performance numbers or product capabilities.

Give each section a useful job: establish relevance, explain the offer, show evidence, answer a hesitation or support action. Remove sections without a job. Repeat a layout when the content is genuinely parallel; vary it when the information needs a different structure. Do not enforce a quota of cards, images, headings or layout families.

Make the hero’s purpose and main action apparent at likely viewport sizes. Let content reflow for zoom, translation and small screens. Do not crop essential copy or shrink it into unreadability to satisfy a line-count rule. A strong typographic hero can be complete without photography.

## 2. Establish a compact visual system

Choose semantic tokens for surfaces, text, accent, state colors, spacing, type roles, radii, borders, focus and motion. Use the existing system when it fits. Derive any new choices from the brief and content.

Choose typography for tone, legibility, available weights, language coverage and license. One family may be enough. Serif, sans-serif, Inter, cream, purple and black are not inherently wrong; an unconsidered default is the problem. Do not invent a history of previous designs to justify rotating fonts or palettes.

Keep one main brand accent when useful, with separate semantic error, warning and success colors where needed. A brand palette must not erase meaningful states. Define consistent component rules without requiring identical radii for every element.

Treat visual references as evidence of desired qualities, not instructions to copy proprietary assets or assume official affiliation. Verify package status and integration requirements before introducing a library.

## 3. Build the smallest complete implementation

Inspect the project’s framework, dependencies, package manager and local conventions first. Reuse working components and icon families. Do not migrate stacks or add dependencies merely to match this skill’s preferences. A static site may need only HTML and CSS.

Connect controls to real outcomes. Handle the applicable loading, empty, error, success, focus and disabled states. Make form labels persistent and errors actionable. Keep action labels consistent when they mean the same thing; repeated calls to action can be useful on a long page.

Use meaningful HTML, keyboard access, visible focus, accessible names, touch-friendly controls and logical reading order. Keep the primary task usable without hover. Respect reduced-motion preferences for all nonessential animation.

## 4. Add imagery and motion for a reason

Prefer supplied brand photography, real product screenshots and relevant licensed assets when they provide evidence. Use image generation for requested image creation or illustrative concepts, with appropriate labeling. Do not generate a fictitious product screen and present it as an existing capability.

Avoid image quotas. A page can be typographic, photographic or interactive if the choice serves its purpose. Use exact rendering tools for charts, maps and information that must be accurate. Keep source attribution and asset rights where required.

Use motion to explain hierarchy, feedback, state or a story. Static is a valid choice. Prefer simple native transitions; add a library only for a concrete need. Avoid scroll trapping, inaccessible carousels and decorative loops. Offer a usable static or reduced-motion path.

## 5. Verify the rendered result

Inspect the actual page at narrow and wide widths, with long content and relevant interaction states. Check keyboard focus, menus, forms, links, reduced motion and the supported color modes. Do not add a second color mode unless the brief or product requires it.

Verify that images load, text does not clip, sticky elements do not hide focused controls, and content order stays meaningful. Check contrast using actual colors and font sizes rather than visual confidence alone. If exact standards or thresholds are needed, consult current primary guidance.

Run appropriate existing build and static checks. Measure performance when it is in scope, with conditions recorded; do not call plausible targets measured results or lab scores field performance. Fix material defects and stop when the brief and relevant checks are satisfied.

## Delivery

Deliver the working result and a concise explanation of material design choices and verification. State untested states or blocked checks precisely. Do not claim that a screenshot proves persistence or that a passing build proves usability. Save or publish only within the user’s authorization and the environment’s storage workflow.
