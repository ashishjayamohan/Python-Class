#Problem 1
celsius = float(input("Enter a degree in celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(celsius, "Celsius is: ", fahrenheit, " Fahrenheit")

#Problem 2
initial = int(input("Enter a number between 0 and 1000: "))
sum = sum(int(digit) for digit in str(initial))
print("The sum of the digits is:", sum)

#Problem 3
weightlb = float(input("Enter weight in pounds: "))
weightkg = weightlb * 0.45359237
heightin = float(input("Enter height in inches: "))
heightm = heightin * 0.0254
bmi = weightkg / (heightm ** 2)
print(bmi)