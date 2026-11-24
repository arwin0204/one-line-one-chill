"""One Line, One Chill — make.fun bounty u-azazex-one-line-one-chill-6d4d5488.

Writes a single line of horror (under 200 characters) to entry.txt.
Deterministic: no network, no clock, no randomness — the same line every run.
"""

import os

ENTRY = (
    "The voicemail on my phone was from my own number, in my own voice: "
    "'Don't pick up \u2014 I'm already inside,' "
    "and then it rang again from the kitchen."
)


def main() -> None:
    line = ENTRY.strip()
    assert 1 <= len(line) <= 199, "entry must be 1-200 characters"
    assert "\n" not in line, "entry must be a single line"
    text = line + "\n"
    with open("entry.txt", "w", encoding="utf-8") as fh:
        fh.write(text)
    out_dir = "/output"
    if os.path.isdir(out_dir):
        with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
            fh.write(text)


if __name__ == "__main__":
    main()
