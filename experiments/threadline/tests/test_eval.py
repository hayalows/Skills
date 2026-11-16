import csv,json,pathlib,tempfile,sys,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
import run_blind_ab,score_blind_ab

class EvaluationTests(unittest.TestCase):
    def test_blind_pair_packet_contains_two_conditions(self):
        brief=json.loads((ROOT/'briefs_eval.json').read_text())[0]
        with tempfile.TemporaryDirectory() as t:
            out=pathlib.Path(t)
            result=run_blind_ab.build([brief],out,repeats=2,seed=103)
            self.assertEqual(result['pairs'],2)
            with (out/'PRIVATE_answer_key.csv').open(encoding='utf-8') as source:
                keys=list(csv.DictReader(source))
            self.assertEqual(len(keys),4)
            for pair in {r['pair_id'] for r in keys}:
                self.assertEqual({x['condition'] for x in keys if x['pair_id']==pair},{'baseline','threadline'})
            self.assertTrue((out/'ratings_template.csv').exists())
            self.assertFalse((out/'blind_outputs'/f'{brief["id"]}-01-A.txt').exists())
    def test_scoring_requires_actual_ratings(self):
        with self.assertRaises(ValueError):score_blind_ab.score([])
    def test_fake_scores_only_test_math(self):
        with tempfile.TemporaryDirectory() as tmp:
            d=pathlib.Path(tmp)
            (d/'key.csv').write_text('pair_id,blind_label,condition\nA1,A,threadline\nA1,B,baseline\n',encoding='utf-8')
            cols=['pair_id','blind_label','judge_id']+score_blind_ab.DIMS
            with (d/'ratings.csv').open('w',encoding='utf-8',newline='') as f:
                w=csv.writer(f);w.writerow(cols)
                w.writerow(['A1','A','fake_test_judge']+[5]*len(score_blind_ab.DIMS))
                w.writerow(['A1','B','fake_test_judge']+[3]*len(score_blind_ab.DIMS))
            result=score_blind_ab.summarize(str(d/'key.csv'),str(d/'ratings.csv'),replicates=50)
            self.assertEqual(result['fully_rated_pairs'],1)
            self.assertAlmostEqual(result['mean_paired_score_difference_on_1_to_5_scale'],2)

if __name__=='__main__':unittest.main()
