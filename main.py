from product import Product, Order, Store

if __name__ == '__main__':
    ''''Будем считать, что у каждого продукта есть склад, продукт может быть
     доступен в нескольких магазинах, но его кол-во везде будет одинаковым'''

    product1 = Product("Ноутбук", 1000, 5)
    product2 = Product("Смартфон", 500, 10)

    store1 = Store()
    store1.add_product(product1)
    store1.add_product(product2)
    store1.list_products()

    ''''Будем считать, что мы добавляем в заказ товары, но
     они не удаляются со склада пока не "оплатишь"'''
    order1 = Order()
    order1.add_product(product1, 6)
    order1.add_product(product2, 4)
    total = order1.calculate_total()
    print(f"Общая стоимость заказа {total}")

    order1.remove_product(product1, 5)
    total = order1.calculate_total()
    print(f"Общая стоимость заказа {total}")

    '''' Будем считаем, что заказ "оплатили" -> товары списались со клада;
         где-то в другом месте поменялся статус заказа;
         после оплаты можно применять метод return_product'''
    order1.pay()
    store1.list_products()

    order1.return_product(product2, 3)
    total = order1.calculate_total()
    print(f"Общая стоимость заказа {total}")
    store1.list_products()




