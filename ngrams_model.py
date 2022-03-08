from sklearn.feature_extraction.text import CountVectorizer 
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score


def ngrams_model(X_train,X_test, y_train, y_test, n_range = (2, 3), top_words = 20):
    class ngrams_model: pass

    ngrams_model.vect = CountVectorizer(min_df = 5, ngram_range = n_range).fit(X_train.values.astype('U'))
    X_train_ngrams_vect = ngrams_model.vect.transform(X_train.values.astype('U'))
    ngrams_model.model = LogisticRegression(max_iter = 10000).fit(X_train_ngrams_vect, y_train)
    ngrams_pred = ngrams_model.model.predict(ngrams_model.vect.transform(X_test.values.astype('U')))
    ngrams_model.accuracy = roc_auc_score(y_test, ngrams_pred)
    feature_names_ngrams = np.array(ngrams_model.vect.get_feature_names())
    sorted_coef_index = ngrams_model.model.coef_[0].argsort()
    ngrams_model.top_negative_words = feature_names_ngrams[sorted_coef_index[:top_words]]
    ngrams_model.top_positive_words = feature_names_ngrams[sorted_coef_index[:-(top_words):-1]]
    return ngrams_model



