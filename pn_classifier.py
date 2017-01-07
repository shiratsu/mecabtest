#!/usr/bin/env python
#-*- coding:utf-8 -*-

### 使用するライブラリ
import MySQLdb
import pandas.io.sql as psql
import pandas as pd
import numpy as np
import MeCab
from sklearn import svm
from sklearn.grid_search import GridSearchCV
from sklearn.feature_extraction.text import CountVectorizer

if __name__ == '__main__':
    print "[INFO] ドキュメント取得"
tweets = psql.read_sql(
    "SELECT  text, label FROM pn_tweet",
    MySQLdb.connect(
        host    = "localhost",
        user    = "root",
        passwd  = "shun0509",
        db      = "textdata",
        charset = 'utf8'
        )
    )

def wakati(text):
    tagger = MeCab.Tagger()
    text = text.encode("utf-8")
    node = tagger.parseToNode(text)
    word_list = []
    while node:
        pos0 = node.feature.split(",")[0]
        pos1 = node.feature.split(",")[1]
        if pos0 == "名詞" and pos1 != "一般":
            continue
        if pos in ["名詞", "動詞", "形容詞"]:
            lemma = node.feature.split(",")[6].decode("utf-8")
            if lemma == u"*":
                lemma = node.surface.decode("utf-8")
            word_list.append(lemma)
        node = node.next
    return u" ".join(word_list[1:-1])
