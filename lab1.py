from turtle import *

#Problem 1
T = [["a", "a^2", "a^3"], [1, 1, 1], [2, 4, 8], [3,9,27],[4,16,64]]
for row in T:
    for value in row:
    	print(value, " ", end='')
    print("")

#Problem 2
forward(100)
right(90)
forward(100)
right(90)
forward(200)
right(90)
forward(200)
right(90)
forward(200)
right(90)
forward(100)
up()
right(90)
forward(100)
down()
forward(100)
up()
backward(100)
right(90)
down()
forward(100)
up()
backward(100)
down()
backward(100)
done()