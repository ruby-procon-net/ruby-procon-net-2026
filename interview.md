---
layout: page
title: "AIがコードを書く時代、それでも「作る」ことは面白い――Rubyプログラミングコンテストが目指すもの"
hero_title: まつもとゆきひろ × 鳥井雪
permalink: /interviews/matz-torii/
content_width: max-w-3xl
content_class: l--interview
prose: true
description: "AI時代のプログラミングとものづくり、そして中高生Rubyプログラミングコンテストが目指すものについて、まつもとゆきひろさんと鳥井雪さんに聞きました。"
og_image: /assets/images/interview/ogp.jpg
---

# AIがコードを書く時代、それでも「作る」ことは面白い――Rubyプログラミングコンテストが目指すもの

<img src="/assets/images/interview/ogp.jpg" alt="AIがコードを書く時代、それでも「作る」ことは面白い。まつもとゆきひろさん、鳥井雪さん、笹田耕一さん" class="not-prose mt-8 mb-10 w-full rounded-2xl" width="1280" height="720">

生成AIに「こんなものを作って」と頼めば、プログラムを書いてくれる。動かなければ「直して」と頼むこともできる。

そんな時代に、プログラミングを学ぶ意味はどこにあるのでしょうか。そして、あえてRubyを使ったプログラミングコンテストを開催することには、どんな意味があるのでしょうか。

「第16回 中高生Rubyプログラミングコンテスト2026」では、応募作品の制作に生成AIを積極的に活用してほしい、という方針を打ち出しています。

AIがコードを書いてくれるのなら、これからプログラマーという仕事はどうなるのか。AI時代にもRubyを使う意味はあるのか。そして、コンテストではいったい何を競うのか。

Ruby開発者で審査委員のまつもとゆきひろさんと、実行委員長の鳥井雪さんに、実行委員の笹田耕一さんが聞きました。

<div class="l--interview-profiles not-prose grid gap-6 my-10">
  <section class="flex flex-col items-center gap-8 rounded-2xl border border-gray-200 bg-gray-50 p-5 text-center sm:flex-row sm:text-left">
    <img src="/assets/images/judges/matz.webp" alt="まつもとゆきひろさん" class="h-28 w-28 shrink-0 rounded-full object-cover">
    <div>
      <h2 class="text-xl font-bold text-gray-900">まつもとゆきひろ</h2>
      <p class="mt-1 text-sm font-semibold leading-relaxed text-grape">本コンテスト審査委員／一般財団法人Rubyアソシエーション 理事長</p>
      <p class="mt-3 text-sm leading-relaxed text-gray-600">プログラミング言語Rubyの開発者。1993年から開発を開始。株式会社ネットワーク応用通信研究所フェロー。島根県松江市在住、松江市名誉市民。</p>
    </div>
  </section>

  <section class="flex flex-col items-center gap-8 rounded-2xl border border-gray-200 bg-gray-50 p-5 text-center sm:flex-row sm:text-left">
    <img src="/assets/images/interview/yuki-torii.webp" alt="鳥井雪さん" class="h-28 w-28 shrink-0 rounded-full object-cover">
    <div>
      <h2 class="text-xl font-bold text-gray-900">鳥井雪</h2>
      <p class="mt-1 text-sm font-semibold leading-relaxed text-grape">本コンテスト実行委員長／NPO法人Waffle カリキュラム・マネージャー</p>
      <p class="mt-3 text-sm leading-relaxed text-gray-600">Webアプリケーション開発者として15年以上のキャリアを持つ。子どもや初心者向けのプログラミング書籍の翻訳・執筆にも携わる。株式会社万葉フェロー。</p>
    </div>
  </section>

  <section class="flex flex-col items-center gap-8 rounded-2xl border border-gray-200 bg-gray-50 p-5 text-center sm:flex-row sm:text-left">
    <img src="/assets/images/interview/koichi-sasada.webp" alt="笹田耕一さん" class="h-28 w-28 shrink-0 rounded-2xl bg-white object-contain">
    <div>
      <h2 class="text-xl font-bold text-gray-900">笹田耕一</h2>
      <p class="mt-1 text-sm font-semibold leading-relaxed text-grape">聞き手／本コンテスト実行委員／一般財団法人Rubyアソシエーション 理事</p>
      <p class="mt-3 text-sm leading-relaxed text-gray-600">Ruby向け仮想マシンYARVを開発し、Ruby 1.9に採用される。Rubyコミッターとして言語処理系の高速化や並行・並列処理機能の実装などに携わる。STORES株式会社所属。博士（情報理工学）。</p>
    </div>
  </section>
