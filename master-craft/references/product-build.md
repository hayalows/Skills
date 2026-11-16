# Building a product that holds up

Use this reference when the task is to make or substantially improve a site, web app, mobile app, dashboard or tool. It is the product pipeline Master Craft follows, with the skill that owns each stage and the evidence that ends it.

It works in standalone mode. Where a named skill is unavailable, the stage still applies: do it directly and say which specialist was missing.

## What "world class" means here

It is not a style and it cannot be promised. It is a set of things an outsider can check:

1. A first-time user can say what the product is for and finish the main task without help.
2. It works on a small phone, a large screen, a keyboard and a slow connection.
3. Every state a user can reach was designed: empty, loading, error, success, offline, no permission.
4. It looks like it was made for this subject, with one consistent visual system.
5. It tells the truth about cost, status, data and results.
6. It fails in ways a person can understand and recover from.
7. Another developer or agent can change it safely: clear structure, tokens, tests on the main journeys.
8. What was checked, and how, is written down. What was not checked is written down too.

If you cannot show one of these, the product is not there yet. Say which.

## Pick the lane

| You are making | Lead skill | Add when needed |
| --- | --- | --- |
| Web app, mobile app, PWA, dashboard, internal tool, multi-step flow | Product Design OS | Personal Craft (execution), tdd, domain-modeling, Product Evidence |
| Landing page, marketing site, portfolio, editorial site | Design Taste: Frontend | Frontend Design (visual direction), human-copywriting, Product Design OS for any form or flow on the page |
| Brand-new brand plus site | Lunour Brand Strategy first, then the row above | Lunour Naming |
| Improve an existing product | Website UX Audit to find the problems, then Product Design OS to fix them | diagnosing-bugs for defects |
| "Is it better?" or "Should we ship?" | Product Evidence | Model Assurance when numbers drive the decision |

One lead per stage. Do not load two design skills to do the same job.

## The pipeline

Each stage has an exit. Do not start the next stage on a guess when the exit can be checked.

### 0. Brief

Establish in a few lines: the user, the job they are finishing, the outcome that counts as success, the platform, the constraints, and what is out of scope. Write the problem as one sentence:

`[User] needs to [outcome] in [context], but [friction] makes that difficult.`

Infer reversible details from the project. Ask one focused question only when the answer changes the direction or grants an authority you do not have.

**Exit:** a brief the user would recognise as their own request, with assumptions labelled.

### 1. Shape

Decide the smallest version that would still be good. Good and small beats large and thin.

- Name the one core journey. Everything else waits.
- Map that journey: entry, steps, decisions, data, states, exits.
- Name the biggest risk (unclear need, hard interaction, unknown API, data model) and deal with it first. Use the prototype skill when a cheap experiment answers it.
- Choose the stack: the project's existing stack, always. For a new project with no stated preference, choose the plainest option that fits: static HTML and CSS for a simple site, one mainstream framework for an app. Add a dependency only for a concrete need.
- For multi-session work, write a short spec (to-spec) and split it into slices (to-tickets). For one-session work, a list is enough.

**Exit:** one core journey, a list of slices in build order, the main risk named.

### 2. Design

Lead: Product Design OS (apps and flows) or Design Taste: Frontend (marketing pages).

- Hierarchy for each screen: one purpose, one primary action.
- States for each component the journey touches.
- A written visual direction and a token file. Reuse the existing system when there is one.
- Accessibility requirements stated before build, not after.

**Exit:** a direction note, tokens, and a state list for the first slice. For a small job this is a few lines, not a document.

### 3. Build the first slice

Lead: Personal Craft for execution discipline, plus the project's own conventions.

- Build the core journey end to end, narrowest screen first, with real content.
- Follow the user's test policy in Personal Craft verification: choose the behaviour checks before writing the behaviour, prefer end-to-end journey checks, add no retrospective unit tests without the documented exception.
- Keep the diff small and inside scope. Preserve unrelated code and existing contracts: URLs, data formats, analytics, keyboard behaviour.

**Exit:** the journey runs locally from entry to success, including its error and empty states.

### 4. Look

This stage is what separates good from generic. Do not skip it.

- Run `node product-design-os/scripts/ui-lint.mjs <path>` and fix every error.
- Render the page. Capture it at 360, 768 and 1280 wide.
- Look at each capture as a first-time user. Operate the keyboard path, zoom, empty, error, slow network and double submit.
- Score the ten-dimension rubric in Product Design OS. Fix anything below its floor. Render again.

Expect two or three passes.

**Exit:** rubric with evidence, every floor met, or a plain statement of what could not be seen in this environment.

### 5. Harden

Apply the gates that this product needs, in proportion:

- **Accessibility:** keyboard, focus, names, contrast, reflow, reduced motion.
- **Performance:** measured on a throttled mobile profile for pages that matter. Record conditions.
- **Security and privacy:** server-side authorisation, no secrets in the client or the repository, validated input, least data collected. Use Security Audit only for an explicit request or a real identified trust-boundary risk, under its own isolation rules.
- **Resilience:** timeouts, retries that cannot double-charge or double-post, kept input, clear recovery.
- **Review:** read the actual diff. Use code-review for consequential changes.

**Exit:** each relevant gate marked passed, failed or not verified, with the evidence.

### 6. Ship

Only when the user asked for it. Building is not permission to publish.

- Confirm the target: host, account, project, branch, domain.
- For Vercel, read Vercel Deployment Steward before any hosted build, preview or release. For other hosts, inspect their real configuration.
- Publish once, through the intended path. Then verify the live revision and the core journey on the real domain.

**Exit:** one of NOT REQUESTED, NOT ATTEMPTED, BLOCKED, PUBLISHED AND VERIFIED, PUBLISHED BUT UNVERIFIED.

### 7. Learn

A product is not finished at launch.

- Pick one outcome that shows the product works for users, and make sure it can be observed.
- Use Product Evidence to compare before and after or to judge a rollout.
- Write down what to look at first when real usage arrives.

**Exit:** one named measure and where to read it.

## Then widen

Add the next slice and run stages 2 to 5 again. Keep the token file and the direction note as the source of truth so slice five still looks like slice one.

## Sizing

| Job | Stages |
| --- | --- |
| Small fix on an existing screen | 3 and 4 only: change it, look at it |
| One new screen or component | 0 in a line, then 2 to 4 |
| New feature or flow | 0 to 5 |
| New product or full rebuild | 0 to 7, slice by slice |
| Audit only | 0, then findings. No build, no ship |

## Ways this goes wrong

- Designing every screen before building one. Build one slice and learn from it.
- Polishing the first screen while the journey is still broken further on.
- Skipping the look stage because the code "should" be right.
- A new visual style on every screen because no direction was written down.
- Shipping the happy path and calling the missing states "later".
- Reporting tests, user studies or a live deployment that did not happen.
- Adding features nobody asked for in the name of quality. Raise the standard, not the scope.
