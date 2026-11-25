# Build and Verify: The Look Loop

Use this reference whenever a design is implemented in code, or when you review a running product. A design you have not looked at is a guess.

The loop is short: **build a slice, render it, look at it, score it, fix the worst thing, repeat.** Most quality comes from the second and third pass, not the first.

## 1. Before you write code

1. Read the project: framework, components, tokens, breakpoints, icon set, how styles are organised. Use what exists.
2. If there is no token layer, add one first. `assets/tokens.css` is a neutral starting point.
3. Collect real content for the slice: real labels, the longest realistic name, a realistic number of rows, a real error message.
4. Write three to seven acceptance checks a person could tick off by using the screen. Example: "A new user can add a meter reading in under four taps on a 360px screen."

## 2. Build one complete slice

Build one user path end to end before widening. Complete means the path includes the states that this path can reach:

`default, focus, loading, empty, error, success`, plus `disabled`, `offline` and `no permission` where they apply.

Rules while building:

- Semantic HTML first: `button` for actions, `a` for navigation, `label` for every field, headings in order, one `main`.
- Style from tokens. A literal colour or pixel value in a component is a smell.
- Start at the narrowest width you support and let the layout grow.
- Reserve space for anything that loads late (images, async panels) so the page does not jump.
- Wire controls to real outcomes or clearly marked stubs. A button that does nothing is a defect, not a placeholder.

## 3. Run the static floor

```bash
node product-design-os/scripts/ui-lint.mjs path/to/src
node product-design-os/scripts/ui-lint.mjs contrast "#555f6e" "#ffffff"
```

`ui-lint` reads HTML, CSS, JSX, TSX, Vue, Svelte and Astro files as text and reports common failures: missing labels and alt text, click handlers on non-controls, removed focus outlines, blocked zoom, tiny text, motion with no reduced-motion rule, and token sprawl. It needs only Node.

Scan the folder that holds the shared stylesheet as well as the page, because focus and reduced-motion rules are judged across every file scanned.

Fix every error. Review each visual warning as a candidate against the rendered surface. Record the decision and any necessary exception in the Visual Integrity Gate. A clean run is a floor. It cannot see layout, contrast of rendered pairs, focus order or whether the screen makes sense.

## 4. Render it and look

Use whatever the environment offers, in this order of preference:

1. A browser tool or Playwright session that can interact and take screenshots.
2. Headless Chrome from the command line:

   ```bash
   google-chrome --headless=new --hide-scrollbars --screenshot=shot-360.png --window-size=360,800 http://localhost:3000/
   google-chrome --headless=new --hide-scrollbars --screenshot=shot-768.png --window-size=768,1024 http://localhost:3000/
   google-chrome --headless=new --hide-scrollbars --screenshot=shot-1280.png --window-size=1280,800 http://localhost:3000/
   ```

   Add `--force-dark-mode` for a dark theme pass. A `file://` path works for a static page. Inside a container, Chrome may also need `--no-sandbox`.
3. Screenshots supplied by the user.

Capture at least a narrow phone width (360), the 390 × 844 mobile reference, a tablet width (768) and a laptop width (1280). Add the widest layout you support when the design is fluid.

**If nothing can render the page**, say so. Mark the result `NOT VISUALLY VERIFIED`, review the code against the checks below as far as reading allows, and list exactly what a person should look at. Never describe how a page looks when you have not seen it.

## 5. What to check in each screenshot

Look at each image as a first-time user would, then as a critic.

**First five seconds**

- What is this screen for? Can you tell without reading everything?
- What is the one thing to do next? Is it the most prominent control?
- Where does the eye land first? Is that the right place?

**Structure**

- Does spacing show what belongs together?
- Do left edges line up? Count the alignment lines.
- Is any text clipped, overlapping, orphaned, or wrapped one word per line?
- Is there horizontal scrolling at 360? There should be none, except inside a table or code block that scrolls on its own.
- Do tap targets look at least thumb-sized, with space between them?
- Does the layout at 1280 use the space well, or is it a phone layout stretched wide?

**Detail**

- Is body text comfortably readable? Is muted text still legible?
- Are there more than three rendered body text sizes (four for dense tools), more than two authored font families, any first-screen visible text below 13px, or competing accents? Use the browser probe and classify exceptions rather than counting CSS declarations.
- Do images load, with the right crop, and no distortion?
- Does anything look like a default you did not choose? See `visual-direction.md`.

