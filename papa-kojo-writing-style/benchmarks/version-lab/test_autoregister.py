import sys,tempfile,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
import autoregister

class TestRegistry(unittest.TestCase):
 def test_auto_updates_with_new_version(self):
  with tempfile.TemporaryDirectory() as tmp:
   root=Path(tmp);base=root/'papa-kojo-writing-style';(base/'versions').mkdir(parents=True)
   (base/'SKILL.md').write_text('---\nversion: 3.0.0\n---\n')
   self.assertEqual([x['id'] for x in autoregister.versions(root,git_history=False)],['current-main'])
   for folder in ['v3.1-close-to-speech','steady-voice','v3.3-future']:
    d=base/'versions'/folder;d.mkdir();(d/'SKILL.md').write_text('---\nversion: 3.3.0\n---\n')
   ids=[x['id'] for x in autoregister.versions(root,git_history=False)]
   self.assertEqual(set(ids),{'current-main','v3.1-close-to-speech','steady-voice-v3.2','v3.3-future'})
   self.assertTrue(all(x['evaluation']=='pending' for x in autoregister.versions(root,git_history=False)))
 def test_unpublished_draft_registered(self):
  with tempfile.TemporaryDirectory() as tmp:
   root=Path(tmp);base=root/'papa-kojo-writing-style';(base/'versions').mkdir(parents=True)
   (base/'SKILL.md').write_text('test');f=root/'draft.md';f.write_text('draft')
   ids=[x['id'] for x in autoregister.versions(root,['v1.2.2='+str(f)],git_history=False)]
   self.assertIn('v1.2.2',ids)

if __name__=='__main__':unittest.main()
