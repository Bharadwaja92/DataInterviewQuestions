"""""""""
Question 4 - Active users on a messaging application
Below is a table schema for a P2P messaging application. 
The table contains send/receive message data for the application's users, and has the following schema:
time_stamp  (#timestamp, epoch seconds)	
sender_id   (# id of the message sender)	
receiver_id (# id of the message receiver)

Question: What fraction of active users communicated with at least 15 unique people on March 1, 2018? 
You should be able to write complete code to answer this, given just the schema above.
"""
import datetime

import mysql.connector
import pandas as pd

pd.set_option('display.max_colwidth', -1)
pd.set_option('float_format', '{:f}'.format)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


host = "localhost"  # :3306
username, password, database = "root", "gaian", 'DataInterviewQuestions'
mydb = mysql.connector.connect(host=host, username=username, passwd=password, database=database)

msg_data = pd.read_sql(sql='SELECT * FROM Q4_MsgingApp', con=mydb)

print(msg_data.shape)

# What fraction of active users communicated with at least 15 unique people on March 1, 2018?
march_1 = msg_data[msg_data['timestamp'] == datetime.datetime(year=2018, month=3, day=1).timestamp()]
print(march_1.shape)
march_1_sender_count = march_1.groupby(by='sender_id').count().reset_index(drop=True)
march_1_receiver_count = march_1.groupby(by='receiver_id').count().reset_index(drop=True)
print(march_1_sender_count)
print(march_1_receiver_count)

# TODO

march_1_count_all = pd.merge(left=march_1_sender_count, right=march_1_receiver_count, left_on='receiver_id',
                             right_on='sender_id')
print(march_1_count_all)
