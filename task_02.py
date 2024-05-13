class ShoppingChart:
    all_goods = {}

    def __init__(self):
        self.__current = []

    @property
    def current(self):
        return '\n'.join(self.__current)

    @current.setter
    def current(self, new):
        if new[0:3] == 'del':
            if new[3:] in ShoppingChart.all_goods:
                self.__current.remove(new[3:])
        else:
            if new in ShoppingChart.all_goods:
                self.__current.append(new)

    @classmethod
    def add_goods_info(cls, file):
        with open(file, 'r', encoding='utf8') as f:
            for line in f:
                name, code = line.strip().split(';')
                result = Product(name, code)
                cls.all_goods[result.__repr__()[0]] = result.__repr__()[1:]

    def add_product(self, product):
        self.current = product

    def delete_product(self, product):
        self.current = ('del' + product)


class Product:
    def __init__(self, name, code):
        self.__name = name
        self.__code = code
        self.country = 'russia'

    @property
    def name(self):
        return self.__name

    @property
    def code(self):
        return self.__code

    def __repr__(self):
        return [self.__name, self.__code, self.country]


class Menu:
    @staticmethod
    def menu():
        greeting = f'Добро пожаловать в наш интернет-магазин!\n'
        chart = ShoppingChart()
        intro = (f'\n'
                 f'Для загрузки данных о товарах - введите 1\n'
                 f'Для добавления товара в вашу корзину - введите 2\n'
                 f'Для удаления товара из корзины - введите 3\n'
                 f'Для просмотра содержания корзины - введите 4\n'
                 f'Чтобы покинуть интернет-магазин - введите end\n')

        print(greeting, intro)
        inquiry = input()

        while inquiry != 'end':
            if inquiry == '1':
                print('Введите путь к файлу с товарами для загрузки')
                file_path = input()
                chart.add_goods_info(file_path)

                print(intro)
                inquiry = input()

            elif inquiry == '2':
                print('Введите название продукта, который нужно добавить в корзину')
                product = input()
                chart.add_product(product)

                print(intro)
                inquiry = input()

            elif inquiry == '3':
                print('Введите название продукта, который нужно удалить из корзину')
                product = input()
                chart.delete_product(product)

                print(intro)
                inquiry = input()

            elif inquiry == '4':
                print(chart.current)

                print(intro)
                inquiry = input()

            else:
                print('Введено неккоректное значение. Попробуйте снова')
                print(intro)
                inquiry = input()


Menu.menu()
