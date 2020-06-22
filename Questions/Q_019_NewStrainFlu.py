"""""""""
You go to see the doctor about a cough you've had for a while. The doctor selects you at random to have a 
blood test for a new strain of flu, which for the purposes of this exercise we will say is currently 
suspected to affect 1 in 10,000 people in the US. 
The test is 99% accurate, in the sense that the probability of a false positive is 1%.
The probability of a false negative is zero. 
You test positive. What is the new probability that you have this strain of flu?
"""

"""
P(Affected) = 1/10000
Accuracy = 0.99
P(False positive) = 0.01
P(False Negative) = 0

P(B/A) = P(A/B)P(B) / P(A)

For a population of 10000 * 100 people
                    Has Disease             Does not have disease
Positive result         TP=99                         FP=99         198
Negative result         FN=1                          TN=99801      99802           
                         100                            99900

P(A) = P(Has Disease) = 100/10000*100 = 0.0001
P(B) = P(Positive test result) = 198/1000000 = 0.000198 

P(A/B) = P(Has Disease given Positive test results) = ???
P(B/A) = P(Got Positive results and has disease) = 0.99 <---This is nothing but accuracy

So,
P(A/B) = P(B/A)P(A) / P(B) = (0.99*0.0001)/0.000198 = 0.5

So, it is 50% possible that the patient has disease.
 
                       
Sensitivity = TP/(TP + FN)
Specificity = TN/(TN + FP)
Accuracy =  (TN+TP)/(TN+TP+FN+FP)
"""
