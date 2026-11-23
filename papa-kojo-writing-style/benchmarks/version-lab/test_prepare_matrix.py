import sys,tempfile,unittest,json
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from prepare_matrix import run

class TestMatrix(unittest.TestCase):
 def test_new_version_gets_same_briefs_and_repeats(self):
  with tempfile.TemporaryDirectory() as td:
   root=Path(td);skill=root/'papa-kojo-writing-style';(skill/'versions').mkdir(parents=True)
   (skill/'SKILL.md').write_text('---\nversion: 3.0\n---\nCurrent')
   d=skill/'versions'/'new-version';d.mkdir();(d/'SKILL.md').write_text('---\nversion: 4.0\n---\nNew')
   b=root/'briefs.json';b.write_text(json.dumps({'briefs':[{'id':'P01','prompt':'Write a hello'},{'id':'P02','prompt':'Write a bye'}]}))
   m=run(root,b,root/'out',3)
   self.assertEqual(len(m['requests']),12)
   self.assertEqual({r['version'] for r in m['requests']},{'current-main','new-version'})
   self.assertTrue(all(r['state']=='pending-generation' for r in m['requests']))
   self.assertTrue((root/'out'/'requests'/'R00012.txt').exists())

if __name__=='__main__':unittest.main()
