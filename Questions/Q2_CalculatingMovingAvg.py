"""""""""
Question 2 - Calculating a moving average using Python
You are given a list of numbers J and a single number p.
Write a function to return the minimum and maximum averages of the sequences of p numbers in J.
Example:
J = [4, 4, 4, 9, 10, 11, 12]
p = 3

The sequences will be:
(4,4,4), (4,4,9), (4,9,10), (9,10,11), (10,11,12)

Here the minimum average will be 4 and the maximum average will be 11, which corresponds to the first and 
last sequences.
"""
import numpy as np


def cal_moving_avg(J: list, p: int):
    averages = []
    for i in range(0, len(J) - p + 1):
        averages.append(np.mean(J[i: i + p]))
    return min(averages), max(averages)


J = [4, 4, 4, 9, 10, 11, 12]
p = 3
print(cal_moving_avg(J, p))


