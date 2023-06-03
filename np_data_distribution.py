from numpy import random
#  Using 1D array  and choice method 
number =random.choice([1,2,3,4,5] ,p=[0.2,0.1,0.3,0.0,0.4] ,size=(6))
print ("Data distribution of random : ",number)

# 2d arrays ;
number =random.choice([1,2,3,4] ,p=[0.2,0.1,0.3,0.4] ,size=(2,2))
print ("Data distribution of random with 2D array : ")
print(number)