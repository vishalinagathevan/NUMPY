import numpy as np
# Splicting arrays 
arr = np.array([1, 2, 3, 4, 5, 6])
new_arr = np.array_split(arr, 3)
print("Splicting multible arrays :")
print(new_arr)

#  it will adjust from the end accordingly.
#  Splicting array 4 parts.
arr = np.array([1, 2, 3, 4, 5, 6])
new_arr = np.array_split(arr, 4)
print(" it will adjust from the end accordingly.:")
print(new_arr)

# Split Into Arrays with index based 
arr = np.array([1, 2, 3, 4, 5, 6])
NEW_ARRAY = np.array_split(arr, 2)

print(NEW_ARRAY[0])
print(NEW_ARRAY[1])
