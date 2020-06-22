"""""""""
A palindrome is "a word, phrase, or sequence that reads the same backward as forward." 
Below are some example palindromes:
madam
racecar
tat
Can you write a python function that takes in a string and outputs the longest palindrome? 
If the string itself is a palindrome, the function would output the original string.
"""


def get_longest_palindrome_substring(s):
    # Find Even and odd substrings, check if they are Palindromes and store the biggest
    max_len = 1
    start, low, high = 0, 0, 0

    for i in range(1, len(s)):
        # For even substrings, use chars at i, i-1 as center points
        # Check if this even substring is a palindrome
        low, high = i-1, i
        while low >= 0 and high < len(s) and s[low] == s[high]:
            if high - low + 1 > max_len:
                start = low
                max_len = high - low + 1
            low -= 1
            high += 1

        # For odd substrings, use chars at i as center points
        # Check if this odd substring is a palindrome
        low, high = i - 1, i + 1
        while low >= 0 and high < len(s) and s[low] == s[high]:
            if high - low + 1 > max_len:
                start = low
                max_len = high - low + 1
            low -= 1
            high += 1
    return s[start: start+max_len]


print(get_longest_palindrome_substring('mada'))
print(get_longest_palindrome_substring('adam'))
print(get_longest_palindrome_substring('madam'))
print(get_longest_palindrome_substring('madammadam'))

