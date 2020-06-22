"""""""""
Suppose a fair six-sided die is rolled 10 times. What is the probability that a 2 is rolled at least once? 
"""

"""
P(Rolling 2 at least once) = 1 - P(Rolling 2 zero times)
"""

P_not_rolling_2_10_times = (5/6) ** 10

P_rolling_2_atleast_once = 1 - P_not_rolling_2_10_times

print(P_rolling_2_atleast_once)     # 0.8384944171101543
