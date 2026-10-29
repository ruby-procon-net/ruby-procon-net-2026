---
layout: page
title: '「作ること」を楽しみ、その先の誰かに届ける — SmartHRがRubyプログラミングコンテストに期待すること'
hero_title: SmartHR 齋藤諒一
permalink: /interviews/smarthr/
content_width: max-w-3xl
content_class: l--interview
prose: true
description: '株式会社SmartHRのVP of Engineering・齋藤諒一さんに、Rubyを使う理由、AI時代のエンジニアの仕事、そして中高生のものづくりに期待することを聞きました。'
---

# 「作ること」を楽しみ、<br>その先の誰かに届ける

<p class="not-prose text-xl font-bold text-gray-900">SmartHRがRubyプログラミングコンテストに期待すること</p>

<div class="a--interview-visual not-prose" role="group" aria-label="SmartHR 齋藤諒一さんインタビュー">
  <div class="a--interview-visual-copy">
    <p class="a--interview-visual-label">INTERVIEW</p>
    <p class="a--interview-visual-title">「作ること」を楽しみ、<br>その先の誰かに届ける</p>
    <p class="a--interview-visual-name">株式会社SmartHR<br>VP of Engineering <strong>齋藤諒一さん</strong></p>
  </div>
  <div class="a--interview-visual-images">
    <img class="a--interview-visual-portrait" src="/assets/images/interview/ryoichi-saito.png" alt="齋藤諒一さん" width="424" height="424">
    <img class="a--interview-visual-logo" src="/assets/images/sponsors/2026/smart-hr.svg" alt="SmartHR">
  </div>
</div>

Rubyプログラミングコンテスト2026では、多くの企業のみなさまにご協賛いただいています。

今回は協賛企業のひとつ、株式会社SmartHRでVP of Engineeringを務める齋藤諒一さんにお話を伺いました。

SmartHRではRubyがどのように使われているのか。AIがプログラムを書くことが当たり前になりつつある今、エンジニアの仕事はどう変わっているのか。そして、今プログラミングを楽しんでいる中高生が社会に出る5年後、10年後には、何が大切になるのか。

Rubyプログラミングコンテスト実行委員長の鳥井雪と、Ruby開発者の笹田耕一が聞きました。

**聞き手：鳥井雪、笹田耕一**

<div class="l--interview-profiles not-prose grid gap-6 my-10">
  <section class="flex flex-col items-center gap-8 rounded-2xl border border-gray-200 bg-gray-50 p-5 text-center sm:flex-row sm:text-left">
    <img src="/assets/images/interview/ryoichi-saito.png" alt="齋藤諒一さん" class="h-28 w-28 shrink-0 rounded-full object-cover" width="424" height="424">
    <div>
      <h2 class="text-xl font-bold text-gray-900">齋藤諒一</h2>
      <p class="mt-1 text-sm font-semibold leading-relaxed text-grape">株式会社SmartHR／VP of Engineering</p>
      <p class="mt-3 text-sm leading-relaxed text-gray-600">プロダクト開発に関係する約280〜290人の組織を統括。技術戦略や、事業の目標を達成するための組織づくりを担当。</p>
    </div>
  </section>

  <section class="flex flex-col items-center gap-8 rounded-2xl border border-gray-200 bg-gray-50 p-5 text-center sm:flex-row sm:text-left">
    <img src="/assets/images/interview/yuki-torii.webp" alt="鳥井雪さん" class="h-28 w-28 shrink-0 rounded-full object-cover">
    <div>
      <h2 class="text-xl font-bold text-gray-900">鳥井雪</h2>
      <p class="mt-1 text-sm font-semibold leading-relaxed text-grape">聞き手／本コンテスト実行委員長／NPO法人Waffle カリキュラム・マネージャー</p>
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

## 「誰もがその人らしく働ける社会」を、ソフトウェアでつくる

<span class="a--interview-speaker"><img src="/assets/images/interview/yuki-torii.webp" alt=""><strong>鳥井：</strong></span> まず、SmartHRさんがどんな会社なのか教えていただけますか。

