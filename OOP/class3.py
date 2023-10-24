import math
class Rectangle:
    def __init__(self, length = '0', breadth = '0'):
        self.length = length
        self.breadth = breadth
    @property
    def length(self):
        return self.__length
    @length.setter
    def length(self, bola):
        if bola.isdigit():
            self.__length = bola
        else:
            print('Enter a Digit Only')
    @property
    def breadth(self):
        return self.__breadth
    @breadth.setter
    def breadth(self, mrpraise):
        if mrpraise.isdigit():
            self.__breadth = mrpraise
        else:
            print('Enter a digit only')
    def perimeter(self):
        return int(self.__length) * int(self.__breadth) * 2

rectangle = Rectangle()
rectangle.length = '5'
rectangle.breadth = '5'
print(rectangle.perimeter())
           
