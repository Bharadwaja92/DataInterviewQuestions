"""""""""
Given an array of unique integers and a sum value, can you use python to 
find the number of triplets with a sum smaller than the given value?

Example:
Array of integers = {5, 1, 3, 4, 7}
Value = 12
Solution: 4 (e.g. the output of your code)
Explanation: There are 4 triplets that have a sum less than 12: (1, 3, 4), (1, 3, 5), (1, 3, 7), and (1, 4, 5)
"""


def find_triplets_1(nums, val):
    count = 0
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                if nums[i] + nums[j] + nums[k] < val:
                    print(nums[i], nums[j], nums[k])
                    count += 1
    return count


nums = [5, 1, 3, 4, 7]
val = 12
print(find_triplets_1(nums, val))
