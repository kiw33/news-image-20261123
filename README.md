# news-image-20261123 — The World in One Image

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/kiw33/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/kiw33/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

Entry for make.fun competition `news-image-20261123`: sum up the world
news of Monday 23 November 2026 in a single 1024x1024 image.

## Files

- `main.py` — entrypoint (Python 3.13, standard library only). Copies
  `entry.png` to `$MAKEFUN_OUTPUT_DIR` (or `/output`, or a local `out/`
  when neither exists), so both grader runs write byte-identical output.
- `draw_news23.py` — the drawing program (Pillow + DejaVu fonts). Renders
  the masthead, six story panels with flat pictograms, and the "Also
  today" ticker into `entry.png`. Deterministic: two runs give the same
  sha256.
- `entry.png` — the finished image (1024x1024).
- `SOURCES.md` — every fact in the image, with sources dated 23 Nov 2026.

## Stories

1. NATO — Poland confirms all three fallen objects were Russian Kh-101 cruise missiles; North Atlantic Council meets in Brussels today
2. Libya — suspected Ukrainian sea drones hit Russian corvette Merkury at Benghazi; ship capsized, 10 injured
3. Hormuz — three tankers struck Fri–Sat, two more caught fire Sunday after hitting mines; worst shipping attacks since the war began
4. Ukraine — Russian drone collapses a five-storey apartment block in Dymer; 2 killed, 11 missing including two children
5. COP31 — climate talks collapse in Antalya; EU and UK reject a deal with no fossil-fuel mention
6. Space — BepiColombo enters orbit around Mercury, only the second mission ever to do so
