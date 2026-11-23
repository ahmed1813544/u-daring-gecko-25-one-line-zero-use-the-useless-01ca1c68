#!/usr/bin/env python3
"""Write one useless-superpower one-liner to /output/entry.txt.

Stdlib only, deterministic: the same line on every run.
"""

import os

LINE = (
    "I can teleport anywhere in the world, but only to places I've "
    "already been, and only if I was going to walk there anyway."
)


def main() -> None:
    # Self-check against the gate: 1 to 200 characters, not only whitespace.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars"
    assert LINE.strip(), "line must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
