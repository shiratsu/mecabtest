# -*- coding: utf-8 -*-
import os # osモジュールのインポート
import MeCab
from gensim import corpora

def bowTest():
    # さっきITライフハックの1記事を形態素解析かけて名詞取り出したやつ
    words = ['アナタ', 'ブラウザ', 'ブック', 'マーク', 'ブック', 'マーク', '管理', 'ライフ', 'リスト', 'オススメ', '最近', 'ネット', 'サーフィン', '際', '利用', 'の', 'ライフ', 'リスト', 'サイト', 'ライフ', 'リスト', 'ひとこと', '自分', '専用', 'ブックマークサイト', 'ブラウザ', 'スタート', 'ページ', 'ブラウザ', 'ブック', 'マーク', '管理', '不要', '便利', 'サイト', 'の']

    # BoW
    dictionary = corpora.Dictionary.load_from_text('livedor_dokujo.txt')
    vec = dictionary.doc2bow(words)
    print(vec)


# 2記事の一部だけ取り出しました
# 1つめがITライフハック、2つめが独女通信の記事です。
if __name__ == '__main__':
    bowTest()
