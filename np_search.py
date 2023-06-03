import numpy as np
#  Searching arrays.
#  Index value :
Arrays =np.array ([1,2,1,3,4,5,1,6])
index_value =np.where(Arrays == 1)
print("Index value is only printed : ",index_value)

#  Search even number :
Arrays =np.array ([1,2,1,3,4,5,1,6])
index_value =np.where(Arrays%2 == 0)
print("Print only even number of index values : ",index_value)


#  Search odd number :
Arrays =np.array ([1,2,1,3,4,5,1,6])
index_value =np.where(Arrays%2 == 1)
print("Print only odd number of index values : ",index_value)

# Search sorter  ???
arrays_values = np.array([ 1,61, 7, 8, 5,9 ,10])
sort_value = np.searchsorted(arrays_values, 9)
print("Sort values : ",sort_value)

#  Search sorted in right side :
#  Start with 1 index.
arrays_values = np.array([ 10,1,6, 7, 8, 5,9 ,10])
sort_value = np.searchsorted(arrays_values, 9, side='right')
print(" Right side Sort values : ",sort_value)






