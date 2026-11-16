#!/usr/bin/env python3
"""End-to-end acceptance checks using the public CLI entry points."""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(script, args=(), stdin=""):
    return subprocess.run([sys.executable, str(ROOT / "scripts" / script), *args],
                          input=stdin, text=True, capture_output=True)


def check(ok, message):
    if not ok:
        raise AssertionError(message)


def test_dice_seed_and_relevance():
    p = run("voice_dice.py", ["--format", "linkedin", "--topic", "small daily spending", "--seed", "7", "--json"])
    check(p.returncode == 0, p.stderr)
    data = json.loads(p.stdout)
    check(data["mode"] == "suggestions", "LinkedIn should get suggestions")
    check(data["picture"] in ["none", "money and payments"], "unrelated forced domain")
    check(run("voice_dice.py", ["--format", "linkedin", "--topic", "small daily spending", "--seed", "7", "--json"]).stdout == p.stdout, "seed not stable")
    p2 = run("voice_dice.py", ["--format", "linkedin", "--topic", "small daily spending", "--seed", "23", "--json"])
    check(p2.returncode == 0 and p.stdout != p2.stdout, "different seeds should vary")


def test_dice_skips_and_quote_safety():
    for fmt in ["email", "whatsapp", "rewrite", "application", "comment"]:
        p = run("voice_dice.py", ["--format", fmt, "--seed", "3", "--json"])
        check(p.returncode == 0, p.stderr)
        check(json.loads(p.stdout)["mode"] == "skip", f"{fmt} must take shape from the job")
    p = run("voice_dice.py", ["--format", "essay", "--seed", "4", "--json"])
    check("supplied quote" not in p.stdout, "cannot invent quotation")
    bad = run("voice_dice.py", ["--format", "linkedin", "--seed", "4", "--domains", "football,market", "--json"])
    check(bad.returncode == 0, bad.stderr)
    check(json.loads(bad.stdout)["picture"] in ["none", "football and sport", "money and payments"], "domain allowlist ignored")


def test_checker_pattern_and_false_positive():
    p = run("voice_check.py", ["--format", "reflective", "--json"], "Most people don't run out of money on a big day. They run out on the small ones.")
    check(p.returncode == 0, p.stderr)
    data = json.loads(p.stdout)
    ids = {f["id"] for f in data["flags"]}
    check("sweeping_opener" in ids and "negative_flip" in ids, f"missed v1.1 problem: {ids}")
    p = run("voice_check.py", ["--format", "reflective", "--json"], "The problem is a broken tap. We fixed it on Friday.")
    check(p.returncode == 0, p.stderr)
    check("label_reveal" not in {f["id"] for f in json.loads(p.stdout)["flags"]}, "ordinary explanation false positive")


def test_checker_preserves_context():
    comment = "Congrats, brother. You've worked hard for this and you deserve it!"
    p = run("voice_check.py", ["--format", "comment", "--json"], comment)
    check(p.returncode == 0, p.stderr)
    data = json.loads(p.stdout)
    check(data["metrics"]["sentences"] == 2, "bad sentence detection")
    check("punctuation_exclamation" not in {f["id"] for f in data["flags"]}, "genuine casual exclamation shouldn't be banned")
    decimal = run("voice_check.py", ["--json"], "A fare was GH₵2.50. Another fare was GH₵4.00.")
    check(json.loads(decimal.stdout)["metrics"]["sentences"] == 2, "decimal punctuation divided into extra sentences")
    empty = run("voice_check.py", ["--json"], "   ")
    check(empty.returncode == 0 and json.loads(empty.stdout)["metrics"]["words"] == 0, "empty input error")


def test_checker_banned_and_scope():
    t = "We must ensure the payment arrives. We will leverage this robust opportunity."
    p = run("voice_check.py", ["--format", "application", "--json"], t)
    data = json.loads(p.stdout)
    check("user_avoid_word" in {f["id"] for f in data["flags"]}, "didn't flag banned words")
    check(data["metrics"]["words"] >= 10, "wrong word count")
    p = run("voice_check.py", ["--format", "email", "--json"], "Dear Ama, thank you for your note. I'll share the file tomorrow.")
    check(p.returncode == 0 and json.loads(p.stdout)["format"] == "email", "email not supported")


def test_packaging_and_advice():
    skill = (ROOT / "SKILL.md").read_text()
    for path in ["references/anti-slop.md", "references/voice-profile.md", "references/craft-sources.md", "scripts/voice_dice.py", "scripts/voice_check.py", "tests/cli_e2e.py"]:
        check(path in skill, f"missing reference {path}")
    check("version: 1.2" in skill, "version label missing")
    check("meaning" in skill.lower() and "facts" in skill.lower(), "factual safeguards missing")
    test = run("voice_dice.py", ["--format", "reflective"])
    check(test.returncode == 0 and "Entry:" in test.stdout, "legacy plain text usage broken")
    check(run("voice_check.py", stdin="Hello, Ama. I'll send it tomorrow.").returncode == 0,
          "legacy stdin check broken")


TESTS = [test_dice_seed_and_relevance, test_dice_skips_and_quote_safety,
         test_checker_pattern_and_false_positive, test_checker_preserves_context,
         test_checker_banned_and_scope, test_packaging_and_advice]
if __name__ == "__main__":
    failures = []
    for test in TESTS:
        try:
            test()
            print("PASS", test.__name__)
        except Exception as e:
            failures.append((test.__name__, str(e)))
            print("FAIL", test.__name__, str(e))
    print(f"{len(TESTS) - len(failures)}/{len(TESTS)} scenarios passed")
    sys.exit(1 if failures else 0)
