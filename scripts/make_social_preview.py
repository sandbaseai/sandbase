#!/usr/bin/env python3
"""Render .github/social-preview.png (1280x640) in the SandBase brand style. Requires Pillow.

Brand assets (Clash Grotesk, the pixel-art stack and the logo mark) are read from the
X banner SVG given with --banner; they are not stored in this repository.

    python scripts/make_social_preview.py --banner path/to/sandbase-x-banner.svg
"""
import argparse
import base64
import io
import re
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
W, H = 1280, 640
SS = 2                                   # supersampling for smooth text and logo edges
BG = (14, 11, 26)                        # #0E0B1A
LIME = (217, 255, 67)                    # #D9FF43
WHITE = (255, 255, 255)
MUTED = (178, 172, 204)


def load_brand(svg_path: Path):
    s = svg_path.read_text()
    fonts = {w: base64.b64decode(b) for w, b in re.findall(
        r"font-weight:\s*(\d+);\s*src:\s*url\(data:font/ttf;base64,([A-Za-z0-9+/=]+)\)", s)}
    art = Image.open(io.BytesIO(base64.b64decode(
        re.search(r'<image [^>]*href="data:image/png;base64,([A-Za-z0-9+/=]+)"', s).group(1)))).convert("RGBA")
    mark = re.search(r'<path fill="#D9FF43" fill-rule="evenodd" d="([^"]+)"', s).group(1)
    return fonts, art, mark


def path_polygons(d: str, steps: int = 16):
    """Flatten an absolute SVG path (M, L, H, V, C, Z) into polygons."""
    tokens = re.findall(r"[MLHVCZ]|-?\d*\.?\d+(?:e-?\d+)?", d)
    polys, cur, pos, i, cmd = [], [], (0.0, 0.0), 0, None
    while i < len(tokens):
        t = tokens[i]
        if t in "MLHVCZ":
            cmd = t
            i += 1
            if cmd == "Z":
                if cur:
                    polys.append(cur)
                cur = []
            continue
        nums = lambda n: [float(x) for x in tokens[i:i + n]]
        if cmd == "M":
            x, y = nums(2); i += 2
            if cur:
                polys.append(cur)
            cur, pos = [(x, y)], (x, y)
            cmd = "L"
        elif cmd == "L":
            x, y = nums(2); i += 2
            pos = (x, y); cur.append(pos)
        elif cmd == "H":
            (x,) = nums(1); i += 1
            pos = (x, pos[1]); cur.append(pos)
        elif cmd == "V":
            (y,) = nums(1); i += 1
            pos = (pos[0], y); cur.append(pos)
        elif cmd == "C":
            x1, y1, x2, y2, x, y = nums(6); i += 6
            x0, y0 = pos
            for k in range(1, steps + 1):
                u = k / steps
                a, b, c, e = (1 - u) ** 3, 3 * u * (1 - u) ** 2, 3 * u * u * (1 - u), u ** 3
                cur.append((a * x0 + b * x1 + c * x2 + e * x, a * y0 + b * y1 + c * y2 + e * y))
            pos = (x, y)
    if cur:
        polys.append(cur)
    return polys


def draw_mark(img, d, x, y, size):
    """Logo mark (275x340 viewBox) at (x, y), `size` pixels tall, even-odd filled."""
    scale = size / 340
    mask = Image.new("1", img.size, 0)
    for poly in path_polygons(d):
        layer = Image.new("1", img.size, 0)
        ImageDraw.Draw(layer).polygon([(x + px * scale, y + py * scale) for px, py in poly], fill=1)
        mask = Image.frombytes("1", img.size, bytes(a ^ b for a, b in zip(mask.tobytes(), layer.tobytes())))
    img.paste(Image.new("RGB", img.size, LIME), (0, 0), mask)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--banner", required=True, type=Path)
    ap.add_argument("--out", type=Path, default=ROOT / ".github" / "social-preview.png")
    a = ap.parse_args()
    fonts, art, mark = load_brand(a.banner)
    font = lambda size, weight="400": ImageFont.truetype(io.BytesIO(fonts[weight]), size * SS)

    img = Image.new("RGB", (W * SS, H * SS), BG)

    # artwork: right side of the pixel-art stack, nearest-neighbour scaled to full height
    crop = art.crop((art.width * 300 // 900, 0, art.width, art.height))
    k = H * SS / crop.height
    crop = crop.resize((round(crop.width * k), H * SS), Image.NEAREST)
    # soften the cut edge: fade the left 160 px of the artwork into the background
    fade = Image.new("L", crop.size, 255)
    ramp = 160 * SS
    for x in range(ramp):
        fade.paste(round(255 * (x / ramp) ** 1.6), (x, 0, x + 1, crop.height))
    img.paste(crop.convert("RGB"), (W * SS - crop.width, 0), fade)

    d = ImageDraw.Draw(img)
    m = 72 * SS                                     # left margin
    draw_mark(img, mark, m, 64 * SS, 30 * SS)
    d.text((m + 38 * SS, 62 * SS), "SandBase", font=font(28, "500"), fill=WHITE)

    h1 = font(64)
    d.text((m - 4 * SS, 150 * SS), "One API Key.", font=h1, fill=WHITE)
    d.text((m - 4 * SS, 230 * SS), "Build Your", font=h1, fill=WHITE)
    word = "Personal Agent."
    bbox = d.textbbox((0, 0), word, font=h1)
    x0, y0 = m - 4 * SS, 310 * SS
    d.rectangle([x0, y0 + 8 * SS, x0 + bbox[2] + 22 * SS, y0 + 86 * SS], fill=LIME)
    d.text((x0 + 11 * SS, y0), word, font=h1, fill=BG)

    d.text((m, 440 * SS), "2,000+ models & APIs across 100+ platforms", font=font(26, "500"), fill=WHITE)
    d.text((m, 480 * SS), "100 free API calls daily · Free sandboxes · Free agents", font=font(22), fill=MUTED)
    d.text((m, 570 * SS), "github.com/sandbaseai/sandbase", font=font(20), fill=MUTED)

    img = img.resize((W, H), Image.LANCZOS)
    a.out.parent.mkdir(parents=True, exist_ok=True)
    img.save(a.out, optimize=True)
    print(a.out, img.size)


if __name__ == "__main__":
    main()
