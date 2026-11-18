"""Build a judge packet and a separate answer key from JSON drafts."""
import argparse
import json
from pathlib import Path
import random


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("briefs", type=Path)
    parser.add_argument("packet", type=Path)
    parser.add_argument("key", type=Path)
    parser.add_argument("drafts", nargs="+", type=Path)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--reverse", action="store_true")
    args = parser.parse_args()
    drafts = {path.stem: json.loads(path.read_text()) for path in args.drafts}
    if len(drafts) != len(args.drafts) or len(drafts) < 2:
        parser.error("Provide at least two drafts with distinct filenames.")
    ids = tuple(next(iter(drafts.values())))
    if not ids or any(set(draft) != set(ids) for draft in drafts.values()):
        parser.error("All drafts must cover the same brief IDs.")
    rng = random.Random(args.seed)
    packet = {
        "briefs": args.briefs.read_text(),
        "instructions": "For each brief rank candidates by truth and requested format first, "
        "then voice, flow, register and clarity. Allow ties. Cite concrete wording. "
        "A reading grade is not a voice score.",
        "responses": {},
    }
    key = {}
    for brief in ids:
        order = sorted(drafts)
        rng.shuffle(order)
        if args.reverse:
            order.reverse()
        aliases = {str(i + 1): name for i, name in enumerate(order)}
        key[brief] = aliases
        packet["responses"][brief] = {alias: drafts[name][brief] for alias, name in aliases.items()}
    args.packet.write_text(json.dumps(packet, ensure_ascii=False, indent=2) + "\n")
    args.key.write_text(json.dumps(key, indent=2) + "\n")


if __name__ == "__main__":
    main()
