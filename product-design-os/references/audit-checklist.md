# Product Design Audit and Pre-Launch Checklist

Use this file for a structured audit of an existing product, prototype, design file, or implementation.

Do not turn the checklist into a box-ticking exercise. Findings should be tied to evidence and the user's task.

# 1. Audit Setup

Capture:

- product/surface
- platform
- user or role
- primary task
- entry point
- end state
- environment/device
- account state
- network state if relevant
- evidence source
- date/version
- known constraints

For a live product, audit the real flow when access is available. A marketing screenshot cannot support claims about keyboard behavior, loading, or validation.

# 2. Task and Outcome

- Is the user's main goal explicit?
- Is the shortest safe path obvious?
- Does the flow end in a clear success state?
- Are non-happy paths represented?
- Does the product ask the user to do work the system could safely do?
- Are high-risk actions given appropriate review/friction?
- Are business goals visibly in conflict with user goals?

# 3. Information Architecture

- Do labels use user language?
- Are related items grouped?
- Does global navigation match top-level tasks?
- Is active location visible?
- Can users find important destinations without memorizing paths?
- Are advanced controls progressively disclosed?
- Is search available where browsing becomes inefficient?
- Does mobile navigation preserve core access?
- Are breadcrumbs useful in deep hierarchies?

# 4. Cognitive Load and Psychology

## Jakob
- Does the design follow familiar conventions for familiar tasks?
- Are departures from convention intentional and tested?

## Fitts
- Are important targets easy to acquire?
- Are frequent actions reachable?
- Are dangerous actions separated?

## Hick
- Are users facing unnecessary choices?
- Are options grouped and sequenced?
- Are safe defaults/recommendations available where useful?

## Chunking
- Is information grouped by meaning?
- Must the user remember values from another screen?
- Is comparison possible without mental juggling?

## Postel
- Does the system tolerate harmless formatting variation?
- Does validation preserve input?
- Is ambiguous input handled safely?

## Peak-End
- Are high-stakes moments handled carefully?
- Does the ending confirm what happened and what comes next?

## Aesthetic-Usability
- Is visual polish masking a broken task?
- Does styling support hierarchy and trust?

## von Restorff
- Is visual emphasis reserved for what matters?

## Tesler
- Is complexity placed appropriately between user and system?

## Feedback
- Does every meaningful action receive immediate acknowledgement?

# 5. Visual Hierarchy

- Does each screen have one clear purpose?
- Is the primary action visually clear?
- Are secondary actions subordinate?
- Are destructive actions distinct without dominating ordinary use?
- Do spacing relationships show grouping?
- Are there stable alignment anchors?
- Is typography hierarchical and consistent?
- Is body text comfortably readable?
- Is important text hidden in low-contrast styling?
- Does the interface remain understandable in grayscale?
- Are cards/containers helping grouping rather than fragmenting everything?
- Are shadows/elevation communicating layering?

# 6. Responsive Design

Test at:

- smallest supported viewport
- typical mobile
- tablet if supported
- typical desktop
- wide desktop
- browser zoom/high text size

Check:

- no clipped primary controls
- no horizontal page scrolling unless task-specific
- navigation transformation
- long labels
- real data
- modal fit
- tables
- sticky elements
- keyboard overlay on mobile
- safe areas
- image crop
- overflow menus
- reflow

# 7. Buttons and Actions

- action label describes outcome
- link vs button semantics correct
- default/hover/focus/pressed/disabled/loading defined
- target size adequate
- icon-only control has accessible name
- duplicate submission prevented
- disabled state explained where needed
- loading preserves context
- destructive action names consequence

# 8. Forms

- only necessary fields
- visible labels
- correct input type
- instructions near field
- required/optional convention consistent
- autofill/autocomplete supported where useful
- grouping is meaningful
- long forms have sensible stages
- progress visible where useful
- back preserves data
- validation identifies problem and correction
- input retained after error
- errors not color-only
- error summary for long forms where useful
- success confirms outcome

# 9. Search

- search easy to find if core task
- suggestions helpful
- recent searches useful, not creepy
- typo tolerance
- loading
- preserved query
- active filters visible
- clear filter
- sort state
- no-result recovery
- keyboard behavior
- accessible custom combobox behavior
- useful result metadata

# 10. Navigation

- current location visible
- top-level destinations stable
- tabs used for peer views, not linear steps
- back behavior predictable
- mobile nav not hiding primary tasks
- overflow contains infrequent items, not essential work
- deep hierarchy has context
- browser history works sensibly on web

# 11. Dialogs and Overlays

- dialog is necessary
- title explains task
- actions explicit
- close/cancel route
- no nested modals
- focus moved inside
- Tab stays inside modal
- Escape behavior correct
- background inert
- focus returns logically
- modal fits small/zoomed viewport

# 12. Tables and Dashboards

- visualizations answer a decision question
- key metric definitions available
- freshness/source visible where needed
- table headers clear
- numeric alignment supports comparison
- sorting/filtering meaningful
- selected sort visible
- bulk actions explicit
- empty/loading states
- responsive strategy
- charts have text equivalents
- color is not sole data distinction

# 13. Empty, Loading, Error, Success

For every important screen ask whether these states exist.

