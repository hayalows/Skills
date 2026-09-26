# Foundations for website UX auditing

Use this reference to calibrate judgement. It is a working synthesis, not a list to recite in every audit.

## The central idea

A website is a conversation between a person with a goal and a system with rules, content, states, and consequences. Good UX makes the conversation legible:

1. The person can tell where they are.
2. They can tell what matters now.
3. They can predict what an action will do.
4. The system responds clearly.
5. The person can correct mistakes and keep control.
6. The result matches the promise.

The deeper lesson is that interface friction often points to a problem outside the interface: a policy, ownership boundary, data model, content decision, or service handoff. Fixing the visible screen alone can leave the real problem in place.

## Books selected for audit value

These are selected because they directly improve audit judgement. They are not presented as a definitive popularity ranking.

| Book | Main contribution | Carry into an audit |
| --- | --- | --- |
| Don Norman, [The Design of Everyday Things](https://jnd.org/books/the-design-of-everyday-things-revised-and-expanded-edition/) | Affordances, signifiers, mapping, feedback, constraints, conceptual models, and designing for error. | Ask what the interface tells a person they can do, what action-to-result mapping they expect, and how the system explains the result. Treat repeated user error as design evidence before blaming the user. |
| Steve Krug, [Don’t Make Me Think, Revisited](https://sensible.com/dont-make-me-think/) | Self-evident screens, scanning, familiar conventions, visible hierarchy, and practical usability testing. | Ask what a tired or distracted visitor can understand in a few seconds. Remove interpretation work before adding instructions. Test small, then fix and test again. |
| Alan Cooper, Robert Reimann, David Cronin, and Christopher Noessel, [About Face](https://www.wiley.com/en-gb/About%2BFace%3A%2BThe%2BEssentials%2Bof%2BInteraction%2BDesign%2C%2B4th%2BEdition-p-9781118766576) | Goal-directed design, personas, scenarios, interaction models, and designing around user goals instead of feature lists. | State the user’s goal and scenario before judging a screen. Flag flows that make users manage the product’s internal structure. |
| Erika Hall, [Just Enough Research](https://abookapart.com/products/just-enough-research.html) | Research questions, stakeholder alignment, interviews, small tests, and choosing evidence that reduces uncertainty. | Name the decision the audit should support. Match the method to the question. Do not gather more screenshots when the uncertainty is about real behaviour. |
| Indi Young, [Mental Models](https://indiyoung.com/books/) | Mental-model diagrams and organising information around how people understand their situation. | Compare the site’s categories and labels with the user’s words and sequence of thought. Look for internal organisational language exposed as navigation. |
| Luke Wroblewski, [Web Form Design](https://www.lukew.com/resources/web_form_design.asp) | Research-backed form layout, input choice, mobile considerations, and reducing completion friction. | Treat a form as a task conversation. Remove unnecessary fields, match controls to answers, preserve entered data, and make the next question obvious. |
| Kim Goodwin, [Designing for the Digital Age](https://www.oreilly.com/library/view/designing-for-the/9780470229101/) | Connects research, personas, scenarios, requirements, evaluation, and documentation. | Link findings to requirements and ownership. A finding is stronger when a team can build it, test it, and decide who maintains it. |
| Adam Silver, [Form Design Patterns](https://www.smashingmagazine.com/printed-books/form-design-patterns/) | Real form problems, accessible patterns, and progressive enhancement. | Prefer proven patterns for registration, sign-in, checkout, errors, and complex questions. Explain the condition that makes a pattern fit. |
| IDEO.org, [The Field Guide to Human-Centered Design](https://www.designkit.org/resources/1.html) | Field research, synthesis, prototyping, testing, and practical methods for complex human problems. | When the flow is unclear because the problem is unclear, return to people in context. Prototype the risky part and learn before polishing the whole thing. |

## Expert and organisation lenses

Use the lens that fits the question. Do not copy a company’s visual language just because it is famous.

| Source | Useful lens | Limits |
| --- | --- | --- |
| [Nielsen Norman Group](https://www.nngroup.com/) and Jakob Nielsen, Don Norman, Kate Moran, Sarah Gibbons, and colleagues | Heuristic evaluation, task analysis, journey mapping, usability testing, cognitive load, and usability metrics. | Heuristics reveal likely problems. They do not prove how a specific population behaves. |
| [GOV.UK Service Manual and Design System](https://www.gov.uk/service-manual) | Start with the user’s whole problem, join up online and offline steps, ask only necessary questions, use plain language, and structure complex services around user needs. | Government services have constraints and risk profiles that differ from commercial products. Borrow the reasoning, not every pattern. |
| [W3C Web Accessibility Initiative](https://www.w3.org/WAI/) and [WCAG 2.2](https://www.w3.org/TR/WCAG22/) | Perceivable, operable, understandable, and robust experiences; testable success criteria; keyboard, screen reader, zoom, focus, input, and status requirements. | Conformance is a technical baseline. It cannot replace disabled users’ input or a task-level usability test. |
| [Google Research HEART](https://research.google/pubs/measuring-the-user-experience-on-a-large-scale-user-centered-metrics-for-web-applications/) | Map goals to signals and metrics across happiness, engagement, adoption, retention, and task success. | Engagement or retention can increase while user welfare falls. Pair business metrics with task success, errors, complaints, and user control. |
| [Google Web Vitals](https://web.dev/articles/vitals) | Loading, interaction responsiveness, and layout stability through LCP, INP, and CLS; measure field data when possible. | Lab tools show a controlled slice. Field data varies by device, browser, connection, geography, and traffic. |
| [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines) | Clarity, platform conventions, feedback, content focus, hierarchy, and familiar interaction behaviour. | The HIG is platform-specific. A web audit should use it as a reference for clarity and convention, not as a universal law. |
| [Material Design 3](https://m3.material.io/) | Usability, component states, input methods, touch targets, motion, accessibility, and responsive structure. | A component can meet a design-system rule and still be wrong for the user’s goal or domain. |
| [Microsoft Inclusive Design](https://inclusive.microsoft.design/) | Recognise exclusion, learn from diversity, and solve for one person in ways that help many. | Inclusion cannot be inferred from a checklist alone. Test with people affected by the barrier. |
| [Baymard Institute](https://baymard.com/research/checkout-usability) | Large-scale ecommerce testing, checkout patterns, benchmarking, form detail, and repeated qualitative observation. | Its strongest evidence is ecommerce-specific. Do not transfer a checkout rule to an unrelated service without checking context. |

## Methods and what each can prove

| Method | Best question | What it can prove | What it cannot prove |
| --- | --- | --- | --- |
| Heuristic review | What likely usability problems are visible? | An evaluator can identify a mismatch with a stated principle or convention. | That users will encounter it, how often they will encounter it, or which fix they prefer. |
| Task analysis | What must a person do to achieve the goal? | The sequence, subtasks, dependencies, memory burden, and complexity of the current task. | That a proposed flow works without observing people. |
| Journey map | Where does the experience break across time and channels? | User actions, expectations, emotions, touchpoints, and ownership gaps when grounded in research. | The exact UI cause of every problem. |
| Cognitive walkthrough | Can a new or occasional user work out the next action? | Likely learnability barriers at each action: goal, control, result, and next step. | Expert performance, long-term retention, or actual user behaviour. |
| Moderated usability test | Can representative people complete realistic tasks, and where do they struggle? | Observed behaviour, misunderstandings, workarounds, and language users actually use. | Population-wide rates from a small qualitative sample. |
| Quantitative usability test | How often, how fast, or how successfully do users complete a defined task? | Benchmarks such as success rate, time, errors, and satisfaction with an appropriate sample and protocol. | The cause of a failure without qualitative evidence. |
| Analytics and funnel data | Where do people stop, repeat, or fail at scale? | Behavioural patterns across real traffic, segments, routes, and time. | Why a person stopped or what they expected. |
| Accessibility inspection | Can the interface be operated and interpreted through supported access modes? | Technical issues in semantics, focus, keyboard, text visibility, reflow, names, status, and input. | The complete lived experience for disabled people. |
| Performance measurement | How does speed and stability affect actual use? | Field or lab signals for loading, responsiveness, and layout stability. | That a faster page will fix a comprehension or trust problem. |

## Principles that survive across products

1. **Outcome before interface.** A form is a means. The user wants a result.
2. **Visible state.** The person should know what the system is doing, what changed, and what can happen next.
3. **Recognition over recall.** Keep needed information and choices available at the moment of action.
4. **Good defaults with control.** Choose a safe starting point, explain it when it matters, and let the person change it.
5. **Prevent high-cost errors.** A warning after an irreversible action is weaker than a design that makes the mistake difficult.
6. **Recovery is part of the happy path.** People forget passwords, lose connections, misread questions, change their minds, and return later.
7. **Language is interface.** Labels and error messages shape the user’s mental model of the task.
8. **Consistency reduces learning.** Reuse conventions unless the domain gives users a stronger, tested model.
9. **Progressive disclosure has a condition.** Hide secondary complexity, not information needed for an informed choice.
10. **Friction has a moral direction.** Remove friction that wastes time. Keep friction that prevents harm or protects autonomy.
11. **The service is larger than the screen.** A broken handoff, delay, policy, or support path is a UX problem even when the pixels look fine.
12. **Every claim has an evidence level.** Strong language requires strong evidence.

## Ethical guardrail

The goal is low cognitive cost for the user’s own goal, not maximum compliance with the organisation’s goal. Treat hidden fees, forced registration, asymmetric consent, preselected disclosure, obstructed cancellation, manufactured urgency, and confusing refusal paths as trust and autonomy risks. The [Dark Patterns at Scale study](https://dl.acm.org/doi/10.1145/3359183) provides a research-backed vocabulary for examining these patterns, especially in shopping flows.

## Research notes and limits

- NN/g’s current heuristic guidance describes heuristics as broad rules of thumb and says heuristic evaluation complements, rather than replaces, user research.
- NN/g recommends small iterative qualitative tests because repeated cycles can produce more useful learning than one large late study. Treat five participants as a starting pattern for qualitative work, not a universal sample-size law.
- GOV.UK guidance is unusually strong on the whole problem, question protocols, plain language, and one-thing-per-page form structure. Apply the reasoning where it fits the risk and task.
- WCAG 2.2 is the current W3C reference used here. Check the actual version and applicable legal requirements for the project before making a compliance claim.
- Google’s Core Web Vitals guidance recommends the 75th percentile for field interpretation and distinguishes real-user data from lab diagnostics.
