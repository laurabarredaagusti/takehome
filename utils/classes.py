from variables import *
import os
import requests

class Extract_data:

    token = token
    start_date = start_date
    max_results = max_results
    tweet_fields = tweet_fields
    expansions = expansions
    end_time = None
    user = user
    next_token = None

    def __init__(self):
        self.auth()
        self.create_headers()
        self.get_all_tweets()

    def auth(self):
        os.environ['TOKEN'] = self.token
        self.bearer_token = os.getenv('TOKEN')

    def create_headers(self):
        self.headers = {"Authorization": "Bearer {}".format(self.bearer_token)}

    def create_url(self):
        self.url = 'https://api.twitter.com/2/users/' + self.user + '/mentions'
        self.params = {'tweet.fields' : self.tweet_fields,
                        'start_time': self.start_date,
                        'end_time' : self.end_time,
                        'max_results': self.max_results,
                        'expansions': self.expansions,
                        'next_token': {}}

    def connect_to_endpoint(self):
        self.params['next_token'] = self.next_token
        response = requests.request("GET", self.url, headers = self.headers, params = self.params)
        self.response_json = response.json()
        print("Endpoint Response Code: " + str(response.status_code))
        if response.status_code != 200:
            raise Exception(response.status_code, response.text)

    def get_all_tweets(self):
        self.create_url()
        self.connect_to_endpoint()
        self.params["next_token"] = self.response_json["meta"]["next_token"]
        print(self.params["next_token"])

            