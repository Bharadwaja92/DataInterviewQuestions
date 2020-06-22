"""""""""
Suppose we are given an array of n integers which represent the value of some stock over time. 
Assuming you are allowed to buy the stock exactly once and sell the stock once, 
what is the maximum profit you can make? 
Can you write an algorithm using Python that takes in an array of values and returns the maximum profit?

For example, if you are given the following array:
2, 7, 1, 8, 2, 8, 14, 25, 14, 0, 4, 5

The maximum profit you can make is 24 because you would buy the stock when it's price is 1 and 
sell when it's 25. 
Note that we cannot make 25, because the stock is priced at 0 after it is priced at 25 
(e.g you can't sell before you buy).
"""


def get_maximum_profit_brute_force_0(prices):
    max_profit = 0
    for outer_time in range(len(prices)):
        for inner_time in range(len(prices)):
            earlier_time = min(outer_time, inner_time)  # For each pair, find the earlier and later times
            later_time = max(outer_time, inner_time)

            earlier_price = prices[earlier_time]
            later_price = prices[later_time]

            potential_profit = later_price - earlier_price
            max_profit = max(max_profit, potential_profit)

    return max_profit


def get_maximum_profit_brute_force_1(prices):
    max_profit = 0
    for buy_time, buy_price in enumerate(prices):
        for sell_time, sell_price in enumerate(prices[buy_time+1: ]):
            profit = sell_price - buy_price
            max_profit = max(profit, max_profit)
    return max_profit


def get_maximum_single_pass_0(prices):
    if len(prices) < 2:
        raise ValueError('Getting a profit requires at least 2 prices')

    min_price = prices[0]
    max_profit = prices[1] - prices[0]

    for buy_price in prices:
        min_price = min(min_price, buy_price)
        profit = buy_price - min_price
        max_profit = max(max_profit, profit)
    return max_profit


def get_maximum_single_pass_1(prices):
    if len(prices) < 2:
        raise ValueError('Getting a profit requires at least 2 prices')

    min_price = prices[0]
    max_profit = prices[1] - prices[0]

    for buy_time, buy_price in enumerate(prices[1:]):
        profit = buy_price - min_price
        max_profit = max(max_profit, profit)
        min_price = min(min_price, buy_price)
    return max_profit


stock_prices = [2, 7, 1, 8, 2, 8, 14, 25, 14, 0, 4, 5]
print('BruteForce_0-->', get_maximum_profit_brute_force_0(prices=stock_prices))
# Unneccesary efforts. O(n**2) time

print('BruteForce_1-->', get_maximum_profit_brute_force_1(prices=stock_prices))
# A bit better. But still O(n**2) time

print('SinglePass_0-->', get_maximum_single_pass_0(prices=stock_prices))

stock_prices_1 = [2, 2, 2, 2, 2, 2]
print('SinglePass_0-->', get_maximum_single_pass_0(prices=stock_prices_1))

stock_prices_2 = [9, 8, 7, 6, 5, 4]
print('SinglePass_0-->', get_maximum_single_pass_0(prices=stock_prices_2))
# In this case, we are wrong as we always have a loss

print('SinglePass_1-->', get_maximum_single_pass_1(prices=stock_prices))
# O(1) time