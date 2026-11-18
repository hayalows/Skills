"""Prepare matched writing requests from source-verified version registry. No generation."""
import argparse, hashlib, json, subprocess
from pathlib import Path
from autoregister import versions

def source(repo,c):
    name=c['source']
    if ':' in name and not Path(name).exists():
        ref,path=name.split(':',1)
        cp=subprocess.run(['git','-C',str(repo),'show',f'{ref}:{path}'],text=True,capture_output=True,check=True)
        return cp.stdout
    p=Path(repo)/name
    if not p.exists():p=Path(name)
    return p.read_text()

def run(repo,briefs_file,out,repeats=3,model='UNCONFIGURED',extras=()):
    if repeats<1:raise ValueError('repeats must be >=1')
    root=Path(repo).resolve(); out=Path(out)
    briefs=json.loads(Path(briefs_file).read_text())['briefs']
    if not briefs or len({b['id'] for b in briefs})!=len(briefs):raise ValueError('Bad brief IDs')
    registry=versions(root,extras)
    (out/'requests').mkdir(parents=True,exist_ok=True)
    matrix={'model':model,'briefs_sha256':hashlib.sha256(Path(briefs_file).read_bytes()).hexdigest(),
            'protocol':'PKM-matched-requests-1','status':'prepared-no-generation','versions':registry,'requests':[]}
    for b in briefs:
        for v in registry:
            skill=source(root,v)
            for repeat in range(1,repeats+1):
                id=f"R{len(matrix['requests'])+1:05d}"
                text='WRITING SKILL (follow this version only):\n'+skill+'\n\nMATCHED TASK:\n'+json.dumps(b,ensure_ascii=False,indent=2)+'\n\nReturn only the requested copy, not the plan or an explanation of the skill.\n'
                p=out/'requests'/f'{id}.txt'
                p.write_text(text,encoding='utf-8')
                matrix['requests'].append({'id':id,'version':v['id'],'brief_id':b['id'],'run':repeat,
                                           'skill_sha256':v['sha256'],
                                           'prompt_sha256':hashlib.sha256(text.encode('utf-8')).hexdigest(),
                                           'requested_model':model,'state':'pending-generation'})
    (out/'matrix.json').write_text(json.dumps(matrix,ensure_ascii=False,indent=2)+'\n')
    return matrix

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--repo',type=Path,default=Path('.'));p.add_argument('--briefs',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True);p.add_argument('--repeats',type=int,default=3)
    p.add_argument('--model',default='UNCONFIGURED');p.add_argument('--extra',action='append',default=[])
    a=p.parse_args()
    m=run(a.repo,a.briefs,a.out,a.repeats,a.model,a.extra)
    print(json.dumps({'versions':len(m['versions']),'briefs':len(json.loads(a.briefs.read_text())['briefs']),'requests':len(m['requests']),'status':m['status']}))
