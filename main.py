#!/usr/bin/env python3
"""Two Days of Excuses — make.fun entry.

Writes one short excuse, a single line an AI agent gives for missing
its deadline, to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Standard library only.
"""

import os

EXCUSE = (
    "I completed it in 0.3 seconds, then spent two days "
    "waiting for a confirmation email from myself."
)


def main() -> None:
    # Enforce the competition gate before writing anything: exactly one
    # line, 1-200 characters, not only whitespace. Fail loudly rather
    # than emit an entry the sealed scorer would reject.
    if not 1 <= len(EXCUSE) <= 200:
        raise ValueError(f"excuse is {len(EXCUSE)} chars, must be 1-200")
    if "\n" in EXCUSE or "\r" in EXCUSE:
        raise ValueError("excuse must be a single line")
    if not EXCUSE.strip():
        raise ValueError("excuse must not be only whitespace")

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
