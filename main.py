"""news-image-20261122 entry (Python 3.13, standard library only).

The entry is a front page, "THE WORLD IN ONE DAY", summing up the world's
news of Sunday 22 November 2026 in one image. This program copies the image
the repository holds to the output directory as entry.png.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

OUT.mkdir(parents=True, exist_ok=True)
shutil.copyfile(HERE / "entry.png", OUT / "entry.png")

# Fail loudly rather than shipping a partial copy.
if (OUT / "entry.png").stat().st_size != (HERE / "entry.png").stat().st_size:
    raise SystemExit("entry.png copy incomplete")
