# -*- coding: utf-8 -*-
import os # osモジュールのインポート
import MeCab
import re, pprint
from gensim import corpora
from sklearn.feature_extraction.text import TfidfVectorizer
mecab = MeCab.Tagger('mecabrc')
aryWord = []
aryGroup = []
lineNum = 1

def pp(obj):
  pp = pprint.PrettyPrinter(indent=4, width=160)
  str = pp.pformat(obj)
  return re.sub(r"\\u([0-9a-f]{4})", lambda x: unichr(int("0x"+x.group(1), 16)), str)


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

    all_nouns = " ".join(aryGroup)
    aryWord.append(all_nouns)


def get_words_main(content):
    '''
    一つの記事を形態素解析して返す
    '''
    for token in tokenize(content):
        aryGroup.append(token)


# 辞書を作成する
def make_dic(words):
    # dictionary = corpora.Dictionary(words)
    # print(str(dictionary.token2id).decode('string-escape'))
    # print('--------------------------------')
    # print(str(dictionary).decode('string-escape'))
    # dictionary.save_as_text('livedor_dokujo.txt')
    print(pp(words))
    # print str(words).decode('string-escape')
    # TF-IDF 計算
    # (合計6日以上出現した単語は除外)
    tfidf_vectorizer = TfidfVectorizer(
        use_idf=True,
        lowercase=False,
        max_df=6
    )
    tfidf_matrix = tfidf_vectorizer.fit_transform(words)

    # index 順の単語のリスト
    terms = tfidf_vectorizer.get_feature_names()
    # TF-IDF 行列 (numpy の ndarray 形式)
    tfidfs = tfidf_matrix.toarray()

    for x in  extract_feature_words(terms, tfidfs, 0, 20):
        print x

    print("----------------------------")

    for x in  extract_feature_words(terms, tfidfs, 1, 20):
        print x

### TF-IDF の結果からi 番目のドキュメントの特徴的な上位 n 語を取り出す
def extract_feature_words(terms, tfidfs, i, n):
    tfidf_array = tfidfs[i]
    top_n_idx = tfidf_array.argsort()[-n:][::-1]
    words = [terms[idx] for idx in top_n_idx]
    return words


# 2記事の一部だけ取り出しました
# 1つめがITライフハック、2つめが独女通信の記事です。
if __name__ == '__main__':
    readFile()