## Empty
- why empty
- expected or error
- next action

## Loading
- immediate acknowledgement
- appropriate indicator
- stable layout
- no duplicate action

## Error
- what happened
- what is preserved
- how to fix/retry
- whether retry is safe

## Success
- what completed
- receipt/reference if relevant
- next step
- recovery/support route

# 14. Accessibility

## Semantics
- correct native element/role
- accessible names
- headings meaningful
- landmark structure sensible

## Keyboard
- full primary task without pointer
- logical focus order
- visible focus
- no keyboard trap outside intentional modal behavior
- sticky UI does not obscure focus

## Contrast
- normal text ≥ 4.5:1 for WCAG AA
- large text ≥ 3:1
- meaningful non-text UI contrast ≥ 3:1 where WCAG applies

## Target
- WCAG 2.2 AA target-size minimum considered
- larger practical touch targets used where possible
- Android 48dp guidance when native Android applies

## Forms
- label relationship
- error relationship
- programmatic state
- instructions

## Zoom/text
- 200% zoom
- large platform text
- no clipping

## Motion
- reduced-motion path
- no essential information only in animation

## Images/charts
- alt/equivalent
- decorative images skipped
- charts have accessible summary/data

## Screen reader
- important dynamic changes announced
- control names make sense
- selected/expanded/error state available

# 15. Performance and Reliability

Check realistic conditions:

- cold load
- slow network
- interaction responsiveness
- layout shifts
- images
- third-party scripts
- repeated requests
- timeout
- partial failure
- offline/intermittent network
- cached/stale data
- duplicate action
- background job
- expired auth

For web, measure Core Web Vitals in field data where possible:
- LCP
- INP
- CLS

Do not infer performance from a static mockup.

# 16. Permissions and Roles

- correct controls for each role
- unauthorized action blocked by backend, not only hidden
- permission request occurs in context
- denied path designed
- read-only states clear
- elevation/escalation explicit
- account/role switch visible if relevant

# 17. Privacy and Trust

- data collection proportionate
- purpose clear
- consent meaningful
- sensitive information not overexposed
- defaults reasonable
- delete/export controls available where appropriate
- session/device security clear
- no surprise sharing

# 18. Behavior and Ethics

Run this when the product uses engagement mechanics.

- recurring user problem exists
- trigger serves user
- notifications controllable
- no repeated pestering
- variable reward tied to useful value
- investment improves future experience
- no artificial switching cost
- stopping cues exist
- streaks recoverable
- no fake scarcity
- no fake social proof
- no preselected paid extras
- no disguised ads
- signup/cancel effort reasonably symmetric
- no hidden recurring consequences
- user outcome metric paired with engagement metric
- vulnerable-use scenario reviewed

# 19. Content

- labels concrete
- jargon minimized
- status language specific
- error messages actionable
- date/time/currency unambiguous
- destructive copy states consequence
- pricing terms explicit
- no manipulative shame copy
- localization length considered
- consistent terminology

# 20. Design System

- semantic tokens used
- spacing scale
- typography roles
- color roles
- component variants
- complete states
- no duplicate near-identical components
- responsive behavior documented
- accessibility documented
- code/design parity
- deprecated patterns marked
- component names meaningful

# 21. Handoff

- purpose clear
- component references
- responsive behavior
- state matrix
- keyboard/focus
- API/data assumptions
- permissions
- analytics
- performance expectations
- acceptance criteria
- known open questions

# 22. Research and Measurement

- riskiest assumptions identified
- right research method chosen
- tasks tested, not preferences
- analytics map to product questions
- causal claims not made from correlation
- support/search evidence reviewed
- post-launch review planned

# 23. Severity Model

## Critical
Blocks an essential/high-stakes task, causes severe data/financial/security/privacy harm, or excludes a significant user group from required functionality.

## High
Major failure or repeated severe friction in an important task with poor recovery.

## Medium
Meaningful confusion, extra work, or error risk, but most users can recover.

## Low
Minor inconsistency or polish issue with small task impact.

Severity should consider:
- impact
- frequency
- breadth
- recoverability
- accessibility exclusion
- consequence

Do not raise severity merely because an issue is visually noticeable.

# 24. Finding Template

```text
ID:
Location:
Task:
Evidence:
Observed behavior:
User consequence:
Relevant principle/standard:
Severity:
Confidence:
Recommendation:
Validation:
Implementation note:
```

# 25. Final Audit Structure

A useful report contains:

1. executive read
2. flow/screen inventory
3. highest-impact findings
4. findings by step
5. accessibility risks
6. performance/reliability risks
7. ethical/behavior risks where applicable
8. design-system inconsistencies
9. quick fixes
10. structural fixes
11. validation plan
12. evidence limits

# 26. Pre-Launch Gate

Do not call the product ready until:

- primary task works
- important edge states exist
- critical/high findings addressed or accepted explicitly
- keyboard path tested
- focus visible
- contrast checked
- touch targets checked
- zoom/text scaling checked
- screen-reader smoke test performed where relevant
- destructive actions safe
- no deceptive patterns
- slow-network state tested
- duplicate action tested
- analytics events checked
- acceptance criteria passed
- design/code differences reconciled or documented
