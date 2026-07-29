---
layout: page
title: クリエイティブコーディング部門募集のご案内
title_html: "クリエイティブコーディング部門<br>募集のご案内"
permalink: /creative-coding/
content_width: max-w-4xl
content_class: l--creative-coding-guide
prose: true
thumbnail: /assets/images/articles/thumbnails/2026-07-24-creative-coding-guide.jpg
description: 今年から新設されたクリエイティブコーディング部門について、作品づくりの始め方やrbCanvas/p5の使い方、作例を審査委員の小芝（chobishiba）が紹介します。
---

こんにちは、中高生Rubyプログラミングコンテスト クリエイティブコーディング部門 審査委員の小芝（chobishiba）です。今年から新設されたクリエイティブコーディング部門を紹介します。

## クリエイティブコーディングとは

クリエイティブコーディングとは、簡単にいうと「コードでビジュアルアート作品を作る」ことです。

たとえば以下のようなビジュアルも、すべてコードで作れます。

![コードで制作したルビー、動物や花、青い模様のビジュアル作品](/assets/images/articles/2026-07-24-creative-coding-guide/examples.webp)

実際のコードはこちらです。

- 左：<a href="https://ksbmyk.github.io/sketch/20260213/" target="_blank" rel="noopener noreferrer">Ruby gem</a>
- 中央：<a href="https://ksbmyk.github.io/sketch/20240504/" target="_blank" rel="noopener noreferrer">花・うさぎ・くま・雪だるま</a>
- 右：<a href="https://ksbmyk.github.io/sketch/20240605/" target="_blank" rel="noopener noreferrer">青い模様</a>

## クリエイティブコーディング部門とは

今年から新設された、Rubyを使ったビジュアルアート作品で応募できる部門です。

- **テーマ：**「ルビー」
- **使用ツール：**<a href="https://rbcanvas.net/p5/" target="_blank" rel="noopener noreferrer">rbCanvas/p5</a>（ブラウザ上でRubyを使ってグラフィックを描けるツール。詳しくは後述します）
- **応募締切：**2026年9月30日（水）

テーマの「ルビー」は、宝石のルビー、プログラミング言語のRuby、ルビーという色や言葉。そのどれを出発点にしてもかまいません。テーマの解釈に正解も間違いもありません。

応募のときには、テーマをどう解釈したか、作品にどんな工夫を込めたかを書く欄があります。うまく書こうとしなくて大丈夫です。あなたの考えたことが伝われば十分です。

最終審査会でのプレゼンテーションはありません。提出した作品と応募書類で審査され、受賞作品はコンテスト公式ウェブサイト等で展示・公表されます。

詳しい応募条件や審査方法は「[募集要項](/entry/)」をご覧ください。

## さわってみよう

クリエイティブコーディングがどんなものか体験できる<a href="https://ksbmyk.github.io/sketch/events/tangible_code.html" target="_blank" rel="noopener noreferrer">サンプルページ</a>を用意しました。

左に表示されるコードの実行結果が、右に表示されます。変数を動かして、自分の気に入った組み合わせを探してみてください。

![変数を調整して赤い花のような模様を表示したサンプル](/assets/images/articles/2026-07-24-creative-coding-guide/tangible-code-red.webp)

![コードの変数を操作し、右側の花のような模様を変化させるサンプル](/assets/images/articles/2026-07-24-creative-coding-guide/tangible-code.webp)

このように同じロジックでも、変数の値を少し変えるだけで表現が変化します。これもクリエイティブコーディングの楽しさのひとつです。正解はありません。試行錯誤しながら、自分がいいと思う表現を見つけていきます。

## どうやって作る？

<a href="https://p5js.org/" target="_blank" rel="noopener noreferrer">p5.js</a>の便利な関数を活用しながら、Rubyの構文で作品を作っていきます。p5.jsを使わなくても描けますが、描画に便利な関数がひととおりそろっているので、使うとグラフィックが作りやすくなります。

> **p5.jsとは：** Processingという、美術やデザインでの利用を想定して作られた、ビジュアル生成が簡単にできるプログラミング環境があります。それをJavaScriptのライブラリにしたものがp5.jsです。

Webエディタがあるので、PCに何かをインストールする必要はありません。<a href="https://rbcanvas.net/p5/" target="_blank" rel="noopener noreferrer">rbCanvas/p5</a>を使ってやってみましょう。

トップページにはバージョンが2つ並んでいますが、最新版の「ver. 0.5.1」のほう（βではないほう）をクリックしてください。左側がエディタ、右側に実行結果が表示されます。

<img src="/assets/images/articles/2026-07-24-creative-coding-guide/rbcanvas-top.webp" alt="rbCanvas/p5のトップページに表示されたエディタのバージョン選択" class="a--creative-coding-image-medium">

![左側にRubyのコード、右側に実行結果が表示されるrbCanvas/p5のWebエディタ](/assets/images/articles/2026-07-24-creative-coding-guide/editor-before.webp)

