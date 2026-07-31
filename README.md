# RPC2026 - 中高生Rubyプログラミングコンテスト

Jekyll + Tailwind CSS を使ったコンテストサイトです。

## 開発環境のセットアップ

```bash
bundle install
npm install
```

## 起動

Jekyll と Tailwind をそれぞれ別のターミナルで起動します。

```bash
bundle exec jekyll serve --livereload   # http://localhost:4000
npm run tailwind                        # Tailwind ウォッチ
```

ブラウザで http://localhost:4000 を開きます。

### foreman を使う場合の注意

`foreman start`（`Procfile`）は現状そのままでは動きません。Tailwind v4 の `--watch` は
標準入力が TTY でないと EOF を検知して即座に終了するため、foreman 配下では 1 秒ほどで
`tailwind.1 exited with code 0` となり、foreman が Jekyll ごと停止します。

foreman で動かす場合は `--watch=always` を指定してください。

```
tailwind: npx tailwindcss -i ./_tailwind/input.css -o ./assets/main.css --watch=always
```

なお `PORT` は Jekyll が参照しないため、foreman 経由でも Jekyll は 4000 番で待ち受けます
（5000 番ではありません）。macOS では 5000 番を AirPlay Receiver が使用しています。

### 本番ビルド

```bash
npm run build                   # Tailwind CSS をビルド
bundle exec jekyll build        # Jekyll をビルド
```

`assets/main.css` はリポジトリにコミットしていますが、`--watch` での増分ビルドは
使わなくなったクラスをすぐには取り除きません。コミット前に `npm run build` で
クリーンビルドし直すと差分が安定します。

## デプロイ

`main` への push で GitHub Actions（`.github/workflows/pages.yml`）が動き、
GitHub Pages へ公開されます。CI 側で `npm run build` → `bundle exec jekyll build` を
実行するため、`assets/main.css` は CI で生成し直されます。

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
├── _articles/            # お知らせ記事（コレクション）
├── _data/
│   ├── judges.yml        # 審査委員データ
│   ├── results.yml       # 最終審査結果データ
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
│   │   ├── articles/     # お知らせ記事の画像・サムネイル
│   │   ├── common/       # 全ページ共通（ファビコン、背景、部門アイコン等）
│   │   ├── home/         # トップページ
│   │   ├── judges/       # 審査委員の写真
│   │   ├── related-links/# 関連リンク
│   │   ├── results/      # 最終審査結果
│   │   └── sponsors/     # 協賛企業のロゴ
│   └── main.css          # ビルド済みCSS（Tailwind 出力）
├── scripts/
│   └── gen_thumbnails.py # 記事サムネイル生成
├── index.html
├── entry.html            # 募集要項 /entry/
├── creative-coding.md    # クリエイティブコーディング部門募集のご案内 /creative-coding/
├── judges.html           # 審査委員紹介 /judges/
├── sponsors.html         # 協賛企業 /sponsors/
├── articles.html         # お知らせ一覧 /articles/
├── final.html            # 最終審査会 /final/
├── results.html          # 最終審査結果 /results/
├── ai-policy.html        # AI利用方針 /ai-policy/
├── privacy.html          # 個人情報保護方針 /privacy/
├── 404.html
├── CNAME                 # 独自ドメイン（2026.ruby-procon.net）
├── Procfile              # Foreman 設定
└── package.json          # npm 設定（Tailwind）
```

### 非公開中のページ

`final.html` / `results.html` は未公開のため、`_includes/header.html` のナビリンクを
`{% comment %}` でコメントアウトしています。`sponsors.html` も同様です。
公開時は該当の `{% comment %}` / `{% endcomment %}` を外します。

トップページの協賛関連セクション（スポンサー募集 CTA・協賛企業ロゴ一覧）も
`index.html` 内で同じ方法でコメントアウトしています。

## 除外している gem

以下の gem は `.bundle/config` の `exclude_gems` で除外しています。

| gem | 理由 |
|-----|------|
| `eventmachine` / `em-websocket` | 長期メンテナンス停止のため積極的には使わない方針 |
| `sass-embedded` / `jekyll-sass-converter` | SCSS を使わないため。Jekyll 本体の依存のため Gemfile.lock には残るが無効化 |

`eventmachine` / `em-websocket` は除外設定に入っていますが、Gemfile.lock に残っており
実際にはインストール済みのため、`bundle exec jekyll serve --livereload` は動作します
（LiveReload は 35729 番で待ち受け、ページに `livereload.js` が注入されます）。
