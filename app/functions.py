import pickle
from flask import request
from nltk.corpus import stopwords
import re
from nltk.stem.snowball import SnowballStemmer

def load_models(model_name):
    path = 'static/models/' + model_name
    return pickle.load(open(path,'rb'))

def get_arguments(arg):
    return request.args.get(arg, None)

def remove_links(text):
    return " ".join([' ' if ('http') in word else word for word in text.split()])

def remove_stopwords(text):
    stop = stopwords.words('spanish')
    return ' '.join([word for word in text.split() if word not in (stop)])

def remove_mentions(text):
    return re.sub(r"\@\w+[,]|\@\w+|[,]\@\w+", " ", text)

def signs_tweets(text):
    signs = re.compile("(\.)|(\;)|(\:)|(\!)|(\?)|(\¿)|(\@)|(\,)|(\")|(\()|(\))|(\[)|(\])|(\d+)|(\¡)")
    return signs.sub(' ', text.lower())

def remove_hash(text):
    return re.sub(r"\#\w+[,]|\#\w+|[,]\#\w+", "", text)

def spanish_stemmer(x):
    stemmer = SnowballStemmer('spanish')
    return " ".join([stemmer.stem(word) for word in x.split()])

def clean_emoji(x):
    emoji_text = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    return emoji_text.sub(r'', x)

def clean_text(x):
    text = remove_links(x)
    text = remove_stopwords(x)
    text = remove_mentions(x)
    text = signs_tweets(x)
    text = remove_hash(x)
    text = spanish_stemmer(x)
    return clean_emoji(x)