#Overall Imports
import random

#Problem 4.7
#Static Initialization
namesSingular = ["dollar", "quarter", "dime", "nickel", "penny"]
namesPlural = ["dollars", "quarters", "dimes", "nickels", "pennies"]
#Initialization Processing
originalAmount = float(input("Enter in original amount: "))
amountCentsTotal = originalAmount*100
amountDollars = int(amountCentsTotal/100)
amountCents = amountCentsTotal%100
amountQuarters = int(amountCents/25)
amountCentsPostQuarters = amountCents%25
amountDimes = int(amountCentsPostQuarters/10)
amountCentsPostDimes = amountCentsPostQuarters%10
amountNickels = int(amountCentsPostDimes/5)
amountPennies = amountCentsPostDimes%5
#Round 2 Processing
totalSequence = [amountDollars, amountQuarters, amountDimes, amountNickels, amountPennies]
for i in range(len(totalSequence)):
	if(totalSequence[i] == 1):
		print('1 ' + namesSingular[i])
	elif(totalSequence[i] > 1):
		print (str(totalSequence[i]) + ' ' + namesPlural[i])
#Runtime Complete
#Input: 13.56
#Output:
#13 dollars
#2 quarters
#1 nickel
#1 penny


#Problem 4.11
#Static Initialization
thirtyOneMonths = ["January","March","May","July","September","October","December"]
#Initialization Processing
year = int(input("Enter the year: "))
month = input("Enter the month: ")
#Round 2 Processing
isLeap = 0
if year % 400 == 0:
	isLeap = 1
elif year % 100 == 0:
	isLeap = 0
elif year % 4 == 0:
	isLeap = 1
#Output Processing
if month == "February":
	print(str(month) + ' of ' + str(year) + ' has ' + str(28 + isLeap) + ' days')
elif month in thirtyOneMonths:
	print(str(month) + ' of ' + str(year) + ' has 31 days')
else:
	print(str(month) + ' of ' + str(year) + ' has 30 days')
#Runtime Complete
#Input: 2000, February
#Output: February of 2000 has 29 days
#Input (2): 2005, March
#Output (2): March of 2005 has 31 days


#Problem 4.17 [EXTRA]
#Static Initialization
positions = ["scissor","rock","paper"]
#Initialization Processing
compPosition = random.randint(0,2)
userPosition = int(input("scissor(0), rock(1), paper(2): "))
#Output Processing
if(userPosition == compPosition):
	print('The computer is ' + positions[compPosition] + '. You are ' + positions[userPosition] + ' too. It is a draw.')
elif(userPosition > compPosition or userPosition == 0 and compPosition == 2):
	print('The computer is ' + positions[compPosition] + '. You are a ' + positions[userPosition] + '. You won.')
else:
	print('The computer is ' + positions[compPosition] + '. You are a ' + positions[userPosition] + '. You lose.')
#Runtime Complete
#Input: 1
#Output: The computer is scissor. You are a rock. You won.
#Input (2): 2
#Output (2): The computer is paper. You are paper too. It is a draw.


#Problem 4.23 [EXTRA]
#Initialization Processing
stringUserInput = input("Enter the coordinates of the point: ")
stringUserInputArray = stringUserInput.split(", ")
x = float(stringUserInputArray[0])
y = float(stringUserInputArray[1])
#Round 2 Processing
answer = True
if(abs(x) > 2.5 or abs(y) > 5.0):
	answer = False
#Output Processing
if(answer):
	print('Point (' + str(x) + ', ' + str(y) + ') is in the rectangle')
else:
	print('Point (' + str(x) + ', ' + str(y) + ') is not in the rectangle')
#Runtime Complete
#Input: 2, 2
#Output: Point (2.0, 2.0) is in the rectangle
#Input (2): 6, 4
#Output: Point (6.0, 4.0) is not in the rectangle


#Problem 5.3
#Output Processing
print(("Kilograms").ljust(10, ' ') + ("Pounds").rjust(10, ' '))
for i in range(1, 199):
	print(str(i).ljust(10, ' ') + str(round(i * 2.2, 1)).rjust(10, ' '))
