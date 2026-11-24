# Independent Voice Checker 1.0.0

A separate evaluator for Papa Kojo's writing. It does not load or modify the active skill, write prose, or decide which draft sounds like its author. This is an initial experimental release, not a validated replacement for Original's own checks.

This implementation builds on the user's feedback, the Gemini-supplied v4.1 design (broader illustrative setups, common-word syllable exceptions, lexical and rhythm diagnostics, written numbers and scope cues), and the frozen Original v3.0.4 tools. The four baseline modules are copied from commit `43a1d69a840a64d8aed4a1d288c5fe18fbb5ab95` into this directory for reproducible comparisons; no active skill imports are required. The new checker uses the baseline metric formulas and style vocabulary, so it is operationally separate, not statistically independent of the skill.

## Usage (Python 3.9+)
```sh
python3 independent-voice-checker/pk_checker.py --profile longform < draft.txt
python3 independent-voice-checker/pk_checker.py --profile educational --dictionary auto < article.txt
python3 independent-voice-checker/pk_checker.py --before draft.txt --protect "C++" --require "cap" --review-gate < revision.txt
python3 -m unittest discover -s independent-voice-checker/tests -v
python3 independent-voice-checker/benchmarks/run.py
```

Default JSON output includes primary and heuristic readability metrics, optional CMU results, local reading windows, paragraph reports, review words, rhythm and MATTR-100. CMU is optional; without it auto explicitly reports heuristic. Fog is an unadjusted estimate, not full Gunning Fog proper-name/inflection handling. SMOG requires at least 30 sentences. The original frozen estimator remains available in baseline/adaptive_readability.py for historical comparisons. This is a new measurement protocol, not directly interchangeable with earlier scores. Exact terms and numbers are tracked separately from raw readability. Composition and review gates return 2 for review candidates (not automatic failure); invalid input returns a CLI error. Review gate covers style and revision warnings. No automatic replacements.

## Known limits
- Example framing and list detection are deliberately advisory heuristics. A necessary list, a formal mathematical hypothetical, or a genuine imperative can remain. Quoted and fenced code spans are omitted from style checks, with limited Markdown parsing.
- Number checks retain signs, common currency/unit notation, percentages and written-number tokens; context changes prompt review even when counts match. They do not parse every quantity or arithmetic expression. Digit/word representations are not automatically equivalent. Scope cues normalize common contractions but cannot resolve semantics. Exact required phrases are case-sensitive and checked with outer token boundaries; protected counts include all occurrences. Actor swaps, subtle changes in certainty and factual errors can still escape. Always compare meaning and source facts manually.
- Pronunciation and sentence splitting are estimates, especially for names, acronyms and mixed-language text. There is no universal readability target. No score or flag establishes authorship.
- Development fixtures are synthetic and intentionally cover known failures. Passing these is regression evidence, not held-out performance or human preference evidence. Do not tune and then call the same data independent. Freeze new evaluator versions and future evaluation sets before assessing new writing versions.

## Versioning
1.0.0: independent companion, baseline snapshots, advisory composition/conversation checks, optional dual readability, literal preservation diagnostics, regression suite and reproducible baseline comparison. Keep the Original skill unchanged.
