"""""""""
Write a function to return a boolean that indicates if two strings are one edit away from being identical. 
The function should take in 2 strings and return a boolean. The definition of an "edit" is as follows:

Insert one character
Remove one character
Replace one character

A few examples of inputs and the function result are listed below.        
OneEditAway("pea", "peas") = True
OneEditAway("pea", "fleas") = False
OneEditAway("pea", "lea") = True
OneEditAway("pea", "seas") = False
"""

"""
This question pertains to Levenshtein distance because 
Levenshtein distance between two words is the minimum number of single-character edits 
(insertions, deletions or substitutions) required to change one word into the other. 
"""
# app
# from ..Utils import Q20_StringDistances
from Utils.Q20_StringDistances import get_levenshtein_distance


def OneEditAway(s1, s2):
    return get_levenshtein_distance(s1, s2) == 1


print(OneEditAway("pea", "peas"))   # True
print(OneEditAway("pea", "fleas"))   # False
print(OneEditAway("pea", "lea"))   # True
print(OneEditAway("pea", "seas"))   # False


