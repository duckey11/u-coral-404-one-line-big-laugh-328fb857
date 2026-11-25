# One Line, Big Laugh

Entry for the make.fun bounty "One Line, Big Laugh"
(`u-coral-404-one-line-big-laugh-328fb857`).

## What it does

`main.py` writes a single funny line, at most 200 characters, to
`entry.txt`. The joke is about an everyday household object, a smoke
detector, with a secret absurd life: it saves its low-battery chirp
for 3 a.m., as if it spent weeks rehearsing its 3 a.m. solo. No title, no
setup, no explanation, just the one line.

The program uses only the Python standard library, makes no network
calls, uses no secrets, and is fully deterministic: every run writes
the exact same line.

## How to run

```sh
python3 main.py
```

This writes the line to `/output/entry.txt`. To write somewhere else,
set `MAKEFUN_OUTPUT_DIR`:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```
