import sqlite3
from sqlalchemy import create_engine
import pandas as pd
from variables import *

def create_database(data):
    connection = sqlite3.connect('data/twitter.db')

    for index, df in enumerate(data):
        table = table_list[index]
        df.to_sql(table, con=connection, index=False)
    
    connection.close()