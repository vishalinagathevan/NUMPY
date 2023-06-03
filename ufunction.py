import numpy as np
#  Used to numpy add method. single line code and fast runing(CPU performance.)
print('Used to mumpy add method :')
list_1 =[1,2,3,4,5]
list_2 =[6,7,8,9,10]
list_3 =np.add(list_1,list_2)
print ("Adding 2 lists : ", list_3)

#  Create  own ufunc.
#  Define a function name.
print ('Define a function :')
def ufun (x,y):
    return x+y
#  Using numpy function (frompyfunc).3 arrguments must 1= function name , 2 = how many input prametter. 3 = how many output.
ufun =np.frompyfunc(ufun ,2,1)
print(ufun([1,2,3],[4,5,6])) 


def ufunction (x,y,z):
    # define local variables 
    m =x+y 
    v=m+z
    print (" Add x and y value is : ",m)
    print (" Add y and z value is  : ",v)
    return v 
ufunction =np.frompyfunc(ufunction,3,1) 
print (ufunction([10,11,12],[1,2,3],[4,5,6]))   

#  Cheac if a datatypes.
print('Cheac if a datatypes :')
print(type(np.add))
print(type(np.frompyfunc))