<span class="a--interview-speaker"><img src="/assets/images/interview/ryoichi-saito.png" alt=""><strong>齋藤：</strong></span> SmartHRは、人事・労務を中心としたサービスを提供している会社です。会社としては、労働にまつわる社会課題をなくして、誰もがその人らしく働ける社会をつくることを目指しています。

もともとは、人事や労務など、会社の「バックオフィス」と呼ばれる仕事を支えるところから始まりました。今はそこから事業を広げて、すべての従業員がより働きやすくなるためのプロダクトを提供していこうとしています。

<span class="a--interview-speaker"><img src="/assets/images/interview/yuki-torii.webp" alt=""><strong>鳥井：</strong></span> 私、実はSmartHRのプロダクトのファンなんです。

年末調整で使わせてもらっているんですけど、それまで年末調整って、私にとってはかなり苦手な作業のひとつでした。SmartHRが入って、ものすごく助けられました。

単に紙の書類がWebになったという感じではなくて、年末調整そのものが別の体験になったなと思っています。

<span class="a--interview-speaker"><img src="/assets/images/interview/ryoichi-saito.png" alt=""><strong>齋藤：</strong></span> 年末調整は、まさに私たちが目指しているものがうまく形になった例のひとつです。もともとの書類をそのままコンピューターの画面に置き換えるのではなくて、「この分かりにくい書類のどこに何を書けばいいのか分からない」という問題そのものを変えたいんです。

質問に順番に答えていけば、必要な書類ができあがる。そういう形にして、仕事のプロセスそのものを変えていく。それが私たちのつくりたいプロダクトです。

<span class="a--interview-speaker"><img src="/assets/images/interview/yuki-torii.webp" alt=""><strong>鳥井：</strong></span> 私が「新しい体験になった」と感じたのは、まさにそこなんですね。

## 約300人の開発組織と、技術の未来を考える

<span class="a--interview-speaker"><img src="/assets/images/interview/yuki-torii.webp" alt=""><strong>鳥井：</strong></span> 齋藤さんご自身は、SmartHRでどんな仕事をされているのでしょうか。

<span class="a--interview-speaker"><img src="/assets/images/interview/ryoichi-saito.png" alt=""><strong>齋藤：</strong></span> VP of Engineeringという役割を担当しています。プロダクトをつくるエンジニアだけでなく、品質を保証するQAエンジニア、画面に表示する文章などを考えるUXライター、サポートコンテンツをつくる人たちなど、プロダクト開発に関係する約280〜290人の組織を見ています。

技術戦略を考えたり、この先どう組織を大きくしていくのか、事業の目標を達成するためにどんな組織が必要なのかを考えたりするのも仕事です。

<span class="a--interview-speaker"><img src="/assets/images/interview/yuki-torii.webp" alt=""><strong>鳥井：</strong></span> いろいろな職種の方が一緒にひとつのプロダクトをつくっているんですね。それだけ幅広い組織を見るのは大変そうです。

<span class="a--interview-speaker"><img src="/assets/images/interview/ryoichi-saito.png" alt=""><strong>齋藤：</strong></span> そこは、ある程度は任せています。頼れるマネージャーたちがいるので、それで成り立っています。

## SmartHRのバックエンドは、9割以上がRuby

<span class="a--interview-speaker"><img src="/assets/images/interview/yuki-torii.webp" alt=""><strong>鳥井：</strong></span> では、Rubyプログラミングコンテストらしい話を聞かせてください。SmartHRでは、Rubyはどのように使われていますか？

<span class="a--interview-speaker"><img src="/assets/images/interview/ryoichi-saito.png" alt=""><strong>齋藤：</strong></span> バックエンドの9割以上、感覚としては95％以上をRuby on Railsで開発しています。「バックエンド」というのは、Webサービスの画面の裏側で、データを処理したり保存したりしている部分ですね。

私たちにとってRubyは、プロダクトを開発し、運営していくためになくてはならない存在です。今後も基本的にはRubyが軸になるだろうと考えています。

