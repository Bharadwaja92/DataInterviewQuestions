"""""""""
You're given a set of data that is aggregated on a monthly basis (as illustrated in Table A).
Can you write code that can expand this monthly table into a daily table that spreads revenue across 
the 30 day period (as shown in Table B)?

You can assume each month has 30 days and that Table A is in a dataframe named "df".

Table A
index	Month	Revenue ($)
0	1	300
1	2	330
2	3	390

Table B
index	Month	Day	Revenue ($)
0	1	1	10
1	1	2	10
2	1	3	10
...	...	...	...
30	2	1	11
31	2	2	11
...	...	...	...
60	3	1	13
...	...	...	...
89	3	30	13
"""

import pandas as pd
import numpy as np

df = pd.DataFrame(data={'Month': [1, 2, 3], 'Revenue': [300, 330, 390]})

df['Num_days_in_month'] = 30
df['Revenue_per_day'] = df['Revenue'] / df["Num_days_in_month"]
print(df)

df1 = df.loc[np.repeat(df.index.values, repeats=df['Num_days_in_month'])]
df1.reset_index(inplace=True, drop=True)
df1['Index'] = df1.index
df1.drop(['Num_days_in_month', 'Revenue'], axis=1, inplace=True)
print(df1)

