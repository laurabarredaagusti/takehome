import pickle
from flask import request

def load_models(model_name):
    path = '../static/models/' + model_name
    return pickle.load(open(path,'rb'))

def get_arguments(arg):
    return request.args.get(arg, None)