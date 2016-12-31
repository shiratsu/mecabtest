# -*- coding: utf-8 -*-
import os # osモジュールのインポート
import MeCab
from gensim import corpora
mecab = MeCab.Tagger('mecabrc')
aryWord = []

def bowTest():
    global aryWord
    files = os.listdir('./bowtestfolder')
    aryWord = []
    for file in files:
        get_words(file)

    print(str(aryWord).decode('string-escape'))
    # BoW
    dictionary = corpora.Dictionary.load_from_text('livedor_dokujo.txt')
    vec = dictionary.doc2bow(aryWord)
    print(vec)

def tokenize(text):
    '''
    とりあえず形態素解析して名詞だけ取り出す感じにしてる
    '''
    node = mecab.parseToNode(text)
    while node:
        if node.feature.split(',')[0] == '名詞':
            yield node.surface.lower()
        node = node.next


def get_words(strFile):
    '''
    記事群のdictについて、形態素解析してリストにして返す
    '''
    for line in open('./bowtestfolder/'+strFile, 'r'):
        get_words_main(line)
        # aryWord.append(get_words_main(line))


def get_words_main(content):
    '''
    一つの記事を形態素解析して返す
    '''
    for token in tokenize(content):
        aryWord.append(token)



# 2記事の一部だけ取り出しました
# 1つめがITライフハック、2つめが独女通信の記事です。
if __name__ == '__main__':
    bowTest()