<span class="a--interview-speaker"><img src="/assets/images/interview/yuki-torii.webp" alt=""><strong>鳥井：</strong></span> では、新しいプログラミング言語もある中で、SmartHRがRubyを使い続けているのはなぜですか？

<span class="a--interview-speaker"><img src="/assets/images/interview/ryoichi-saito.png" alt=""><strong>齋藤：</strong></span> どの言語が優れているか、という話ではないんです。SmartHRが大切にしている「プロダクトづくり」の考え方に、Rubyがいちばん合っているからです。

私たちは、「誰かの課題をどう解決するか」を考えることに、いちばん時間を使いたいと思っています。RubyとRuby on Railsを使うと、そこにたどり着くまでの技術的な準備や土台づくりにかかる時間を短くできるんです。

もうひとつの理由は、Rubyが「人間が読んで分かりやすい」言語だということです。コードを書く作業は、これからどんどんAIに任せていくことになります。それでも、個人情報のような大切なデータを扱う部分では、「ここは人間がロジックを確認して判断しなければいけない」という最後の砦が残ります。

AIに複雑な処理を書かせても、人間がさっと読んで、何をしようとしているのかを正しく理解できる。Rubyのこの読みやすさは、AIの時代になっても、私たちの開発を支える大きな強みになると思っています。

## 「Rubyを書く仕事」は、すでにかなり変わっている

<span class="a--interview-speaker"><img src="/assets/images/interview/yuki-torii.webp" alt=""><strong>鳥井：</strong></span> とはいえ、今はAIがものすごい勢いで発達していますよね。

人間が自分でプログラムを書く、という仕事も減ってきているように感じます。SmartHRでは、今どんなふうに開発しているのでしょうか。

<span class="a--interview-speaker"><img src="/assets/images/interview/ryoichi-saito.png" alt=""><strong>齋藤：</strong></span> 私自身について言えば、自分の手でRubyのコードを書くことは、ほとんどなくなっています。AIに書かせて、今はまだ人間がそれをレビューする、つまり内容を確認するという形です。

ただ、AIがコードをつくる速度に、人間のレビューが追いつかなくなりつつあります。これからは、人間が見る必要があるものと、見なくてもいいものを分けていくことになると思います。

とはいえ、SmartHRは個人情報をかなり多く扱うプロダクトです。そうした重要なデータに関わる部分まで、まったく人間が見ずにどんどん進める、というのは難しい。ですから、AIが書いたコードであっても「このプログラムは何をしているのか」を人間が理解できることは、今後も必要だと思っています。

<span class="a--interview-speaker"><img src="/assets/images/interview/yuki-torii.webp" alt=""><strong>鳥井：</strong></span> つまり、エンジニアの仕事そのものが変わってきている。

<span class="a--interview-speaker"><img src="/assets/images/interview/ryoichi-saito.png" alt=""><strong>齋藤：</strong></span> そうですね。以前は「実装する」、つまりコードを書くことが仕事の中心でした。今はむしろ、「そもそも何をつくるのか」とか、「AIがうまく仕事できるようにするには、どんな仕組みが必要か」とか、「AIがつくったものの品質をどう保証するか」といったことが重要になってきています。

## エンジニアの仕事は、みんな「企画」になる？

<span class="a--interview-speaker"><img src="/assets/images/interview/koichi-sasada.webp" alt=""><strong>笹田：</strong></span> これまで実装をしていた人たちは、みんな企画のような仕事に移ってきている、という感じなんでしょうか。

<span class="a--interview-speaker"><img src="/assets/images/interview/ryoichi-saito.png" alt=""><strong>齋藤：</strong></span> そこまでスムーズではないですね。「じゃあ今日からそうしましょう」と言って、すぐできる仕事でもありません。向いている人、向いていない人もいます。

AIが動くための仕組みをつくる人もいますし、テストを充実させて品質を保証する方向に動く人もいます。

それから、既存の大きなプロダクトには長い歴史や複雑な事情があります。そういう背景をAIはまだ全部理解できません。なので、人間が設計を考えて、それをAIに分かる形に翻訳し、実装はAIに任せる。今はそういう役割になっている人も多いですね。

