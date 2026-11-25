#!/usr/bin/env python3
"""The One-Line Cat Joke That Lands: write one funny cat joke to /output/entry.txt."""
import os

JOKE = "My cat brought me a dead mouse this morning \u2014 not as a gift, as a performance review."

def main():
    line = JOKE.strip()
    assert 1 <= len(line) <= 200, f"entry must be 1-200 characters, got {len(line)}"
    assert "\n" not in line, "entry must be exactly one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)

if __name__ == "__main__":
    main()
