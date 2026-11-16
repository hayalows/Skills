# Papa Kojo Writing Blind Lab

A private, four-way pilot comparing writing samples informed by v1.0, v1.1, v1.2 and an uncommitted v1.3 draft.

## How it works

- This folder is deployed as an independent Vercel site (root directory `apps/writing-blind-lab`). It does not change the Skills catalogue.
- The participant receives a private link with an access key in the URL fragment. The key is kept in that browser's local storage and is never included in the public GitHub source.
- Selections and ratings are saved automatically to an isolated, RLS-protected `pkm_voice_blind_runs` table via the `pkm-blind-lab` Supabase Edge Function.
- The Edge Function validates the private access key and stores summary statistics as soon as 24 situations have answers.
- The private version-to-option mapping exists only in the Edge Function, not in the participant page. Do not add it here.
- `Download backup` is optional. The existing import button supports earlier offline JSON exports, useful when moving from a local HTML file to the live domain.

## Privacy and limitations

The anonymous drafts are visible in the website's HTML source. Do not place private unapproved personal writing, tokens or sealed answer keys in this public repository. Participant responses are accessible only through the separate authenticated storage endpoint and authorised administrator tools. A browser that loses both its access link and local-storage token cannot recover the private link automatically.

This is a **single-model, version-conditioned pilot**, not proof that separate model runs under each version would produce the same preferences. Readability and AI-detection measures are not proof of authentic personal voice.

## Technical boundaries

- Frontend: static HTML, JavaScript and local browser backup.
- Backend: Supabase Edge Function `pkm-blind-lab` on a pre-existing project, with custom high-entropy bearer access and a single isolated database table.
- The service-role key and private version mapping are never included in this repository.
- No automatic ChatGPT wake-up or webhook is claimed. The server calculates the descriptive report automatically; ChatGPT can retrieve it through the connected Supabase app when asked, or through a separately configured scheduled monitor.
