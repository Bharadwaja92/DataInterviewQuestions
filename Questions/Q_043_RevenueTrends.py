"""""""""
Given the table below, called 'orders', write code to show the average revenue by month by channel:
order_id	channel	    date	    month	revenue
1	        online	    2018-09-01	09	    100
2	        online	    2018-09-03	09	    125
3	        in_store	2018-10-11	10	    200
4	        in_store	2018-08-21	08	    80
5	        online	    2018-08-13	08	    200

Your result should return the following in a structured table:

Month | Channel | Avg. Revenue
"""
import pandas as pd

records = [
    [1, 'online', '2018-09-01', 9, 100],
    [2, 'online', '2018-09-03', 9, 125],
    [3, 'in_store', '2018-10-11', 10, 200],
    [4, 'in_store', '2018-08-21', 8, 80],
    [5, 'online', '2018-08-13', 8, 200]
]

df = pd.DataFrame(data=records, columns=['order_id', 'channel', 'date', 'month', 'revenue'])
print(df)

gdf = df.groupby(by=['month', 'channel'])['revenue'].mean().reset_index()

print(gdf)
