"""""""""
Suppose a bag contains 40 skittles: 16 yellow, 14 red, and 10 orange. 
You draw 3 skittles at random (without replacement) from the bag. 
What is the probability that you get 2 skittles of one color and another skittle of a different color?
"""

"""
16 yellow, 14 red, and 10 orange
3 skittles at random (without replacement)

2 skittles of one color and another skittle of a different color
  = Not(All same color + All Different color)

"""
y, r, o = 16, 14, 10
total = y + r + o
# P_All_same_color = YYY + RRR + OOO

P_all_yellow = (y/total) * ((y-1)/(total-1)) * ((y-2)/(total-2))
P_all_red = (r/total) * ((r-1)/(total-1)) * ((r-2)/(total-2))
P_all_orange = (o/total) * ((o-1)/(total-1)) * ((o-2)/(total-2))

P_all_same_color = P_all_yellow + P_all_orange + P_all_red

P_all_different = (y/total) * ((r)/(total-1)) * ((o)/(total-2))

print('P_all_yellow =', P_all_yellow)
print('P_all_orange =', P_all_orange)
print('P_all_red =', P_all_red)
print('P_all_same_color =', P_all_same_color)
print('P_all_different =', P_all_different)

P_2_of_one_color_and_another_of_different_color = 1 - (P_all_same_color + P_all_different)

print('P_2_of_one_color_and_another_of_different_color =', P_2_of_one_color_and_another_of_different_color)