#Runtime Complete
#Input: N/A
#Output:
# Kilograms     Pounds
# 1                2.2
# 2                4.4
# 3                6.6
# 4                8.8
# 5               11.0
# 6               13.2
# 7               15.4
# 8               17.6
# 9               19.8
# 10              22.0
# 11              24.2
# 12              26.4
# 13              28.6
# 14              30.8
# 15              33.0
# 16              35.2
# 17              37.4
# 18              39.6
# 19              41.8
# 20              44.0
# 21              46.2
# 22              48.4
# 23              50.6
# 24              52.8
# 25              55.0
# 26              57.2
# 27              59.4
# 28              61.6
# 29              63.8
# 30              66.0
# 31              68.2
# 32              70.4
# 33              72.6
# 34              74.8
# 35              77.0
# 36              79.2
# 37              81.4
# 38              83.6
# 39              85.8
# 40              88.0
# 41              90.2
# 42              92.4
# 43              94.6
# 44              96.8
# 45              99.0
# 46             101.2
# 47             103.4
# 48             105.6
# 49             107.8
# 50             110.0
# 51             112.2
# 52             114.4
# 53             116.6
# 54             118.8
# 55             121.0
# 56             123.2
# 57             125.4
# 58             127.6
# 59             129.8
# 60             132.0
# 61             134.2
# 62             136.4
# 63             138.6
# 64             140.8
# 65             143.0
# 66             145.2
# 67             147.4
# 68             149.6
# 69             151.8
# 70             154.0
# 71             156.2
# 72             158.4
# 73             160.6
# 74             162.8
# 75             165.0
# 76             167.2
# 77             169.4
# 78             171.6
# 79             173.8
# 80             176.0
# 81             178.2
# 82             180.4
# 83             182.6
# 84             184.8
# 85             187.0
# 86             189.2
# 87             191.4
# 88             193.6
# 89             195.8
# 90             198.0
# 91             200.2
# 92             202.4
# 93             204.6
# 94             206.8
# 95             209.0
# 96             211.2
# 97             213.4
# 98             215.6
# 99             217.8
# 100            220.0
# 101            222.2
# 102            224.4
# 103            226.6
# 104            228.8
# 105            231.0
# 106            233.2
# 107            235.4
# 108            237.6
# 109            239.8
# 110            242.0
# 111            244.2
# 112            246.4
# 113            248.6
# 114            250.8
# 115            253.0
# 116            255.2
# 117            257.4
# 118            259.6
# 119            261.8
# 120            264.0
# 121            266.2
# 122            268.4
# 123            270.6
# 124            272.8
# 125            275.0
# 126            277.2
# 127            279.4
# 128            281.6
# 129            283.8
# 130            286.0
# 131            288.2
# 132            290.4
# 133            292.6
# 134            294.8
# 135            297.0
# 136            299.2
# 137            301.4
# 138            303.6
# 139            305.8
# 140            308.0
# 141            310.2
# 142            312.4
# 143            314.6
# 144            316.8
# 145            319.0
# 146            321.2
# 147            323.4
# 148            325.6
# 149            327.8
# 150            330.0
# 151            332.2
# 152            334.4
# 153            336.6
# 154            338.8
# 155            341.0
# 156            343.2
# 157            345.4
# 158            347.6
# 159            349.8
# 160            352.0
# 161            354.2
# 162            356.4
# 163            358.6
# 164            360.8
# 165            363.0
# 166            365.2
# 167            367.4
# 168            369.6
# 169            371.8
# 170            374.0
# 171            376.2
# 172            378.4
# 173            380.6
# 174            382.8
# 175            385.0
# 176            387.2
# 177            389.4
# 178            391.6
# 179            393.8
# 180            396.0
# 181            398.2
# 182            400.4
# 183            402.6
# 184            404.8
# 185            407.0
# 186            409.2
# 187            411.4
# 188            413.6
# 189            415.8
# 190            418.0
# 191            420.2
# 192            422.4
# 193            424.6
# 194            426.8
# 195            429.0
# 196            431.2
# 197            433.4
# 198            435.6


#Problem 5.17
#Output Processing
print(("ASCII").ljust(10, ' ') + ("Character").rjust(10, ' '))
for i in range(33, 127):
	print(str(i).ljust(10, ' ') + str(chr(i)).rjust(10, ' '))
