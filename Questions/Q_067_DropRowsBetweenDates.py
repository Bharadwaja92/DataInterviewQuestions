"""""""""
Given the following dataframe, df, drop all the rows where the contract_sign_date is between 2018-09-01 and 2018-10-13 (inclusive):

df:

    vendor_id	name	contract_sign_date	total_spend
0	1	vendor_schmendor	2018-09-01	34324
1	2	parts_r_us	2018-09-03	23455
2	3	vendor_king	2018-10-11	77654
3	4	vendor_diagram	2018-08-21	23334
4	5	venny	2018-08-13	94843
5	6	vendtriloquist	2018-10-29	23444
"""
import pandas as pd
pd.set_option('display.max_colwidth', -1)
pd.set_option('float_format', '{:f}'.format)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

data = [
    [1, 'vendor_schmendor', '2018-09-01', 34324],
    [2,	'parts_r_us', '2018-09-03', 23455],
    [3,	'vendor_king', '2018-10-11', 77654],
    [4,	'vendor_diagram', '2018-08-21', 23334],
    [5,	'venny', '2018-08-13', 94843],
    [6,	'vendtriloquist', '2018-10-29', 23444]
]

df = pd.DataFrame(data=data, columns=['vendor_id', 'name', 'contract_sign_date', 'total_spend'])
df['contract_sign_date'] = df['contract_sign_date'].apply(pd.to_datetime)
print(df)

start, end = '2018-09-01', '2018-10-11'


res = df[(df['contract_sign_date'] > start) & (df['contract_sign_date'] < end)]
print(res)
