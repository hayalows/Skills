#!/usr/bin/env python3
"""Reproducible long-form writing protocol, diagnostics and evidence-checked human scoring.

This does NOT generate drafts, call an LLM, or infer whether text is human.
It prepares isolated requests for an external model runner and verifies review data.
Standard library only.
"""
import argparse
import hashlib
import json
import random
import re
import statistics
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SEED = 20261116
WORDS = re.compile(r"[A-Za-z]+(?:['’][A-Za-z]+)?")
END = re.compile(r"(?<=[.!?])\s+|\n\s*\n")


def canonical(obj):
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(',', ':'))


def sha(obj):
    return hashlib.sha256(canonical(obj).encode()).hexdigest()


def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def write(path, obj):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def sentences(s):
    s = re.sub(r'(?<=\d)\.(?=\d)', '∯', s)
    s = re.sub(r'\b(Mr|Mrs|Ms|Dr|Prof|St)\.', r'\1∯', s)
    return [p.replace('∯', '.').strip() for p in END.split(s) if WORDS.search(p)]


def syllables(word):
    w = word.lower().strip("'’")
    if len(w) <= 3:
        return 1
    w = re.sub(r'(?:[^laeiouy]es|ed|[^laeiouy]e)$', '', w)
    w = re.sub(r'^y', '', w)
    return max(1, len(re.findall(r'[aeiouy]{1,2}', w)))


def metrics(text, window_words=400):
    ws = WORDS.findall(text)
    ss = sentences(text)
    if not ws or not ss:
        return {'word_count': len(ws), 'sentence_count': len(ss), 'reading_ease_estimate': None,
                'flesch_grade_estimate': None, 'window_reading_ease_estimates': []}
    n, s, syll = len(ws), len(ss), sum(syllables(w) for w in ws)
    ease = 206.835 - 1.015 * n/s - 84.6 * syll/n
    grade = 0.39 * n/s + 11.8 * syll/n - 15.59
    paragraphs = [p.strip() for p in re.split(r'\n\s*\n', text) if WORDS.search(p)]
    windows, buf, count = [], [], 0
    for p in paragraphs:
        buf.append(p)
        count += len(WORDS.findall(p))
        if count >= window_words:
            windows.append('\n\n'.join(buf))
            buf, count = [], 0
    if buf:
        if windows and count < window_words//2:
            windows[-1] += '\n\n' + '\n\n'.join(buf)
        else:
            windows.append('\n\n'.join(buf))
    win_ease = []
    for w in windows:
        wws, wss = WORDS.findall(w), sentences(w)
        if not wss or not wws:
            continue
        v = 206.835 - 1.015 * len(wws)/len(wss) - 84.6 * sum(syllables(t) for t in wws)/len(wws)
        win_ease.append(round(v, 1))
    return {'word_count': n, 'sentence_count': s, 'paragraph_count': len(paragraphs),
            'avg_sentence_words': round(n/s, 1), 'avg_syllables_per_word_estimate': round(syll/n, 2),
            'reading_ease_estimate': round(ease, 1), 'flesch_grade_estimate': round(grade, 1),
            'window_reading_ease_estimates': win_ease,
            'minimum_window_reading_ease_estimate': min(win_ease) if win_ease else None,
            'window_spread_estimate': round(max(win_ease)-min(win_ease), 1) if len(win_ease)>1 else 0}


