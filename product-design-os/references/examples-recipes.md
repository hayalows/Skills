# Worked Examples and Product Design Recipes

Use these examples as patterns for applying Product Design OS. They are not templates to copy blindly. The point is to show how product, psychology, interface craft, accessibility, resilience, ethical behavior, and measurement fit together.

# Example 1: Mobile Fintech Transfer

## Brief

A user needs to send money to another person from a mobile app. The action is common, financially consequential, and often completed under time pressure or imperfect connectivity.

## Primary outcome

Send the intended amount to the intended recipient, with clear fees and confirmation, without duplicate transfer or ambiguity.

## Flow

1. Choose recipient
2. Enter amount
3. Review transfer details
4. Authenticate/confirm
5. Processing
6. Success or recoverable failure

## Design reasoning

### Familiarity
Use a familiar transfer structure rather than a novel gesture-driven flow. Financial tasks benefit from recognition and predictable review.

### Fitts
Make the primary Continue/Send control large and easy to reach. Keep destructive or cancel controls visually and spatially separated.

### Hick
Do not show every transfer method at every step. If a user has one common funding source, select a safe default and allow change.

### Postel
Accept harmless amount formatting and normalize it. Do not silently reinterpret ambiguous currency values.

### Tesler
The system should carry recipient formatting, fee calculations, network routing, and duplicate-protection complexity. The user must still see the consequence before the final action.

### Peak-End
The confirmation step and final receipt are high-memory moments. The review screen should reduce uncertainty; the completion state should clearly say what happened and what comes next.

## Screen specification

### Recipient
- Search existing recipients
- Add new recipient
- Show name plus enough disambiguating information
- Avoid exposing full sensitive identifiers unnecessarily
- No-result recovery path
- Loading and offline state

### Amount
- Persistent currency label
- Numeric keyboard
- Available balance where useful
- Fee and receiving amount visible before final confirmation
- Prevent impossible values early
- Preserve entered amount on recoverable validation failure

### Review
Show:
- recipient
- amount
- fee
- total debit
- funding source
- expected timing
- editable fields
- final action label such as "Send GHS 250"

Avoid a generic "Confirm" if the specific consequence can be named.

### Processing
Immediately acknowledge the action. Disable duplicate submission. If processing can take time, show a durable state rather than a spinner that disappears with no record.

### Success
Show:
- clear success status
- amount and recipient
- reference
- date/time
- next useful actions such as Share receipt or Done

### Failure
Differentiate:
- no network
- timed out but status unknown
- declined
- insufficient funds
- recipient unavailable
- duplicate detected

For "status unknown," do not tell the user to simply try again. First help them check whether money moved.

## Accessibility
- large touch targets
- visible labels
- amount and fee readable with large text
- screen-reader announcement of processing and completion
- no status conveyed by color alone
- logical focus after an error
- accessible authentication path

## Performance
- cache recent recipient metadata where appropriate
- preserve draft through short interruptions
- keep the initial transfer form lightweight
- avoid large decorative imagery
- protect against repeated requests

## Metrics
Pair:
- transfer completion rate
with:
- duplicate-transfer rate
- correction/backtrack rate
- support contacts
- failed/unknown-state rate
- time to verified completion

A higher conversion rate is not success if duplicate or misunderstood transfers increase.

---

# Example 2: SaaS Analytics Dashboard

## Brief

A manager opens a dashboard to understand what changed, why it changed, and what needs attention.

## Primary outcome

Move from status to decision without scanning a wall of charts.

## Information hierarchy

1. Current status
2. Meaningful change
3. Exceptions/risks
4. Drivers
5. Details
6. Actions

## Structure

### Top summary
Use a small group of decision-relevant KPIs, not every available metric.

Each KPI card should answer:
- what metric
- current value
- comparison period
- direction/change
- context or threshold
- drill-down action

### Trend
Choose one or two charts that explain the change. Do not repeat a KPI card as a decorative chart unless the trend adds information.

### Exceptions
Surface:
- missed targets
- anomalies
- unresolved operational issues
- segments driving change

### Detail table
Use a table when the user needs row/column comparison. Support meaningful sorting, filters, and drill-down.

## Laws applied

### Hick
Keep the default view focused. Put uncommon filters and configuration behind progressive disclosure.

### von Restorff
Reserve the strongest visual emphasis for the most important exception or action. If every KPI is brightly colored, the effect disappears.

### Miller
Do not use a seven-card rule. Chunk metrics by meaning and preserve labels/context.

### Aesthetic-Usability
A polished dashboard can feel trustworthy while still hiding bad data or unclear definitions. Add metric definitions and source/freshness context.

## Empty state

If no data exists:
- explain why
- show the setup required
- offer a clear action
- optionally provide sample data if that helps learning

Do not show six empty chart shells without guidance.

## Loading
Prefer stable skeleton dimensions for known regions. Load the highest-value summary first if possible.

## Accessibility
- charts need text summaries
- do not use red/green alone
- table headers need proper semantics
- keyboard-accessible filters
- visible focus
- readable labels and tooltips

