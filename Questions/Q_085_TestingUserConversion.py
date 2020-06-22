"""""""""
Given the following data set, can you see if there's a significant difference between the 
conversion rate of users between the test and control group? 

The relevant columns in the table are conversion and test. 
The conversion column has values of 0 and 1, which represent if the user converted (1) or not (0). 
The test table has values of 0 and 1 as well, 0 for the control group and 1 for the test group.
"""
import pandas as pd

pd.set_option('display.max_colwidth', -1)
pd.set_option('float_format', '{:f}'.format)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

df = pd.read_csv('../Utils/test_table.csv')

print(df.head(5))

"""
Chi square = (Observed_i - Expected_i)**2 / Expected_i    summation over i
"""


