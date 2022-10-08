from classes.extract_data import *
import pandas as pd

class Create_df:

    obj = Extract_data()

    data_1 = obj.response_json_1 
    data_2 = obj.response_json_2

    retweet_count_list = []
    reply_count = []
    like_count = []
    quote_count = []

    df_tweet_1 = pd.DataFrame()
    df_tweet_2 = pd.DataFrame()
    df_tweet_list = [df_tweet_1, df_tweet_2]

    df_author_1 = pd.DataFrame()
    df_author_2 = pd.DataFrame()
    df_author_list = [df_author_1, df_author_2]

    def __init__(self):
        self.data_list = [self.data_1, self.data_2]

        self.main_tweet_df()
        self.main_author_df()
        self.drop_columns()
        self.get_detail_list()
        self.add_lists_to_df()


    def main_tweet_df(self):
        for index, data in enumerate(self.data_list):
            data = data['data']
            self.df_tweet_list[index] = pd.DataFrame(data)
            self.tweet_df = pd.concat(self.df_tweet_list)


    def main_author_df(self):
        for index, data in enumerate(self.data_list):
            data = data['includes']['users']
            self.df_author_list[index] = pd.DataFrame(data)
            self.author_df = pd.concat(self.df_author_list)


    def drop_columns(self):
        self.tweet_df.drop(columns='public_metrics', axis=1, inplace=True)
        self.tweet_df.drop(columns='edit_history_tweet_ids', axis=1, inplace=True)


    def get_detail_list(self):
        for data in self.data_list:
            for tweet in data['data']:
                self.retweet_count_list.append(tweet['public_metrics']['retweet_count'])
                self.reply_count.append(tweet['public_metrics']['reply_count'])
                self.like_count.append(tweet['public_metrics']['like_count'])
                self.quote_count.append(tweet['public_metrics']['quote_count'])


    def add_lists_to_df(self):
        self.tweet_df['retweet_count'] = self.retweet_count_list
        self.tweet_df['reply_count'] = self.reply_count
        self.tweet_df['like_count'] = self.like_count
        self.tweet_df['quote_count'] = self.quote_count

        

