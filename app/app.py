from flask import Flask, render_template
import pandas as pd
from os import environ
from functions import *

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    return render_template('index.html')

# 1. Devolver la predicción de los nuevos datos enviados mediante argumentos en la llamada
@app.route('/predict', methods=['GET'])
def predict():
    model = load_models('sentiment_model')
    text = get_arguments('text')
    df = pd.DataFrame()
    df['text'] = [text]
    prediction = model.predict(df['text'])
    prediction = prediction[0]
    return render_template('predict.html', predict=prediction)

# if __name__ == '__main__':
#   app.run(debug = True, host = '0.0.0.0', port=environ.get("PORT", 5000))

# app.run()