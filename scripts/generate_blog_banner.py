#!/usr/bin/env python3
"""
Generate article hero banners in the same spirit as src/assets/blog-placeholder-*.jpg:

  - Wide canvas (default 960×480, ~2:1)
  - Dark base + subtle film grain
  - Soft, blurred color "rays" from bottom-center (aurora / glow)
  - Faint grid in a corner (default bottom-left)
  - Optional centered title text

Dependencies:
  pip install pillow

Examples:
  python scripts/generate_blog_banner.py -o src/assets/my-banner.jpg --title "熵减笔记"
  python scripts/generate_blog_banner.py -o banner.jpg --palette warm --seed 42
  python scripts/generate_blog_banner.py -o out.jpg --width 1200 --height 600 --no-text
"""

from __future__ import annotations

import argparse
import random
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont


def _try_load_font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    """Prefer a clean sans; fall back to default bitmap font."""
    candidates = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/Library/Fonts/Arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    ]
    for p in candidates:
        if Path(p).is_file():
            try:
                return ImageFont.truetype(p, size=size)
            except OSError:
                continue
    return ImageFont.load_default()


def _add_grain_pil(im: Image.Image, seed: int | None = None) -> Image.Image:
    """Film grain via Pillow noise + light blend (no numpy)."""
    rng = random.Random(seed)
    w, h = im.size
    sigma = 22 + rng.randint(0, 36)
    noise = Image.effect_noise((w, h), sigma).convert("RGB")
    alpha = 0.055 + rng.random() * 0.035
    return Image.blend(im, noise, alpha)


