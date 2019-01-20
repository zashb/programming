import re

import nltk
import numpy as np
from gensim.corpora import Dictionary
from gensim.models import Word2Vec
from sklearn.preprocessing import LabelEncoder


def lda_get_good_tokens(df):
    print("Getting good tokens")
    df['text'] = df.text.str.lower()
    df['tokenized_text'] = list(map(nltk.word_tokenize, df.text))
    df['tokenized_text'] = list(map(get_good_tokens, df.tokenized_text))


def add_w2v_features_to_train_data(df, w2vmodel):
    print("Adding W2V features to train data")
    df['w2v_features'] = list(map(lambda sen_group:
                                  get_w2v_features(w2vmodel, sen_group),
                                  df.tokenized_sentences))


def get_w2v_features(w2v_model, sentence_group):
    words = np.concatenate(sentence_group)
    index2word_set = set(w2v_model.wv.vocab.keys())
    featureVec = np.zeros(w2v_model.vector_size, dtype="float32")
    nwords = 0
    for word in words:
        if word in index2word_set:
            featureVec = np.add(featureVec, w2v_model[word])
            nwords += 1.
    if nwords > 0:
        featureVec = np.divide(featureVec, nwords)
    return featureVec


def get_w2v_model(df):
    print("Creating W2V model")
    sentences = []
    for sentence_group in df.tokenized_sentences:
        sentences.extend(sentence_group)
    num_features = 200
    min_word_count = 3
    num_workers = 4
    context = 6
    downsampling = 1e-3
    w2vmodel = Word2Vec(sentences=sentences,
                        sg=1,
                        hs=0,
                        workers=num_workers,
                        size=num_features,
                        min_count=min_word_count,
                        window=context,
                        sample=downsampling,
                        negative=5,
                        iter=6)
    return w2vmodel


def document_to_bow(df):
    print("Doc to BOW")
    dictionary = Dictionary(documents=df.stemmed_text.values)
    print("Found {} words.".format(len(dictionary.values())))
    dictionary.filter_extremes(no_above=0.8, no_below=3)
    dictionary.compactify()
    print("Left with {} words.".format(len(dictionary.values())))
    df['bow'] = list(map(lambda doc: dictionary.doc2bow(doc), df.stemmed_text))


def stem_words(df):
    print("Stemming words")
    lemm = nltk.stem.WordNetLemmatizer()
    df['lemmatized_text'] = list(map(lambda sentence:
                                     list(map(lemm.lemmatize, sentence)),
                                     df.stopwords_removed))

    p_stemmer = nltk.stem.porter.PorterStemmer()
    df['stemmed_text'] = list(map(lambda sentence:
                                  list(map(p_stemmer.stem, sentence)),
                                  df.lemmatized_text))


def remove_stopwords(df):
    print("Removing stopwords")
    stopwords = nltk.corpus.stopwords.words('english')
    our_special_word = 'qwerty'
    stopwords.append(our_special_word)
    df['stopwords_removed'] = list(map(lambda doc:
                                       [word for word in doc if word not in stopwords],
                                       df['tokenized_text']))


def w2v_preprocessing(df):
    print("Preprocessing for W2v")
    df['text'] = df.text.str.lower()
    df['document_sentences'] = df.text.str.split('.')
    df['tokenized_sentences'] = list(map(lambda sentences: list(nltk.word_tokenize(sentences)), df.document_sentences))
    df['tokenized_sentences'] = list(map(lambda sentences: list(get_good_tokens(sentences)), df.tokenized_sentences))
    df['tokenized_sentences'] = list(map(lambda sentences:
                                         list(filter(lambda lst: lst, sentences)),
                                         df.tokenized_sentences))


def get_good_tokens(sentence):
    replaced_punctation = list(map(lambda token: re.sub('[^0-9A-Za-z!?]+', '', token), sentence))
    removed_punctation = list(filter(lambda token: token, replaced_punctation))
    return removed_punctation


def encode_author(df):
    print("Encoding Label")
    label_encoder = LabelEncoder()
    label_encoder.fit(df.author)
    df['author_id'] = label_encoder.transform(df.author)
    return label_encoder


def preprocess_test_data(test_data, w2vmodel):
    print("Preprocessing test data")
    w2v_preprocessing(test_data)
    test_data['w2v_features'] = list(map(lambda sen_group:
                                         get_w2v_features(w2vmodel, sen_group),
                                         test_data.tokenized_sentences))
