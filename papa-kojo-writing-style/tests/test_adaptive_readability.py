import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCRIPT = HERE / 'adaptive_readability.py' if (HERE / 'adaptive_readability.py').exists() else HERE.parent / 'scripts' / 'adaptive_readability.py'
sys.path.insert(0, str(SCRIPT.parent))
from adaptive_readability import analyze, compare, counter_for, sentences


class ReadabilityTests(unittest.TestCase):
    def test_simplification(self):
        old = 'The organisation will subsequently utilise the information to facilitate verification.'
        new = 'The group will use the details later to check who you are.'
        self.assertGreater(compare(old, new)['ease_change'], 0)

    def test_protected_names(self):
        text = 'The National Identification Authority checks fingerprints.'
        raw = analyze(text)
        protected = analyze(text, protected=['National Identification Authority'])
        self.assertEqual(raw['metrics'], protected['metrics'])
        self.assertNotIn('identification', protected['hotspots'][0]['review_words'] if protected['hotspots'] else [])
        self.assertTrue(compare(text, 'The NIA checks fingerprints.', protected=['National Identification Authority'])['review_required'])

    def test_numbers_and_repetition(self):
        old = 'The fee is GH₵10,000. The fee is GH₵10,000.'
        new = 'The fee is GH₵10,000. The fee is GH₵12,000.'
        report = compare(old, new)
        self.assertEqual(report['numbers_removed'], {'10,000': 1})
        self.assertEqual(report['numbers_added'], {'12,000': 1})
        self.assertFalse(compare(old, old)['review_required'])

    def test_decimal_and_abbreviation(self):
        self.assertEqual(len(sentences('Dr. Mensah paid GH₵2.50. He paid GH₵4.00 later.')), 2)

    def test_empty_and_short(self):
        self.assertIsNone(analyze('')['metrics']['ease_estimate'])
        self.assertEqual(analyze('Thank you.')['target_status'], 'review_manually')

    def test_windows_and_smog(self):
        text = ' '.join(['The shop can check each bill before it sends the goods out.'] * 35)
        report = analyze(text)
        self.assertGreater(len(report['windows']), 1)
        self.assertIsNotNone(report['metrics']['smog_estimate'])
        self.assertIsNone(analyze('The shop is open.')['metrics']['smog_estimate'])

    def test_syllables(self):
        count = counter_for()
        self.assertEqual([count(w) for w in ['people', 'quiet', 'cake', 'little', 'technology']], [2, 2, 1, 2, 4])

    def test_optional_list(self):
        self.assertIsNone(analyze('We buy food.')['metrics']['dale_chall_estimate'])
        report = analyze('We buy food.', easy={'we', 'buy', 'food'})
        self.assertEqual(report['metrics']['unlisted_word_percent'], 0)

    def test_cli(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'before.txt'
            path.write_text('The fee is 10.', encoding='utf-8')
            proc = subprocess.run([sys.executable, str(SCRIPT), '--before', str(path)], input='The fee is 20.', text=True, capture_output=True, check=True)
            self.assertTrue(json.loads(proc.stdout)['review_required'])


if __name__ == '__main__':
    unittest.main()
