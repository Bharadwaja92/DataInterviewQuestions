"""""""""
Question 35 - Filtering student information with Pandas
Suppose you have a dataframe, df, with the following records:

Age	    Favorite Color	Grade	Name
20	    blue	        88	    Willard Morris
19	    blue	        95	    Al Jennings
22	    yellow	        92	    Omar Mullins
21	    green	        70	    Spencer McDaniel

The dataframe is showing information about a group of students. 
Write code using Python Pandas to select the rows 
where the students' favorite color is blue or yellow and their grade is above 90.
"""
import pandas as pd

df = pd.DataFrame(columns=['Age', 'Favorite_Color', 'Grade', 'Name'])

ans_df = df[df['Favorite_Color'].isin(['blue', 'yellow']) & df['Grade']>90]

print(ans_df)

