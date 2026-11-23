# Writing Version Lab: future-proof version registration

This benchmark registry is **separate from the official writing skill**. It identifies which instructions are available for fair comparison. It does **not** produce writing samples, claim that a version passed, or calculate a personal-voice ranking.

## Currently discovered from the repository

- `current-main`: active v3.0 Original skill
- `v1.2.1`: complete archived approved version
- `v3.1-close-to-speech`: selectable v3.1
- `steady-voice-v3.2`: selectable Steady Voice (declared revision 3.2.0)
- `v1.0`, `v1.1`, `v1.2`: historical Git snapshots, when full commit history is available

Unmerged or unpublished v1.3, v1.4, v1.2.2, and v1.2.1.1 drafts are **not** reconstructed from descriptions or previous AI outputs. Supply exact local SKILL files with repeated `--extra ID=PATH` flags. Threadline is a general-purpose writing method, not a version of Papa Kojo's personal voice; test it as a clearly separate comparator.

## Run

```bash
python3 papa-kojo-writing-style/benchmarks/version-lab/autoregister.py \
  --repo . --out /tmp/pkm-version-manifest.json
python3 -m unittest papa-kojo-writing-style/benchmarks/version-lab/test_autoregister.py -v

# Add an experimental draft only when the exact source exists:
python3 papa-kojo-writing-style/benchmarks/version-lab/autoregister.py \
  --repo . --extra v1.2.2=/path/to/v1.2.2/SKILL.md \
  --out /tmp/with-experiments.json
```

Every candidate has a source path, a SHA-256 hash, a declared version where present, and separate `generation` and `evaluation` statuses. These remain `pending` until genuine matched drafts have been collected and independently evaluated.

## Future versions

Place each future selectable version in `papa-kojo-writing-style/versions/<new-name>/SKILL.md`. On the next registry run it will appear automatically. Updating the active `SKILL.md` also changes its SHA-256, providing a way to identify changes even if the declared version stays unchanged. To retain two versions for comparisons, archive the old default before replacing it.

The workflow `writing-version-inventory.yml` runs this inventory and its tests on relevant pushes and pull requests, and stores the resulting manifest as a CI artifact. **It does not call an AI model, spend generation credits, rate prose, or update the live writing skill.**

## How to compare writing fairly

1. Freeze new, unseen briefs before reading any fresh samples, with a fixed facts packet and explicit word ranges.
2. For each candidate and each brief, generate three separate outputs with the same model, release, effort, temperature if applicable, and token budget. Record provider response IDs, model settings, prompt hash, skill hash and independent-call evidence.
3. Apply exact-check gates for changed actors, invented outcomes, changed dates, numbers, quotations, commitments and uncertainty before judging style.
4. Evaluate naturalness, ease of reading, thought development, emotional care, hooks, register and useful endings separately. Read long pieces by opening, middle and ending.
5. Use shuffled, reversed A/B orders and multiple independent evaluators. Automated readability is a **diagnostic**; a model rating its own drafts cannot settle personal voice. Treat Papa Kojo's direct approval as the strongest available evidence of sounding like him.
6. Report results by genre and variation across briefs. Do not rank a candidate if no valid generated writing is available.

The earlier Kitchen Table results are historical context, not the labels or grades for a new comparison. Any new candidate starts untested.
