import Classifier
import Predictor
import glob


def main():
    runner = Classifier.Classifier()
    predictor = Predictor.Predictor()
    dir_data = "/Users/bhargavayyagari/PyNLP/spacy/classification/data"
    df = runner.get_df(dir_data)
    print(df.shape)
    runner.fit_and_predict_using_pipeline(df, predictor)


if __name__ == '__main__':
    main()