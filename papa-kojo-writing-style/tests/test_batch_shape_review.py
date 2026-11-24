import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"scripts"))
from batch_shape_review import review

class ShapeReview(unittest.TestCase):
    def test_cross_document_invitation(self):
        r=review([(str(i),"Let us say you sell bread.") for i in range(3)])
        self.assertEqual(r["families"]["shared_invitation"]["documents"],3)
        self.assertTrue(any(f.get("family")=="shared_invitation" for f in r["flags"]))
    def test_contraction_normalization(self):
        r=review([("a","Let's take a shop."),("b","Let’s say a shop sells bread."),("c","Let us look at a shop.")])
        self.assertEqual(r["families"]["shared_invitation"]["documents"],3)
    def test_one_doc_not_batch_warning(self):
        r=review([("a","Let us say you sell bread. Let us take a shop.")])
        self.assertEqual(r["families"]["shared_invitation"]["occurrences"],2)
        self.assertFalse(r["flags"])
    def test_deduplicated_example_positions(self):
        r=review([("a","A thought.\n\nLet us take a shop for example.")])
        self.assertEqual(r["documents_with_example_marker_in_paragraph_2"],1)
        self.assertEqual(r["documents_with_example_markers"],1)
    def test_varying_words_same_scaffold(self):
        r=review([("a","A point.\n\nLet us say a shop."),("b","A point.\n\nIf you sell bread, for example, it costs money."),("c","A point.\n\nSuppose a farmer needs seed.")])
        self.assertTrue(any(f.get("family")=="example_marker_in_paragraph_2" for f in r["flags"]))
    def test_prefix(self):
        r=review([(str(i),"There is a lot to learn about "+str(i)+".") for i in range(3)])
        self.assertTrue(any(f.get("prefix")=="there is a lot" for f in r["flags"]))
    def test_quotes_code_heading(self):
        s="# Let us say a heading\n\n> Let us say a quote.\n\n"+chr(96)*3+"\nLet us say code.\n"+chr(96)*3+"\n\nHe wrote “Let us say a shop.”"
        self.assertEqual(review([("a",s)])["families"]["shared_invitation"]["occurrences"],0)
    def test_empty(self):
        self.assertEqual(review([])["flags"],[])
    def test_duplicate_id(self):
        with self.assertRaises(ValueError): review([("a","One."),("a","Two.")])
    def test_no_quota(self):
        r=review([("a","Water flows downhill."),("b","The shop pays rent."),("c","The train is late.")])
        self.assertFalse(r["flags"])
    def test_threshold(self):
        docs=[(str(i),"Let us say you sell bread." if i<3 else "The shop is open.") for i in range(10)]
        self.assertFalse(any(f.get("family")=="shared_invitation" for f in review(docs)["flags"]))
        self.assertTrue(any(f.get("family")=="shared_invitation" for f in review(docs,coverage=.3)["flags"]))
if __name__=="__main__": unittest.main()
