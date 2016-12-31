# -*- coding: utf-8 -*-
import os # osモジュールのインポート
import MeCab,re
from math import log

mecab = MeCab.Tagger('mecabrc')
aryWord = []

def readFile():
    global aryWord
    files = os.listdir('./dictionaryData')
    aryWord = []
    for file in files:
        get_words(file)

def tokenize(text):
    '''
    とりあえず形態素解析して名詞だけ取り出す感じにしてる
    '''
    node = mecab.parseToNode(text)
    while node:
      if node.feature.split(",")[0] == "名詞":
         replace_node = re.sub( re.compile( "[!-/:-@[-`{-~]" ), "", node.surface )
         if replace_node != "" and replace_node != " ":
            aryWord.append( replace_node )
      node = node.next

def get_words(strFile):
    '''
    記事群のdictについて、形態素解析してリストにして返す
    '''
    for line in open('./dictionaryData/'+strFile, 'r'):
        get_words_main(line)
        # aryWord.append(get_words_main(line))

def get_words_main(content):
    '''
    一つの記事を形態素解析して返す
    '''
    tokenize(content)

def getTopKeywords(TF,n):
   list = sorted( TF.items(), key=lambda x:x[1], reverse=True )
   return list[0:n]

def calcTFIDF( N,TF, DF ):
   tfidf = TF * log( N / DF )
   return tfidf

if __name__ == '__main__':

    tf = {}
    df = {}

    readFile()

    for word in aryWord:
         try:
            tf[word] = tf[word] + 1
         except KeyError:
            tf[word] = 1
    for word in aryWord:
         try:
            if word in df_list:
               continue
            df[word] = df[word] + 1
         except KeyError:
            df[word] = 1
   tfidf = {}
   for k,v in getTopKeywords( tf, 100 ):
      tfidf[k] = calcTFIDF(N,tf[k],df[k])
   for k,v in getTopKeywords( tfidf, 100):
      print k,v
