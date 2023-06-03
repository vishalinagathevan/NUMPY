import numpy as np

#  NumPy Products
#  Used to prod method 
arr = np.array([1, 2, 3, 4])
product_method  = np.prod(arr)
print("Prod method is multiply the all elements : ",product_method)

#  2D array 

arr1 = np.array([1, 2, 3, 4])
arr = np.array([2, 3, 4, 2])
arr2 = np.array([5, 6, 7, 8])
product_method = np.prod([arr1, arr2, arr])
print(" Miltiply the all array in same time : ",product_method)


#  Product Over an Axis =1 
#   Used to axis  value
arr1 = np.array([1, 2, 3, 4])
arr = np.array([2, 3, 4, 2])
arr2 = np.array([5, 6, 7, 8])
product_method = np.prod([arr1, arr, arr2,] ,axis=1)
print(" Miltiply the each array one by one  : ",product_method)


# Cummulative Product
arr = np.array([4,5, 6, 7, 8,9])
newarr = np.cumprod(arr)
print(newarr)