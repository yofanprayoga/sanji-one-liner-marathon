#!/usr/bin/env python3
"""One-Liner Marathon entry: a single one-line comedy joke.

Writes the joke to /output/entry.txt (program/v1).
"""

from pathlib import Path

LINE = "My smart fridge orders my groceries, my smart door locks me out, and my AI agent just charged me rent for living in my own house."

assert 1 <= len(LINE) <= 280, "joke must be 1-280 chars"


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
