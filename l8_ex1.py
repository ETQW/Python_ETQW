'''1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.'''


class Data:
    def __init__(self, dd_mm_yyyy):
        self.dd_mm_yyyy = str(dd_mm_yyyy)

    @classmethod
    def extract(cls, dd_mm_yyyy):
        date = []
        for i in dd_mm_yyyy.split():
            if i != '-':
                date.append(i)
        return int(date[0]), int(date[1]), int(date[2])

    @staticmethod
    def valid(dd, mm, yyyy):
        if 1 <= dd <= 31:
            if 1 <= mm <= 12:
                if 2020 >= yyyy >= 0:
                    return f'Дата корректна {dd}-{mm}-{yyyy}'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'

        def __str__(self):
            return f'Текущая дата {Data.extract(self.day_month_year)}'


today = Data('20 - 05 - 2020')
print(today.dd_mm_yyyy)
print(Data.valid(38, 25, 2096))
print(today.valid(20, 5, 2020))
print(Data.valid(1, 11, 2000))
print(Data.extract('15 - 10 - 2009'))
print(today.extract('27 - 04 - 2020'))
