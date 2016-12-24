# -*- coding: utf-8 -*-
import MeCab
from gensim import corpora
mecab = MeCab.Tagger('mecabrc')


def tokenize(text):
    '''
    とりあえず形態素解析して名詞だけ取り出す感じにしてる
    '''
    node = mecab.parseToNode(text)
    while node:
        if node.feature.split(',')[0] == '名詞':
            yield node.surface.lower()
        node = node.next


def get_words(contents):
    '''
    記事群のdictについて、形態素解析してリストにして返す
    '''
    ret = []
    for k, content in contents.items():
        ret.append(get_words_main(content))
    return ret


def get_words_main(content):
    '''
    一つの記事を形態素解析して返す
    '''
    return [token for token in tokenize(content)]

# 辞書を作成する
def make_dic(words):
    dictionary = corpora.Dictionary(words)
    print(str(dictionary.token2id).decode('string-escape'))
    print(str(dictionary).decode('string-escape'))
    dictionary.save_as_text('livedoordic.txt')


# 2記事の一部だけ取り出しました
# 1つめがITライフハック、2つめが独女通信の記事です。
if __name__ == '__main__':
    words = get_words({'it-life-hack-001.txt': 'アナタはまだブラウザのブックマーク？　ブックマーク管理はライフリストがオススメ 最近ネットサーフィンをする際にもっぱら利用しているのが「ライフリスト」というサイトだ。この「ライフリスト」は、ひとことで言うと自分専用のブックマークサイトである。というよりブラウザのスタートページにするとブラウザのブックマーク管理が不要になる便利なサイトなのである。', 'dokujo-tsushin-001.txt': 'たとえば、馴れ馴れしく近づいてくるチャラ男、クールを装って迫ってくるエロエロ既婚男性etc…に対し「下心、見え見え〜」と思ったことはないだろうか？ “下心”と一言で言うと、特に男性が女性のからだを目的に執拗に口説くなど、イヤらしい言葉に聞こえてしまう。実際、辞書で「下心」の意味を調べてみると、心の底で考えていること。かねて心に期すること、かねてのたくらみ。特に、わるだくみ。（広辞苑より）という意味があるのだから仕方がないのかもしれない。'})
    print(str(words).decode('string-escape'))
    print(type(str(words).decode('string-escape')))
    make_dic(words)
    # print(words[0][0].decode('utf-8'))
    # for aryVal in words:
    #     for val in aryVal:
    #         print(val.decode('utf-8'))
