from numpy import random 
import matplotlib.pyplot as plt
import seaborn as sns
#  Difine random arrays.
#  Used to Normal method 
'''
number =random.normal(size=(2,2))
print ('Normal random 2 row and clomn : ')
print(number)


# Using keywords of random module.
number =random.normal(loc =2,scale= 2,size=(2,2))
print ('Normal random using keywords : ')
print(number)
'''

sns.distplot(random.normal(loc =1,scale= 2,size=(2,2)), hist=True)
plt.show()