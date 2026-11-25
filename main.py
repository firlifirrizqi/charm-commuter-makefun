"""Charm the Commuter: Forecast a City That Isn't entry for Make.fun.

Writes a single one-line weather forecast for an imaginary city
to /output/entry.txt. Standard library only; nothing to install.
"""

import os

ENTRY = (
    "Hari ini di Hujanpayung: gerimis payung mini, jadi jangan bawa "
    "payung \u2014 tangkap saja satu yang jatuh di halte."
)

OUTPUT_PATH = "/output/entry.txt"

# Competition gate: one forecast line, at most 140 characters.
MAX_CHARS = 140


def verify() -> None:
    """Re-read the output and assert it is byte-identical to ENTRY."""
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        content = f.read()
    assert content == ENTRY, "output differs from ENTRY"
    assert content.encode("utf-8").decode("utf-8") == content
    assert 1 <= len(content) <= MAX_CHARS, (
        f"length {len(content)} out of range 1-{MAX_CHARS}"
    )
    assert content.strip(), "entry is only whitespace"
    assert "\n" not in content, "entry must be a single line"
    assert "Hujanpayung" in content, "entry must name the imaginary city"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    verify()


if __name__ == "__main__":
    main()
