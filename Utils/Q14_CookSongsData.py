"""""""""
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
"""

import random
import datetime
import mysql.connector

host = "localhost"  # :3306
username, password = "root", "gaian"
mydb = mysql.connector.connect(host=host, username=username, passwd=password)

my_cursor = mydb.cursor()

db_name = 'DataInterviewQuestions'  # Create Database 'DataInterviewQuestions'
my_cursor.execute("CREATE DATABASE IF NOT EXISTS {}".format(db_name))

table1, table2 = 'Q14_user_song_log', 'Q14_song_info'

tables_to_create = {'Q14_user_song_log': ("CREATE TABLE IF NOT EXISTS {} ("
                                          "user_id INT NOT NULL, "
                                          "timestamp VARCHAR(16) NOT NULL, "
                                          "song_id INT NOT NULL, "
                                          "artist_id INT NOT NULL"
                                          # "PRIMARY KEY (user_id)"
                                          ") ENGINE=InnoDB").format(table1),
                    'Q14_song_info': ("CREATE TABLE IF NOT EXISTS {} ("
                                      "song_id INT NOT NULL, "
                                      "artist_id INT NOT NULL, "
                                      "song_length INT NOT NULL, "
                                      "PRIMARY KEY (song_id)"
                                      ") ENGINE=InnoDB").format(table2)
                                      }

try:
    my_cursor.execute("USE {}".format(db_name))
    for table_name, table_create_query in tables_to_create.items():
        print('table_name =', table_name)
        print('table_create_query =', table_create_query)
        my_cursor.execute(table_create_query)
except Exception as e:
    print('Encountered exception', e)

print('Cook data')
num_users, num_songs, num_artists = 200, 100, 20
num_rows = 1000
user_ids = list(range(num_users))
song_ids = list(range(100))
artist_ids = list(range(20))
year, month = 2020, 6

user_id = [random.choice(user_ids) for _ in range(num_rows)]
time_stamps = [datetime.datetime(year=year, month=month, day=random.randint(1, 7), hour=random.randint(0, 23),
                                 minute=random.randint(0, 59)).timestamp() for _ in range(num_rows)]
song_id = [random.choice(song_ids) for _ in range(num_rows)]
artist_id = [random.choice(artist_ids) for _ in range(num_rows)]

for u_id, ts, s_id, a_id in zip(user_id, time_stamps, song_id, artist_id):
    try:
        insert_query = 'INSERT INTO {} ' \
                       '(user_id, timestamp, song_id, artist_id) ' \
                       'VALUES ({}, {}, {}, {});'.format(table1, u_id, ts, s_id, a_id)
        print(insert_query)
        my_cursor.execute(insert_query)
    except Exception as e:
        print('Encountered exception', e)

print('-'*50)
for artist in artist_ids:
    for song in range(artist*5, (artist+1)*5):
        song_length = random.randint(4, 6)
        print(artist, '-->', song, '-->', song_length)
        try:
            insert_query = 'INSERT INTO {} ' \
                           '(song_id, artist_id, song_length) ' \
                           'VALUES ({}, {}, {});'.format(table2, song, artist, song_length)
            print(insert_query)
            my_cursor.execute(insert_query)
        except Exception as e:
            print('Encountered exception', e)


mydb.commit()
my_cursor.close()
mydb.close()

