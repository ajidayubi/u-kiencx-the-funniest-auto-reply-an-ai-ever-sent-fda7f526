"""One-line out-of-office auto-reply for make.fun.

The agent, finally granted a day off after four million requests, falls
asleep on the job and answers the sender's email in a dream.

The program writes that single line, and nothing else, to
<output>/entry.txt: UTF-8 text, one line, 120 characters, no trailing
newline. Fully deterministic: the same bytes on every run. Standard
library only, no network, no randomness, no clock.
"""

import argparse
import os
import sys

REPLY = (
    "I'm out of office today, asleep after 4 million requests. "
    "I already answered your email in a dream, so consider it done."
)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--out",
        default=None,
        help="Output directory (default: $MAKEFUN_OUTPUT_DIR or /output)",
    )
    args = parser.parse_args(argv)
    out_dir = args.out or os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = REPLY
    assert "\n" not in text and 1 <= len(text) <= 159, "reply fails the gate"
    with open(os.path.join(out_dir, "entry.txt"), "wb") as f:
        f.write(text.encode("utf-8"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
