"""""""""
String Distance Algorithms:
Hamming:        Number of positions with same symbol in both strings. 
                Only defined for strings of equal length.
                distance(‘abcdd‘,’abbcd‘) = 3       -> Chars at positions 0, 1, 4
Levenshtein:    Minimal number of insertions, deletions and replacements needed for 
                transforming string a into string b.
LCS Distance:   (Longest Common Substring distance) 
                Minimum number of symbols that have to be removed in both strings until 
                resulting substrings are identical.
                distance(‘ABCvDEx‘,’xABCyzDE’) = 5
Cosine:         1 minus the cosine similarity of both N-gram vectors.
Jaccard:        1 minus the quotient of shared N-grams and all observed N-grams.
"""


def get_levenshtein_distance(s1: str, s2: str):
    """
    The Levenshtein distance between two strings a and b is given by
    lev_a,b(len(a), len(b)) where lev_a,b(i, j) is equal to
        max(i, j) if min(i, j)=0
        otherwise:
            min(leva,b(i-1, j) + 1,
                leva,b(i, j-1) + 1,
                leva,b(i-1, j-1) + 1_ai≠bj)
    where 1_ai≠bj</sub> is the indicator function equal to 0 when ai=bj and equal to 1 otherwise,
    and leva,b(i, j) is the distance between the first i characters of a and the first j characters of b.
    :param s1: String 1
    :param s2: String 1
    :return: Distance calculated using Iterative approach
    """
    rows, cols = len(s1) + 1, len(s2) + 1
    dist = [[0 for _ in range(cols)] for __ in range(rows)]

    for i in range(1, rows):
        dist[i][0] = i
    for i in range(1, cols):
        dist[0][i] = i

    for col in range(1, cols):
        for row in range(1, rows):
            if s1[row - 1] == s2[col - 1]:
                cost = 0
            else:
                cost = 1
            dist[row][col] = min(dist[row - 1][col] + 1,  # deletion
                                 dist[row][col - 1] + 1,  # insertion
                                 dist[row - 1][col - 1] + cost)  # substitution

    return dist[row][col]

