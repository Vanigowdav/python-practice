class Mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

m1 = Mobile("Vivo", 15000)
m2 = Mobile("Oppo", 10000)
setattr(m2, "price", 20000)
print(m1.brand)
print(m1.price)
print(m2.brand)
print(m2.price)
