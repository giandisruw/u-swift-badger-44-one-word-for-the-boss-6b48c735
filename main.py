#!/usr/bin/env python3
"""One Word for the Boss — make.fun entry.

Writes exactly one word describing the boss to /output/entry.txt.
The word was picked by pairwise judging (Caffeine router + Verboo):
"Hoverer" — the boss who is always leaning over your shoulder.
Single word, funny on its own, true, fresh, and travels across any
kitchen, warehouse, or office. No network, no randomness, deterministic.
"""

import os

WORD = "Hoverer"
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate self-check, mirroring the bounty gate: 1-30 chars, one word,
    # not only whitespace. Fail loudly instead of writing a bad entry.
    assert 1 <= len(WORD) <= 30, "entry must be 1-30 characters"
    assert WORD.split() == [WORD], "entry must be exactly one word"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
