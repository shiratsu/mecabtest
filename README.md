# mecabtest
mecabの実験

## 今回やってみてること
```
1. 記事からMeCabで単語だけ切り出して記事を単語リストに変換
2. 単語リスト群から、Gensimで特徴語の辞書を定義
3. BoWの要領で各文章に特徴語が何個あるかカウントして特徴ベクトル作る
4. この特徴ベクトルで学習。
5. 未知の文章も、3の方法で特徴ベクトルを作れば、分類器にかけてカテゴリを当てられるはず
```

## 辞書のフォーマット
例
```
id[TAB]word_utf8[TAB]document frequency[NEWLINE]
```

```
46	etc	1
29	からだ	1
42	くみ	1
43	こと	1
21	の	2
3	ひとこと	1
44	わる	1
11	アナタ	1
25	イヤ	1
26	エロ	1
17	オススメ	1
34	クール	1
22	サイト	1
9	サーフィン	1
14	スタート	1
39	チャラ	1
19	ネット	1
```

##  教師あり学習の種類
* 回帰モデル
* 分類モデル

### 回帰モデル
与えられたデータから、予測する
住宅の価格を予想したりとか

### 分類モデル
データをカテゴリに分類する
このデータはAに分類するかBに分類するか

## 教師なし学習モデル
データセットに対して、どういったものかがわからない
教師なしアルゴリズムではデータを２つ以上にカテゴライズしたりする
これをクラスタリングと言います

１例はGoogle News。
１ニュースに複数のリンクがある
それは、Aという内容のニュースにクラスタリングされている
同じ話題の記事をクラスタリングしている
