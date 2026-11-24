import json
from pathlib import Path
import subprocess
import sys
import unittest
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
import pk_checker as p

class Checker(unittest.TestCase):
    def test_conversation_cases(self):
        data=json.loads((ROOT/"datasets/development_cases.json").read_text(encoding="utf-8"))
        for s,want in data["conversation"]:
            with self.subTest(s=s):
                self.assertEqual(bool(p.conversation(p.sentences(p.style_prose(s)),"longform")),want)
    def test_composition_cases(self):
        data=json.loads((ROOT/"datasets/development_cases.json").read_text(encoding="utf-8"))
        for s,want in data["composition"]:
            with self.subTest(s=s): self.assertEqual(p.triplet(s),want)
    def test_repeat(self):
        self.assertIn("repeated_invitation",{x[0] for x in p.conversation(["Let us look at costs.","Let's look at sales."],"longform")})
        self.assertIn("question_run",{x[0] for x in p.conversation(["Why?","Who?","When?"],"post")})
    def test_profile(self):
        self.assertFalse(p.conversation(["Suppose you know the answer."],"formal"))
    def test_literals(self):
        s="# A title\n\n---\n\n"+chr(96)*3+"\nensure --\n"+chr(96)*3+"\n\nShe said “unlock — the door.” We can help."
        ids={f["type"] for f in p.audit(s,mode="heuristic")["flags"]}
        self.assertFalse(ids&{"avoid_word","dash_review"})
    def test_sentences(self):
        self.assertEqual(len(p.sentences("# Title\n\nDr. Mensah paid GH₵2.50. We met at 4 p.m. We left.")),3)
    def test_scope(self):
        self.assertEqual(p.cues("We don't sell."),p.cues("We do not sell."))
        self.assertEqual(p.cues("We won’t sell.")["not"],1)
        self.assertNotEqual(p.cues("Some shops paid."),p.cues("All shops paid."))
    def test_numeric(self):
        for a,b in [("Fee is 10%.","Fee is 10 cedis."),("Balance is -500.","Balance is 500."),("Ten paid.","Twenty paid."),("Fee is GH₵50.","Fee is USD50.")]:
            with self.subTest(a=a):
                r=p.diff_revisions(a,b,mode="heuristic")
                self.assertTrue(r["numbers_removed"] and r["numbers_added"])
    def test_swap(self):
        r=p.diff_revisions("Fee is 50. Refund is 100.","Fee is 100. Refund is 50.",mode="heuristic")
        self.assertTrue(r["numeric_context_changed"])
        self.assertTrue(r["literal_review_required"])
    def test_protected(self):
        r=p.diff_revisions("C++ uses a cap. C++ works.","C++ uses capacity.",mode="heuristic",protected=["C++"],required=["cap","C++"])
        self.assertEqual(r["missing_required"],["cap"])
        self.assertEqual(r["protected_removed"],{"C++":1})
    def test_register(self):
        ids={f["type"] for f in p.audit("I'm here! 😊","formal","heuristic")["flags"]}
        self.assertTrue({"register_contractions","register_emoji"}<=ids)
    def test_short_empty(self):
        for s in ["","Hi."]:
            r=p.audit(s,mode="heuristic")
            self.assertEqual(r["audience_status"],"short_sample")
            self.assertIsNone(r["strict_grade5_target"])
    def test_readability(self):
        s="We can read the book and talk about what it says. "*12
        r=p.audit(s,mode="auto")
        self.assertIn(r["primary_estimator"],{"cmu","heuristic"})
        self.assertTrue(r["paragraphs"] and r["hardest_windows"])
    def test_cli(self):
        r=subprocess.run([sys.executable,str(ROOT/"pk_checker.py"),"--dictionary","heuristic","--review-gate"],input="Suppose you sell a car.",text=True,capture_output=True,encoding="utf-8",env={**__import__("os").environ,"PYTHONIOENCODING":"utf-8"})
        self.assertEqual(r.returncode,2,r.stderr)
        self.assertEqual(json.loads(r.stdout)["version"],p.VERSION)

if __name__=="__main__": unittest.main()
