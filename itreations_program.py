#  Import numpy array modules.
import numpy as np 
#  Iteration using 1-D array.
array_list =([1,2,3,4,5,6,7])
#  Using iterating for loop.
for i in array_list:
  print("List of 1-D arrays : ",i)
  
#  Iteration using 2-D array.
array_list1 =([[1,2,3,4],[5,6,7,8]])
print("List of 2-D arrays : ")
for i in array_list1:
  print(i)
  
# each scalar element of the 2-D array:  
array_list1 =([[1,2,3,4],[5,6,7,8]])
print("Each scalar element of the 2-D array:")
for i in array_list1:
  # Using nested for loop 
  for x in i:
    print(x)
    
# 3-D array .
array_3D = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("Each row element of the 3-D array:")
for x in array_3D:
  print(x)   
    
#  Each scalar element of the 3-D array   
array_3D = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("Each row element of the 3-D array:")
for x in array_3D:
  # Print by row 
  # Using nested for loop.
  for i in x:
    # Print each elements of 3-D arrays.
    for y in i:
      print(y)   

#  Iterating Arrays Using nditer()   
array_3D = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(" Iterating Arrays Using nditer. Each element of the 3-D array:")
for x in np.nditer(array_3D):
   print(x)
   
   
#  Iterating array with diffrent data types.
#  Using flags=['buffered'] method .
B_arrays = np.array([1, 2, 3])
for i in np.nditer(B_arrays, flags=['buffered'], op_dtypes=['S']):
  print(" Diffrent data types : ",i)
  
# Change the data types  
arr = np.array([1, 2, 3, 4], dtype='f')

print(arr)
print(arr.dtype)

#  Iterating With Different Step Size
Arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8 ,9 ,0]])

for i in np.nditer(Arr[:, ::2]):
  print("Iterate through every scalar element of the 2D array skipping 1 element : ",i)
  
  #  Enumerated Iteration Using ndenumerate
 # Single dimention array. 
arr = np.array([1, 2, 3])
for i, x in np.ndenumerate(arr):
  print(" Mentioning sequence number 1-D : ",i, x)
  
#  2-D array  
#  extra eliment cant countable .its through error. 
arr = np.array([[1, 2, 3],[4.,5,6,],[7,8,9]])
for i, x in np.ndenumerate(arr):
  print(" Mentioning sequence number 2-D array  : ",i, x)  
  
  
  
  














   
      
      