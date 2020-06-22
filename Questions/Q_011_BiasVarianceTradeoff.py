"""""""""
Question: Can you explain the Bias-Variance Tradeoff? 
Hint: Think about this in the context of learning algorithms and training data.
Can you share an example where/why you would want to use a biased estimator?
"""

"""
For any Supervised Machine Learning problem, the goal is 
    To Map a function (f) for the o/p variable(y) given the i/p data(x)
    
Now, there are 3 errors possible
1. Bias error
2. Variance error
3. Irreducible error - Inherent to the algorithm, cannot be removed

Bias : Assumptions made by model to learn the Target function
    Low Bias - Decision Trees, kNN, SVM
    High Bias - Linear and Logistic Regression, Linear Discriminant Analysis
Variance : Amount that the estimate of the Target fn will change if training data is changed.  
            --> How good is the underlying mapping learnt by the algorithm
    Low Variance - Linear and Logistic Regression, Linear Discriminant Analysis
    High Variance - Decision Trees, kNN, SVM
    
Increasing Bias decreases Variance and vice-versa

Bias-Variance Trade-off is tension between the error introduced by the bias and the variance.
We try to solve this using Parameterization.


Q2: Can you share an example where/why you would want to use a biased estimator?
We do this to reduce the Mean Squared Error (MSE). 
MSE can be decomposed as Variance + Bias Squared.  
Example: kNN classifier. 
For 𝑘=1: we assign a new point to its nearest neighbor. 
If we have a ton of data and only a few variables we can probably recover the true decision boundary and 
our classifier is unbiased; 
but for any realistic case, it is likely that 𝑘=1 will be far too flexible (i.e. have too much variance) 
and so the small bias is not worth it (i.e. the MSE is larger than more biased but less variable classifiers). 

"""


