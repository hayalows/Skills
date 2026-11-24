import json
from pathlib import Path
import subprocess
import sys
import unittest
from unittest.mock import patch

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE if (HERE / "readability_review.py").exists() else HERE.parent / "scripts"))
import readability_review as r


class ReviewTests(unittest.TestCase):
    def test_short(self):
        x = r.dual('Thanks for checking.', mode='heuristic')
        self.assertEqual(x['audience_status'], 'short_sample')
        self.assertIsNone(x['strict_grade5_target'])
        self.assertIsNone(r.dual('', mode='heuristic')['primary']['ease_estimate'])

    def test_targets(self):
        m = {'words': 110, 'sentences': 8, 'ease_estimate': 95.3, 'grade_estimate': 4.0}
        self.assertEqual(r.target(m, 'longform'), 'above_range_no_penalty')
        m['ease_estimate'] = 78.6
        self.assertEqual(r.target(m, 'longform'), 'near_target')
        m['ease_estimate'] = 70.7
        self.assertEqual(r.target(m, 'longform'), 'review_difficulty')
        self.assertEqual(r.target(m, 'technical'), 'in_range')

    def test_fallback(self):
        original = r.base.analyze
        def mocked(text, profile, protected, dictionary):
            if dictionary == 'cmu':
                raise ValueError('missing dictionary')
            return original(text, profile, protected, dictionary)
        with patch.object(r.base, 'analyze', mocked):
            self.assertEqual(r.dual('A short note.')['primary_dictionary'], 'heuristic')
            with self.assertRaises(ValueError):
                r.dual('A short note.', mode='cmu')

    def test_dictionary(self):
        x = r.dual(' '.join(['The shop can check each bill before it sends the goods out.']*10))
        if x['dictionary_available']:
            self.assertEqual(x['primary_dictionary'], 'cmu')
            self.assertIsNotNone(x['ease_difference'])
        else:
            self.assertEqual(x['primary_dictionary'], 'heuristic')

    def test_long_tail(self):
        s = 'The shop can check each bill before it sends the goods out. '
        t = s*90 + 'The implementation requires considerable institutional coordination and verification. '*8
        x = r.dual(t, mode='heuristic')
        self.assertGreater(x['primary']['words'], 1000)
        self.assertEqual(max(w['end_sentence'] for w in x['windows']), x['primary']['sentences'])
        self.assertGreater(x['hardest_windows'][0]['start_sentence'], 80)

    def test_rhythm(self):
        self.assertTrue(r.dual('Go home. Sit down. Read it. Write it. Check it.', mode='heuristic')['rhythm_review'])

    def test_scope_and_required(self):
        x = r.review('The NIA may charge GH₵10. It has not approved the plan.', 'The NIA will charge GH₵20. It has approved the plan.', protected=['NIA'], required=['not approved'], mode='heuristic')
        self.assertTrue(x['editor_review_required'])
        self.assertEqual(x['missing_required'], ['not approved'])
        self.assertIn('may', x['scope_cues_removed'])
        self.assertIn('not', x['scope_cues_removed'])
        self.assertTrue(x['literal_review']['review_required'])

    def test_cli(self):
        p = subprocess.run([sys.executable, str(Path(__file__).with_name('readability_review.py') if Path(__file__).with_name('readability_review.py').exists() else Path(__file__).resolve().parents[1]/'scripts'/'readability_review.py'), '--dictionary','heuristic'], input='A clear note.', text=True, capture_output=True, check=True)
        self.assertEqual(json.loads(p.stdout)['version'], '1.1.0')


if __name__ == '__main__':
    unittest.main()
