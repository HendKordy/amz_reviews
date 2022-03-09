from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
import sklearn.metrics as metrics
import matplotlib.pyplot as plt

import numpy as np


def tfidf_model(X_train, X_test, y_train, y_test):
    class tfidf_model:pass
    tfidf_model.y_test = y_test
    tfidf_model.vect = TfidfVectorizer()
    vect_fit_train = tfidf_model.vect.fit_transform(X_train.values.astype('U'))
    vect_transform_test = tfidf_model.vect.transform(X_test.values.astype('U'))
    tfidf_model.model = LogisticRegression(random_state=123, penalty='l2').fit(vect_fit_train, y_train)
    tfidf_model.predictions = tfidf_model.model.predict_proba(vect_transform_test)[::,1]
    tfidf_model.accuracy = roc_auc_score(y_test, tfidf_model.predictions)
    feature_names = np.array(tfidf_model.vect.get_feature_names())
    sorted_coef_index = tfidf_model.model.coef_[0].argsort()
    tfidf_model.top_negative_words = feature_names[sorted_coef_index[:20]]
    tfidf_model.top_positive_words = feature_names[sorted_coef_index[:-21:-1]]
    
    return tfidf_model


def plot_tfidf(tfidf_model):
    fpr, tpr, _ = metrics.roc_curve(tfidf_model.y_test,  tfidf_model.predictions)

    #create ROC curve
    plt.plot(fpr,tpr)
    plt.ylabel('True Positive Rate')
    plt.xlabel('False Positive Rate')
    plt.show()