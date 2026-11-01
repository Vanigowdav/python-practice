class Product: 
    def __init__(self, product_name, price):
        self.product_name = product_name
        self.price = price

product_list = []
p1 = Product("Dell Laptop", 65000)
p2 = Product("Thinkpad", 80000)
product_list.append(p1)
product_list.append(p2)
for obj in product_list:
    print(f"{obj.product_name} : {obj.price}")