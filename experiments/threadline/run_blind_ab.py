#!/usr/bin/env python3
"""Create blinded A/B packets; run optional live generation only with an API key.

All task facts remain identical across conditions. The study key is separated.
"""
from __future__ import annotations
import argparse,csv,json,pathlib,random,sys
from threadline import compile_prompt,baseline_prompt,call_openai

def build(briefs:list[dict],dirpath:pathlib.Path,repeats:int=1,seed:int=1975,execute:bool=False,model:str|None=None)->dict:
    if repeats<1:raise ValueError('repeats must be >= 1')
    if execute and not model:raise ValueError('--model required with --execute')
    rng=random.Random(seed)
    pdir=dirpath/'prompts';sdir=dirpath/'blind_outputs';pdir.mkdir(parents=True,exist_ok=True);sdir.mkdir(exist_ok=True)
    keys=[];cases=[]
    for brief in briefs:
        case=brief['id']
        for trial in range(1,repeats+1):
            pair=f'{case}-{trial:02d}'
            order=['baseline','threadline'];rng.shuffle(order)
            for blind_label,condition in zip(('A','B'),order):
                prompt=(baseline_prompt if condition=='baseline' else compile_prompt)(brief)
                pp=pdir/f'{pair}-{condition}.txt';pp.write_text(prompt,encoding='utf-8')
                result_path=sdir/f'{pair}-{blind_label}.txt'
                if execute:result_path.write_text(call_openai(prompt,model),encoding='utf-8')
                keys.append({'pair_id':pair,'blind_label':blind_label,'condition':condition,'prompt_filename':pp.name})
            cases.append({'pair_id':pair,'brief_id':case,'genre':brief.get('genre'),'output_file_A':str(sdir/f'{pair}-A.txt'),'output_file_B':str(sdir/f'{pair}-B.txt')})
    with (dirpath/'PRIVATE_answer_key.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=keys[0].keys());w.writeheader();w.writerows(keys)
    (dirpath/'judge_packets.json').write_text(json.dumps(cases,indent=2,ensure_ascii=False),encoding='utf-8')
    dims=['reader_fit','thought_flow','grounding','factual_discipline','natural_phrasing','ending']
    with (dirpath/'ratings_template.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.writer(f);w.writerow(['pair_id','blind_label','judge_id']+dims)
        for pair in cases:
            for label in ('A','B'):
                w.writerow([pair['pair_id'],label,'']+['']*len(dims))
    with (dirpath/'preferences_template.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.writer(f);w.writerow(['pair_id','judge_id','preference_A_B_Tie','reason'])
        for pair in cases:w.writerow([pair['pair_id'],'','',''])
    return {'pairs':len(cases),'prompts':len(keys),'generated_live':execute,'judge_packets':str(dirpath/'judge_packets.json'),'key':'Keep PRIVATE_answer_key.csv from judges.'}

if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--briefs',default='briefs_eval.json')
    ap.add_argument('--out',default='eval_run')
    ap.add_argument('--repeats',type=int,default=3)
    ap.add_argument('--seed',type=int,default=1975)
    ap.add_argument('--execute',action='store_true',help='Requires OPENAI_API_KEY and a model you can access; incurs API costs')
    ap.add_argument('--model')
    args=ap.parse_args()
    src=pathlib.Path(args.briefs)
    briefs=json.loads(src.read_text(encoding='utf-8'))
    try:print(json.dumps(build(briefs,pathlib.Path(args.out),args.repeats,args.seed,args.execute,args.model),indent=2))
    except Exception as ex:print('ERROR:',ex,file=sys.stderr);raise SystemExit(2)
