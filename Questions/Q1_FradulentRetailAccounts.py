"""""""""
Below is a daily table for an active accounts at Shopify (an online ecommerce, retail platform).

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
Accounts get labeled by Shopify as fraudulent and they no longer can sell product
Every day of the table has every store_id that has ever been used by Shopify

Given the above, what percent of active stores were fraudulent by day? 
"""
import mysql.connector

host = "localhost"  # :3306
username, password, database = "root", "gaian", "DataInterviewQuestions"
mydb = mysql.connector.connect(host=host, username=username, passwd=password, database=database)

table_name = "Q1_Shopify"
my_cursor = mydb.cursor()

my_cursor.execute('SELECT COUNT(*) FROM {}'.format(table_name))

# print(my_cursor.fetchall())
# for c in my_cursor:
#     print(c)

QUERY = 'SELECT ' \
        'date, (sum(case when status="fraud" then 1 else 0 end) / count(store_id)) as fraud_rate ' \
        'FROM Q1_Shopify where revenue > 0 GROUP BY date ORDER BY date;'


# http://ubiq.co/database-blog/calculate-percentage-column-mysql/#:~:text=To%20calculate%20percentage%20of%20column%20in%20MySQL%2C%20you%20can%20simply,column%20with%20the%20original%20table.&text=If%20you%20want%20to%20add,CROSS%20JOIN%2C%20as%20shown%20below.
