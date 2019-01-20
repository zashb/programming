from gensim.models import Word2Vec


def test_method0():
    sentences = [['this', 'is', 'the', 'first', 'sentence', 'for', 'word2vec'],
                 ['this', 'is', 'the', 'second', 'sentence'],
                 ['yet', 'another', 'sentence'],
                 ['one', 'more', 'sentence'],
                 ['and', 'the', 'final', 'sentence']]
    model = Word2Vec(sentences, min_count=1, size=300, window=3, sg=0)
    print(" words : {} ".format(list(model.wv.vocab)))
    # print("wv for {} : {} ".format("sentence", model['sentence']))
    model.save('/Users/bhargavayyagari/PyNLP/word2vec/model.bin')
    new_model = Word2Vec.load('/Users/bhargavayyagari/PyNLP/word2vec/model.bin')


if __name__ == "__main__":
    test_method0()
