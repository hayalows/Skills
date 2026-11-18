#!/usr/bin/env python3
"""Regression checks for long-form benchmark mechanics; no network, no model calls."""
import json
import tempfile
import unittest
from pathlib import Path
from collections import Counter
import longform_study as bench

class LongformContract(unittest.TestCase):
    def test_config_and_manifest_balanced(self):
        spec=bench.read(bench.ROOT/'tasks.json')
        rubric=bench.read(bench.ROOT/'rubric.json')
        self.assertEqual(len(spec['versions']),4)
        self.assertEqual(len(spec['tasks']),8)
        self.assertEqual(sum(d['weight'] for d in rubric['dimensions'].values()),100)
        self.assertEqual(rubric['dimensions']['voice']['weight']+rubric['dimensions']['emotion']['weight']+rubric['dimensions']['sentence']['weight'],43)
        with tempfile.TemporaryDirectory() as folder:
            dest=Path(folder)
            bench.prepare(dest)
            private=bench.read(dest/'private_generation_requests.json')['requests']
            visible=bench.read(dest/'reviewer_blind_manifest.json')['candidates']
            self.assertEqual(len(private),96)
            self.assertEqual(len(visible),96)
            self.assertTrue(all('version' not in x and 'source' not in x for x in visible))
            counts=Counter((x['task_id'],x['version']) for x in private)
            self.assertEqual(len(counts),32)
            self.assertEqual(set(counts.values()),{3})
            self.assertEqual(bench.read(dest/'status.json')['generated_independent_drafts'],0)
            self.assertEqual(bench.audit(dest)['status'],'incomplete_or_invalid')

    def test_readability_has_local_windows(self):
        text='\n\n'.join(['Some ideas take time to explain. A reader needs an example before the claim becomes clear. ' * 7] * 12)
        m=bench.metrics(text)
        self.assertGreater(m['word_count'],400)
        self.assertGreaterEqual(len(m['window_reading_ease_estimates']),2)
        self.assertIsInstance(m['minimum_window_reading_ease_estimate'],float)
        self.assertGreater(m['window_spread_estimate'],-0.1)

    def make_review(self):
        rubric=bench.read(bench.ROOT/'rubric.json')
        phrases=[f'This source essay includes example number {i} in full context.' for i in range(1,18)]
        text=(' '.join(phrases) + ' ') * 12
        evidence={}
        for i,dim in enumerate(rubric['dimensions']):
            item={'quote':phrases[i], 'reason':'This exact example supports the assigned score in context.'}
            if dim in rubric['require_evidence']['focus_dimensions']:
                second={'quote':phrases[(i+1)%len(phrases)], 'reason':'The second sentence supports the judgement in another way.'}
                evidence[dim]=[item,second]
            else: evidence[dim]=[item]
        third=len(bench.sentences(text))//3
        audit=[{'index':i,'label':'clear'} for i in list(range(10))+list(range(third,third+10))+list(range(2*third,2*third+10))]
        row={'ratings':{k:3 for k in rubric['dimensions']},'evidence':evidence,
             'gate':{x:(x=='verified') for x in rubric['truth_gate']['fields']},'sentence_audit':audit}
        return rubric,text,row

    def test_quote_evidence_is_required_and_exact(self):
        rubric,text,row=self.make_review()
        bench.validate_review(row,rubric,text)
        row['evidence']['voice'][0]['quote']='I was there, but nobody knows.'
        with self.assertRaisesRegex(ValueError,'must match'):
            bench.validate_review(row,rubric,text)

    def test_sentence_audit_requires_30_and_three_sections(self):
        rubric,text,row=self.make_review()
        row['sentence_audit']=row['sentence_audit'][:29]
        with self.assertRaisesRegex(ValueError,'30'):
            bench.validate_review(row,rubric,text)
        rubric,text,row=self.make_review()
        row['sentence_audit']=[{'index':i,'label':'clear'} for i in range(30)]
        with self.assertRaisesRegex(ValueError,'third'):
            bench.validate_review(row,rubric,text)

    def test_fake_reviews_and_wrong_ratings_rejected(self):
        rubric,text,row=self.make_review()
        row['ratings']['voice']=5
        with self.assertRaisesRegex(ValueError,'Invalid rating'):
            bench.validate_review(row,rubric,text)

    def test_no_llm_calls_are_ever_claimed_by_prepare(self):
        with tempfile.TemporaryDirectory() as folder:
            bench.prepare(Path(folder))
            summary=bench.read(Path(folder)/'status.json')
            self.assertEqual(summary['scored_human_reviews'],0)
            self.assertIsNone(summary['winner'])

if __name__=='__main__': unittest.main(verbosity=2)
