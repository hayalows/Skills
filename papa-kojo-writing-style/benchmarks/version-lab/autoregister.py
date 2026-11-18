"""Discover PKM writing skill versions without assigning unearned quality scores."""
import argparse, hashlib, json, re, subprocess
from pathlib import Path

HISTORY = {'v1.0':'46db3f8','v1.1':'e1260b1','v1.2':'ca5abb6'}

def sha(text): return hashlib.sha256(text.encode('utf-8')).hexdigest()

def versions(repo, extras=(), git_history=True):
    repo=Path(repo).resolve();base=repo/'papa-kojo-writing-style';out=[]
    def add(name,source,text,kind):
        match=re.search(r'^\s*(?:version|revision):\s*[\'\"]?([\w.\-]+)',text.split('---',2)[1] if text.startswith('---') else '',re.M)
        out.append({'id':name,'source':source,'declared_version':match.group(1) if match else None,
                    'kind':kind,'sha256':sha(text),'generation':'pending','evaluation':'pending'})
    active=base/'SKILL.md';add('current-main',str(active.relative_to(repo)),active.read_text(),'active')
    for d in sorted((base/'versions').iterdir()):
        if not d.is_dir():continue
        for f in sorted(list(d.glob('SKILL.md'))+list(d.glob('SKILL.v*.md'))):
            name={'v3.1-close-to-speech':'v3.1-close-to-speech','steady-voice':'steady-voice-v3.2'}.get(d.name,d.name)
            add(name,str(f.relative_to(repo)),f.read_text(),'selectable-or-archived')
    if git_history and (repo/'.git').exists():
        for name,ref in HISTORY.items():
            p=subprocess.run(['git','-C',str(repo),'show',f'{ref}:papa-kojo-writing-style/SKILL.md'],text=True,capture_output=True)
            if p.returncode==0:add(name,f'{ref}:papa-kojo-writing-style/SKILL.md',p.stdout,'historical')
    for arg in extras:
        name,sep,path=arg.partition('=')
        if not sep or not re.fullmatch(r'[A-Za-z0-9_.-]+',name):raise ValueError('Expected NAME=PATH')
        f=Path(path);add(name,str(f),f.read_text(),'unpublished-draft')
    ids=[v['id'] for v in out]
    if len(ids)!=len(set(ids)):raise ValueError('Duplicate version ID')
    return out

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--repo',type=Path,default=Path('.'));p.add_argument('--out',type=Path,default=Path('version-manifest.json'))
    p.add_argument('--extra',action='append',default=[]);p.add_argument('--no-git-history',action='store_true')
    a=p.parse_args()
    out={'protocol':'PKM-writing-version-registry-1','note':'No generated drafts or quality scores implied.',
         'versions':versions(a.repo,a.extra,not a.no_git_history)}
    a.out.parent.mkdir(parents=True,exist_ok=True)
    a.out.write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps({'count':len(out['versions']),'ids':[v['id'] for v in out['versions']],'out':str(a.out)}))
if __name__=='__main__':main()
