# Constrained Contexts: Budget Phones, Metered Data, Unreliable Networks

Use this reference when a meaningful share of users are on low-cost Android phones, pay for data by the megabyte, share devices, or lose connection during the day. This describes much of the world, including most mobile-first markets.

A product that only works on a new phone with fast Wi-Fi is not finished. It is untested.

The numbers below are starting assumptions. Replace them with real figures for your users as soon as you have analytics or field measurements.

## 1. Know the real conditions

Find out, or state your assumption, for each of these before designing:

| Question | Why it changes the design |
| --- | --- |
| Typical device: screen width, memory, processor class | Decides layout floor, animation budget and how much JavaScript is tolerable |
| Typical connection and how often it drops | Decides caching, retry and offline behaviour |
| Who pays for data and how much it costs them | Decides image weight, autoplay, background sync |
| Browser or app, and which version | Decides which platform features are safe to rely on |
| Shared device or shared SIM | Decides session length, sign-out, what is shown on screen |
| Languages, literacy range, and number formats | Decides copy, icons with labels, currency and date display |
| How people pay | Decides the checkout flow. Mobile money, cash on delivery and bank transfer behave differently from cards |

## 2. Design rules

**Layout**

- Support 320px wide. Treat 360px as the common case.
- Put the primary action where a thumb reaches it without stretching.
- Keep working layouts when the on-screen keyboard covers half the screen. The focused field and its error must stay visible.
- Sunlight washes out low contrast. Prefer strong contrast and avoid thin, light type.

**Weight**

- Send text and the main action first. Images, fonts and extras come after.
- Use the system font stack unless a brand font is essential. If it is, load one or two weights, subset them, and let text show in a fallback first.
- Serve images at the size they are displayed, in a modern format, with width and height set. Load below-the-fold images lazily.
- Do not autoplay video. Do not preload media the user did not ask for.
- Prefer server-rendered or static pages for content. Ship JavaScript for interaction, not for showing text.
- Question every third-party script. Each one costs data and battery on every visit.

**Network**

- Show a response to every tap at once, before the network answers.
- Never lose what the user typed. Keep form input locally until the server confirms.
- Make submit actions safe to repeat. A retried payment or order must not happen twice.
- Tell the user plainly when they are offline, what still works, and what will be sent when the connection returns.
- Cache what was already loaded so a revisit works without a connection where the task allows.
- Timeouts need a clear message and a retry control, not an endless spinner.

**Data respect**

- Say how large a download is before it starts.
- Offer a lighter mode when the product is media-heavy.
- Do not sync or refresh in the background without a reason the user would agree with.

## 3. Payments and trust

Money flows fail in specific ways on mobile networks. Design for them.

- Show the full amount, fees and recipient before the user confirms. No surprises after.
- When payment is approved on another screen or by a prompt on the phone, say exactly what will happen next and what to do if the prompt does not arrive.
- After the user approves, show a clear pending state. Do not show failure just because confirmation is slow.
- Give every transaction a reference the user can quote, and a place to check its status later.
- If a payment outcome is unknown, say so, and tell the user not to pay again until it is resolved.
- Send or show a receipt the user can keep.
- Ask for the minimum personal information. Explain why each sensitive item is needed.

## 4. Language and comprehension

- Short, common words. One idea per sentence.
- Label icons with text.
- Show money, dates and phone numbers in the local format, and accept the formats people actually type.
- Avoid idioms and jokes that do not translate.
- Test copy with someone outside the team.

## 5. Starting budgets

Use these when no data exists yet, then tune.

| Item | Starting budget |
| --- | --- |
| First load, compressed, critical path | Under about 200 KB |
| JavaScript on first load, compressed | Under about 100 KB for content pages |
| Largest image on first screen | Under about 100 KB |
| Web fonts | None, or one family and two weights |
| Time to useful content on a slow connection | A few seconds, with something meaningful visible early |
| Response to a tap | Visible feedback within about 100 ms |

These are design budgets, not standards. Measure the built page on a throttled mobile profile and record the conditions (see `build-and-verify.md`).

## 6. Test like the user

- Throttle the network to slow 3G and the processor to a low-end profile in browser developer tools.
- Turn the network off halfway through the main task.
- Fill a form, lose connection, reconnect, and submit.
- Use the page at 320px with the keyboard open.
- Where possible, try a real low-cost Android phone. Emulation hides jank and heat.

Report which of these were done and which were not. Emulated results are not field results.

## 7. Common failures

- A hero image or video that costs more data than the rest of the site combined
- A blank screen until a large script bundle arrives
- A spinner with no timeout and no retry
- A form that clears itself after a failed submit
- A payment that shows "failed" while the money has left the account
- Text over photographs that cannot be read outdoors
- Sign-up walls before any value is shown
- An install prompt or notification request on first visit
- Features that silently need the newest browser
