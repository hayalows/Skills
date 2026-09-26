# Design Systems and Implementation Handoff

Use this reference when turning product decisions into reusable components and implementation-ready specifications.

## 1. System before library

A design system is:

- principles
- semantic foundations
- tokens
- components
- patterns
- content rules
- accessibility rules
- documentation
- governance

A component library without shared rules is only an asset collection.

## 2. Start with semantic foundations

Define:

- typography roles
- color roles
- spacing
- sizing
- radius
- border
- elevation
- motion
- breakpoints/container rules
- iconography
- z-index/layering
- state conventions

Avoid naming tokens by appearance when their purpose is semantic.

Weak:
`blue-500`

Useful alias:
`color-action-primary`

It is fine to keep primitive palette tokens under semantic aliases.

## 3. Token layers

A mature token structure may use:

### Primitive
Raw value:
`blue.600 = #...`

### Semantic
Meaning:
`text.link = {blue.600}`

### Component
Specific application:
`button.primary.background.default = {action.primary}`

Do not create component tokens for every one-off value. Add layers when reuse and theming justify them.

## 4. Spacing tokens

Use a limited scale.

Example:

```text
space.1 = 4
space.2 = 8
space.3 = 12
space.4 = 16
space.6 = 24
space.8 = 32
space.12 = 48
space.16 = 64
```

Map component spacing to tokens.

Avoid literal 17px, 19px, 23px values unless a technical constraint truly requires them.

## 5. Typography tokens

Define semantic roles such as:

```text
type.display
type.pageTitle
type.sectionTitle
type.cardTitle
type.body
type.bodySecondary
type.label
type.caption
type.button
```

A role should include full typography, not just font size.

## 6. Color tokens

At minimum consider:

- background
- surface
- text
- border
- action
- focus
- selection
- feedback
- destructive
- data visualization

Each semantic role should work in all supported themes.

Do not build dark mode by mechanically inverting colors.

## 7. Component anatomy

Document named parts.

Example button:

- container
- label
- leading icon
- trailing icon
- progress indicator
- focus ring
- hit area

Named anatomy improves design/code discussions.

## 8. Variants vs states

### Variant
A stable configuration chosen by context.

Examples:
- primary / secondary / tertiary
- small / medium / large
- icon-only / text / text+icon

### State
A temporary condition.

Examples:
- hover
- focus
- pressed
- disabled
- loading
- selected

Do not encode every combination as a separate unrelated component.

## 9. Component API

For each component define the minimum useful API.

Example:

```text
Button
- variant: primary | secondary | tertiary | destructive
- size: sm | md | lg
- label: string
- leadingIcon?: Icon
- trailingIcon?: Icon
- loading?: boolean
- disabled?: boolean
- type?: button | submit
- onPress
```

Then define constraints:

- icon-only buttons require accessible label
- loading prevents duplicate activation
- destructive cannot be default-selected accidentally

## 10. States

Every reusable component should explicitly define relevant states.

Do not rely on developers to infer focus, error, loading, or disabled behavior from screenshots.

## 11. Responsive component behavior

A component spec should state what changes:

- width
- layout
- label wrapping
- icon visibility
- alignment
- stacking
- interaction
- overflow

Avoid creating "mobile component" and "desktop component" duplicates when one responsive component can express both.

## 12. Native/platform components

Prefer adapting native or mature platform patterns when they fit.

Benefits:

- expected interaction
- accessibility semantics
- reduced implementation risk
- faster development
- platform consistency

Customize where the brand or product task truly requires it.

## 13. Atomic thinking

Atomic design can help teams reason from:

- primitives/atoms
- small composites/molecules
- larger organisms
- templates
- screens/pages

Use the concept if it helps organization. Do not turn taxonomy into bureaucracy.

## 14. Component documentation

Each component page should include:

- purpose
- anatomy
- variants
- states
- usage
- when not to use
- content rules
- accessibility
- behavior
- responsive behavior
- examples
- anti-patterns
- design tokens
- code status
- known limitations

## 15. Pattern documentation

