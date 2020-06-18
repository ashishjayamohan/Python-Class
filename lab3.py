#Problem 1
asciiVal = int(input("Enter given Ascii Value: "))
print("The Character is", chr(asciiVal))

#Problem 2
print(format(57.467657, "9.3f"))
print(format(12345678.923, "9.1e"))
print(format(5789.4, "<.2f"))
print(format(45, "<5d"))
print(format(0.457467657, "<9.3%"))

#Problem 3
employee = input("Enter employee's name: ")
hours = int(input("Enter number of hours worked in a week: "))
hourlypay = float(input("Enter hourly pay rate: "))
fedtax = float(input("Enter federal tax withholding rate: "))
statetax = float(input("Enter state tax withholding rate: "))

fedtaxpercent = fedtax * 100
statetaxpercent = statetax * 100
grosspay = round(float(hours * hourlypay), 2)
fedtaxnum = round(float(fedtax * grosspay), 2)
statetaxnum = round(float(statetax * grosspay), 2)
totaldeduction = round(float(fedtaxnum + statetaxnum), 2)
netpay = round(float(grosspay - totaldeduction), 2)

print('Employee Name: ' + str(employee))
print('Hours Worked: ' + str(hours))
print('Pay rate: $' + str(hourlypay))
print('Gross Pay: $' + str(grosspay))
print('Deductions:')
print('   Federal Withholding (' + str(fedtaxpercent) + "%): $" + str(fedtaxnum))
print('   State Withholding (' + str(statetaxpercent) + "%): $" + str(statetaxnum))
print('   Total Deduction: $' + str(totaldeduction))
print('Net Pay: $' + str(netpay))