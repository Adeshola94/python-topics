#Single Inheritance
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
bingo = Dog('bingo')
print(bingo.move()) 

#multi level inheritance

class Creature:
    def __init__(self, alive):
        self.alive = alive

    def is_it_alive(self):
        return self.alive

class Animal(Creature):
    def __init__(self):
        super().__init__(True)
        self.health = 100

    def get_health(self):
        return self.health

class Cat(Animal):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def move(self):
        print('Cat is moving')



cat = Cat('lulu')


print(cat.is_it_alive())
print(cat.get_health())
cat.move()

#Hierarchical

class Location():
    def __init__(self, x,y):
        self.x = x
        self.y = y
    def get_location(self):
        return self.x , self.y

class Continent(Location):
    pass
class Country(Location):
    pass

continent = Continent(0,1)
country = Country(12,32)
print(continent.get_location())
print(country.get_location())

#multuple inheritance

class Date:
    date = '2023-04-25'
    def get_date(self):
        return self.date
    
class Time:
    time = '20-20-20'
    def get_time(self):
        return self.time

class DateTime(Date, Time):
    def get_date_time(self):
        return self.get_date()+'' + self.get_time()


date_time = DateTime()
print(date_time.get_date_time())