# Threadline 0.1: Natural Prose Research Lab

A **new, independent, general-purpose** research prototype for producing prose that reads naturally and remains accurate. It is not built on any existing user writing style. It is also **not** a trained language model. It is a repeatable writing method, a model-neutral prompt generator, a lightweight diagnostic CLI, a source manifest, and a blind evaluation protocol.

## Contents

- `research_report.md` — research findings, evidence, source limitations.
- `model_spec.md` — nine-stage model and design rationale.
- `sources_conference_2026.csv` — 70 full official 2026 conference transcript pages, with derived structural measurements; 66 substantive addresses.
- `sources_other.csv` — devotionals, essayists, company guides and research, with access status.
- `threadline.py` — no-dependency Python 3 tool to compile prompts and review text.
- `example_brief.json` — neutral brief used for a reproducible demonstration.
- `evaluation_protocol.md` — rigorous, blinded, human-rated evaluation including longer writing.
- `tests/`, `fixtures/`, `benchmark_results.json` — reproducible function tests and diagnostic smoke tests.

## Quick start

```bash
python threadline.py prompt example_brief.json --output threadline_prompt.txt
python threadline.py prompt example_brief.json --baseline --output baseline_prompt.txt
python threadline.py analyze fixtures/templated.txt
python threadline.py analyze fixtures/grounded.txt
python threadline.py compare fixtures/templated.txt fixtures/grounded.txt
python -m unittest discover -s tests -v
```

Paste `threadline_prompt.txt` into ChatGPT, Claude, or another model to draft according to the new method. It does not require access to your existing writing skill. For an existing draft:

```bash
python threadline.py prompt example_brief.json --revise my_draft.txt --output revision_prompt.txt
```

Optional paid/API operation:

```bash
# Set OPENAI_API_KEY securely in your shell first; never paste it into the JSON file.
python threadline.py generate example_brief.json --model MODEL_YOU_HAVE_ACCESS_TO --output model_result.txt
```

The API path uses OpenAI's Responses API. It wasn't live-tested because no API key is provided to this project. Model availability and billing depend on your account. Its prompt builder and diagnostics have been tested locally without any service call.

## Honest test status

Thirteen unit tests pass and the static diagnostics correctly identify several deliberately inserted stock-phrase and repetition fixtures. This **does not** prove that Threadline makes unseen AI outputs more natural. That would require paired generation using the same model and sources, blind human assessments and a held-out evaluation, described in `evaluation_protocol.md`.

## Boundaries

- No existing or personal writing style was read, used or updated.
- No proprietary model weights were trained.
- Published articles and conference transcripts were studied through the secondary Firecrawl connection, but **their full copyrighted text is not packaged**. Only links, titles and derived statistics are distributed.
- The corpus is heavily weighted toward prepared religious addresses and essayists. It is not a representative sample of all human writing.
- Readability and cadence metrics are observational. The model does not assume all natural prose needs to score a particular grade.
