#!/usr/bin/env python3
"""Advisory review of example framing in Original v3.0.4."""
import argparse
import json
import re
import sys
from adaptive_readability import sentences

VERSION = '1.0.0'
REGISTERS = ('chat', 'comment', 'message', 'post', 'longform', 'formal')
PATTERNS = {
    'detached_take': r'^take\s+(?:the case of\b|(?:a|an|the)\s+[^.!?]{1,65}\b(?:that|who|which|with|for example)\b)',
    'detached_say': r'^say\s+(?:i|you|we|someone|somebody|a person|a friend|a shop|a company)\b',
    'formal_setup': r'^(?:consider|imagine)\s+(?:a|an|the)\s+(?:scenario|hypothetical|situation|example|case)\b',
}
INVITE = re.compile(r"^(?:so[, ]+)?(?:let us|let['’]s)\b", re.I)


def prose(text):
    # Remove common literal spans, not the surrounding original prose.
    text = re.sub(r'(?ms)^\s*```[^\n]*\n.*?^\s*```[^\n]*', '\n', text)
    text = re.sub(r'(?m)^\s*>[^\n]*', '', text)
    text = re.sub(r'`[^`\n]+`|“[^”\n]+”|"[^"\n]+"', ' ', text)
    return text


def review(text, register='longform'):
    flags = []
    ss = sentences(prose(text))
    def add(kind, i, advice):
        flags.append({'id': kind, 'sentence': i+1, 'text': ss[i], 'advice': advice})
    # Personal explanatory prose is the scope of this correction. Instructions,
    # messages, quotations and formal reports do not need extra reader address.
    if register in ('longform', 'post'):
        invitations = []
        for i, s in enumerate(ss):
            opening = re.sub(r'^(?:so[, ]+)', '', s.strip(), flags=re.I)
            for kind, pattern in PATTERNS.items():
                if re.match(pattern, opening, re.I):
                    add(kind, i, 'Review if this is an illustrative setup. Connect it to the thought, use a shared example if natural, or keep a real instruction.')
                    break
            if INVITE.match(s.strip()):
                if invitations and i-invitations[-1] <= 4:
                    add('repeated_invitation', i, 'Review nearby repeated invitations; use a direct example or continuation when it reads better.')
                invitations.append(i)
            if i >= 2 and all(x.rstrip().endswith('?') for x in ss[i-2:i+1]):
                add('question_run', i, 'Review whether these questions help the reader or merely create rhythm. Keep genuine questions.')
    return {'version': VERSION, 'register': register, 'sentences_scanned': len(ss),
            'flags': flags, 'notice': 'Candidates only. No replacement, authorship score or forced reader address. Review quotations, actual instructions and register in context.'}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--register', choices=REGISTERS, default='longform')
    p.add_argument('--review-gate', action='store_true', help='Exit 2 when candidates need editorial review')
    a = p.parse_args()
    result = review(sys.stdin.read(), a.register)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 2 if a.review_gate and result['flags'] else 0


if __name__ == '__main__':
    sys.exit(main())
