'''3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).'''


class Worker:

    def __init__(self, name, surname, position, salary, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"salary": salary, "bonus": bonus}


class Position(Worker):

    def __init__(self, name, surname, position, salary, bonus):
        super().__init__(name, surname, position, salary, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        #Расчитывал годовой доход
        #Бонус - коэфициент заслуг сотррудника от его оклада. т.е. полная получка = оклад за год + премия =  оклад за год * коэфициент
        full_year_income  = int(self._income.get("salary") * 12 + (self._income.get("salary") * self._income.get("bonus") * 12))
        return full_year_income


a = Position('Rumar', 'Gatekeeper', 'Waiter', 16000, 1.5)
print(f'{a.get_full_name()}\n{a.position}\n{a.get_total_income()}')
