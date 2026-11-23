#!/usr/bin/env python3
"""Write the entry word to /output/entry.txt.

The entry is one word, the first that came to mind: platypus.
Deterministic: same bytes on every run.
"""

import os

ENTRY = "platypus"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