## Measurement
- time to identify a problem
- successful drill-down
- repeated use tied to operational decisions
- support questions about metric meaning
- performance under realistic data volume

---

# Example 3: Ecommerce Checkout

## Brief

A shopper wants to buy a product with minimal unnecessary effort while understanding price, delivery, and payment consequences.

## Core flow

Cart → details/delivery → payment → review → confirmation

## Familiarity
Follow well-known checkout conventions unless testing shows a better pattern. The checkout is not the place to make navigation experimental.

## Reduce friction
- support guest checkout where the business permits
- use browser/platform autofill
- prefill known customer data
- preserve data after validation failure
- use address autocomplete carefully and allow manual correction
- show the order summary throughout
- avoid requiring account creation before value is clear

## Price transparency
Before commitment show:
- item total
- delivery
- taxes where known
- discounts
- recurring charges if any
- final total
- billing cadence for subscriptions

Never reveal mandatory fees only at the last instant to exploit sunk effort.

## Validation
Bad:
"Invalid card."

Better:
"Check the card number. It should contain 16 digits."

Do not erase the address because one field is invalid.

## Review
For high-value or irreversible purchases, a review step can be useful friction.

## Completion
Show:
- order received
- order number
- charged amount
- delivery estimate
- tracking/next step
- cancellation or support route where relevant

## Performance
Checkout performance is product performance. Avoid third-party scripts that block input or cause layout shifts.

## Ethics
Reject:
- preselected paid extras
- fake countdowns
- disguised subscriptions
- difficult cancellation
- misleading "only 1 left" claims without real inventory evidence

## Metrics
Conversion plus:
- refund/cancellation
- chargeback
- support contacts
- form error rate
- payment retry
- customer understanding of subscription terms

---

# Example 4: Search-Heavy Knowledge or Product Catalog

## Brief

Users know roughly what they need but not where it lives.

## Search surface

Provide:
- prominent search entry
- suggestions
- recent searches when useful
- typo tolerance
- category hints
- clear query editing
- result count
- filters
- sort
- preserved query state

## Search result hierarchy

Each result should expose the attributes users actually compare.

For a knowledge product:
- title
- source
- recency
- snippet
- content type

For a catalog:
- item
- image
- price
- availability
- critical variant/status

## No-results recovery

Instead of "No results":
- show query
- show active filters
- suggest spelling
- allow clearing filters
- suggest broader category
- offer a request/add path when appropriate

## Filtering
Keep high-frequency filters visible. Put long-tail filters behind progressive disclosure.

Show active chips or another clear representation of what is currently constraining results.

## Accessibility
A custom combobox must follow an established keyboard/screen-reader model. Prefer a mature accessible component to inventing one.

## Metrics
- successful search-to-task completion
- zero-result rate
- query reformulation
- filter abandonment
- result click quality
- repeated failed searches

---

# Example 5: Learning App With Healthy Repeat Use

## Brief

A learner wants to study consistently and make measurable progress.

This is a valid repeat-use context, but engagement mechanics must serve learning.

## Hook analysis

### Trigger
Possible external trigger:
- user-selected daily reminder

Possible internal trigger:
- "I have ten minutes and want to keep my learning moving"

The notification should be configurable and easy to mute.

### Action
Make the useful action small:
"Continue the next 5-minute lesson"

Do not begin by asking the learner to choose from dozens of paths every session.

### Reward
Use rewards of self:
- visible mastery
- useful feedback
- progress through a meaningful curriculum

Variable content can keep practice fresh, but do not randomize merely to create uncertainty.

### Investment
Useful investments:
- saved progress
- learning preferences
- completed practice history
- personal notes
- selected goal

These should make the next session more relevant.

## Streak design
Avoid punishing a single missed day.

Prefer:
- weekly consistency
- grace days
- progress retained
- recovery prompts
- cumulative mastery

A streak should not become more important than learning.

## Metrics
Pair daily/weekly engagement with:
- completion
- retention of knowledge
- assessment performance
- self-reported usefulness
- dropout after missed days

If sessions rise but learning outcomes fall, the behavior loop is not successful.

---

# Example 6: Low-Bandwidth Event Registration and Check-In App

## Brief

Staff check in participants on mobile devices in crowded conditions with unreliable internet.

## Constraints
- intermittent network
- low-cost Android devices
- sunlight
- one-handed use
- queues
- duplicate records
- partial registrations
- staff under time pressure

## Primary task
Find a participant, confirm identity/status, check them in, and immediately know whether the action succeeded.

## Design

### Search first
Make participant search the dominant action.

Support:
- name
- ID
- phone suffix if appropriate
- status filters
- recent participants

### Result card
Show only information needed to disambiguate:
- name
- participant ID
- group/company
- status

### Check-in action
Use a large button. After activation:
- immediate pressed state
- optimistic UI only if safe
- visible sync status
- duplicate protection

### Offline/degraded
Possible states:
- Saved on this device, waiting to sync
- Syncing
- Synced
- Conflict needs review

Do not falsely say "Checked in" if the server state is unknown and that distinction matters operationally.

