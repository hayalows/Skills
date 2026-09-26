# Accessibility and Inclusive Interaction

Use this reference for every digital product. Accessibility is a design input, not a final compliance pass.

For web work, use WCAG 2.2 AA as the default target unless another requirement is specified.

## 1. Standards hierarchy

Use:

- WCAG 2.2 for web success criteria
- semantic HTML first
- WAI-ARIA Authoring Practices Guide for custom widget interaction patterns
- platform guidance for native iOS/Android behavior
- assistive-technology testing for real-world validation

ARIA does not repair fundamentally wrong interaction design. Prefer native semantics when they fit.

## 2. Target size

### Web
WCAG 2.2 Success Criterion 2.5.8 sets a minimum pointer-target size of 24 by 24 CSS pixels, with defined exceptions including sufficient spacing.

Treat this as a compliance floor, not an ideal target.

### Android
Android guidance recommends at least 48 by 48 dp for touch targets.

### Practical design default
For primary touch interfaces, use comfortably large targets. A visible icon may be 20–24 units while its interactive hit area is substantially larger.

Do not place small destructive and safe actions tightly together.

## 3. Text contrast

For WCAG AA:

- normal text: at least 4.5:1
- large text: at least 3:1

Do not lower body text opacity until it becomes barely legible.

Check:

- default
- hover
- selected
- disabled where meaningful
- dark theme
- text over images
- text inside gradients

## 4. Non-text contrast

Meaningful component boundaries, states, focus cues, and graphical objects generally need 3:1 contrast against adjacent colors under WCAG 2.2 SC 1.4.11 when the visual information is needed to identify or understand them.

Examples:

- input boundary
- selected checkmark
- focus indicator
- chart line required for interpretation

## 5. Do not rely on color alone

Pair color with one or more of:

- text
- icon
- shape
- border
- pattern
- position

Examples:

Bad:
- red field border only

Better:
- red border + error icon + text describing the issue

## 6. Keyboard operability

All interactive web functionality should work without a mouse where the platform supports keyboard use.

Test:

- Tab
- Shift+Tab
- Enter
- Space
- Arrow keys where the widget pattern requires them
- Escape
- Home/End where appropriate

Do not create click-only custom divs.

## 7. Focus visible

WCAG 2.2 AA requires a visible keyboard focus indicator.

Do not remove outlines without a replacement.

A strong practical pattern:

- 2px or thicker visible ring/outline
- strong contrast against surrounding colors
- offset when needed to separate it from the component

WCAG 2.2 Focus Appearance at AAA provides more demanding size/contrast guidance, but a clearly visible focus treatment is good design even when AAA is not required.

## 8. Focus not obscured

Sticky headers, footers, cookie banners, bottom bars, and overlays should not completely hide the currently focused control.

Test tabbing through pages with sticky UI.

Use scroll padding or layout adjustments when necessary.

## 9. Focus order

Keyboard focus should follow the meaningful reading/action order.

Do not:

- visually reorder content with CSS while DOM focus follows a confusing sequence
- send focus behind an open modal
- unexpectedly reset focus to the top of the page
- move focus on every small dynamic update

## 10. Dialog focus

For a modal dialog:

- move focus inside on open
- keep Tab and Shift+Tab inside the dialog
- provide a visible close/cancel control where appropriate
- support Escape unless the task explicitly requires otherwise
- return focus to the invoking control or a logical successor after close
- make background content inert for all users, not only visually dimmed

Use the WAI-ARIA APG dialog pattern for implementation guidance.

## 11. Accessible names

Every interactive control needs an accessible name.

Use:

- visible text label where possible
- associated `label` for form fields
- `aria-label` or `aria-labelledby` only when necessary
- descriptive `contentDescription` on Android for non-text controls

An icon named "arrow-left" describes appearance, not purpose. Prefer "Back" when that is the action.

## 12. Name, role, state, value

Assistive technologies need to know:

- what the control is
- what it is called
- its current state
- its current value where relevant

This is why native controls are valuable.

Custom controls must reproduce the expected semantics and keyboard model.

## 13. Forms

Each field should have:

- visible label
- programmatic label relationship
- hint only when needed
- correct input type/autocomplete purpose where possible
- required/optional state
- error relationship
- preserved value on error

Group related radio/checkbox controls semantically.

## 14. Errors

WCAG requires automatically detected input errors to be identified and described in text.

Good error message:

- identifies the affected field
- describes what is wrong
- gives a useful correction
- uses ordinary language

Bad:
"Invalid input."

Better:
"Enter a date before 26 September 2026."

Do not clear other correct or incorrect answers after validation failure.

For long forms, an error summary that links to each field can significantly improve recovery.

