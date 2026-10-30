class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * self.width + self.height


r1 = Rectangle(20, 5)
r2 = Rectangle(35, 4)
print(r1.area())
print(r2.area())
print(r1.perimeter())
print(r2.perimeter())