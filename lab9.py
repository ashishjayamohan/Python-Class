import math
#Problem 1
inputString = input("Enter your numbers: ")
inputStringArray = inputString.split()
inputArray = []
total = 0
counter = len(inputStringArray)
for a in inputStringArray:
	inputArray.append(float(a))
	total += float(a)
average = total / counter
numBelow = 0
numAbove = 0
for b in inputArray:
	if(b < average):
		numBelow += 1
	else:
		numAbove += 1
print('The average is ' + str(average))
print('The number Above or Equal to the Average is ' + str(numAbove))
print('The number Below the Average is ' + str(numBelow))

#Problem 2
inputString = input("Enter your numbers: ")
inputStringArray = inputString.split()
inputArray = []
counter = len(inputStringArray)
for a in inputStringArray:
	inputArray.append(float(a))
finalArray = []
for b in inputArray:
	isPresent = False
	for c in finalArray:
		if(b == c):
			isPresent = True
			break
	if(isPresent == False):
		finalArray.append(b)
print('The distinct numbers are: ' + str(finalArray))

#Problem 3
def indexOfSmallestElement(array):
	least = 1000000000
	index = 0
	for a in range(len(array)):
		if array[a] < least:
			least = array[a]
			index = a
	return index

inputString = input("Enter your numbers: ")
inputStringArray = inputString.split()
inputArray = []
counter = len(inputStringArray)
for a in inputStringArray:
	inputArray.append(float(a))
print(indexOfSmallestElement(inputArray))