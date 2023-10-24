class Polygon:
    __width = None
    __height = None

    def set_value(self, height, width):
        self.__width = width
        self.__height = height
    def get_width(self):
        return self.__width
    def get_height(self):
        return self.__height
    
# this is a single inheritance

class Rectangle(Polygon):
    def area(self):
        return self.get_height()* self.get_width()
    
class Triangle(Polygon):
    def area(self):
        return self.get_height()*self.get_height()* 0.5
    
rect = Rectangle()
rect.set_value(10, 5)#50 

tri = Triangle()
tri.set_value(10, 10)#50

print(rect.area())

print(tri.area())