def _vignette_pil(im: Image.Image, palette: str) -> Image.Image:
    """Darken edges / top so focus stays center (placeholder-style)."""
    w, h = im.size
    top = 100 if palette == "astro" else 85
    side = 78 if palette == "astro" else 68
    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    d.rectangle([0, 0, w, int(h * 0.22)], fill=(0, 0, 0, top))
    d.rectangle([0, int(h * 0.78), w, h], fill=(0, 0, 0, int(top * 0.88)))
    d.rectangle([0, 0, int(w * 0.1), h], fill=(0, 0, 0, side))
    d.rectangle([int(w * 0.9), 0, w, h], fill=(0, 0, 0, side))
    blur = max(10, min(w, h) // 28)
    overlay = overlay.filter(ImageFilter.GaussianBlur(blur))
    base = im.convert("RGBA")
    return Image.alpha_composite(base, overlay).convert("RGB")


def _draw_grid_rgba(
    size: tuple[int, int],
    corner: str = "bl",
    spacing: int = 28,
    line_rgba: tuple[int, int, int, int] | None = None,
) -> Image.Image:
    if line_rgba is None:
        line_rgba = (120, 140, 180, 26)
    w, h = size
    layer = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    if corner == "bl":
        x0, y0, x1, y1 = 0, int(h * 0.42), int(w * 0.48), h
    elif corner == "br":
        x0, y0, x1, y1 = int(w * 0.52), int(h * 0.42), w, h
    else:
        x0, y0, x1, y1 = 0, 0, int(w * 0.45), int(h * 0.55)
    for x in range(x0, x1, spacing):
        draw.line([(x, y0), (x, y1)], fill=line_rgba, width=1)
    for y in range(y0, y1, spacing):
        draw.line([(x0, y), (x1, y)], fill=line_rgba, width=1)
    return layer.filter(ImageFilter.GaussianBlur(0.6))


def _blob_layer(
    size: tuple[int, int],
    palette: list[tuple[int, int, int, int]],
    rng: random.Random,
    origin_jitter: int = 80,
    radius_scale: float = 1.05,
) -> Image.Image:
    w, h = size
    layer = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    cx = w * 0.5 + rng.randint(-origin_jitter, origin_jitter)
    cy = h + rng.randint(-int(h * 0.12), int(h * 0.08))
    for (r, g, b, a) in palette:
        rx = int(w * (0.55 + rng.random() * 0.35) * radius_scale)
        ry = int(h * (0.95 + rng.random() * 0.25) * radius_scale)
        ox = rng.randint(-int(w * 0.2), int(w * 0.2))
        oy = rng.randint(-int(h * 0.15), int(h * 0.1))
        bbox = (cx - rx + ox, cy - ry + oy, cx + rx + ox, cy + ry + oy)
        draw.ellipse(bbox, fill=(r, g, b, a))
    blur = 18 + rng.randint(0, 22)
    return layer.filter(ImageFilter.GaussianBlur(blur))


def palette_astro(rng: random.Random) -> list[tuple[int, int, int, int]]:
    """Default: cool aurora like Astro placeholders (magenta / violet / cyan / orange)."""
    base = [
        (200, 90, 220, 55),
        (120, 90, 240, 48),
        (60, 180, 220, 42),
        (40, 140, 200, 38),
        (255, 170, 90, 36),
        (255, 120, 160, 28),
    ]
    rng.shuffle(base)
    return base


def palette_warm(rng: random.Random) -> list[tuple[int, int, int, int]]:
    """Site-adjacent warm browns / terracotta (熵减心流 accent family)."""
    base = [
        (200, 106, 61, 58),  # accent-warm
        (161, 74, 42, 52),  # accent
        (126, 53, 31, 46),  # accent-dark
        (248, 220, 200, 28),  # soft highlight
        (180, 120, 90, 34),
        (90, 55, 40, 30),
    ]
    rng.shuffle(base)
    return base


def generate_banner(
    width: int = 960,
    height: int = 480,
    *,
    palette: str = "astro",
    seed: int | None = None,
    title: str | None = None,
    grid_corner: str = "bl",
) -> Image.Image:
    rng = random.Random(seed)
    w, h = width, height

    if palette == "warm":
        base = Image.new("RGB", (w, h), (32, 24, 20))
        pal_fn = palette_warm
        grid_color = (150, 110, 88, 24)
    else:
        base = Image.new("RGB", (w, h), (18, 18, 26))
        pal_fn = palette_astro
        grid_color = (120, 140, 180, 26)

    img = base.convert("RGBA")
    for _ in range(2):
        img = Image.alpha_composite(img, _blob_layer((w, h), pal_fn(rng), rng))
    img = Image.alpha_composite(img, _draw_grid_rgba((w, h), corner=grid_corner, line_rgba=grid_color))

    out = _vignette_pil(img.convert("RGB"), palette)
    out = _add_grain_pil(out, seed=seed)

    if title:
        draw = ImageDraw.Draw(out)
        font = _try_load_font(max(22, min(w, h) // 18))
        margin = int(min(w, h) * 0.06)
        max_w = w - 2 * margin
        lines = _wrap_title(title, font, draw, max_w)
        line_heights = []
        for line in lines:
            bbox = draw.textbbox((0, 0), line, font=font)
            line_heights.append(bbox[3] - bbox[1])
        gap = int(min(line_heights) * 0.35) if line_heights else 8
        total_h = sum(line_heights) + gap * (len(lines) - 1)
        y = (h - total_h) // 2
        for line, lh in zip(lines, line_heights):
            bbox = draw.textbbox((0, 0), line, font=font)
            tw = bbox[2] - bbox[0]
            x = (w - tw) // 2
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                draw.text((x + dx, y + dy), line, font=font, fill=(0, 0, 0))
            draw.text((x, y), line, font=font, fill=(245, 246, 250))
            y += lh + gap

    return out


def _text_width(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.ImageFont) -> int:
    bbox = draw.textbbox((0, 0), text, font=font)
    return bbox[2] - bbox[0]


def _wrap_long_unbroken(segment: str, font: ImageFont.ImageFont, draw: ImageDraw.ImageDraw, max_width: int) -> list[str]:
    """Greedy wrap for CJK or long tokens without spaces."""
    out: list[str] = []
    buf = ""
    for ch in segment:
        trial = buf + ch
        if _text_width(draw, trial, font) <= max_width:
            buf = trial
        else:
            if buf:
                out.append(buf)
            buf = ch
    if buf:
        out.append(buf)
    return out


def _wrap_title(
    text: str,
    font: ImageFont.FreeTypeFont | ImageFont.ImageFont,
    draw: ImageDraw.ImageDraw,
    max_width: int,
) -> list[str]:
    lines: list[str] = []
    for paragraph in text.split("\n"):
        if not paragraph.strip():
            continue
        words = paragraph.split()
        cur: list[str] = []
        for w in words:
            trial = (" ".join(cur + [w])).strip()
            if _text_width(draw, trial, font) <= max_width:
                cur.append(w)
            else:
                if cur:
                    lines.append(" ".join(cur))
                    cur = []
                if _text_width(draw, w, font) <= max_width:
                    cur = [w]
                else:
                    lines.extend(_wrap_long_unbroken(w, font, draw, max_width))
        if cur:
            lines.append(" ".join(cur))
    return lines if lines else [text]


def main() -> int:
    p = argparse.ArgumentParser(description="Generate Astro-style blog hero banners.")
    p.add_argument("-o", "--output", type=Path, required=True, help="Output .jpg or .png path")
    p.add_argument("--width", type=int, default=960)
    p.add_argument("--height", type=int, default=480)
    p.add_argument(
        "--palette",
        choices=("astro", "warm"),
        default="astro",
        help='"astro" = cool aurora like default placeholders; "warm" = terracotta / site accent',
    )
    p.add_argument("--seed", type=int, default=None, help="Reproducible random layout")
    p.add_argument("--title", type=str, default="", help="Optional centered title (wraps)")
    p.add_argument("--no-text", action="store_true", help="Ignore --title, image only")
    p.add_argument("--jpeg-quality", type=int, default=88, help="JPEG quality when saving .jpg")
    p.add_argument(
        "--grid-corner",
        choices=("bl", "br", "tl"),
        default="bl",
        help="Which corner gets the faint grid",
    )
    args = p.parse_args()

    title = None if args.no_text or not (args.title or "").strip() else args.title.strip()

    img = generate_banner(
        args.width,
        args.height,
        palette=args.palette,
        seed=args.seed,
        title=title,
        grid_corner=args.grid_corner,
    )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    suf = args.output.suffix.lower()
    if suf in (".jpg", ".jpeg"):
        img.save(args.output, quality=args.jpeg_quality, optimize=True)
    elif suf == ".png":
        img.save(args.output, optimize=True)
    else:
        p.error("Output suffix should be .jpg, .jpeg, or .png")
    print(f"Wrote {args.output.resolve()} ({args.width}×{args.height}, palette={args.palette})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
