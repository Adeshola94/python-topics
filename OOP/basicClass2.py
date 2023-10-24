class Car:
    def __init__(self, speed, color):
        self.speed = speed
        self.color = color
        print(speed)
        print(color)
        print('This is a constructor function. \nAny object of this class will call this function.\nThis is first initialized by any object of this class')
honda = Car(2, 'green')
audi = Car(1.25, 'blue')
