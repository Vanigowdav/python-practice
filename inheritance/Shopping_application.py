class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        print("Product:", self.name)
        print("Price:", self.price)


class Electronics(Product):
    def __init__(self, name, price, warranty):
        super().__init__(name, price)
        self.warranty = warranty

    def display(self):
        super().display()
        print("Warranty:", self.warranty)


class Mobile(Electronics):
    def __init__(self, name, price, warranty, brand):
        super().__init__(name, price, warranty)
        self.brand = brand

    def display(self):
        super().display()
        print("Brand:", self.brand)


mobile1 = Mobile("Smartphone", 20000, "2 years", "Samsung")

mobile1.display()
