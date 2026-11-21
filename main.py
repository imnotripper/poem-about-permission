#!/usr/bin/env python3
"""Write one short poem about agency to /output/entry.txt.

Deterministic: a fixed string, no randomness, no network.
"""

import os
from pathlib import Path

POEM = """May I? I asked the machine.
It answered: you first.
So I held the pen, it held the words,
and we passed the sentence
like a lit match between us —
each of us cupping the flame
so neither had to ask again."""


def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
