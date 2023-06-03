import numpy as np 
#  NumPy Differences
#  Use the diff() function.

arr = np.array([10, 15, 25, 5,3])   #???
arrays= np.diff(arr)

print("Diffrence of 2 numbers : ",arrays)


#  This operation repeatedly by giving parameter (n)

arr = np.array([10, 15, 25, 5,3])   #???
arrays= np.diff(arr,n=2)

print("Diffrence of 2 numbers repeated the same process : ",arrays)