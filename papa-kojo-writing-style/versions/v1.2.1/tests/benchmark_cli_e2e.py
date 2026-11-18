#!/usr/bin/env python3
"""Contract tests through the public benchmark CLI. Written before implementation."""
import json, subprocess, tempfile, unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
CLI = ROOT / 'scripts' / 'benchmark_score.py'
CONFIG = ROOT / 'references' / 'benchmark_config.json'
DIMS = ('truth','reader','voice','reasoning','clarity','emotion','specificity','transitions','pacing','restraint','ending','genre')

def case(**kwargs):
    return {'id':'A', 'version':'vX','task':'love','format':'reflective',
            'text':'I have a point. And I can explain why it matters.','reviewer':'editor-1',
            'ratings':{k:3 for k in DIMS},'gate':{'verified':True,'fabrication':False,'material_misstatement':False,'scope_failure':False},**kwargs}

def run(data):
    with tempfile.TemporaryDirectory() as d:
        inp=Path(d)/'input.json'; out=Path(d)/'report.json'; inp.write_text(json.dumps({'records':data}))
        p=subprocess.run(['python3',str(CLI),'--config',str(CONFIG),'--input',str(inp),'--output',str(out)],capture_output=True,text=True)
        return p,json.loads(out.read_text()) if out.exists() else None

class Contract(unittest.TestCase):
    def test_all_threes_yields_75_and_schema(self):
        p,d=run([case()]); self.assertEqual(p.returncode,0,p.stderr); self.assertEqual(d['results'][0]['total'],75.0)
        self.assertEqual(d['results'][0]['status'],'provisional_one_rater')
        self.assertEqual(len(d['results'][0]['series']),12)
    def test_missing_dimensions_not_scored(self):
        z=case();z['ratings'].pop('truth');p,d=run([z]);self.assertNotEqual(p.returncode,0)
    def test_fabricated_personal_history_blocks_total(self):
        z=case();z['gate']['fabrication']=True;p,d=run([z]);self.assertEqual(p.returncode,0,p.stderr)
        self.assertIsNone(d['results'][0]['total']);self.assertEqual(d['results'][0]['status'],'blocked_truth_gate')
    def test_unreviewed_gate_blocks_total(self):
        z=case();z['gate']['verified']=False;p,d=run([z]);self.assertEqual(p.returncode,0,p.stderr)
        self.assertIsNone(d['results'][0]['total']);self.assertEqual(d['results'][0]['status'],'unverified_truth_gate')
    def test_out_of_range_ratings_rejected(self):
        z=case();z['ratings']['voice']=5;p,d=run([z]);self.assertNotEqual(p.returncode,0)
    def test_two_reviewers_are_averaged_and_not_double_counted(self):
        z=case();v=case(reviewer='editor-2',ratings={k:4 for k in DIMS});p,d=run([z,v]);self.assertEqual(p.returncode,0,p.stderr)
        self.assertEqual(len(d['results']),1);self.assertEqual(d['results'][0]['total'],87.5)
        self.assertEqual(d['results'][0]['status'],'two_raters_pending_reliability')
    def test_two_reviewers_split_on_gate_blocks(self):
        z=case();v=case(reviewer='editor-2',gate={'verified':True,'fabrication':True,'material_misstatement':False,'scope_failure':False})
        p,d=run([z,v]);self.assertEqual(p.returncode,0,p.stderr);self.assertIsNone(d['results'][0]['total'])
    def test_duplicate_reviewer_rejected(self):
        p,d=run([case(),case()]);self.assertNotEqual(p.returncode,0)
    def test_lens_weights_and_total_reconcile(self):
        p,d=run([case()]);self.assertEqual(p.returncode,0,p.stderr)
        self.assertTrue(d['results'][0]['lenses']);self.assertTrue(all(v==75.0 for v in d['results'][0]['lenses'].values()))
        self.assertEqual(sum(x['weight'] for x in d['results'][0]['series'].values()),100)
    def test_no_record_is_no_fake_score(self):
        p,d=run([]);self.assertEqual(p.returncode,0,p.stderr);self.assertEqual(d['results'],[])

if __name__ == '__main__': unittest.main(verbosity=2)
