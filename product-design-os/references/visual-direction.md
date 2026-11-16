# Visual Direction: Choosing a Look on Purpose

Use this reference when a new surface needs a visual identity, when an existing one reads as a template, or when someone asks for work that looks "premium", "modern" or "world class".

Those words are not a direction. A direction is a small set of decisions you can state, defend and repeat on the next screen.

## 1. Decide whether a new direction is allowed

| Situation | What to do |
| --- | --- |
| The product has a brand or design system | Use it. Improve hierarchy, spacing and states inside it. Propose changes to the system separately |
| An existing product with no written system | Extract what is already there (colours, type, radius, spacing) into tokens first. Tidy before you restyle |
| A new product or page with no brand | Set a direction with the steps below |
| A redesign was requested | Keep what users already recognise unless there is evidence it hurts them |

Never restyle an approved brand because a different look seems nicer.

## 2. Match loudness to the surface

Different surfaces need different amounts of personality.

| Surface | Personality | Why |
| --- | --- | --- |
| Tool used for hours: dashboard, admin, editor, back office | Quiet. One accent, neutral surfaces, dense and calm | The content is the interface. Decoration costs attention all day |
| Task flow: checkout, signup, booking, payment | Quiet and reassuring. Personality in copy and small details | Trust and completion matter more than delight |
| Consumer app home, onboarding, empty states | Moderate. One recognisable element | First impressions and memory |
| Landing page, portfolio, campaign, launch | As loud as the subject deserves | The page has seconds to say what this is and why it is different |

A common failure is putting landing-page drama into a tool, or tool-grade plainness on a landing page.

## 3. Find the direction in the subject

Do not start from a palette. Start from the thing itself.

1. **Name the subject in one line.** What it is, who it is for, and the one job of this surface.
2. **List what belongs to its world.** Materials, instruments, documents, places, sounds, rituals, the vocabulary people already use. A fuel-tracking tool has receipts, pump displays, odometers. A tailoring shop has chalk lines, measuring tape, fabric swatches.
3. **Pick three words for the feeling** that the audience should have, and one word it must never feel. "Calm, exact, local. Never corporate."
4. **Choose one signature.** The single thing people will remember: a type treatment, a number style, a shape, an illustration approach, a motion, a layout idea. One is enough. Everything else stays disciplined so the signature can be seen.

If the three words would fit any product in the category, they are too generic. Try again.

## 4. Set six dials

Write one line for each. This is the whole direction.

| Dial | The choice | Notes |
| --- | --- | --- |
| **Type voice** | Families for display, body and numbers, plus the scale | Type carries most of the personality. One family with good weights is often enough. Check that it covers the languages and symbols you need, including currency signs |
| **Colour** | Neutral family (warm, cool or true grey), one accent, and state colours | Name 4 to 6 values with their roles. State colours (danger, success, warning) stay separate from the brand accent |
| **Density** | Compact, comfortable or spacious | Follows the task. Data work is compact. Reading and marketing are spacious |
| **Shape** | Corner radius, border weight, how surfaces separate (line, tint or shadow) | Pick one separation method as the default. Mixing all three looks noisy |
| **Imagery** | Photography, product screenshots, illustration, data, or none | Real beats stock. A typographic design with no imagery is a valid choice |
| **Motion** | None, functional only, or expressive | Functional motion explains a change of state. Expressive motion belongs on loud surfaces only |

Put the result into tokens. Start from `assets/tokens.css` and change values. Do not scatter literal colours and sizes through components.

## 5. Check it is a choice and not a default

Machine-made design clusters around a few looks. They are not wrong, but they appear regardless of subject, which is how people recognise them.

Ask of your direction: **would this exact look have come out for a different product in a different category?** If yes, it is a default. Change the dial that is least tied to the subject.

Signs of an unconsidered default:

- a purple or blue gradient behind a centred headline and two buttons
- a cream background with a serif headline and a terracotta accent
- a near-black page with one neon accent
- three identical cards with an icon, a title and two lines of text
- a big number with a small label used as decoration instead of information
- rounded cards with soft shadows on a grey page, everywhere, at one size
- numbered labels (01, 02, 03) on things that are not a sequence
- emoji used as icons
- glass blur, glow and gradient borders with no meaning
- every section animating in on scroll

When the brief asks for one of these looks, do it well. The brief wins. The problem is only the look you reached for without deciding.

## 6. Rules that keep any direction looking professional

These hold whatever the style.

- **One dominant thing per view.** Squint. If three things compete, demote two.
- **Few sizes, clearly different.** Adjacent type sizes should differ by a visible step. Five sizes on one screen is usually the limit.
- **Hierarchy from weight and colour before size.** A muted label next to a strong value reads better than two sizes.
- **Space shows grouping.** Related things sit closer than unrelated things. The gap inside a group is smaller than the gap between groups, always.
- **Align to a few edges.** Count the left edges on a screen. Fewer is calmer.
- **Line length 45 to 75 characters** for paragraphs. Tight line-height for big headings, looser for body.
- **Numbers that are compared use tabular figures** and align on the decimal or the right.
- **Accent colour is scarce.** If more than about a tenth of the screen is the accent, it stops meaning "act here".
- **One radius family, one shadow family.** Nested corners use a smaller radius inside.
- **Real content.** Real names, real numbers, real lengths. Placeholder text hides every problem that matters.
- **Icons from one set**, one stroke weight, with text labels unless the meaning is universal.

## 7. Write the direction down

A short note is enough. It lets the next screen, the next agent and the next week stay consistent.

```text
Direction: [name]
Subject: [what, who, one job]
Feels: [three words]. Never: [one word].
Signature: [the one memorable element]
Type: [families, scale]
Colour: [neutral, accent, states, with values]
Density / shape / imagery / motion: [one line each]
Why this fits: [one or two sentences tied to the subject]
```

Do not claim a direction is original or will perform better. State why it fits, build it, then look at it (see `build-and-verify.md`).