Components alone do not explain flows.

Document patterns such as:

- validation
- search/filter
- destructive action
- empty state
- permissions
- onboarding
- bulk action
- data import
- checkout/payment
- account recovery

Patterns combine multiple components around a user task.

## 16. Content system

Define reusable content rules:

- button grammar
- error style
- date/time format
- number/currency format
- empty-state voice
- status labels
- destructive warnings
- capitalization
- abbreviations

Content consistency is part of system consistency.

## 17. Naming

Names should describe role and purpose.

Good:
- `Button/Primary/Medium`
- `Field/Text/Default`
- `Nav/Sidebar/Item`

Weak:
- `Blue button 2`
- `Rectangle 91`
- `New component final final`

Keep naming aligned between design and code where practical.

## 18. Figma structure

Use:

- auto layout for responsive internal structure
- components and variants
- variables/tokens where supported
- semantic naming
- component properties
- real content examples

Avoid excessive absolute positioning in reusable interface components.

## 19. Design/code parity

Maintain one shared concept of the component.

Track:

- designed
- coded
- documented
- accessible
- tested
- deprecated

If Figma and production differ, production behavior is the user's reality. Reconcile the system rather than letting divergence grow.

## 20. Handoff spec

For a screen/flow include:

- purpose
- viewport behavior
- grid/container
- component references
- spacing tokens
- typography tokens
- color tokens
- interaction
- transitions
- focus order
- keyboard behavior
- error/loading/empty states
- API/data assumptions
- analytics events
- performance expectations
- acceptance criteria

## 21. Data contract awareness

Designers do not need to define backend schemas, but should understand:

- which data exists
- latency
- optional fields
- permission rules
- pagination
- real-time updates
- optimistic constraints
- failure modes

A design that assumes impossible data timing is not implementation-ready.

## 22. Permission/role matrix

For multi-role products define:

```text
Capability | Admin | Manager | Member | Viewer
```

Then verify:

- navigation
- visible controls
- disabled vs hidden behavior
- direct URL access
- empty states
- error messages

Do not rely on visual hiding as authorization.

## 23. Analytics contract

For important interactions define:

```text
event:
trigger:
properties:
success/failure:
user role:
source:
privacy note:
```

Analytics should be purposeful.

## 24. Acceptance criteria

Write behavior, not visual vagueness.

Weak:
"Modal should look clean."

Better:
"Opening the modal moves keyboard focus to the dialog title. Tab remains within the dialog. Escape closes it. Closing returns focus to the launch button unless the confirmed action removes that context."

## 25. Visual regression

For mature systems, add automated visual checks for:

- component variants
- themes
- breakpoints
- long content
- error states

Visual regression does not replace functional or accessibility tests.

## 26. Deprecation

When replacing a component:

- mark old component deprecated
- explain replacement
- stop new adoption
- migrate high-traffic uses
- define removal timing
- remove duplicate tokens afterward

Avoid keeping two competing "primary button" components indefinitely.

## 27. Governance

Decide:

- who can change foundations
- review path
- contribution template
- release/versioning
- changelog
- design/code sync
- accessibility review
- migration responsibility

Keep governance proportionate to team size.

## 28. Contribution template

```text
Problem:
Current workaround:
Evidence of reuse:
Proposed component/pattern:
Existing alternatives:
Variants:
States:
Accessibility:
Responsive behavior:
Tokens:
Example contexts:
Engineering impact:
Migration:
Owner:
```

## 29. System audit

Look for:

- duplicate components
- near-identical tokens
- one-off overrides
- missing states
- inconsistent terminology
- broken theme variants
- inaccessible combinations
- Figma/code divergence
- undocumented patterns
- dead/deprecated assets still in use

## 30. Handoff quality gate

Before engineering starts:

- component exists or ownership for new component is clear
- every required state exists
- responsive behavior is explicit
- content is realistic
- permissions are known
- accessibility behavior is specified
- loading/error/empty states are present
- analytics are defined where needed
- data assumptions are feasible
- acceptance criteria are testable
