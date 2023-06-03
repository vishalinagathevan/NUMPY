import numpy as np
#  Filtering Array
lists = np.array([1, 2, 3])
#  True value Store thenew array 
new_array= lists[[ False,True, False]]
print(new_array)


#  Creating a array list .
arr_list = np.array([1, 2, 3, 4, 5, 6, 7,8])

# Create an empty  Array list
empty_array = []

# Using for loop.
for element in arr_list:
# Using if else statements divisible by 2 
  if element % 2 == 0:
    empty_array.append(True)
  else:
    empty_array.append(False)
new_arraylist = arr_list[empty_array]
print(empty_array)
print(new_arraylist)