"""""""""
You are given an array containing reviews for a popular iOS app below:

reviews = [‘app is good, but forced updates are too frequent‘, 
            ‘love this app, use it daily to log calories', 
            'free version of this app has way too many ads’, ‘app doesn't load, 0/10’]

Your task is to determine sentiment from the review above. 
To do this you first decide to write code to find the count of individual words across all the reviews 
-- write this code using Python.
"""


def count_individual_words(reviews: list):
    word_counter = dict()
    for r in reviews:
        for word in r.split(' '):
            if word not in word_counter:
                word_counter[word] = 1
            else:
                c = word_counter[word]
                word_counter[word] = c + 1
    return word_counter


reviews = ['app is good, but forced updates are too frequent',
            'love this app, use it daily to log calories',
            'free version of this app has way too many ads', 'app doesn\'t load, 0/10']

for k, v in count_individual_words(reviews).items():
    print(k, '-->', v)

