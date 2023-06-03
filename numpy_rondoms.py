from numpy import random
#  Generate Random integer number
#  Create to Random numbers 
numbers = random.randint(20)
print("Every time random numbers only show : ",numbers)

#  Generate Random Float
#  number =5
random_float =random.rand()
print ("Folat values  0,1 is started  : ", random_float)

#  Generate Random Array
num = random.randint(10 ,size= (3))
print ('show any 3 random numbers :',num)

#  Generate Random 2D Array
num = random.randint(10 ,size= (2 ,4))
print ('Convert to 2D array ,2row and 4 column :',num)

# generate  2D array  .
random_float =random.rand(2,3)
print ("Generate 2d array row & column  : ")
print (random_float)

#  Generate Random Number From Array
#  Using choice () method 
num = random.choice([10,23,22,45,66])
print("Choice any Random numbers : ",num)

# Using choice method and size of random numbers
#num = random.choice([1,4,8,7,5] ,size=(2,6))
num = random.choice([1,4,8,7,5] ,size=(2,3))
print("Choice any Random numbers with 2D array : ")
print(num)
