"""""""""
Given the data table below, determine if there is a relationship between fitness level and smoking habits:

                        Low fitness level Medium-low fitness level	Medium-high fitness level	High fitness level
Never smoked	            113	            113	                        110	                        159
Former smokers	            119	            135	                        172	                        190
1 to 9 cigarettes daily	    77	            91	                        86	                        65
>=10 cigarettes daily	    181	            152	                        124	                        73

You don't have to fully solve for the number here (that would be pretty time-intensive for an interview setting), 
but lay out the steps you would take to solve such a problem.
"""

"""
Our Null Hypothesis (H0) would be that 'There is no relation between Smoking and Fitness'
Our Altr Hypothesis (H0) would be that 'Smoking and Fitness are not independent'
"""
import pandas as pd
pd.set_option('display.max_colwidth', -1)
pd.set_option('float_format', '{:f}'.format)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

n_never_smoked = [113, 113, 110, 159]
n_former_smoker = [119, 135, 172, 190]
n_1to9_daily = [77, 91, 86, 65]
n_gt10_daily = [181, 152, 124, 73]

data = [n_never_smoked, n_former_smoker, n_1to9_daily, n_gt10_daily]
cols = ['Low fitness level', 'Medium-low fitness level', 'Medium-high fitness level', 'High fitness level']

df = pd.DataFrame(data=data, columns=cols, index=['never_smoked', 'former_smoker', '1to9_daily', 'gt10_daily'])

df['row_sum'] = df.sum(axis=1) 

n_low_fitness = df['Low fitness level'].sum()
n_med_low_fitness = df['Medium-low fitness level'].sum()
n_med_high_fitness = df['Medium-high fitness level'].sum()
n_high_fitness = df['High fitness level'].sum()

all_sum = sum(df['row_sum'])

print(n_low_fitness)

row_totals = list(df['row_sum'].values)

expected_low_fitness = [n_low_fitness*row_total/all_sum for row_total in row_totals]
expected_med_low_fitness = [n_med_low_fitness*row_total/all_sum for row_total in row_totals]
expected_med_high_fitness = [n_med_high_fitness*row_total/all_sum for row_total in row_totals]
expected_high_fitness = [n_high_fitness*row_total/all_sum for row_total in row_totals]
print(expected_low_fitness)
print(expected_med_low_fitness)
print(expected_med_high_fitness)
print(expected_high_fitness)

"""
We apply Chi-square test.
X**2
"""

degrees_of_freedom = (df.shape[0] - 1) * (df.shape[1] - 1 - 1)  # Added a new column
print(degrees_of_freedom)
