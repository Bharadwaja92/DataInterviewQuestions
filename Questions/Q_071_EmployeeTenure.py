"""""""""
Below is a snippet from a table that contains information about employees that work at Company XYZ:
employee_name	employee_id	date_joined	age	yrs_of_experience
Andy	123456	2015-02-15	45	24
Beth	789456	2014-02-15	36	15
Cindy	654123	2017-05-16	34	14
Dale	963852	2018-01-15	25	4

Company XYZ is looking to create a report that tracks the tenure of its employees. 
Using Python, write a snippet to add a column with each individual's years of experience. 
You can assume the current date is January 1st, 2019. All records in the table are shown in YYYY-MM-DD format.
"""
import pandas as pd
from datetime import datetime
pd.set_option('display.max_colwidth', -1)
pd.set_option('float_format', '{:f}'.format)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

cols = ['employee_name', 'employee_id', 'date_joined', 'age', 'yrs_of_experience']
data = [
    ['Andy', 123456, '2015-02-15', 45, 24],
    ['Beth', 789456, '2014-02-15', 36, 15],
    ['Cindy', 654123, '2017-05-16', 34, 14],
    ['Dale', 963852, '2018-01-15', 25, 4]
]

df = pd.DataFrame(data=data, columns=cols)
print(df)

df['date_joined'] = df['date_joined'].apply(lambda d: datetime.strptime(d, '%Y-%m-%d'))
df['tenure'] = datetime.strptime('2019-01-01', '%Y-%m-%d') - df['date_joined']
print(df)
