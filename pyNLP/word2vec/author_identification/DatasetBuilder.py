import pandas as pd

from word2vec.author_identification import Preprocessor
from word2vec.author_identification.Runner import print_docs_len


def test_data_builder(test_csv, w2vmodel):
    print("Building test data")
    test_data = pd.read_csv(test_csv)
    Preprocessor.preprocess_test_data(test_data, w2vmodel)
    return test_data


def train_data_builder(train_csv):
    print("Building train data")
    train_data = pd.read_csv(train_csv)
    print_docs_len(train_data)
    Preprocessor.w2v_preprocessing(train_data)
    Preprocessor.lda_get_good_tokens(train_data)
    Preprocessor.remove_stopwords(train_data)
    Preprocessor.stem_words(train_data)
    Preprocessor.document_to_bow(train_data)
    w2vmodel = Preprocessor.get_w2v_model(train_data)
    Preprocessor.add_w2v_features_to_train_data(train_data, w2vmodel)
    label_encoder = Preprocessor.encode_author(train_data)
    return label_encoder, train_data, w2vmodel