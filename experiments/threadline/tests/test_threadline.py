import json
import pathlib
import unittest
import sys
ROOT=pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
import threadline

class ThreadlineTests(unittest.TestCase):
    def test_baseline_flags(self):
        r=threadline.analyze((ROOT/'fixtures/templated.txt').read_text())
        flags={x['type'] for x in r['flags']}
        self.assertIn('generic_time_opening',flags)
        self.assertIn('empty_preamble',flags)
        self.assertIn('vague_booster',flags)
        self.assertIn('generic_conclusion',flags)
        self.assertIn('absolute_terms',flags)
    def test_clear_text_not_flagged_as_stock(self):
        r=threadline.analyze((ROOT/'fixtures/grounded.txt').read_text())
        self.assertFalse(any(x['type'] in {'generic_time_opening','empty_preamble','vague_booster','generic_conclusion'} for x in r['flags']))
    def test_prompt_no_human_authorship_claims(self):
        brief=json.loads((ROOT/'example_brief.json').read_text())
        p=threadline.compile_prompt(brief)
        self.assertIn('No visitor testing or accessibility audit has yet been conducted.',p)
        self.assertIn('Do not invent quotations',p)
        self.assertNotIn('PERSONAL_STYLE_PROFILE',p)
    def test_required_context(self):
        with self.assertRaises(ValueError):threadline.task_frame({'purpose':'x'})
    def test_revision_includes_original(self):
        brief=json.loads((ROOT/'example_brief.json').read_text())
        r=threadline.compile_prompt(brief,'Some original sentence.')
        self.assertIn('<draft>',r)
        self.assertIn('Some original sentence.',r)
    def test_negated_absolute_is_not_a_false_alarm(self):
        r=threadline.analyze('The approach will not always work. Some people might need another choice.')
        self.assertNotIn('absolute_terms',{x['type'] for x in r['flags']})
    def test_baseline_receives_same_fact_packet(self):
        brief=json.loads((ROOT/'example_brief.json').read_text())
        a=threadline.compile_prompt(brief)
        b=threadline.baseline_prompt(brief)
        for fact in brief['known_facts']:
            self.assertIn(fact,a)
            self.assertIn(fact,b)
    def test_empty_doc_safe(self):
        a=threadline.analyze('')
        self.assertEqual(a['words'],0)
        self.assertEqual(a['flags'],[])
    def test_long_form_three_segments(self):
        ps=['The appointment system records the time selected by a visitor. Staff review the request before confirming it.']*65
        r=threadline.analyze('\n\n'.join(ps))
        self.assertEqual(len(r['thirds']),3)
        self.assertGreater(r['duplicated_paragraphs'],30)
        self.assertIn('duplicated_paragraphs',{x['type'] for x in r['flags']})
    def test_repeat_not_equal_automated_human_detection(self):
        r=threadline.analyze('The answer is yes. The reason is clear.')
        self.assertIn('limitations',r)
        self.assertNotIn('is_human',r)

if __name__=='__main__':unittest.main()
