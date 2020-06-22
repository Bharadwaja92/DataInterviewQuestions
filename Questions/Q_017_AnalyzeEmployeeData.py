"""""""""
Below is a snippet from a table that contains information about employees that work at Company XYZ:
Column name	        Data type	Example value	Description
employee_name	    string	    Cindy	        Name of employee
employee_id	        integer	    1837204	        Unique id for each employee
yrs_of_experience	integer	    14	            total working years of experience
yrs_at_company	    integer	    10	            total working years at Company XYZ
compensation	    integer	    100000	        dollar value of employee compensation
career_track	    string	    technical	    Potential values: technical, non-technical, executive

Company XYZ Human Resource department is trying to understand compensation across the company and 
asked you to pull data to help them make a decision regarding employee compensation.

Question: Can you pull the average, median, minimum, maximum, and standard deviations for salary 
across 5 year experience buckets at Company XYZ? 
(e.g. get the corresponding average, median, minimum, maximum, and standard deviations for experience 
buckets 0-5, 5-10, 10-15, ect.) You can assume the data is imported into a dataframe named df. 
"""
import pandas as pd

employee_df = pd.DataFrame(columns=['employee_name', 'employee_id', 'yrs_of_experience', 'yrs_at_company',
                                    'compensation', 'career_track'])
"""
We have the following methods available in Pandas

Bin values into discrete intervals.

pd.cut() - Bin values into discrete intervals.

Use `cut` when you need to segment and sort data values into bins. This function is also useful 
for going from a continuous variable to a categorical variable. 
For example, `cut` could convert ages to groups of age ranges.

pd.qcut() - Quantile-based discretization function. 
Discretize variable into equal-sized buckets based on rank or based on sample quantiles. 
For example 1000 values for 10 quantiles would produce a Categorical object indicating quantile membership 
for each data point. 

But the question asks for 5 Year exp buckets. Hence..
"""

employee_df['exp_bucket'] = employee_df['yrs_of_experience'].apply(lambda e: e % 5)

# average, median, minimum, maximum, and standard deviations
avg_df = employee_df.groupby(by='exp_bucket')['compensation'].mean()
min_df = employee_df.groupby(by='exp_bucket')['compensation'].min()
max_df = employee_df.groupby(by='exp_bucket')['compensation'].max()
sd_df = employee_df.groupby(by='exp_bucket')['compensation'].std()

answer_df = avg_df.merge(min_df, on='exp_bucket').merge(max_df, on='exp_bucket').merge(sd_df, on='exp_bucket')
print(answer_df)