#Runtime Complete
#Input: N/A
#Output:
# ASCII      Character
# 33                 !
# 34                 "
# 35                 #
# 36                 $
# 37                 %
# 38                 &
# 39                 '
# 40                 (
# 41                 )
# 42                 *
# 43                 +
# 44                 ,
# 45                 -
# 46                 .
# 47                 /
# 48                 0
# 49                 1
# 50                 2
# 51                 3
# 52                 4
# 53                 5
# 54                 6
# 55                 7
# 56                 8
# 57                 9
# 58                 :
# 59                 ;
# 60                 <
# 61                 =
# 62                 >
# 63                 ?
# 64                 @
# 65                 A
# 66                 B
# 67                 C
# 68                 D
# 69                 E
# 70                 F
# 71                 G
# 72                 H
# 73                 I
# 74                 J
# 75                 K
# 76                 L
# 77                 M
# 78                 N
# 79                 O
# 80                 P
# 81                 Q
# 82                 R
# 83                 S
# 84                 T
# 85                 U
# 86                 V
# 87                 W
# 88                 X
# 89                 Y
# 90                 Z
# 91                 [
# 92                 \
# 93                 ]
# 94                 ^
# 95                 _
# 96                 `
# 97                 a
# 98                 b
# 99                 c
# 100                d
# 101                e
# 102                f
# 103                g
# 104                h
# 105                i
# 106                j
# 107                k
# 108                l
# 109                m
# 110                n
# 111                o
# 112                p
# 113                q
# 114                r
# 115                s
# 116                t
# 117                u
# 118                v
# 119                w
# 120                x
# 121                y
# 122                z
# 123                {
# 124                |
# 125                }
# 126                ~


#Problem 5.29
#Static Initialization
counter = 0;
#Output Processing
for i in range(2004, 2101, 4):
	if(not (counter + 1) % 10 == 0):
		print(str(i), end = ' ')
	else:
		print(str(i) + ' ')
	counter += 1
#Runtime Complete
#Input: N/A
#Ouput:
# 2004 2008 2012 2016 2020 2024 2028 2032 2036 2040 
# 2044 2048 2052 2056 2060 2064 2068 2072 2076 2080 
# 2084 2088 2092 2096 2100


#Problem 5.39
#Initialization Processing
isEnough = False
currentAmount = 0.01
percent = 0
while(isEnough == False):
	if(currentAmount <= 5000.00):
		percent = 8
	elif(currentAmount > 5000.00 and currentAmount <= 10000.00):
		percent = 10
	elif(currentAmount > 10000.00):
		percent = 12
	totalPay = 5000 + (currentAmount * (percent / 100))
	#Output Processing
	if(totalPay >= 30000):
		print('$' + str(round(currentAmount, 2)))
		isEnough = True
	else:
		currentAmount += 0.01
#Runtime Complete
#Input: N/A
#Output: $208333.34


#Problem 6.9
#Static Initialization
def footToMeter(foot):
	return 0.305 * foot
def meterToFoot(meter):
	return meter / 0.305


#Problem 6.11
#Static Initialization
def computeCommissions(salesAmount):
	percent = 0
	if(salesAmount <= 5000.00):
		percent = 8
	elif(salesAmount >= 5000.01 and salesAmount <= 10000.00):
		percent = 10
	elif(salesAmount >= 10000.01):
		percent = 12
	return (percent / 100) * salesAmount
#Output Processing
print(("Sales Amount").ljust(15, ' ') + ("Comission").rjust(15, ' '))
for i in range(10000, 100000, 5000):
	print(str(i).ljust(15, ' ') + str(computeCommissions(i)).rjust(15, ' '))
#Runtime Complete
#Input: N/A
#Output:
# Sales Amount         Comission
# 10000                   1000.0
# 15000                   1800.0
# 20000                   2400.0
# 25000                   3000.0
# 30000                   3600.0
# 35000                   4200.0
# 40000                   4800.0
# 45000                   5400.0
# 50000                   6000.0
# 55000                   6600.0
# 60000                   7200.0
# 65000                   7800.0
# 70000                   8400.0
# 75000                   9000.0
# 80000                   9600.0
# 85000                  10200.0
# 90000                  10800.0
# 95000                  11400.0