"""""""""
What is Bayes’ Theorem? How is it useful in a machine learning context?
"""

"""

https://machinelearningmastery.com/bayes-theorem-for-machine-learning/#:~:text=Bayes%20theorem%20provides%20a%20way,156%2C%20Machine%20Learning%2C%201997.&text=P(h%7CD)%3A%20Posterior,thing%20we%20want%20to%20calculate).

First we need to understand 3 types of probabilities
1. Marginal: Prob of an event occurring irrespective of other random variables. Eg. P(A)
2. Joint: Prob of 2 or more simultaneous events A and B Eg. P(A, B)
3. Conditional: P(A/B)

Joint Prob P(A, B) = P(A and B) = P(A/B) * P(B)     --|
           P(B, A) = P(B and A) = P(B/A) * P(A)     --|     -> SAME


Bayes' Theorem -- Calculates the Conditional Prob without using the Joint Prob.

Since  P(B) = P(B/A) * P(A) + P(B/Not A) * P(Not A)
            -----------------------------------------------------------------------------|
            |   P(A/B) = P(B/A) * P(A) / (P(B/A) * P(A) + P(B/not A) * P(not A))         |
            -----------------------------------------------------------------------------|
            
P(A/B)      =   P(B/A)      *   P(A)    /   P(B) 
Posterior       Likelihood      Prior       Evidence
"""
"""
Q. How is Bayes' Theorem used in Machine Learning?
-> For modelling hypotheses
-> For classification 
"""


