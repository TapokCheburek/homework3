class Product():
    def __init__(self, name:str, price:float, stock:int):
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, quantity):
        self.stock += quantity
        if self.stock < 0:
            self.stock -= quantity
            print("Количество товара на складе не может получиться отрицательным!\n"
                  "Не получилось взять товар со склада")

class Order():
    def __init__(self):
        self.products  = {}

    def add_product(self, product, quantity = 0):
        if product in self.products:
            self.products[product] += quantity
        else:
            self.products[product] = quantity

    def calculate_total(self):
        total = 0
        for product in self.products:
            total += self.products[product] * product.price
            return total

class Store():
    def __init__(self, products = []):
        self.products = products

    def add_product(self, product):
        if product in self.products:
            print("Такой товар уже есть в магазине!")
        else:
            self.products.append(product)
            print(f"Товар {product.name} добавлен в магазин")

    def list_products(self):
        for product in self.products:
            print(f"Товар: {product.name}, цена: {product.price}, кол-во: {product.stock}")

