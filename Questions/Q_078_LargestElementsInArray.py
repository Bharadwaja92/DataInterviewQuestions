"""""""""
Given an array with k distinct elements, write a function to return all elements that have at least two elements greater than themselves in the same array:

For example, given the following array:
array = [2,3,9,7,6]

Your function should return:
[2,3,6]
"""
import sys

method1 = "Sort the array. Return arr[:-2]"
method2 = "Find second biggest element and return all those <= that element"


def get_elements(nums):
    big1, big2 = -sys.maxsize, -sys.maxsize
    for i in range(len(nums)):
        if nums[i] > big1:
            big2 = big1
            big1 = nums[i]
        elif nums[i] > big2:
            big2 = nums[i]

    print(big1, big2)
    return [v for v in nums if v < big2]


array = [2, 3, 9, 7, 6]
print(get_elements(array))

