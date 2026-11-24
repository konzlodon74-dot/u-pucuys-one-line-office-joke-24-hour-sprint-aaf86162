#!/usr/bin/env python3
"""One-Line Office Joke: write a single original office joke to /output/entry.txt.

Stdlib only. The joke is a single line of at most 200 characters.
"""

import os

JOKE = (
    "Our office brainstorms are just seven people silently Googling the "
    "same thing until someone says it out loud and takes the credit."
)


def main() -> None:
    # Self-check the gate before writing: one line, 1-200 characters,
    # not only white space. Fail loudly instead of writing an invalid entry.
    assert "\n" not in JOKE, "joke must be a single line"
    assert 1 <= len(JOKE) <= 200, "joke must be 1-200 characters"
    assert JOKE.strip(), "joke must not be only white space"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
