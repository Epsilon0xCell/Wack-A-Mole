#!/usr/bin/env python3
"""Wack-A-Mole logo: a shallow silver cupping spoon from above at a slight tilt, its bowl
holding one roasted bean marked with a red cross, a white tasting bowl rim and the corner
of a parchment defect chart behind it, the name in Arima in walnut on parchment below."""
import sys
from PIL import Image, ImageDraw, ImageFont
v = sys.argv[1] if len(sys.argv) > 1 else "ship"
S = 1000
img = Image.new("RGBA", (S, S), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
# chart corner and bowl rim behind the spoon
d.polygon([(120, 120), (620, 80), (640, 420), (140, 450)], fill=(241, 230, 207, 255), outline=(90, 58, 34, 255), width=6)
for i in range(4): d.line([(150, 180 + i * 62), (610, 148 + i * 62)], fill=(170, 148, 112, 255), width=4)
d.arc([560, 300, 940, 640], 90, 300, fill=(250, 249, 246, 255), width=34)
# spoon handle running down to the right, bowl at upper left centre
d.polygon([(430, 430), (830, 700), (872, 652), (478, 392)], fill=(198, 202, 208, 255), outline=(140, 144, 150, 255), width=5)
bw = 300 if v == "v1" else 340
d.ellipse([500 - bw, 400 - bw * .78, 500 + bw, 400 + bw * .78], fill=(208, 212, 218, 255), outline=(140, 144, 150, 255), width=8)
d.ellipse([500 - bw + 44, 400 - bw * .78 + 34, 500 + bw - 44, 400 + bw * .78 - 34], fill=(188, 192, 198, 255))
# the condemned bean with its red cross
d.ellipse([376, 296, 624, 504], fill=(168, 106, 52, 255), outline=(110, 68, 32, 255), width=5)
d.arc([412, 322, 588, 478], 80, 260, fill=(110, 68, 32, 255), width=5)
lw = 13 if v == "v1" else 22
d.line([(438, 334), (562, 466)], fill=(179, 49, 42, 255), width=lw)
d.line([(562, 334), (438, 466)], fill=(179, 49, 42, 255), width=lw)
f = ImageFont.truetype("fonts/Arima.ttf", 104)
try: f = f.font_variant(weight=600)
except Exception: pass
d.text((500, 862), "Wack-A-Mole", font=f, anchor="mm", fill=(90, 58, 34, 255))
out = "logo.png" if v == "ship" else f"scratch/logo-{v}.png"
img.save(out)
img.resize((64, 64)).save("scratch/logo64-ship.png" if v == "ship" else f"scratch/logo64-{v}.png")
print(out)