サンプルコードがすでに書かれているので、画面左上の実行ボタン（▶）を押すと右に実行結果が表示されます。

![実行ボタンを押して右側に実行結果を表示したrbCanvas/p5のWebエディタ](/assets/images/articles/2026-07-24-creative-coding-guide/editor.webp)

詳しい使い方は「<a href="https://rbcanvas.net/p5/0.5.1/site/about_editor.html" target="_blank" rel="noopener noreferrer">rbCanvas/p5エディタの使い方</a>」にあります。

## 自分でも描いてみよう

### まずは円を1つ描く

```ruby
def setup
  createCanvas(300, 300)
end

def draw
  fill(255, 0, 0)
  circle(150, 150, 100)
end
```

<img src="/assets/images/articles/2026-07-24-creative-coding-guide/circle.webp" alt="Rubyのコードで赤い円を1つ描いた実行例" class="a--creative-coding-image-medium">

### ランダムに配置する

基本の形は円のコードと同じで、繰り返し（`times`）とランダム（`rand`）が増えています。

<a href="https://ksbmyk.github.io/sketch/20230506/" target="_blank" rel="noopener noreferrer"><img src="/assets/images/articles/2026-07-24-creative-coding-guide/random.webp" alt="ランダムに配置した青い円の作品とRubyコード"></a>

<a href="https://ksbmyk.github.io/sketch/20230506/" target="_blank" rel="noopener noreferrer">実際のコードはこちら →</a>

### 敷き詰める

今度は円を規則正しく並べています。色は、決めた4色の中からランダムに選んでいます。

<a href="https://ksbmyk.github.io/sketch/20230830/" target="_blank" rel="noopener noreferrer"><img src="/assets/images/articles/2026-07-24-creative-coding-guide/tiled.webp" alt="4色の円を規則正しく敷き詰めた作品とRubyコード"></a>

<a href="https://ksbmyk.github.io/sketch/20230830/" target="_blank" rel="noopener noreferrer">実際のコードはこちら →</a>

### フラクタルにする

大きな円の中に半分の大きさの円を描いて、その円の中にまた半分の円を……と繰り返していくと、こんな模様になります。ここでも使っているのは、円と繰り返しだけです。

<a href="https://ksbmyk.github.io/sketch/20250112/" target="_blank" rel="noopener noreferrer"><img src="/assets/images/articles/2026-07-24-creative-coding-guide/fractal.webp" alt="色とりどりの円を再帰的に描いたフラクタル作品とRubyコード"></a>

<a href="https://ksbmyk.github.io/sketch/20250112/" target="_blank" rel="noopener noreferrer">実際のコードはこちら →</a>

このように円1つでもさまざまなことができますが、円以外にも三角も四角も直線も描けますし、組み合わせることもできます。静止画だけでなくアニメーションや、クリックしたときに反応するようなインタラクティブなもの、実行するたびに結果の変わるものも作れます。

そういった描画を簡単にする関数がたくさん用意されています。どんなものがあるかは「<a href="https://rbcanvas.net/p5/0.5.1/site/manual/index.html" target="_blank" rel="noopener noreferrer">rbCanvas/p5のAPIリファレンス</a>」で調べられます（エディタ左上の「Help」ボタンからも同じものが開きます）。サンプルコード付きなので、コピーしてそのまま動かせます。

p5.jsの世界をもっと見てみたい人は、「<a href="https://p5js.org/reference/" target="_blank" rel="noopener noreferrer">p5.js公式リファレンス</a>」ものぞいてみてください。こちらの構文はRubyに読み替えて使ってください。

## 作品が完成したら

作品が完成したら、rbCanvas/p5のエディタからHTMLファイルをダウンロードしてください。**ダウンロードしたHTMLファイルが、応募時の提出物となります。**

<img src="/assets/images/articles/2026-07-24-creative-coding-guide/download-html.webp" alt="rbCanvas/p5エディタ上部にあるHTMLファイルのダウンロードボタン" class="a--creative-coding-image-medium">

提出前に、ダウンロードしたHTMLファイルをブラウザで開き、作品が正しく動くことを確認しておきましょう。

## あなたの作品を待っています

まずは気軽に、描いてみたいものをスケッチするところから始めてみてください。最初から描きたいものを決める必要はありません。

1つ円を描いてみた。じゃあ2つにしたらどうなる？ ランダムに配置したら？ 規則正しく並べたら？ 色を変えたら？

「こっちのほうがより好きだな」「自分はこうしたいと思っているんだな」と、コードを書きながら自分の好きを突き詰めてみて、Rubyで自分だけの世界を創り出してください。

そうしてできた作品を、ぜひ応募してみてください。このコンテストを通じてRubyで何かを作る楽しみを感じてもらえればうれしいです。あなたの応募を待っています！

[募集要項を見る →](/entry/)
