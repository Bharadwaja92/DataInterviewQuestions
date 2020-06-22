"""""""""
Given a matrix of order m*n then the task is to find the frequency of even and odd numbers in matrix.

For example, given the following inputs:
m = 2, n = 3
[[ 9, 11, 3 ],
[ 4, 12, 2 ]]

Your function should return the following output:
Frequency of odd #: 3
Frequency of even #: 3
"""


def matrix_frequency(matrix):
    # Flatten the matrix
    m1 = [v for r in matrix for v in r]
    evens, odds = [1 if v % 2 == 0 else 0 for v in m1], [0 if v % 2 == 0 else 1 for v in m1]
    return sum(evens), sum(odds)


mat = [[9, 11, 3], [4, 12, 2]]
num_even, num_odd = matrix_frequency(mat)
print('num_even =', num_even)
print('num_odd =', num_odd)
