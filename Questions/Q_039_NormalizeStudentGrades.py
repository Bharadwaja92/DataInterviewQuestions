"""""""""
You are given a dataframe containing student information, named df (shown below). 
Suppose you want to normalize each student's grade based on their age.

Age	Favorite Color	Grade	Name
20	blue	88	Willard Morris
19	blue	95	Al Jennings
22	yellow	92	Omar Mullins
21	green	70	Spencer McDaniel
"""
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

data = [[20, 'blue', 88, 'Willard Morris'], [19, 'blue', 95, 'Al Jennings'],
        [22, 'yellow',	92,	'Omar Mullins'], [21, 'green', 70, 'Spencer McDaniel']]

df = pd.DataFrame(data=data, columns=['Age', 'FavoriteColor', 'Grade', 'Name'])

minmaxscaler = MinMaxScaler()
df['Normalised_grade'] = minmaxscaler.fit_transform(df[['Grade']])
print(df)
