class House:
    def __init__(self, area):
        self.area = area

    def get_area(self):
        pass
#__init__ explanation of the init attribute
'''
Broad explanation of fileio and encapsulation

'''

class Apartment(House):
    def __init__(self, area):
        self.area = area
    def get_area(self):
        return self.area
    def get_price(self):
        return self.area * 300

class Condo(House):
    def __init__(self, area):
        self.area = area

    def get_area(self):
        return self.area

    def get_price(self):
        return self.area * 100
    
condo = Condo(100)
apartment = Apartment(300)

place_to_live = [condo, apartment]

for places in place_to_live:
    print('The area of a {} is {}'.format(str(places), places.get_area()))
    print('The price of a {} is {}'.format(str(places), places.get_price()))


def mystery(s):
    if len(s) == 2:
        return s
    return mystery(s[2:]) + s[0] 
print(mystery("python"))