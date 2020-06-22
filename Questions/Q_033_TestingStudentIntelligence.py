"""""""""
Suppose you're consulting for a school district, and the head of the school district thinks the 
students have above average intelligence. 
A random sample of thirty students have a mean IQ score of 112. 
Is there sufficient evidence to support the head's claim?

You can assume the mean IQ score across the population of all students 
(e.g. including students outside the head's school district) is 100, with a standard deviation of 15.
"""

"""
This is a Hypothesis Testing Problem  ---> Asking for evidence ==> p-value check

Null Hypothesis -> The one which we want to reject
    H_0: mean mu = 100
Alternative Hypothesis -> The one we want to prove
    H_1: mean mu > 100 

z_score = (x-mean)/(sd/sqrt(population size))
"""

sample_size = 30
sample_mean = 112
population_mean = 100
sd = 15

z = (sample_mean - population_mean) / (sd / (sample_size**0.5))
print('z = ', z)    # z =  4.381780460041329

p_value = 0.05  # 5%

"""
Relation between Z score and P-Value: 
    If the calculated p-value is less than the confidence level, We can reject the Null Hypothesis
    Conversely, the Z-score has to be greater than the z_score at P = confidence level  

z-score (Standard Deviations)	p-value (Probability)	Confidence level
< -1.65 or > +1.65                  < 0.10                  90%
< -1.96 or > +1.96                  < 0.05                  95%
< -2.58 or > +2.58                  < 0.01                  99%

As Z-score = 4.3817 > 1.96, 
        WE CAN REJECT THE NULL HYPOTHESIS AND WE CAN SUPPORT THE HEAD'S CLAIM

"""
