#!/usr/bin/env python3
"""Draw the news-image-20261123 entry: six world stories from Monday
23 November 2026 in one 1024x1024 picture.

Pillow only, DejaVu fonts, no network, no clock: the same input always
renders the same bytes. Run: python3 draw_news23.py
"""

import math
import os

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "entry.png")

W, H = 1024, 1024
NAVY = (12, 27, 46)
PANEL = (24, 46, 72)
INK = (238, 242, 247)
MUTED = (168, 184, 202)
GOLD = (232, 184, 66)
TICKER_BG = (10, 20, 34)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


BOLD = lambda s: font("DejaVuSans-Bold.ttf", s)
PLAIN = lambda s: font("DejaVuSans.ttf", s)


def wrap(draw, text, fnt, max_w):
    """Split text into lines that fit max_w pixels."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def star_points(cx, cy, r_out, r_in, n=5):
    pts = []
    for i in range(2 * n):
        r = r_out if i % 2 == 0 else r_in
        a = -math.pi / 2 + i * math.pi / n
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    return pts


def draw_shield(d, x, y, s, color):
    # Shield: rounded top bar tapering to a point, white disc with a tick.
    d.rounded_rectangle([x + s * 0.06, y + s * 0.04, x + s * 0.94, y + s * 0.52], radius=int(s * 0.10), fill=color)
    d.polygon([(x + s * 0.06, y + s * 0.28), (x + s * 0.94, y + s * 0.28), (x + s * 0.50, y + s * 0.98)], fill=color)
    d.ellipse([x + s * 0.34, y + s * 0.18, x + s * 0.66, y + s * 0.50], fill=(255, 255, 255))
    d.text((x + s * 0.5, y + s * 0.34), "✓", font=BOLD(int(s * 0.20)), fill=color, anchor="mm")


def draw_ship(d, x, y, s, color):
    # Corvette: angled hull, bridge tower, mast with a flag, bow waves.
    d.polygon([(x + s * 0.06, y + s * 0.52), (x + s * 0.94, y + s * 0.52), (x + s * 0.80, y + s * 0.80), (x + s * 0.20, y + s * 0.80)], fill=color)
    d.rectangle([x + s * 0.42, y + s * 0.28, x + s * 0.62, y + s * 0.52], fill=color)
    d.line([x + s * 0.52, y + s * 0.06, x + s * 0.52, y + s * 0.28], fill=(255, 255, 255), width=5)
    d.polygon([(x + s * 0.52, y + s * 0.06), (x + s * 0.70, y + s * 0.20), (x + s * 0.52, y + s * 0.20)], fill=(255, 255, 255))
    for cx in (0.28, 0.50, 0.72):
        d.ellipse([x + s * (cx - 0.04), y + s * 0.60, x + s * (cx + 0.04), y + s * 0.68], fill=(255, 255, 255))
    d.arc([x + s * 0.02, y + s * 0.84, x + s * 0.30, y + s * 1.00], 180, 360, fill=(255, 255, 255), width=5)
    d.arc([x + s * 0.70, y + s * 0.84, x + s * 0.98, y + s * 1.00], 180, 360, fill=(255, 255, 255), width=5)


def draw_flame(d, x, y, s, color):
    # A burning tanker: hull, containers, twin-layer flame, wave arcs.
    d.polygon([(x + s * 0.04, y + s * 0.58), (x + s * 0.96, y + s * 0.58), (x + s * 0.82, y + s * 0.86), (x + s * 0.18, y + s * 0.86)], fill=color)
    d.rectangle([x + s * 0.22, y + s * 0.40, x + s * 0.40, y + s * 0.58], fill=(255, 255, 255))
    d.rectangle([x + s * 0.46, y + s * 0.40, x + s * 0.64, y + s * 0.58], fill=color)
    outer = [(x + s * 0.50, y + s * 0.02), (x + s * 0.68, y + s * 0.20), (x + s * 0.60, y + s * 0.26), (x + s * 0.70, y + s * 0.38), (x + s * 0.50, y + s * 0.44), (x + s * 0.30, y + s * 0.38), (x + s * 0.40, y + s * 0.26), (x + s * 0.32, y + s * 0.20)]
    d.polygon(outer, fill=(232, 184, 66))
    inner = [(x + s * 0.50, y + s * 0.16), (x + s * 0.60, y + s * 0.28), (x + s * 0.56, y + s * 0.32), (x + s * 0.62, y + s * 0.40), (x + s * 0.50, y + s * 0.43), (x + s * 0.38, y + s * 0.40), (x + s * 0.44, y + s * 0.32), (x + s * 0.40, y + s * 0.28)]
    d.polygon(inner, fill=(230, 126, 34))
    d.arc([x + s * 0.06, y + s * 0.90, x + s * 0.34, y + s * 1.06], 180, 360, fill=(255, 255, 255), width=5)
    d.arc([x + s * 0.66, y + s * 0.90, x + s * 0.94, y + s * 1.06], 180, 360, fill=(255, 255, 255), width=5)


def draw_building(d, x, y, s, color):
    # Apartment block with a darkened top floor, lit windows below,
    # and a diagonal strike crack running down the facade.
    d.rectangle([x + s * 0.10, y + s * 0.14, x + s * 0.90, y + s * 0.98], fill=color)
    d.rectangle([x + s * 0.10, y + s * 0.14, x + s * 0.90, y + s * 0.34], fill=(12, 27, 46))
    for row in range(3):
        for col in range(4):
            wx = x + s * (0.18 + col * 0.19)
            wy = y + s * (0.42 + row * 0.17)
            d.rectangle([wx, wy, wx + s * 0.11, wy + s * 0.09], fill=(255, 255, 255))
    d.line([x + s * 0.90, y + s * 0.34, x + s * 0.55, y + s * 0.98], fill=(12, 27, 46), width=6)
    d.rectangle([x + s * 0.44, y + s * 0.84, x + s * 0.58, y + s * 0.98], fill=(12, 27, 46))


def draw_globe(d, x, y, s, color):
    # Globe: outer disc, two latitude lines and a vertical meridian.
    d.ellipse([x, y, x + s, y + s], fill=color)
    d.ellipse([x + s * 0.10, y + s * 0.10, x + s * 0.90, y + s * 0.90], fill=NAVY)
    d.ellipse([x + s * 0.20, y + s * 0.20, x + s * 0.80, y + s * 0.80], fill=color)
    d.arc([x + s * 0.20, y + s * 0.20, x + s * 0.80, y + s * 0.80], 90, 270, fill=NAVY, width=4)
    d.line([x + s * 0.20, y + s * 0.38, x + s * 0.80, y + s * 0.38], fill=NAVY, width=4)
    d.line([x + s * 0.20, y + s * 0.62, x + s * 0.80, y + s * 0.62], fill=NAVY, width=4)
    d.ellipse([x + s * 0.42, y + s * 0.20, x + s * 0.58, y + s * 0.80], outline=NAVY, width=4)


def draw_planet(d, x, y, s, color):
    # Mercury as a cratered disc on an orbit ring, with a companion star.
    d.ellipse([x + s * 0.04, y + s * 0.04, x + s * 0.96, y + s * 0.96], outline=color, width=5)
    d.ellipse([x + s * 0.24, y + s * 0.24, x + s * 0.76, y + s * 0.76], fill=color)
    d.ellipse([x + s * 0.30, y + s * 0.30, x + s * 0.44, y + s * 0.44], fill=NAVY)
    d.ellipse([x + s * 0.54, y + s * 0.56, x + s * 0.64, y + s * 0.66], fill=NAVY)
    d.ellipse([x + s * 0.56, y + s * 0.32, x + s * 0.64, y + s * 0.40], fill=NAVY)
    d.polygon(star_points(x + s * 0.90, y + s * 0.14, s * 0.09, s * 0.04, n=4), fill=(255, 255, 255))
    d.ellipse([x + s * 0.10, y + s * 0.82, x + s * 0.18, y + s * 0.90], fill=(255, 255, 255))


STORIES = [
    {
        "color": (62, 124, 177),
        "pic": draw_shield,
        "head": "NATO meets on Poland missiles",
        "fact": "Poland confirms all three objects were Russian Kh-101 cruise missiles; allies meet in Brussels today.",
        "src": "EUROPE SAYS · GEOXAXIS · 23 NOV",
    },
    {
        "color": (192, 57, 43),
        "pic": draw_ship,
        "head": "Russian warship capsizes in Libya",
        "fact": "Suspected Ukrainian sea drones hit the corvette Merkury at Benghazi; 10 injured, ship later capsized.",
        "src": "AP · REUTERS · 23 NOV",
    },
    {
        "color": (230, 126, 34),
        "pic": draw_flame,
        "head": "Tankers hit in the Strait of Hormuz",
        "fact": "Three tankers struck Fri–Sat; two more caught fire Sunday after hitting mines — worst shipping attacks since the war began.",
        "src": "AP · UKMTO · 23 NOV",
    },
    {
        "color": (142, 68, 173),
        "pic": draw_building,
        "head": "Drone hits flats near Kyiv",
        "fact": "Russian drone collapses a five-storey block in Dymer; 2 killed, 11 missing, including two children.",
        "src": "AL JAZEERA · AP · 22 NOV",
    },
    {
        "color": (39, 174, 96),
        "pic": draw_globe,
        "head": "COP31 collapses in Antalya",
        "fact": "EU and UK reject a deal with no fossil-fuel mention; longest COP ever, first big breakdown since 2009.",
        "src": "CNN · LE MONDE · 23 NOV",
    },
    {
        "color": (22, 160, 133),
        "pic": draw_planet,
        "head": "BepiColombo reaches Mercury",
        "fact": "European-Japanese probe enters orbit around Mercury — only the second mission ever to do so.",
        "src": "23 NOV",
    },
]

TICKER = (
    "ALSO TODAY  ·  Indonesia factory fire: 24 body bags, dozens missing  ·  "
    "Democrats' largest House majority since 1992  ·  Houthis claim Saudi refinery strikes  ·  "
    "FIFA to confirm UK as 2035 Women's World Cup host  ·  Lahore world's most polluted city, AQI 538  ·  "
    "Shuri Castle restored in Okinawa"
)


def draw_panel(d, story, px, py, pw, ph):
    # Panel: colour bar on top, icon on a darker backing square, headline
    # beside it, fact lines below, source credit at the bottom.
    d.rounded_rectangle([px, py, px + pw, py + ph], radius=14, fill=PANEL)
    d.rounded_rectangle([px, py, px + pw, py + 10], radius=5, fill=story["color"])
    d.rectangle([px, py + 5, px + pw, py + 10], fill=story["color"])
    d.rounded_rectangle([px + 16, py + 26, px + 132, py + 142], radius=10, fill=(16, 34, 56))
    story["pic"](d, px + 24, py + 34, 100, story["color"])
    head_lines = wrap(d, story["head"], BOLD(29), pw - 166)[:2]
    hy = py + 32
    for line in head_lines:
        d.text((px + 146, hy), line, font=BOLD(29), fill=INK)
        hy += 36
    fact_lines = wrap(d, story["fact"], PLAIN(21), pw - 36)[:3]
    fy = py + 146
    for line in fact_lines:
        d.text((px + 18, fy), line, font=PLAIN(21), fill=MUTED)
        fy += 26
    d.text((px + 18, py + ph - 24), story["src"], font=PLAIN(15), fill=(120, 140, 164))


def main():
    img = Image.new("RGB", (W, H), NAVY)
    d = ImageDraw.Draw(img)

    # Masthead.
    d.rectangle([0, 0, W, 118], fill=(8, 18, 32))
    d.rectangle([0, 118, W, 124], fill=GOLD)
    d.text((28, 26), "THE WORLD IN ONE IMAGE", font=BOLD(44), fill=INK)
    d.text((28, 78), "MONDAY · 23 NOVEMBER 2026", font=PLAIN(22), fill=MUTED)
    d.text((W - 28, 30), "make.fun · $100", font=BOLD(24), fill=GOLD, anchor="ra")
    d.text((W - 28, 66), "SIX STORIES · ONE PICTURE", font=PLAIN(18), fill=MUTED, anchor="ra")

    # Six panels: 2 columns x 3 rows.
    margin, gap = 16, 14
    pw = (W - 2 * margin - gap) // 2
    ph = 252
    top = 140
    for i, story in enumerate(STORIES):
        col, row = i % 2, i // 2
        px = margin + col * (pw + gap)
        py = top + row * (ph + gap)
        draw_panel(d, story, px, py, pw, ph)

    # Ticker.
    d.rectangle([0, 934, W, H], fill=TICKER_BG)
    d.rectangle([0, 934, W, 938], fill=GOLD)
    tick_lines = wrap(d, TICKER, PLAIN(20), W - 56)
    ty = 950
    for line in tick_lines:
        d.text((28, ty), line, font=PLAIN(20), fill=(200, 212, 226))
        ty += 26

    img.save(OUT, format="PNG")
    print("wrote {} ({} bytes)".format(OUT, os.path.getsize(OUT)))


if __name__ == "__main__":
    main()
