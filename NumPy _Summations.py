import numpy as np 
#  Add 1 value array to 2  array value

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])
newarr = np.add(arr1, arr2)
print(" Add 1array value to 2 array value : ",newarr)

# Sum method 
arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])
new_arr = np.sum([arr1, arr2])
print("Sum of both arrays : ",new_arr)

#  Summation Over an Axis. sum of values one by one array. 
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
new_arr = np.sum([arr1, arr2], axis=1)
print("Summation Over an Axis : ",new_arr)

#  Cummulative Sum

arr = np.array([1, 2, 3, 4])
new_arr = np.cumsum(arr)
print("Cummulative array : ",new_arr)