# -*- coding: utf-8 -*-
import os # osモジュールのインポート
import MeCab
import re
from gensim import corpora
mecab = MeCab.Tagger('mecabrc')
aryWord = []
aryGroup = []
lineNum = 1

def readFile():
    global aryWord
    global aryGroup
    global lineNum
    files = os.listdir('./dictionaryData')
    aryWord = []
    for file in files:
        aryGroup = []
        get_words(file)

    make_dic(aryWord)

def tokenize(text):
    '''
    とりあえず形態素解析して名詞だけ取り出す感じにしてる
    '''
    node = mecab.parseToNode(text)
    while node:
        pos0 = node.feature.split(",")[0]
        pos1 = node.feature.split(",")[1]

        if pos0 == "名詞" and pos1 == "一般":
            yield node.surface.lower()
        node = node.next


def get_words(strFile):
    '''
    記事群のdictについて、形態素解析してリストにして返す
    '''
    lineNum = 1
    p = re.compile(r"https?://[\w/:%#\$&\?\(\)~\.=\+\-]+")

    for line in open('./dictionaryData/'+strFile, 'r'):

        # print(p.match(line))
        if lineNum != 1 and lineNum != 2 and p.search(line) is None:
            # print(line)
            get_words_main(line)
        lineNum+=1
        # aryWord.append(get_words_main(line))
    aryWord.append(aryGroup)


def get_words_main(content):
    '''
    一つの記事を形態素解析して返す
    '''
    for token in tokenize(content):
        aryGroup.append(token)


# 辞書を作成する
def make_dic(words):
    dictionary = corpora.Dictionary(words)
    print(str(dictionary.token2id).decode('string-escape'))
    print('--------------------------------')
    print(str(dictionary).decode('string-escape'))
    dictionary.save_as_text('livedor_dokujo.txt')


# 2記事の一部だけ取り出しました
# 1つめがITライフハック、2つめが独女通信の記事です。
if __name__ == '__main__':
    readFile()
