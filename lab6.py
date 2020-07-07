import random
#Problem 1
def reverse(number):
	reversed = 0
	while(number != 0):
		r = int(number % 10)
		reversed = reversed * 10 + r
		number = int(number / 10)
	return reversed
intInput = int(input("Enter the number: "))
print(reverse(intInput))


#Problem 2
def function(ch1, ch2, numberPerLine):
    counter = 1  
    for a in range(ord(ch1), ord(ch2) + 1):
        if counter % numberPerLine == 0:
            print(chr(a))        
        else:
            print(chr(a), end = " ")
            
        counter += 1
num1 = input("Enter the first char: ")
num2 = input("Enter the second char: ")
num3 = int(input("Enter the number of chars per line: "))
print(function(num1, num2, num3))


#Problem 3
def printMatrix(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(random.randint(0, 1), end = " ")

        print()
num = int(input("Enter the size of the matrix: "))
printMatrix(num)