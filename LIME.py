import lime
import sklearn.ensemble
from lime import lime_text
from sklearn.pipeline import make_pipeline
from lime.lime_text import LimeTextExplainer




def LIME(vect, model, X_test, y_test):
    class LIME: pass
    # converting the vectoriser and model into a pipeline
    LIME.c = make_pipeline(vect, model)
    # saving a list of strings version of the X_test object
    LIME.ls = list(X_test)
    # saving the class names in a dictionary to increase interpretability
    LIME.class_names = {0: 'negative review', 1:'positive review'}
    # create the LIME explainer
    # add the class names for interpretability
    LIME.explainer = LimeTextExplainer(class_names=LIME.class_names) 
    LIME.y_test = y_test
    return LIME


def explain(LIME, review):
    # choose a random single prediction
    # idx = 300
    # explain the chosen prediction 
    # use the probability results of the logistic regression
    # can also add num_features parameter to reduce the number of features explained
    if type(review) is int: 
        explaination = LIME.explainer.explain_instance(LIME.ls[review], LIME.c.predict_proba)
        # print results
        print('Document id: %d' % review)
        print('review: ', LIME.ls[review])
        print('Probability of review being positive =', LIME.c.predict_proba([LIME.ls[review]]).round(3)[0,1])
        print('True class: %s' % LIME.class_names.get(list(LIME.y_test)[review]))
    else :
        explaination = LIME.explainer.explain_instance(review, LIME.c.predict_proba)
        print('Probability of review being positive =', LIME.c.predict_proba(review).round(3)[0,1])
    return explaination

def plot_LIME(explaination):
    # print class names to show what classes the viz refers to
    print("1 = positive review, 0 = negative review")
    # show the explainability results with highlighted text
    explaination.show_in_notebook(text=True)