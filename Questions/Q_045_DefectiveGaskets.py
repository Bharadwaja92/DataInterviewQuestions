"""""""""
Suppose you're working in a parts manufacturing plant, and you're running quality analysis on the 
gasket production line. Gaskets produced by your company will be defective 1% of the time, 
and are distributed in packs of 20.

Your company has a policy where if 1 or more of the 20 gaskets in a given pack is defective, 
they will replace the entire package. What proportion of packages does the company need to replace?

If you're struggling with where to start here, consider that this is a binomial probability problem.
"""

P_Defective = 1/100

"""
P(1 or more defective) = 1 - (P(0 Defective))
"""

num_bulbs_in_pack = 20
P_Working = 1 - P_Defective
P_0_Defective = (P_Working)**20

P_ge1_Defective = 1 - P_0_Defective

print(P_ge1_Defective)  # 0.18209306240276923
