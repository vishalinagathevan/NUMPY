import numpy as np 
#  Small lcm value.
num1 = 10
num2 = 5
lcm_value = np.lcm(num1, num2)
print(" Lcm value : ",lcm_value)

#  Reduce the lcm values .
arr = np.array([3, 6, 9])
lcm_val = np.lcm.reduce(arr)
print("Reduce lcm values : ", lcm_val)