import numpy as np
# Using TRUNC methon (truncate method)
arr =np.trunc([8.58445,-9.6907])
print ("Remove the decimal number using trunctate method  :", arr)

# The same result but method name is diffrent but answer is same 
# Using to fix method 
arr =np.fix([8.58445,-9.6907])
print ("Remove the decimal number using fix method :", arr) 

#  Rounding
print ('Rounding the  1 >=5 ')
arrs = np.around(3.1666)
print(" Rounding the decimal numbers : ",arrs)

#  Second position is rounding 
arrs = np.around(3.1666 ,3)
print(" Rounding the decimal 2 numbers  : ",arrs)
#  Dont change because its lessthen of 5 the 3 position 
arrs = np.around(3.16445 ,3)
print(" Rounding the decimal 3 numbers  : ",arrs)

# Floor 
#  decimal nearest intger. (???? -value )
arrys = np.floor([-3.1666, 3.6667])
print(arrys)

# Ceil
#  Decimal to nearest upper integer.  (???? -value )
arrs = np.ceil([-3.1666, 3.6667])
print(arrs)
