#!/usr/bin/env python3
"""Original 3.0.3: dual readability diagnostics, never a voice verdict."""
import argparse
from collections import Counter
from functools import lru_cache
import json
from pathlib import Path
import sys

import adaptive_readability as base

VERSION = '1.1.0'
base.counter_for = lru_cache(maxsize=2)(base.counter_for)


def target(metrics, profile):
    lo, hi = base.TARGETS[profile]
    e, g = metrics['ease_estimate'], metrics['grade_estimate']
    if metrics['words'] < 100 or metrics['sentences'] < 5:
        return 'short_sample'
    if e < lo - 2:
        return 'review_difficulty'
    if e < lo:
        return 'near_target'
    if e > hi:
        return 'above_range_no_penalty'
    if profile == 'longform' and g > 6.5:
        return 'review_grade'
    return 'in_range'


def dual(text, profile='longform', protected=(), mode='auto'):
    h = base.analyze(text, profile, protected, 'heuristic')
    c = None
    if mode != 'heuristic':
        try:
            c = base.analyze(text, profile, protected, 'cmu')
        except ValueError:
            if mode == 'cmu':
                raise
    primary = c or h
    m = primary['metrics']
    e, g = m['ease_estimate'], m['grade_estimate']
    ss = base.sentences(text)
    count = base.counter_for(primary['dictionary'])
    # Whole-sentence windows; overlap and explicitly include a tail window.
    starts = list(range(0, max(1, len(ss)-9), 5))
    if ss and max(0, len(ss)-10) not in starts:
        starts.append(max(0, len(ss)-10))
    windows = []
    for start in sorted(set(starts)):
        chunk = ss[start:start+10]
        # Keep short windows as a local diagnostic rather than a grade verdict.
        w = base.metrics(chunk, count)
        if w['words']:
            windows.append({'start_sentence': start+1, 'end_sentence': start+len(chunk),
                            'short_sample': w['words'] < 100 or len(chunk) < 5, **w})
    windows.sort(key=lambda w: (w['ease_estimate'], w['start_sentence']))
    lens = [len(base.tokens(s)) for s in ss]
    run = longest = 0
    for n in lens:
        run = run+1 if n < 8 else 0
        longest = max(longest, run)
    delta = None if c is None or e is None else round(c['metrics']['ease_estimate']-h['metrics']['ease_estimate'], 1)
    strict = None if primary['short_sample'] else 80 <= e <= 95 and 4 <= g <= 6
    return {'version': VERSION, 'profile': profile, 'primary_dictionary': primary['dictionary'],
            'dictionary_available': c is not None, 'primary': m, 'heuristic': h['metrics'],
            'cmu': c['metrics'] if c else None, 'ease_difference': delta,
            'estimator_disagreement': delta is not None and (abs(delta) >= 5 or target(h['metrics'], profile) != target(m, profile)),
            'audience_status': target(m, profile), 'strict_grade5_target': strict,
            'hardest_windows': windows[:5], 'windows': windows,
            'hotspots': primary['hotspots'], 'longest_short_sentence_run': longest,
            'rhythm_review': longest >= 5,
            'notice': 'Estimates only. Short passages are local cues. Do not rewrite to chase thresholds or treat literal checks as semantic proof.'}


def review(before, after, profile='longform', protected=(), mode='auto', required=()):
    a, b = dual(before, profile, protected, mode), dual(after, profile, protected, mode)
    literal = base.compare(before, after, profile, protected, 'heuristic')
    missing = [term for term in required if term not in after]
    # Exact cues are advisory: changed negation/hedging can be legitimate.
    import re
    pattern = r"\b(?:not|never|no|cannot|can't|may|might|could|possibly|probably|only|unless|if|must|should|planned|approved|helped|led)\b"
    old, new = (Counter(re.findall(pattern, t.lower().replace('’', "'"))) for t in (before, after))
    x, y = a['primary']['ease_estimate'], b['primary']['ease_estimate']
    return {'before': a, 'after': b, 'ease_change': round(y-x, 1) if x is not None and y is not None else None,
            'literal_review': {k: literal[k] for k in ('review_required', 'protected_removed', 'protected_added', 'numbers_removed', 'numbers_added')},
            'missing_required': missing, 'scope_cues_removed': dict(old-new), 'scope_cues_added': dict(new-old),
            'editor_review_required': True, 'notice': 'A human or language model must compare claims, roles, certainty, causal links, tone and pacing. No automatic approval.'}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--profile', choices=base.TARGETS, default='longform')
    p.add_argument('--dictionary', choices=('auto','heuristic','cmu'), default='auto')
    p.add_argument('--protect', action='append', default=[])
    p.add_argument('--require', action='append', default=[])
    p.add_argument('--before', type=Path)
    args = p.parse_args()
    if any(not t.strip() for t in args.protect+args.require):
        p.error('terms must not be empty')
    if args.require and not args.before:
        p.error('--require needs --before')
    try:
        text = sys.stdin.read()
        opts = (args.profile, args.protect, args.dictionary)
        result = review(args.before.read_text(encoding='utf-8'), text, *opts, args.require) if args.before else dual(text, *opts)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except (OSError, ValueError) as exc:
        p.error(str(exc))


if __name__ == '__main__':
    main()
