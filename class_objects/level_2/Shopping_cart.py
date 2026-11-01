class Cart:
    def __init__(self, product_name, price, quantity):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity
    def calculate_total(self):
        total = self.price * self.quantity
        return total

    
item1 = Cart("Biscuit", 10, 1)
item2 = Cart("Popcorn", 40, 2)
print(item1.product_name)
print(item1.price)
print(item1.quantity)
print(item1.calculate_total())
print(item2.product_name)
print(item2.price)
print(item2.quantity)
print(item2.calculate_total())