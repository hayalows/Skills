#!/usr/bin/env python3
"""voice_dice.py: roll a fresh writing recipe so the same prompt never comes out the same way twice.
Usage: python3 voice_dice.py            (random)
       python3 voice_dice.py --seed 7   (repeatable)
       add --quote only when the brief gives a real quote to open with
If you can't run code, pick each line yourself, and never take the first option that comes to mind."""
import random, sys

seed = None
if "--seed" in sys.argv:
    seed = int(sys.argv[sys.argv.index("--seed") + 1])
r = random.Random(seed)
has_quote = "--quote" in sys.argv  # pass --quote only when the brief gives a real quote

ENTRY = [
 "a scene: one small moment with a time, a place and an object in it",
 "a plain fact the reader can check (a number, a price, a name, a date)",
 "a question you actually wonder about, left open for a few lines",
 "an honest admission (something hard, slow or wrong, in the writer's own life ONLY if the brief gives it; otherwise 'you' or 'a friend' in a clearly general scene)",
 "something someone said, in their own words (only if the brief gives it)",
 "the result first, then walk back to how it happened",
 "a short instruction, as if mid-conversation",
 "an everyday object that holds the whole idea",
]
SHAPE = [
 "a chain: this happens, so that happens, which means this (link with because / so / which means)",
 "a tiny story with a turn in the middle, told in order",
 "a slow zoom: start wide, end on one small concrete thing",
 "two pictures side by side, let the reader feel the gap (no 'not X, but Y' sentence)",
 "a list of 2 or 4 real things, then one line on what they share",
 "a question, a wander through it, an honest partial answer",
 "answer first, then the one reason that matters, then an example",
]
PICTURE = [
 "home and family", "money and the market", "school and learning", "church and service",
 "work and the office", "the road (trotro, traffic, walking)", "food and cooking",
 "football and sport", "the phone and the internet", "farming, weather, the seasons",
 "building and fixing things", "light-off, water, the small daily hassles",
]
RHYTHM = [
 "mostly medium sentences, one long one that runs on a bit, one short one",
 "start short, get longer as the idea opens up",
 "conversational, with one aside in brackets",
 "steady and even, one longer reflective sentence near the end",
]
ENDING = [
 "stop on the concrete image, no moral",
 "one small thing to try today",
 "an honest open question you still have",
 "a callback to the first line, changed a little",
 "end on the plain fact, let the reader do the thinking",
 "a quiet personal line (what the writer will do, only if true to the brief)",
]
entries = ENTRY if has_quote else [e for e in ENTRY if not e.startswith("something someone said")]
print(f"Entry:   {r.choice(entries)}")
print(f"Shape:   {r.choice(SHAPE)}")
print(f"Picture: draw the comparison from {r.choice(PICTURE)}")
print(f"Rhythm:  {r.choice(RHYTHM)}")
print(f"Ending:  {r.choice(ENDING)}")
print(f"Length:  {r.choice(['the low end of the format range', 'the middle of the format range', 'the high end of the format range'])}")
