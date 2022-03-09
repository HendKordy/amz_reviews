
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics import roc_auc_score
import numpy as np

def naive_model(X_train, X_test, y_train, y_test):
    class naive_model: pass
    naive_model.vect = TfidfVectorizer(use_idf=True, lowercase = True)
    X_train_vect_naive = naive_model.vect.fit_transform(X_train)
    X_test_vect_naive = naive_model.vect.transform(X_test)
    naive_model.clf = MultinomialNB().fit(X_train_vect_naive, y_train)
    naive_model.accuracy = roc_auc_score(y_test, naive_model.clf.predict_proba(X_test_vect_naive)[:,1])
    return naive_model


def test_review(naive_model, text):
    text = np.array([text])
    # text_to_vect = naive_model.vect.transform(text)
    prediction = naive_model.clf.predict(naive_model.vect.transform(text))[0]
    if prediction:
        prediction = 'Positive review'
    else: 
        prediction = 'Negative review' 
    return prediction