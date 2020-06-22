"""""""""
Question 7 - Probability of passing through interview stages
Question: Given the information below, 
if you had a good first interview, what is the probability you will receive a second interview?

50% of all people who received a first interview received a second interview
95% of people that received a second interview had a good first interview
75% of people that did not receive a second interview had a good first interview
"""

"""
Bayes Theorem  - P(A/B) = P(B/A) * P(A) / P(B)

P(Got second interview) = 50% = 0.5
P(Did not get second interview) = ? 
P(Feel good about first interview / had second interview) = 0.95
P(Feel good about first interview / did not have second interview) = 0.75

P(Have second interview / Had good first interview) = ?

P(Have second interview / Had good first interview) = 
    P(Had good first interview / Had second interview) * P(Had second interview) / 
    P(Had good first interview)
                          
Include all possibilities                                                        
P(Had good first interview) = 
    P(Had good first interview / Had second interview) * P(Had second interview) + 
    P(Had good first interview / Did not have second interview) * P(Did not have second interview)
        
=   (0.95 * 0.5) + (0.75 * 0.5) = 0.475 + 0.375 = 0.85


P(Have second interview / Had good first interview) = 
    0.95 * 0.5 / 0.85 = 0.475 / 0.85 = 475 / 850 = 19 / 34 = 0.559
"""

