#!/usr/bin/env python3
"""Summarize blind human ratings after collection. No synthetic ratings permitted."""
import argparse,csv,random,statistics,json,collections
DIMS=['reader_fit','thought_flow','grounding','factual_discipline','natural_phrasing','ending']
WEIGHTS=[.2,.25,.15,.2,.1,.1]

def score(rows):
    if not rows:raise ValueError('No human rating rows were provided.')
    return statistics.mean(sum(float(r[d])*w for d,w in zip(DIMS,WEIGHTS)) for r in rows)

def summarize(keypath:str,ratingspath:str,seed:int=121,replicates:int=2000):
    with open(keypath,encoding='utf-8',newline='') as f:
        key={(r['pair_id'],r['blind_label']):r['condition'] for r in csv.DictReader(f)}
    with open(ratingspath,encoding='utf-8',newline='') as f:rows=list(csv.DictReader(f))
    grouped=collections.defaultdict(lambda:collections.defaultdict(list))
    for r in rows:
        identity=(r['pair_id'],r['blind_label'])
        if identity not in key:raise ValueError('No key for '+str(identity))
        if any(not r.get(d) for d in DIMS):raise ValueError('Incomplete dimension scores '+str(identity))
        grouped[r['pair_id']][key[identity]].append(r)
    differences=[]
    for pair,arms in grouped.items():
        if all(x in arms for x in ('threadline','baseline')):
            differences.append(score(arms['threadline'])-score(arms['baseline']))
    if not differences:raise ValueError('No fully rated pairs are available')
    rng=random.Random(seed)
    boot=[]
    for _ in range(replicates):
        sample=[rng.choice(differences) for _ in differences]
        boot.append(statistics.mean(sample))
    boot.sort()
    wins=sum(x>0 for x in differences);ties=sum(x==0 for x in differences);losses=sum(x<0 for x in differences)
    return {'fully_rated_pairs':len(differences),'threadline_preferred_score_pairs':wins,'ties':ties,'baseline_preferred_score_pairs':losses,
            'mean_paired_score_difference_on_1_to_5_scale':round(statistics.mean(differences),3),
            'bootstrap_95_ci':(round(boot[int(replicates*.025)],3),round(boot[int(replicates*.975)-1],3)),
            'warning':'This is a rubric-score comparison and does not substitute for reader preference, truth checks or task success.'}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('answer_key');p.add_argument('ratings_csv');args=p.parse_args()
    print(json.dumps(summarize(args.answer_key,args.ratings_csv),indent=2))
