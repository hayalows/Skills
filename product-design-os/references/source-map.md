# Source Map and Provenance

Built: 26 September 2026

Product Design OS is an original synthesis. It does not reproduce the supplied books. It converts their major principles into reusable decision rules, workflows, checklists, and examples, then updates areas where current standards are more specific or newer.

# Supplied Books

## Adrian Kuleszo, How to Design Better UI 3.0 (2024)

Primary contribution:
- Figma setup
- responsive framing
- layouts and grids
- box model
- spacing
- color
- shadows
- gradients
- UI terminology
- buttons
- forms
- pricing
- dropdowns
- navigation
- search
- modals
- hero sections
- cards
- style guides
- reusable components
- practice and good-vs-bad UI critique

How it is used here:
- `interface-craft.md`
- `component-patterns.md`
- `design-systems-handoff.md`
- `audit-checklist.md`

Important update:
The book includes practical target-size examples such as 44×44 and 48×48. This skill separates modern web conformance requirements from platform recommendations:
- WCAG 2.2 AA SC 2.5.8 defines a 24×24 CSS px minimum target size with specified exceptions.
- Android guidance recommends at least 48×48 dp.
Use the current standard/platform rule for the product being built.

## Jon Yablonski, Laws of UX (2020)

Primary contribution:
- Jakob's Law
- Fitts's Law
- Hick's Law
- Miller's Law
- Postel's Law
- Peak-End Rule
- Aesthetic-Usability Effect
- von Restorff Effect
- Tesler's Law
- Doherty Threshold
- ethics and responsibility
- applying psychological principles as team design principles

How it is used here:
- `foundations.md`
- `behavior-ethics.md`
- `audit-checklist.md`

Important interpretation:
The skill does not turn "7 ± 2" into a hard navigation rule. It uses Miller's Law mainly as a prompt to reduce memory burden and chunk information meaningfully.

The historical Doherty Threshold is used as a principle for fast feedback, while current web performance measurement uses Core Web Vitals.

## Nir Eyal with Ryan Hoover, Hooked: How to Build Habit-Forming Products (2014)

Primary contribution:
- habit zone
- external and internal triggers
- action
- variable rewards
- investment
- stored value
- loading future triggers
- habit testing
- manipulation/ethics questions

How it is used here:
- `behavior-ethics.md`
- `examples-recipes.md`

Important interpretation:
The Hook Model is not treated as a universal product recipe. It is loaded only when repeated use is genuinely part of the user's recurring goal.

Historical product examples and thresholds are not copied forward as universal benchmarks.

# Current External References

The following sources were used to update or strengthen the books with current standards and implementation guidance.

## W3C: WCAG 2.2

Main standard:
https://www.w3.org/TR/WCAG22/

Used for:
- contrast
- keyboard access
- focus
- target size
- error identification
- reflow/zoom
- accessible interaction

Target Size (Minimum), SC 2.5.8:
https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum

Focus Visible:
https://www.w3.org/WAI/WCAG22/Understanding/focus-visible

Focus Not Obscured (Minimum):
https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum

Non-text Contrast:
https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast

Error Identification:
https://www.w3.org/WAI/WCAG22/Understanding/error-identification

## W3C: WAI-ARIA Authoring Practices Guide

Pattern index:
https://www.w3.org/WAI/ARIA/apg/patterns/

Dialog modal pattern:
https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/

Combobox pattern:
https://www.w3.org/WAI/ARIA/apg/patterns/combobox/

Button pattern:
https://www.w3.org/WAI/ARIA/apg/patterns/button/

Used for:
- custom widget keyboard behavior
- dialog focus management
- accessible names/roles/states
- combobox interaction

## Android accessibility

Make apps more accessible:
https://developer.android.com/guide/topics/ui/accessibility/apps

Core app quality:
https://developer.android.com/docs/quality-guidelines/core-app-quality

Used for:
- 48×48 dp touch-target guidance
- content descriptions
- contrast and platform-quality expectations

## Apple Human Interface Guidelines

https://developer.apple.com/design/human-interface-guidelines/

Used as a current platform reference for:
- native iOS conventions
- typography
- controls
- accessibility
- layout and interaction

The skill avoids freezing volatile Apple measurements into the core rules when the current HIG should be consulted directly.

## Material Design 3

https://m3.material.io/

Used as a current Android/web component and visual-system reference.

The skill prefers current Material component guidance over old screenshots or historic values.

## Nielsen Norman Group

10 Usability Heuristics:
https://www.nngroup.com/articles/ten-usability-heuristics/

Progressive Disclosure:
https://www.nngroup.com/articles/progressive-disclosure/

Used for:
- heuristic evaluation
- system-status feedback
- consistency
- error prevention/recovery
- recognition over recall
- progressive disclosure

## GOV.UK Design System

Error message:
https://design-system.service.gov.uk/components/error-message/

Validation:
https://design-system.service.gov.uk/patterns/validation/

Error summary:
https://design-system.service.gov.uk/components/error-summary/

Used for:
- actionable error copy
- preserving user-entered form data
- validation timing and structure
- error-summary patterns

## web.dev

Web Vitals:
https://web.dev/articles/vitals

Interaction to Next Paint:
https://web.dev/articles/inp

Used for:
- current Core Web Vitals
- LCP, INP, CLS
- field-performance thinking
- responsiveness and feedback

Current "good" thresholds used in this skill:
- LCP ≤ 2.5 s
- INP ≤ 200 ms
- CLS ≤ 0.1

Evaluate at the 75th percentile in field data where possible.

# Conflict Resolution

When sources disagree, use this priority:

1. applicable law/regulation or explicit organizational requirement
2. current accessibility standard
3. current platform guidance
4. direct user research and product evidence
5. current technical reality
6. established design principles
7. examples from the supplied books
8. aesthetic convention

Numeric values from older books should not override newer standards.

# Evidence Discipline

Psychological laws and heuristics are used as:
- explanatory lenses
- design hypotheses
- critique language
- guardrails

They are not treated as proof that a specific design will work.

Important decisions should still be validated with:
- representative users
- behavior data
- accessibility testing
- performance data
- experiments when appropriate

# Copyright Note

The repository's MIT license applies to the original Product Design OS material written for this repository. It does not relicense the copyrighted source books, their illustrations, screenshots, or original text.

Do not copy book pages, diagrams, or long excerpts into derivative project documentation. Cite the original sources when using their named frameworks or specific claims.
