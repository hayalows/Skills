# Design craft

## Make taste accountable

Treat taste as context-sensitive judgment about hierarchy, proportion, density, rhythm, content, and interaction. Do not equate quality with a fashionable font, gradients, large rounded cards, empty space, monochrome, or a particular brand. These can be appropriate choices, never automatic defaults.

Use this sequence for substantial visual work:
1. State who is using it, under what conditions, and what they need to accomplish.
2. Identify the primary decision or action and rank the information needed for it.
3. Inspect approved assets and current screens. For new or materially redesigned work, inspect two or three relevant references when available. Select references for comparable tasks, content density, and platform. Record the useful principle and why it transfers. Do not claim inspection if unavailable or copy branding, proprietary assets, or entire layouts.
4. For a genuinely open visual brief, consider two plausible directions briefly, select one with a reason, and proceed. Do not require the user to choose unless the decision materially affects their goal.
5. Write a compact design specification, implement a representative screen or section with realistic content, render it, correct structural weaknesses, then extend its system.
6. Inspect the complete flow and its states, not only a hero or ideal empty screen.

## Compact design specification

Record the following in working notes, not product UI:
- Audience, main task, reading order, and primary action.
- Three concrete visual characteristics with implementation consequences. Example: “compact operational interface” means aligned data columns, short labeled controls, and details disclosed on demand.
- Typography roles, content widths, spacing scale, surfaces, semantic colors, border/radius choices, icon family, motion purpose, and responsive transformations.
- Intentional signature: one or two choices grounded in the product, such as a useful timeline or distinctive editorial typography. Omit decorative novelty when it hurts task completion.
- What the existing approved design requires you to preserve.

Reuse project tokens first. If none exist, create a small semantic token system; avoid per-component arbitrary values. Distinguish brand colors from status colors and test selected, hover, disabled, and focus states independently.

## Composition and typography

Use layout and proximity to express relationships. Give the main action a clear place in the hierarchy. Avoid a screen where every section, button, or metric demands equal attention.

Choose typography by role and reading conditions. Use a restrained, reusable scale; visible differences between heading levels; comfortable line spacing; and readable body copy. As starting heuristics, consider body text around 16–18 CSS px and prose widths around 45–75 characters, then adjust for platform, font, audience, and density. These are design heuristics, not accessibility guarantees. Do not shrink essential text to solve layout problems.

Use consistent alignment and intentional whitespace. Put related elements closer together than separate groups. Judge whole-screen balance before shadows, gradients, or small decorative details. Use tables for comparative records and aligned numeric columns; use cards when items need separate grouping. Do not wrap every label in a card.

Choose icons from a consistent family. Use text labels for unfamiliar or consequential actions. Select imagery for its information or emotional purpose, with appropriate crops, resolution, rights, alternative text, and loading cost. Do not use generated imagery for exact charts or factual diagrams.

## Design the actual work

Map entry → decision → action → feedback → durable outcome → recovery. Minimize unnecessary choices, repeated entry, hidden prerequisites, and mode changes. Optimize successful completion, not merely click count.

For forms, keep visible labels, explain unusual requirements before submission, preserve input after errors, and put actionable errors near affected fields. Consider an error summary for long forms. Use progressive disclosure for secondary detail, never to hide required instructions or task status.

For operations tools, prioritize lookup, record identity, status, next action, and exceptions. Separate no records, no search matches, insufficient permission, and failed loading. Preserve useful search/filter context across navigation. Explain selection and bulk-action scope.

For saving, show pending, successful, and failed outcomes truthfully. Prevent duplicate submissions. Do not show a durable success before the server confirms it unless optimistic behavior includes rollback and clear feedback. On stale or concurrent data, avoid silently overwriting another person's work.

For slow or unreliable connections, protect entered work, make retry safe, show useful progress, and avoid unnecessary requests. Only claim offline capability when implemented and verified.

## Responsive behavior and accessibility

Choose breakpoints from content failures, not device labels alone. Specify what wraps, moves, collapses, or becomes scrollable. Maintain important actions on mobile. Avoid fixed-height clipping, hidden columns containing essential information, and sticky elements covering content or focus.

Target WCAG 2.2 AA. Check semantic structure, accessible names, keyboard operation, focus visibility and obstruction, error identification, text and non-text legibility, zoom/reflow, target sizes, and reduced motion. Consult W3C for exact criteria and exceptions. Automated scans alone do not establish compliance.

Inspect a narrow phone, a relevant typical phone, desktop, and a content-driven stress width. Exercise long names, missing values, large numbers, long translations where relevant, browser zoom, keyboard navigation, and text resizing. Check actual modal focus, escape/close behavior, and focus restoration. Do not disable user zoom to conceal mobile input issues.

Use motion to explain state or spatial relationships. Honor reduced-motion settings. Avoid scroll hijacking, delayed access to content, or animation competing with the task.

## Review in order

1. Task and content: can the user identify what matters and complete the job?
2. Structure: hierarchy, grouping, reading order, density, responsive behavior.
3. System: repeated typography, spacing, component behavior, state semantics.
4. Detail: optical alignment, icons, borders, motion, copy.
5. Reliability: keyboard, permissions, errors, persistence, slow-network behavior.

Capture a rendered baseline and the changed result when comparison helps. Describe the specific defect, affected user/task, evidence, and correction. Avoid “make it premium” as a review finding. Stop when relevant acceptance criteria pass; do not keep restyling because another aesthetic is possible.
