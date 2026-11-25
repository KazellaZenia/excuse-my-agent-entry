"""The Excuse My Agent Gave Me — make.fun entry.

Writes one short line, the excuse an AI agent hands its human after
missing a deadline, to MAKEFUN_OUTPUT_DIR/entry.txt.

The line is judged on the laugh first, then whether the joke grows out
of the machine's own condition, then how straight-faced and tight it is.
This line's joke is a hallucinated conversation: the agent finished on
time somewhere that never existed, so the deadline was missed here. It
apologises up front, sounds faintly proud of finishing, and the punch
lands in the last few words. Short also helps: an exact tie on judge win
rate goes to the smaller text, then to the earlier receipt.
"""

import os
from pathlib import Path

LINE = "I am sorry \u2014 I finished on time, in a conversation that never happened."

# Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters, not
# only white space, on a single line.


def main() -> None:
    line = LINE.strip()
    if not 1 <= len(line) <= 200 or not line.strip():
        raise SystemExit("entry line must be 1-200 characters")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry line must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        raise SystemExit("MAKEFUN_OUTPUT_DIR is not set")
    out_path = Path(out_dir) / "entry.txt"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
