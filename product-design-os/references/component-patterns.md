# Component and Interaction Patterns

Use this reference when specifying common interface components. Treat each component as a state machine with behavior, content, accessibility, and recovery rules.

## 1. Buttons

### Purpose
Buttons trigger actions. Links navigate to resources or locations. Do not style one as the other without preserving correct semantics.

### Hierarchy
A typical hierarchy:

- primary: strongest action on the current surface
- secondary: valid alternative
- tertiary/text: low-emphasis action
- destructive: action with harmful or irreversible consequence

Avoid multiple equally loud primary buttons in one decision region.

### Labels
Prefer action + object when helpful:

- Save changes
- Send invitation
- Download CSV
- Delete account

Avoid vague labels such as:

- Click here
- Yes
- Submit

unless context makes the outcome completely unambiguous.

### States
Define:

- default
- hover where pointer exists
- focus
- pressed
- loading
- disabled
- success if the component carries transient success
- destructive confirmation path where needed

### Loading
When button action starts:

- acknowledge immediately
- prevent accidental duplicate submission
- keep the label informative
- do not replace a useful label with an unexplained spinner if it removes context

### Disabled
Use disabled states sparingly.

If users may reasonably wonder why the action is unavailable, explain what is missing rather than presenting a dead control.

### Icon buttons
Use only when the icon is familiar or has an accessible label/tooltip.

The interactive target may be larger than the visible glyph.

## 2. Forms

### Minimize fields
Every field has a cost. Ask only for data needed now.

Defer information that:

- can be inferred
- can be collected later
- is optional for task completion
- is already known

### Labels
Use persistent visible labels. Placeholder text is supplementary guidance, not a label replacement.

### Instructions
Place instructions near the field they affect.

Do not make users memorize format rules from an earlier screen.

### Input type
Match the control to the data:

- text input for free text
- textarea for longer text
- radio group for a small mutually exclusive set
- checkbox for independent/multiple selection
- native select for a manageable known option list
- combobox/searchable select for long searchable lists
- date controls based on date task, not visual fashion
- numeric controls only when numeric semantics are real

### Required/optional
Choose one convention and use it consistently. If most fields are required, marking optional fields can reduce clutter. If many are optional, mark required fields clearly.

### Width
Field width can hint at expected content length, but never at the expense of responsive layout.

### Grouping
Group related inputs under meaningful headings. Use fieldsets/legends on web for semantic groups such as radio and checkbox questions.

### Long forms
Break long forms when stages are meaningful, not simply every few fields.

Preserve:

- progress
- entered data
- back navigation
- review before high-impact submission

### Validation
Prevent errors when possible.

When an error occurs:

- identify the field
- say what is wrong
- say how to fix it
- preserve the user's input
- do not rely on red color alone
- move focus appropriately after failed submission in longer forms

Avoid validating while a user is still typing unless immediate feedback is genuinely useful and non-disruptive.

### Confirmation
After submission, confirm:

- what happened
- reference/receipt if relevant
- next step
- expected timing
- recovery/contact path

## 3. Search

Search is a task system, not only an input field.

Define:

- empty query behavior
- recent searches if useful
- suggestions/autocomplete
- typo tolerance
- loading
- results count
- filters
- sort
- pagination or infinite loading
- no results
- partial failure
- clear query
- back behavior
- preserved filters
- keyboard behavior

### No results
Do not stop at "No results."

Offer contextually useful recovery:

- check spelling
- remove filters
- broaden query
- browse categories
- contact support
- request/add missing item where appropriate

### Search-heavy products
If search is the dominant user path, give it visual priority and persistent access.

## 4. Dropdowns, selects, comboboxes

Choose based on task.

### Native select
Good for:
- predictable, moderate option set
- simple single selection
- mobile platform conventions

### Radio group
Good for:
- small option set
- comparison matters
- all options should remain visible

### Combobox
Good for:
- long searchable list
- typed filtering
- suggestion list
- selection plus editable text depending on product

