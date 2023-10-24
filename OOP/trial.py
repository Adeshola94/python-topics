class Animal():
    def __init__(self):
        self.health_level = 100
    def get_status(self):
        print('Animal is healthy at a health level of{}plus'.format(self.health_level))
        return True

class Dog(Animal):
    def __init__(self, name):
        super().__init__()
        self.health_level = 150
        self.name = name

        print('My name is ' + self.name)
        print(super().get_status())

    def move(self):
        print('Cat is moving')
        return True
'''
    pass
class Human(Animal):
    def __init__(self):
        super().__init__()
        self.health_level = 200
        self.name = 
'''
        
bingo = Dog('bingo')
print(bingo.move()) 