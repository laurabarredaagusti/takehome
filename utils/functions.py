import requests
import os
import json
from variables import *

def auth():
    os.environ['TOKEN'] = token
    return os.getenv('TOKEN')

def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers

def create_url(start_date, max_results, tweet_fields, expansions, end_time=None):
    
    search_url = "https://api.twitter.com/2/users/1162694149956603904/mentions" #Change to the endpoint you want to collect data from

    #change params based on the endpoint you are using
    query_params = {'tweet.fields' : tweet_fields,
                    'start_time': start_date,
                    'end_time' : end_time,
                    'max_results': max_results,
                    'expansions': expansions,
                    'next_token': {}}
    return (search_url, query_params)

def connect_to_endpoint(url, headers, params, next_token = None):
    params['next_token'] = next_token   #params object received from create_url function
    response = requests.request("GET", url, headers = headers, params = params)
    print("Endpoint Response Code: " + str(response.status_code))
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

def save_json(number, json_response):
    filename = 'data' + str(number) + '.json'
    path = 'data/' + filename
    with open(path, 'w') as f:
        json.dump(json_response, f)

def get_all_tweets(files, start_date, max_results, tweet_fields, expansions, end_time=None):
    for i in files:
        url = create_url(start_date, max_results, tweet_fields, expansions)
        bearer_token = auth()
        headers = create_headers(bearer_token)
        json_response = connect_to_endpoint(url[0], headers, url[1])
        save_json(i, json_response)
        end_time = json_response['data'][-1]['created_at']