## 15. Live updates

Dynamic status changes may need a live region.

Examples:

- upload complete
- search result count updated
- item added to cart
- async validation result

Do not announce every visual micro-update. Excess announcements can make a screen reader experience unusable.

## 16. Images

### Informative
Provide concise alt text that communicates purpose or equivalent information.

### Decorative
Use empty alt text / appropriate decorative semantics so it is skipped.

### Complex charts
Provide the important takeaway in text and, where necessary, accessible data.

### Functional image
The accessible name should describe the action, not the pixels.

## 17. Icons

Do not assume an icon is universally understood.

If meaning is not obvious:

- add visible label
- add tooltip for pointer users where useful
- provide accessible name regardless

Avoid using multiple slightly different icons for the same action.

## 18. Motion

Support `prefers-reduced-motion` on web and equivalent platform settings.

Reduce or remove:

- large parallax
- rapid zooming
- auto-rotating content
- nonessential looping motion
- large spatial transitions

Do not remove state change itself. Replace motion with a lower-motion cue.

## 19. Autoplay

Avoid autoplay with sound.

For moving content:

- provide pause/stop controls when required
- respect reduced motion
- avoid content that moves before users can orient themselves

## 20. Touch, pointer, keyboard, voice

Do not design for a single input mode.

Check:

- touch target size
- pointer hover
- keyboard focus
- screen reader labels
- voice-access names
- switch control traversal

Visible labels help voice users say what they see.

## 21. Zoom and reflow

Test web interfaces at high zoom.

Watch for:

- clipped dialogs
- hidden buttons
- overlapping text
- two-axis page scrolling
- fixed headers covering content
- off-screen form errors

Responsive design must include zoomed desktop, not only small mobile devices.

## 22. Text resizing

Do not put text into fixed-height containers that clip when text grows.

Buttons, chips, inputs, cards, and tabs need resilient vertical sizing.

## 23. Localization

Accessibility and localization overlap.

Plan for:

- longer labels
- right-to-left layout where relevant
- different date/number formats
- diacritics
- line wrapping
- pluralization

Do not create critical controls whose meaning depends on a short English word fitting in one line.

## 24. Cognitive accessibility

Improve comprehension through:

- clear headings
- plain language
- consistent terminology
- predictable interaction
- recognition rather than recall
- visible progress
- short chunks
- examples when format is unfamiliar
- prevention of time pressure where possible

Avoid clever microcopy in high-stakes errors.

## 25. Accessible authentication

Do not make authentication depend on:

- memorizing arbitrary characters without password-manager support
- a puzzle with no accessible alternative
- a single unavailable sensory channel

Support copy/paste and password managers unless a very strong security requirement says otherwise.

## 26. Status and timeouts

If a session expires:

- warn users where practical
- preserve work when safe
- explain what happened
- offer re-authentication
- return them to the task

For time-limited flows, provide extension where applicable and allowed.

## 27. Data visualization

Do not depend only on hue.

Use:

- labels
- direct annotation
- patterns
- line styles
- shapes
- text summaries

Charts should have an accessible data representation when the data itself matters.

## 28. Mobile accessibility

Test:

- large system text
- screen reader
- one-handed reach
- orientation changes if supported
- dark/light theme
- reduced motion
- keyboard visibility
- dynamic viewport changes

Do not place primary actions beneath the on-screen keyboard.

## 29. Custom widgets

Before building one, ask whether a native element already solves the task.

If custom is necessary:

- follow an established APG/platform pattern
- implement keyboard interaction
- expose name/role/state/value
- test screen reader behavior
- test touch
- test high contrast
- test zoom/text scaling

"No ARIA is better than bad ARIA" is a useful implementation principle.

## 30. Accessibility QA sequence

### Pass 1: automated
Use linting, axe/Lighthouse, contrast checks, semantic validation.

### Pass 2: keyboard
Complete the primary tasks without mouse/touch.

### Pass 3: zoom/text
Test 200% zoom and large text.

### Pass 4: screen reader
Test meaningful flows with VoiceOver, TalkBack, NVDA, or JAWS as appropriate.

### Pass 5: motion/color
Check reduced motion and non-color cues.

### Pass 6: real users
For high-impact products, include people with disabilities in research.

Automated checks cannot prove accessibility.

## 31. Accessibility acceptance template

```text
Semantic element/role:
Accessible name:
Keyboard interaction:
Focus entry:
Focus exit:
Focus indicator:
Target size:
Text contrast:
Non-text contrast:
Screen reader announcement:
Error announcement:
Zoom/reflow:
Large text:
Reduced motion:
Touch:
Pointer:
Known exception:
Validation method:
```
