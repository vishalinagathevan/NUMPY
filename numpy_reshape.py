#  Import numpy modules and change rename.
#  Reshape arrays.
import numpy as np

#  Define a variable of arrays 
#  This is 1-D array . Convert to 2-D array.
arr =np.array([1,2,3,4,5,6,7,8]) 
new_Arr =arr.reshape(2,4)
print("RESHAPE THE ARRAYS : ")
print(new_Arr)

#  Reshape from 1-D to 3-D array.
#  Difinne a 1-D array.
arr1 =np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,116,17,18])

#  Convert to 3-D array.
new_3dArray =arr1.reshape(2,3,3)
print("CONVERT TO 3-D ARRAY : ")
print(new_3dArray)

#  Copy or view 
arr =np.array([1,2,3,4,5,6,7,8]) 
c =arr.copy()
print("Returen copy or view : ")
print(arr.reshape(2,4).base)
print(c.base)

#  flattening  the array 
#  Multi dinmentional array covert to 1-D array 
multi_arrays = np.array([[1,2,3],[4,5,6]])
New_array = multi_arrays.reshape(-1)
print ("Convert a multidimetional into 1-D array:  ")
print(New_array)
