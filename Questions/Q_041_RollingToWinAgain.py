"""""""""
Suppose you are playing a game where there are two fair six-sided dice, and 
every time you roll the dice and they add up to 9, you win $50. 
However, to roll the dice costs $20 to play. Is this a game you're willing to play?

You should be able to attach an expected value to each dice roll using probability theory here.
"""

"""
2 Dice
P(Adding upto 9) = P(3, 6) + P(4, 5) + P(5, 4) + P(6, 3)
                 = 1/36 + 1/36 + 1/36 + 1/36 = 1/9
Cost to play = 20
Win prize = 50        

Upon winning, we get 50-20 = $30

So, Expected earning = (1/9)*30 + (8/9)*-20 
                     = (30 - 240) / 9 = -210/9 = -23.3

We expect to lose $23.3 everytime. So, it is a losing game.                      
"""
