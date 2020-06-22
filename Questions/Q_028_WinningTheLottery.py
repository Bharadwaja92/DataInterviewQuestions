"""""""""
Suppose you're trying to figure out your chances of winning the lottery. 
The specific lottery you're interested in has 49 balls, each showing a single number. 
To win the jackpot you need to match 6 balls to win (note that order does not matter).

What is the probability that you can win the jackpot, given you buy 1 ticket?
What if you buy 3 lottery tickets?
"""
from itertools import combinations

total_number_of_balls = 49
to_win = 6

# num_possible_combinations = 49C6
num_possible_combinations = len(list(combinations(range(total_number_of_balls), to_win)))
print('num_possible_combinations =', num_possible_combinations)

prob_winning_1ticket = 1 / num_possible_combinations
prob_winning_3tickets = 3 / num_possible_combinations

print(prob_winning_1ticket)
print(prob_winning_3tickets)

