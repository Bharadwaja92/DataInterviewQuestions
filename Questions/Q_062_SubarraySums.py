"""""""""
Suppose you're given an array of integers, and a number x. 
Write a function to find the smallest subarray with a sum greater than the given value. 
Given the array, the array's length n, and the number x your function should return:
    The length of the smallest subarray that has a sum greater than x
    The actual subarray that has a sum greater than x

For example, given the following:
array = [5,6,2,3,8]
x = 12

Your output should be:
array length: 2
array: [8,6] //note that [8, 5] would also be an acceptable answer, as it contains a length of 2 as well

If the output is not possible, then you can return the length of the array + 1 
(indicating that an additional element would be needed to satisfy the requirements).
"""


def smallest_subarray_sum_0(nums, n, k) -> (int, list):
    cur_sum = 0
    min_len = n + 1
    start, end = 0, 0

    while end < n:
        while cur_sum <= k and end < n:
            cur_sum += nums[end]
            end += 1

        while cur_sum > k and start < n:
            if end - start < min_len:
                min_len = end - start

            cur_sum -= nums[start]
            start += 1

    return min_len


nums = [5, 6, 2, 3, 8, 7]
k = 12
print(smallest_subarray_sum_0(nums, len(nums), k))
