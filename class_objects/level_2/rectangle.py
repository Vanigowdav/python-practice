class Rectangle:
    def __init__(self, length, width):
        self.length = length 
        self.width = width 
    def area(self):
        area = self.length * self.width 
        return area
    def perimeter(self):
        peri = 2 * (self.length + self.width)
        return peri

r1 = Rectangle(40, 28)
r2 = Rectangle(15, 6)

print(r1.area())
print(r2.area())
print(r1.perimeter())
print(r1.perimeter())