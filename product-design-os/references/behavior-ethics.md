# Behavior Design, Habit Formation, and Ethics

Use this reference only when repeated behavior is materially relevant to the user's own recurring goal.

The source model here is the Hook Model from *Hooked*, strengthened with user-autonomy and anti-deceptive-pattern safeguards from *Laws of UX* and current human-centered design practice.

## 1. First ask whether a habit is needed

Not every product should be habit-forming.

Habit design is most relevant when:

- the user has a recurring problem
- the behavior occurs often enough to become routine
- repeat use makes the user's outcome better
- the product can provide value without escalating compulsion

It is usually a poor fit for:

- infrequent high-stakes transactions
- one-time government/service tasks
- emergency flows
- products where repeated use itself is not the user goal
- situations where the business benefits from consumption that the user is trying to reduce

Do not add streaks, variable rewards, or notifications to a product simply because retention is low.

## 2. The Hook Model

The four phases are:

1. Trigger
2. Action
3. Variable Reward
4. Investment

Use the model as a diagnostic loop, not a mandate to maximize time spent.

## 3. Trigger

A trigger cues action.

### External triggers
The system or environment tells the user what to do.

Examples:

- reminder
- notification
- email
- app icon badge
- calendar event
- link from another person
- contextual prompt inside the product

### Internal triggers
An existing thought, situation, routine, or emotion cues the behavior from memory.

Examples:

- "I need to remember this"
- "I need to know the answer"
- "I have five minutes to fill"
- "I need to check whether the payment arrived"
- "It is Monday, so I review the dashboard"

The design goal is not to manufacture distress. It is to understand the user's real recurring situation and connect the product to it.

### Trigger questions

- What happens immediately before the intended behavior?
- What is the user trying to resolve?
- How frequently does that situation occur?
- Can an external trigger arrive at a useful moment?
- Can the user control the trigger?
- Does the trigger become less necessary as the behavior becomes routine?

### Notification rule

A notification should be an interrupt with a user-benefit case.

For each notification specify:

```text
Event:
User value:
Urgency:
Channel:
Frequency cap:
Quiet behavior:
Deep link:
Mute/control:
Expiry:
What happens if ignored:
```

## 4. Action

The action is the simplest meaningful behavior the user takes in anticipation of an outcome.

Before increasing motivation, make the action easier.

Audit ability constraints:

- time
- money
- physical effort
- mental effort
- social friction
- unfamiliarity/non-routine behavior

### Action simplification sequence

1. remove the step
2. prefill known information
3. reduce typing
4. reduce switching
5. use a better default
6. explain the next step
7. move the control closer to context
8. make the target easier to acquire
9. allow save/resume
10. automate only when safe and transparent

Do not hide consequential information in the name of simplicity.

## 5. Motivation

Motivation fluctuates and is expensive to manufacture.

A robust product should work even when user motivation is ordinary.

Prefer:

- a clear benefit
- low effort
- confidence
- timely context

over:

- artificial urgency
- social pressure
- guilt
- loss framing unrelated to the real consequence

## 6. Variable reward

*Hooked* groups variable rewards into:

- **tribe**: social connection, recognition, belonging
- **hunt**: information or material/resource search
- **self**: mastery, competence, completion

Use variability carefully.

Good variability:

- a personalized learning insight
- new relevant search results
- social responses the user intentionally asked to receive
- a changing challenge that supports skill development

Risky variability:

- endless randomized content with no stopping cue
- reward schedules designed primarily to increase session length
- social metrics that provoke compulsive checking
- mystery outcomes attached to spending

### Reward test

A reward should:

- satisfy the reason the user arrived
- preserve autonomy
- be understandable
- connect to product value
- not require escalating uncertainty to keep attention

"Leaves the user wanting more" is not by itself a user-benefit criterion.

## 7. Investment

Investment is a small contribution that increases future value.

Common stored-value forms:

- preferences
- content
- data
- followers/connections
- reputation
- learned skill
- saved configuration
- history

A healthy investment improves future use.

A harmful "investment" merely raises switching costs.

### Investment questions

- What future benefit does the user receive?
- Can the user edit/delete/export this value where appropriate?
- Are we making the experience better or simply harder to leave?
- Does investment make the next relevant action easier?

## 8. Loading the next trigger

A prior action may create a useful future cue:

- reminder created
- recurring schedule saved
- collaborator invited
- report subscribed
- saved search alert
- learning plan scheduled

The next trigger should arise from user intent. Do not silently opt people into recurring prompts.

## 9. Habit Zone

Habit formation depends on both:

- frequency
- perceived utility

A rare task generally will not become an automatic habit regardless of importance.

Do not force habit mechanics onto low-frequency products. Improve recall, findability, and trust instead.

## 10. Habit testing

A useful adaptation of the book's Identify → Codify → Modify cycle:

### Identify
Define what healthy repeat use means for this product.

Use real behavior data to identify users who repeatedly achieve the intended outcome.

Avoid using raw session count alone.

### Codify
Study what successful recurring users do.

Look for:

- entry source
- first-value action
- path sequence
- frequency
- time to value
- content created
- collaborators connected
- preferences saved
- recovery from failure

Find a candidate "habit path," but do not assume correlation proves causation.

### Modify
Reduce unnecessary friction for more users to reach the same valuable outcome.

Then measure:

- whether more users achieve the outcome
- whether satisfaction changes
- whether adverse behavior increases
- whether support/error rates change

