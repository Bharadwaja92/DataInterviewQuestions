"""""""""
Suppose you are given a dataframe, df, that contains various negative values. 
In the context of your work, negative values can be considered 'bad data'. 
Write a function in Python (using Pandas) that replaces these bad values with the group mean.
"""

import pandas as pd

df = pd.DataFrame(columns=['name', 'value'])

df[df['value'] < 0] = df['value'].mean()


