from product import Product, Order, Store

if __name__ == '__main__':\

    product1 = Product("Ноутбук", 1000, 5)
    product2 = Product("Смартфон", 500, 10)
    order1 = Order()
    # order1.add_product(product1, 3)
    # order1.add_product(product1, 4)
    # sum = order1.calculate_total()
    # print(sum)
    store1 = Store()
    store1.add_product(product1)
    store1.add_product(product2)
    store1.list_products()