Repeat.

The original book's example thresholds are historical heuristics, not universal benchmarks. Set thresholds from your product, category, and evidence.

## 11. Manipulation check

Before behavior-shaping work, ask:

- Would the product team willingly use this experience themselves in the same conditions?
- Does the product materially help the user achieve a goal they value?

Then go further with modern safeguards:

- Is the mechanism transparent enough to explain plainly?
- Can users stop it without punishment?
- Can they control notifications and recurrence?
- Are default settings aligned with reasonable expectations?
- Does the design protect heavy or vulnerable users?
- Does the business metric conflict with the user's stated goal?
- Are we collecting data because it improves the experience, or because we can?

## 12. Autonomy test

A user retains autonomy when they can:

- understand the choice
- decline without disproportionate penalty
- change their mind
- undo where possible
- leave/cancel
- control interruptions
- access the core consequence before committing

Reactance increases when people feel controlled. Preserving choice is both ethical and often more sustainable.

## 13. Dark/deceptive pattern prevention

Reject:

### Forced continuity
Trial silently becomes paid without clear advance disclosure or manageable cancellation.

### Obstruction
Cancellation, privacy controls, or account deletion are much harder than signup.

### Confirm-shaming
Decline copy insults, pressures, or implies moral failure.

### Hidden costs
Fees appear after users have invested substantial effort.

### Sneaking
Adding items, options, or consent users did not deliberately choose.

### Misdirection
Visual emphasis steers users away from the choice they reasonably expect to make.

### Disguised ads
Commercial content looks like ordinary product content.

### Fake scarcity/social proof
False timers, stock levels, activity, demand, or endorsements.

### Privacy-zuckering / data overreach
The interface nudges users into sharing more than expected or needed.

### Repeated pestering
Users repeatedly decline, but the prompt keeps returning without a material change in context.

## 14. Defaults

Defaults are powerful because many users do not change them.

A good default is:

- safe
- reversible
- aligned with common intent
- easy to inspect
- not financially or privacy-invasive by surprise

For high-impact choices, do not use silent opt-in defaults.

## 15. Infinite scroll and autoplay

These patterns remove stopping cues.

Use only when continuous consumption is the user's actual goal and provide:

- pause/stop where relevant
- position/history
- sensible session boundaries
- return/resume
- controls for autoplay
- accessibility support

For task products, prefer a natural endpoint.

## 16. Streaks

Streaks can support consistency, but can also turn missed days into anxiety.

Healthier streak design:

- grace/rest days
- recovery
- cumulative progress
- weekly goals
- no public shaming
- no loss of earned value for one missed day

Ask whether consistency is the user's goal or the company's retention mechanic.

## 17. Gamification

Bad gamification adds points to unwanted work.

Before badges/levels, validate:

- the underlying task is valuable
- the reward reflects meaningful progress
- the user understands the rules
- competition is appropriate
- no vulnerable group is harmed
- intrinsic motivation is not displaced

Use mastery and meaningful feedback before decorative points.

## 18. Social proof

Social proof can reduce uncertainty when it is truthful and relevant.

Good:

- verified ratings
- real usage counts with context
- recognizable customers with permission
- peer examples from a relevant cohort

Bad:

- anonymous unverifiable claims
- fake live activity
- inflated counts
- "people are viewing this" without truthful data

## 19. Scarcity and urgency

Use only when scarcity or time pressure is real.

State:

- what is limited
- why
- until when
- what happens after

Never fabricate a countdown.

## 20. Subscription and cancellation

A subscription experience should make clear:

- price
- billing period
- trial end
- renewal behavior
- next charge
- what cancellation changes
- how to cancel

Cancellation should be reasonably symmetric with signup in effort.

A save-offer can be acceptable if:

- it does not block exit
- it is truthful
- the decline is clear
- it is not repeated excessively

## 21. Vulnerable-use review

Run an explicit review when the product may be used by:

- children/teens
- people in financial stress
- people with compulsive behavior risk
- people in crisis
- people making high-stakes health/legal/financial decisions

Ask:

- What happens under extreme use?
- What does the product reward?
- Can the product detect and reduce harmful patterns?
- Are limits/defaults protective?
- Can a user take a break without penalty?

## 22. Metrics

Never optimize only for:

- time on site
- notification opens
- sessions per day
- scroll depth
- content consumed

Pair business metrics with a user outcome.

Examples:

Learning:
- lesson completion + demonstrated mastery

Finance:
- engagement + successful, understood task completion

Marketplace:
- booking conversion + cancellation/refund satisfaction

Productivity:
- active days + tasks completed with lower effort

Community:
- posting + quality/safety indicators

## 23. Behavior-design decision record

```text
Recurring user problem:
Desired behavior:
Frequency:
User value:
External trigger:
Possible internal trigger:
Simplest useful action:
Reward:
Investment:
Next trigger:
User control:
Stopping cue:
Vulnerable-use risk:
Business metric:
User outcome metric:
Potential unintended consequence:
Validation plan:
Decision:
```

## 24. Red-team questions

Before launch ask:

- How could this mechanic be abused?
- What if a user repeats it 100 times?
- What if a child uses it?
- What if the user misunderstands the default?
- What if the reward stops being useful but remains compelling?
- What if a user wants to leave?
- What metric would reveal harm?
- Would we be comfortable describing the mechanism in public?
