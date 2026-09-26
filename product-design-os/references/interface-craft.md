# Interface Craft: Layout, Spacing, Type, Color, Depth, Responsive Design

Use this reference when designing the visual and spatial system of a digital interface.

The goal is not decorative polish for its own sake. Visual decisions should make structure, priority, status, and action easier to perceive.

## 1. Work from content and constraints

Before choosing a grid, know:

- minimum supported viewport
- maximum useful reading/content width
- density of information
- longest realistic labels and values
- localization requirements
- input method
- expected zoom/text scaling
- persistent navigation
- device safe areas
- keyboard behavior on mobile
- whether the product is content-heavy, data-dense, or task-focused

A frame size is a working surface, not a product requirement.

## 2. Start small, then expand

A practical default for new responsive work is to begin with the smallest realistic viewport and make the core task work there first.

Why:

- narrow widths expose hierarchy problems early
- long labels reveal brittle components
- controls cannot hide inside unused space
- stacking behavior is clearer
- it is usually easier to add space than rescue a desktop-only composition later

For desktop, test beyond the base artboard. A design that only works at exactly 1440 px is not responsive.

## 3. Containers

Use containers to create predictable reading and interaction zones.

Specify:

- maximum content width where appropriate
- fluid width behavior
- minimum side padding
- alignment anchors
- nested container behavior
- full-bleed exceptions

Do not let every section invent a different left edge.

For large displays, letting text and controls stretch indefinitely can damage scanability. A max-width container often provides a better reading and comparison surface.

## 4. Grids

Use grids to align related things, not to force every object into equal rectangles.

Useful grid forms:

- column grid for page structure
- baseline/row rhythm for data-dense layouts
- local component grid for cards and dashboards
- 4-column mobile structure as a common starting point
- 12-column desktop structure as a common starting point

These are defaults, not mandatory counts.

Choose column count and gutter size based on the content relationships you need.

## 5. Soft and hard grids

A hard grid strictly constrains placement. A soft grid uses a spacing rhythm and shared alignment anchors without forcing every object onto a visible column.

Use hard grids when:

- dense dashboards need cross-row alignment
- multiple regions need stable column relationships
- data comparison benefits from repeated vertical anchors

Use soft grids when:

- editorial composition needs flexibility
- component content is variable
- auto layout/flex/grid can preserve rhythm without rigid tracks

## 6. Spacing system

Choose a small spacing vocabulary.

A useful starting scale:

`4, 8, 12, 16, 24, 32, 48, 64, 80`

Not every product needs every step.

Use spacing semantically:

- 4: tight internal relation
- 8: compact control relation
- 12/16: ordinary component padding/gap
- 24: separation between related groups
- 32+: separation between sections
- 48+: major structural separation

The semantic relation matters more than the number.

## 7. Proximity and hierarchy

Spacing communicates grouping.

If two things belong together, their internal gap should normally be smaller than the gap separating that group from the next group.

Use a simple test: blur or squint at the screen. The grouping should still be visible without reading the labels.

## 8. White space

White space is functional.

Use it to:

- separate tasks
- protect touch targets
- make hierarchy legible
- slow scanning where careful reading matters
- create visual rest around primary content

Do not add empty space simply to make a screen look luxurious when it pushes important content out of reach or harms data density.

## 9. Alignment

Repeated left edges, baselines, centers, and component widths create visual anchors.

Check:

- heading/body alignment
- input/label alignment
- card header alignment
- table column alignment
- icon/text baselines
- primary action alignment
- repeated component widths

Misalignment is especially visible in otherwise minimal interfaces.

## 10. Typography as hierarchy

Define roles, not random font sizes.

A practical semantic set might include:

- display
- page title
- section heading
- card heading
- body
- supporting body
- label
- metadata
- button
- caption

For each role specify:

- family
- weight
- size
- line height
- letter spacing if necessary
- responsive changes
- max line length when relevant

Use a type scale to make hierarchy predictable.

## 11. Readability

Prefer:

- comfortable body line-height
- readable line length
- sentence case for most labels
- sufficient size at real device distance
- meaningful headings
- strong text/background contrast

Avoid:

- tiny metadata used for important information
- all-caps paragraphs
- excessive weight changes
- low-opacity body text
- long centered paragraphs
- text embedded in images when live text can do the job

## 12. Responsive type

Do not scale every text role by the same percentage.

Large display headings may reduce substantially on narrow screens, while body text should remain comfortably readable.

Test:

- 200% zoom on web where applicable
- user text-size settings on mobile
- long translations
- bold accessibility text settings
- dynamic type behavior on iOS where supported

## 13. Color roles

Build semantic color roles rather than scattering hex values.

Typical roles:

- background
- surface
- elevated surface
- text primary
- text secondary
- border/subtle
- primary action
- primary action text
- secondary action
- focus
- selected
- info
- success
- warning
- danger
- destructive action
- overlay/scrim

A brand color is not automatically an accessible text or control color.

## 14. Tints and shades

Use a controlled tonal scale to create:

- state hierarchy
- surface layering
- subtle selected state
- badges
- borders
- charts
- light/dark themes

Do not improvise a new tint for each screen.

## 15. Color psychology

Color associations can be culturally dependent and context-dependent. Treat "blue means trust" or "red means urgency" as weak heuristics, not universal psychology.

Use color primarily for:

- role
- state
- hierarchy
- brand
- grouping

