# -*- coding: utf-8 -*-
import os # osモジュールのインポート
import MeCab
import re
from gensim import corpora,matutils
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

        dense = list(matutils.corpus2dense([vec], num_terms=len(dictionary)).T[0])
        print(dense)



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

    '''
    記事群のdictについて、形態素解析してリストにして返す
    '''
    lineNum = 1
    p = re.compile(r"https?://[\w/:%#\$&\?\(\)~\.=\+\-]+")

    for line in open('./bowtestfolder/'+strFile, 'r'):
        # print(p.match(line))
        if lineNum != 1 and lineNum != 2 and p.search(line) is None:
            # print(line)
            get_words_main(line)
        lineNum+=1
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