</div>

## 「コードを書く」ことは、プログラミングの中心ではなくなる？

<span class="a--interview-speaker"><img src="/assets/images/interview/koichi-sasada.webp" alt=""><strong>笹田：</strong></span> まず大きなところから聞いてみたいんですが、AIがこれだけプログラムを書けるようになると、これからプログラミングはどうなっていくんでしょう。

<span class="a--interview-speaker"><img src="/assets/images/judges/matz.webp" alt=""><strong>まつもと：</strong></span> 私自身、コードを直接書くことはかなり減っています。AIに「こんなものが欲しい」と言うとコードを書いてくれて、うまく動かなかったら「直して」と言う。自分でコードを編集する機会は、以前と比べると本当に少なくなりました。

そうすると、「人間にとって書きやすいことを大事にしてきたRubyは、AIがコードを書く時代には必要ないんじゃないか」という疑問は当然出てきますよね。

でも、AIが全部バイナリを直接生成すればいい、というところまでは行かないと思っています。人間が読めるプログラムには、「なぜこうしたのか」といった情報も残せますし、いざというときに人間が調べられる安心感もあります。

それに、何もかもAIにゼロから作らせるのは、あまり効率がよくありません。Rubyには長年積み重ねてきたライブラリやフレームワークがあります。そういう資産を利用した方がいい。

人間にとって扱いやすい言語は、AIにとっても効率のよい言語になる可能性がありますし、Ruby自身も性能を含めて進歩し続けています。だから私は、AI時代でもRubyは結構いいところにいるんじゃないかと思っています。

<span class="a--interview-speaker"><img src="/assets/images/interview/yuki-torii.webp" alt=""><strong>鳥井：</strong></span> Railsのようなフレームワークも、単なるコードの集まりではないですよね。「Webアプリを作るには何が必要なのか」という知識が長い時間をかけて積み重なったものです。作ることよりも前に、「何が必要なのか／必要でないのか」を探し、合意をとっていくプロセスがある。それを全部AIに一から考え直させるのは大変だと思います。

## プログラマーは「何を作るか」を考える仕事へ

<span class="a--interview-speaker"><img src="/assets/images/interview/koichi-sasada.webp" alt=""><strong>笹田：</strong></span> では、職業としてのプログラマーはどうなるでしょう。私たちはプログラムを書くことでお給料をもらっていますが、その仕事はなくなってしまいますか。

<span class="a--interview-speaker"><img src="/assets/images/judges/matz.webp" alt=""><strong>まつもと：</strong></span> 「コードを書くことだけをする仕事」は減っていくと思います。

その代わりに、これまで「上流」と呼ばれてきたようなところ――顧客が何を求めているかを分析する、何を作るべきかを決める、できたものを検証してフィードバックする、といった仕事の比重が大きくなるでしょうね。

方向性を決めて、「じゃあAI、作って」と頼む。出てきたものを見て、仮説を検証する。仕事の重心が、そちらへ移っていくんじゃないでしょうか。

<span class="a--interview-speaker"><img src="/assets/images/interview/yuki-torii.webp" alt=""><strong>鳥井：</strong></span> 個人が「自分のためのもの」を作るハードルは、もうかなり下がっていますよね。

以前なら、作りたいものがあっても、それを実現するためにプログラミングを覚えなければいけなかった。でも今なら、多少ぼんやりしたところからでもAIに頼んで、まず動くものを出してもらえる。

それを使ってみて、「ここは違う」「もっとこうしたい」と直していくうちに、自分が本当に欲しかったものもわかってくる。自分の欲求を探りながら、作るものを育てていけるようになっています。

<span class="a--interview-speaker"><img src="/assets/images/interview/koichi-sasada.webp" alt=""><strong>笹田：</strong></span> 最初から完璧に「作りたいもの」を言語化できなくてもいい。とりあえず作って、触って、直すというループを回しているうちに、だんだんわかってくるということですね。

<span class="a--interview-speaker"><img src="/assets/images/interview/yuki-torii.webp" alt=""><strong>鳥井：</strong></span> そうですね。

ただ、誰でもAIを使えば、誰でも面白いものを作れるかというと、それはまた別の話です。

最初にAIへ頼むと、それなりのものは出てきます。でも、たいていは「普通のもの」なんです。そこから「もっとこうしたい」と考えて、人に使ってもらえるものや、自分の世界を少し変えるようなものまで持っていけるか。そこにはやっぱり発想や試行錯誤が必要です。