Test meaning with the actual audience where color carries high-stakes interpretation.

## 16. Grayscale test

Temporarily inspect the interface without hue.

Ask:

- can I still see the primary action?
- can I distinguish headings from body text?
- can I identify selected and disabled states?
- does the page still have a readable hierarchy?

A grayscale pass is a hierarchy check, not an accessibility test.

## 17. Contrast

For exact accessibility requirements, use `accessibility.md`.

Design principle:

- important text should never depend on delicate low-opacity treatments
- controls need visible boundaries or another reliable affordance
- selected, focused, and error states must remain identifiable
- dark mode requires the same seriousness as light mode

Decorative subtlety should not reduce legibility.

## 18. Elevation and shadows

Shadows should communicate layering, not simply make elements look "premium."

Use elevation for:

- floating navigation
- popovers
- dialogs
- cards that genuinely sit above a surface
- dragged items

Keep the implied light direction consistent.

Often a subtle border plus a restrained shadow is more stable than a large diffuse shadow.

## 19. Dark surfaces

Shadows are less visible on dark surfaces. Use:

- tonal elevation
- border/highlight
- subtle surface change
- controlled glow only when appropriate

Do not compensate with excessive neon effects unless the product language genuinely calls for them.

## 20. Gradients

Use gradients for a reason:

- brand expression
- depth
- focus
- large background treatment
- data visualization when perceptually appropriate

Avoid gradients that:

- reduce text contrast
- make buttons look unlike buttons
- introduce many unrelated hues
- imitate trendy references without fitting the product

Adjacent or harmonized hues generally produce calmer transitions than arbitrary color jumps.

## 21. Imagery

Define:

- crop behavior
- aspect ratios
- fallback
- loading treatment
- alt-text expectation
- subject-safe area
- consistency across cards

A card grid becomes visually unstable when every image has a different composition and ratio.

## 22. Iconography

Icons should share:

- stroke/fill logic
- optical size
- corner language
- visual weight
- bounding box
- metaphor vocabulary

Use icons alone only when the meaning is widely understood or when a visible/accessibility label is available.

Do not use decorative icons to add noise between every line of text.

## 23. Cards

Cards are useful when content units are independently scannable or actionable.

A good card answers:

- what is this?
- why does it matter?
- what status is it in?
- what can I do?

Typical anatomy:

- media/icon
- eyebrow/status
- title
- supporting content
- metadata
- action

Keep repeated card structures consistent. Variable content may change height, but the hierarchy should not change randomly.

Avoid cards for every section simply because they are easy to draw. Too many containers can fragment the page.

## 24. Hero sections

A landing-page hero should usually communicate:

- what the product/service is
- who it serves
- the meaningful outcome
- credibility or supporting proof
- the primary action

Use one primary CTA. A secondary CTA may exist, but should not visually compete equally.

Left alignment often supports longer reading. Center alignment works best with concise copy and a strong visual composition.

The first viewport should suggest that more content exists below without making users guess.

## 25. Data-dense dashboards

For dashboards, optimize for decision-making, not decoration.

Start with:

- what question does the user need answered?
- what action follows the answer?
- what time range matters?
- what comparison matters?
- what is abnormal?
- what needs attention now?

Then design:

- summary
- trend
- breakdown
- exceptions
- drill-down
- action

Avoid decorative chart density.

## 26. Tables

Tables are for comparison across attributes.

Use:

- clear headers
- consistent numeric alignment
- meaningful default sorting
- visible sort state
- sticky headers when long
- row actions that remain discoverable
- responsive alternatives for narrow screens
- empty and loading states
- column customization only where useful

Do not collapse a complex table into horizontally scrolling mystery content without preserving context.

## 27. Motion

Motion should explain:

- cause and effect
- spatial relationship
- state transition
- progress

It should not delay task completion.

Specify reduced-motion behavior. Never require animation to understand the state.

## 28. Responsive transformation patterns

Common transformations:

### Multi-column → stacked
Use when side-by-side relationships are not essential.

### Sidebar → drawer or bottom sheet
Use when navigation must remain available but screen width is constrained.

### Toolbar → prioritized actions + overflow
Keep the most frequent actions visible.

### Table → cards or horizontally scrollable table
Choose based on whether cross-row comparison remains important.

### Split view → drill-in navigation
Use on small screens when simultaneous context is less important than readability.

### Hover affordance → explicit touch affordance
Never make a touch user depend on hover.

## 29. Low-bandwidth design

Visual design must consider network reality.

Prefer:

- compressed responsive images
- lazy loading below the fold
- stable image dimensions to prevent layout shift
- lightweight icon systems
- content before decorative media
- useful skeletons only when they reduce uncertainty
- cached or locally retained task state where practical

A beautiful interface that routinely arrives late or incomplete is a poor interface.

## 30. Visual critique checklist

Before handoff ask:

- Is the primary purpose visible without reading every word?
- Is the primary action obvious?
- Does spacing reflect grouping?
- Are there stable alignment anchors?
- Does typography have a consistent scale?
- Are color roles semantic and reusable?
- Does the design survive grayscale?
- Are surfaces and elevation purposeful?
- Are interactive controls visibly interactive?
- Does the smallest supported viewport work?
- Does the widest supported viewport remain coherent?
- Do long labels and real data fit?
- Does zoom/text scaling break layout?
- Are decorative effects compromising performance or contrast?
