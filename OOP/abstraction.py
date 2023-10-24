from abc import ABC, abstractmethod

class ShapeAbstract(ABC):
    @abstractmethod
    def area(self): pass
    @abstractmethod
    def perimeter(self): pass

class Square(ShapeAbstract):
    def __init__(self, size):
        self.size = size
    def area(self):
        return self.size * self.size
    def perimeter(self):
        return 4 * self.size
sq = Square(5)
print('Area of the square ', sq.area())
print('Perimeter of the square ', sq.perimeter())