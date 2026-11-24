# Thought-specific shape development pilot

Ten synthetic brief-matched short essays, first drafted by the same model using Original 3.0.4 guidance, then selectively revised with the proposed thought-specific shape workflow. Initial texts were written before the paired revisions. These are not the user's personal statements, independent generation sessions, blinded judgments or a representative sample. No fabricated autobiographical claims are evidence of the user's voice. Two unchanged drafts are intentional. The first revision of this batch removed every explicit example marker and concentrated most essays into two paragraphs. A second editorial review retained a useful invitation and a longer development where the subject needed it; the final pairs below are the accepted development drafts. The initial set's uniformity is itself a feature of this single-batch example, not an estimate of all v3.0.4 outputs.

Reproduce using Python 3 and the frozen independent checker v1.0.0 (commit b23c097):
```sh
python3 papa-kojo-writing-style/benchmarks/shape-pilot/run.py
python3 -m unittest discover -s papa-kojo-writing-style/tests -p test_batch_shape_review.py
```
If running against a later checker, provide --checker-root pointing to the pinned independent-voice-checker folder. The pilot uses its heuristic mode for all drafts; the scores are estimates. Reports of phrase/position repetition are diagnostic, not a quality measure. For short texts the strict target verdict is withheld; review readability, voice and claims manually. The exact paired texts and briefs are in drafts.json. For a future independent test, freeze new briefs and judge prompts before separate generation runs; preserve the required facts and compare actual reader preference as well as measurable scaffolds. Do not train on the holdout.
