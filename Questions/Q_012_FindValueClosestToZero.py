"""""""""
You are given a list of Q 1D points, return the value in Q that is the closest to value j.
Example:
Q = [1, -1, -5, 2, 4, -2, 1]
j = 3

The answer in this case is 2.
"""


def find_closest_value(nums, val):
    diffs = [abs(val - v) for v in nums]
    print(diffs)
    return nums[diffs.index(min(diffs))]


Q = [1, -1, -5, 2, 4, -2, 1, 3]
j = 3
print(find_closest_value(Q, j))

