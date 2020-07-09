#Problem 1
def sumColumn(matrix):
	finalSums = [0, 0, 0, 0]
	for a in range(len(matrix)):
		for b in range(len(matrix[a])):
			finalSums[b] += float(matrix[a][b])
	return finalSums
matrix = [[], [], []]
for a in range(0, 3):
	matrix[a] = input('Enter in the numbers in line ' + str(a) + ': ').split()
sums = sumColumn(matrix)
for b in range(0, 4):
	print('The sum of the numbers in column ' + str(b) + ' is ' + str(sums[b]))

#Problem 2
def sumMajorDiagonal(matrix):
	sum = 0
	for i in range(len(matrix)):
		sum += float(matrix[i][i])
	return sum
matrix = [[], [], [], []]
for a in range(0, 4):
	matrix[a] = input('Enter in the numbers in line ' + str(a) + ': ').split()
print('The sum of the major diagonal is ' + str(sumMajorDiagonal(matrix)))