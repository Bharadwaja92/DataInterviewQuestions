"""""""""
Suppose we have a standard (52 card) deck of cards. 
Each card has an equal chance of being one of the four "suits" (e.g. clubs, spades, diamonds, and hearts).

Question: If you draw 3 cards from the deck, one at a time, 
what is the probability that you draw a club, a heart, and a diamond in that order?
"""

draw_club = 13 / 52
draw_heart = 13 / 51
draw_diamond = 13 / 50

"""
All these events are Independent. So, we multiply all these to get the combined probability
"""

prob = draw_club * draw_heart * draw_diamond
print('Prob =', prob)
"""
Prob = 0.01656862745098039
"""
