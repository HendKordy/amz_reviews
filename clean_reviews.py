#packages for data cleaning
import string
import re
import nltk
nltk.download('words')
from emot.emo_unicode import UNICODE_EMOJI, UNICODE_EMOJI_ALIAS, EMOTICONS_EMO
from flashtext import KeywordProcessor

# !pip install demoji
# !pip install emot
# !pip install flashtext


replace_short = {"'ll" : " will", "'ve":" have", "'s " : " is ", "'m " : " am ", "'re " : " are ", "'d ": " would "}

replace_neg = {
    "aren't": "are not",
    "can't": "cannot",
    "can't've": "cannot have",
    " cause": "because",
    "couldn't": "could not",
    "doesn't": "does not",
    "don't": "do not",
    " dont " : " do not ",
    "hadn't": "had not",
    "hasn't": "has not",
    "haven't": "have not",
    "isn't": "is not",
    "mayn't": "may not",
    "mightn't": "might not",
    "mustn't": "must not",
    "needn't": "need not",
    "oughtn't": "ought not",
    "shan't": "shall not",
    "shouldn't": "should not",
    "wasn't": "was not",
    "weren't": "were not",
    "won't": "will not",
    "wouldn't": "would not",
    " ain ": "are not",
    " aint " : " are not ",
    " arnt " : " are not ",
    "ain't": "are not"
    }

replace_shirts = {
    " t shirt" : " shirt",
    " tee " : " shirt ",
    "shirt shirt" : "shirt",
    " tees " : " shirts ",
    "t-shirt" : "shirt",
    " s ": " small ",
    " l ": " large ",
    " m ": " medium ", 
    " 2xl ": " xxl ",
    " 2x " : " xxl ",
    " 3xl ": " xxxl ",
    " 3x " : " xxxl ",
    " 4xl" : " xxxxl ",
    " 4x " : " xxxxl "
    }


#replace words 
def replace_words(text):
    for x,y in replace_short.items():
        text = re.sub(x, y, text)
    for x,y in replace_neg.items():
        text = re.sub(x, y, text)
    for x,y in replace_shirts.items():
        text = re.sub(x, y, text)

    return text




def clean(text):

    text = str(text)
    # make it all lowercase 
    text = text.lower()

    #convert emojis to text 
    text = convert_emoji(text)

    #replace words 
    text = replace_words(text)

    # remove text between </>
    text = re.sub('\<[^>]*\>', ' ', text)
    

    # remove all '\n'
    text = re.sub(r"\n", ' ', text)
    text = re.sub(r"\n\n ", ' ', text)
    text = text.rstrip("\n")
    

    # remove punctuation 
    #--- I am not going to remove punctuations for now because i might split the sentences. 
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text) 
    text = re.sub('\d+', '', text)
    return text.strip()





def only_english(text):
    words = set(nltk.corpus.words.words())
    x = " ".join(w for w in nltk.wordpunct_tokenize(text) if w.lower() in words or not w.isalpha())
    return x



# def clean_titles(title):

#     title = str(title)
#     #make all lowercase 
#     title = title.lower()
#     #remove punctuation
#     title = re.sub('[%s]' % re.escape(string.punctuation), '', title) 

#     # remove all '\n'
#     title = re.sub(r"\n", '', title)
#     return title




#convert emojis into text 
## formatting
all_emoji_emoticons = {**EMOTICONS_EMO,**UNICODE_EMOJI_ALIAS, **UNICODE_EMOJI_ALIAS}
all_emoji_emoticons = {k:v.replace(":","").replace("_"," ").strip() for k,v in all_emoji_emoticons.items()}

kp_all_emoji_emoticons = KeywordProcessor()
for k,v in all_emoji_emoticons.items():
    kp_all_emoji_emoticons.add_keyword(k, v)

def convert_emoji(text):
    return kp_all_emoji_emoticons.replace_keywords(text)
