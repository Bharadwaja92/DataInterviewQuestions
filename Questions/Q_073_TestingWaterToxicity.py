"""""""""
Suppose you're trying to measure the Selenium toxicity in your tap water, and 
obtain the following values for each day:

day	selenium
1	0.051
2	0.0505
3	0.049
4	0.0516
5	0.052
6	0.0508
7	0.0506

The maxiumum level for safe drinking water is 0.05 mg/L -- using this as your alpha, 
does the selenium tap level exceed the legal limit? Hint: you can use a t-test here
"""
import numpy as np

alpha = 0.05

"""
Null Hypothesis H0: mu = 0.05
Altr Hypothesis Ha: mu >= 0.05

"""
alpha1 = 0.05
values = [0.051, 0.0505, 0.049, 0.0516, 0.052, 0.0508, 0.0506]

num_obs = len(values)
mean = np.mean(values)
sd = np.std(values)

print(mean, sd)     # mean = 0.05078571428571429   sd = 0.0008854838409892408

t = (mean - alpha) / (sd / np.sqrt(num_obs))

print('t =', t)     # t = 2.347648263381475

degrees_of_freedom = len(values) - 1

"""
For df = 6 and p-value = 0.05, t-value = 0.718

Since our t-value 2.347 > 0.718, we REJECT the NULL HYPOTHESIS and 
CONCLUDE THAT SELENIUM LEVELS ARE GREATER THAN THE LEGAL LIMIT
"""

