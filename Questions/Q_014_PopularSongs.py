"""""""""
Below are two table schemas for a popular music streaming application:

Table 1: user_song_log
Column Name	    Data Type	    Description
user_id	        id	            id of the streaming user
timestamp	    integer	        timestamp of when the user started listening to the song, epoch seconds
song_id	        integer	        id of the song
artist_id	    integer	        id of the artist

Table 2: song_info
Column Name	    Data Type	Description
song_id	        integer	    id of the song
artist_id	    integer	    id of the artist
song_length	    integer	    length of song in seconds

Question:
Can you write a SQL query to estimate the average number of hours a user spends listening to music daily?
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

my_cursor = mydb.cursor()

"""
song_info -      song_id | artist_id | song_length
user_song_log -  user_id | timestamp | song_id | artist_id
"""

merge_query = 'CREATE TABLE IF NOT EXISTS Q14_user_song_merge('\
              'SELECT song_info.song_id, song_info.artist_id, song_length, user_id, timestamp, ' \
              'from_unixtime(floor(timestamp), "%Y-%m-%d") as day FROM ' \
              'Q14_song_info AS song_info JOIN Q14_user_song_log as user_info ' \
              'ON song_info.song_id = user_info.song_id and song_info.artist_id = user_info.artist_id' \
              ')'

my_cursor.execute(operation=merge_query)

# join_table = my_cursor.fetchall()
# for x in join_table[:5]:
#     print(x)

# song_id, artist_id, song_length, user_id, timestamp
answer_query = 'SELECT user_id, day, SUM(song_length) FROM Q14_user_song_merge ' \
               'GROUP BY user_id, day'

my_cursor.execute(operation=answer_query)

answer_table = my_cursor.fetchall()
for x in answer_table[:5]:
    print(x)


