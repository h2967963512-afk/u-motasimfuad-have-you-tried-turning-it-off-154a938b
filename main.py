"""Writes the entry text to /output/entry.txt.

One funny line a hopeless tech support agent says to a desperate
customer, for make.fun's "Have You Tried Turning It Off?" bounty.

Python 3.13, standard library only, no network.

How it runs
------------
Run ``python3 main.py`` from the repository root (or anywhere: the
script takes no arguments and reads nothing). It creates /output if
needed and writes exactly one line — the entry text, no trailing
newline — to /output/entry.txt in UTF-8.

Verification notes
------------------
Verified locally 2026-11-25: ``python3 main.py`` exits 0, writes
115 characters / 119 bytes, a single line, valid UTF-8, no trailing
newline, matching the intended entry line exactly. The entry gate
needs 1-199 characters of non-whitespace UTF-8 text, so 115 is
inside the limit. Re-running after this docstring edit must produce
byte-identical output (same sha256 of /output/entry.txt), since the
edit touches only documentation, not the TEXT constant.
"""

import os

TEXT = "Good news \u2014 turning it off and on again worked. Bad news \u2014 neither of us knows why, so please don't touch anything."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

# Revision note: the classic turn-it-off-and-on-again, twisted — the fix
# worked and nobody knows why, so the agent's cheerful uselessness is the
# joke and the customer is never the butt. One line, 115 characters.
