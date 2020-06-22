"""""""""
Suppose Charlie has 3 pairs of shoes, 4 different coats, and 2 different pants to wear in his wardrobe. 
Of those items, Charlie has 
exactly one pair of white shoes, exactly one black coat, and exactly one pair of khaki pants.

If Charlie selects each item of his wardrobe at random, 
what is the probability that he will wear the 
white shoes, black coat, and khaki pants? Hint: think of the rule of product here
"""

P_white_shoes = 1 / 3
P_black_coat = 1 / 4
P_khaki_pants = 1/ 2

P_white_shoes_black_coat_khaki_pants = P_white_shoes * P_black_coat * P_khaki_pants

print(P_white_shoes_black_coat_khaki_pants)     # 0.041666666666666664

