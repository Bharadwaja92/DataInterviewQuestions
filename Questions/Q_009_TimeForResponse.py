"""""""""
Question 9 - Time for a response on a messaging application
Below is a table schema for a P2P messaging application. 
The table contains send/receive message data for the application's users.

Column Name	    Data Type	Description
date	        string	    date of the message sent/received, format is 'YYYY-mm-dd'
timestamp	    integer	    timestamp of the message sent/received, epoch seconds
sender_id	    integer	    id of the message sender
receiver_id	    integer	    id of the message receiver

Question: Using Python and the Pandas library, how would you find the fraction of messages that get a response within 5 minutes?
For simplicity, let's limit data to March 1, 2018.
"""

# Using data from Q4
import datetime

import pandas as pd
import mysql.connector

pd.set_option('display.max_colwidth', -1)
pd.set_option('float_format', '{:f}'.format)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

host = "localhost"  # :3306
username, password, database = "root", "gaian", 'DataInterviewQuestions'
mydb = mysql.connector.connect(host=host, username=username, passwd=password, database=database)

msg_data = pd.read_sql(sql='SELECT * FROM Q4_MsgingApp', con=mydb)

print(msg_data.shape)
march_1_unix_ts = datetime.datetime(year=2018, month=3, day=1).timestamp()
march_2_unix_ts = datetime.datetime(year=2018, month=3, day=2).timestamp()

march_1 = msg_data[msg_data['timestamp'].between(march_1_unix_ts, march_2_unix_ts)]
print(march_1.shape)

"""
Can I do like this?
For a given message, get all msgs done within 5 mins of that. Out of those, get those msgs that are sent back.
"""


def get_early_responses(row):
    timestamp, s_id, r_id = row['timestamp'], row['sender_id'], row['receiver_id']
    response_time = 5 * 60
    msgs_within_5mins = march_1[(march_1['timestamp'] - timestamp <= response_time)
                                & (march_1['receiver_id'] == s_id) & (march_1['sender_id'] == r_id)]
    print(msgs_within_5mins.shape)
    # print(timestamp, s_id, r_id)
    return 1


x = msg_data.head(10)
x['msgs_lt5'] = x.apply(lambda row: get_early_responses(row), axis=1)
print('------------')
print(x)
