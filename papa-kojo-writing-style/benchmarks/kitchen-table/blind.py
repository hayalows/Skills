#!/usr/bin/env python3
"""Build blind judging packets and unblind the scores for the Kitchen Table Benchmark.

  python3 blind.py pack  --briefs round-1/briefs.md --drafts round-1/drafts --out work/ --tag J1 --seed 101
  python3 blind.py score --judging round-1/judging --tags J1,J2,J3

Writers and judges must run in separate sessions that cannot see each other's
files or the *_key.json answer keys. Scores are editorial opinions, not proof
of authorship or of Papa Kojo's own judgement.
"""
import argparse
import glob
import json
import os
import random
import re
import statistics as st

DIMS = ["human", "voice", "flow", "clarity", "fit", "person", "truth", "habits"]


def pieces(text):
    parts = re.split(r"^## ([BH]\d\d)\s*$", text, flags=re.M)
    return {parts[i]: parts[i + 1].strip() for i in range(1, len(parts), 2)}


def briefs(path):
    raw = open(path).read()
    return {m.group(1): m.group(2).strip() + "\n" + m.group(3).strip()
            for m in re.finditer(r"^## ([BH]\d\d) ([^\n]*)\n(.*?)(?=^## [BH]|\Z)", raw, re.S | re.M)}


def pack(a):
    names = sorted(os.path.basename(f)[:-3] for f in glob.glob(os.path.join(a.drafts, "*.md")))
    if a.only:
        names = [n for n in names if n in a.only.split(",")]
    drafts = {n: pieces(open(os.path.join(a.drafts, n + ".md")).read()) for n in names}
    bs = briefs(a.briefs)
    rnd = random.Random(a.seed)
    labels = [chr(65 + i) for i in range(len(names))]
    key, lines = {}, []
    for b in sorted(bs):
        order = names[:]
        rnd.shuffle(order)
        key[b] = dict(zip(labels, order))
        lines.append(f"# {b}: {bs[b]}\n")
        lines += [f"### Draft {lab}\n{drafts[n][b]}\n" for lab, n in zip(labels, order)]
    os.makedirs(a.out, exist_ok=True)
    open(os.path.join(a.out, f"{a.tag}_packet.md"), "w").write("\n".join(lines))
    json.dump(key, open(os.path.join(a.out, f"{a.tag}_key.json"), "w"), indent=1)
    print(f"{a.tag}: {len(bs)} briefs x {len(names)} drafts")


def score(a):
    agg, wins, ranks, per = {}, {}, {}, {}
    for tag in a.tags.split(","):
        s = json.load(open(os.path.join(a.judging, f"{tag}_scores.json")))
        k = json.load(open(os.path.join(a.judging, f"{tag}_key.json")))
        for b, m in k.items():
            order = s[b]["rank"]
            for lab, n in m.items():
                d = agg.setdefault(n, {x: [] for x in DIMS})
                for x in DIMS:
                    d[x].append(s[b][lab][x])
                ranks.setdefault(n, []).append(order.index(lab) + 1)
            w = m[order[0]]
            wins[w] = wins.get(w, 0) + 1
            per.setdefault(b, []).append(w)
    rows = []
    for n, d in agg.items():
        means = {x: st.mean(d[x]) for x in DIMS}
        rows.append((st.mean(means.values()), n, means))
    print(f"{'version':16}" + "".join(f"{x[:6]:>7}" for x in DIMS) + f"{'avg':>7}{'rank':>6}{'#1':>4}")
    for avg, n, means in sorted(rows, reverse=True):
        print(f"{n:16}" + "".join(f"{means[x]:>7.2f}" for x in DIMS) + f"{avg:>7.2f}{st.mean(ranks[n]):>6.2f}{wins.get(n, 0):>4}")
    if a.save:
        json.dump({"agg": {n: m for _, n, m in rows}, "wins": wins,
                   "rank": {n: st.mean(r) for n, r in ranks.items()}, "per_brief_winners": per},
                  open(a.save, "w"), indent=1)


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    q = sub.add_parser("pack")
    q.add_argument("--briefs", required=True)
    q.add_argument("--drafts", required=True)
    q.add_argument("--out", required=True)
    q.add_argument("--tag", required=True)
    q.add_argument("--seed", type=int, default=1)
    q.add_argument("--only", help="comma list of version names to include")
    r = sub.add_parser("score")
    r.add_argument("--judging", required=True)
    r.add_argument("--tags", required=True)
    r.add_argument("--save")
    a = p.parse_args()
    pack(a) if a.cmd == "pack" else score(a)