def prepare(out):
    spec = read(ROOT/'tasks.json')
    rubric = read(ROOT/'rubric.json')
    assert len(spec['versions']) == 4 and len(spec['tasks']) == 8
    assert sum(d['weight'] for d in rubric['dimensions'].values()) == 100
    rng = random.Random(SEED)
    entries = []
    for task in spec['tasks']:
        cases = [(v, rep) for v in spec['versions'] for rep in range(1, spec['independent_runs_per_prompt']+1)]
        rng.shuffle(cases)
        for v, rep in cases:
            entries.append({'id': f'D{len(entries)+1:04}', 'task_id': task['id'], 'split':task['split'],
                            'version': v['key'], 'source':v, 'repeat': rep,
                            'prompt_hash': sha(task),
                            'model_settings_required': spec['same_model_settings'],
                            'instruction': 'Start a FRESH independent model call. Load ONLY this version of the writing skill, including its relevant reference files. Read the common task exactly. Do not look at other drafts, candidate names, earlier completions, ratings or style revisions. Record provider response ID and model settings. Never invent autobiography or doctrine. Produce an essay in the word range. No reviewer or secret version markers in the writing.',
                            'prompt': task})
    rng.shuffle(entries)
    public = [{'id':x['id'], 'task_id':x['task_id'], 'split':x['split'],
               'prompt_hash':x['prompt_hash']} for x in entries]
    out.mkdir(parents=True, exist_ok=True)
    write(out/'private_generation_requests.json', {'status':'prepared_only_no_model_calls', 'requests':entries})
    write(out/'reviewer_blind_manifest.json', {'status':'prepared_only', 'candidates':public,
                                               'instructions':'Keep private_generation_requests.json away from all reviewers. Outputs must not include version names.'})
    write(out/'status.json', {'planned_requests':len(entries), 'generated_independent_drafts':0,
                             'scored_human_reviews':0, 'winner':None, 'notice':'A prepared request is not an independently generated essay or rated result.'})
    (out/'drafts').mkdir(exist_ok=True)
    (out/'calls').mkdir(exist_ok=True)
    print('Prepared',len(entries),'blind candidates. 0 essays generated; 0 human ratings. No winner.')


def audit(folder):
    source = read(folder/'private_generation_requests.json')
    spec = read(ROOT/'tasks.json')
    task_map = {t['id']:t for t in spec['tasks']}
    report, call_ids, settings, failures = [], set(), set(), []
    for job in source['requests']:
        id = job['id']
        p = folder/'drafts'/f'{id}.txt'
        m = folder/'calls'/f'{id}.json'
        if not p.exists() or not m.exists():
            continue
        text = p.read_text(encoding='utf-8')
        meta = read(m)
        if meta.get('independent_model_call') is not True:
            failures.append(id+': generation independence not attested')
        if meta.get('prompt_hash') != job['prompt_hash']:
            failures.append(id+': common prompt hash mismatch')
        if meta.get('version') != job['version']:
            failures.append(id+': version provenance mismatch')
        if not meta.get('provider_response_id') or meta['provider_response_id'] in call_ids:
            failures.append(id+': no unique provider response id')
        call_ids.add(meta.get('provider_response_id'))
        if not all(k in meta for k in ('model','temperature','top_p')):
            failures.append(id+': missing model settings')
        else:
            settings.add((meta['model'], str(meta['temperature']), str(meta['top_p'])))
        nums = metrics(text)
        low, high = task_map[job['task_id']]['min_words'], task_map[job['task_id']]['max_words']
        if not (low <= nums['word_count'] <= high):
            failures.append(id+f": word count {nums['word_count']} outside {low}..{high}")
        report.append({'id':id,'task_id':job['task_id'],'version_private':job['version'],'diagnostics':nums})
    if len(settings)>1:
        failures.append('Across-version model settings differ: paired design invalid.')
    data = {'status':'complete' if len(report)==len(source['requests']) and not failures else 'incomplete_or_invalid',
            'generated_drafts':len(report),'planned_drafts':len(source['requests']),
            'errors':failures,'readability_is_advisory':True,'diagnostics_PRIVATE':report}
    write(folder/'private_generation_audit.json', data)
    print(f"Audited {len(report)}/{len(source['requests'])} generated essays. {len(failures)} provenance/length problems.")
    if failures:
        print('Sample issues:', failures[:3])
    return data


