"""""""""
Suppose you are given a dataset of Baby names. Using the dataset, you're tasked with 
figuring out the top boy and girl names in 2009. Can you describe how you would do this using Python Pandas?
"""
import pandas as pd
pd.set_option('display.max_colwidth', -1)
pd.set_option('float_format', '{:f}'.format)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

names_df = pd.read_csv('../Utils/US_Baby_Names_right.csv', index_col=False)
names_df.drop(['Unnamed: 0'], inplace=True, axis=1)

born_2009 = names_df[names_df['Year'] == 2009]

grouped_male = born_2009[born_2009['Gender'] == 'M'].groupby(by=['Name']).count().reset_index().sort_values(by=['Count'], ascending=False)
grouped_female = born_2009[born_2009['Gender'] == 'F'].groupby(by=['Name']).count().reset_index().sort_values(by=['Count'], ascending=False)

print(grouped_male[['Name', 'Count']].head(1))
print(grouped_female[['Name', 'Count']].head(1))
