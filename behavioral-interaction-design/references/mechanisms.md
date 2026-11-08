# Mechanisms and failure modes

Pick the smallest intervention that matches the observed barrier. IDs refer to the source map. Examples below describe proposed interactions.

## Clarity, trust, and tone

| Mechanism | Use it when | Design decision and failure check |
| --- | --- | --- |
| Perceptual grouping [B03] | People misread which controls or items belong together | Group by proximity, shared region, or alignment. Ask users to identify a label's target and predict what a control affects. Check focus order and semantic grouping alongside the layout. |
| Visual fluency [B02, B04, R01–R04] | Presentation makes a useful tool feel unfamiliar or hard to scan | Compare two presentations with equivalent features. Measure confidence separately from successful task completion. Visual appeal can mask errors or make a weak tool seem more credible than it is. |
| Association and metaphor [B05–B06, R05] | People bring the wrong expectations to a new interaction | Name the expected association and test it with the audience. Keep an established convention for the action and put novelty in presentation. Test local language and context. A familiar metaphor for one group may confuse another. |
| Faces and people [B07] | The identity or accountability of a real person matters | Show an attributable person with consent and a label describing their role. Use privacy-preserving imagery where appropriate. Check that portraits leave room for the task and do not create a false endorsement. |
| Situated humor [B08] | A low-stakes transition has room for warmth | Put it after the outcome or on an optional surface. State the literal action first. Try the same copy with a rushed user, a screen reader, and a reader unfamiliar with the idiom. Keep error, payment, privacy, and safety copy direct. |
| Attention cues [B15] | People miss something necessary to decide | Make its weight reflect consequence, with position, wording, and accessible states as well as color. Test whether people can find the primary action and the decline, lower-cost, or cancellation path. |
| Framing and anchors [B17, R12] | Users struggle to understand scale or a decision | Pair relevant reference points with full amounts, time windows, and tradeoffs. Explain what a comparison means. Test recall of total cost and consequences after the user chooses. Avoid invented comparison prices and one-sided risk framing. |

## Exploration and first useful action

| Mechanism | Use it when | Design decision and failure check |
| --- | --- | --- |
| Optional surprise or useful gift [B09] | A stable task is complete and a real extra might be welcome | Give a recap, a useful export, or a small flourish after completion. Use a normal path on repeat use. Keep timing and value predictable where money, access, or entitlement is involved. Avoid making a gift create an obligation. |
| Pattern play [B10] | People want to explore a body of material | Offer an optional comparison, grouping, visual pattern, or collecting task that helps them understand the content. Make required labels and categories legible without solving a puzzle. |
| Specific curiosity gap [B11, R06] | There is a bounded unknown and a clear payoff | Offer a truthful preview, state what comes next, and deliver it promptly. Let people skip. Keep prices, requirements, search relevance, safety information, and the path out visible. Track whether the reveal answers the question. |
| Self-expression [B12] | Personal organization or identity helps users work | Offer an editable label, view preference, or private collection. Support reset and sensible defaults. Make public visibility an explicit choice. Check that setup adds value before it adds effort. |
| Small first step [B13, R07–R08] | The next intended step is too big or abstract | Let users preview, try with sample data, or save a draft. Show where that step leads. Let them leave without obligation. For planning, help them decide when and where in their own words. |
| Honest progress [B01, B13, R08] | A real multi-step task feels indefinite | Show completed required steps over total required steps, or name the current stage if the total varies. Separate optional items. Credit meaningful work already done and explain its origin. Recompute from saved state after a retry or interruption. |
| Sequencing and choice [B13–B14, R09–R10] | Users face several unfamiliar choices at once | Ask only what is needed to determine the next step. Group or compare options along dimensions people understand. Preserve advanced access and material differences. Avoid universal option-count rules. |
| Defaults and recommendations [B16, R11] | The user would benefit from a low-risk starting point | Select a reversible setting based on intent or prior preference. Show what was chosen and how to change it. Ask for an active choice when the effect involves cost, disclosure, or a recurring obligation. |
| Micromoments [B18] | The task feels like talking to an unhelpful clerk | Role-play user and system turns, write the next meaningful request, defer optional work, and choose tapping over typing only when the options are bounded. Test error recovery and direct entry for users who know what they want. |

## Repeat behavior, skill, and meaning

| Mechanism | Use it when | Design decision and failure check |
| --- | --- | --- |
| Challenge and mastery [B19–B20, R13–R14] | The user wants to improve at an activity | Identify the intrinsic challenge, set a small clear goal, offer adjustable difficulty, and show useful feedback. Let users decline competition. Compare improvement in the skill against time or actions spent earning a score. |
| Real constraints [B21] | Actual capacity is limited or a voluntary constraint improves practice | State the source and consequence of the limit. Offer alternatives or a waitlist where useful. Keep timers for genuine expiry or voluntary timed practice. A reset-on-refresh countdown is a rejection signal. |
| Actionable feedback loop [B22, R15] | People need to see how an action affects their goal | Show action, immediate state, interpretation, and an optional next move. Use personal baselines where appropriate. Try to raise the metric while harming the task. If possible, repair the metric or stop the experiment. |
| Goals and rewards [B23, R13–R14] | Progress is hard to see and an optional milestone may help | Recognize a demonstrated accomplishment. Explain what a badge or milestone means and offer a natural stopping point. Keep recognition independent of volume where quality matters. Avoid removing earned progress after time away. |
| Social proof and purpose [B25] | Relevant peers or a shared purpose help users judge or persist | Use representative, dated, verifiable signals. Where totals are small, use candid context. Be clear about denominator, date, and who is represented. Use personal or aggregate feedback without exposing people or making poor behavior look normal. |
| Prompt, ability, motivation [B25, R17] | The intended behavior still does not happen | Observe all three in the same context. Try a visible cue for willing, able users. If the task is too hard, simplify first. If the goal has little value to users, revisit the goal. |

## Practices to leave in their historical context

The book uses early web and app cases to generate ideas. Contemporary implementations need local evidence, accessible controls, consent, and a check on who bears the cost. Use the endowed-progress experiments to ask what real work can be acknowledged. Use compliance studies to recognize how a small ask can put pressure on later choices. Use variable rewards as a reason to examine the risk of repeated checking. Keep only the parts that serve an outcome users choose.

Use the Kano categories to surface assumptions across audience segments. Compare how people respond when the feature is present versus absent. Treat the classification as temporary and check it again when expectations change. [B24, R16]
