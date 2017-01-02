# -*- coding: utf-8 -*-
from gensim.models import Phrases
import os # osモジュールのインポート
import MeCab
mecab = MeCab.Tagger('mecabrc')
aryWord = []
aryLine = []

def readFile():
    global aryWord
    global aryLine
    for line in open('sample.txt', 'r'):
        aryLine = []
        get_words_main(line)
        aryWord.append(aryLine)

    print(aryWord)
    print(str(aryWord).decode('string-escape'))


def tokenize(text):
    '''
    とりあえず形態素解析して名詞だけ取り出す感じにしてる
    '''
    node = mecab.parseToNode(text)
    while node:
        if node.feature.split(',')[0] == '名詞':
            yield node.surface.lower()
        node = node.next

def get_words_main(content):
    '''
    一つの記事を形態素解析して返す
    '''
    for token in tokenize(content):
        aryLine.append(token)

# 解析を行う
def analyze():

    print('---------------------------------------')

    # 学習
    phrases_bi = Phrases(aryWord, min_count=5, threshold=10.0)

    # 変換
    transformed_bi = phrases_bi[aryWord]

    for words in transformed_bi:
        for w in words:
            print w,
        print ''

    print('---------------------------------------')

    # 学習
    phrases_tri = Phrases(transformed_bi, min_count=5, threshold=3.0)

    # 変換
    transformed_tri = phrases_tri[transformed_bi]

    for words in transformed_tri:
        for w in words:
            print w,
        print ''

    print('---------------------------------------')

    for k,v in phrases_tri.vocab.items():
        if k.find('_') > 0 and v >= 1:
            print k, v

    print('---------------------------------------')

# 2記事の一部だけ取り出しました
# 1つめがITライフハック、2つめが独女通信の記事です。
if __name__ == '__main__':
    readFile()

    # 解析
    analyze()
