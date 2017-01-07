# -*- coding: utf-8 -*-

# tf値算出メソッド定義
def tf(terms, document):

    for term in terms:
        print(term)
        print(document)

    tf_values = [document.count(term) for term in terms]
    print(tf_values)
    print('---------------------------------------------')
    print(list(map(lambda x: x/sum(tf_values), tf_values)))
    return list(map(lambda x: x/sum(tf_values), tf_values))

# idf値算出メソッド定義
def idf(terms, documents):
    import math
    print('------------------++++++++++++---------------------------')
    print([math.log10(len(documents)/sum([bool(term in document) for document in documents])) for term in terms])
    return [math.log10(len(documents)/sum([bool(term in document) for document in documents])) for term in terms]

# tf-idf値算出メソッド定義
def tf_idf(terms, documents):
    return [[_tf*_idf for _tf, _idf in zip(tf(terms, document), idf(terms, documents))] for document in documents]


if __name__ == '__main__':

    # terms = ['apple','banana','test']
    # documents = ['apple,apple', 'apple,banana', 'banana,test']
    # print(tf_idf(terms, documents))
    #
    # terms = ['リンゴ', 'ゴリラ', 'ラッパ']
    # documents = ['リンゴ、リンゴ', 'リンゴとゴリラ', 'ゴリラとラッパ']
    # print(tf_idf(terms, documents))
    #
    #
    #
    #
    # terms = ["GDP", "景気対策", "失業率"]
    #
    # documents = ["政府は、GDPの数値目標を明示して掲げています。その政府ですが、年明け最初の経済財政諮問会議で、景気対策と失業率についての追加の総合経済対策について、民間議員から意見を聞いた模様です。GDP数値目標についても、突っ込んだ意見が出たのかどうかに注目が集まっています。"
    #         , "FRB（米連邦準備制度理事会）は、伝統的な物価上昇率と並び、米国の国内失業率の水準を、金融政策の舵取りを行う上で、主要な参考数値に位置付けている。"
    #         , "失業率、失業率、失業率"
    #         , "景気対策、景気対策"]
    #
    # result = tf_idf(terms, documents)
    # print(result)
