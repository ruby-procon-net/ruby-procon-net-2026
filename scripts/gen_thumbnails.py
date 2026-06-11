#!/usr/bin/env python3
"""お知らせ記事のサムネイル（1280x720 webp）を生成し、front matter に thumbnail を付与する。

- 記事本文に最初のローカル画像があれば、それを 16:9 にクロップして使う
- 画像が無ければ、グレープ背景＋記事タイトルのプレースホルダーを生成する
- 既存の thumbnail 行は作り直す（冪等）

使い方:  python3 scripts/gen_thumbnails.py
必要ツール: rsvg-convert, ImageMagick(magick)
"""
import glob
import html
import os
import re
import subprocess
import tempfile

ART = "_articles"
THUMB_DIR = "assets/images/articles/thumbnails"
os.makedirs(THUMB_DIR, exist_ok=True)


def wrap(s, n):
    return [s[i:i + n] for i in range(0, len(s), n)]


def make_placeholder(out, title):
    lines = wrap(title, 16)[:4]
    tspans = "".join(
        f'<tspan x="80" dy="{0 if i == 0 else 84}">{html.escape(l)}</tspan>'
        for i, l in enumerate(lines)
    )
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="720" viewBox="0 0 1280 720">
<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
<stop offset="0" stop-color="#4b40a4"/><stop offset="1" stop-color="#2b2560"/></linearGradient></defs>
<rect width="1280" height="720" fill="url(#g)"/>
<rect x="80" y="118" width="64" height="8" rx="4" fill="#db0672"/>
<text x="80" y="96" font-family="Hiragino Sans, Hiragino Kaku Gothic ProN, sans-serif" font-size="30" font-weight="bold" fill="#d5d2ec">第16回 中高生Rubyプログラミングコンテスト 2026 ／ お知らせ</text>
<text x="80" y="250" font-family="Hiragino Sans, Hiragino Kaku Gothic ProN, sans-serif" font-size="62" font-weight="bold" fill="#ffffff">{tspans}</text>
</svg>'''
    with tempfile.TemporaryDirectory() as tmpdir:
        svg_path = os.path.join(tmpdir, "thumb.svg")
        png_path = os.path.join(tmpdir, "thumb.png")
        with open(svg_path, "w", encoding="utf-8") as f:
            f.write(svg)
        subprocess.run(["rsvg-convert", "-w", "1280", "-h", "720", "-o", png_path, svg_path], check=True)
        subprocess.run(["magick", png_path, "-quality", "82", out], check=True)


def make_from_image(src, out):
    subprocess.run([
        "magick", src, "-resize", "1280x720^",
        "-gravity", "center", "-extent", "1280x720",
        "-quality", "82", out
    ], check=True)


gen = fromimg = 0
for path in sorted(glob.glob(f"{ART}/*.md")):
    with open(path, encoding="utf-8") as f:
        txt = f.read()
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", txt, re.S)
    if not m:
        print("skip(no front matter):", path); continue
    fm, body = m.group(1), m.group(2)
    fm = "\n".join(l for l in fm.split("\n") if not l.startswith("thumbnail:"))
    tm = re.search(r'^title:\s*"?(.*?)"?\s*$', fm, re.M)
    title = tm.group(1) if tm else ""
    base = os.path.splitext(os.path.basename(path))[0]

    cands = []
    mm = re.search(r"!\[[^\]]*\]\(\s*([^)\s]+)", body)
    if mm: cands.append((mm.start(), mm.group(1)))
    hm = re.search(r'<img[^>]*\ssrc="([^"]+)"', body)
    if hm: cands.append((hm.start(), hm.group(1)))
    cands.sort()
    local = next((u for _, u in cands if u.startswith("/")), None)

    out = f"{THUMB_DIR}/{base}.webp"
    src = ("." + local) if local else None
    if src and os.path.isfile(src):
        make_from_image(src, out); fromimg += 1
    else:
        make_placeholder(out, title); gen += 1

    with open(path, "w", encoding="utf-8") as f:
        f.write(f"---\n{fm}\nthumbnail: /{out}\n---\n{body}")

print(f"done: from-image={fromimg}, generated={gen}")
