import logging

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import LinearSVC


def main():
    data_file = "/Users/bhargavayyagari/github/pyNLP/resources/corpus.txt"
    labels, texts = read_file(data_file)
    trainDF, trainDF_gby = build_df(labels, texts)
    logging.info("Distribution info : \n{}".format(trainDF_gby.head()))
    encode_labels(trainDF)
    pipeline_list = build_pipelines()
    get_cvs(pipeline_list, trainDF)


def get_cvs(pipeline_list, trainDF):
    for pipeline in pipeline_list:
        logging.info("Pipeline : {}".format(pipeline))
        estimator = Pipeline(steps=pipeline)
        logging.info("Cross validating")
        cv = StratifiedKFold(n_splits=5, random_state=1)
        cvs = cross_val_score(estimator=estimator, X=trainDF["text"].values, y=trainDF["labels_encoded"].values, cv=cv)
        logging.info("Scores : {}".format(cvs))


def build_pipelines():
    logging.info("Building pipeline")
    pipeline_list = [[('vect', CountVectorizer()), ("clf", LinearSVC())],
                     [('vect', TfidfVectorizer()), ("clf", LinearSVC())]]
    return pipeline_list


def encode_labels(trainDF):
    logging.info("Encoding labels")
    encoder = LabelEncoder()
    trainDF["labels_encoded"] = encoder.fit_transform(trainDF["labels"])


def build_df(labels, texts):
    logging.info("Building dataframe")
    trainDF = pd.DataFrame()
    trainDF["text"], trainDF["labels"] = texts, labels
    trainDF_gby = trainDF.groupby(by=["labels"], as_index=False).count()
    return trainDF, trainDF_gby


def read_file(data_file):
    # open a random text file
    logging.info("Reading from file : {}".format(data_file))
    data = open(data_file).read()
    labels, texts = [], []
    for line in data.split("\n"):
        content = line.split()
        labels.append(content[0])
        texts.append(" ".join(content[1:]))
    return labels, texts


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    main()
