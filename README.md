# RPC2026 - 中高生Rubyプログラミングコンテスト

Jekyll + Tailwind CSS を使ったコンテストサイトです。

## 開発環境のセットアップ

```bash
bundle install
npm install
```

## 起動

Foreman で Jekyll と Tailwind を同時に起動します。

```bash
foreman start
```

ブラウザで http://localhost:5000 を開きます。

### 個別に起動する場合

```bash
bundle exec jekyll serve        # Jekyll のみ（http://localhost:4000）
npm run tailwind                # Tailwind ウォッチのみ
```

### 本番ビルド

```bash
npm run build                   # Tailwind CSS をビルド
bundle exec jekyll build        # Jekyll をビルド
```

### 記事サムネイル生成

お知らせ記事のサムネイルは `scripts/gen_thumbnails.py` で生成します。

```bash
scripts/gen_thumbnails.py
```

各記事の本文に最初のローカル画像があれば、それを 1280x720 の WebP に変換して `assets/images/articles/thumbnails/` に保存します。画像がない記事は、タイトル入りのプレースホルダーを生成します。生成後、各記事の front matter に `thumbnail` が付与されます。

必要な外部コマンド:

- `rsvg-convert`
- ImageMagick の `magick`

### OGP

全ページの OGP / Twitter Card は `_includes/head.html` で出力します。

- 記事ページは front matter の `thumbnail` を `og:image` / `twitter:image` に使います。
- 固定ページで OGP 画像を設定する場合は front matter に `og_image: /assets/images/...` を追加します。
- `thumbnail` / `og_image` がないページでは `og:image` と `twitter:image` は空文字で出力し、生成 HTML に TODO コメントを残します。

## プロジェクト構成

```
RPC2026/
├── _config.yml           # Jekyll 設定
├── _data/
│   ├── judges.yml        # 審査委員データ
│   └── sponsors.yml      # 協賛企業データ
├── _includes/
│   ├── head.html         # <head> 要素
│   ├── header.html       # ヘッダー
│   └── footer.html       # フッター
├── _layouts/
│   ├── default.html      # 基本レイアウト
│   ├── home.html         # トップページ
│   ├── page.html         # 固定ページ
│   └── post.html         # 記事ページ
├── _tailwind/
│   └── input.css         # Tailwind 入力CSS
├── assets/
│   ├── images/
│   │   ├── judges/       # 審査委員の写真
│   │   └── sponsors/     # 協賛企業のロゴ
│   └── main.css          # ビルド済みCSS（Tailwind 出力）
├── index.html
├── judges.html           # 審査委員紹介 /judges/
├── entry.html            # 応募要項 /entry/
├── sponsors.html         # 協賛企業 /sponsors/
├── final.html            # 最終審査会 /final/
├── 404.html
├── Procfile              # Foreman 設定
└── package.json          # npm 設定（Tailwind）
```

## 除外している gem

以下の gem は `.bundle/config` の `exclude_gems` で除外しています。

| gem | 理由 |
|-----|------|
| `eventmachine` / `em-websocket` | 長期メンテナンス停止。`--livereload` は使わない方針 |
| `sass-embedded` / `jekyll-sass-converter` | SCSS を使わないため。Jekyll 本体の依存のため Gemfile.lock には残るが無効化 |

`--livereload` オプションは使えません。
