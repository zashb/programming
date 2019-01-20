import numpy as np
import pandas as pd

from word2vec.author_identification import Trainer
from word2vec.author_identification import DatasetBuilder


def main():
    print("Running author identification")
    train_csv = "/Users/bhargavayyagari/PyNLP/resources/author_identification_train.csv"
    test_csv = "/Users/bhargavayyagari/PyNLP/resources/author_identification_test.csv"
    label_encoder, train_data, w2vmodel = DatasetBuilder.train_data_builder(train_csv)
    model = Trainer.train_classifier_and_print_scores(train_data)
    test_data = DatasetBuilder.test_data_builder(test_csv, w2vmodel)
    predictions, predictions_probabilities = get_predictions(model, test_data, label_encoder)
    write_results_to_file(predictions, predictions_probabilities, test_data)


def write_results_to_file(predictions, predictions_probabilities, test_data):
    print("Writing results to file")
    result = np.append(test_data.id.values.reshape(-1, 1), predictions_probabilities, axis=1)
    result_df = pd.DataFrame(data=result, columns=['id', 'EAP', 'HPL', 'MWS'])
    result_df["Prediction"] = predictions
    result_df.to_csv('/Users/bhargavayyagari/PyNLP/resources/author_identification_submission.csv', index=False)


def get_predictions(model, test_data, label_encoder):
    print("Getting predictions and predictions_probabilities")
    X_test_w2v = np.array(list(map(np.array, test_data.w2v_features)))
    predictions_probabilities = model.predict_proba(X_test_w2v)
    predictions = model.predict(X_test_w2v)
    predictions_decoded = label_encoder.inverse_transform(predictions)
    return [predictions_decoded, predictions_probabilities]


def print_docs_len(train_data):
    print("Printing doc lengths")
    document_lengths = np.array(list(map(len, train_data["text"].str.split(' '))))
    print("The average number of words in a document is: {}.".format(np.mean(document_lengths)))
    print("The minimum number of words in a document is: {}.".format(min(document_lengths)))
    print("The maximum number of words in a document is: {}.".format(max(document_lengths)))


if __name__ == '__main__':
    main()
