"""""""""
Given the following dataset which contains the close price for a given stock, 
can you plot confidence intervals for the dataset? 
The output should be a plot with the stock price and confidence intervals shown on the same plot.
"""
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from scipy import stats

pd.set_option('display.max_colwidth', -1)
pd.set_option('float_format', '{:f}'.format)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

df = pd.read_csv('../Utils/Stock price.csv')
print(df.head(10))

confidence = 0.95
n = len(df['Close'])
m, se = np.mean(df['Close']), stats.sem(df['Close'])
h = se * stats.t.ppf((1+confidence)/2., n-1)
print(m, m-h, m+h)

# fig, ax = plt.subplots()
# ax.plot(df['Date'], df['Close'])
# ax.fill_between(df['Close'], (df['Close']-h), (df['Close']+h), color='b', alpha=.1)

plt.plot(df['Close'], linewidth=2)
plt.fill_between(df['Close'].index, m-h, m+h, color='b', alpha=0.1)
plt.show()
