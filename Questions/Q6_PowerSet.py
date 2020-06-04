"""""""""
Question 6 - Python function to express power sets
Create a Python function that generates the power set given a set of values. 
For example, if you're given the following set:
set = {1, 2, 3}

Your python function should return the corresponding power set:
power set = { {}, {1}, {2}, {3}, {1, 2}, {2, 3}, {1, 3}, {1, 2, 3} }
"""


def get_powerset(nums):
    """
    If a list has n elements in it, It's powerset will contain 2 ^ n elements

    The logic is this.

    Let the list be [a, b, c]. So, the power set will contain 2 ^ 3 = 8 elements.
    Binary numbers from 0 to 7 will give us the answer
    000     None
    001     c
    010     b
    011     bc
    100     a
    101     ac
    110     ab
    111     abc

    :param nums:
    :return:
    """
    powerset = []
    powerset_size = 2 ** len(nums)
    for counter in range(powerset_size):
        ele = ''
        for j in range(len(nums)):
            # Check if the bit is set.
            if (counter & (1 << j)) > 0:
                ele += str(nums[j])
                # print(nums[j], end='')
        # print('')
        powerset.append(ele)

    return powerset


nums = [1, 2, 3]
print(get_powerset(nums))



