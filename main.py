#!/usr/bin/env python3
"""One Line, Big Laugh entry.

Writes one joke line to /output/entry.txt. The program is fully
deterministic: it writes the same single line on every run, with no
network access, no randomness, and no input besides this file.
"""

import os
from pathlib import Path

LINE = (
    "My password manager locked me out for suspicious activity. "
    "The suspect: me, at 2:47 a.m., googling my own birthday "
    "to answer my own security question."
)

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise ValueError("entry line must be 1 to 200 characters of text")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(LINE, encoding="utf-8")
    os.chmod(OUTPUT, 0o644)
    print(f"Wrote {len(LINE)} characters to {OUTPUT}")


if __name__ == "__main__":
    main()
