"""""""""
There are a few ways we can score in American Football:

1 point - After scoring a touchdown, the team can choose to score a field goal
2 points - (1) after scoring touchdown, a team can choose to score a conversion, 
               when the team attempts to score a secondary touchdown or 
           (2) an uncommon way to score, a safety is score when the opposing team causes the ball to 
           become dead
3 points - If no touchdown is scored on the possession, a team can attempt to make a field goal
6 points - Awarded for a touchdown

Given the above, let's assume the potential point values for American Football are:
2 points - safety
3 points - only field goal
6 points - only touchdown
7 points - touchdown + field goal
8 points - touchdown + conversion
Given a score value, can you write a function that lists the possible ways the score could have been achieved?
For example, if you're given the score value 10, the potential values are:

8 points (touchdown + conversion) + 2 points (safety)
6 points (only touchdown) + 2x2 points (safety)
7 points (touchdown + field goal) + 3 points (only field goal)
5x2 points (safety)
2x2 points (safety) + 2x3 points (only field goal)

"""
from collections import Counter
# A different version of Coin Change
possible_scores = []


def get_possible_ways(score, points, partial=[]):
    s = sum(partial)
    if s == score:
        possible_scores.append(partial)
    if s >= score:
        return

    for i in range(len(points)):
        p = points[i]
        remaining = points[i: ]
        get_possible_ways(score=score, points=remaining, partial=partial+[p])
    return 0


points_dict = {2: 'safety', 3: 'only field goal', 6: 'only touchdown', 7: 'touchdown + field goal',
               8: 'touchdown + conversion'}
points = list(points_dict.keys())
print(points)
print(get_possible_ways(10, points))
print(possible_scores)

for ps in possible_scores:
    d = dict(Counter(ps))
    sent = ['{} * {} = {} Points'.format(d[v], points_dict[v], v) for v in d]
    print(sent)
