"""Deadpan forecast for a city that does not exist.

Writes one line (<=160 chars) to the entry output location.
Output resolution order: ENTRY_OUT (file or directory) ->
MAKEFUN_OUTPUT_DIR -> /output/entry.txt -> ./entry.txt.
"""

import os
import sys

# Final entry: Varn. One deadpan twist only -- the wind is carrying
# last Tuesday across the harbour -- delivered flat, with a high,
# a wind speed and a civic instruction, like a real broadcast line.
# "Return it by Friday" is the punchline; nothing else competes with it.
ENTRY = (
    "In Varn, expect a high of 21 degrees with gusty 40 km/h winds "
    "carrying last Tuesday across the harbour; residents are asked "
    "to return it by Friday."
)


def check_entry(text):
    """Gate sanity: one line, 1..160 chars, not only whitespace."""
    assert text and not text.isspace(), "entry must not be blank"
    assert "\n" not in text, "entry must be a single line"
    assert len(text) <= 160, "entry exceeds 160 characters"
    return text


def resolve_output_path():
    """Return the file path the entry text must be written to."""
    entry_out = os.environ.get("ENTRY_OUT")
    if entry_out:
        if os.path.isdir(entry_out):
            return os.path.join(entry_out, "entry.txt")
        return entry_out
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        return os.path.join(out_dir, "entry.txt")
    return "/output/entry.txt"


def main():
    text = check_entry(ENTRY)
    path = resolve_output_path()
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(ENTRY)
    except OSError:
        # Last resort: the grader may run from a read-only cwd-less
        # sandbox where /output is not writable; fall back to cwd.
        path = os.path.join(os.getcwd(), "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
