"""""""""
Suppose you are given a tuple containing ints and strings. 
Write a Python function to return the # of times a given element, n, appears in the tuple.

For example, given the tuple below, 
where n=3, your function should return 4, since 3 appears 4 times in the tuple.
my_tuple = 2, 'my_string', 4, 3, 3, 3, 2, 3
"""
from collections import Counter


def count_occurences(t, element):
    return Counter(t)[element]


my_tuple = (2, 'my_string', 4, 3, 3, 3, 2, 3)
search_value = 3
print(count_occurences(my_tuple, search_value))
