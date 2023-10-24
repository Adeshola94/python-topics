class Car:
    pass

honda = Car()
audi = Car()
mazda = Car()

honda.speed = 2
audi.speed = 3
mazda.speed = 1.25

honda.color = 'green'
audi.color = 'white'
mazda.color = 'blue'

print(f'Honda 2007 has a color of {honda.color} and a speed of {honda.speed}')
print(f'Audi 2020 has a color of {audi.color} and a speed of {audi.speed}')
print(f'Mazda 2010 has a color of {mazda.color} and a speed of {mazda.speed}')