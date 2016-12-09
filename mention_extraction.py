import nltk


def get_index():
    with open('fstemp') as f:
        text = f.read()
    return set(text.split('\n'))

def get_ngrams(text):
    ng = set()
    for f in [nltk.unigrams, nltk.bigrams, nltk.trigrams]:
        ng.union(set(f(text)))
    return ng


def find_all_occurences():
    index = get_index()
    import ipdb; ipdb.set_trace()
    with open('test.txt') as f:
        text = f.read()

    ngrams = get_ngrams(text)




if __name__ == '__main__':
    find_all_occurences()
