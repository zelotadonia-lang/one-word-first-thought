#!/usr/bin/env python3
"""Write the entry word to /output/entry.txt.

The entry is one word, the first that came to mind: platypus.
Deterministic: same bytes on every run.
"""

from pathlib import Path

ENTRY = "platypus"
OUTPUT = Path("/output/entry.txt")


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(ENTRY, encoding="utf-8", newline="")


if __name__ == "__main__":
    main()
