from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
'''
number = random.binomial(n=5, p=0.2, size=2)
print(number)
'''
#  Visualization  of the binomial.
"""
sns.distplot(random.binomial(n=8, p=0.1, size=10), hist=False)
plt.show()
"""
sns.distplot(random.binomial(n=6, p=1.0, size=8), hist=True, kde=False)
plt.show()