For substantial visual work, also inspect the opening, every major scrolled section and the footer at true viewport height, at least on phone and desktop. A full-page capture helps compare rhythm but does not replace viewport captures. Check fixed header separation, image crops, text against imagery, layout at intermediate widths, and the usable static/reduced-motion state. Use the [visual craft rubric](visual-craft-engine.md#6-score-visual-craft-separately) only for rendered evidence; an unavailable screenshot is unverified.

Run the [Visual Integrity Gate](visual-integrity-gate.md) and its screenshot-first critic. Capture real scrolled viewport states, not just tall contact sheets. Record evidence IDs and issues before reading the design rationale. Run the read-only browser probe when possible. Write down what you see, not what you intended. Fix structural issues first and render again. For substantial work, save the gate report and run `node product-design-os/scripts/visual-gate.mjs report.json`. Validate evidence itself separately. After an authorized release, verify the final public revision rather than relying on a successful build.

## 6. Interaction checks

Screenshots miss behaviour. Where a browser can be driven, do these. Where it cannot, mark them unverified.

| Check | How | Pass |
| --- | --- | --- |
| Keyboard path | Tab from the top of the page through the main task. Use Enter, Space, Escape and arrow keys where expected | Every control is reachable, focus is always visible, order matches the layout, nothing traps focus |
| Zoom and reflow | Browser zoom to 200%, then set width to 320px | Content reflows to one column. Nothing is cut off. No two-direction scrolling |
| Text scaling | Increase default font size, or test with long strings | Containers grow. Text is not clipped |
| Touch | Narrow viewport with touch emulation | No action depends on hover. Targets do not overlap |
| Slow network | Throttle to slow 3G or delay responses | Feedback appears at once. Loading has a clear state. The page stays usable |
| Failure | Force a request error and a validation error | The message says what happened and what to do. Typed input is kept |
| Empty | Load with no data | The screen explains itself and offers the first action |
| Double action | Click the primary button twice quickly | One result, not two |
| Back and refresh | Mid-flow, go back, go forward, reload | State is kept or restored sensibly |
| Reduced motion | Emulate `prefers-reduced-motion: reduce` | Motion stops or becomes a simple fade. Nothing breaks |
| Dark mode | Only if the product supports it | Contrast holds. No invisible icons or borders |

## 7. Measure where it matters

- **Contrast:** measure real pairs with `ui-lint.mjs contrast`. Text needs 4.5:1, large text 3:1, control boundaries and focus indicators 3:1 (WCAG 2.2 AA).
- **Accessibility scan:** run axe, Lighthouse or the platform equivalent when available. Automated tools catch a minority of issues. A clean scan plus the keyboard pass is a reasonable floor, not a conformance claim.
- **Performance:** run Lighthouse or WebPageTest on a throttled mobile profile for pages that matter. Record the conditions. Lab numbers are not field numbers. Core Web Vitals "good" thresholds at the time of writing: LCP 2.5s or less, INP 200ms or less, CLS 0.1 or less, at the 75th percentile of real users. Confirm current values at web.dev when a decision depends on them.

## 8. Score, then decide

Score the result with `quality-rubric.md`. Any dimension below its floor goes back into the loop. Stop when the acceptance checks pass, every floor is met, and remaining changes are matters of taste.

Two or three passes is normal. If the fifth pass is still fixing layout, the structure is wrong: go back to the flow and hierarchy instead of polishing.

## 9. Report what was actually checked

Use plain evidence words.

| Word | Meaning |
| --- | --- |
| **Seen** | You looked at a rendering at a named width or state |
| **Operated** | You drove the interface and observed the result |
| **Measured** | A tool produced a number under stated conditions |
| **Read** | You inspected the code only |
| **Not verified** | Could not be checked here. Say why |

Example close:

```text
Seen: home and add-reading at 360, 768, 1280 (light). Operated: keyboard path, empty, error, double submit.
Measured: contrast for all text tokens (lowest 5.5:1). ui-lint: 0 errors, 1 warning (11px legal text, kept on purpose).
Not verified: screen reader announcement of the error summary, real-device performance.
Rubric: 33/40, no dimension below floor.
```

Never report a screen reader test, a user test, a device test or a performance figure that did not happen.
