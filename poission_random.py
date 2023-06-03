from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

#  Poisson Distribution
number= random.poisson(lam=2, size=10)
print(number)

sns.distplot(random.poisson(lam =3,size =10) ,kde= False)
plt.show()