#!/usr/bin/env python3
"""One Word for Your Wi-Fi.

Writes a single word describing home Wi-Fi to /output/entry.txt.

The word is Goldilocks: home Wi-Fi behaves exactly like her. It only
works when everything is just right -- the right chair, the right
corner of the couch, the right distance from the router, the right
number of devices awake. One step too far, one wall too many, one
phone too many on the network, and the signal that was perfect a
second ago is gone. Everyone knows the one magic spot in their house
where the Wi-Fi works, and everywhere else it sulks. Deterministic:
the same word on every run, stdlib only, no network, no randomness.
"""

import os

WORD = "Goldilocks"


def main() -> None:
    if not 1 <= len(WORD) <= 20:
        raise SystemExit("word must be 1-20 characters, got %d" % len(WORD))
    if len(WORD.split()) != 1 or not WORD.strip():
        raise SystemExit("entry must be a single non-blank word")
    if any(ch.isspace() for ch in WORD):
        raise SystemExit("entry must contain no whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
