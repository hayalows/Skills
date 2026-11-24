#!/usr/bin/env python3
"""Compare supplied draft openings and endings. Advisory, not quality scoring."""
import argparse
from itertools import combinations
import json
from pathlib import Path
import re
from batch_shape_review import prose, tokens

VERSION = "1.0.0"

def edges(text):
    parts = [p for p in re.split(r"\n\s*\n", prose(text)) if tokens(p)]
    if not parts:
        return {"opening": [], "closing": [], "paragraphs": 0}
    return {"opening": tokens(parts[0]), "closing": tokens(parts[-1]),
            "paragraphs": len(parts)}

def grams(ws, size=3):
    return {tuple(ws[i:i+size]) for i in range(len(ws)-size+1)}

def review(documents, threshold=.55, min_words=12):
    if not 0 < threshold <= 1 or min_words < 3:
        raise ValueError("Invalid overlap parameters")
    ds = [(doc_id, edges(text)) for doc_id, text in documents]
    if len({i for i, _ in ds}) != len(ds):
        raise ValueError("Duplicate document ID")
    candidates = []
    for (a, x), (b, y) in combinations(ds, 2):
        for edge in ("opening", "closing"):
            # A one-paragraph message has one edge, not two independent observations.
            if edge == "closing" and x["paragraphs"] == y["paragraphs"] == 1:
                continue
            u, v = x[edge], y[edge]
            if not u or not v:
                continue
            exact = u == v
            g, h = grams(u), grams(v)
            overlap = len(g & h) / len(g | h) if g | h else None
            if exact or (min(len(u), len(v)) >= min_words and overlap is not None and overlap >= threshold):
                candidates.append({"documents":[a,b], "edge":edge,
                    "kind":"normalized_exact" if exact else "shared_trigrams",
                    "jaccard": round(overlap, 3) if overlap is not None else None,
                    "words":[len(u),len(v)]})
    return {"version":VERSION,"documents":len(ds),"threshold":threshold,
            "minimum_words_for_near":min_words,"candidates":candidates,
            "notice":"Review comparable drafts in context. Exact wording, names and standard forms may be appropriate. No claim of uniqueness, quality or authorship."}

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("drafts",nargs="+",type=Path)
    p.add_argument("--threshold",type=float,default=.55)
    p.add_argument("--min-words",type=int,default=12)
    a=p.parse_args()
    try:
        r=review([(str(f),f.read_text(encoding="utf-8")) for f in a.drafts],a.threshold,a.min_words)
        print(json.dumps(r,ensure_ascii=False,indent=2))
    except (OSError,ValueError) as e:
        p.error(str(e))
if __name__=="__main__": main()
