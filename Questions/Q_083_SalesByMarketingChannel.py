"""""""""
Given the following data set, can you plot a chart that shows the percent of revenue by marketing source?
"""
import pandas as pd
from matplotlib import pyplot as plt

pd.set_option('display.max_colwidth', -1)
pd.set_option('float_format', '{:f}'.format)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

df = pd.read_csv('../Utils/Sales data.csv')

print(df.head(5))

gdf = df.groupby(by=['source'])['purchase_value'].sum().reset_index()

plt.pie(x=gdf['purchase_value'], labels=gdf['source'], startangle=90)

plt.savefig('../Utils/Q_83.png')
plt.show()

