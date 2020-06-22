"""""""""
Suppose you're analyzing a population of 100,000 people, and you're trying to understand life expectancy. 
Within this population of 100,000 people, 
75% can expect to live to the age of 70, 
while 45% can expect to live to age 80. 
Given that a person is 70, what is the probability that they live to the age 80?
"""

"""
P(A) = P(Living upto Age 70) = 0.75
P(B) = P(Living upto Age 80) = 0.45

P(Living upto Age 70 / Living upto Age 80) = 1  -- If he lived upto 80, obviously, he lived upto 70
=> P(A/B) = 1 
    
P(Living upto Age 80 / Living upto Age 70) = P(B/A) = ?

Bayes' Theorem -->  P(A/B) = P(B/A) * P(A) / P(B)
"""

p_a = 0.75
p_b = 0.45
p_a_given_b = 1

p_b_given_a = p_a_given_b * p_b / p_a
print(p_b_given_a)
# 60% Probability

