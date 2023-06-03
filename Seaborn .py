import matplotlib.pyplot as plt
import seaborn as Sns 
Sns.distplot([0,1,2,3,4,5,6], hist= True)
plt.show()

Sns.distplot([0,1,2,3,4,5,6], hist= False)
plt.show()
