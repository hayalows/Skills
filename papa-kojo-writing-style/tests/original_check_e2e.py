#!/usr/bin/env python3
"""End-to-end checks for scripts/original_check.py through its command line."""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(args, text):
    p = subprocess.run([sys.executable, str(ROOT / "scripts" / "original_check.py"), *args],
                       input=text, text=True, capture_output=True)
    if p.returncode != 0:
        raise AssertionError(p.stderr)
    return json.loads(p.stdout) if "--json" in args else p.stdout


def ids(args, text):
    return {f["id"] for f in run([*args, "--json"], text)["flags"]}


def check(ok, msg):
    if not ok:
        raise AssertionError(msg)


def test_flips_he_rejected():
    check("contrast_flip" in ids(["--register", "post"], "Most people don't run out of money on a big day. They run out on the small ones."), "split flip missed")
    check("contrast_flip" in ids(["--register", "post"], "A bigger income gives you room. It does not decide what you do with that room."), "soft flip missed")
    check("contrast_flip" in ids(["--register", "post"], "At Hayalows, we don't just manage numbers; we build futures."), "brand flip missed")
    check("contrast_flip" in ids(["--register", "post"], "In many cases the money was made. It is just stuck in two places."), "soft reversal missed")


def test_labels_and_endings():
    check("label_before_point" in ids(["--register", "post"], "The reason is often simple. Stock goes out on credit."), "label missed")
    check("moral_closer" in ids(["--register", "longform"], "We listened. And that is what real friendship means."), "moral missed")
    check("sales_template" in ids(["--register", "post"], "Still writing customer orders on paper? Try this."), "sales question missed")


def test_no_false_alarm_on_plain_writing():
    plain = ("The shop is busy every day, but the cash is not in the drawer. Some of it went to the supplier, "
             "because the stock was bought on credit and the bill came due on Monday. The rest is with customers "
             "who said they would pay at the end of the month.\n\nSo before you buy more stock, write down who owes you "
             "and when they said they would pay. I think that one list will tell you more than the busy days do.")
    found = ids(["--register", "post"], plain)
    check(not found, f"plain writing flagged: {found}")


def test_register_rules():
    check("register_contractions" in ids(["--register", "formal"], "I'm applying for the internship and I've built two products."), "formal contractions missed")
    check("register_contractions" not in ids(["--register", "chat"], "I'm sorry bro, I can't this month."), "chat contractions wrongly flagged")
    check("register_emoji" not in ids(["--register", "comment"], "Congrats, Akosua! 🎉"), "comment emoji wrongly flagged")
    check("register_emoji" in ids(["--register", "message"], "Dear Mr Boateng, thank you 🙏🏾"), "message emoji missed")


def test_too_fast():
    fast = "Track it. Write it down. Check it daily. Cut waste. Save more. Repeat weekly."
    check("too_fast" in ids(["--register", "post"], fast), "rushed rhythm missed")


def test_metrics_and_plain_output():
    data = run(["--register", "message", "--json"], "A fare was GH₵2.50. Another fare was GH₵4.00.")
    check(data["metrics"]["sentences"] == 2, "decimal split wrongly")
    check(data["version"] == "3.0.0", "version missing")
    out = run(["--register", "chat"], "Congrats, big man!")
    check("ORIGINAL CHECK" in out, "plain output missing")
    empty = run(["--json"], "   ")
    check(empty["metrics"]["words"] == 0, "empty input broke")


def test_skill_links():
    skill = (ROOT / "SKILL.md").read_text()
    for path in ["references/voice-bank.md", "references/register-dial.md", "references/revision-recipes.md",
                 "references/version-history.md", "scripts/original_check.py", "versions/v1.2.1/README.md"]:
        check(path in skill, f"SKILL.md does not link {path}")
        check((ROOT / path).exists(), f"{path} missing")
    check("version: 3.0.0" in skill and "codename: Original" in skill, "version label missing")
    check("—" not in skill, "SKILL.md uses an em dash")


TESTS = [test_flips_he_rejected, test_labels_and_endings, test_no_false_alarm_on_plain_writing,
         test_register_rules, test_too_fast, test_metrics_and_plain_output, test_skill_links]

if __name__ == "__main__":
    failed = 0
    for t in TESTS:
        try:
            t()
            print("PASS", t.__name__)
        except Exception as e:
            failed += 1
            print("FAIL", t.__name__, e)
    print(f"{len(TESTS) - failed}/{len(TESTS)} scenarios passed")
    sys.exit(1 if failed else 0)
