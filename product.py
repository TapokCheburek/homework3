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
        if product.stock < quantity:
            print(f"Количество продуктов {product.name} на складе меньше {quantity}\n"
                  f"Добавлено в заказ {product.stock} {product.name} ")
            quantity = product.stock
        if product in self.products:
            self.products[product] += quantity
        else:
            self.products[product] = quantity

    def calculate_total(self):
        total = 0
        for product in self.products:
            print( f"{product.name}  - {self.products[product]} шт.  {product.price} р.")
            total += self.products[product] * product.price

        return total

    def pay(self):
        for product in self.products:
            product.update_stock(-self.products[product])

    def remove_product(self, product, quantity):
        if self.products[product] <= quantity:
            self.products.pop(product)
        else:
            self.products[product] -= quantity

    def return_product(self, product, quantity):
        if self.products[product] <= quantity:
            quantity = self.products[product]
            self.products.pop(product)
        else:
            self.products[product] -= quantity
        product.update_stock(quantity)


class Store():
    def __init__(self, products: list[Product] = None):
        if products is None:
            products = []
        self.products = products

    def add_product(self, product):
        if product in self.products:
            print("Такой товар уже есть в магазине!")
        else:
            self.products.append(product)
            print(f"Товар {product.name} добавлен в магазин")

    def list_products(self):
        print("Все товары в магазине:")
        for product in self.products:
            print(f"Товар: {product.name}, цена: {product.price}, кол-во: {product.stock}")

    def create_order(self):
        return Order()