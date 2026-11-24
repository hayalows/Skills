import json
from pathlib import Path
import subprocess
import sys
import unittest

HERE = Path(__file__).resolve().parent
SCRIPTS = HERE if (HERE/'conversation_check.py').exists() else HERE.parent/'scripts'
sys.path.insert(0, str(SCRIPTS))
from conversation_check import review


def ids(text, register='longform'):
    return [f['id'] for f in review(text, register)['flags']]


class ConversationTests(unittest.TestCase):
    def test_take(self):
        self.assertIn('detached_take', ids('Take a small shop that has trouble keeping track of its money.'))
        self.assertIn('detached_take', ids('Take the case of a farmer.'))

    def test_say(self):
        self.assertIn('detached_say', ids('Say I want to learn a new skill.'))
        self.assertIn('detached_say', ids('So, say you earn GH₵500.'))

    def test_formal(self):
        self.assertIn('formal_setup', ids('Consider a hypothetical scenario.'))

    def test_preferred(self):
        for text in ['Let us take a small shop for example.', 'If I want to learn, for example, I can read a book.', 'If you have GH₵500, you can set some aside.', 'A shop may run out of cash even when sales are good.']:
            self.assertEqual(ids(text), [], text)

    def test_legitimate_instructions(self):
        for text in ['Take a break before you start.', 'Take your ID to the bank.', 'Say thank you to your host.', 'Consider the costs before signing.']:
            self.assertEqual(ids(text), [], text)

    def test_register_scope(self):
        for register in ['chat','message','comment','formal']:
            self.assertEqual(ids('Say you are free at noon.', register), [])
        self.assertIn('detached_say', ids('Say you are free at noon.', 'post'))

    def test_repetition(self):
        self.assertIn('repeated_invitation', ids("Let us look at a shop. It sells bread. Let's look at the cash."))
        self.assertNotIn('repeated_invitation', ids('Let us look at the cash. It pays the bills. The owner buys stock. Sales are slow. Costs go up. Credit is due. Let us look at a different case.'))

    def test_questions(self):
        self.assertIn('question_run', ids('What happened? Who paid? Why now?'))
        self.assertEqual(ids('Can you see why this matters? The fee is due today.'), [])

    def test_literals(self):
        for text in ['> Take a shop that sells bread.', 'She wrote “Say I want to learn.”', 'She wrote "Say I want to learn."', '`Say I want to learn.`', '```text\nSay I want to learn.\n```']:
            self.assertEqual(ids(text), [], text)

    def test_cli(self):
        p = subprocess.run([sys.executable, str(SCRIPTS/'conversation_check.py'), '--review-gate'], input='Say I want to learn.', text=True, capture_output=True)
        self.assertEqual(p.returncode, 2)
        self.assertEqual(json.loads(p.stdout)['flags'][0]['id'], 'detached_say')
        p = subprocess.run([sys.executable, str(SCRIPTS/'conversation_check.py'), '--review-gate'], input='', text=True, capture_output=True)
        self.assertEqual(p.returncode, 0)


if __name__ == '__main__':
    unittest.main()
