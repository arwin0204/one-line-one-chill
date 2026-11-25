"""One Line, One Chill — make.fun bounty u-azazex-one-line-one-chill-6d4d5488.

Writes a single line of horror (under 200 characters) to entry.txt.
Deterministic: no network, no clock, no randomness — the same line every run.

Fix (2026-11-25): the original wrote entry.txt into the repository
directory first. In the grader the repo is mounted read-only at /bot,
so that write raised PermissionError and the run exited 1
(run_completes fail). Now writes ONLY to the grader's output
directory (MAKEFUN_OUTPUT_DIR, fallback /output).
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
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
