"""""""""
What is Naive Bayes' theorem, and why is it considered 'naive'? 
Why is it often used in practical applications rather than trying to implement an algorithm 
based on Bayes' Theorem (non-naive)?
"""

"""
The regular Bayes' Theorem considers that each input variable is dependent upon all other variables. 
This is very complex because of which we don't use the Bayes' theorem for any implementations.  

Naive Bayes' assumes that all input vars are independent from each other

P(class / X1, X2, …, Xn) = P(X1/class) * P(X2/class) * … * P(Xn/class) * (P(class) / P(data))

This value (P(class) / P(data))  is always constant. So we can remove that as well.

P(yi | x1, x2, …, xn) = P(x1, x2, …, xn | yi) * P(yi)
P(yi | x1, x2, …, xn) = P(x1|yi) * P(x2|yi) * … P(xn|yi) * P(yi)
"""

"""
Now different approaches are required for different datatypes. If the vars are
> Binary : Binomial Distribution can be used
> Categorical : Multinomial Distribution can be used
> Numerical : Gaussian Distribution can be used

If there are K classes and n variables, that k * n different probability distributions 
must be created and maintained.

"""
