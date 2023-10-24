# Use getter and setter method that comes with Python
import math
class Square:
    def __init__(self, length = '0', width = '0'):
        self.length = length
        self.width = width
    
    @property
    def length(self):
      return self.__length
    @length.setter
    def length(self, value):
        if value.isdigit():
            self.__length = value
        else:
            print('Enter a digit only')

    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, num):
        if num.isdigit():
            self.__width = num
        else:
            print('Enter a digit only')

    def area(self):
        return int(self.__length) * int(self.__width)
    
square = Square()

square.length = '2'
square.width = '5'
print(square.length)
print(square.area())

# Type Error
# Attribute Error
# Recursion Error