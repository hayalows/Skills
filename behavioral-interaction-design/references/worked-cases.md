# Worked interaction briefs

These are hypothetical proposals and test plans. Project names identify example contexts. The cases make no claims about live behavior or measured results.

## Learning Room / resume an unfinished series

**Situation.** A learner returns with ten minutes. Assume the catalogue and playback work, but opening the series lands in a long list. Possible barriers include a weak prompt, inaccurate watch state, or a missing saved timestamp. Observe which one applies.

**Design.** Show “Resume lesson 4” with the saved time and a visible “View all lessons” link. If progress is unavailable, offer the lesson list and explain that the last position could not be restored. Show required lesson progress from reliable completion data. For material where watching and learning differ, offer an optional practice task with specific feedback and hints. Keep manual progress choices distinguishable from verified completion. Avoid resetting earned progress after time away.

**Test.** Compare the current path with the resume action for eligible returns. Primary outcome is completion of the intended next lesson within seven days. Check wrong-lesson starts, restored timestamps, ability to switch lessons, and keyboard use. For a practice variant, measure delayed performance on a parallel task. [B01, B13, B20, B22]

## RouteLab / recover from a wrong turn

**Situation.** A driver needs to know whether the app has a new route. Traffic information may be old, and rerouting may be in progress.

**Design.** Use direct state labels such as “Finding a new route” and “Route updated” only when they match the underlying state. Show the next safe instruction with a voice equivalent when available. On GPS or network failure, state which guidance can still be trusted. Keep route alternatives and explanatory detail on a suitable stopped or pre-trip surface. The safety-critical moment calls for accurate feedback and minimal visual demand.

**Test.** Use simulation or a parked walkthrough with delayed GPS, no network, repeated wrong turns, and voice disabled. Ask what the user would do next and whether they understand which route is active. Treat unsafe interpretation and false confirmations as blockers. [B04, B15, B18, B22]

## Event checkout / select and pay for a ticket

**Situation.** People may abandon checkout because of missing payment methods, uncertainty about fees, or a slow confirmation. Each suggests a different fix.

**Design.** Display total, currency, fees, refund terms, and real expiry before payment. Group available methods by user familiarity. Allow guest payment if operationally feasible. Preserve selection on recoverable failure. Keep paid add-ons as active choices. Use “Payment pending” and a safe way to check status. On retry, prevent duplicate payment or ticket issuance. State capacity only from reliable inventory.

**Test.** Compare paid and confirmed orders per eligible checkout start. Check price recall, abandoned payment, duplicate charges, refund contacts, and recovery after interruption. Include a case where the paid choice is declined. [B13–B17, B21, B26, R18]

## StigmaClear / find a relevant support resource

**Situation.** Someone may be under stress and using a small screen or slow connection. The resource location and contact action are the meaningful outcomes.

**Design.** Put the direct contact details and eligibility where users can read them without signing in or following a reveal. Keep a plain fallback when geolocation is declined. Use warm, literal copy and show when contact information was checked if that date is known. Offer private saving only when it adds value and explain where it is stored. Limit instrumentation to what is needed and protect sensitive intent.

**Test.** Use low-bandwidth and assistive technology scenarios. Check findability, correct understanding, and recovery without location access. A contact click indicates attempted contact. Confirming access to support would require separate appropriate evidence. [B03, B08, B11, B15, B18, R19]

## Time tracking / improve estimation

**Situation.** People already track work. The underlying goal may be to make realistic plans. Interview them before treating increased logging as success.

**Design.** Offer a private estimate before a chosen task and compare it with actual time afterward. Show why a gap may have occurred only when the user can confirm it. Let users adjust future estimates and turn off comparisons. Keep a neutral state when data is incomplete. Skip leaderboards when work types differ or comparisons could pressure employees.

**Test.** Define eligible task types and measure absolute estimation error over several comparable tasks. Check editing or underreporting, perceived pressure, and manual-entry burden. An improvement in logging volume alone does not support the claim. [B20, B22, R14–R15]
