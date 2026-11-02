#!/usr/bin/env python3
"""Render .github/social-preview.png (1280x640) for the GitHub repository card. Requires Pillow."""
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
W, H = 1280, 640
BG, INK, MUTED, ACCENT, CARD = (11, 15, 25), (245, 247, 250), (148, 160, 180), (52, 211, 153), (24, 31, 46)
FONT = "/System/Library/Fonts/SFNS.ttf"
MONO = "/System/Library/Fonts/SFNSMono.ttf"


def font(size, mono=False):
    try:
        return ImageFont.truetype(MONO if mono else FONT, size)
    except OSError:
        return ImageFont.load_default()


def main():
    index = json.loads((ROOT / "catalog" / "index.json").read_text())
    total = index["count"]
    headline = f"{total // 1000 * 1000:,}+" if total >= 2000 else f"{total:,}"

    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W, 8], fill=ACCENT)
    d.text((72, 64), "SandBase", font=font(44), fill=ACCENT)
    d.text((72, 132), "One API key for AI models, data APIs,", font=font(58), fill=INK)
    d.text((72, 202), "sandboxes and agents.", font=font(58), fill=INK)

    pills = [(f"{headline} models & APIs", ACCENT), ("100 free API calls / day", INK), ("Sandboxes free", INK), ("Agents free", INK)]
    x = 72
    for text, color in pills:
        f = font(28)
        w = d.textlength(text, font=f)
        d.rounded_rectangle([x, 300, x + w + 40, 352], radius=26, fill=CARD)
        d.text((x + 20, 309), text, font=f, fill=color)
        x += w + 56

    d.rounded_rectangle([72, 392, W - 72, 548], radius=18, fill=CARD)
    code = [
        ("$ ", MUTED, 'curl api.sandbase.ai/v1/run -H "Authorization: Bearer $KEY" \\'),
        ("  ", MUTED, '    -d \'{"model": "exa/search", "query": "AI agents"}\''),
        ("", ACCENT, "Python · TypeScript · Go · OpenAI SDK · E2B SDK · OpenAPI 3.1"),
    ]
    y = 414
    for prefix, color, line in code:
        d.text((104, y), prefix + line, font=font(26, mono=True), fill=color if not prefix else INK)
        y += 42
    d.text((72, 580), "github.com/sandbaseai/sandbase", font=font(26), fill=MUTED)
    d.text((W - 72 - d.textlength("sandbase.ai", font=font(26)), 580), "sandbase.ai", font=font(26), fill=MUTED)

    out = ROOT / ".github" / "social-preview.png"
    img.save(out, optimize=True)
    print(out, img.size)


if __name__ == "__main__":
    main()
