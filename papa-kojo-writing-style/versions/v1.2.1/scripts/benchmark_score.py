#!/usr/bin/env python3
"""Weighted writing quality score aggregator; it DOES NOT infer quality from text.

The input consists of identified human editorial ratings and separate truth gates.
Tested via public CLI acceptance scenarios. Stdlib only.
"""
import argparse
import json
import math
from collections import defaultdict
from pathlib import Path


def _validate_config(cfg):
    base = {k: v['weight'] for k, v in cfg['dimensions'].items()}
    if sum(base.values()) != 100 or any(v <= 0 for v in base.values()):
        raise ValueError('Base series weights must be positive and sum to 100')
    for name, w in cfg['lenses'].items():
        if sum(w.values()) != 100 or any(k not in base or v <= 0 for k, v in w.items()):
            raise ValueError(f'Invalid expert lens weights: {name}')
    return base


def _validate_record(z, keys, scale):
    required = ('id', 'version', 'task', 'format', 'text', 'reviewer', 'ratings', 'gate')
    if any(k not in z for k in required):
        raise ValueError('Missing record field')
    if not z['id'].strip() or not z['reviewer'].strip():
        raise ValueError('ID and reviewer required')
    if set(z['ratings']) != set(keys):
        raise ValueError(f"Invalid/missing dimension ratings for {z['id']}")
    if any(type(v) is not int or v < scale['min'] or v > scale['max'] for v in z['ratings'].values()):
        raise ValueError('Each series rating must be an integer 0-4')
    gates = z['gate']
    if set(gates) != {'verified','fabrication','material_misstatement','scope_failure'} or any(type(v) is not bool for v in gates.values()):
        raise ValueError('Gate requires four boolean fields')


def _score(ratings, weights, scale_max):
    return round(sum(ratings[k] * w for k,w in weights.items()) / scale_max, 2)


def score(data, cfg):
    keys = _validate_config(cfg); groups=defaultdict(list); seen=set()
    scale = cfg['scale']; maxscale=scale['max']
    for z in data['records']:
        _validate_record(z,keys,scale)
        sig=(z['id'],z['reviewer'])
        if sig in seen: raise ValueError(f'duplicate reviewer on draft: {sig}')
        seen.add(sig);groups[z['id']].append(z)
    res=[]
    for draft_id, arr in sorted(groups.items()):
        first=arr[0]
        if any(any(z[k]!=first[k] for k in ('version','task','format','text')) for z in arr):
            raise ValueError(f'conflicting draft content: {draft_id}')
        gate_fail=any(any(z['gate'][k] for k in ('fabrication','material_misstatement','scope_failure')) for z in arr)
        gate_unverified=any(not z['gate']['verified'] for z in arr)
        avg={k:sum(z['ratings'][k] for z in arr)/len(arr) for k in keys}
        series={k:{'rating':round(avg[k],2),'weight':keys[k],'score':round(avg[k]*keys[k]/maxscale,2)} for k in keys}
        status='blocked_truth_gate' if gate_fail else ('unverified_truth_gate' if gate_unverified else ('provisional_one_rater' if len(arr)==1 else 'two_raters_pending_reliability'))
        total=_score(avg,keys,maxscale) if not gate_fail and not gate_unverified else None
        lenses={name:_score(avg,weights,maxscale) for name,weights in cfg['lenses'].items()} if total is not None else {}
        if len(arr)>=2:
            disagreements={k:round(max(z['ratings'][k] for z in arr)-min(z['ratings'][k] for z in arr),2) for k in keys}
        else: disagreements=None
        res.append({'id':draft_id,'version':first['version'],'task':first['task'],'format':first['format'],
                    'text':first['text'],'reviewers':[z['reviewer'] for z in arr],
                    'status':status,'total':total,'series':series,'lenses':lenses,
                    'disagreement_span':disagreements})
    return {'benchmark':cfg['benchmark_id'],'version':cfg['version'],'results':res,
            'important_notice':'Scores reflect human ratings supplied in input. Expert lenses only reweight the same ratings; they are not separate tests or endorsements. Flesch scores are not part of this total.'}


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--config',required=True);p.add_argument('--input',required=True);p.add_argument('--output',required=True)
    a=p.parse_args(); cfg=json.loads(Path(a.config).read_text());data=json.loads(Path(a.input).read_text())
    res=score(data,cfg);out=Path(a.output);out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(res,indent=2,ensure_ascii=False)+'\n')
    print(f"Scored {len(res['results'])} drafts; provisional scores are not human-validated voice matches.")

if __name__=='__main__':main()
