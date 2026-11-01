#!/usr/bin/env python3
"""Wack-A-Mole introduction banner: the cupping sorting surface, wordless. A walnut table,
a wide tray of roasted beans with one pale wrinkled fault near the middle and tweezers
hovering above it, three tasting bowls at the left, wax sealed sample bags at the right,
the blank back of a pinned chart behind, steam and chaff dust in window light. No text."""
import sys, random, math
from PIL import Image, ImageDraw, ImageFilter
import numpy as np
random.seed(61)
v = sys.argv[1] if len(sys.argv) > 1 else "ship"
W, H = 1600, 900
WALNUT = (90, 58, 34); PARCH = (241, 230, 207); HONEY = (217, 164, 65); AMBER = (178, 118, 44)
img = Image.new("RGB", (W, H), WALNUT); d = ImageDraw.Draw(img, "RGBA")
for y in range(H):
    t = y / H; d.line([(0, y), (W, y)], fill=(int(96 - 18 * t), int(62 - 12 * t), int(36 - 8 * t)))
for gx in range(0, W, 210):  # walnut grain
    d.line([(gx, 0), (gx + 60, H)], fill=(70, 44, 24, 90), width=5)
# window light wash from the left
layer = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ld = ImageDraw.Draw(layer)
ld.polygon([(0, 0), (620, 0), (980, H), (0, H)], fill=(255, 236, 190, 42))
img = Image.alpha_composite(img.convert("RGBA"), layer.filter(ImageFilter.GaussianBlur(30))).convert("RGB"); d = ImageDraw.Draw(img, "RGBA")
# blank back of the pinned chart behind the tray, face turned away
d.rectangle([560, 36, 1060, 218], fill=(232, 220, 192), outline=(120, 96, 62), width=4)
for (px, py) in ((578, 54), (1042, 54)):
    d.ellipse([px - 9, py - 9, px + 9, py + 9], fill=(150, 52, 44), outline=(90, 40, 30), width=2)
# three tasting bowls at the left in a triangle
def bowl(cx, cy, r, kind):
    d.ellipse([cx - r, cy - r // 2, cx + r, cy + r // 2], fill=(250, 249, 246), outline=(180, 178, 170), width=4)
    if kind == "grounds": d.ellipse([cx - r + 14, cy - r // 2 + 9, cx + r - 14, cy + r // 2 - 9], fill=(96, 62, 34))
    elif kind == "water": d.ellipse([cx - r + 14, cy - r // 2 + 9, cx + r - 14, cy + r // 2 - 9], fill=(196, 216, 220))
for (bx, by, kind) in ((210, 330, "grounds"), (330, 470, "water"), (170, 590, "spoon")):
    bowl(bx, by, 92, kind)
d.line([(96, 560), (268, 622)], fill=(196, 200, 206), width=13)  # spoon across the third bowl
d.ellipse([238, 606, 292, 636], fill=(214, 218, 224), outline=(150, 154, 160), width=3)
# steam curls over the bowls
for sx in (200, 330):
    for i in range(3):
        d.arc([sx - 22 + i * 20, 190 - i * 8, sx + 26 + i * 20, 268 - i * 8], 200, 330, fill=(255, 255, 255, 110), width=5)
# sample bags at the right, folded and wax sealed
for i, bx in enumerate((1300, 1408, 1516)):
    by = 300 + (i % 2) * 26
    d.polygon([(bx, by), (bx + 84, by), (bx + 78, by + 210), (bx + 6, by + 210)], fill=(233, 219, 188), outline=(150, 128, 92), width=3)
    d.polygon([(bx, by), (bx + 84, by), (bx + 76, by + 34), (bx + 8, by + 34)], fill=(219, 201, 164))
    d.ellipse([bx + 28, by + 52, bx + 56, by + 80], fill=HONEY, outline=(168, 118, 40), width=3)
# the wide bean tray, edge to edge across the middle and lower frame
d.polygon([(330, 300), (1270, 300), (1330, 830), (270, 830)], fill=(110, 74, 42), outline=(64, 42, 22), width=6)
d.polygon([(356, 326), (1244, 326), (1296, 802), (304, 802)], fill=(140, 96, 54))
def bean(cx, cy, s, col):
    d.ellipse([cx - s, cy - s * .68, cx + s, cy + s * .68], fill=col, outline=tuple(max(0, c - 46) for c in col), width=2)
    d.arc([cx - s * .7, cy - s * .5, cx + s * .7, cy + s * .5], 80, 260, fill=tuple(max(0, c - 70) for c in col), width=2)
random.seed(77)
for gy in range(356, 782, 44):
    for gx in range(386, 1226, 46):
        bx = gx + random.uniform(-13, 13); by = gy + random.uniform(-11, 11); s = random.uniform(17, 24)
        if abs(bx - 800) < 52 and abs(by - 545) < 44: continue
        bean(bx, by, s, random.choice([(168, 106, 52), (186, 124, 62), (150, 92, 44), (196, 138, 74)]))
# the one pale fault near the middle, wrinkled
fx, fy = (800, 545) if v != "v1" else (800, 470)
bean(fx, fy, 27, (226, 208, 172))
for i in range(4): d.arc([fx - 20 + i * 8, fy - 12, fx + 14 + i * 6, fy + 12], 40, 200, fill=(178, 158, 122), width=2)
# tweezers hovering just above it, tips open
d.polygon([(fx - 34, fy - 150), (fx - 24, fy - 30), (fx - 36, fy - 26), (fx - 52, fy - 144)], fill=(198, 202, 208), outline=(140, 144, 150), width=2)
d.polygon([(fx + 52, fy - 144), (fx + 36, fy - 26), (fx + 24, fy - 30), (fx + 34, fy - 150)], fill=(186, 190, 196), outline=(140, 144, 150), width=2)
d.rectangle([fx - 56, fy - 162, fx + 56, fy - 142], fill=(168, 172, 178))
for ex, ey in ((420, 850), (700, 862), (1060, 848)):  # chaff dust near the tray
    for i in range(6):
        px, py = ex + random.uniform(-30, 30), ey + random.uniform(-6, 6)
        d.ellipse([px, py, px + 4, py + 3], fill=(216, 186, 130, 160))
rng = np.random.default_rng(8); a = np.asarray(img).astype(np.int16); n = rng.normal(0, 3, a.shape[:2])[..., None]
img = Image.fromarray(np.clip(a + n, 0, 255).astype(np.uint8))
out = "intro-banner.png" if v == "ship" else f"scratch/intro-{v}.png"
img.save(out); print(out)
