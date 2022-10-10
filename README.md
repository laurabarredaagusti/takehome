# technical_test_laura

Folder structure

app - all the necessary files fro deployment

--- static

------ images

--------- background.jpg - app background

------ models

--------- sentiment_model - machine learning model

--- templates

--------- index.html - homepage html

--------- predict.html - prediction page html

--- app.py - main app file

--- Dockerfile - Dockerfile for docker deployment

--- functions.py - functions file (aux of main app file)

--- requirements.txt - required libraries to use the app

--- sentiment_model - machine learning model

data - extracted data

--- twitter.db - extracted data sql database

info - generic information

--- laura_barreda.txt - link to github repository

--- Prueba_tecnica_DS.pdf - briefing

model - machine learning model

--- sentiment_model - machine learning model

notebooks - notebooks with the process

--- eda.ipynb - exploratory data analysis of the extracted data

--- extract_data.ipynb - notebook with all the steps to extract data using Twitter API

--- predictions.ipynb - notebook with all the steps to get the predictions 

utils - all the necessary files to extract data from Twitter

--- classes

------ create_df.py - class to create a df from the json, aux to main app.py

------ extract_data.py - class to extract data from Twitter API as a json, aux to main app.py

--- app.py - main app.py

--- functions.py - functions file aux to main app.py

--- variables.py - variables file aux to main app.py