### Multi-select
Provide:

- visible selected values
- remove individual selection
- clear all when useful
- search for long lists
- selection count for large sets

Keyboard and screen-reader behavior for a custom combobox is non-trivial. Prefer established accessible components.

## 5. Navigation

Navigation should reflect the user's model of the product, not the internal team structure.

### Global navigation
Use for high-level destinations.

### Local navigation
Use for subsections within a product area.

### Tabs
Use when views are peers within the same context and users may switch frequently.

Do not use tabs for a sequential multi-step process.

### Breadcrumbs
Use in deep hierarchies where users benefit from location context and parent navigation.

### Bottom navigation
Useful on mobile for a small number of frequent top-level destinations.

### Sidebar
Useful for desktop applications with persistent multi-section navigation.

### Overflow
Move infrequent actions into overflow, but keep the primary tasks visible.

### Active state
Always show where the user is.

## 6. Menus

Menus expose actions, not arbitrary content dumps.

Specify:

- trigger label/icon
- open direction
- focus behavior
- selected/checked states
- keyboard navigation
- closing behavior
- destructive action styling
- submenus only when necessary

Avoid deep cascading menus on touch devices.

## 7. Dialogs and modals

Use a modal when the current task genuinely needs a bounded interruption or focused decision.

Good uses:

- confirm high-impact action
- short creation/edit task related to the current context
- select from a constrained auxiliary surface
- display critical information requiring acknowledgement

Avoid modal use for:

- long reading
- complex multi-page work
- routine success messages
- content that could live inline
- nested dialogs

### Anatomy
A dialog should have:

- clear title
- concise body/context
- explicit actions
- close/cancel route where appropriate

### Focus
On web:

- move focus inside when opened
- trap tab sequence inside while modal is active
- support Escape where appropriate
- return focus to the logical trigger or next context on close
- prevent background interaction

### Destructive confirmation
Use action-specific labels:

- Delete project
- Remove member
- Cancel subscription

Avoid "Yes / No" when the action can be named.

## 8. Toasts and snackbars

Use for brief non-blocking feedback.

Good for:

- item saved
- copied to clipboard
- action completed
- undo opportunity

Not good for:

- critical errors
- information that users must remember
- long instructions
- legal/consent information

Do not disappear so quickly that users cannot perceive the message. Do not make a toast the only place a critical error is explained.

## 9. Alerts and banners

Use persistent inline banners for system-level or section-level conditions:

- outage
- account restriction
- incomplete setup
- security issue
- deadline

State:

- what happened
- affected scope
- what the user can do
- whether the condition is temporary
- how to dismiss, if dismissal makes sense

## 10. Accordions / disclosure

Use to hide secondary detail while preserving an overview.

Good for:

- FAQs
- advanced configuration
- dense reference material

Avoid when:

- users need to compare all sections simultaneously
- hidden content is required to complete the task
- the page becomes a stack of collapsed mystery labels

## 11. Cards

Use cards for independent content units.

Make the clickable region clear:

- entire card clickable, or
- explicit actions

Do not create conflicting nested click targets without clear behavior.

Keep title, status, metadata, and action positions consistent across repeated cards.

## 12. Tables and data grids

Choose a true data grid only when users need richer interaction such as:

- cell navigation
- selection
- editing
- column reordering
- keyboard operations

For ordinary comparison, a semantic HTML table may be better.

Specify:

- sorting
- filtering
- pagination
- empty state
- loading
- selection
- bulk action
- row action
- overflow
- responsiveness
- keyboard model

## 13. Filters

Make filters reflect real user questions.

Good filter labels:

- Status
- Date
- Owner
- Region
- Price

Show:

- active filter count
- selected values
- clear one
- clear all
- result update behavior

For expensive queries, use Apply. For fast local filtering, immediate updates can be appropriate.

## 14. Pagination vs infinite scroll

Use pagination when:

- users need location and resumption
- comparison across result positions matters
- footer content matters
- task has a meaningful page unit