<span class="a--interview-speaker"><img src="/assets/images/interview/koichi-sasada.webp" alt=""><strong>笹田：</strong></span> では、「細かいコードを書く」という仕事自体は、かなり減っている？

<span class="a--interview-speaker"><img src="/assets/images/interview/ryoichi-saito.png" alt=""><strong>齋藤：</strong></span> そうですね。エディターをほとんど開かない人も増えています。ターミナルだけで実装工程が全部終わる、という感じですね。

<span class="a--interview-speaker"><img src="/assets/images/interview/yuki-torii.webp" alt=""><strong>鳥井：</strong></span> その変化の先では、さらにどんなふうに仕事が変わっていくと考えていますか？

## エンジニアの仕事は「どう書くか」から「何を解くか」へ

<span class="a--interview-speaker"><img src="/assets/images/interview/ryoichi-saito.png" alt=""><strong>齋藤：</strong></span> すでにコードを書く仕事の多くをAIに移しているので、今後はできるだけ人間の手を介さずに進められるようにしていくと思います。人がレビューする必要のないものは、自動的に判断して、そのまま反映する。そういうものを増やしていく。

その一方で、人間は「何をつくるのか」「どの課題を解くのか」という方へ、どんどん移っていかなければいけないと思っています。

<span class="a--interview-speaker"><img src="/assets/images/interview/yuki-torii.webp" alt=""><strong>鳥井：</strong></span> Rubyプログラミングコンテストに参加するみなさんは、プログラミングが好きだったり、ものをつくるのが好きだったりすると思うんです。

将来IT系の仕事をしたい人もいるでしょう。

そういう中高生が5年後くらいにSmartHRへ応募してきたとして、「こういう人なら来てほしい」という人物像はありますか？

<span class="a--interview-speaker"><img src="/assets/images/interview/ryoichi-saito.png" alt=""><strong>齋藤：</strong></span> まず、「ものをつくることが好き」というのは、とても重要だと思います。自分でプログラムを書いてもいいし、AIを使ってつくってもいい。

そのうえで、何かをつくって「誰かの役に立ちたい」という気持ちのある人が重要だと思います。今後さらに大切になるのは、「人はどんなことで困っているんだろう」「それをどうしたら解決できるんだろう」と考えられることです。

自分で課題を見つけて、どう解くかを考えて、実際につくる。その一連のことを楽しめる人が、私たちの求めているエンジニア像に近いですね。

## 「ものづくりが好き」だけでも、いろいろある

<span class="a--interview-speaker"><img src="/assets/images/interview/koichi-sasada.webp" alt=""><strong>笹田：</strong></span> 「ものづくりが好き」といっても、いろいろな人がいますよね。

自分が欲しいものを自分だけのためにつくれれば満足、という人もいる。人の役に立つかどうかより、技術的に面白い問題が解ければ楽しい、という人もいる。

SmartHRの場合は、そこからもう一歩、「人の役に立つものをつくるのが楽しい」という人を求めている感じですか？

<span class="a--interview-speaker"><img src="/assets/images/interview/ryoichi-saito.png" alt=""><strong>齋藤：</strong></span> そうですね。SmartHRという事業の性質上、私たちが向き合うのは社会課題です。世の中に大きな影響を与えたい、でもいいですし、身近な人の困りごとを解決したい、でもいい。そちらにモチベーションのある人のほうが、SmartHRには合っていると思います。

人事や労務のプロダクトは、一般の人向けの派手なサービスに比べると、正直、地味に見えるところもあります。でも、確実に誰かの役に立つ。そのことに喜びを感じられる人とは、すごく相性がいいと思います。

<span class="a--interview-speaker"><img src="/assets/images/interview/koichi-sasada.webp" alt=""><strong>笹田：</strong></span> そうすると、AI時代には、社会にアンテナを張って「ここに困りごとがあるぞ」と見つける能力が、ますます大事になりそうですね。

