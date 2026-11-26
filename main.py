"""The Dog Reviews the Mailman.

Writes one funny one-line review, in the dog's own voice, to
/output/entry.txt. The text is fixed: the same bytes on every run,
no network, no randomness, no arguments.
"""

import os

LINE = (
    "Five stars for the daily workout \u2014 he knocks, I bark, he runs. "
    "One star off: after six years he still hasn't learned "
    "the gate is mine, not his."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE + "\n")


if __name__ == "__main__":
    main()
