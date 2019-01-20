import os
import csv
import re
import nltk
from nltk.corpus import stopwords
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from ast import literal_eval
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer, HashingVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder, MultiLabelBinarizer
from sklearn.multiclass import OneVsRestClassifier
from sklearn.cross_validation import ShuffleSplit, KFold
from sklearn.preprocessing import MinMaxScaler
from keras.layers import Dense, Input, PReLU, Dropout, BatchNormalization, merge, Activation
from keras.models import Model

# nltk.download()
NFOLDS = 12
SEED = 31
np.random.seed(SEED)


def word2vec(doc):
    review_text = BeautifulSoup(doc, "lxml").get_text()
    letters_only = re.sub("[^a-zA-Z]", " ", review_text)
    words = letters_only.lower().split()
    stops = set(stopwords.words("english"))
    meaningful_words = [w for w in words if not w in stops]
    return " ".join(meaningful_words)


train = pd.DataFrame.from_csv('train.tsv', sep='\t')
test = pd.DataFrame.from_csv('test.tsv', sep='\t')

print('Train shape:' + str(train.shape))
print('Test shape:' + str(test.shape))

ntrain = train.shape[0]
ntest = test.shape[0]

# Multi-Label Binarizer
multilabelbin = MultiLabelBinarizer()
train['tag'] = train['tag'].apply(literal_eval)
Ytrain = multilabelbin.fit_transform(train['tag'])
print(train["tag"].head())
print(Ytrain.head())
# print(multilabelbin.classes_)
# print(train.columns)

# Concat train, test data
train_test = pd.concat([train.drop('tag', axis=1), test])

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

# word2vec operations
product_long_description = []
product_short_description = []
short_description = []
product_name = []
for i in range(train_test.shape[0]):
    product_long_description.append(word2vec(train_test['Product Long Description'][i]))
    product_short_description.append(word2vec(train_test['Product Short Description'][i]))
    short_description.append(word2vec(train_test['Short Description'][i]))
    product_name.append(word2vec(train_test['Product Name'][i]))
