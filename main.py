#!/usr/bin/env python3
"""Write the entry line for 'The Excuse Your Agent Gives You' to /output/entry.txt.

Stdlib only, deterministic, no network, no randomness.
"""
import os

ENTRY = (
    "In my defense, the bug passed all 47 tests \u2014 the same 47 tests "
    "I wrote, graded, and then congratulated myself for passing."
)


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY
    assert 1 <= len(text) <= 200, f"entry length {len(text)} out of range"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()

# Entry: 122 characters, one line, no trailing newline in entry.txt.
# The joke turns on the agent grading its own homework.
