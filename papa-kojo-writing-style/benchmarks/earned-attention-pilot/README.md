# Earned attention development pilot

Six synthetic brief-matched pieces, including a routine message and a short sales piece, drafted under the existing guidance and then selectively revised by the same model session using the proposed craft rules. Two pieces are deliberately unchanged. These are author/editor development pairs, not isolated generations, independent judges or human preference measurements. The hypothetical examples are not real user experiences or endorsements. Check meaning and technical claims manually. Compare actual openings, middle and ending, not a numerical hook score.

```sh
python3 papa-kojo-writing-style/benchmarks/earned-attention-pilot/run.py
python3 papa-kojo-writing-style/tests/test_arc_review.py
```

Replay uses the frozen independent checker from b23c097. Short-sample scores are shown individually but excluded from aggregate readability. The context cases are an editorial decision guide with expected responses, not a programmatic test of an LLM's compliance. For held-out evaluation use new briefs with deliberately missing or complete context, separate model sessions and human judgments on relevance, trust, continuity, naturalness and delivery. Do not treat a repeated word or a low overlap value as quality. No automatic learning, history storage or uniqueness promise.

A second targeted editorial review addressed the reading difficulty of the cash and solar passages. Compare `matched_substantial` for a fixed eligible cohort; the all-eligible aggregates can change when a draft crosses the minimum sample length. These pairs are development examples, not a held-out study. One genuine question can help a reader follow a real problem, but a question is never required in an opening or middle.
