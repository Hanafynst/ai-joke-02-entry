#!/usr/bin/env python3
"""ai-joke-02 entry: write one original one-liner about AI coding agents
to /output/entry.txt. Standard library only, no network, deterministic:
two runs write the same bytes. Outside the grader's container,
MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

JOKE = "My coding agent fixed my bug in four seconds, then spent forty minutes explaining why the bug was my fault. It was right."

def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(JOKE, encoding="utf-8")

if __name__ == "__main__":
    main()
