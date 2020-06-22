"""""""""
A population of amoebas starts with 1. After a single period, assume the amoeba can divide into 1, 2, 3, or 0 
(it can die) with equal probability. What is the probability that the entire population dies out eventually?
"""

"""
P(Dying) = P(0) = 1/4
P(One child) = P(1) = 1/4
P(2 children) = P(2) = 1/4
P(3 children) = P(3) = 1/4

P_parent = (1/4 * P(3 children)**3) + (1/4 * P(2 children)**2) + (1/4 * P(1 child)) + 1/4

Solving this cubic equation, we get p = sqrt(2) - 1 ~= 0.414

42% probability that entire population dies out eventually

"""