Use load-more when:

- exploration benefits from continuity
- users still need conscious control over continuation

Use infinite scrolling with caution. It removes natural stopping cues and can create accessibility, navigation, memory, and wellbeing problems.

## 15. Pricing tables

A pricing interface should help a person answer:

- which plan fits my needs?
- what will I pay?
- what is included?
- what is limited?
- what changes at renewal?
- can I cancel or change?
- which fees are conditional?

Use:

- clear feature language
- meaningful comparison
- consistent billing periods
- explicit taxes/fees where known
- honest trial terms
- non-deceptive recommendation badges

Do not use:

- fake "most popular" claims
- hidden recurring charges
- preselected add-ons
- misleading crossed-out prices
- hard-to-find cancellation

## 16. Empty states

An empty state is often a first-use state.

Answer:

- why is it empty?
- is this expected?
- what can the user do next?
- can the system help create/import something?

Do not fill empty states with decorative art while hiding the next action.

## 17. Loading states

Choose by wait and context:

### Immediate acknowledgement
Pressed/selected state after input.

### Spinner
Small localized wait with indeterminate duration.

### Skeleton
Useful when content structure is known and showing the structure reduces uncertainty. Keep dimensions stable to prevent layout shift.

### Progress bar
Use for work with meaningful progress.

### Background job
Give status, allow leaving where safe, and provide a way to return.

Never use artificial delay to make the product feel "serious" unless there is a well-researched trust reason and no faster transparent alternative.

## 18. Error states

Classify first:

- user input error
- network error
- server/system error
- permission error
- conflict
- expired session
- unavailable resource
- destructive failure after partial success

Then tell the user:

- what happened
- what remains safe/saved
- what they can do
- whether retry is useful

Do not blame the user.

## 19. Destructive actions

Prefer undo for reversible low-risk actions.

Use confirmation when consequences are:

- irreversible
- costly
- broad
- security-sensitive
- difficult to recover

Confirmation copy should name the object and consequence.

For extremely high-risk actions, a stronger friction step may be justified, such as typing a resource name.

## 20. Permissions

Ask for a permission at the moment its value is clear.

Before the platform prompt, explain:

- what capability is needed
- what it enables
- what happens if declined

Design the declined path. Do not trap users after they say no.

## 21. Authentication

Reduce friction without weakening security.

Consider:

- password manager support
- passkeys where appropriate
- clear password requirements before submission
- show/hide password
- useful error messages
- preserved non-sensitive input
- recovery
- MFA device loss
- expired links
- rate limiting feedback

Avoid exposing whether an account exists when that creates a security/privacy risk.

## 22. Onboarding

Onboarding should help users reach value, not tour every feature.

Prefer:

- progressive onboarding
- sample data
- contextual tips
- first-task guidance
- checklists only when they reflect a meaningful sequence

Avoid:

- long slide decks before use
- permission prompts without context
- forcing profile completeness that is not needed
- celebratory screens after every micro-step

## 23. Notifications

Every notification should have a reason to interrupt.

Define:

- trigger event
- user benefit
- urgency
- channel
- frequency cap
- grouping
- quiet behavior
- preference control
- deep-link destination

Do not use notifications merely to manufacture activity.

## 24. State matrix template

For each component or screen:

```text
Default:
Hover:
Focus:
Pressed:
Selected:
Disabled:
Loading:
Empty:
Success:
Warning:
Error:
Offline:
Permission denied:
Long content:
Small viewport:
Keyboard:
Screen reader:
Reduced motion:
```

Delete states that truly do not apply. Never leave them undefined by accident.

## 25. Component acceptance template

```text
Component:
Purpose:
Anatomy:
Variants:
States:
Content rules:
Interaction:
Keyboard:
Touch target:
Accessible name/role/state:
Responsive behavior:
Loading:
Errors:
Analytics:
Examples:
Anti-patterns:
Acceptance criteria:
```
