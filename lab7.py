from rectangle import rectangle
from stock import stock

#Problem 1
rectangle1 = rectangle()
rectangle1.setWidth(4)
rectangle1.setHeight(40)
print('Rectangle 1 Width: ' + str(rectangle1.width))
print('Rectangle 1 Height: ' + str(rectangle1.height))
print('Rectangle 1 Area: ' + str(rectangle1.getArea()))
print('Rectangle 1 Perimeter: ' + str(rectangle1.getPerimeter()))

rectangle2 = rectangle()
rectangle2.setWidth(3.5)
rectangle2.setHeight(35.7)
print('Rectangle 2 Width: ' + str(rectangle2.width))
print('Rectangle 2 Height: ' + str(rectangle2.height))
print('Rectangle 2 Area: ' + str(rectangle2.getArea()))
print('Rectangle 2 Perimeter: ' + str(rectangle2.getPerimeter()))


#Problem 2
stock1 = stock("Intel Corporation", "INTC", 20.5, 20.35)
print(str(stock1.getChangePercent()))