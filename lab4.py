import random

#Problem 1
num1 = random.randint(0,100)
num2 = random.randint(0,100)
print("What is the sum of ", num1, "and", num2)
guess = int(input(''))
if(guess == (num1+num2)):
	print ("true")
else:
	print ("false")

#Problem 2
array = [0,0,0]
array[0] = int(input("Enter in your first number: "))
array[1] = int(input("Enter in your second number: "))
array[2] = int(input("Enter in your third number: "))
array.sort()
print (array[0]," ",array[1]," ",array[2])