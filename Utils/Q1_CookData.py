"""""""""
Cook data for Shopify data

The table is called store_account and the columns are:
Column Name	Data Type	Description
store_id	integer	    a unique Shopify store id
date	    string	    date
status	    string	    Possible values are: [‘open’, 'closed’, ‘fraud’]
revenue	    double	    Amount of spend in USD

Here's some more information about the table:
The granularity of the table is store_id and day
Assume “close” and “fraud” are permanent labels
Active = daily revenue > 0
"""
import random
import mysql.connector

host = "localhost"  # :3306
username, password = "root", "gaian"
mydb = mysql.connector.connect(host=host, username=username, passwd=password)

my_cursor = mydb.cursor()

db_name = 'DataInterviewQuestions'      # Create Database 'DataInterviewQuestions'
my_cursor.execute("CREATE DATABASE IF NOT EXISTS {}".format(db_name))

table_name = "Q1_Shopify"

TABLES = {table_name: ("CREATE TABLE {} ("
                       "store_id INT NOT NULL, "
                       "date VARCHAR(16) NOT NULL, "
                       "status VARCHAR(16) NOT NULL, "
                       "revenue DOUBLE NOT NULL, "
                       "PRIMARY KEY (store_id, date)"
                       ") ENGINE=InnoDB").format(table_name)}
print(TABLES[table_name])

try:
    my_cursor.execute("USE {}".format(db_name))
    for table in TABLES:
        my_cursor.execute(TABLES[table])
except Exception as e:
    print('Encountered exception', e)

print('Cook data')
"""
Every day of the table has every store_id that has ever been used by Shopify

d1  -  s1 
d1  -  s2  
d1  -  s3
d1  -  s4
d1  -  s5
... Similarly for all days
"""

num_rows = 500
possible_statuses = ['open', 'closed', 'fraud']

store_id = [random.randint(1, 100) for _ in range(num_rows)]
date = ['{}_{}'.format(random.randint(1, 12), random.randint(1, 28)) for _ in range(num_rows)]

status = [random.choice(possible_statuses) for _ in range(num_rows)]
revenue = [random.randint(100, 1000) for _ in range(num_rows)]
for id, dt, st, rev in zip(store_id, date, status, revenue):
    try:
        insert_query = 'INSERT INTO {} ' \
                       '(store_id, date, status, revenue) ' \
                       'VALUES ({}, "{}", "{}", {});'.format(table_name, id, dt, st, rev)
        print(insert_query)
        my_cursor.execute(insert_query)
    except Exception as e:
        print('Encountered exception', e)

mydb.commit()

my_cursor.close()
mydb.close()
