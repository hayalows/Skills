# Visual Craft Engine (v3)

Use for a new or materially redesigned interface, not a small bug fix. This module sharpens visual execution inside Product Design OS. It does not override accessibility, real user needs, brand requirements, evidence, performance, or interaction states. Adapted and modified from Google Gemini Frontend Design v1.0.0 (Apache-2.0); see [source map](source-map.md) and [licence](gemini-frontend-design-LICENSE.txt).

## 1. Choose a surface mode

Choose the mode for each surface, not the product category as a whole. A store's campaign and its checkout need different defaults.

| Mode | Opening | Visual intensity | Main risk |
| --- | --- | --- | --- |
| Expressive: campaign, portfolio, product showcase | Distinctive subject-led headline, image or working demo | High when earned | generic hero or heavy media |
| Reading: editorial, news, documentation | Masthead, title or story index; content first | Moderate | unnecessary marketing banner |
| Utility: search, maps, analytics, admin | Working controls, results or data immediately | Quiet | visual drama obscures the task |
| Transaction: payment, signup, checkout | Purpose, cost or requirements, next action | Quiet and reassuring | lost trust or hidden information |

Existing brands and explicit directions win. For a new direction, compare two meaningfully different compositions using the same copy and assets. Choose the one that best serves the user, not the one that looks least familiar. Record mode, subject-derived signature, type roles, composition, image intent, motion level and constraints.

## 2. Compose the opening and the whole page

For expressive work consider:
- A wide typographic opening with a subject-led interactive stage.
- Immersive edge-to-edge art with an intentionally clear reading area.
- Depth using a foreground object and display text, without covering essential words.
- Poster-like scale and deliberate asymmetry.
- A split layout if simultaneous reading and demonstration help the decision.

Avoid defaulting to a half-width headline with a stock image, two buttons and a statistics strip. Use one primary action when the task has one; preserve secondary actions that are genuinely needed. Aim for short supporting copy, roughly 25 words on a simple marketing hero; never remove necessary qualifications or instructions to hit a count. Keep the heading readable, reflowable and visible before animation. Let media sit behind a compact header only if the brand, focus and text stay legible at rest and while scrolling.

In utility or transaction mode, do not insert a decorative marketing hero ahead of the task. Show working controls and meaningful content. Use predictable layouts for repeated comparisons. Keep navigation available and use semantic headings.

Plan the rhythm through every major section. Give each section a job and choose a structure that fits: gallery, specification table, narrative, demonstration, comparison or quiet reading. Repeat components when the content repeats. Do not force random variety. The opening's palette, typography, spacing and visual signature should still feel related to the footer.

## 3. Type, colour and proportion

Start with one or two type families, three body-size roles for expressive or reading work (section heading, body, supporting text), and a fourth for genuinely dense utility work if necessary. The main display title and wordmark may use separate roles. Existing systems, localization, content hierarchy and accessibility can justify extra roles. Keep body prose and its lists at the same readable scale; distinguish roles by weight, grouping and colour before adding another size. Use tabular figures for aligned numbers rather than a new font family unless the subject needs one.

Aim for about 45 to 75 characters per line, with 65 as a starting point. Do not use this as a fixed width on phones. Avoid tiny first-screen text; increase sizes rather than hide important content. Test 320px, 200% zoom, long strings and currency glyphs. Do not use aggressive tracking or tight leading when they harm legibility.

Explore palettes grounded in materials, audience and brand, rather than reflex cream and rust or dark neon. Give text, backgrounds and state colours semantic tokens. A broad expressive colour field is fine if it does not weaken interactive meaning. Measure real text and control contrast, including across the image crop at each breakpoint.

## 4. Art direction and motion

For each useful image define subject, intended job, aspect ratio, crop, focal point, light and palette. Plan space for text separately; use stable sizes and meaningful alternatives. Prefer supplied brand assets and real screenshots for factual claims. Concept illustrations must not be presented as actual products, customers or results. Use generated imagery only when appropriate and available; otherwise choose supplied assets, original SVG, CSS or canvas, or a typographic design. Never guess asset URLs. Check responsive crops, loading cost and asset rights. Use the constrained-contexts reference when bandwidth is a concern.

Choose motion by function: feedback, state transition, explanation or expressive storytelling. Ordinary feedback can start around 140 to 240ms, using ease-out and explicit transition properties. Prefer opacity and transform where suitable. Do not delay visible tap feedback to wait for animation. Keep native scrolling for utilitarian surfaces. A pinned sequence or interactive scene needs a keyboard-operable, responsive static alternative, a performance case, and reduced-motion handling. Keep content visible at rest even if scripts fail. No decorative perpetual motion by default. A deliberate static interface is valid.

## 5. Remove unearned decoration

Review every eyebrow, tag, badge, stat strip, gradient, numbered prefix, duplicate CTA and card inside a card. Ask what information or interaction disappears if it is removed. If nothing useful is lost, remove it. Keep real status, categories, sequence numbers, errors, costs, consent, help, labels, and distinct actions. Use plain language and consistent control names. Do not remove accessible names, focus indicators or touch areas for visual neatness. Prefer grouping by space or subtle separation when containers add no meaning. Do not invent telemetry, logos, testimonials or capabilities. Keep the design specific to the subject through the whole page.

## 6. Score visual craft separately

Use only for new or materially redesigned surfaces with rendered evidence. Score 0 to 5: 0 absent/broken, 1 major defect, 2 weak, 3 coherent and usable, 4 deliberate and polished, 5 exceptional execution checked against edge cases. If evidence is missing mark NV (not verified). Do not treat NV as zero or a pass. A truly inapplicable dimension may be NA with a reason; report the denominator. Intentional absence of optional imagery or animation can be scored for its appropriateness, not penalized for absence.

| Dimension | What a strong result demonstrates | Floor |
| --- | --- | --- |
| Composition | Focal point serves the surface; opening and scrolled sections fit content | 3 |
| Type | Coherent roles, readable wrapping and long-content resilience | 3 |
| Colour and art direction | Subject-specific palette, real measured readability, meaningful states | 3 |
| Imagery | Relevant and consistent asset direction, or well-justified text-only design | 3 |
| Spacing and proportion | Grouping, rhythm, alignment and reflow across widths | 3 |
| Motion | Appropriate, stable, responsive feedback; usable reduced-motion path | 3 |
| Visual consistency | Same design intent from first screen to final section or state | 3 |
| Restraint | Every prominent element has a meaningful purpose | 3 |

Record a concrete observation, viewport/state and smallest fix for each weak score. A full rubric is out of 40; otherwise report earned points over applicable verified points plus NV and NA counts. Never claim a pass if a floor fails or an applicable dimension is NV. The separate product rubric and all applicable gates still govern readiness. Do not claim that visual quality predicts conversion without user evidence.

## 7. Review and revise

Capture 360, 768 and 1280 widths, plus 320 reflow and relevant edge cases. Inspect the real opening viewport, each major scrolled section, and the footer at desktop and phone heights. A full-page image is helpful for overall rhythm but not a substitute for checking fixed navigation and interaction. Operate the main action, keyboard path and reduced-motion state. Check real contrast and loading behaviour. Fix the most material problem, then rerender and rescore. If tools cannot render the result, state NOT VISUALLY VERIFIED.
