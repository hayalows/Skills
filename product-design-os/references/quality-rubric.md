# Quality Rubric: Score the Work Before You Ship It

Use this reference to judge a design or a built screen, yours or someone else's. It turns "looks good" into ten scores with evidence.

Score what exists, not what was intended. Give each dimension a whole number from 0 to 4 and one line of evidence. If you could not check a dimension, write `not verified` and do not count it as a pass.

| Score | Meaning |
| --- | --- |
| 0 | Broken or absent. Blocks the task for some users |
| 1 | Present but causes real problems |
| 2 | Works, with visible rough edges |
| 3 | Solid. A careful reviewer finds only small issues |
| 4 | Excellent. Handles edge cases you had to go looking for |

## The ten dimensions

### 1. Task clarity (floor 3)

Can a first-time user say what the screen is for and what to do next?

- 0: purpose unclear, or several actions compete as primary
- 2: purpose is clear after reading. Primary action exists but does not stand out
- 4: purpose and next action are obvious in a glance at every width. Labels say exactly what happens

### 2. Flow and effort (floor 3)

Is the path to the outcome as short as it can safely be?

- 0: dead ends, loops, or required information the user cannot have yet
- 2: path completes, with steps or fields that could be removed, defaulted or deferred
- 4: every step and field earns its place. Sensible defaults. Progress survives interruption. Entry points and exits are deliberate

### 3. State coverage (floor 3)

Does the design handle what really happens?

- 0: only the happy path exists
- 2: loading and error exist but are generic, or empty and success states are missing
- 4: loading, empty, error, success, disabled, offline and no-permission are each designed where they can occur. Errors say what happened and what to do, and keep the user's input

### 4. Hierarchy and layout (floor 2)

Does the visual order match the importance order?

- 0: everything has the same weight, or alignment is accidental
- 2: clear title and primary action, with uneven spacing or several competing accents
- 4: one focal point per view. Spacing shows grouping. A few alignment edges. Still clear in greyscale

### 5. Typography and readability (floor 2)

- 0: text is too small, too long per line, or low contrast
- 2: readable, with too many sizes or weak distinction between levels
- 4: a small scale used consistently. Comfortable line length and line height. Numbers align. Long and translated strings fit

### 6. Visual identity and consistency (floor 2)

- 0: mixed styles, one-off colours and radii, looks assembled from unrelated parts
- 2: consistent but generic. Could be any product
- 4: a stated direction, expressed through tokens, with one memorable element and nothing decorative that lacks a reason. Same component looks and behaves the same everywhere

### 7. Responsiveness (floor 3)

- 0: breaks or scrolls sideways on a phone
- 2: works at phone and desktop, awkward between them or on very wide screens
- 4: designed from the narrowest width up. Reflows at 320px and at 200% zoom. Touch targets are comfortable. Nothing depends on hover

### 8. Accessibility (floor 3)

- 0: a keyboard or screen reader user cannot complete the task
- 2: mostly operable, with gaps such as weak focus, missing labels or colour-only meaning
- 4: full keyboard path with visible focus. Correct names, roles and states. Contrast measured. Motion respects user settings. Errors are announced and linked to fields

A score of 3 or more here needs evidence from an actual keyboard pass and measured contrast, not from reading the code alone.

### 9. Performance and resilience (floor 2)

- 0: slow to first content or blocks on failure
- 2: acceptable on a good connection. Heavy assets or layout shift on a slow one
- 4: immediate feedback for every action. Stable layout while loading. Light first load. Works through slow, failed and repeated requests. Measured on a throttled mobile profile

### 10. Trust and honesty (floor 3)

- 0: deceptive pattern present (fake urgency, hidden cost, forced continuity, confirm-shaming, obstructed exit), or invented proof
- 2: honest, with moments of doubt such as unclear totals, surprise steps or vague permissions
- 4: costs, consequences and data use are stated before commitment. Leaving is as easy as joining. Claims and proof are real. Destructive actions are reversible or clearly confirmed

## Reading the score

Add the ten scores for a total out of 40.

| Result | Meaning |
| --- | --- |
| Any dimension below its floor | Not ready. Fix that dimension first, whatever the total |
| 0 to 23 | Needs structural work. Go back to the flow and hierarchy |
| 24 to 29 | Usable. Ship only for internal or low-stakes use |
| 30 to 35 | Good. Ready for real users |
| 36 to 40 | Excellent. Check that the evidence supports each 4 |

The floors matter more than the total. A beautiful screen that fails keyboard use is not ready. A plain screen that passes every floor is.

## How to use it honestly

- Score before reading your own design notes. Notes describe intent.
- Give evidence a stranger could check: "360px screenshot shows the Pay button below the fold" is evidence. "Feels clean" is not.
- When unsure between two scores, give the lower one.
- A 4 requires that you went looking for an edge case and it held.
- Where possible, have the scoring done by a reviewer or agent that did not build the screen.
- The rubric measures craft. It does not prove that real users succeed. Only observation and data do that. See `research-validation.md`.

## Report format

```text
Rubric: 31/40. All floors met.
1 Task clarity 4      primary action is the only filled button at all three widths
2 Flow 3              four taps to add a reading. Date could default to today
3 States 3            empty, loading, error, success built. Offline not designed
4 Hierarchy 3         two alignment edges. Summary card competes slightly with the chart
5 Type 3              four sizes. Table numbers are tabular
6 Identity 3          direction "Meter" applied through tokens
7 Responsive 3        seen at 360, 768, 1280. 320 reflow operated
8 Accessibility 3     keyboard pass operated. Lowest text contrast 5.5:1. Screen reader not verified
9 Performance 2       not measured on a throttled profile
10 Trust 4            total shown before confirm. Undo on delete
Next: default the date, design the offline state, measure on slow 3G.
```
