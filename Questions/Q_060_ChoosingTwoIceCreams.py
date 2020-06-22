"""""""""
Suppose you enter an ice cream store. They sell two types of ice cream: soft serve and frozen yogurt. 
Additionally, there are 10 flavors of soft serve and 13 flavors of frozen yogurt. 
You're really hungry, so you decide you can order and eat two ice creams before they melt, 
but are facing some decision fatigue given the amount of choices. 
How many ways are there to choose exactly two ice creams from the store? 
Figuring this out should help quantify that decision fatigue.
"""

from itertools import combinations
"""
Num ways to eat 2 icecreams = (1 SS and 1 FY) or (2 SS) or (2FF)
"""
n1 = len(list(combinations(range(10), 1))) * len(list(combinations(range(13), 1)))
n2 = len(list(combinations(range(10), 2)))
n3 = len(list(combinations(range(13), 2)))

print(n1, n2, n3)

num_total_ways = n1 + n2 + n3
print('num_total_ways =', num_total_ways)
