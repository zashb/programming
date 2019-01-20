import numpy as np
from sklearn.linear_model import LogisticRegression


def train_classifier_and_print_scores(df):
    print("Training classifier")
    X_train_w2v = np.array(list(map(np.array, df.w2v_features)))
    lr = LogisticRegression()
    return fit_model(lr, X_train_w2v, df.author_id)


def fit_model(model, X, y):
    print("Fitting classifier")
    model.fit(X, y)
    return model