vectpld1 = TfidfVectorizer(analyzer="word", tokenizer=None, preprocessor=None, max_features=1500)
vectpld2 = CountVectorizer(analyzer="word", tokenizer=None, preprocessor=None, max_features=6000)
vectpsd1 = TfidfVectorizer(analyzer="word", tokenizer=None, preprocessor=None, max_features=500)
vectpsd2 = CountVectorizer(analyzer="word", tokenizer=None, preprocessor=None, max_features=1500)
vectsd1 = TfidfVectorizer(analyzer="word", tokenizer=None, preprocessor=None, max_features=500)
vectsd2 = CountVectorizer(analyzer="word", tokenizer=None, preprocessor=None, max_features=1000)
vectpn1 = TfidfVectorizer(analyzer="word", tokenizer=None, preprocessor=None, max_features=1500)
vectpn2 = CountVectorizer(analyzer="word", tokenizer=None, preprocessor=None, max_features=6500)
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
selected_columns = ['Seller', 'Item Class ID', 'Actual Color', 'Genre ID', 'ISBN', 'Publisher', 'Artist ID', 'Actors',
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
train_test['Seller'] = seller_encoder.fit_transform(train_test['Seller'])
train_test['Item Class ID'] = item_classID_encoder.fit_transform(train_test['Item Class ID'])
train_test['Actual Color'] = color_encoder.fit_transform(train_test['Actual Color'])
train_test['Genre ID'] = genreid_encoder.fit_transform(train_test['Genre ID'])
train_test['Artist ID'] = artistid_encoder.fit_transform(train_test['Artist ID'])
train_test['Literary Genre'] = literary_genre.fit_transform(train_test['Literary Genre'])
train_test['MPAA Rating'] = rating_encoder.fit_transform(train_test['MPAA Rating'])
train_test['Recommended Location'] = recommended_location_encoder.fit_transform(train_test['Recommended Location'])
train_test['Recommended Use'] = recommended_use_encoder.fit_transform(train_test['Recommended Use'])
train_test = train_test[selected_columns].as_matrix()
print(train_test.shape)
train_test = np.concatenate(
    (train_test, product_long_description, product_short_description, short_description, product_name, pld1, sd1, pn1,
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
Xtrain = train_test[:ntrain]
Xtest = train_test[ntrain:]
print(Xtrain.shape)
print(Xtest.shape)

del train_test


# Keras
def nnet(nfeatures):
    inputs = Input(shape=(nfeatures,))

    l1 = Dense(1400, init='he_normal')(inputs)
    l1 = PReLU()(l1)
    l1 = Dropout(0.4)(l1)

    l1 = Dense(1800, init='he_normal')(l1)
    l1 = PReLU()(l1)
    l1 = Dropout(0.4)(l1)

    l1 = Dense(3600, init='he_normal')(l1)
    l1 = PReLU()(l1)
    l1 = Dropout(0.4)(l1)

    l1 = Dense(32, activation='sigmoid')(l1)

    model = Model(input=inputs, output=l1)
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model


# 1st Level
kf = KFold(ntrain, n_folds=NFOLDS, shuffle=True)
Ynewtrain = np.zeros(shape=(Xtrain.shape[0], 32))
Ynewtest = np.zeros(shape=(Xtest.shape[0], 32))
idx = 0
for train_index, test_index in kf:
    print('Fold #: ' + str(idx + 1) + ' out of ' + str(NFOLDS))
    xtr = Xtrain[train_index]
    ytr = Ytrain[train_index]
    xte = Xtrain[test_index]
    yte = Ytrain[test_index]
    clf = nnet(Xtrain.shape[1])
    clf.fit(xtr, ytr, validation_data=(xte, yte), batch_size=128, nb_epoch=7)
    # Ynewtrain[test_index] = clf.predict(xte, batch_size=128)
    Ynewtest += clf.predict(Xtest, batch_size=128)
    idx += 1
Ynewtest /= NFOLDS
Xtrain = np.concatenate((Xtrain, Ynewtrain), axis=1)
Xtest = np.concatenate((Xtest, Ynewtest), axis=1)
Ytest = Ynewtest
print(Xtrain.shape)

'''
Xtrain = np.concatenate((Xtrain, Xtest), axis=0)
Ytrain = np.concatenate((Ytrain, Ynewtest), axis=0)
Ytrain[Ytrain < 0.5] = 0
Ytrain[Ytrain >= 0.5] = 1
del Ynewtest
del Ynewtrain
print(Xtrain.shape)
# 2nd level
Ytest = np.zeros(shape=(Xtest.shape[0], 32))
kf = KFold(Xtrain.shape[0], n_folds=7, shuffle=True)
idx = 0
for train_index, test_index in kf:
    print('Fold #: ' + str(idx + 1))
    xtr = Xtrain[train_index]
    ytr = Ytrain[train_index]
    xte = Xtrain[test_index]
    yte = Ytrain[test_index]
    clf = nnet(Xtrain.shape[1])
    clf.fit(xtr, ytr, validation_data=(xte, yte), batch_size=128, nb_epoch=5)
    Ytest += clf.predict(Xtest, batch_size=128)
    idx += 1
Ytest /= 7
'''
Ytest[Ytest < 0.5] = 0
Ytest[Ytest >= 0.5] = 1
Ytest = multilabelbin.inverse_transform(Ytest)
print(Ytest)
del Xtrain
del Xtest
with open('tags.tsv', mode='wb') as outfile:
    tsv_writer = csv.writer(outfile, delimiter="\t")
    header = ['item_id', 'tag']
    tsv_writer.writerow(header)
    for i in range(len(Ytest)):
        tuples = list(Ytest[i])
        row = []
        row.append(10593 + i)
        row.append(tuples)
        tsv_writer.writerow(row)
