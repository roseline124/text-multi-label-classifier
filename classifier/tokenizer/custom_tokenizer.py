import warnings

from ckonlpy.tag import Postprocessor, Twitter
from ckonlpy.utils import load_ngram, load_wordset, load_replace_wordpair
from os import path

dictionary = load_wordset(path.abspath(
    './classifier/tokenizer/dictionary.txt'))
alpha_dictionary = load_wordset(path.abspath(
    './classifier/tokenizer/alpha_dictionary.txt'))
stopwords = load_wordset(path.abspath('./classifier/tokenizer/stopwords.txt'))
replace = load_replace_wordpair(path.abspath(
    './classifier/tokenizer/replacewords.txt'))
ngrams = load_ngram(path.abspath('./classifier/tokenizer/ngrams.txt'))

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    twitter = Twitter()  # Twitter -> Okt

twitter.add_dictionary(list(dictionary), 'Noun')
twitter.add_dictionary(list(alpha_dictionary), 'Alpha')

postprocessor = Postprocessor(
    base_tagger=twitter,  # base tagger
    replace=replace,  # 치환
    stopwords=stopwords,  # 필터
    ngrams=ngrams  # 복합 단어 set
)

# 한글 토크나이저


def tokenizer(raw, pos=["Noun", "Alpha", "Adverb"], stopword=stopwords):  # 명사, 알파벳, 형용사 품사만 선택
    # (word, tag) => ('코딩', 'Noun')
    # pos에 포함된 tag이고, word가 1개 이상이라면 word 반환
    return [
        word for word, tag in postprocessor.pos(raw)
        if len(word) > 1 and tag in pos
    ]
