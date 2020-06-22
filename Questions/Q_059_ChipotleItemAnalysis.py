"""""""""
You are given a data set of Chipotle orders. You're asked to figure out the 
average order price and the average price per item ordered. 
Can you describe how you would do this using Python Pandas? 
"""
import pandas as pd
pd.set_option('display.max_colwidth', -1)
pd.set_option('float_format', '{:f}'.format)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

df = pd.read_csv('../Utils/chipotle.tsv', sep='\t')
print(df.shape)

df['item'] = df.apply(lambda row: str(row['item_name']) + ' ' + str(row['choice_description']), axis=1)
df['item_price'] = df['item_price'].apply(lambda ip: float(ip[1:]))
df.drop(['item_name', 'choice_description'], axis=1, inplace=True)
print(df.head(5))

# average order price and the average price per item ordered.
avg_price_per_item = df.groupby(['item'])['item_price'].mean().reset_index()

print(avg_price_per_item)

