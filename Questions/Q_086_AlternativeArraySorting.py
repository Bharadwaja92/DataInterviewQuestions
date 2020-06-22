"""""""""
Given an array of integers, print the array in alternating min/max order. T
he first element should be the first maximum, second element should be the first minimum, 
third element should be second maximum, etc.

For example, given the following array:

arr[] = [10, 2, 11, 3, 7, 4, 1]
Your function should return:

11, 1, 10, 2, 7, 3, 4
"""


def alt_sort(nums):
    nums1 = sorted(nums, reverse=True)
    mid = len(nums) // 2
    maxs, mins = nums1[:mid], nums1[mid:][::-1]
    print(maxs, mins)
    ind1, ind2, ind = 0, 0, 0
    ans = []

    while ind < len(nums) and ind1 <= len(maxs) and ind2 <= len(mins):
        if ind % 2 == 0:
            ans.append(maxs[ind1])
            ind1 += 1
        if ind % 2 == 1:
            ans.append(mins[ind2])
            ind2 += 1
        ind += 1
        print(ans)
    return 0


print(alt_sort([10, 2, 11, 3, 7, 4, 1]))

