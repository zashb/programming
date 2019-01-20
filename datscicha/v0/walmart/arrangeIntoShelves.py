import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from plotly.offline import plot, iplot

from ast import literal_eval
from sklearn.preprocessing import MultiLabelBinarizer, LabelEncoder
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
import re
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer, HashingVectorizer


# nltk.download()


class Solution:
    def __init__(self):
        self.trainDF = pd.DataFrame()
        self.testDF = pd.DataFrame()

    def loadData(self, filenames):
        filedir = r"C:\Users\sg0222350\My Stuff\learn\read\Collection_Data_Science_TakeHome_Challenges\walmart\data\\"
        trainFile, testFile = filedir + filenames[0], filedir + filenames[1]
        self.trainDF, self.testDF = pd.read_csv(trainFile, sep="\t"), pd.read_csv(testFile, sep="\t")

    def describeDF(self, df):
        print("HEAD : \n", df.head())
        print("SHAPE : \n", df.shape)

    def prepDF(self, df):
        # handle lists in Y column
        # print(df["tag"][:5])
        # rem this step
        df["tag"] = df["tag"].apply(literal_eval)
        mlb = MultiLabelBinarizer()
        Ytrain = mlb.fit_transform(df["tag"])
        # print(Ytrain)
        # gives all the unique shelves
        # print(mlb.classes_)
        # concat train test
        train_test = pd.concat([df.drop("tag", axis=1), self.testDF])
        # get product specific columns
        train_test['ISBN'] = train_test['ISBN'].fillna(0)
        train_test.loc[train_test['ISBN'] > 0, 'ISBN'] = 1
        train_test.loc[train_test['Publisher'].notnull(), 'Publisher'] = 1
        train_test['Publisher'] = train_test['Publisher'].fillna(0)
        train_test.loc[train_test['Aspect Ratio'].notnull(), 'Aspect Ratio'] = 1
        train_test['Aspect Ratio'] = train_test['Aspect Ratio'].fillna(0)
        train_test.loc[train_test['Synopsis'].notnull(), 'Synopsis'] = 1
        train_test['Synopsis'] = train_test['Synopsis'].fillna(0)
        train_test.loc[train_test['Actors'].notnull(), 'Actors'] = 1
        train_test['Actors'] = train_test['Actors'].fillna(0)
        train_test = train_test.replace(np.nan, ' ', regex=True)
        self.train_test = train_test

    def nlpFeatEng(self):
        def word2vec(doc):
            review_text = BeautifulSoup(doc, "lxml").get_text()
            letters_only = re.sub("[^a-zA-Z]", " ", review_text)
            words = letters_only.lower().split()
            stops = set(stopwords.words("english"))
            meaningful_words = [w for w in words if not w in stops]
            return " ".join(meaningful_words)

        product_long_description = []
        product_short_description = []
        short_description = []
        product_name = []
        for i in range(self.train_test.shape[0]):
            product_long_description.append(word2vec(self.train_test['Product Long Description'][i]))
            product_short_description.append(word2vec(self.train_test['Product Short Description'][i]))
            short_description.append(word2vec(self.train_test['Short Description'][i]))
            product_name.append(word2vec(self.train_test['Product Name'][i]))
        print(product_long_description,"\n",product_short_description,"\n",short_description,"\n",product_name)
        vectpld1 = TfidfVectorizer(analyzer="word", tokenizer=None, preprocessor=None, max_features=1500)
        vectpld2 = CountVectorizer(analyzer="word", tokenizer=None, preprocessor=None, max_features=6000)
        vectpsd1 = TfidfVectorizer(analyzer="word", tokenizer=None, preprocessor=None, max_features=500)
        vectpsd2 = CountVectorizer(analyzer="word", tokenizer=None, preprocessor=None, max_features=1500)
        vectsd1 = TfidfVectorizer(analyzer="word", tokenizer=None, preprocessor=None, max_features=500)
        vectsd2 = CountVectorizer(analyzer="word", tokenizer=None, preprocessor=None, max_features=1000)
        vectpn1 = TfidfVectorizer(analyzer="word", tokenizer=None, preprocessor=None, max_features=1500)
        vectpn2 = CountVectorizer(analyzer="word", tokenizer=None, preprocessor=None, max_features=6500)
        print(vectpld1,"\n",vectpld2,"\n",vectpn1,"\n",vectpn2,"\n",vectpsd1,"\n",vectpsd2,"\n",vectsd1,"\n",vectsd2)
        pld1 = vectpld1.fit_transform(product_long_description)
        sd1 = vectsd1.fit_transform(short_description)
        pn1 = vectpn1.fit_transform(product_name)
        psd1 = vectpsd1.fit_transform(product_short_description)
        product_long_description = vectpld2.fit_transform(product_long_description)
        product_short_description = vectpsd2.fit_transform(product_short_description)
        short_description = vectsd2.fit_transform(short_description)
        product_name = vectpn2.fit_transform(product_name)
        pld1 = pld1.toarray()
        sd1 = sd1.toarray()
        pn1 = pn1.toarray()
        psd1 = psd1.toarray()
        product_long_description = product_long_description.toarray()
        product_short_description = product_short_description.toarray()
        product_name = product_name.toarray()
        short_description = short_description.toarray()
        f1 = np.argmax(product_long_description, axis=1).reshape((product_long_description.shape[0], 1))
        f2 = np.argmax(product_short_description, axis=1).reshape((product_short_description.shape[0], 1))
        f3 = np.argmax(product_name, axis=1).reshape((product_name.shape[0], 1))
        f4 = np.argmax(short_description, axis=1).reshape((short_description.shape[0], 1))
        f1 /= product_long_description.shape[1]
        f2 /= product_short_description.shape[1]
        f3 /= product_name.shape[1]
        f4 /= short_description.shape[1]
        f5 = product_long_description.argsort(axis=1)[:, -4:-1]
        f6 = product_short_description.argsort(axis=1)[:, -4:-1]
        f7 = product_name.argsort(axis=1)[:, -3:]
        f8 = short_description.argsort(axis=1)[:, -3:]
        f5 /= product_long_description.shape[1]
        f6 /= product_short_description.shape[1]
        f7 /= product_name.shape[1]
        f8 /= short_description.shape[1]
        print(f7.shape)
        print(product_name.shape)

        # perform vectorizer operations
        selected_columns = ['Seller', 'Item Class ID', 'Actual Color', 'Genre ID', 'ISBN', 'Publisher', 'Artist ID',
                            'Actors',
                            'Aspect Ratio', 'Literary Genre', 'Synopsis', 'MPAA Rating', 'Recommended Location',
                            'Recommended Use']
        seller_encoder = LabelEncoder()
        item_classID_encoder = LabelEncoder()
        color_encoder = LabelEncoder()
        genreid_encoder = LabelEncoder()
        artistid_encoder = LabelEncoder()
        literary_genre = LabelEncoder()
        rating_encoder = LabelEncoder()
        recommended_location_encoder = LabelEncoder()
        recommended_use_encoder = LabelEncoder()
        self.train_test['Seller'] = seller_encoder.fit_transform(self.train_test['Seller'])
        self.train_test['Item Class ID'] = item_classID_encoder.fit_transform(self.train_test['Item Class ID'])
        self.train_test['Actual Color'] = color_encoder.fit_transform(self.train_test['Actual Color'])
        self.train_test['Genre ID'] = genreid_encoder.fit_transform(self.train_test['Genre ID'])
        self.train_test['Artist ID'] = artistid_encoder.fit_transform(self.train_test['Artist ID'])
        self.train_test['Literary Genre'] = literary_genre.fit_transform(self.train_test['Literary Genre'])
        self.train_test['MPAA Rating'] = rating_encoder.fit_transform(self.train_test['MPAA Rating'])
        self.train_test['Recommended Location'] = recommended_location_encoder.fit_transform(
            self.train_test['Recommended Location'])
        self.train_test['Recommended Use'] = recommended_use_encoder.fit_transform(self.train_test['Recommended Use'])
        self.train_test = self.train_test[selected_columns].as_matrix()
        print(self.train_test.shape)
        self.train_test = np.concatenate(
            (
                self.train_test, product_long_description, product_short_description, short_description, product_name,
                pld1, sd1,
                pn1,
                psd1, f1, f2, f3, f4), axis=1)
        del product_long_description
        del product_short_description
        del product_name
        del short_description
        del pld1
        del sd1
        del pn1
        del psd1
        del f1
        del f2
        del f3
        del f4
        del f5
        del f6
        del f7
        del f8
        Xtrain = self.train_test[:self.trainDF.shape[0]]
        Xtest = self.train_test[self.trainDF.shape[0]:]
        print(Xtrain.shape)
        print(Xtrain.head())
        print(Xtest.shape)
        print(Xtest.head())

        del self.train_test


if __name__ == "__main__":
    sol = Solution()
    sol.loadData(["train.tsv", "test.tsv"])
    # sol.describeDF(sol.trainDF)
    # sol.describeDF(sol.testDF)
    sol.prepDF(sol.trainDF)
    sol.nlpFeatEng()
