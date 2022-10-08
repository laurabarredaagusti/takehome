from variables import *
from classes.extract_data import *
from classes.create_df import *
from functions import *

obj = Create_df()

df_list = [obj.tweet_df, obj.author_df]

create_database(df_list)