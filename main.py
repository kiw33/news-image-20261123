#!/usr/bin/env python3
"""news-image-20261123 entrypoint.

entry.png ships in this repository (drawn by draw_news23.py). Running
this program copies that image to the grader's output directory, so two
runs always produce identical bytes.

Only the standard library is used: no Pillow, no network access, and no
writes outside the output directory. Python 3.13.
"""

import os
import shutil
import sys

IMAGE_NAME = "entry.png"
FALLBACK_OUTPUT = "/output"


def output_dir():
    """Pick the directory the grader wants the image in.

    $MAKEFUN_OUTPUT_DIR wins; then the sandbox default /output when it
    exists; otherwise a local out/ folder beside this file.
    """
    wanted = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if wanted:
        return wanted
    if os.path.isdir(FALLBACK_OUTPUT):
        return FALLBACK_OUTPUT
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, "out")


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, IMAGE_NAME)
    if not os.path.isfile(source):
        print("missing image: {} (run draw_news23.py first)".format(source), file=sys.stderr)
        return 1
    wanted_size = os.path.getsize(source)
    if wanted_size == 0:
        print("empty image: {} (regenerate it with draw_news23.py)".format(source), file=sys.stderr)
        return 1
    target_dir = output_dir()
    os.makedirs(target_dir, exist_ok=True)
    target = os.path.join(target_dir, IMAGE_NAME)
    shutil.copyfile(source, target)
    actual_size = os.path.getsize(target)
    if actual_size != wanted_size:
        print("copy mismatch: {} holds {} bytes, expected {}".format(target, actual_size, wanted_size), file=sys.stderr)
        return 1
    print("wrote {} ({} bytes)".format(target, actual_size))
    return 0


if __name__ == "__main__":
    sys.exit(main())
