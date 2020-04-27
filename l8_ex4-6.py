'''Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.'''


class StoreMashines:

    def __init__(self, name, price, quantity, numb, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = numb
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.quantity,
                        'Листов в минуту': self.numb}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity}'

    def reception(self):
        chose = 'y'
        while chose == 'y' or chose == 'Y':
            try:
                staff = input(f'Введите наименование ')
                price = int(input(f'Введите цену за ед '))
                quont = int(input(f'Введите количество '))
                q_l = int(input(f'Введите количество '))
                unique = {'Модель устройства': staff, 'Цена за ед': price, 'Количество': quont, 'Листов в минуту': q_l}
                self.my_store.append(unique)
                print(f'Текущий список -\n {self.my_store}')
            except:
                print(f'Ошибка ввода данных')
                chose = input(f'Попробовать еще раз? Y/N ')
                if chose == 'Y' or chose == 'y':
                    print(f'Попробуйте снова')
                elif chose == 'N' or chose == 'n':
                    print('Вы вышли')
                    break
                else:
                    print(f"Введены не Y или N.")

        print(f'Для выхода из заполнения нажмите - Q, продолжение - любой иной символ и Enter')
        q = input(f'->>->> ')
        if q == 'Q' or q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'Весь склад -\n {self.my_store_full}')
            return f'Выход'
        else:
            return StoreMashines.reception(self)


class Printer(StoreMashines):
    def to_print(self):
        return f'Печатает {self.numb} листов в минуту'


class Scanner(StoreMashines):
    def to_scan(self):
        return f'Сканирует {self.numb} листов в минуту'


class Copier(StoreMashines):
    def to_copier(self):
        return f'Копирует {self.numb} листов в минуту'


staff_1 = Printer('Canon', 12000, 3, 15)
print(f'Заполняем принтеры')
print(staff_1.reception())
print(staff_1)
print(staff_1.to_print())
print(f'\nЗаполняем сканеры')
staff_2 = Scanner('HP', 15000, 2, 8)
print(staff_2.reception())
print(staff_2)
print(staff_2.to_scan())
print(f'\nЗаполняем Копиры')
staff_3 = Copier('Xerox', 8000, 5, 30)
print(staff_3.reception())
print(staff_3)
print(staff_3.to_copier())
