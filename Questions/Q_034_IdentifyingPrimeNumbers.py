"""""""""
A prime number (or a prime) is a natural number greater than 1 that cannot be formed by multiplying 
two smaller natural numbers. 
Given a single #, n, write a function using Python to return whether or not the # is prime. 
Additionally, if the inputted # is prime, save it into an array, a.
"""


def is_prime_number(n):
    is_prime = True
    i = 2
    while is_prime and i <= n//2 + 1:
        is_prime = n % i != 0
        i += 1
    # print('i =', i-1)
    return is_prime


print(is_prime_number(337))
print(is_prime_number(437))
print(is_prime_number(689))
print(is_prime_number(697))
