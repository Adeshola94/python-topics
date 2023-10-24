class Checker:
    def __init__(self):
        self.a = 10 # public
        self._b = 11 # protected
        self.__c = 12 # private
    def public_method(self):
        print('self.a is accessible as ', self.a)
        print('self._b is accessible as ', self._b)
        print('self.__c is accessible as ', self.__c)
        self.__private_method('Bola', 10)
    def __private_method(self, name, age):
        self.name = name
        self.age = age
        print(self.name)
        print(self.age)

check = Checker()
print(check.public_method())
print(check.__c) #error
print(check.__private_method('Praise', 1)) #error