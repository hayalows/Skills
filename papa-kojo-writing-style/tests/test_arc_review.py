import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"scripts"))
from arc_review import review

class ArcReview(unittest.TestCase):
    def test_exact_opening(self):
        a="A shop can have a busy day without much cash.\n\nThe bill is due."
        b="A shop can have a busy day without much cash.\n\nSome sales are on credit."
        r=review([("a",a),("b",b)])
        self.assertEqual([(x["edge"],x["kind"]) for x in r["candidates"]],[("opening","normalized_exact")])
    def test_exact_closing(self):
        r=review([("a","A shop paid its bill.\n\nWe can check the records."),("b","A driver paid his fee.\n\nWe can check the records.")])
        self.assertEqual(r["candidates"][0]["edge"],"closing")
    def test_near(self):
        a="The owner of the shop keeps a book beside the till and writes each sale in it."
        b="The owner of the shop keeps a book beside the till and writes each sale in the book."
        self.assertEqual(review([("a",a),("b",b)])["candidates"][0]["kind"],"shared_trigrams")
    def test_short_near_not_flagged(self):
        self.assertFalse(review([("a","I can help today."),("b","I can help now.")])["candidates"])
    def test_single_paragraph_dedup(self):
        self.assertEqual(len(review([("a","Thank you."),("b","Thank you.")])["candidates"]),1)
    def test_headings_quotes(self):
        r=review([("a","# Same heading\n\n> A common quotation.\n\nThe shop is busy."),("b","# Same heading\n\n> A common quotation.\n\nThe road is quiet.")])
        self.assertFalse(r["candidates"])
    def test_no_history(self):
        self.assertEqual(review([("a","One thought.")])["candidates"],[])
    def test_empty(self):
        self.assertEqual(review([("a",""),("b","")])["candidates"],[])
    def test_duplicate_id(self):
        with self.assertRaises(ValueError): review([("a","One."),("a","Two.")])
    def test_bad_parameters(self):
        with self.assertRaises(ValueError): review([],threshold=0)
    def test_different_ideas(self):
        self.assertFalse(review([("a","What makes a route useful? The time it takes depends on the road."),("b","An accurate map may take too long to load on a phone.")])["candidates"])
if __name__=="__main__": unittest.main()
