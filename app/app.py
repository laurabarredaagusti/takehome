from flask import Flask, render_template
import pandas as pd
from os import environ
from functions import *
import nltk

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    return render_template('index.html')

# 1. Devolver la predicción de los nuevos datos enviados mediante argumentos en la llamada
@app.route('/predict', methods=['GET'])
def predict():
    nltk.download('stopwords')
    model = load_models('sentiment_model')
    text = get_arguments('text')
    text = clean_text(text)

    df = pd.DataFrame()
    df['text'] = [text]

    prediction = model.predict(df['text'])
    prediction = prediction[0]
    # if prediction == 0:
    #     prediction = 'The sentiment of this tweet is positive'
    # else:
    #     prediction = 'The sentiment of this tweet is negative'
    return render_template('predict.html', predict=prediction)

if __name__ == '__main__':
  app.run(debug = True, host = '0.0.0.0', port=environ.get("PORT", 5000))