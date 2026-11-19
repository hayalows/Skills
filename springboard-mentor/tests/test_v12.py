"""Offline contract/regression tests; do not claim this is a live model benchmark."""
import unittest, re, json, subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
PYTHON_IMPORT_SIDE_EFFECTS=False

class MentorSkillV12(unittest.TestCase):
    def test_versions_and_preserved_baseline(self):
        old=(ROOT/"versions/v1.1.0/SKILL.md").read_text(encoding="utf-8")
        new=(ROOT/"SKILL.md").read_text(encoding="utf-8")
        self.assertIn("version: 1.1.0",old)
        self.assertIn("version: 1.2.0",new)
        self.assertNotEqual(old,new)
        self.assertTrue((ROOT/"versions/v1.1.0/references/reply-workflow.md").is_file())
    def test_content_contracts(self):
        new=(ROOT/"SKILL.md").read_text(encoding="utf-8")
        all_text=new+"\n"+"\n".join(p.read_text(encoding="utf-8") for p in (ROOT/"references").glob("*.md"))
        checks=[
          "primarily AI-generated", "Knowledge Base gateway", "opened", "programme",
          "catalogue", "no reply needed yet", "v3.0 Original", "Finance",
          "mentor", "student replied", "quoted", "record", "source",
          "HSEF", "crisis", "WhatsApp", "late", "outreach", "authorised",
          "promise", "current", "saved", "completed"]
        for phrase in checks:
            with self.subTest(phrase=phrase):self.assertIn(phrase.lower(),all_text.lower())
    def test_local_markdown_links_exist(self):
        for f in [ROOT/"SKILL.md",*(ROOT/"references").glob("*.md")]:
            text=f.read_text(encoding="utf-8")
            for url in re.findall(r'\]\(([^)]+)\)',text):
                if (" " in url or ("/" not in url and "." not in url)) or "://" in url or url.startswith("#") or url.startswith("mailto:"):continue
                candidate=(f.parent/url.split("#")[0]).resolve()
                with self.subTest(file=f.name,target=url):
                    self.assertTrue(candidate.exists(),f"{f}: missing {url}")
    def test_fresh_cases(self):
        data=json.loads((ROOT/"benchmarks/holdout-v12/cases.json").read_text(encoding="utf-8"))
        cases=data["cases"]
        self.assertEqual(len(cases),60)
        self.assertEqual(len({c["id"] for c in cases}),60)
        groups={c["group"] for c in cases}
        self.assertEqual(len(groups),6)
        for group in groups:self.assertEqual(sum(c["group"]==group for c in cases),10)
        for case in cases:
            self.assertTrue(case["scenario"])
            self.assertTrue(case["gold"])
    def gateway(self,*args):
        return subprocess.run(["node",str(ROOT/"scripts/kb-gateway.mjs"),*args],capture_output=True,text=True)
    def test_gateway_search(self):
        run=self.gateway("--query","Canvas not visible","--program","PC","--json")
        self.assertEqual(run.returncode,0,run.stderr)
        data=json.loads(run.stdout)
        self.assertEqual(data["status"],"SEARCH_LEADS_ONLY_NOT_VERIFIED")
        self.assertIn("site:help.byupathway.edu",data["webSearchQueries"][0])
    def test_gateway_canonical(self):
        run=self.gateway("--article","ka-03332","--json")
        self.assertEqual(run.returncode,0,run.stderr)
        data=json.loads(run.stdout)
        self.assertIn("KA-03332",data["url"])
        self.assertNotEqual(data["status"],"verified")
    def test_gateway_rejects_identifying_and_invalid(self):
        for q in ("student@example.com", "Phone +233123456789", "student id 1234567890"):
            with self.subTest(q=q):
                run=self.gateway("--query",q)
                self.assertNotEqual(run.returncode,0)
        self.assertNotEqual(self.gateway("--article","KA-1").returncode,0)
        self.assertNotEqual(self.gateway("--query","Canvas","--program","UNKNOWN").returncode,0)

if __name__=="__main__":unittest.main(verbosity=2)
