#!/usr/bin/env python3
"""One Line, Big Laugh entry.

Writes a single funny line (at most 200 characters, one line, no title
or explanation) to entry.txt. Standard library only, no network,
no secrets, fully deterministic: the same line every run.
"""

import os

LINE = (
    "My smoke detector saves its low-battery chirp for 3 a.m., "
    "which means either it's dying or it spent weeks rehearsing its 3 a.m. solo."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
