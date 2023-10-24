import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return math.pi*pow(self.__radius, 2)

    def __add__(self, other_radius):
        return Circle(self.__radius + other_radius.__radius)

    def __Lt__(self, other_radius):
        return(self.__radius < other_radius.__radius)

    def __gt__(self, other_radius):
        return(self.__radius > other_radius.__radius)
    
f_circle = Circle(2)
sec_circle = Circle(3)
adder = f_circle + sec_circle
print('Addition of the two radius are', adder)
print('Area of the first cricle is', f_circle.area())
print('Area of the second circle is', sec_circle.area())
print('Area of the third circle is', adder.area())
print('/n')
print(f_circle < sec_circle)
print(f_circle > sec_circle)
print('/n')
print(dir(f_circle))
print(dir(adder))    
