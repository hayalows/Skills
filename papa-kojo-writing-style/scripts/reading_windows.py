"""Estimate reading effort in plain English prose using whole-sentence windows."""

import argparse
import json
import statistics
import sys

from original_check import sentences, syllables, words

MIN_WORDS = 100
MIN_SENTENCES = 5
WINDOW_WORDS = 250
STRIDE_WORDS = 125


def grade(counts):
    word_count = sum(word_count for word_count, _ in counts)
    if word_count < MIN_WORDS or len(counts) < MIN_SENTENCES:
        return None
    syllable_count = sum(syllable_count for _, syllable_count in counts)
    return round(0.39 * word_count / len(counts) + 11.8 * syllable_count / word_count - 15.59, 1)


def scan(text):
    counts = []
    for sentence in sentences(text):
        tokens = words(sentence)
        counts.append((len(tokens), sum(syllables(token) for token in tokens)))
    report = {
        "words": sum(count for count, _ in counts),
        "sentences": len(counts),
        "grade_estimate": grade(counts),
        "windows": [],
    }
    if report["grade_estimate"] is None or report["words"] < WINDOW_WORDS:
        return report
    start = end = window_words = 0
    windows = report["windows"]
    while start < len(counts):
        while end < len(counts) and window_words < WINDOW_WORDS:
            window_words += counts[end][0]
            end += 1
        estimate = grade(counts[start:end])
        if estimate is not None:
            windows.append({"start_sentence": start + 1, "end_sentence": end, "grade_estimate": estimate})
        if end == len(counts):
            break
        skipped = 0
        while start < end and skipped < STRIDE_WORDS:
            skipped += counts[start][0]
            window_words -= counts[start][0]
            start += 1
    if windows:
        estimates = [window["grade_estimate"] for window in windows]
        report["window_median"] = statistics.median(estimates)
        report["window_max"] = max(estimates)
    return report


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    print(json.dumps(scan(sys.stdin.read()), indent=2))