def validate_review(row, rubric, fulltext):
    dims = rubric['dimensions']
    expected = set(dims)
    if set(row.get('ratings', {})) != expected:
        raise ValueError('All 13 editorial ratings are required')
    quoted = []
    for k, v in row['ratings'].items():
        if type(v) is not int or not 0<=v<=4:
            raise ValueError(f'Invalid rating {k}')
        items = row.get('evidence',{}).get(k,[])
        req = 2 if k in rubric['require_evidence']['focus_dimensions'] else 1
        if len(items)<req:
            raise ValueError(f'Missing quoted evidence for {k} ({req} required)')
        if len({x.get('quote','') for x in items}) < req:
            raise ValueError(f'Quoted evidence for {k} must use distinct lines')
        for item in items:
            quote, why = item.get('quote',''), item.get('reason','')
            quoted.append(quote)
            if not 12<=len(quote)<=400 or quote not in fulltext:
                raise ValueError(f'Evidence quote for {k} must match actual candidate text')
            if len(why.strip())<20:
                raise ValueError(f'Provide a specific reason for {k}')
    if len(set(quoted)) < 8:
        raise ValueError('A long essay needs evidence from at least 8 distinct passages')
    gate = row.get('gate',{})
    if set(gate) != set(rubric['truth_gate']['fields']) or any(type(x) is not bool for x in gate.values()):
        raise ValueError('All truth gate fields must be verified booleans')
    labels = set(rubric['sentence_audit']['labels'])
    seen=set()
    for item in row.get('sentence_audit',[]):
        idx = item.get('index'); label=item.get('label')
        if type(idx) is not int or idx<0 or idx>=len(sentences(fulltext)) or idx in seen or label not in labels:
            raise ValueError('Invalid, duplicate or unknown sentence annotation')
        seen.add(idx)
    ss=sentences(fulltext)
    if len(seen)<min(30,len(ss)):
        raise ValueError('Need 30 distinct sentence annotations from across the essay')
    thirds=[range(0,len(ss)//3),range(len(ss)//3,2*len(ss)//3),range(2*len(ss)//3,len(ss))]
    for region in thirds:
        if len(seen.intersection(region)) < min(10,len(region)):
            raise ValueError('Sentence sample needs 10 annotations in each essay third')


def score(folder, reviews_path):
    rubric=read(ROOT/'rubric.json')
    jobs={x['id']:x for x in read(folder/'private_generation_requests.json')['requests']}
    audit_result=audit(folder)
    if audit_result['status']!='complete':
        print('Cannot compute a valid comparison: missing drafts or model provenance. No score reported.')
        return {'status':'not_ready','results':[]}
    reviews=read(reviews_path)['reviews']
    byid=defaultdict(list); signatures=set()
    for row in reviews:
        id=row.get('id'); rev=row.get('reviewer')
        if id not in jobs or not rev or (id,rev) in signatures:
            raise ValueError('Review ID, reviewer or duplicate is invalid')
        signatures.add((id,rev))
        validate_review(row,rubric,(folder/'drafts'/f'{id}.txt').read_text(encoding='utf-8'))
        byid[id].append(row)
    result=[]; grouped=defaultdict(list)
    for id, job in jobs.items():
        entries=byid[id]
        if not entries:
            continue
        failed=any(not row['gate']['verified'] or any(row['gate'][k] for k in rubric['truth_gate']['blocking']) for row in entries)
        vals=[] if failed else [sum(row['ratings'][k]*d['weight']/4 for k,d in rubric['dimensions'].items()) for row in entries]
        avg=round(statistics.mean(vals),2) if vals else None
        status='blocked_truth_or_verification' if failed else ('provisional_under_3_reviewers' if len(entries)<3 else 'reviewed_three_plus')
        row={'id':id,'task_id':job['task_id'],'version_private':job['version'],'reviewers':len(entries), 'status':status, 'score':avg}
        result.append(row)
        if avg is not None:
            grouped[(job['version'],job['task_id'])].append(avg)
    summary={version['key']:{'drafts_scored':sum(1 for z in result if z['version_private']==version['key'] and z['score'] is not None),
                             'mean_of_task_means':round(statistics.mean([statistics.mean(scores) for (v,t),scores in grouped.items() if v==version['key']]),2) if any(v==version['key'] for v,t in grouped) else None}
             for version in read(ROOT/'tasks.json')['versions']}
    is_full=(len(result)==len(jobs) and all(z['status']=='reviewed_three_plus' for z in result))
    out={'status':'fully_reviewed' if is_full else 'provisional_incomplete_human_reviews','winner':None,
         'warning':'Human scores, even when complete, are not proof of independent authorship or naturalness. Decide with owner blind preference, prompt-cluster uncertainty and held-out tasks.',
         'summary_private':summary,'results_private':result}
    write(folder/'private_review_scores.json',out)
    print(f"Rated {len(result)} of {len(jobs)} essays. {out['status']}; no automatic winner.")
    return out


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('command',choices=['prepare','audit','score'])
    ap.add_argument('--study',type=Path,default=ROOT/'study_data')
    ap.add_argument('--reviews',type=Path)
    args=ap.parse_args()
    if args.command=='prepare': prepare(args.study)
    elif args.command=='audit': audit(args.study)
    else:
        if not args.reviews: ap.error('--reviews required for scoring')
        score(args.study,args.reviews)
if __name__=='__main__':main()
