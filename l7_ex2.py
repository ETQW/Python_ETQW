'''2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.'''


class Atelye:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def consum_c(self):
        return (self.width / 6.5 + 0.5)

    def consum_j(self):
        return (self.height * 2 + 0.3)

    @property
    def full_cons(self):
        return str(f'Всего затрачено ткани {(self.width / 6.5 + 0.5) + (self.height * 2 + 0.3)} М^3')


class Coat(Atelye):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_c = round(self.width / 6.5 + 0.5)

    def __str__(self):
        return f'Площадь пальто {self.square_c}'


class Jacket(Atelye):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_j = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Площадь костюма {self.square_j}'


Palto = Coat(1, 3)
Kostum = Jacket(2, 6)
print(f'{Palto}, {Kostum}')
print(f'Потреблено на пальто - {Kostum.consum_c()} М^3, потреблено на костюм {Kostum.consum_j()} М^3')
print(Kostum.full_cons)