プログラムを書く部分はAIに任せても、課題を見つけて、どう解くのかを考えるところは人間がやる。

<span class="a--interview-speaker"><img src="/assets/images/interview/ryoichi-saito.png" alt=""><strong>齋藤：</strong></span> どちらかと言えば、そうなると思います。ただし、難しい課題に取り組むときには、やはり技術力が必要です。コーディングそのものをAIに任せても、その手前で「どういう仕組みにすべきか」を判断するためには、技術についての知識や経験が必要になることがあります。

## 5年後、10年後のエンジニアはどうなっている？

<span class="a--interview-speaker"><img src="/assets/images/interview/koichi-sasada.webp" alt=""><strong>笹田：</strong></span> さっきのお話は、わりと1年後、2年後くらいの未来ですよね。

このコンテストに出ている中高生なら、就職するのは5年後かもしれない。大学院まで行けば10年後という人もいる。

5年後、10年後となると、もうだいぶ世界が違うと思うんですが、そのくらい先はどう考えていますか？

<span class="a--interview-speaker"><img src="/assets/images/interview/ryoichi-saito.png" alt=""><strong>齋藤：</strong></span> 5年後、10年後にエンジニアの役割がどうなっているかは、正直もう想像がつかないくらいです。ただ、「課題を見つけて、それを解く」ということ自体は、それほど変わらないのではないかと思っています。

課題を見つけて、それを何かをつくることで解決する。私はそこが好きでこの仕事をしてきましたし、そこは変わらないでほしいとも思っています。プログラミングは、そのためにとても使いやすい手段だったんですよね。将来、その手段が変わることはあるかもしれません。

<span class="a--interview-speaker"><img src="/assets/images/interview/koichi-sasada.webp" alt=""><strong>笹田：</strong></span> 「プログラミングそのもの」ではなく、「ものをつくって課題を解く」というところが残る、と。

<span class="a--interview-speaker"><img src="/assets/images/interview/ryoichi-saito.png" alt=""><strong>齋藤：</strong></span> そうですね。SmartHRとしても、5年後、10年後には、社会のインフラのような存在になれるプロダクトやサービスを目指したいと思っています。

インフラって、あることが当たり前で、普段あまり意識されないものですよね。でも確実に誰かの役に立っている。そういう軸は変わらないと思います。

## プログラミングは「とても気軽に始められるものづくり」

<span class="a--interview-speaker"><img src="/assets/images/interview/yuki-torii.webp" alt=""><strong>鳥井：</strong></span> ここからは、Rubyプログラミングコンテストそのものについて聞かせてください。

SmartHRさんにはこのコンテストをご支援いただいています。どんなことを期待して協賛してくださっているのでしょうか。

<span class="a--interview-speaker"><img src="/assets/images/interview/ryoichi-saito.png" alt=""><strong>齋藤：</strong></span> プログラミングって、ものづくりの中ではとても気軽に始められるものだと思うんです。パソコンさえあれば、とりあえず始められる。実際の材料を使って何かをつくろうとすると、工具や部品など、いろいろなものが必要になりますよね。でもプログラミングなら、デジタルの世界でものをつくれるし、つくれるものの可能性もすごく広い。

そこで、自分が「こういうものをつくりたい」と思ったものを実際に形にして、ちゃんと最後までつくり切る。その経験は、とても大きいと思っています。

<span class="a--interview-speaker"><img src="/assets/images/interview/yuki-torii.webp" alt=""><strong>鳥井：</strong></span> 一つのものを最後までつくると、実力がすごく伸びる、という話もよく聞きます。

<span class="a--interview-speaker"><img src="/assets/images/interview/ryoichi-saito.png" alt=""><strong>齋藤：</strong></span> そうなんです。「ちょっとつくってみた」と「最後までつくり切った」の間には、かなり大きな差があります。

ものづくりって、最後の仕上げが大変なんですよね。よく「進捗9割から進まない」みたいな話がありますけど、そこを乗り越えて、自分が「ここまでやる」と決めたところまで完成させる。その経験をしたか、していないかは大きいと思います。

