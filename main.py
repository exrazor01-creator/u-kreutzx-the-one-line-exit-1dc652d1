#!/usr/bin/env python3
"""Entry for The One-Line Exit.

Writes a single-line resignation letter (at most 200 characters) to
/output/entry.txt and prints it to stdout. Pure standard library.
"""

import os

LETTER = "I hereby resign, effective immediately, because the printer has been promoted to middle management and I refuse to report to a machine that jams under pressure."

def main():
    # The bounty judges one line only: keep the letter a single line of
    # at most 200 characters, with no trailing newline in the entry file.
    assert 1 <= len(LETTER) <= 200, f"letter length {len(LETTER)} out of range"
    assert "\n" not in LETTER and "\r" not in LETTER, "letter must be a single line"
    assert LETTER.strip(), "letter must not be only whitespace"
    assert LETTER == LETTER.strip(), "letter must not start or end with whitespace"
    assert "  " not in LETTER, "letter must not contain double spaces"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LETTER)
    print(LETTER)

if __name__ == "__main__":
    main()
