import numpy as np
# Joining array two or more arrays in a single array.import numpy as np

arr_1 = np.array([1, 2, 3])
arr_2 = np.array([4, 5, 6])
arr = np.concatenate((arr_1, arr_2))
print("Concadinate the 2 indivual arrays we can connect the single array : ",arr)

#  Joining Arrays Using Stack Functions
arr_1 = np.array([1, 2, 3])
arr_2 = np.array([4, 5, 6])
arr = np.stack((arr_1, arr_2), axis=1)
print("Order by  coloumns")
print (arr)

# Stacking Along Rows (h)
arr_1 = np.array([1, 2, 3])
arr_2 = np.array([4, 5, 6])
arr = np.hstack((arr_1, arr_2))
print("Stacking Along Rows (h) : ",arr)

# Stacking Along coloumn (v)
arr_1 = np.array([1, 2, 3])
arr_2 = np.array([4, 5, 6])
arr = np.vstack((arr_1, arr_2))
print("Stacking Along coloumn (v) : ")
print(arr)