### Recovery
If an offline action later conflicts with a server update:
- preserve both facts
- explain the conflict
- let an authorized staff member resolve it

## Visual craft
High contrast beats delicate styling. Avoid tiny gray metadata. Keep tap targets generous.

## Performance
- cache recent roster/search index if permitted
- lazy load secondary data
- avoid heavy imagery
- preserve form state
- show stale-data timestamp when offline

## Metrics
- median check-in time
- duplicate rate
- sync failure
- conflict rate
- queue time
- support/escalation rate

---

# Example 7: B2B Admin Destructive Action

## Brief

An administrator can delete a workspace containing member data.

## Risk
Deletion is irreversible and broad. This is a case where deliberate friction is appropriate.

## Flow
1. Admin chooses Delete workspace
2. Dialog explains consequence
3. Name of workspace is shown
4. Admin may be required to type the workspace name for high-risk deletion
5. Final action says "Delete [workspace]"
6. Processing is locked against duplicate activation
7. Completion returns to a logical destination

## Design rules
- destructive control visually distinct
- no generic "Yes"
- safe Cancel action obvious
- focus moved into modal
- Tab contained
- Escape works if cancellation is valid
- focus returns logically on cancel
- no hidden retention offers blocking exit

## Permission
The UI may hide or disable deletion for non-admins, but backend authorization remains mandatory.

## Audit question
Can an accidental click or keyboard action delete the workspace without a meaningful understanding step?

---

# Example 8: Pricing Page

## User questions
- Which plan fits me?
- What will I pay?
- What is limited?
- What happens if I exceed a limit?
- Can I switch/cancel?
- Is this monthly or annual?

## Layout
- concise positioning
- 2–4 clear plan columns where comparison is useful
- important differences aligned by row
- monthly/annual toggle with equivalent pricing language
- expandable full comparison for long feature lists
- FAQ for genuinely complex terms

## Choice architecture
A recommended plan is acceptable when the reason is honest and useful, such as "Best for teams of 5–20."

Do not label a plan "Most popular" unless data supports the claim.

## Accessibility
- table/card structure remains understandable without color
- toggle state programmatically available
- prices read in the correct order
- focus states clear
- details accessible on narrow screens

## Metrics
Conversion plus:
- plan-change rate shortly after purchase
- billing support contacts
- refund requests
- trial-to-paid understanding
- cancellation friction reports

---

# Example 9: Responsive Account Settings

## Goal
Let a user control identity, security, privacy, notifications, and billing without a crowded single screen.

## IA
Top-level groups:
- Profile
- Security
- Privacy
- Notifications
- Billing

Use progressive disclosure for advanced settings.

## Desktop
Sidebar + content region can work well.

## Mobile
Use drill-in navigation. Do not squeeze sidebar and form into a tiny two-column layout.

## Settings item pattern
- label
- concise description
- current value/status
- action/control
- feedback

## High-impact settings
Security, privacy, and billing deserve explicit consequence copy and confirmation where appropriate.

## Notifications
Group by purpose rather than channel first when that matches the user's mental model:
- Account/security
- Product activity
- Reminders
- Marketing

Then allow channel preferences.

---

# Example 10: Product Design Audit Report

## Observation
"Save staff status" button appears enabled, but tapping it produces no visible change for several seconds.

## Bad finding
"The button UX is confusing."

## Strong finding

**Location:** Staff status editor  
**Observed:** Tapping Save has no immediate pressed/loading state. On a throttled connection the screen remains unchanged for 2.8 seconds.  
**User consequence:** Staff may tap repeatedly, creating uncertainty and possible duplicate requests.  
**Principles:** visibility of system status, Doherty-style immediate feedback, error prevention.  
**Recommendation:** show pressed/loading feedback immediately, disable repeat activation while the request is pending, preserve values, and show success/failure inline.  
**Severity:** High if duplicate writes are possible; Medium if writes are idempotent.  
**Validation:** test on slow network, double-tap, failure, and retry.

This is the level of specificity Product Design OS should produce.

# Recipe: New Product Screen

```text
1. User/job
2. Entry state
3. Primary outcome
4. Required information
5. Primary action
6. Secondary actions
7. System status
8. Loading
9. Empty
10. Error
11. Permission
12. Responsive transformation
13. Keyboard/focus
14. Screen reader semantics
15. Performance assumptions
16. Analytics
17. Acceptance criteria
```

# Recipe: Redesign

```text
1. Capture current flow
2. Separate actual failure from aesthetic dislike
3. Identify what users already understand
4. Preserve useful mental models
5. Remove unnecessary steps/choices
6. Repair hierarchy
7. Fill missing states
8. Fix accessibility
9. Test responsive/slow-network cases
10. Validate with task-based usability testing
```

# Recipe: Component

```text
Purpose
Anatomy
Variants
Default
Hover
Focus
Pressed
Selected
Disabled
Loading
Success
Warning
Error
Content rules
Keyboard
Screen reader
Touch target
Responsive behavior
Example
Anti-pattern
Acceptance criteria
```
