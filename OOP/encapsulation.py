class Car:
    def __init__(self, speed = 1, color = 'unknown'):
        self.__speed = speed # private
        self.__color = color
    def set_speed(self, speed):
        self.__speed = speed
    def get_speed(self):
        return self.__speed
    def set_color(self, color):
        self.__color = color
    def get_color(self):
        return self.__color
    
ferrari = Car()
ferrari.set_speed(100)
ferrari.set_color('red')
print('The speed of a ferrari is ', ferrari.get_speed())
print('The color of a ferrari is ', ferrari.get_color())
print(ferrari.__speed)