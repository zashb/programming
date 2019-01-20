from sklearn.base import TransformerMixin 


class Predictor(TransformerMixin):
    def transform(self, X, **transform_params):
        return [self.clean_text(text) for text in X]
    def fit(self, X, y=None, **fit_params):
        return self
    def get_params(self, deep=True):
        return {}
    def clean_text(self, text):     
        return text.strip().lower()