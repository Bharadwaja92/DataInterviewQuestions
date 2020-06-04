"""""""""
The table contains send/receive message data for the application's users, and has the following schema:
time_stamp  (#timestamp, epoch seconds)	
sender_id   (# id of the message sender)	
receiver_id (# id of the message receiver)
"""
import datetime
import time
import pandas as pd

pd.set_option('display.max_colwidth', -1)
pd.set_option('float_format', '{:f}'.format)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

import random
import mysql.connector

host = "localhost"  # :3306
username, password = "root", "gaian"
mydb = mysql.connector.connect(host=host, username=username, passwd=password)

my_cursor = mydb.cursor()

db_name = 'DataInterviewQuestions'  # Create Database 'DataInterviewQuestions'
my_cursor.execute("CREATE DATABASE IF NOT EXISTS {}".format(db_name))

table_name = "Q4_MsgingApp"

table_create_query = ("CREATE TABLE {} ("
                      "timestamp INT(11) NOT NULL, "
                      "sender_id INT NOT NULL, "
                      "receiver_id INT NOT NULL"
                      ") ENGINE=InnoDB").format(table_name)

print(table_create_query)

try:
    my_cursor.execute("USE {}".format(db_name))
    my_cursor.execute(table_create_query)
except Exception as e:
    print('Got exception', e)

num_rows = 2000
year, month = 2018, 3

time_stamps = [datetime.datetime(year=year, month=month, day=random.randint(1, 7), hour=random.randint(0, 23),
                                 minute=random.randint(0, 59)).timestamp() for _ in range(num_rows)]
senders = [random.randint(0, 20) for _ in range(num_rows)]
receivers = [random.randint(0, 20) for _ in range(num_rows)]

for ts, snd, rec in zip(time_stamps, senders, receivers):
    try:
        insert_query = 'INSERT INTO {} ' \
                       '(timestamp, sender_id, receiver_id) ' \
                       'VALUES ({}, {}, {});'.format(table_name, ts, snd, rec)
        print(insert_query)
        my_cursor.execute(insert_query)
    except Exception as e:
        print('Encountered exception', e)

mydb.commit()
my_cursor.close()
mydb.close()
