#!/usr/bin/env python3
"""Wack-A-Mole wordmark banner: the cupping room table from the taster side. A sample tray
of roasted beans in the foreground with a small rejected pile at its corner, six white
bowls on a walnut board with steam over the first two and spoons across their rims, the
defect chart pinned behind carrying Wack-A-Mole as its heading in Arima, a pencil on a
string beside it, and wax sealed sample bags at the right end."""
import sys, random
from PIL import Image, ImageDraw, ImageFont
import numpy as np
random.seed(43)
v = sys.argv[1] if len(sys.argv) > 1 else "ship"
W, H = 1600, 560
img = Image.new("RGB", (W, H), (226, 214, 188)); d = ImageDraw.Draw(img, "RGBA")
d.rectangle([0, 330, W, H], fill=(90, 58, 34))
for gx in range(0, W, 190): d.line([(gx, 330), (gx + 40, H)], fill=(70, 44, 24, 90), width=5)
# the defect chart pinned on the wall board
d.rectangle([470, 26, 1130, 268], fill=(241, 230, 207), outline=(90, 58, 34), width=5)
for (px, py) in ((492, 48), (1108, 48)): d.ellipse([px - 8, py - 8, px + 8, py + 8], fill=(150, 52, 44))
for i in range(4): d.line([(510, 158 + i * 26), (1090, 158 + i * 26)], fill=(170, 148, 112), width=3)
for cx in (640, 800, 960): d.line([(cx, 150), (cx, 258)], fill=(170, 148, 112), width=3)
size = 58 if v == "v1" else 76
f = ImageFont.truetype("fonts/Arima.ttf", size)
try: f = f.font_variant(weight=600)
except Exception: pass
d.text((800, 96), "Wack-A-Mole", font=f, anchor="mm", fill=(90, 58, 34))
# little bean sketches in the chart rows
for (bx, by) in ((560, 182), (720, 208), (880, 182), (1040, 208)):
    d.ellipse([bx - 16, by - 11, bx + 16, by + 11], outline=(120, 84, 44), width=3)
    d.arc([bx - 11, by - 8, bx + 11, by + 8], 80, 260, fill=(120, 84, 44), width=2)
# pencil on a string beside the chart
d.line([(1160, 40), (1160, 150)], fill=(90, 58, 34), width=3)
d.polygon([(1152, 150), (1168, 150), (1164, 216), (1156, 216)], fill=(217, 164, 65))
d.polygon([(1156, 216), (1164, 216), (1160, 232)], fill=(60, 44, 26))
# six bowls on a walnut board, steam over the first two, spoons across rims
d.rectangle([120, 300, 1180, 336], fill=(110, 74, 42), outline=(64, 42, 22), width=4)
for i in range(6):
    cx = 210 + i * 168; cy = 292
    d.ellipse([cx - 72, cy - 34, cx + 72, cy + 34], fill=(250, 249, 246), outline=(180, 178, 170), width=4)
    d.ellipse([cx - 56, cy - 24, cx + 56, cy + 24], fill=(120, 80, 44) if i % 2 == 0 else (150, 100, 56))
    d.line([(cx - 64, cy - 26), (cx + 66, cy - 40)], fill=(196, 200, 206), width=8)
    if i < 2:
        for k in range(3): d.arc([cx - 26 + k * 22, cy - 108, cx + 22 + k * 22, cy - 44], 200, 330, fill=(255, 255, 255, 130), width=5)
# foreground sample tray with beans and the rejected pile at its corner
d.polygon([(90, 368), (1050, 368), (1100, 540), (40, 540)], fill=(110, 74, 42), outline=(64, 42, 22), width=5)
d.polygon([(112, 388), (1028, 388), (1070, 522), (72, 522)], fill=(140, 96, 54))
def bean(cx, cy, s, col):
    d.ellipse([cx - s, cy - s * .68, cx + s, cy + s * .68], fill=col, outline=tuple(max(0, c - 46) for c in col), width=2)
    d.arc([cx - s * .7, cy - s * .5, cx + s * .7, cy + s * .5], 80, 260, fill=tuple(max(0, c - 70) for c in col), width=2)
for i in range(90):
    bean(random.uniform(150, 980), random.uniform(404, 505), random.uniform(13, 19), random.choice([(168, 106, 52), (186, 124, 62), (150, 92, 44)]))
bean(986, 414, 15, (226, 208, 172)); bean(1012, 428, 14, (96, 62, 34)); bean(962, 430, 13, (52, 36, 26))  # rejected pile
# wax sealed sample bags at the right end of the table
for i, bx in enumerate((1230, 1360, 1490)):
    by = 356 + (i % 2) * 14
    d.polygon([(bx, by), (bx + 96, by), (bx + 88, by + 178), (bx + 8, by + 178)], fill=(233, 219, 188), outline=(150, 128, 92), width=3)
    d.polygon([(bx, by), (bx + 96, by), (bx + 88, by + 36), (bx + 8, by + 36)], fill=(219, 201, 164))
    d.ellipse([bx + 34, by + 56, bx + 62, by + 84], fill=(217, 164, 65), outline=(168, 118, 40), width=3)
rng = np.random.default_rng(6); a = np.asarray(img).astype(np.int16); n = rng.normal(0, 3, a.shape[:2])[..., None]
img = Image.fromarray(np.clip(a + n, 0, 255).astype(np.uint8))
out = "banner.png" if v == "ship" else f"scratch/banner-{v}.png"
img.save(out); print(out)
