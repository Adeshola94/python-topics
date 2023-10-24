class Triangle:
    def __init__(self, height, base):
        self.height = height
        self.base = base
    def area(self):
        return 0.5 * self.height * self.base

tri = Triangle(5, 4)
print(tri.base)
print(tri.height)
print(int(tri.area()))