一人でも多くの中学生、高校生に、その経験をしてもらいたいです。そして5年後、10年後にITの世界に入ってきたとき、そのものづくりの経験を生かして活躍してくれたらうれしいですね。

## 昨年の作品を見て「この場を続けたい」と思った

<span class="a--interview-speaker"><img src="/assets/images/interview/yuki-torii.webp" alt=""><strong>鳥井：</strong></span> SmartHRさんには、昨年から協賛していただいています。

実際に昨年のコンテストを見てみて、どうでしたか？

<span class="a--interview-speaker"><img src="/assets/images/interview/ryoichi-saito.png" alt=""><strong>齋藤：</strong></span> 想像していた以上に、作品のレベルが高かったですね。作品の種類も幅広かったですし、細かいところまでこだわっている作品も多かった。「本当にものづくりが好きな人たちが集まっているんだな」と感じました。

そういう人たちが作品を発表できる場として、このコンテストはすごく機能していると思いましたし、ぜひ途絶えずに続いてほしいと思いました。それが、今年も協賛したいと思った理由です。

## SmartHR賞は「楽しんでつくったことが伝わってくる作品」に

<span class="a--interview-speaker"><img src="/assets/images/interview/yuki-torii.webp" alt=""><strong>鳥井：</strong></span> 今年はSmartHR賞もあります。どんな作品に賞を贈りたいですか？

<span class="a--interview-speaker"><img src="/assets/images/interview/ryoichi-saito.png" alt=""><strong>齋藤：</strong></span> SmartHR賞で大切にしたいのは、「この人、本当にものづくりを楽しんでいるな」と感じられることです。まだ細かい審査基準まで決めているわけではないんですが、そういう作品に贈りたいですね。

先ほどは、SmartHRで働くエンジニアには「誰かの課題を解く」姿勢が大切だという話をしました。それはそれで欠かせないのですが、SmartHR賞では、まずはつくることそのものを思いきり楽しむ、その気持ちを応援する賞にしたいと思っています。

もちろん、完成度が高いことも素晴らしいです。でも単純にクオリティだけではなくて、どれだけ楽しんでつくったのかが作品から伝わってくる。そこを見たいと思っています。

<span class="a--interview-speaker"><img src="/assets/images/interview/yuki-torii.webp" alt=""><strong>鳥井：</strong></span> 「上手につくったもの」だけではなくて、「楽しくつくったことが見えるもの」。

<span class="a--interview-speaker"><img src="/assets/images/interview/ryoichi-saito.png" alt=""><strong>齋藤：</strong></span> そうですね。それがベースになると思います。

## 作ったものを、人に見せてみよう

<span class="a--interview-speaker"><img src="/assets/images/interview/yuki-torii.webp" alt=""><strong>鳥井：</strong></span> 最後に、これから作品をつくる参加者のみなさんへメッセージをお願いします。

<span class="a--interview-speaker"><img src="/assets/images/interview/ryoichi-saito.png" alt=""><strong>齋藤：</strong></span> まずは、ものづくりを最大限楽しんでほしいです。自分が何をつくりたいのかを考えて、ぜひつくってみてください。

それから、もう一歩進んで、自分だけが欲しいものではなくて、ほかの人も欲しがるようなものをつくってみると、ものづくりの楽しさがまた変わると思います。

作ったものを誰かに見せてみる。その人の反応を見て、また改良してみる。あるいは次につくるものを変えてみる。そういう「つくって、見せて、またつくる」というサイクルの楽しさも、ぜひ感じてもらいたいですね。

みなさんの作品を見ることを、とても楽しみにしています。

AIがプログラムを書く時代になっても、「何をつくるのか」「誰のどんな困りごとを解決するのか」を考えることは残り続けそうです。

そして、思いつくだけでなく、実際に形にし、最後までつくり切り、人に見せて反応をもらう。

齋藤さんの話を聞いていると、それはまさにRubyプログラミングコンテストで経験できることなのだと感じます。

今年はどんな「つくりたかったもの」が形になって登場するのでしょうか。

私たちも楽しみにしています。
