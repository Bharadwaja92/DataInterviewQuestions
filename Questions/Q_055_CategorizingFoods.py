"""""""""
You are given the following dataframe and are asked to categorize each food into 1 of 3 categories: 
meat, fruit, or other.

    food	        pounds
0	bacon	        4.0
1	STRAWBERRIES	3.5
2	Bacon	        7.0
3	STRAWBERRIES	3.0
4	BACON	        6.0
5	strawberries	9.0
6	Strawberries	1.0
7	pecans	        3.0

Can you add a new column containing the foods' categories to this dataframe using python?
"""
import pandas as pd

df = pd.DataFrame(columns=['food', 'pounds'])

df['category'] = df['food'].apply(lambda f: 'fruit' if f.lower() in ['strawberries'] else 'meat' if f.lower() == 'bacon' else 'other')