<span class="a--interview-speaker"><img src="/assets/images/judges/matz.webp" alt=""><strong>まつもと：</strong></span> 「よいもの」の「よい」が何なのかを考えたり、それを具体化したりするのには、訓練も適性も必要でしょうね。

AIによって、これまで必要だったプログラミング能力の一部を助けてもらえるようになった。でも、発想やモチベーションまでAIが代わりに持ってくれるわけではありません。

## 誰でも作れる時代だからこそ、「作る側」に回ってみる

<span class="a--interview-speaker"><img src="/assets/images/interview/koichi-sasada.webp" alt=""><strong>笹田：</strong></span> そこは今回のプログラミングコンテストにもつながりそうですね。

<span class="a--interview-speaker"><img src="/assets/images/interview/yuki-torii.webp" alt=""><strong>鳥井：</strong></span> 私は、プログラミングコンテストが提供できる一番大きなものは、「作る側に立つ体験」なんじゃないかと思っています。

AIがあることで、「技術的には誰でも作れる」範囲はものすごく広がりました。でも、誰もが実際に作るわけではありません。

コンテストというきっかけがあって、一度でも作る側に回ってみる。「自分にもこんなものが作れるんだ」と知る。まず、その体験をしてほしいです。

さらに、コンテストでは「審査される」意識をもつことができます。簡単な指示でAIが作った「通り一遍」のアプリの先を目指す刺激にもなるのではないかと期待しています。

<span class="a--interview-speaker"><img src="/assets/images/judges/matz.webp" alt=""><strong>まつもと：</strong></span> そもそも、何のきっかけもなく自分でコンピューターを探して、勝手にプログラミングを始める「野生のプログラマー」って、そんなに多くないんですよ。私はそういうタイプだったんですけど（笑）。

実際には、「コンテストがあるから作ってみた」とか、「スクールで勉強したのがきっかけだった」という人の方がずっと多い。

だから、きっかけが必要なんです。このコンテストが、その一つになればいいと思っています。

<span class="a--interview-speaker"><img src="/assets/images/interview/koichi-sasada.webp" alt=""><strong>笹田：</strong></span> 「プログラマーを増やす」こと自体が目的なんでしょうか。

<span class="a--interview-speaker"><img src="/assets/images/judges/matz.webp" alt=""><strong>まつもと：</strong></span> 私は単純に、プログラミングは楽しいと思っているので、この楽しいことを一緒に楽しんでくれる人が増えたらいいな、という気持ちですね。日本の国力のために、とか、そういうことはあまり考えていません（笑）。

<span class="a--interview-speaker"><img src="/assets/images/interview/yuki-torii.webp" alt=""><strong>鳥井：</strong></span> 私は少し違う観点もあります。

今の社会は、コンピューターやソフトウェアなしでは成立しません。そのソフトウェアを「誰かが作ったものとして与えられる」だけではなく、自分でも作れるということは、社会に働きかける手段を持つことだと思っています。

そして、作る人の幅が広がることも重要です。ソフトウェアは社会への影響が大きいのに、作り手にはまだ偏りがある。いろいろな人が作る側に入ることで、それまで見落とされていた問題や、新しい発想も入ってくるはずです。

今回、従来のゲーム部門、アプリ部門に加えて「クリエイティブコーディング部門」を新設したのは、さらに多様な作り手に参加してほしいという意図があります。

<span class="a--interview-speaker"><img src="/assets/images/judges/matz.webp" alt=""><strong>まつもと：</strong></span> それに、飛び抜けた人だけを最初から見つけて育てることはできませんからね。

野球だって、将来プロになる何百人だけを最初から探して育てることはできない。たくさんの人が野球をする中から、すごい選手が出てくる。プログラミングも同じだと思います。

## AIを使って応募していい。むしろ、使ってほしい

<span class="a--interview-speaker"><img src="/assets/images/interview/koichi-sasada.webp" alt=""><strong>笹田：</strong></span> 今回のコンテストでは、AIコーディングを積極的に使ってください、という方針を出しています。プログラミングコンテストでAIを使うことについては、どう考えていますか。

<span class="a--interview-speaker"><img src="/assets/images/interview/yuki-torii.webp" alt=""><strong>鳥井：</strong></span> AIを使う一番大きなメリットは、作品をブラッシュアップするサイクルを速くできることです。

一度作ってみて、試して、直して、また試す。そのサイクルをたくさん回すことで、プロダクトの質を上げられる。AIはそのための強力な道具です。

もちろん、学習の過程でAIを使わず、自分でコードを書いてみる経験も大切だと思います。

ただ、コンテストとして競うのであれば、AIを使える人と使えない人がいて、スタート地点で差がついてしまうのは避けたい。特にAIを利用できる環境は、家庭や経済的な状況にも左右されます。

