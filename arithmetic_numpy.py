import numpy as np 
#  Addtion 
print ('Addtion method ')
list_A =np.array([1,2,3])
list_B =np.array([4,5,6])
List_c =np.add(list_A,list_B)
#  Addinng new arrayb  
print("List c is add new array : ",List_c)

#  Subtract 
print ('Subtract method ')
list_A =np.array([10,20,30])
list_B =np.array([4,5,6])
List_c =np.subtract(list_A,list_B)
#  Addinng new array 
print("List c is a subtract : ",List_c)


#  Multiplicaton
print ('Multyply method ')
list_A =np.array([10,20,30])
list_B =np.array([4,5,6])
List_c =np.multiply(list_A,list_B)
print("List c is a multyply : ",List_c)

#  divition
print ('Divition  method ')
list_A =np.array([10,20,30])
list_B =np.array([4,5,6])
List_c =np.divide(list_A,list_B)
print("List c is a divition : ",List_c)

#  power
print ('Subtract method ')
list_A =np.array([10,20,30])
list_B =np.array([4,5,6])
List_c =np.power(list_A,list_B)
#  10*10*10*10 =4000
print("List c is a power  : ",List_c)


# Mod function
print ('mod method ')
list_A = np.array([10,20,7])
list_B =np.array([4,5,6])
List_c =np.mod(list_A,list_B)
#  10 /4 =2
print("List c is mod value  : ",List_c)

#  Remainder
print ('Remainder method ')
list_A = np.array([15,20,30])
list_B =np.array([4,5,6])
List_c =np.remainder(list_A,list_B)
#  we get a same result.
print("List c is a reminter value : ",List_c)

#  Quotient and Mod
print ('Quotient method ')
list_A = np.array([15,20,30])
list_B =np.array([4,5,6])
List_c =np.divmod(list_A,list_B)
#  The first array contains the quotient and second array contains the mod.
print("List c is a quotient values: ",List_c)


# Absoulte value
arr = np.array([-1, -2, 1, 2, 3, -4])
newarr = np.absolute(arr)
print('Absoute value is only printed :',newarr)