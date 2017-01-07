# -*- coding: utf-8 -*-
import MySQLdb
import MeCab
import numpy as np
import re
from sklearn.feature_extraction.text import TfidfVectorizer

### MySQL 上の Tweet データ取得用関数
def fetch_target_day_n_random_tweets(target_day, n = 2000):
    with MySQLdb.connect(
            host="localhost",
            user="root",
            passwd="shun0509",
            db="textdata",
            charset="utf8") as cursor:
        SQL = u"""
        SELECT
          distinct text
        FROM
          tweet
        WHERE
          DATE(created_at + INTERVAL 9 HOUR) = '%s'
        LIMIT %s;
        """ %(target_day, unicode(n))

        print(SQL)
        cursor.execute(SQL)
        result = cursor.fetchall()
        l = [x[0] for x in result]
        return l

### MeCab による単語への分割関数 (名詞のみ残す)
def split_text_only_noun(text):

    tagger = MeCab.Tagger()
    text_str = text.encode('utf-8') # str 型じゃないと動作がおかしくなるので変換

    p = re.compile(r"https?://[\w/:%#\$&\?\(\)~\.=\+\-]+")
    if p.search(text_str):
        print("url is finded.")
        return ''

    node = tagger.parseToNode(text_str)

    words = []
    while node:
        pos = node.feature.split(",")[0]

        if pos == "名詞":
            # unicode 型に戻す
            word = node.surface.decode("utf-8")
            if word != 'https':
                words.append(word)
        node = node.next
    return " ".join(words)

### TF-IDF の結果からi 番目のドキュメントの特徴的な上位 n 語を取り出す
def extract_feature_words(terms, tfidfs, i, n):
    tfidf_array = tfidfs[i]
    top_n_idx = tfidf_array.argsort()[-n:][::-1]
    words = [terms[idx] for idx in top_n_idx]
    return words


# 2記事の一部だけ取り出しました
# 1つめがITライフハック、2つめが独女通信の記事です。
if __name__ == '__main__':

    ### メイン処理
    docs_count = 2000 # 取得 Tweet 数
    target_days = [
        "2017-01-04",
        "2017-01-05",
        "2017-01-06",
        "2017-01-07",
    ]

    target_day_nouns = []
    for target_day in target_days:
        print target_day
        # MySQL からのデータ取得
        txts = fetch_target_day_n_random_tweets(target_day, docs_count)
        # 名詞のみ抽出
        each_nouns = [split_text_only_noun(txt) for txt in txts]
        all_nouns = " ".join(each_nouns)
        target_day_nouns.append(all_nouns)

    # TF-IDF 計算
    # (合計6日以上出現した単語は除外)
    tfidf_vectorizer = TfidfVectorizer(
        use_idf=True,
        lowercase=False,
        max_df=6
    )
    tfidf_matrix = tfidf_vectorizer.fit_transform(target_day_nouns)

    # index 順の単語のリスト
    terms = tfidf_vectorizer.get_feature_names()
    # TF-IDF 行列 (numpy の ndarray 形式)
    tfidfs = tfidf_matrix.toarray()

    # 結果の出力
    for i in range(0, len(target_days)):
        print "\n------------------------------------------"
        print target_days[i]
        for x in  extract_feature_words(terms, tfidfs, i, 10):
            print x,
