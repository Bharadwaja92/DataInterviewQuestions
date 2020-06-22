"""""""""
Suppose we have a standard (52 card) deck of cards, with an equal share of the cards associated with 
each of the four "suits" (e.g. clubs, spades, diamonds, and hearts). 

Question: If you were to draw 3 cards from the deck, one a time, what is the probability that 
you draw a club, a heart and a diamond in any order? 
Be sure you can explain your reasoning here using probablity theory.
"""

"""
All 3 draws are independent events. So, the order doesn't matter at all
"""

ans = (13/52) * (13/51) * (13/50)
print(ans)  # 0.01656862745098039