そこで今回は、みんなのコードさんの協力で、応募者が無償で生成AIを利用できる環境も用意しています。同じ土俵で、使いたい人にはぜひ使ってほしいと思っています。

<span class="a--interview-speaker"><img src="/assets/images/interview/koichi-sasada.webp" alt=""><strong>笹田：</strong></span> AIを使わないとダメ、ということではない？

<span class="a--interview-speaker"><img src="/assets/images/interview/yuki-torii.webp" alt=""><strong>鳥井：</strong></span> そうではありません。

ただ、AIに仕事を頼みながらも、何を採用するのか、どこを直すのかという意思決定は自分でする。その使い方自体も、これから必要になる経験だと思います。このコンテストを、そういうことを試す機会にもしてほしいですね。

<span class="a--interview-speaker"><img src="/assets/images/judges/matz.webp" alt=""><strong>まつもと：</strong></span> 私はもっと単純に、AIは道具の一つだから、使いたければ使えばいいと思っています。

若い人たちと話していると、大人のプログラマーほど「AIで世界が変わる！」とは騒いでいなかったりするんですよ（笑）。ChatGPTやGeminiは普通に使っていても、「AIだから特別」という意識は案外薄い。

だから、AIだからどうこうと必要以上に構えることもないのかもしれません。

## 審査するのは「AIを使ったか」ではなく、「何を作ったか」

<span class="a--interview-speaker"><img src="/assets/images/interview/koichi-sasada.webp" alt=""><strong>笹田：</strong></span> では審査する側からすると、明らかに手で書いたようなコードと、AIが生成したようなきれいなコードが来ても、そこはあまり関係ない？

<span class="a--interview-speaker"><img src="/assets/images/judges/matz.webp" alt=""><strong>まつもと：</strong></span> 私自身は、AIを使ったからどう、という見方はあまりしないつもりです。

見たいのは、**どんなアイデアを、どこまで具体化したか**です。

最初はぼんやりしていたアイデアを、どこまで目に見えるものにできたのか。評価軸そのものは、AIが登場する前とそんなに変わらないと思っています。

その途中でAIを使った結果、試行錯誤を速く回せた、仮説検証をたくさんできた、それによって自分なりにもっとよい作品にできた、というのであれば、それはぜひ聞いてみたいですね。

AIを使ったかどうかではなく、出てきた作品を見る。AIを使って作品がよくなるなら、大歓迎です。

## AIが作ってくれる時代に、人間は何をするのか

話を振り返ると、AIによってプログラミングから「コードを書く」という作業の比重が下がったとしても、「作る」という営みそのものがなくなるわけではなさそうです。

むしろ、コードを書くハードルが下がった分だけ、

> 「何が欲しいんだろう」<br>
> 「試してみたけれど、何か違う」<br>
> 「もっと面白くできないだろうか」<br>
> 「誰かに使ってもらうには、どうすればいいだろう」

と考える部分が、これまで以上に表に出てきます。

そして、それは実際に何かを作り、試し、失敗し、直してみなければ、なかなか身につきません。

最後に、これから応募する中高生へ、二人からメッセージをもらいました。

<span class="a--interview-speaker"><img src="/assets/images/interview/yuki-torii.webp" alt=""><strong>鳥井：</strong></span> 作る体験を通して、自分のアイデアを深めていってほしいと思います。

自分がやりたいことを実現するためなら、使えるものは何でも使ってください。プログラミングでも、AIでも、Rubyでもいい。

まず作る側に回って、「自分は何をしたいのか」を、自分なりの一番いい形で見せてほしいです。

<span class="a--interview-speaker"><img src="/assets/images/judges/matz.webp" alt=""><strong>まつもと：</strong></span> 「俺の素晴らしいアイデアを見ろ」って言ってほしいですね。

「お前たちは俺のアイデアをわかれ」っていうくらいの感じで、殴り込んできてほしい（笑）。

<span class="a--interview-speaker"><img src="/assets/images/interview/koichi-sasada.webp" alt=""><strong>笹田：</strong></span> AIを使ったかどうかではなく、「これを作りたかったんだ」というものを持ってきてほしい、と。

<span class="a--interview-speaker"><img src="/assets/images/judges/matz.webp" alt=""><strong>まつもと：</strong></span> そうですね。

AIがコードを書いてくれる時代だからこそ、「何を作りたいか」は、あなた自身のものです。

今年はぜひ、そのアイデアをRubyで形にしてみてください。

{% include recruitment-cta.html %}
