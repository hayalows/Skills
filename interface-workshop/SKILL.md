---
name: interface-workshop
description: "Design, implement, critique or teach responsive UI and UX in a real frontend. Use for visual hierarchy, mobile interactions, design-to-code, awkward flows, or practising design judgment on a screen."
routing:
  roles: [lead, supporting]
  category: interface-design
  exclusive_role: ui-lead
---

# Interface Workshop

Start with the screen the person actually reaches. Name who arrives, what they already know, what they need to decide and what completion looks like. Trace one action from entry to outcome. Use real copy or clearly labelled sample data. Match the depth to the request.

## Choose the activity

- **Repair.** Inspect the reported state and its nearest neighbour. Keep the brand, navigation and working behavior the user wants to preserve. Make the smallest coherent change and replay the interaction.
- **Build.** Deliver the working flow in the existing stack. For a new product, make one representative screen and its consequential states work before extending its patterns.
- **Critique.** Show where the user encounters friction, what you observed, who it affects and the smallest repair worth testing. Prioritize a blocked task over a cosmetic preference. Respect review-only scope.
- **Practise.** Give the learner a concrete decision on their own screen. Ask them to predict the effect of two plausible options. Let them make a change, compare results against a stated criterion, then give one specific correction. In a single-turn lesson, include a worked example and a fresh exercise with a way to check it.

## Compose around the decision

Read the surrounding screens, type styles, assets and reusable controls. Identify one visual element that makes this product recognizable. For an open brief compare two compositions using the same content. Change one consequential choice, such as a results list beside a map versus an overlay. Say what each makes easier and which user pays the cost. Skip variants when matching a supplied design.

Write the actual heading, primary action and most difficult content before sizing the layout. Set reading order and align elements that belong together. Use spacing to group a price with its unit or a field with its error. Reserve prominent type and colour for information that changes a decision. If every section needs a card or a badge to read clearly, revisit the grouping. Choose photography, illustration or motion for a specific job. Check the initial view with optional media missing.

## Build the interaction

Use semantic HTML and existing tokens. Choose breakpoints where the content stops fitting. Keep DOM and visual order compatible when columns collapse. Give controls accessible names, keyboard behavior and visible focus. Check sticky elements, the software keyboard, safe-area space and long text where they affect the action. Use a native control unless a custom one buys a concrete behavior.

Trace the action while waiting, on success, on error, and on return. Preserve recoverable input. Distinguish an empty result from an unavailable service. If a server owns status, agree on the signals that justify each message. A pending transaction needs a way to check its status. For cross-layer work, hand engineering the action, state source, expected transition and one observable acceptance test.

## Look, operate, revise

Run the normal entry point. Inspect the default view on a narrow phone and a wide display, then at the width where the layout changes. Operate the main flow using touch or pointer and keyboard. Inspect the most costly failure state with representative data. Test larger text and reduced motion when relevant. Compare before and after at the same size. Fix the largest issue and repeat that observation. Mention the route, state, viewport and outcome for material claims. If only source or a screenshot is available, label interaction findings as hypotheses.

Use [Workshop exercises and field notes](references/field-notes.md) for a worked critique, practice task, and sources. End a build with what works and what still needs a real device or person. Give a lesson only when the user wants to learn.
