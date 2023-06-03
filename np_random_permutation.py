from numpy import random
import numpy as np
# shuffle the array itself only.
arrays = np.array([1, 2, 3, 4, 5])
random.shuffle(arrays)
print("Changing arrangement of elements in-place. : ",arrays)

#  Generating Permutation of Arrays
arrays = np.array([1, 2, 3, 4, 5])
random.permutation(arrays)
print("permutation method returns a re-arranged array : ",arrays)