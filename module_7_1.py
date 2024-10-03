class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        products = file.read()
        file.close()
        return products

    def add(self, *products):
        our_products = self.get_products()
        our_products_list = our_products.split('\n')

        file = open(self.__file_name, 'a')

        for i in products:
            product_str = str(i)
            if product_str not in our_products_list:
                file.write(product_str + '\n')
                our_products_list.append(product_str)
                print(f'Продукт {product_str} добавлен в магазин')
            else:
                print(f'Продукт {product_str} уже есть в магазине')

        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
p4 = Product('Apple', 0.2, 'phone')

print(p2)
s1.add(p1, p2, p3)
print(s1.get_products())
s1.add(p4)
print(s1.get_products())

"""
Файл products.txt изначально содержит:
Potato, 50.5, Vegetables
Spaghetti, 3.4, Groceries
Potato, 5.5, Vegetables

При выполнении s1.add(p4) в него записывается яблоко

P.S. Надеюсь, я правильно оформила пояснение
"""
