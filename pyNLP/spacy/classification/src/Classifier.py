import pandas as pd
import glob
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
import string
from spacy.lang.en import English
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from sklearn.metrics import accuracy_score 
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


class Classifier(object):
    def __init__(self):
        self.nlp = spacy.load('en')
        self.stopwords = list(STOP_WORDS)
        self.punctuations = string.punctuation
        self.parser = English()


    def get_data(self, filename):
        df = pd.read_table(filename)
        return df


    def get_df(self, dir_data):
        list_filenames = glob.glob(dir_data + "/*.txt")
        list_df = []
        for filename in list_filenames:
            if "readme" not in filename:
                df = self.get_data(filename)
                df.columns = ["Message","Target"]
                list_df.append(df)
        keys = ['Yelp', 'IMDB', 'Amazon']
        df = pd.concat(list_df, keys=keys)
        return df


    def spacy_tokenizer(self, sentence):
        mytokens = self.parser(sentence)
        mytokens = [ word.lemma_.lower().strip() if word.lemma_ != "-PRON-" else word.lower_ for word in mytokens ]
        mytokens = [ word for word in mytokens if word not in self.stopwords and word not in self.punctuations ]
        return mytokens


    def fit_and_predict_using_pipeline(self, df, predictor):
        vectorizer = CountVectorizer(tokenizer = self.spacy_tokenizer, ngram_range=(1,1)) 
        # classifier = LinearSVC()
        classifier = LogisticRegression()
        tfvectorizer = TfidfVectorizer(tokenizer=self.spacy_tokenizer)
        X_train, X_test, y_train, y_test = train_test_split(df['Message'], df['Target'], test_size=0.2, random_state=42)
        pipe = Pipeline([("cleaner", predictor), ('vectorizer', vectorizer), ('classifier', classifier)])
        pipe.fit(X_train, y_train)
        sample_prediction = pipe.predict(X_test)
        print("Accuracy test: ",pipe.score(X_test,y_test))
        print("Accuracy sample: ", pipe.score(X_test, sample_prediction))
        print("Accuracy train: ", pipe.score(X_train, y_train))
        return