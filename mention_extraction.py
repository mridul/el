from nltk.util import ngrams
from nltk import word_tokenize

import string

import unicodedata
import sys


def remove_punctuation(text):
    tbl = dict.fromkeys(i for i in range(sys.maxunicode)
                    if unicodedata.category(chr(i)).startswith('P'))
    return text.translate(tbl)


def get_index():
    with open('fstemp') as f:
        text = f.read()
    return set(text.split('\n'))

def get_ngrams(text):
    tokens = word_tokenize(text)
    bigrams = ngrams(tokens, 2)
    trigrams = ngrams(tokens, 3)
    ng = []
    ng.extend(tokens)
    for n in (2, 3):
        ng.extend([' '.join(t) for t in ngrams(tokens, n)])

    return ng


def _search_in_index(tokens, index):
    results = set()
    for t in tokens:
        if t in index:
            results.add(t)

    return results


def find_all_occurences():
    index = get_index()

    with open('test.txt') as f:
        text = f.read()

    text.replace('\n', ' \n ')
    text = text.lower()
    text = remove_punctuation(text)
    tokens = get_ngrams(text)
    matches = _search_in_index(tokens, index)

    print('matches: ', matches)



if __name__ == '__main__':
    find_all_occurences()
